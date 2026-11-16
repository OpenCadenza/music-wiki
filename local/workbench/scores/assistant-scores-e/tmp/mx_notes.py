"""Generic MusicXML measure/note dumper for verification work.

Usage:
  python mx_notes.py <file.mxl|.xml> <partIndex1based> <selStart> <selEnd> [--idx|--num]

--idx : selStart/selEnd are absolute 0-based measure indices (default)
--num : selStart/selEnd are the 'number' attributes of measures
"""
import sys, zipfile
import xml.etree.ElementTree as ET

STEP = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def midi(step, alter, octave):
    return 12 * (int(octave) + 1) + STEP[step] + int(alter or 0)


def pname(step, alter, octave):
    m = midi(step, alter, octave)
    return '%s%s=%d' % (NAMES[m % 12], octave, m)


def load(path):
    if path.endswith('.mxl'):
        z = zipfile.ZipFile(path)
        names = [n for n in z.namelist() if n.lower().endswith('.xml') and 'META-INF' not in n]
        data = z.read(names[0])
    else:
        data = open(path, 'rb').read()
    root = ET.fromstring(data)
    for el in root.iter():
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
    return root


def notes_of_measure(m, div):
    out = []
    for el in m:
        if el.tag == 'direction':
            words = [w.text.strip() for w in el.iter('words') if w.text and w.text.strip()]
            dyn = [d.tag for d in el.iter('dynamics')]
            if words or dyn:
                out.append('  <<%s%s>>' % ('/'.join(dyn), (' ' + '|'.join(words)) if words else ''))
        elif el.tag == 'sound':
            pass
        elif el.tag == 'note':
            if el.find('grace') is not None:
                rest = el.find('rest')
                if rest is not None:
                    out.append('  grace REST')
                    continue
                p = el.find('pitch')
                out.append('  grace %s' % pname(p.findtext('step'), p.findtext('alter'),
                                               p.findtext('octave')))
                continue
            dur = el.findtext('duration')
            dur_q = (float(dur) / div) if dur else None
            typ = el.findtext('type') or '?'
            dot = '.' * len(el.findall('dot'))
            staff = el.findtext('staff') or '1'
            voice = el.findtext('voice') or ''
            p = el.find('pitch')
            if p is None:
                nm = 'REST'
            else:
                nm = pname(p.findtext('step'), p.findtext('alter'), p.findtext('octave'))
            tie = ''.join(t.get('type')[0] for t in el.findall('tie'))
            n = el.find('notations')
            arts = []
            if n is not None:
                for a in n:
                    if a.tag in ('slur', 'tied'):
                        arts.append('%s:%s' % (a.tag, a.get('type')[0]))
                    elif a.tag in ('articulations', 'ornaments'):
                        for c in a:
                            arts.append(c.tag)
                    elif a.tag in ('dynamics',):
                        for c in a:
                            arts.append('dyn:' + c.tag)
                    else:
                        arts.append(a.tag)
            chord = 'chord ' if el.find('chord') is not None else ''
            out.append('  %s%s dur=%g %s%s s%s v%s tie=%s %s' % (
                chord, nm, dur_q, typ, dot, staff, voice, tie, ','.join(arts)))
    return out


def main():
    path, part_idx, s, e = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    by_num = '--num' in sys.argv
    root = load(path)
    parts = list(root.iter('part'))
    part = parts[part_idx - 1]
    ms = list(part.iter('measure'))
    print('### part=%s measures=%d' % (part.get('id'), len(ms)))
    div = 1
    for i, m in enumerate(ms):
        attrs = m.find('attributes')
        attrs_info = []
        if attrs is not None:
            d = attrs.findtext('divisions')
            if d:
                div = int(d)
                attrs_info.append('div=%s' % d)
            k = attrs.find('key')
            t = attrs.find('time')
            if k is not None:
                attrs_info.append('fifths=%s' % k.findtext('fifths'))
            if t is not None:
                attrs_info.append('time=%s/%s' % (t.findtext('beats'), t.findtext('beat-type')))
        num = m.get('number')
        if by_num:
            try:
                n = int(num)
            except (TypeError, ValueError):
                continue
            sel = s <= n <= e
        else:
            sel = s <= i <= e
        if not sel:
            continue
        print('--- idx=%d num=%s %s' % (i, num, ' '.join(attrs_info)))
        for line in notes_of_measure(m, div):
            print(line)


if __name__ == '__main__':
    main()
