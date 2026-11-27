#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""md2ly (score-r6)：把 md2parse 读出的分谱片段写成 LilyPond 音符串（绝对音高 + 显式时值）。

要点：
- MuseData 八度记法 C4 = 中央 C；LilyPond 绝对音高 c' = 中央 C，故撇号数 = octave - 3。
- 前缀 g 的音符是装饰音：本工具直接跳过（与 ABC 底本处理一致，谱例不展开装饰音）。
- 三连音：MuseData 里连续 3 个等长、且单独写不进普通时值的音（如 divisions=12 时 dur=2），
  按 \\tuplet 3/2 包裹，内部写成它的记谱时值。
- 降号：这批 md2 用 **f 后缀** 写降号（如 `Ef6`，属性列另标 `f`），也用 `-` 与 `n`；三者都认。
- 连音线：dur 后缀 '-' 或标记 '_' 且与下一个音同高时加 '~'。
"""
import re
from fractions import Fraction

LETTER_SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
PITCH_RE = re.compile(r"^g?([A-Ga-g])([#fn-]?)(-?\d+)$")


def split_tok(tok):
    m = re.match(r"^(g?)([A-Ga-g])([#fn-]?)(-?\d+)$", tok)
    if not m:
        return None
    return {"grace": m.group(1) == "g", "letter": m.group(2).upper(),
            "acc": m.group(3), "oct": int(m.group(4))}


def ly_pitch(info):
    name = info["letter"].lower()
    if info["acc"] == "#":
        name += "s"
    elif info["acc"] in ("f", "-"):
        name += "f"
    marks = info["oct"] - 3          # c' = C4
    if marks > 0:
        name += "'" * marks
    elif marks < 0:
        name += "," * (-marks)
    return name


def dur_to_ly(frac):
    for dots in range(4):
        factor = sum(Fraction(1, 2 ** i) for i in range(dots + 1))
        for denom in (1, 2, 4, 8, 16, 32, 64, 128, 256):
            if frac == Fraction(1, denom) * factor:
                return str(denom) + "." * dots
    return None


def part_to_ly(part, first, last):
    div = part["divisions"]
    out = []
    for meas in part["measures"]:
        if meas["num"] < first or meas["num"] > last:
            continue
        notes = []
        for n in meas["notes"]:
            info = split_tok(n["tok"]) if n.get("tok") else None
            if n.get("tok") and info is None:
                # 硬保护：音高记号认不出就报错，绝不静默当休止（曾因不认 f 降号漏过音）
                raise ValueError("无法解析的音高记号 %r（m.%d）" % (n["tok"], meas["num"]))
            if info and info["grace"]:
                continue
            frac = Fraction(n["dur"], div * 4) if n["dur"] else Fraction(0)
            if n["pitch"] is None:
                notes.append({"rest": True, "frac": frac})
            else:
                notes.append({"rest": False, "frac": frac, "ly": ly_pitch(info),
                              "tok": n["tok"], "tail": n.get("tail", ""),
                              "pitch": n["pitch"]})
        evs = []
        i = 0
        while i < len(notes):
            n = notes[i]
            if n["rest"]:
                if n["frac"]:
                    dly = dur_to_ly(n["frac"])
                    evs.append(("r" if dly else "") + (dly or ""))
                i += 1
                continue
            dly = dur_to_ly(n["frac"])
            if dly is None:
                # 可能是三连音：收集同长的连续音
                j = i
                while (j < len(notes) and not notes[j]["rest"]
                       and notes[j]["frac"] == n["frac"]):
                    j += 1
                run = notes[i:j]
                total = n["frac"] * len(run)
                inner = None
                if len(run) == 3:
                    cand = n["frac"] * Fraction(3, 2)
                    inner = dur_to_ly(cand)
                    ratio = "3/2"
                elif len(run) == 6:
                    cand = n["frac"] * Fraction(3, 2)
                    inner = dur_to_ly(cand)
                    ratio = "3/2"
                if inner is None or dur_to_ly(total) is None:
                    raise ValueError("无法表示的时值 %s（%s）" % (n["frac"], n["tok"]))
                grp = []
                for k in run:
                    ev = k["ly"] + inner
                    if "-" in k["tail"]:
                        ev += "~"
                    grp.append(ev)
                evs.append("\\tuplet %s { %s }" % (ratio, " ".join(grp)))
                i = j
                continue
            ev = n["ly"] + dly
            nxt = notes[i + 1] if i + 1 < len(notes) else None
            if ("-" in n["tail"]) and nxt and not nxt["rest"] and nxt["pitch"] == n["pitch"]:
                ev += "~"
            evs.append(ev)
            i += 1
        out.append(" ".join(e for e in evs if e) + " |")
    return out
