# -*- coding: utf-8 -*-
"""把 .ly 里手写的 4 个声部与主源 XML 做「逐小节 × 起音/奏法」比对。

.ly 的约定：每个声部块以 `|` 切小节（一小节可能跨行）。
"""
import os, re
from lxml import etree

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LY = os.path.join(HERE, 'schubert-d929-mvt2-mm1-21.ly')
XML = os.path.join(HERE, 'src', 'src3_98865.xml')

root = etree.parse(XML).getroot()
text = open(LY, encoding='utf-8').read()

blocks = {}
for name in ['violin', 'cello', 'pianoRH', 'pianoLH']:
    m = re.search(r'\n' + name + r' = \{(.*?)\n\}', text, re.S)
    body = m.group(1)
    cleaned = '\n'.join(ln.split('%')[0] for ln in body.splitlines())
    segs = [s.strip() for s in cleaned.split('|')]
    blocks[name] = [s for s in segs if s]

PITCHSTEP = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}


def ly_pitch(tok):
    m = re.fullmatch(r"([a-g])([fs]?)([',]*)", tok)
    if not m:
        raise ValueError(tok)
    step, acc, octmarks = m.group(1), m.group(2), m.group(3)
    alt = 1 if acc == 's' else (-1 if acc == 'f' else 0)
    octave = 3 + octmarks.count("'") - octmarks.count(',')
    return PITCHSTEP[step] + alt + (octave + 1) * 12


def ly_parse(line):
    line = line.split('%')[0]
    graces = []
    for g in re.finditer(r'\\grace\s*\{([^}]*)\}', line):
        for t in g.group(1).split():
            graces.append(ly_pitch(re.sub(r'\d+\.*$', '', t)))
    line = re.sub(r'\\grace\s*\{[^}]*\}', ' ', line)
    line = re.sub(r'\\mark\s*\\markup\s*\{[^}]*\}', ' ', line)
    line = re.sub(r'"[^"]*"', ' ', line)
    tok_re = re.compile(r"<([^>]*)>(\d+\.*)|([a-g][fs]?[',]*)(\d+\.*)")
    groups = []
    for m in tok_re.finditer(line):
        chord, dur1, single, dur2 = m.group(1), m.group(2), m.group(3), m.group(4)
        if chord:
            groups.append(sorted(ly_pitch(t.strip()) for t in chord.split()))
        else:
            groups.append([ly_pitch(single)])
    arts = {
        'staccato': len(re.findall(r'-\.', line)),
        'accent': len(re.findall(r'->', line)) + len(re.findall(r'\\accent', line)),
        'tenuto': len(re.findall(r'--', line)) + len(re.findall(r'\\tenuto', line)),
        'tie': line.count('~'),
        'slur_start': line.count('('),
        'slur_stop': line.count(')'),
    }
    return groups, arts, graces


XMLPITCH = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def xml_measure(pid, idx):
    sp = root.find(f"./part[@id='{pid}']")
    mm = sp.findall('./measure')[idx]
    groups = []
    arts = {'staccato': 0, 'accent': 0, 'tenuto': 0, 'tie': 0, 'slur_start': 0, 'slur_stop': 0}
    graces = []
    notes = mm.findall('./note')
    i = 0
    while i < len(notes):
        n = notes[i]
        if n.find('./chord') is not None:
            i += 1
            continue
        pitches = []

        def pv(el):
            p = el.find('./pitch')
            if p is None:
                return None
            return (XMLPITCH[p.findtext('step')] + int(p.findtext('alter') or 0)
                    + (int(p.findtext('octave')) + 1) * 12)
        if pv(n) is not None:
            pitches.append(pv(n))
        j = i + 1
        while j < len(notes) and notes[j].find('./chord') is not None:
            if pv(notes[j]) is not None:
                pitches.append(pv(notes[j]))
            j += 1
        is_grace = n.find('./grace') is not None
        nn = n.find('./notations')
        if nn is not None:
            for a in nn.findall('./articulations/*'):
                if a.tag in arts:
                    arts[a.tag] += 1
            arts['slur_start'] += len([s for s in nn.findall('./slur') if s.get('type') == 'start'])
            arts['slur_stop'] += len([s for s in nn.findall('./slur') if s.get('type') == 'stop'])
        t = n.find('./tie')
        if t is not None and t.get('type') == 'start':
            arts['tie'] += 1
        if is_grace:
            graces.extend(pitches)
        elif pitches:
            groups.append(sorted(pitches))
        i = j
    return groups, arts, graces


PAIRS = [('violin', 'P1'), ('cello', 'P2'), ('pianoRH', 'P3'), ('pianoLH', 'P4')]
bad = 0
for lname, pid in PAIRS:
    segs = blocks[lname]
    assert len(segs) == 21, (lname, len(segs))
    for idx in range(21):
        lg, la, lgrac = ly_parse(segs[idx])
        xg, xa, xgrac = xml_measure(pid, idx)
        if lg != xg:
            bad += 1
            print(f"[音高] {lname} m{idx + 1}\n   ly : {lg}\n   xml: {xg}")
        if la != xa:
            bad += 1
            print(f"[奏法] {lname} m{idx + 1}\n   ly : {la}\n   xml: {xa}")
        if sorted(lgrac) != sorted(xgrac):
            bad += 1
            print(f"[装饰音] {lname} m{idx + 1}: ly={lgrac} xml={xgrac}")
print("不一致条目：", bad)
