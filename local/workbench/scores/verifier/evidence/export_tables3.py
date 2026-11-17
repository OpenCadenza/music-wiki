#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""导出 Kern 逐小节逐声部音符清单（保留原谱拼写，供报告附表使用）。"""
import re

kb = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\source-packages"
chor = kb + r"\humdrum\bach-370-chorales-main\bach-370-chorales-main\kern"
q74 = kb + r"\beethoven-score-sources\beethoven-string-quartets-main\beethoven-string-quartets-main\kern\quartet10-1.krn"

DUR = {4.0:'1', 3.0:'2.', 2.0:'2', 1.5:'4.', 1.0:'4', 0.75:'8.', 0.5:'8', 0.25:'16'}
def dstr(d): return DUR.get(round(d,3), "%gq" % d)

def tok(tokstr):
    t = tokstr.strip()
    if t in ('', '.'): return None
    out = []
    for part in t.split(' '):
        p = part
        if p[:1] in '([': p = p[1:]
        if p.endswith(']'): p = p[:-1]
        m = re.match(r'^(\d+)(\.*)(.*)$', p)
        if not m: continue
        num = int(m.group(1)); dots = len(m.group(2)); rest = m.group(3)
        dur = 4.0/num; add = dur
        for _ in range(dots): add /= 2.0; dur += add
        pm = re.match(r'^([a-gA-G]+)((?:#|-|n|X|Y)*)', rest)
        if not pm:
            out.append(('r', dur)); continue
        L, acc = pm.group(1), pm.group(2)
        n = len(L)
        octv = 4 + (n-1) if L[0].islower() else 4 - n
        s = L[0].upper()
        for ch in acc:
            if ch == '#': s = s + '#'
            elif ch == '-': s = s + 'b'
        out.append((s + str(octv), dur))
    return out

def parse(path, keep):
    spines = None; meas = 0; beat = []; res = {}
    for line in open(path, encoding='utf-8', errors='replace'):
        line = line.rstrip('\n')
        if line.startswith('**'):
            spines = line.split('\t'); beat = [0.0]*len(spines); continue
        if line.startswith('!') or line.startswith('*'): continue
        toks = line.split('\t')
        if spines is None or len(toks) != len(spines): continue
        if toks[0].startswith('='):
            mm = re.match(r'(\d+)', toks[0][1:])
            if mm: meas = int(mm.group(1))
            beat = [0.0]*len(spines); continue
        for i, tk in enumerate(toks):
            r = tok(tk)
            if not r: continue
            step = max(d for _, d in r)
            if i in keep:
                for name, d in r:
                    if name != 'r':
                        res.setdefault((meas, i), []).append((beat[i], name, d))
            beat[i] += step
    return res

jobs = [
 ("1. BWV 269 mm.3-4 (chor001.krn)", chor+r"\chor001.krn", [3,4], [('S',3),('A',2),('T',1),('B',0)]),
 ("2. BWV 347 mm.3-4 (chor002.krn)", chor+r"\chor002.krn", [3,4], [('S',3),('A',2),('T',1),('B',0)]),
 ("3. BWV 38/6 mm.12-13 (chor010.krn)", chor+r"\chor010.krn", [12,13], [('S',3),('A',2),('T',1),('B',0)]),
 ("4. BWV 153/5 mm.3-4 (chor021.krn)", chor+r"\chor021.krn", [3,4], [('S',3),('A',2),('T',1),('B',0)]),
 ("5. BWV 87/7 mm.1-3 (chor096.krn)", chor+r"\chor096.krn", [1,2,3], [('S',3),('A',2),('T',1),('B',0)]),
 ("6. BWV 269 mm.5-7 (chor001.krn)", chor+r"\chor001.krn", [5,6,7], [('S',3),('A',2),('T',1),('B',0)]),
 ("7. BWV 60/5 mm.1-4 (chor216.krn)", chor+r"\chor216.krn", [1,2,3,4], [('S',3),('A',2),('T',1),('B',0)]),
 ("8. Op.74 I mm.18-24 (quartet10-1.krn)", q74, list(range(18,25)), [('Vn1',6),('Vn2',4),('Va',2),('Vc',0)]),
]

for title, path, ms, vlist in jobs:
    k = parse(path, set(sp for _, sp in vlist))
    print("\n**" + title + "**\n")
    print("| 声部 | " + " | ".join("m.%d" % m for m in ms) + " |")
    print("| :--- | " + " | ".join(":---" for _ in ms) + " |")
    for v, sp in vlist:
        cells = []
        for m in ms:
            evs = sorted(k.get((m, sp), []))
            if not evs:
                cells.append("—"); continue
            g = {}
            for b, nm, d in evs:
                g.setdefault(b, []).append((nm, d))
            parts = []
            for b in sorted(g):
                names = '+'.join(nm for nm, _ in g[b])
                parts.append("%s(%s)" % (names, dstr(g[b][0][1])))
            cells.append(" ".join(parts))
        print("| %s | " % v + " | ".join(cells) + " |")

