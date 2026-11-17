# -*- coding: utf-8 -*-
import os
from lxml import etree

BASE = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s9\src"
FILES = {
    "A": os.path.join(BASE, "src2_125808.xml"),
    "B": os.path.join(BASE, "src3_98865.xml"),
    "C": os.path.join(BASE, "src4_99688.xml"),
}
roots = {k: etree.parse(v).getroot() for k, v in FILES.items()}

print("### m1 attributes per part (A)")
for sp in roots['A'].findall('./part'):
    ms = sp.findall('./measure')
    a = ms[0].find('./attributes')
    print(sp.get('id'), 'measures=', len(ms),
          '| key', a.findtext('./key/fifths'), a.findtext('./key/mode'),
          '| time', a.findtext('./time/beats'), '/', a.findtext('./time/beat-type'),
          '| clef', a.findtext('./clef/sign'), a.findtext('./clef/line'),
          '| divisions', a.findtext('./divisions'))

print("\n### metronome anywhere (all files)")
for k, r in roots.items():
    hits = 0
    for sp in r.findall('./part'):
        for mm in sp.findall('./measure'):
            for m in mm.iter('metronome'):
                hits += 1
                print(f"  {k} {sp.get('id')} m{mm.get('number')}: {m.findtext('beat-unit')}={m.findtext('per-minute')}")
    print(f"  {k}: metronome count = {hits}")

print("\n### directions with <words> in mm.1-25 that are NOT inside <harmony> (A)")
for sp in roots['A'].findall('./part'):
    for mm in sp.findall('./measure')[:25]:
        for d in mm.findall('./direction'):
            w = [x.text for x in d.iter('words') if x.text]
            if w:
                print(f"  {sp.get('id')} m{mm.get('number')}: {w} sound={[s.get('tempo') for s in d.iter('sound')]}")

print("\n### barline list (A, P1)")
for mm in roots['A'].find('./part[@id="P1"]').findall('./measure'):
    for b in mm.findall('./barline'):
        print(f"  m{mm.get('number')}: {b.get('location')} {b.findtext('bar-style')} repeat={b.find('./repeat') is not None}")

print("\n### key / time / clef 变化 (A, 各 part 全部 measure 里的 attributes)")
for sp in roots['A'].findall('./part'):
    for mm in sp.findall('./measure'):
        a = mm.find('./attributes')
        if a is None: continue
        bits = []
        if a.find('./key') is not None: bits.append(f"key={a.findtext('./key/fifths')}")
        if a.find('./time') is not None: bits.append(f"time={a.findtext('./time/beats')}/{a.findtext('./time/beat-type')}")
        for c in a.findall('./clef'):
            bits.append(f"clef={c.findtext('sign')}{c.findtext('line')}")
        if a.find('./divisions') is not None: bits.append(f"div={a.findtext('divisions')}")
        if bits:
            print(f"  {sp.get('id')} m{mm.get('number')}: {' '.join(bits)}")
