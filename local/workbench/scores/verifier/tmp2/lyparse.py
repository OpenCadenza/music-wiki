"""把 LilyPond 规范文本（\\displayLilyMusic 输出）解析成事件表。

输出事件: (全局起点/四分拍, 时值/四分拍, midi)
并记录小节线时间、\\partial、装饰音，用于 barcheck 复核。
"""
import re
from pathlib import Path

SEMI = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
ACC = {"": 0, "f": -1, "ff": -2, "s": 1, "ss": 2, "is": 1, "es": -1}
NOTE_RE = re.compile(r"^([a-g])(ff|ss|f|s)?((?:'+|,+)*)(\d*)(\.*)")
DUR = {1: 4.0, 2: 2.0, 4: 1.0, 8: 0.5, 16: 0.25, 32: 0.125, 64: 0.0625, 128: 0.03125}
NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def nm(p):
    return f"{NAMES[p % 12]}{p // 12 - 1}"


def midi_of(letter, acc, oct_marks):
    return 12 * (3 + oct_marks.count("'") - oct_marks.count(",") + 1) + SEMI[letter] + ACC[acc or ""]


def dur_value(num, dots):
    if not num:
        return None
    base = DUR[int(num)]
    val, add = base, base
    for _ in dots:
        add /= 2
        val += add
    return val


def strip_balanced(text, start):
    """从 text[start] 的花括号起，返回匹配结束后的下标（start 必须是 '{'）。"""
    depth = 0
    i = start
    while i < len(text):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise SystemExit("花括号不平衡")


def preprocess(text):
    # 1) \markup <平衡花括号 或 单 token>
    out = []
    i = 0
    while i < len(text):
        m = re.match(r"\\markup\s*", text[i:])
        if m:
            i += m.end()
            j = text.find("{", i)
            if j >= 0 and text[i:j].strip() == "":
                i = strip_balanced(text, j)
            else:
                m2 = re.match(r'"[^"]*"|\S+', text[i:])
                i += m2.end() if m2 else 0
            continue
        out.append(text[i])
        i += 1
    text = "".join(out)
    # 2) 结构性命令整体删除
    pats = [
        r"\\key\s+[a-g][sf]?\s+\\(?:major|minor)",
        r"\\clef\s+\"[^\"]*\"",
        r"\\clef\s+\\?\w+",
        r"\\time\s+\d+/\d+",
        r"\\tempo\s+\"[^\"]*\"\s*\d+\s*=\s*#?\d+",
        r"\\bar\s+\"[^\"]*\"",
        r"\\set\s+[\w.-]+\s*=\s*#?-?\d+",
        r"\\set\s+[\w.-]+\s*=\s*\\?\w+",
        r"\\override\s+[\w. ]+",
        r"\\once\s+",
        r"\\stemUp|\\stemDown|\\voiceOne|\\voiceTwo|\\oneVoice",
        r"\"[^\"]*\"",           # 残余字符串
        r"#[^\s{}]*",            # scheme 字面量
        r"\\[pfd]+\b",           # 力度
        r"=\s*",                 # 赋值号
    ]
    for p in pats:
        text = re.sub(p, " ", text)
    return text


def tokenize(text):
    toks = []
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        if ch in " \t\r\n":
            i += 1
            continue
        if text.startswith("<<", i):
            toks.append(("par_start", None)); i += 2; continue
        if text.startswith(">>", i):
            toks.append(("par_end", None)); i += 2; continue
        if text.startswith("\\\\", i):
            toks.append(("voice_sep", None)); i += 2; continue
        if ch == "{":
            toks.append(("brace_open", None)); i += 1; continue
        if ch == "}":
            toks.append(("brace_close", None)); i += 1; continue
        if ch == "\\":
            m = re.match(r"\\([A-Za-z][A-Za-z0-9-]*|.)", text[i:])
            word = m.group(1)
            i += m.end()
            if word == "partial":
                m2 = re.match(r"\s*(\d+)(\.*)", text[i:])
                toks.append(("partial", dur_value(m2.group(1), m2.group(2))))
                i += m2.end()
                continue
            if word in ("grace", "appoggiatura", "acciaccatura"):
                toks.append(("ornament", word))
                continue
            toks.append(("cmd", word))
            continue
        if ch == "<":
            toks.append(("chord_start", None)); i += 1; continue
        if ch == ">":
            m = re.match(r">(\d*)(\.*)", text[i:])
            dur = dur_value(m.group(1), m.group(2)) if m.group(1) else None
            toks.append(("chord_end", dur))
            i += m.end()
            continue
        if ch == "|":
            toks.append(("bar", None)); i += 1; continue
        if ch in "[]~-()!^_.":
            i += 1; continue
        if ch in "rsR":
            m = re.match(r"([rsR])(\d*)(\.*)", text[i:])
            dur = dur_value(m.group(2), m.group(3)) if m.group(2) else None
            kind = "spacer" if ch == "s" else "rest"
            toks.append((kind, dur))
            i += m.end()
            continue
        m = NOTE_RE.match(text[i:])
        if m:
            letter, acc, octs, dnum, dots = m.groups()
            toks.append(("note", (midi_of(letter, acc, octs), dur_value(dnum, dots))))
            i += m.end()
            continue
        raise SystemExit(f"无法解析的字符 {ch!r} @ {i}: {text[i:i+80]!r}")
    return toks


class Track:
    def __init__(self, name):
        self.name = name
        self.events = []      # (t, dur, midi)
        self.barlines = []    # t
        self.ornaments = []   # (t, [midi...])
        self.partial = 0.0


def parse(toks, t, track, dfault=None):
    i = 0
    n = len(toks)
    pending = dfault
    while i < n:
        kind, val = toks[i]
        if kind == "par_start":
            j = i + 1
            depth = 1
            groups, cur = [], []
            while j < n:
                k2, v2 = toks[j]
                if k2 == "par_start":
                    depth += 1
                elif k2 == "par_end":
                    depth -= 1
                    if depth == 0:
                        groups.append(cur)
                        break
                elif k2 == "voice_sep" and depth == 1:
                    groups.append(cur); cur = []
                    j += 1
                    continue
                cur.append(toks[j])
                j += 1
            ends = [parse(g, t, track, pending)[0] for g in groups]
            t = max(ends) if ends else t
            i = j + 1
            continue
        if kind == "bar":
            track.barlines.append(t)
            i += 1
            continue
        if kind == "brace_open":
            j = i + 1
            depth = 1
            inner = []
            while j < n:
                if toks[j][0] == "brace_open":
                    depth += 1
                elif toks[j][0] == "brace_close":
                    depth -= 1
                    if depth == 0:
                        break
                inner.append(toks[j])
                j += 1
            t, pending = parse(inner, t, track, pending)
            i = j + 1
            continue
        if kind == "brace_close":
            i += 1
            continue
        if kind == "partial":
            track.partial = val
            i += 1
            continue
        if kind == "cmd":
            i += 1
            continue
        if kind == "ornament":
            j = i + 1
            graces = []
            if j < n and toks[j][0] == "brace_open":
                j += 1
                depth = 1
                while j < n:
                    if toks[j][0] == "brace_open":
                        depth += 1
                    elif toks[j][0] == "brace_close":
                        depth -= 1
                        if depth == 0:
                            break
                    if toks[j][0] == "note":
                        graces.append(toks[j][1][0])
                    j += 1
                i = j + 1
            else:
                while j < n and toks[j][0] == "cmd":
                    j += 1
                if j < n and toks[j][0] == "note":
                    graces.append(toks[j][1][0])
                    j += 1
                i = j
            track.ornaments.append((t, graces))
            continue
        if kind == "chord_start":
            pitches, dur = [], None
            j = i + 1
            while j < n and toks[j][0] != "chord_end":
                if toks[j][0] == "note":
                    pitches.append(toks[j][1][0])
                    if toks[j][1][1]:
                        dur = toks[j][1][1]
                j += 1
            if j < n and toks[j][1]:
                dur = toks[j][1]
            if dur is None:
                dur = pending if pending else 1.0
            pending = dur
            for p in pitches:
                track.events.append((t, dur, p))
            t += dur
            i = j + 1
            continue
        if kind == "note":
            midi, dur = val
            if dur is None:
                dur = pending if pending else 1.0
            pending = dur
            track.events.append((t, dur, midi))
            t += dur
            i += 1
            continue
        if kind in ("rest", "spacer"):
            dur = val if val else (pending if pending else 1.0)
            pending = dur
            t += dur
            i += 1
            continue
        raise SystemExit(f"未处理 token {toks[i]}")
    return t, pending


def split_top_braces(txt):
    blocks = []
    i = 0
    n = len(txt)
    while i < n:
        j = txt.find("{", i)
        if j == -1:
            break
        k = strip_balanced(txt, j)
        blocks.append(txt[j + 1:k - 1])
        i = k
    return blocks


def load(path, names):
    txt = Path(path).read_text(encoding="utf-8").split("-----STDERR-----")[0]
    blocks = split_top_braces(txt)
    assert len(blocks) == len(names), f"{path}: 块数 {len(blocks)} != 变量数 {len(names)}"
    out = {}
    for name, blk in zip(names, blocks):
        tr = Track(name)
        parse(tokenize(preprocess(blk)), 0.0, tr)
        out[name] = tr
    return out


def by_measure(track, bar_len, partial):
    """按小节分组: 返回 {measure_index: [(onset_in_measure, dur, midi)]}"""
    out = {}
    for t, d, p in track.events:
        if t < partial - 1e-9:
            m = 0
        else:
            m = int((t - partial) / bar_len + 1e-9) + 1
        onset = t - (partial + (m - 1) * bar_len) if m > 0 else t
        out.setdefault(m, []).append((round(onset, 4), round(d, 4), p))
    for k in out:
        out[k].sort()
    return out


if __name__ == "__main__":
    import sys
    names = sys.argv[2:]
    for name, tr in load(sys.argv[1], names).items():
        print(f"=== {name}  partial={tr.partial}  barlines={['%.3f' % b for b in tr.barlines]}")
        for t, d, p in tr.events:
            print(f"  @{t:7.3f} +{d:6.3f} {nm(p)}({p})")
        if tr.ornaments:
            print("  装饰音:", [(round(t, 3), [nm(x) for x in g]) for t, g in tr.ornaments])
