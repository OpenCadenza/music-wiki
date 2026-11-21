#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把一份 Mutopia 风格的分谱 .ly 逐小节展开，报告每一小节各声部是否发声。

用途：核对 Op.92 第二乐章"木管铜管是否沉默"这类定性断言时，先确定
每个乐器的首次进入小节。做法是按 2/4 拍把 token 累加为拍数（\time 可覆盖），
累加到整小节时切成一条记录。

只做正常记号（音符、和弦、休止、tie、slur、力度、<< >> 叠加、\times、\repeat unfold）；
遇到无法解析的记号就报错退出，不猜。
"""
import re
import sys
import os

PITCH = r"[a-g](?:i{1,2}s|e{1,2}s|ff|ss|[fst])?[!?]?[',]*[!?]?"

TOKEN_RE = re.compile(r"""(
    <<                          # 叠加声部开始
  | >>                          # 叠加声部结束
  | \\\\                        # 换声部
  | "[^"]*"                     # 字符串（\bar "||" 等）
  | <[^<>]*>\ *[0-9.]*          # chord <c e>4.
  | \\[A-Za-z]+\ *[0-9./]*      # \command
  | \\[^A-Za-z\s]               # \! \> \( \) \\ 等
  | R\ *[0-9.]*                 # 休止（multi-measure / rest measure）
  | r\ *[0-9.]*                 # 休止
  | """ + PITCH + r"""\ *[0-9.]*   # 音符（含荷兰语/英语变化音后缀）
  | [{}<>\[\]()!?]
  | [|.~^_+-]
  | \s+
)""", re.X)


class Cursor:
    def __init__(self, text, beats_per_bar):
        self.s = text
        self.i = 0
        self.beats = 0.0
        self.beats_per_bar = beats_per_bar
        self.measures = []  # list of (beats_in_measure, has_sound)
        self.stack = []     # 叠加声部：记录 << 内每声部起始拍数
        self.tuplet = []    # 连音比率栈

    def scale(self):
        r = 1.0
        for x in self.tuplet:
            r *= x
        return r

    def add(self, dur, sounds):
        dur *= self.scale()
        self.beats += dur
        # 记录当前小节
        while len(self.measures) * self.beats_per_bar < self.beats - 1e-9:
            self.measures.append([0.0, False])
        m = int((self.beats - 1e-9) // self.beats_per_bar)
        if m >= len(self.measures):
            self.measures.append([0.0, False])
        self.measures[m][0] += dur
        if sounds:
            self.measures[m][1] = True


def parse_len(text):
    """把 '4.' '8..' '16' '2' '' 解析为拍数（四分音符=1拍）。"""
    if not text:
        return 1.0
    m = re.match(r"^([0-9]+)(\.*)$", text)
    if not m:
        raise ValueError("bad duration %r" % text)
    base = 4.0 / int(m.group(1))
    dots = m.group(2)
    mult = 1.0
    add = 0.5
    for _ in dots:
        mult += add
        add /= 2
    return base * mult


def run(path, beats=2.0, limit_measures=None):
    text = open(path, encoding="utf-8").read()
    # 去掉行注释
    text = re.sub(r"%[^\n]*", "", text)
    cur = Cursor(text, beats)
    # 找 \time
    mt = re.search(r"\\time\s+([0-9]+)/([0-9]+)", text)
    if mt:
        beats = float(mt.group(1)) / float(mt.group(2)) * 4.0
        cur.beats_per_bar = beats
    # 只从 \time 之后开始解析（前面是 \set/\clef/\key 等声明）
    if mt:
        cur.i = mt.end()
    pending_dur = None
    while cur.i < len(text):
        mx = TOKEN_RE.match(text, cur.i)
        if not mx:
            raise ValueError("unparsed at %r ... %r" % (path, text[cur.i:cur.i + 40]))
        tok = mx.group(1)
        cur.i = mx.end()
        t = tok.strip()
        if not t:
            continue
        if t.startswith("%"):
            continue
        if t == "<<":
            # 叠加：先保存外层拍数，解析各声部后取最长
            start = cur.beats
            cur.stack.append((start, len(cur.measures), [m[:] for m in cur.measures]))
            continue
        if t == ">>":
            start, nmeas, saved = cur.stack.pop()
            cur.beats = start
            cur.measures = saved
            continue
        if t == "\\\\":
            # 换声部：拍数回到叠加起点
            start, nmeas, saved = cur.stack[-1]
            # 保留已记录的发声信息
            merged = []
            for k in range(max(len(saved), len(cur.measures))):
                a = saved[k] if k < len(saved) else [0.0, False]
                b = cur.measures[k] if k < len(cur.measures) else [0.0, False]
                merged.append([max(a[0], b[0]), a[1] or b[1]])
            cur.stack[-1] = (start, nmeas, merged)
            cur.beats = start
            cur.measures = [m[:] for m in merged]
            continue
        if t.startswith("\\times"):
            m = re.match(r"\\times\s+([0-9]+)/([0-9]+)", t)
            num, den = int(m.group(1)), int(m.group(2))
            cur.tuplet.append(num / den)  # \times 2/3 → 每个时值 × 2/3
            continue
        if t.startswith("\\"):
            cmd = t.split()[0] if " " in t else t
            if cmd == "\\repeat":
                continue
            if cmd == "\\clef":
                # 吃掉下一个记号（clef 名）
                mx2 = TOKEN_RE.match(text, cur.i)
                if mx2:
                    cur.i = mx2.end()
                continue
            if cmd in ("\\markup", "\\set", "\\override", "\\revert", "\\once",
                       "\\setStaff", "\\layout", "\\midi", "\\header",
                       "\\tupletUp", "\\tupletDown"):
                # 若同行的下一个非空白字符是 {，跳整个平衡块；否则跳到行尾
                j = cur.i
                while j < len(text) and text[j] in " \t":
                    j += 1
                if j < len(text) and text[j] == "{":
                    depth = 0
                    while j < len(text):
                        if text[j] == "{":
                            depth += 1
                        elif text[j] == "}":
                            depth -= 1
                            if depth == 0:
                                j += 1
                                break
                        j += 1
                    cur.i = j
                else:
                    nl = text.find("\n", cur.i)
                    cur.i = len(text) if nl < 0 else nl
                continue
            if cmd == "\\key":
                # \key a \major  → 吃掉调名与调式
                for _ in range(2):
                    while cur.i < len(text) and text[cur.i] in " \n\t":
                        cur.i += 1
                    mx2 = TOKEN_RE.match(text, cur.i)
                    if mx2:
                        cur.i = mx2.end()
                continue
            if cmd == "\\grace" or cmd == "\\acciaccatura" or cmd == "\\appoggiatura":
                # 吃掉后面的 { ... }
                while cur.i < len(text) and text[cur.i] in " \n\t":
                    cur.i += 1
                if cur.i < len(text) and text[cur.i] == "{":
                    depth = 0
                    while cur.i < len(text):
                        if text[cur.i] == "{":
                            depth += 1
                        elif text[cur.i] == "}":
                            depth -= 1
                            if depth == 0:
                                cur.i += 1
                                break
                        cur.i += 1
                continue
            # \times 的结束：靠 } 处理（下面统一处理括号）
            continue
        if t == "{":
            # \times { 或 voice 组；记录是否需要还原
            continue
        if t == "}":
            if cur.tuplet:
                cur.tuplet.pop()
            continue
        if t == "[" or t == "]" or t == "|" or t == "~" or t == ".":
            continue
        if t in ("^", "_", "-", "+", "(", ")", "!"):
            continue
        if t.startswith('"'):
            continue
        if t.startswith("<"):
            m = re.match(r"<.*>\s*([0-9.]*)", t)
            dur = parse_len(m.group(1))
            cur.add(dur, True)
            continue
        if t.startswith("R"):
            m = re.match(r"R\s*([0-9.]*)", t)
            dur = parse_len(m.group(1))
            cur.add(dur, False)
            continue
        if t.startswith("r"):
            m = re.match(r"r\s*([0-9.]*)", t)
            dur = parse_len(m.group(1))
            cur.add(dur, False)
            continue
        # 音符
        m = re.match("(" + PITCH + r")\s*([0-9.]*)", t)
        dur = parse_len(m.group(2))
        cur.add(dur, True)
    return cur


def main():
    d = sys.argv[1]
    bpb = 2.0
    parts = ["flauti", "oboi", "clarinetti", "fagotti", "corni", "trombe", "timpani",
             "violinoone", "violinotwo", "viola", "violoncello", "basso"]
    data = {}
    for p in parts:
        path = os.path.join(d, p + ".ly")
        cur = run(path, bpb)
        data[p] = cur.measures
        tot = sum(m[0] for m in cur.measures)
        print("%-14s measures=%d beats=%.1f (≈%.1f bars)" % (
            p, len(cur.measures), tot, tot / bpb))
    print()
    print("发声区间（bar 级，S=有音）：")
    for p in parts:
        runs = []
        start = None
        for k, m in enumerate(data[p]):
            if m[1] and start is None:
                start = k + 1
            elif not m[1] and start is not None:
                runs.append((start, k))
                start = None
        if start is not None:
            runs.append((start, len(data[p])))
        txt = ", ".join(("%d" % a) if a == b else ("%d-%d" % (a, b)) for a, b in runs)
        print("  %-14s %s" % (p, txt))
    print()
    hdr = "bar  " + " ".join("%-4s" % p[:4] for p in parts)
    print(hdr)
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 60
    for k in range(min(n, max(len(v) for v in data.values()))):
        row = "%3d  " % (k + 1)
        for p in parts:
            m = data[p][k] if k < len(data[p]) else [0, False]
            row += "%-4s " % ("S" if m[1] else ".")
        print(row)


if __name__ == "__main__":
    main()
