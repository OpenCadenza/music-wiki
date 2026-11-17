"""Compare a .ly excerpt against the corresponding passage of a MusicXML score.

Locates the movement by a marker string, then compares, per measure and per
part, the pitch multiset (with durations) against the .ly voice variables.

usage: python cmp_xml.py <score.xml> <marker> <excerpt.ly> <mapJSON> <nMeasures>
mapJSON: {"1": ["violinOne"], "2": ["violinTwo"], ...}  (part index 1-based)
"""
import sys, os, json, collections
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cmp_staff as C

NAME = C.NAME


def nm(p):
    return '%s%d' % (NAME[int(p) % 12], int(p) // 12 - 1)


def find_marker(score, marker):
    """return index (within part elements) of the measure holding `marker`."""
    root = ET.parse(score).getroot()
    parts = root.findall('part')
    p0 = parts[0]
    for i, meas in enumerate(p0.findall('measure')):
        txt = ''.join(t.text or '' for t in meas.iter())
        if marker.lower() in txt.lower():
            return i, meas.get('number')
    return None, None


def read_part(score, part_index, start, count):
    """events per measure from part `part_index` (1-based), starting at start."""
    root = ET.parse(score).getroot()
    parts = root.findall('part')
    part = parts[part_index - 1]
    meas_list = part.findall('measure')
    divisions = 1
    out = []
    for meas in meas_list[start:start + count]:
        # inherit divisions/key/time from preceding measures
        for a in meas.findall('attributes'):
            d = a.find('divisions')
            if d is not None:
                divisions = int(d.text)
        ev = []
        cursor = 0.0
        for el in meas:
            if el.tag == 'attributes':
                d = el.find('divisions')
                if d is not None:
                    divisions = int(d.text)
            elif el.tag == 'backup':
                cursor -= float(el.findtext('duration', '0')) / divisions
            elif el.tag == 'forward':
                cursor += float(el.findtext('duration', '0')) / divisions
            elif el.tag == 'note':
                dur = float(el.findtext('duration', '0')) / divisions
                if el.find('grace') is not None:
                    continue
                if el.find('chord') is None:
                    onset = cursor
                    cursor += dur
                else:
                    onset = cursor - dur
                rest = el.find('rest') is not None
                if rest:
                    continue
                st = el.find('pitch/step')
                if st is None:
                    continue
                alt = el.find('pitch/alter')
                oc = el.find('pitch/octave')
                semis = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}[st.text]
                midi = (int(oc.text) + 1) * 12 + semis + (
                    int(round(float(alt.text))) if alt is not None and alt.text else 0)
                ev.append((onset, midi, dur / 4.0))
        out.append(ev)
    return out


def main():
    score, marker, ly, smap, count = (sys.argv[1], sys.argv[2], sys.argv[3],
                                     json.loads(sys.argv[4]), int(sys.argv[5]))
    idx, num = find_marker(score, marker)
    print('marker %r -> measure index %s (number %s)\n' % (marker, idx, num))
    if idx is None:
        return
    start = int(sys.argv[6]) if len(sys.argv) > 6 else idx
    text = open(ly, encoding='utf-8').read()
    C.detect_key(text)
    blocks = C.split_vars(text)
    ly_meas = {k: C.parse_block(v) for k, v in blocks.items()}
    for pk, vars_ in smap.items():
        pi = int(pk)
        src = read_part(score, pi, start, count)
        comb = {}
        for v in vars_:
            for n, mv in enumerate(ly_meas.get(v, []), 1):
                comb.setdefault(n, []).extend(mv)
        for n in range(1, count + 1):
            a = C.expansions(comb.get(n, []))
            b = [(m, d) for (_, m, d) in src[n - 1]] if n - 1 < len(src) else []
            A = collections.Counter(a); B = collections.Counter(b)
            SA = set(x for x, _ in a); SB = set(x for x, _ in b)
            if A == B:
                print('[OK  ] part%d m%d' % (pi, n))
                continue
            flag = 'SET!' if SA != SB else 'DUR!'
            print('[%s] part%d m%d  ly=%g xml=%g' % (flag, pi, n,
                  sum(d for _, d in a), sum(d for _, d in b)))
            if SA != SB:
                if SB - SA:
                    print('      xml-only: ' + ', '.join(nm(x) for x in sorted(SB - SA)))
                if SA - SB:
                    print('      ly-only : ' + ', '.join(nm(x) for x in sorted(SA - SB)))
            else:
                if B - A: print('      xml dur: ' + ', '.join(f'{nm(p)}/{d:g}' for p, d in sorted((B - A).elements())))
                if A - B: print('      ly  dur: ' + ', '.join(f'{nm(p)}/{d:g}' for p, d in sorted((A - B).elements())))


if __name__ == '__main__':
    main()
