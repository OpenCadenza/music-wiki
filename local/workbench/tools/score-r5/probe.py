#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick inspector: show which parts actually sound in a measure range."""
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, __file__.rsplit('\\', 1)[0])
from emit import parse_measure, movement_segments, note_type  # noqa


def main():
    path = sys.argv[1]
    lo, hi = int(sys.argv[2]), int(sys.argv[3])
    seg = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    root = ET.parse(path).getroot()
    names = {}
    for sp in root.findall('./part-list/score-part'):
        names[sp.get('id')] = sp.findtext('part-name')
    for part in root.findall('./part'):
        pid = part.get('id')
        measures, nums, segs = movement_segments(part)
        a, b = segs[seg]
        sel = [i for i in range(a, b + 1) if nums[i] is not None and lo <= nums[i] <= hi]
        if not sel:
            print(pid, names.get(pid), 'NO RANGE')
            continue
        total = 0
        preview = []
        for i in sel:
            info, evs, maxpos = parse_measure(measures[i])
            sounding = [e for e in evs if e.kind == 'note']
            total += len(sounding)
            if len(preview) < 8:
                preview.append(midiview(evs))
        print('%-4s %-30s notes=%-5d %s' % (pid, (names.get(pid) or '')[:30], total,
                                            ' ; '.join(preview[:4])))


def midiview(evs):
    out = []
    for e in evs:
        if e.kind == 'rest':
            continue
        nm = e.name + ('' if not e.chord else '+' + '+'.join(e.chord))
        out.append(nm)
        if len(out) >= 8:
            break
    return ','.join(out)


if __name__ == '__main__':
    main()
