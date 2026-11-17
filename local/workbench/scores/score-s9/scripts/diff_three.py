# -*- coding: utf-8 -*-
import os, sys
from lxml import etree

BASE = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s9\src"
FILES = {
    "A": os.path.join(BASE, "src2_125808.xml"),
    "B": os.path.join(BASE, "src3_98865.xml"),
    "C": os.path.join(BASE, "src4_99688.xml"),
}
roots = {k: etree.parse(v).getroot() for k, v in FILES.items()}

PITCH = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
def midi(step, alter, octv):
    v = PITCH[step] + int(alter or 0) + (int(octv)+1)*12
    return v

def note_tokens(mm, part):
    """canonical list of note tokens for comparison"""
    toks = []
    for n in mm.findall('./note'):
        rest = n.find('./rest') is not None
        p = n.find('./pitch')
        if p is not None:
            pitch = (p.findtext('step'), (p.findtext('alter') or '0'), p.findtext('octave'))
        else:
            pitch = None
        toks.append((n.findtext('./voice'), n.findtext('./staff'),
                     pitch, n.findtext('./duration'), n.findtext('./type'),
                     len(n.findall('./dot')), n.find('./chord') is not None, rest,
                     (n.find('./tie').get('type') if n.find('./tie') is not None else ''),
                     (n.findtext('./stem') or '')))
    return toks

print("### 三份源 mm.1-21 逐小节音符比对")
diff_total = 0
for pid in ['P1','P2','P3','P4']:
    for i in range(1, 22):
        per = {}
        for k, r in roots.items():
            sp = r.find(f"./part[@id='{pid}']")
            ms = sp.findall('./measure')
            per[k] = note_tokens(ms[i-1], pid)
        if not (per['A'] == per['B'] == per['C']):
            diff_total += 1
            print(f"  DIFF {pid} m{i}")
            for k in 'ABC':
                print(f"    {k}: {per[k]}")
print(f"  --> 差异小节数: {diff_total}")

# 全曲逐小节比对（只看音符规范序列）
print("\n### 全曲 212 小节 三份源音符比对")
alldiff = []
for pid in ['P1','P2','P3','P4']:
    for i in range(1, 213):
        per = {}
        for k, r in roots.items():
            sp = r.find(f"./part[@id='{pid}']")
            per[k] = note_tokens(sp.findall('./measure')[i-1], pid)
        if not (per['A'] == per['B'] == per['C']):
            alldiff.append((pid, i))
print("  差异:", alldiff if alldiff else "无 —— 三份源音符内容完全一致")
