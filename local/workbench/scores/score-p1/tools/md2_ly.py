#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MuseData Stage-2 (.md2) → LilyPond token 抽取（CCARH Op.125 语料专用，够用即止）。

要点：
  * 每个 part 有自己的 `$  K:.. Q:.. T:.. C:..` 行，**Q 不一定相同**（弦乐 Q:24，圆号/小号/定音鼓 Q:8）
  * `measure N` 之后的记录属第 N 小节；文件开头到第一个 `measure` 之间的记录属第 1 小节
  * 音符行：第 1 段音高（如 `E4` / `C#4` / `B-3`），第 2 段 divisions（尾随 `-` 表示连音），
    第 3 段 voice 号；**行首有一个空格 = 同一 staff 的第 2 声部**（MuseData 用缩进区分声部）
  * `rest <divs> <voice>`；`back <divs>` = 该小节内另起声部
  * divisions → 时值：以 Q 为四分音符，48/Q=2 拍/小节等按 T 计算

用法：python md2_ly.py <file.md2> <part_no> <start> <end>
"""
import re
import sys

PITCH_RE = re.compile(r"^([A-G])([#\-n]?)(\d)$")

# divisions 相对 Q:24 的时值名（Q 不是 24 时按比例换算后再查）
def dur_name(divs, q):
    """把 divisions 换算成以四分音符为 1 的拍数，给出 LilyPond 时值字符串。"""
    beats = divs / float(q)            # 四分音符数
    table = [
        (4.0, "1"), (3.0, "2."), (2.0, "2"), (1.5, "4."), (1.0, "4"),
        (0.75, "8."), (0.5, "8"), (0.375, "16."), (0.25, "16"),
        (1.0 / 6, "T16"), (1.0 / 12, "T32"), (0.125, "32"), (0.0625, "64"),
    ]
    for val, name in table:
        if abs(beats - val) < 1e-6:
            return name
    return "?%d" % divs   # 不认识就报出来


LY_OCT = {0: ",,,", 1: ",,", 2: ",", 3: "", 4: "'", 5: "''", 6: "'''", 7: "''''", 8: "'''''"}


def ly_pitch(p):
    m = PITCH_RE.match(p)
    if not m:
        return None
    letter, acc, octv = m.group(1).lower(), m.group(2), int(m.group(3))
    a = "s" if acc == "#" else ("f" if acc == "-" else "")
    # MuseData：中央 C = C4 → LilyPond c'
    return letter + a + LY_OCT.get(octv, "")


def split_parts(lines):
    idx = []
    for i, ln in enumerate(lines):
        if ln.startswith("score: part"):
            no = int(re.match(r"score: part (\d+)", ln).group(1))
            name = ""
            for j in range(i - 1, max(0, i - 6), -1):
                if lines[j].startswith("First Movement"):
                    name = lines[j + 1].strip()
                    break
            idx.append((no, name, i))
    out = {}
    for k, (no, name, start) in enumerate(idx):
        end = idx[k + 1][2] - 8 if k + 1 < len(idx) else len(lines)
        out[no] = (name, lines[start:end])
    return out


def parse_part(body):
    q = 24
    for ln in body:
        m = re.match(r"^\$\s+.*Q:(\d+)", ln)
        if m:
            q = int(m.group(1))
            break
    ts = "2/4"
    for ln in body:
        m = re.search(r"T:(\d+/\d+)", ln)
        if m:
            ts = m.group(1)
            break
    measures = {}
    cur = 1
    voice = 1
    measures.setdefault(1, {})
    for ln in body:
        if ln.startswith("measure "):
            m = re.match(r"measure (\d+)", ln)
            cur = int(m.group(1))
            voice = 1
            measures.setdefault(cur, {})
            continue
        if ln.startswith("back"):
            voice += 1
            continue
        stripped = ln.strip()
        if not stripped:
            continue
        if stripped.startswith("rest"):
            m = re.match(r"rest\s+(\d+)", stripped)
            if m:
                measures[cur].setdefault(voice, []).append(("rest", None, int(m.group(1)), False))
            continue
        if stripped[0] not in "ABCDEFG":
            continue
        f = stripped.split()
        if len(f) < 3:
            continue
        pitch, durf = f[0], f[1]
        try:
            divs = int(durf.rstrip("-"))
        except ValueError:
            continue
        indented = ln.startswith(" ") or ln.startswith("\t")
        v = 2 if indented else 1
        if voice > 1 and not indented:
            v = voice
        tie = durf.endswith("-")
        measures[cur].setdefault(v, []).append(("note", pitch, divs, tie))
    return q, ts, measures


def main():
    path, part = sys.argv[1], int(sys.argv[2])
    lo = int(sys.argv[3]); hi = int(sys.argv[4])
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    parts = split_parts(lines)
    name, body = parts[part]
    q, ts, meas = parse_part(body)
    print("# part %d: %s  (Q:%d, T:%s)" % (part, name, q, ts))
    for mm in range(lo, hi + 1):
        voices = meas.get(mm, {})
        if not voices:
            print("== m.%d == (空)" % mm)
            continue
        print("== m.%d ==" % mm)
        for v in sorted(voices):
            items = []
            for kind, pitch, divs, tie in voices[v]:
                dn = dur_name(divs, q)
                if kind == "rest":
                    items.append("r" + dn.replace("T16", "16").replace("T32", "32"))
                else:
                    items.append("%s%s%s" % (ly_pitch(pitch), dn, "~" if tie else ""))
            print("  v%d: %s" % (v, " ".join(items)))


if __name__ == "__main__":
    main()
