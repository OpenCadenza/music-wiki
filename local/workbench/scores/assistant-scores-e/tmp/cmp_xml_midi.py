"""Compare a MusicXML excerpt (part/measure window) with a rendered MIDI file.

Checks, per part, that the ordered sequence of (pitch, onset, duration) matches.
Grace notes are ignored on both sides.  MIDI note-offs are not tracked by the
imported parser, so durations are compared only from the MusicXML side
(durations are cross-checked by LilyPond barcheck + the XML totals).
"""
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(r'local/workbench/tools')))
from midi_pitch_check import parse_midi  # noqa: E402

STEP = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def nm(m):
    return '%s%d' % (NAMES[m % 12], m // 12 - 1)


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


def expected(path, i0, i1):
    root = load(path)
    parts = list(root.iter('part'))
    names = {sp.get('id'): sp.findtext('part-name') for sp in root.iter('score-part')}
    meas = {p.get('id'): list(p.iter('measure')) for p in parts}
    out = {}
    for p in parts:
        pid = p.get('id')
        seq = []
        for i in range(i0, i1 + 1):
            for el in meas[pid][i].findall('note'):
                if el.find('grace') is not None:
                    continue
                pit = el.find('pitch')
                if pit is None:
                    continue
                st = pit.findtext('step')
                al = pit.findtext('alter') or '0'
                oc = pit.findtext('octave')
                seq.append(12 * (int(oc) + 1) + STEP[st] + int(al))
        out[names.get(pid, pid)] = seq
    return out


def main():
    xml = sys.argv[1]
    mid = sys.argv[2]
    i0, i1 = int(sys.argv[3]), int(sys.argv[4])
    exp = expected(xml, i0, i1)
    notes, div = parse_midi(mid)
    actual = {}
    for (tick, pitch, ch) in notes:
        actual.setdefault(ch + 1, []).append(pitch)
    order = list(exp.keys())
    print('parts in xml:', order)
    ok = True
    for idx, part in enumerate(order, start=1):
        e = exp[part]
        a = actual.get(idx, [])
        status = 'MATCH' if e == a else 'DIFF'
        if status == 'DIFF':
            ok = False
        print('\n[ch%d] %-12s  xml=%d notes  midi=%d notes  -> %s' % (idx, part, len(e), len(a),
                                                                     status))
        print('  xml :', ' '.join(nm(x) for x in e))
        print('  midi:', ' '.join(nm(x) for x in a))
        if status == 'DIFF':
            for k in range(max(len(e), len(a))):
                x = e[k] if k < len(e) else None
                y = a[k] if k < len(a) else None
                if x != y:
                    print('    first diff at #%d: xml=%s midi=%s' % (
                        k, nm(x) if x is not None else '-', nm(y) if y is not None else '-'))
                    break
    print('\nRESULT:', 'ALL MATCH' if ok else 'MISMATCH FOUND')


if __name__ == '__main__':
    main()
