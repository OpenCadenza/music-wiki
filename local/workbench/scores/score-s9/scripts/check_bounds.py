# -*- coding: utf-8 -*-
import os
from lxml import etree

BASE = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s9\src"
root = etree.parse(os.path.join(BASE, "src3_98865.xml")).getroot()

print("### dynamics 位置（前 60 小节）")
for sp in root.findall('./part'):
    out = []
    for mm in sp.findall('./measure')[:60]:
        for d in mm.findall('./direction'):
            dyn = [x.tag for x in d.iter('dynamics/*')]
            if dyn:
                out.append((mm.get('number'), dyn))
    print(" ", sp.get('id'), out[:10])

print("\n### mm.1-21 内的 slur/tie 事件（检查跨 m21 边界）")
for pid in ['P1','P2','P3','P4']:
    sp = root.find(f"./part[@id='{pid}']")
    for mm in sp.findall('./measure')[:22]:
        n = mm.get('number')
        for note in mm.findall('./note'):
            t = note.find('./tie')
            nn = note.find('./notations')
            sl = [(s.get('type'), s.get('number')) for s in (nn.findall('./slur') if nn is not None else [])]
            td = [(x.get('type'), x.get('number')) for x in (nn.findall('./tied') if nn is not None else [])]
            if (t is not None and int(n) >= 20) or sl or td:
                if int(n) >= 18:
                    print(f"  {pid} m{n}: tie={t.get('type') if t is not None else None} slur={sl} tied={td}")

print("\n### m21 之后 m22-23 内容（判断小提琴是否接棒）")
for pid in ['P1','P2','P3','P4']:
    sp = root.find(f"./part[@id='{pid}']")
    for mm in sp.findall('./measure')[21:23]:
        notes = []
        for note in mm.findall('./note'):
            r = note.find('./rest') is not None
            p = note.find('./pitch')
            if r: notes.append('R')
            else: notes.append(f"{p.findtext('step')}{p.findtext('alter') or ''}{p.findtext('octave')}/{note.findtext('type')}{'.'*len(note.findall('./dot'))}")
        print(f"  {pid} m{mm.get('number')}: {notes}")
