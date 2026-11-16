import sys
import xml.etree.ElementTree as ET

STEP = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def nm(step, alter, octv):
    m = 12 * (int(octv) + 1) + STEP[step] + int(alter or 0)
    return '%s%s(%d)' % (NAMES[m % 12], octv, m)


def main():
    p = sys.argv[1]
    lo = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    hi = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    root = ET.parse(p).getroot()
    for el in root.iter():
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
    div = 1
    for m in root.iter('measure'):
        a = m.find('attributes')
        if a is not None and a.findtext('divisions'):
            div = int(a.findtext('divisions'))
        try:
            num = int(m.get('number'))
        except (TypeError, ValueError):
            continue
        if not (lo <= num <= hi):
            continue
        print('--- m.%d ---' % num)
        # absolute position tracked by backup/forward, plus per-staff cursor
        pos = 0.0
        cursor = {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}
        events = []
        marks = []
        for el in m:
            if el.tag == 'backup':
                d = float(el.findtext('duration')) / div
                pos -= d
                continue
            if el.tag == 'forward':
                d = float(el.findtext('duration')) / div
                pos += d
                continue
            if el.tag == 'direction':
                w = [x.text.strip() for x in el.iter('words') if x.text and x.text.strip()]
                d = [x.tag for x in el.iter('dynamics')]
                o = [x.tag for x in el.iter('ornaments')]
                if w or d or o:
                    marks.append('beat%.2f %s' % (pos + 1, '/'.join(d + w + o)))
                continue
            if el.tag != 'note':
                continue
            st = int(el.findtext('staff') or 1)
            dur = float(el.findtext('duration') or 0) / div
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
            if el.find('chord') is not None:
                onset = events[-1][0] if events else pos
            else:
                onset = pos
                cursor[st] = pos + dur
                pos += dur
                if el.find('grace') is not None:
                    pos -= dur
            events.append((onset, st, label, typ, '.' * len(el.findall('dot')),
                           ','.join(arts), el.find('grace') is not None))
        for st in sorted({e[1] for e in events}):
            row = []
            for e in events:
                if e[1] != st:
                    continue
                board = 'GRACE ' if e[6] else ''
                row.append('%.2f %s%s/%s%s%s' % (e[0] + 1, board, e[2], e[3], e[4],
                                                 ('[' + e[5] + ']') if e[5] else ''))
            print('  staff%d: %s' % (st, ' | '.join(row)))
        if marks:
            print('  marks:', '; '.join(marks))


main()
