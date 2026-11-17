# -*- coding: utf-8 -*-
import os
from lxml import etree
from collections import Counter

BASE = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s9\src"
FILES = {
    "A": os.path.join(BASE, "src2_125808.xml"),
    "B": os.path.join(BASE, "src3_98865.xml"),
    "C": os.path.join(BASE, "src4_99688.xml"),
}
roots = {k: etree.parse(v).getroot() for k, v in FILES.items()}

def canon(el, drop=('print','sound','direction')):
    # copy and strip layout-only nodes
    e = etree.fromstring(etree.tostring(el))
    for tag in drop:
        for x in e.iter(tag):
            x.getparent().remove(x)
    return etree.tostring(e, method='c14n')

print("### 全曲元素标签计数")
for k, r in roots.items():
    c = Counter(x.tag for x in r.iter())
    print(f"  {k}: {dict(sorted(c.items()))}")

print("\n### 音符级标记（articulations / slur / dynamics 等）mm.1-21 计数")
for k, r in roots.items():
    c = Counter()
    for sp in r.findall('./part'):
        for mm in sp.findall('./measure')[:21]:
            for n in mm.findall('./note'):
                nt = n.find('./notations')
                if nt is None: continue
                for ch in nt.iter():
                    if ch is nt: continue
                    c[(sp.get('id'), ch.tag)] += 1
    print(f"  {k}: {dict(sorted(c.items()))}")

print("\n### mm.1-21 规范化 XML 差异（去 print/direction/sound）")
cnt = 0
for pid in ['P1','P2','P3','P4']:
    for i in range(1,22):
        vals = {}
        for k, r in roots.items():
            m = r.find(f"./part[@id='{pid}']").findall('./measure')[i-1]
            vals[k] = canon(m)
        if not (vals['A']==vals['B']==vals['C']):
            cnt += 1
            print(f"  DIFF {pid} m{i}; lens " + str({k: len(v) for k,v in vals.items()}))
print("  差异:", cnt)

print("\n### defaults / credit / identification")
for k, r in roots.items():
    print(f"  {k}: children = {[x.tag for x in r]}")
    i = r.find('./identification')
    if i is not None:
        print("      identification:", etree.tostring(i, encoding='unicode').strip()[:400].replace('\n',' '))
