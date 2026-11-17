#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse Mozart K.465 MusicXML (OpenScore) and print mm.10-16 of movement IV
per part, with pitch/duration/type/dot/tie. Movement IV is located by its 2/4
time signature.
"""
import glob
import sys
import xml.etree.ElementTree as ET

f = glob.glob(r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s2\downloads\mozart-mxl\**\*.xml", recursive=True)[0]
root = ET.parse(f).getroot()
parts = root.findall('part')
print('parts:', len(parts))

STEP = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}

def pitch_of(note):
    p = note.find('pitch')
    if p is None:
        return None
    step = p.findtext('step')
    octv = int(p.findtext('octave'))
    alter = int(p.findtext('alter') or 0)
    return (octv + 1) * 12 + STEP[step] + alter

def note_info(note):
    rest = note.find('rest') is not None
    p = pitch_of(note)
    dur = int(note.findtext('duration') or 0)
    typ = note.findtext('type') or ''
    dots = len(note.findall('dot'))
    tie = note.find('tie')
    tied = tie is not None
    return rest, p, dur, typ, dots, tied

# find first measure (in part 0) whose attributes contain time 2/4
first_iv = None
for i, m in enumerate(parts[0].findall('measure')):
    attrs = m.find('attributes')
    if attrs is None:
        continue
    t = attrs.find('time')
    if t is not None and t.findtext('beats') == '2' and t.findtext('beat-type') == '4':
        first_iv = i
        break
print('first 2/4 measure index in part0:', first_iv)
if first_iv is None:
    sys.exit('movement IV not found')

# The movement IV measure sequence may contain repeated numbers (repeats).
# Print measure numbers from first_iv onward for a sense of numbering.
ms = parts[0].findall('measure')
print('measure numbers around IV start:', [ms[i].get('number') for i in range(first_iv, min(first_iv+16, len(ms)))])

for pi, part in enumerate(parts):
    ms = part.findall('measure')
    print(f'=== part {pi+1} ===')
    # take measures at offset first_iv+10 .. first_iv+16 (m.10-16 of movement IV)
    for off in range(first_iv + 10, first_iv + 17):
        if off >= len(ms):
            break
        m = ms[off]
        num = m.get('number')
        items = []
        for note in m.findall('note'):
            rest, p, dur, typ, dots, tied = note_info(note)
            if rest:
                items.append(f'rest({typ}{"."*dots})')
            else:
                items.append(f'{p}({typ}{"."*dots}{"~" if tied else ""})')
        # collect time sig changes in this measure
        print(f'  m{num}: ' + ' '.join(items))
