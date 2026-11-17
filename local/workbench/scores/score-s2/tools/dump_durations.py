#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump duration values for movement IV m.14-15 of Mozart K.465."""
import glob
import xml.etree.ElementTree as ET

f = glob.glob(r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s2\downloads\mozart-mxl\**\*.xml", recursive=True)[0]
root = ET.parse(f).getroot()
parts = root.findall('part')
STEP = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}

def pitch(n):
    p = n.find('pitch')
    if p is None:
        return None
    return (int(p.findtext('octave')) + 1) * 12 + STEP[p.findtext('step')] + int(p.findtext('alter') or 0)

first = None
for i, m in enumerate(parts[0].findall('measure')):
    a = m.find('attributes')
    if a is None:
        continue
    t = a.find('time')
    if t is not None and t.findtext('beats') == '2' and t.findtext('beat-type') == '4':
        first = i
        break

divs = 1
for m in parts[0].findall('measure'):
    a = m.find('attributes')
    if a is not None and a.find('divisions') is not None:
        divs = int(a.findtext('divisions'))
        break
print('divisions per quarter:', divs)

for pi, part in enumerate(parts):
    ms = part.findall('measure')
    print('== part', pi + 1, '==')
    for off in (first + 14, first + 15):
        m = ms[off]
        num = m.get('number')
        items = []
        total = 0
        for n in m.findall('note'):
            dur = int(n.findtext('duration') or 0)
            total += dur
            if n.find('rest') is not None:
                items.append('r(%d)' % dur)
            else:
                items.append('%d(%d)' % (pitch(n), dur))
        print('  m%s: %s   total=%d (%.2f quarters)' % (num, ' '.join(items), total, total / divs))
