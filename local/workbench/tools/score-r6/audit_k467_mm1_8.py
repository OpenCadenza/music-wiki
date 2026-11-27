#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""audit_k467_mm1_8 (score-r6)：把既有 mozart-k467-i-mm1-8 围栏与 CCARH md2 逐小节对照。

只做音高（MIDI）多重集对照，用来判断既有围栏的声部分配是否与底本一致。
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import md2parse

MD2 = os.path.join("local", "origin_resources", "sources",
                   "ccarh-musedata-concertos", "mozart-k467-mvt1.md2")
DOC = os.path.join("content", "techniques", "structure",
                   "concertante-principle-and-double-exposition.md")
SEMI = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}

FENCE_STAFFS = [
    ("timpani", "Timp./C-G"),
    ("oboeOne", "Ob_1_"),
    ("oboeTwo", "Ob_2_"),
    ("bassoonOne", "Fag_1_"),
    ("hornOne", "Cor_1_/(C)"),
    ("trumpetOne", "Clr_1_/(C)"),
    ("violinOne", "Vln_1_"),
    ("cello", "Vc_"),
]

NOTE = re.compile(r"([a-g])(s{0,2}|f{0,2})?(,*)(\'*)")


def fence_pitches(text, var):
    """抽出围栏里某个变量的每小节音高（MIDI）列表。"""
    m = re.search(r"^%s = \{(.*?)^\}" % re.escape(var), text, re.S | re.M)
    if not m:
        return None
    body = m.group(1)
    bars = []
    cur = []
    for line in body.splitlines():
        s = line.split("%")[0]
        if s.strip().startswith(("\\", "%")):
            continue
        for mm in NOTE.finditer(s):
            letter, acc, commas, apos = mm.group(1), mm.group(2) or "", mm.group(3), mm.group(4)
            # 跳过 \clef bass 之类伪命中（前面紧跟反斜杠）
            if mm.start() > 0 and s[mm.start() - 1] == "\\":
                continue
            alter = acc.count("s") - acc.count("f")
            octv = 3 + len(apos) - len(commas)   # c' = C4
            cur.append((octv + 1) * 12 + SEMI[letter.upper()] + alter)
        if "|" in s:
            bars.append(sorted(cur))
            cur = []
    if cur:
        bars.append(sorted(cur))
    return bars


def main():
    text = open(DOC, encoding="utf-8").read()
    parts = {p["name"]: p for p in md2parse.parse(MD2)}
    for fvar, mpart in FENCE_STAFFS:
        bars = fence_pitches(text, fvar)
        if bars is None:
            print("!! 围栏里找不到变量", fvar)
            continue
        src = {m["num"]: sorted(n["pitch"] for n in m["notes"]
                                if n["pitch"] is not None and not (n.get("tok") or "").startswith("g"))
               for m in parts[mpart]["measures"] if 1 <= m["num"] <= 8}
        ok = 0
        bad = []
        for i, bar in enumerate(bars[:8], start=1):
            if sorted(bar) == sorted(src.get(i, [])):
                ok += 1
            else:
                bad.append(i)
        print("%-11s ↔ %-10s 一致 %d/8  不一致小节 %s" % (fvar, mpart, ok, bad or "-"))
        for i in bad[:3]:
            print("    m%d 围栏=%s" % (i, sorted(bars[i - 1])))
            print("       底本=%s" % (src.get(i),))


if __name__ == "__main__":
    main()
