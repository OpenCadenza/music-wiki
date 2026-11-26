#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cross-check a compiled LilyPond excerpt's MIDI pitches against the kern model.

Usage: python verify_midi.py <spec.json> <compiled.mid>

Compares, per staff, the *set* of sounding pitches (kern model vs MIDI tracks),
plus the per-measure pitch sets.  Sets are used because LilyPond's MIDI merges
tied notes and unison doublings, which changes note counts but not pitch content.
"""
import json
import os
import struct
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kern2ly


def read_midi(path):
    data = open(path, 'rb').read()
    assert data[:4] == b'MThd'
    div = struct.unpack('>H', data[12:14])[0] & 0x7FFF
    ntrks = struct.unpack('>H', data[10:12])[0]
    pos = 14
    tracks = []
    for _ in range(ntrks):
        assert data[pos:pos + 4] == b'MTrk'
        ln = struct.unpack('>I', data[pos + 4:pos + 8])[0]
        tracks.append(data[pos + 8:pos + 8 + ln])
        pos += 8 + ln
    notes = []
    end_tick = 0
    for ti, tr in enumerate(tracks):
        i, tick, status = 0, 0, None
        while i < len(tr):
            v = 0
            while True:
                b = tr[i]
                i += 1
                v = (v << 7) | (b & 0x7F)
                if not b & 0x80:
                    break
            tick += v
            end_tick = max(end_tick, tick)
            if i >= len(tr):
                break
            b = tr[i]
            i += 1
            if b == 0xFF:
                meta = tr[i]
                i += 1
                ln2 = tr[i]
                i += 1
                i += ln2
                continue
            if b in (0xF0, 0xF7):
                ln2 = tr[i]
                i += 1
                i += ln2
                continue
            if b & 0x80:
                status = b
            else:
                i -= 1
            kind = status & 0xF0
            if kind in (0xC0, 0xD0):
                i += 1
                continue
            d1, d2 = tr[i], tr[i + 1]
            i += 2
            if kind == 0x90 and d2 > 0:
                notes.append((ti, tick, d1))
    return div, notes, end_tick


def main():
    spec = json.load(open(sys.argv[1], encoding='utf-8'))
    mid = sys.argv[2]
    piece = kern2ly.load(spec['kern'])
    s0, s1 = kern2ly.resolve_range(piece, spec['from'], spec['to'])
    # measure boundaries in quarter notes
    starts, acc = {}, Fraction(0)
    for seq in range(s0, s1 + 1):
        starts[seq] = acc
        acc += piece['len'].get(seq) * 4
    total_q = acc
    # expected per staff: (measure pitch set, excerpt pitch set)
    exp = []
    grace_pitches = set()
    for st in spec['staves']:
        staff_no = st['staff']
        per_measure = {}
        allp = set()
        for seq in range(s0, s1 + 1):
            pm = per_measure.setdefault(seq, set())
            for vid, evs in piece['measures'].get(seq, {}).get(staff_no, {}).items():
                for e in evs:
                    for g in e.grace:
                        for n in g['notes']:
                            pm.add(n['midi'])
                            allp.add(n['midi'])
                            grace_pitches.add(n['midi'])
                    if e.kind != 'note':
                        continue
                    for n in e.notes:
                        pm.add(n['midi'])
                        allp.add(n['midi'])
        exp.append({'label': st.get('label', st['var']), 'pm': per_measure,
                    'all': allp})
    div, notes, max_tick = read_midi(mid)
    tracks = {}
    for ti, tick, pitch in notes:
        tracks.setdefault(ti, []).append((tick, pitch))
    # LilyPond's MIDI division may be per quarter or per whole note; calibrate
    # the tick<->quarter mapping against the excerpt's total length.
    scale = (max_tick / (div * float(total_q))) if total_q else 1.0
    act = []
    for ti in sorted(tracks):
        pm = {}
        for tick, pitch in tracks[ti]:
            q = tick / (div * scale) if scale else tick / div
            seq = None
            for s in range(s0, s1 + 1):
                if starts[s] <= q < starts.get(s + 1, total_q):
                    seq = s
                    break
            if seq is None:
                seq = s1
            pm.setdefault(seq, set()).add(pitch)
        act.append({'label': 'track%d' % ti, 'pm': pm,
                    'all': set(p for _, p in tracks[ti])})
    # match actual tracks to expected staves greedily by pitch-set overlap
    unused = list(range(len(act)))
    pairs = []
    for e in exp:
        best, bestscore = None, -1
        for ai in unused:
            score = len(e['all'] & act[ai]['all']) - len(act[ai]['all'] - e['all'])
            if score > bestscore:
                best, bestscore = ai, score
        if best is not None and bestscore >= 0:
            unused.remove(best)
            pairs.append((e, act[best]))
    print('%s: %d staves, %d MIDI tracks with notes'
          % (os.path.basename(mid), len(exp), len(act)))
    ok = True
    for e, a in pairs:
        only_exp = sorted(e['all'] - a['all'])
        only_act = sorted(a['all'] - e['all'])
        bad = bool(only_exp or only_act)
        ok = ok and not bad
        print('  %-6s pitches %d/%d  %s'
              % (e['label'], len(e['all']), len(a['all']),
                 'OK' if not bad else 'MISMATCH'))
        if bad:
            print('    only in kern :', only_exp[:12])
            print('    only in MIDI :', only_act[:12])
        # per-measure sets (ignore one-measure boundary spill of grace notes)
        for seq in sorted(e['pm']):
            de = (e['pm'][seq] - a['pm'].get(seq, set())) - grace_pitches
            da = (a['pm'].get(seq, set()) - e['pm'][seq]) - grace_pitches
            if de or da:
                nxt = e['pm'].get(seq + 1, set())
                if da and not de and da <= nxt:
                    continue
                ok = False
                print('    %-8s m.%s: kern-only %s midi-only %s'
                      % (e['label'], kern2ly.fmt_seq(piece, seq),
                         sorted(de), sorted(da)))
    print('RESULT', 'OK' if ok else 'MISMATCH')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
