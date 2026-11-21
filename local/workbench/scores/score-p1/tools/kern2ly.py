#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""kern（钢琴双谱表）→ LilyPond 骨架。仅用于把底本音符按小节搬进 .ly，之后人工复核。

用法： python kern2ly.py <file.krn> <start> <end> [--tempo "..."] [--key "d \\major"]

octave 映射（kern 标准，c = C4）：c→c'（C4）、cc→c''（C5）、C→c（C3）、CC→c,（C2）
"""
import re
import sys

BASED = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
LY_OCT = {1: ",,", 2: ",", 3: "", 4: "'", 5: "''", 6: "'''", 7: "''''"}
DUR = {1: "1", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64"}


def parse(tok):
    t = tok
    if t in (".", ""):
        return ("null", None)
    if t[0] in "rR":
        m = re.match(r"[rR]+([0-9]*)", t)
        return ("rest", int(m.group(1)) if m.group(1) else None)
    m = re.match(r"^([0-9]*)([a-gA-G]+)([#\-n]*)([0-9]*)(.*)$", t)
    if not m:
        return ("other", t)
    dur_lead, letters, acc, dur_trail, tail = m.groups()
    n = len(letters)
    case = n if letters[0].islower() else -n
    octv = {1: 4, 2: 5, 3: 6, -1: 3, -2: 2, -3: 1}.get(case, 4)
    dur = int(dur_lead) if dur_lead else (int(dur_trail) if dur_trail else None)
    return ("note", {"letter": letters[0].lower(), "oct": octv, "acc": acc,
                     "dur": dur, "tail": tail, "raw": t})


def ly_pitch(info):
    name = info["letter"]
    acc = ""
    if "s" in info["acc"] or "#" in info["acc"]:
        acc = "s"
    elif "f" in info["acc"] or "-" in info["acc"]:
        acc = "f"
    return name + acc + LY_OCT.get(info["oct"], "")


def conv_note(info):
    d = DUR.get(info["dur"], "")
    if d == "":
        return None
    p = ly_pitch(info)
    tail = info["tail"]
    out = p + d
    if "[" in tail:
        out += "~"
    if "(" in tail:
        out += "("
    if ")" in tail:
        out = out.replace("(", "") + ")"
    return out


def main():
    path, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    measures = []
    cur = None
    for ln in lines:
        if ln.startswith("="):
            m = re.match(r"=+([0-9]+)", ln)
            cur = {"num": int(m.group(1)) if m else None, "L": [], "R": []}
            measures.append(cur)
            continue
        if cur is None or not ln.strip() or ln.startswith("*") or ln.startswith("!"):
            continue
        f = ln.split("\t")
        for idx, key in ((0, "L"), (1, "R")):
            if idx < len(f):
                cur[key].append(f[idx])
    for m in measures:
        if m["num"] is None or not (start <= m["num"] <= end):
            continue
        print("%% m.%d" % m["num"])
        for key in ("L", "R"):
            toks = []
            for slice_ in m[key]:
                items = [parse(t) for t in slice_.split()]
                notes = [(k, v) for k, v in items if k == "note"]
                rests = [(k, v) for k, v in items if k == "rest"]
                if notes:
                    if len(notes) == 1:
                        s = conv_note(notes[0][1])
                        if s:
                            toks.append(s)
                    else:
                        d = DUR.get(notes[0][1]["dur"], "")
                        body = " ".join(ly_pitch(v) for _, v in notes)
                        tail = ""
                        if any("[" in v["tail"] for _, v in notes):
                            tail = "~"
                        toks.append("<%s>%s%s" % (body, d, tail))
                elif rests:
                    d = DUR.get(rests[0][1], "")
                    if d:
                        toks.append("r" + d)
            print("%s = { %s }" % ("upper" if key == "R" else "lower", " ".join(toks)))
    print("%% END")


if __name__ == "__main__":
    main()
