"""ABC（hum2abc 输出）→ 事件表：按 [V:n] 与 & 子声部计算 onset。

用法: python src_abc.py <abc> <起行> <止行>
"""
import re
import sys
from pathlib import Path

SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def nm(p):
    return f"{NAMES[p % 12]}{p // 12 - 1}"


def parse_len(s, i, unit):
    m = re.match(r"(\d*)((?:/\d*)*)", s[i:])
    num, slashes = m.group(1), m.group(2)
    val = unit * (int(num) if num else 1)
    j = 0
    while j < len(slashes):
        j += 1
        k = j
        while k < len(slashes) and slashes[k].isdigit():
            k += 1
        if k > j:
            val /= int(slashes[j:k])
            j = k
        else:
            val /= 2
    return val, i + m.end()


def parse_acc(s, i):
    if s[i] == "=":
        return "=", i + 1
    c = s[i]
    j = i
    while j < len(s) and s[j] == c:
        j += 1
    return c * (j - i), j


def pitch(letter, acc, octs, key_alters, state=None):
    base = SEMI[letter.upper()]
    octave = 4 if letter.isupper() else 5      # ABC: C = 中央 C(C4), c = C5
    octave += octs.count("'") - octs.count(",")
    if acc == "":
        if state is not None and (letter, octave) in state:
            alter = state[(letter, octave)]
        else:
            alter = key_alters.get(letter.upper(), 0)
    elif acc == "=":
        alter = 0
        if state is not None:
            state[(letter, octave)] = 0
    else:
        alter = (1 if acc[0] == "^" else -1) * len(acc)
        if state is not None:
            state[(letter, octave)] = alter
    return 12 * (octave + 1) + base + alter


def parse_field(text, unit, key_alters, t0=0.0):
    """返回 [voice_events,...]（每个声部 [(onset, midi|None, dur)], 相对 t0），和首个声部总长。"""
    voices = [[]]
    t = t0
    state = {}
    i, n = 0, len(text)
    next_scale = 1.0
    while i < n:
        ch = text[i]
        if ch.isspace():
            i += 1
            continue
        if ch == "&":
            voices.append([])
            t = t0
            i += 1
            next_scale = 1.0
            continue
        if ch in "|: ]":
            i += 1
            continue
        if ch == "!":
            j = text.find("!", i + 1)
            i = (j + 1) if j != -1 else n
            continue
        if ch == "{":
            j = text.find("}", i)
            i = (j + 1) if j != -1 else n
            continue
        if ch == "[":
            j = text.find("]", i)
            if j == -1:
                raise SystemExit("未闭合的 [")
            inner = text[i + 1:j]
            if re.match(r"[IKMQdkLlNQ]:", inner):
                i = j + 1
                continue
            pitches, last_len = [], None
            m = 0
            while m < len(inner):
                if inner[m].isspace():
                    m += 1
                    continue
                acc = ""
                if inner[m] in "^_=":
                    acc, m = parse_acc(inner, m)
                letter = inner[m]
                m += 1
                octs = ""
                while m < len(inner) and inner[m] in "',":
                    octs += inner[m]
                    m += 1
                pitches.append(pitch(letter, acc, octs, key_alters, state))
                d, m2 = parse_len(inner, m, unit)
                if m2 > m:
                    last_len = d
                m = m2
            dur, i2 = parse_len(text, j + 1, unit)
            if i2 == j + 1 and last_len is not None:
                dur = last_len
            dur *= next_scale
            next_scale = 1.0
            for p in pitches:
                voices[-1].append((t, p, dur))
            t += dur
            i = i2
            continue
        if ch in "zxXZ":
            dur, i = parse_len(text, i + 1, unit)
            dur *= next_scale
            next_scale = 1.0
            voices[-1].append((t, None, dur))
            t += dur
            continue
        if ch == ">":
            while i < n and text[i] == ">":
                i += 1
            onset, p, old = voices[-1][-1]
            new = old * 1.5
            voices[-1][-1] = (onset, p, new)
            t += new - old
            next_scale = 0.5
            continue
        if ch == "<":
            while i < n and text[i] == "<":
                i += 1
            onset, p, old = voices[-1][-1]
            new = old / 1.5
            voices[-1][-1] = (onset, p, new)
            t -= old - new
            next_scale = 1.5
            continue
        if ch in ".-":
            if ch == ".":
                i += 1
                continue
            i += 1
            continue
        if ch == '"':
            j = text.find('"', i + 1)
            i = (j + 1) if j != -1 else n
            continue
        acc = ""
        if text[i] in "^_=":
            acc, i = parse_acc(text, i)
        letter = text[i]
        if not letter.isalpha():
            raise SystemExit(f"ABC 无法解析 {letter!r} @{i}: {text[i:i+40]!r}")
        i += 1
        octs = ""
        while i < n and text[i] in "',":
            octs += text[i]
            i += 1
        dur, i = parse_len(text, i, unit)
        dur *= next_scale
        next_scale = 1.0
        voices[-1].append((t, pitch(letter, acc, octs, key_alters, state), dur))
        t += dur
    return voices, t - t0


def main():
    path, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    lines = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()
    unit = 0.5          # L:1/8
    key_alters = {"B": -1}   # K:F
    seq = {}
    starts = {}
    for idx in range(a - 1, b):
        m = re.match(r"\s*\[V:(\d+)\]\s*(.*)$", lines[idx])
        if not m:
            continue
        v = int(m.group(1))
        seq.setdefault(v, []).append((idx + 1, m.group(2)))
    for v, items in seq.items():
        t = 0.0
        for lineno, text in items:
            voices, total = parse_field(text, unit, key_alters)
            starts.setdefault(v, []).append((lineno, t, voices))
            print(f"V{v} 行{lineno} 起点{t:g} 总长{total:g}")
            for vi, ev in enumerate(voices):
                for onset, midi, dur in ev:
                    label = nm(midi) if midi is not None else "rest"
                    print(f"    v{vi+1} @{t + onset:6.3f} +{dur:5.3f} {label}"
                          + (f"({midi})" if midi is not None else ""))
            t += total


if __name__ == "__main__":
    main()
