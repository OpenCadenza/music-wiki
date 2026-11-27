#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""md2parse (score-r6)：读 CCARH MuseData stage-2（.md2）单乐章多分谱文件。

只解析出谱所需的字段：分谱（part）、小节、音高、时值（以 $ Q: 的 divisions 为单位，
Q:12 表示四分音符=12）、以及连音线标记 [ ] _ [[。

**音高记法（务必注意）**：这一批 MuseData 的降号写作 **`f` 后缀**（`Ef6`=E♭6、`Bf5`=B♭5），
不是 `-`；升号写 `#`，还原写 `n`。K.467 第一乐章全文件有 1089 处 `f` 降号。
只按 `-` 读降号会把它们**静默当成休止**（`mozart-k467-i-mm9-28` 首版就漏了 mm.18–19 的 E♭6）。
另外：认不出的音高记号要直接报错（见 md2ly.part_to_ly 的硬保护），并配合「raw 行数 vs 解析实音数」
逐小节对账——只做同源 MIDI 比对抓不到这类丢音。

用法：
  python md2parse.py <file.md2> --parts Fl.,Ob_1_ --measures 1-8 [--dump]
"""
import argparse
import json
import re

LETTER_SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
PITCH_RE = re.compile(r"([A-Ga-g])([#fn-]?)(-?\d+)$")


def midi_of(tok):
    m = PITCH_RE.match(tok)
    if not m:
        return None
    letter, acc, octv = m.group(1).upper(), m.group(2), int(m.group(3))
    alter = 1 if acc == "#" else -1 if acc in ("f", "-") else 0
    return (octv + 1) * 12 + LETTER_SEMI[letter] + alter


def parse(path):
    lines = open(path, encoding="latin-1").read().splitlines()
    parts = []            # [{name, divisions, measures:[{num, notes:[...]}]}]
    cur = None
    measure = None
    pending_spines = 0
    divisions = 12
    started = False
    for raw in lines:
        line = raw.rstrip()
        if line.startswith("@filename"):
            cur = {"name": None, "measures": [], "divisions": 12, "spines": []}
            started = False
            parts.append(cur)
            measure = None
            continue
        if cur is None:
            continue
        if line.startswith("P ") or line.startswith("P  "):
            # 分谱名：形如 "P   C0:p100k16t3a1r1z31Fl."
            m = re.search(r"[a-z0-9]*?(?P<name>[A-Za-z][A-Za-z0-9_/()\-.]*?)\s*(?:/(?:C|G)[^ ]*)?\s*$", line)
            name = None
            mm = re.search(r"z\d+([A-Za-z][^\s]*)", line)
            if mm:
                name = mm.group(1)
            if name and cur["name"] is None:
                cur["name"] = name.rstrip(".")
            if name:
                cur["spines"].append(name)
            continue
        if line.startswith("$"):
            m = re.search(r"Q:(\d+)", line)
            if m:
                divisions = int(m.group(1))
                cur["divisions"] = divisions
            continue
        m = re.match(r"^measure\s+(\d+)", line)
        if m:
            measure = {"num": int(m.group(1)), "notes": []}
            cur["measures"].append(measure)
            continue
        if line.startswith("rest") or line.startswith("space") or re.match(r"^[gG]?[A-Ga-g][#fn-]?-?\d+\s+\d+", line):
            if measure is None and cur["spines"]:
                measure = {"num": 1, "notes": []}
                cur["measures"].append(measure)
        if line.startswith("rest") or line.startswith("space"):
            if measure is not None:
                mm = re.match(r"^(rest|space)\s+(\d+)", line)
                dur = int(mm.group(2)) if mm else 0
                measure["notes"].append({"pitch": None, "dur": dur,
                                         "tie": "", "grace": False})
            continue
        if line.startswith(("C0:", "C1:", "C2:", "C3:")) or line.startswith(("*", "&", "=")):
            continue
        if not line.strip():
            continue
        # 音符行：pitch duration ...
        mm = re.match(r"^([A-Ga-g][#fn-]?-?\d+)\s+(\d+)", line)
        if mm and measure is not None:
            tok, dur = mm.group(1), int(mm.group(2))
            tail = line[mm.end():]
            ties = ""
            if "[[" in tail:
                ties = "[["
            elif "[" in tail:
                ties = "["
            elif "]" in tail:
                ties = "]"
            elif "_" in tail:
                ties = "_"
            grace = bool(re.search(r"\bq\b", tail[:12])) and dur == 0
            measure["notes"].append({"pitch": midi_of(tok), "tok": tok, "dur": dur,
                                     "tie": ties, "grace": grace, "tail": tail[:14]})
            continue
        # 其他（clef/key 变化行、barlines 等）忽略
    return parts


def dump(parts, names, first, last):
    out = {}
    for p in parts:
        if names and p["name"] not in names:
            continue
        key = p["name"] or "?"
        mm = {}
        for meas in p["measures"]:
            if first <= meas["num"] <= last:
                mm[str(meas["num"])] = [n["pitch"] for n in meas["notes"] if n["pitch"] is not None]
        out[key] = mm
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--parts", default="")
    ap.add_argument("--measures", default="1-1000")
    ap.add_argument("--json")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()
    parts = parse(args.path)
    if args.list:
        for p in parts:
            print("%-24s measures=%-4d div=%s" % (p["name"], len(p["measures"]), p["divisions"]))
        return
    first, last = [int(x) for x in args.measures.split("-")]
    names = set(args.parts.split(",")) if args.parts else None
    res = dump(parts, names, first, last)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(res, fh, ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False))


if __name__ == "__main__":
    main()
