"""Dump MusicXML measures (absolute index range) for all parts, with duration totals."""
import sys, zipfile
import xml.etree.ElementTree as ET

STEP = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def pn(step, alter, oct):
    m = 12 * (int(oct) + 1) + STEP[step] + int(alter or 0)
    return '%s%s' % (NAMES[m % 12], oct)


def load(path):
    if path.endswith('.mxl'):
        z = zipfile.ZipFile(path)
        n = [x for x in z.namelist() if x.lower().endswith('.xml') and 'META-INF' not in x]
        data = z.read(n[0])
    else:
        data = open(path, 'rb').read()
    r = ET.fromstring(data)
    for el in r.iter():
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
    return r


def main():
    path = sys.argv[1]
    i0, i1 = int(sys.argv[2]), int(sys.argv[3])
    root = load(path)
    parts = list(root.iter('part'))
    names = {}
    for sp in root.iter('score-part'):
        names[sp.get('id')] = sp.findtext('part-name')
    # measure windows
    meas = {p.get('id'): list(p.iter('measure')) for p in parts}
    order = [p.get('id') for p in parts]
    div = 1
    for i in range(i0, i1 + 1):
        anym = meas[order[0]][i]
        a = anym.find('attributes')
        if a is not None and a.findtext('divisions'):
            div = int(a.findtext('divisions'))
        print('================ idx=%d num=%s ================' % (i, anym.get('number')))
        for pid in order:
            m = meas[pid][i]
            tot = 0.0
            lines = []
            for el in m:
                if el.tag == 'note':
                    if el.find('grace') is not None:
                        p = el.find('pitch')
                        lines.append('(g %s)' % pn(p.findtext('step'), p.findtext('alter'),
                                                   p.findtext('octave')))
                        continue
                    d = el.findtext('duration')
                    q = (float(d) / div) if d else 0
                    tot += q
                    p = el.find('pitch')
                    nm = pn(p.findtext('step'), p.findtext('alter'),
                            p.findtext('octave')) if p is not None else 'R'
                    t = el.findtext('type') or '?'
                    ty = el.findall('tie')
                    arts = []
                    no = el.find('notations')
                    if no is not None:
                        for c in no:
                            if c.tag in ('slur', 'tied'):
                                arts.append('%s%s' % (c.tag[:2], c.get('type')[0]))
                            elif c.tag in ('articulations', 'ornaments'):
                                for g in c:
                                    arts.append(g.tag)
                    lines.append('%s/%s%s%s' % (nm, t, '.' * len(el.findall('dot')),
                                                ('[' + ','.join(arts) + ']') if arts else ''))
                elif el.tag == 'direction':
                    w = [x.text.strip() for x in el.iter('words') if x.text and x.text.strip()]
                    dy = [x.tag for x in el.iter('dynamics')]
                    if w or dy:
                        lines.append('{%s%s}' % ('/'.join(dy), ' '.join(w)))
            print('  %-12s tot=%g : %s' % (names.get(pid, pid), tot, ' '.join(lines)))


if __name__ == '__main__':
    main()
