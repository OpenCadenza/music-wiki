#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 craigsapp 风格的 **kern 双谱表（piano）某小节区间，翻译成 LilyPond 可读的清单。

用法： python kern_dump.py <file.krn> <start_measure> <end_measure> [--ly]

输出：每小节一行块，左=**kern 第 1 谱表（staff2，通常左手），右=第 2 谱表。
--ly 时把音名/时值翻成 LilyPond 写法（english），便于人工核对后粘进 .ly。

只做翻译，不做排版判断：连音线/断奏/踏板记号原样以 < > ( ) [ ] _ 附注输出。
"""
import re
import sys

KERN_OCT = {}


def pos_of(letter, case):
    """返回 kern 字母+大小写对应的科学音高八度（middle C = C4 = kern 'c'）。"""
    base = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}[letter.lower()]
    # kern: 'c'=C4, 'cc'=C5, 'C'=C3, 'CC'=C2
    if case == 1:      # 单个小写
        octave = 4
    elif case == 2:    # 两个小写
        octave = 5
    elif case == 3:
        octave = 6
    elif case == -1:   # 单个大写
        octave = 3
    elif case == -2:
        octave = 2
    elif case == -3:
        octave = 1
    else:
        octave = 4
    return base, octave


ACC = {"#": "s", "-": "f", "n": ""}

DUR_NAMES = {1: "1", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64"}

LY_OCT = {1: ",,,", 2: ",,", 3: ",", 4: "", 5: "'", 6: "''", 7: "'''"}


def parse_token(tok):
    """返回 (kind, info) ；kind in note/rest/null/other"""
    t = tok
    if t in (".", ""):
        return ("null", None)
    # 去掉前导的重音/连音线等修饰记号
    m0 = re.match(r"^[\(\[\)\]]+(\S+)$", t)
    if m0:
        t = m0.group(1)
    # 时值前置的休止：8r / 16r / 4r.
    mr = re.match(r"^([0-9.]+)[rR]+$", t)
    if mr:
        d = mr.group(1).rstrip(".")
        return ("rest", {"dur": int(d) if d else None, "raw": tok})
    if t[0] in "rR":
        m = re.match(r"[rR]+([0-9]*)", t)
        return ("rest", {"dur": int(m.group(1)) if m.group(1) else None, "raw": tok})
    # 音高：可选前导时值 + 字母（可重复）+ 变化音 + 可选时值 + 修饰
    m = re.match(r"^([0-9]*)([a-gA-G]+)([#\-n]*)([0-9]*)(.*)$", t)
    if not m:
        return ("other", {"raw": t})
    dur_lead, letters, acc, dur_trail, tail = m.groups()
    letter = letters[0].lower()
    n = len(letters)
    case = n if letters[0].islower() else -n
    base, octave = pos_of(letter, case)
    dur = int(dur_lead) if dur_lead else (int(dur_trail) if dur_trail else None)
    # 修饰（连音线/倚音等）
    flags = []
    for ch in tail or "":
        if ch in "([)]_":
            flags.append(ch)
        elif ch == "L":
            flags.append("<")
        elif ch == "J":
            flags.append(">")
        elif ch == "q":
            flags.append("grace")
        elif ch in "zZ":
            flags.append("grace")
        elif ch == ";":
            flags.append("fermata")
        elif ch == "t":
            flags.append("trill")
        else:
            flags.append("?" + ch)
    return ("note", {"letter": letter, "base": base, "octave": octave,
                     "acc": acc, "dur": dur,
                     "flags": flags, "raw": t})


def ly_pitch(info):
    name = info["letter"]
    acc = ""
    for ch in info["acc"]:
        acc = ACC.get(ch, "")
    octv = LY_OCT.get(info["octave"], "")
    # LilyPond english: flats written as f-suffix (ef, bf), sharps s-suffix
    if acc == "f":
        return name + "f" + octv
    if acc == "s":
        return name + "s" + octv
    return name + octv


def main():
    path, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    as_ly = "--ly" in sys.argv
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    rows = []
    cur = None
    for ln in lines:
        if ln.startswith("="):
            m = re.match(r"=+([0-9]+)", ln)
            num = int(m.group(1)) if m else None
            cur = {"num": num, "slices": []}
            rows.append(cur)
            continue
        if cur is None:
            continue
        if ln.startswith("*") or ln.startswith("!"):
            continue
        if not ln.strip():
            continue
        fields = ln.split("\t")
        cur["slices"].append(fields)
    for r in rows:
        if r["num"] is None or not (start <= r["num"] <= end):
            continue
        print("== measure %d ==" % r["num"])
        for si in range(3):
            out = []
            for slice_ in r["slices"]:
                f = slice_[si] if si < len(slice_) else "."
                toks = []
                for tok in f.split():
                    kind, info = parse_token(tok)
                    if kind == "note":
                        if as_ly:
                            d = DUR_NAMES.get(info["dur"], "?" + str(info["dur"]))
                            fl = "".join(x for x in info["flags"] if x in "()_")
                            toks.append("%s%s%s" % (ly_pitch(info), d, ("[" + fl + "]") if fl else ""))
                        else:
                            toks.append(info["raw"])
                    elif kind == "rest":
                        toks.append(("R" + str(info["dur"])) if as_ly else info["raw"])
                    elif kind == "null":
                        toks.append(".")
                    else:
                        toks.append(info["raw"])
                out.append(" ".join(toks) if toks else ".")
            name = ["LH", "RH", "dyn"][si]
            print("  %-3s | %s" % (name, " | ".join(out)))
    return


if __name__ == "__main__":
    main()
