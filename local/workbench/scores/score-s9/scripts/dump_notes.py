# -*- coding: utf-8 -*-
import os, sys
from lxml import etree

BASE = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s9\src"
FILE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "src3_98865.xml")
M0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1
M1 = int(sys.argv[3]) if len(sys.argv) > 3 else 21
root = etree.parse(FILE).getroot()

# divisions = 48 per quarter (verified from <divisions>48</divisions>)
DIVMAP = {192:'w',96:'h',48:'q',24:'e',12:'s',6:'t',3:'x',
          144:'h.',72:'q.',36:'e.',18:'s.',9:'t.',
          8:'t-trip',16:'s-trip',32:'e-trip',64:'q-trip'}
def dlab(d):
    d = int(d)
    return DIVMAP.get(d, f'[{d}]')

def note_str(n):
    bits = []
    if n.find('./grace') is not None: bits.append('GRACE')
    if n.find('./chord') is not None: bits.append('+')
    p = n.find('./pitch')
    if n.find('./rest') is not None:
        r = n.find('./rest')
        bits.append('R' + ('(meas)' if r.get('measure')=='yes' else ''))
    else:
        step = p.findtext('step'); alt = p.findtext('alter'); oc = p.findtext('octave')
        acc = {'-2':'bb','-1':'b','0':'','1':'#','2':'##'}[alt or '0']
        bits.append(f"{step}{acc}{oc}")
    d = n.findtext('duration')
    if d is not None: bits.append(dlab(d))
    ty = n.findtext('type'); dots = len(n.findall('./dot'))
    if ty: bits.append(ty + '.'*dots)
    t = n.find('./tie')
    if t is not None: bits.append('~'+t.get('type'))
    nn = n.find('./notations')
    if nn is not None:
        for sl in nn.findall('./slur'):
            bits.append('SLUR' + (sl.get('number') or '') + ':' + (sl.get('type') or ''))
        for ar in nn.findall('./articulations/*'):
            bits.append(ar.tag)
    tm = n.find('./time-modification')
    if tm is not None:
        bits.append(f"TUPLET{tm.findtext('actual-notes')}:{tm.findtext('normal-notes')}"
                    + ("(<type>%s)" % tm.findtext('normal-type') if tm.findtext('normal-type') else ""))
    st = n.findtext('./stem')
    if st: bits.append('st' + st[0])
    return ' '.join(bits)

def walk_sum(m):
    tot = 0
    for n in m.findall('./note'):
        if n.find('./chord') is not None: continue
        if n.find('./grace') is not None: continue
        d = n.findtext('duration')
        if d: tot += int(d)
    return tot

for i in range(M0, M1+1):
    print("="*100)
    attrs_all = []
    for pid in ['P1','P2','P3','P4']:
        sp = root.find(f"./part[@id='{pid}']")
        m = sp.findall('./measure')[i-1]
        a = m.find('./attributes')
        if a is not None:
            if a.find('./key') is not None: attrs_all.append(f"{pid}:key{a.findtext('./key/fifths')}")
            if a.find('./time') is not None: attrs_all.append(f"{pid}:time{a.findtext('./time/beats')}/{a.findtext('./time/beat-type')}")
            for c in a.findall('./clef'): attrs_all.append(f"{pid}:clef{c.findtext('sign')}{c.findtext('line')}")
    print(f"### MEASURE {i}  {' '.join(attrs_all)}")
    for pid in ['P1','P2','P3','P4']:
        sp = root.find(f"./part[@id='{pid}']")
        m = sp.findall('./measure')[i-1]
        print(f"-- {pid}  sum={walk_sum(m)}/96")
        for n in m.findall('./note'):
            v = n.findtext('./voice'); s = n.findtext('./staff')
            print(f"   v{v}s{s or '-'} {note_str(n)}")
        for d in m.findall('./direction'):
            ws = [x.text for x in d.iter('words')]
            dyn = [x.text for x in d.iter('dynamics/*')]
            if ws or dyn:
                print(f"   DIR {d.get('placement')} words={ws} dyn={dyn}")
        for b in m.findall('./barline'):
            print(f"   BARLINE {b.get('location')} {b.findtext('bar-style')}")
