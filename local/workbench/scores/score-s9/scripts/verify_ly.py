# -*- coding: utf-8 -*-
"""把 .ly 里手写的 4 个声部与主源 XML 做「逐小节 × 逐音符」比对。

比对项：
  * 起音音高组（含和弦）
  * 每个音符上挂的 断奏 / 重音 / tenuto 数量
  * 每个音符上挂的 slur start / slur stop / tie（按音符位置，不只看总数）
  * 每个音符上挂的力度记号（\p \pp ...，按音符位置）
  * 装饰音音高

.ly 约定：每个声部块以 `|` 切小节（一小节可能跨行）。
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
TOK_RE = re.compile(r"<([^>]*)>(\d+\.*)|([a-g][fs]?[',]*)(\d+\.*)")


def ly_pitch(tok):
    m = re.fullmatch(r"([a-g])([fs]?)([',]*)", tok)
    if not m:
        raise ValueError(tok)
    step, acc, octmarks = m.group(1), m.group(2), m.group(3)
    alt = 1 if acc == 's' else (-1 if acc == 'f' else 0)
    octave = 3 + octmarks.count("'") - octmarks.count(",")
    return PITCHSTEP[step] + alt + (octave + 1) * 12


DYN_RE = re.compile(r"\\(ppp|pp|mp|mf|ff|f|p)\b")


def ly_parse(line):
    line = line.split('%')[0]
    graces = []
    for g in re.finditer(r'\\grace\s*\{([^}]*)\}', line):
        for t in g.group(1).split():
            graces.append(ly_pitch(re.sub(r'\d+\.*$', '', t)))
    line = re.sub(r'\\grace\s*\{[^}]*\}', ' ', line)
    line = re.sub(r'\\mark\s*\\markup\s*\{[^}]*\}', ' ', line)
    line = re.sub(r'"[^"]*"', ' ', line)

    matches = list(TOK_RE.finditer(line))
    groups = []
    for i, m in enumerate(matches):
        chord, _, single, _ = m.groups()
        pitches = sorted(ly_pitch(t.strip()) for t in chord.split()) if chord else [ly_pitch(single)]
        tail = line[m.end(): matches[i + 1].start() if i + 1 < len(matches) else len(line)]
        dyn = DYN_RE.findall(tail)
        groups.append({
            'pitches': pitches,
            'slur_start': '(' in tail,
            'slur_stop': ')' in tail,
            'tie': '~' in tail,
            'staccato': len(re.findall(r'-\.', tail)),
            'accent': len(re.findall(r'->', tail)) + len(re.findall(r'\\accent', tail)),
            'tenuto': len(re.findall(r'--', tail)) + len(re.findall(r'\\tenuto', tail)),
            'dyn': dyn,
        })
    return groups, graces


XMLPITCH = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}


def xml_measure(pid, idx):
    sp = root.find(f"./part[@id='{pid}']")
    mm = sp.findall('./measure')[idx]
    groups = []
    graces = []
    dyn_events = []          # (onset, symbol)
    t = 0.0
    for child in mm:
        if child.tag == 'note':
            n = child
            if n.find('./chord') is not None:
                continue
            p = n.find('./pitch')
            pitch = None
            if p is not None:
                pitch = (XMLPITCH[p.findtext('step')] + int(p.findtext('alter') or 0)
                         + (int(p.findtext('octave')) + 1) * 12)
            pitches = [pitch] if pitch is not None else []
            # 收集和弦成员
            for sib in n.itersiblings():
                if sib.tag != 'note' or sib.find('./chord') is None:
                    break
                q = sib.find('./pitch')
                if q is not None:
                    pitches.append(XMLPITCH[q.findtext('step')] + int(q.findtext('alter') or 0)
                                   + (int(q.findtext('octave')) + 1) * 12)
            nn = n.find('./notations')
            sl = tl = 0
            if nn is not None:
                sl = len([s for s in nn.findall('./slur') if s.get('type') == 'start'])
                tl = len([s for s in nn.findall('./slur') if s.get('type') == 'stop'])
            arts = {}
            if nn is not None:
                for a in nn.findall('./articulations/*'):
                    arts[a.tag] = arts.get(a.tag, 0) + 1
            tie = n.find('./tie')
            is_grace = n.find('./grace') is not None
            g = {
                'pitches': sorted(pitches),
                'onset': t,
                'slur_start': sl > 0,
                'slur_stop': tl > 0,
                'tie': tie is not None and tie.get('type') == 'start',
                'staccato': arts.get('staccato', 0),
                'accent': arts.get('accent', 0),
                'tenuto': arts.get('tenuto', 0),
                'dyn': [],
            }
            if is_grace:
                graces.extend(pitches)
            elif pitches:
                groups.append(g)
            d = n.findtext('duration')
            if not is_grace and d:
                t += float(d)
        elif child.tag == 'direction':
            for sym in child.findall('.//dynamics/*'):
                off = child.findtext('./offset')
                dyn_events.append((t + (float(off) if off else 0.0), sym.tag))
    # 把力度事件挂到 onset 最近的音组上
    for onset, sym in dyn_events:
        best = 0
        for i, g in enumerate(groups):
            if g['onset'] <= onset + 1e-6:
                best = i
        groups[best]['dyn'].append(sym) if groups else None
    return groups, graces


PAIRS = [('violin', 'P1'), ('cello', 'P2'), ('pianoRH', 'P3'), ('pianoLH', 'P4')]
bad = 0
for lname, pid in PAIRS:
    segs = blocks[lname]
    assert len(segs) == 21, (lname, len(segs))
    for idx in range(21):
        lg, lgrac = ly_parse(segs[idx])
        xg, xgrac = xml_measure(pid, idx)
        m = idx + 1
        lp = [g['pitches'] for g in lg]
        xp = [g['pitches'] for g in xg]
        if lp != xp:
            bad += 1
            print(f"[音高] {lname} m{m}\n   ly : {lp}\n   xml: {xp}")
            continue
        for i, (a, b) in enumerate(zip(lg, xg)):
            for k in ['slur_start', 'slur_stop', 'tie', 'staccato', 'accent', 'tenuto']:
                if a[k] != b[k]:
                    bad += 1
                    print(f"[{k}] {lname} m{m} 第{i + 1}个音: ly={a[k]!r} xml={b[k]!r} pitch={a['pitches']}")
            if a['dyn'] != b['dyn']:
                bad += 1
                print(f"[力度] {lname} m{m} 第{i + 1}个音: ly={a['dyn']} xml={b['dyn']} pitch={a['pitches']}")
        if sorted(lgrac) != sorted(xgrac):
            bad += 1
            print(f"[装饰音] {lname} m{m}: ly={lgrac} xml={xgrac}")
print("不一致条目：", bad)
