#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""导出 Kern 逐小节逐声部音符清单（供报告附表使用）。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from compare import parse_kern, fmt

kb = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\source-packages"
chor = kb + r"\humdrum\bach-370-chorales-main\bach-370-chorales-main\kern"
q74 = kb + r"\beethoven-score-sources\beethoven-string-quartets-main\beethoven-string-quartets-main\kern\quartet10-1.krn"

DUR = {4.0:'1', 3.0:'2.', 2.0:'2', 1.5:'4.', 1.0:'4', 0.75:'8.', 0.5:'8', 0.25:'16'}
def dstr(d):
    return DUR.get(round(d,3), f"{d:g}q")

jobs = [
 ("1. BWV 269 mm.3–4（chor001.krn）", chor+r"\chor001.krn", [3,4], {'S':3,'A':2,'T':1,'B':0}),
 ("2. BWV 347 mm.3–4（chor002.krn）", chor+r"\chor002.krn", [3,4], {'S':3,'A':2,'T':1,'B':0}),
 ("3. BWV 38/6 mm.12–13（chor010.krn）", chor+r"\chor010.krn", [12,13], {'S':3,'A':2,'T':1,'B':0}),
 ("4. BWV 153/5 mm.3–4（chor021.krn）", chor+r"\chor021.krn", [3,4], {'S':3,'A':2,'T':1,'B':0}),
 ("5. BWV 87/7 mm.1–3（chor096.krn）", chor+r"\chor096.krn", [1,2,3], {'S':3,'A':2,'T':1,'B':0}),
 ("6. BWV 269 mm.5–7（chor001.krn）", chor+r"\chor001.krn", [5,6,7], {'S':3,'A':2,'T':1,'B':0}),
 ("7. BWV 60/5 mm.1–4（chor216.krn）", chor+r"\chor216.krn", [1,2,3,4], {'S':3,'A':2,'T':1,'B':0}),
 ("8. Op.74 I mm.18–24（quartet10-1.krn）", q74, list(range(18,25)), {'Vn1':6,'Vn2':4,'Va':2,'Vc':0}),
]

for title, path, ms, vmap in jobs:
    k = parse_kern(path)
    print("\n#### " + title)
    print("| 声部 | " + " | ".join(f"m.{m}" for m in ms) + " |")
    print("| :--- | " + " | ".join(":---" for _ in ms) + " |")
    for v, sp in vmap.items():
        cells = []
        for m in ms:
            evs = sorted(k.get((m, sp), []))
            if not evs:
                cells.append("—")
                continue
            # 合并同时发声音
            g = {}
            for b, p, d, t in evs:
                g.setdefault(b, []).append((p, d))
            parts = []
            for b in sorted(g):
                ps = g[b]
                name = '+'.join(fmt(p) for p, d in ps)
                dd = ps[0][1]
                parts.append(f"{name}({dstr(dd)})")
            cells.append(" ".join(parts))
        print(f"| {v} | " + " | ".join(cells) + " |")
