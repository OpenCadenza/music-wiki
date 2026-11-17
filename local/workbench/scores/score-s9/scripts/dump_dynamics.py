# -*- coding: utf-8 -*-
"""按文档顺序累积时值，定位 mm.1-30 每条 dynamics 的 onset（divisions，1 拍 = 48）"""
import os
from lxml import etree

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XML = os.path.join(HERE, 'src', 'src3_98865.xml')
root = etree.parse(XML).getroot()
DIV = 48

def beatname(pos):
    names = {0: '第1拍', 24: '第1拍后半', 48: '第2拍', 72: '第2拍后半', 96: '小节线'}
    return names.get(int(pos), f'{pos:g}')

rows = []
for sp in root.findall('./part'):
    pid = sp.get('id')
    for mm in sp.findall('./measure')[:30]:
        t = 0.0
        for child in mm:
            if child.tag == 'note':
                if child.find('./chord') is not None or child.find('./grace') is not None:
                    continue
                d = child.findtext('duration')
                t += float(d) if d else 0.0
            elif child.tag == 'direction':
                dyn = child.findall('.//dynamics/*')
                if not dyn:
                    continue
                off = child.findtext('./offset')
                off = float(off) if off else 0.0
                rows.append((pid, mm.get('number'), t + off, [x.tag for x in dyn],
                             child.get('placement'), off))

print(f"{'声部':<4}{'小节':<6}{'onset/div':<10}{'拍位':<12}{'符号':<8}{'placement':<10}{'offset'}")
for pid, mnum, pos, sym, pl, off in rows:
    print(f"{pid:<6}{mnum:<8}{pos:<12g}{beatname(pos):<14}{','.join(sym):<10}{pl or '':<12}{off:g}")

print("\nmm.1-21 内的 dynamics 条数：", sum(1 for r in rows if int(r[1]) <= 21))
print("按声部：", {p: len([r for r in rows if r[0] == p and int(r[1]) <= 21]) for p in ['P1', 'P2', 'P3', 'P4']})
