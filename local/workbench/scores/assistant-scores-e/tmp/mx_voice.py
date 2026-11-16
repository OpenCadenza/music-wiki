import sys
import xml.etree.ElementTree as ET
from pathlib import Path

STEP = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def nm(step, alter, octv):
    m = 12 * (int(octv) + 1) + STEP[step] + int(alter or 0)
    return '%s%s' % (NAMES[m % 12], octv)


p = sys.argv[1]
root = ET.parse(p).getroot()
for el in root.iter():
    if '}' in el.tag:
        el.tag = el.tag.split('}', 1)[1]
div = 1
for m in root.iter('measure'):
    a = m.find('attributes')
    if a is not None and a.findtext('divisions'):
        div = int(a.findtext('divisions'))
    num = m.get('number')
    if int(num) < 1 or int(num) > 8:
        continue
    print('--- m.%s ---' % num)
    cur_beat = 0.0
    staff_notes = {1: [], 2: []}
    for el in m:
        if el.tag == 'backup':
            cur_beat -= float(el.findtext('duration')) / div
            continue
        if el.tag == 'forward':
            cur_beat += float(el.findtext('duration')) / div
            continue
        if el.tag != 'note':
            if el.tag == 'direction':
                w = [x.text.strip() for x in el.iter('words') if x.text and x.text.strip()]
                d = [x.tag for x in el.iter('dynamics')]
                o = [x.tag for x in el.iter('ornaments')]
                if w or d or o:
                    staff_notes.setdefault('dir', []).append(
                        ('b%.2f' % cur_beat + 1, '/'.join(d + w + o)))
            continue
        dur = float(el.findtext('duration') or 0) / div
        st = int(el.findtext('staff') or 1)
        pt = el.find('pitch')
        if el.find('rest') is not None:
            label = 'R'
        else:
            label = nm(pt.findtext('step'), pt.findtext('alter'), pt.findtext('octave'))
        typ = el.findtext('type') or '?'
        arts = []
        no = el.find('notations')
        if no is not None:
            for c in no:
                if c.tag in ('slur', 'tied'):
                    arts.append('%s:%s' % (c.tag, c.get('type')[0]))
                elif c.tag in ('articulations', 'ornaments'):
                    for g in c:
                        arts.append(g.tag)
        chord = '=chord ' if el.find('chord') is not None else ''
        grace = 'GRACE ' if el.find('grace') is not None else ''
        if not el.find('chord') is not None:
            pass
        staff_notes[st].append('%.2f %s%s%s/%s%s%s' % (
            cur_beat + 1, chord, grace, label, typ and typ, '.' * len(el.findall('dot')),
            ('[' + ','.join(arts) + ']') if arts else ''))
        if el.find('chord') is None:
            cur_beat += dur
    for st in (1, 2):
        print('  staff%d:' % st, ' | '.join(staff_notes[st]))
    if 'dir' in staff_notes:
        print('  marks:', staff_notes['dir'])
