# -*- coding: utf-8 -*-
"""最小 MIDI 解析 + 与 MusicXML 的逐小节音高比对。"""
import struct, os, sys
from lxml import etree
from collections import defaultdict

MID = r"schubert-d929-mvt2-mm1-21.mid"
XML = r"src\src3_98865.xml"

def read_vlq(b, i):
    v = 0
    while True:
        c = b[i]; i += 1
        v = (v << 7) | (c & 0x7F)
        if not (c & 0x80): break
    return v, i

def parse_midi(path):
    d = open(path, 'rb').read()
    assert d[:4] == b'MThd'
    hlen = struct.unpack('>I', d[4:8])[0]
    fmt, ntrk, div = struct.unpack('>HHH', d[8:14])
    i = 8 + hlen
    tracks = []
    while i < len(d) and len(tracks) < ntrk:
        assert d[i:i+4] == b'MTrk', d[i:i+4]
        tlen = struct.unpack('>I', d[i+4:i+8])[0]
        body = d[i+8:i+8+tlen]
        i += 8 + tlen
        evs = []
        j = 0; t = 0; status = None
        while j < len(body):
            dt, j = read_vlq(body, j)
            t += dt
            b0 = body[j]
            if b0 & 0x80:
                status = b0; j += 1
            if status == 0xFF:
                meta = body[j]; j += 1
                ln, j = read_vlq(body, j)
                data = body[j:j+ln]; j += ln
                evs.append((t, 'meta', meta, data))
            elif status in (0xF0, 0xF7):
                ln, j = read_vlq(body, j); j += ln
            else:
                hi = status & 0xF0
                n = 2 if hi in (0x80, 0x90, 0xA0, 0xB0, 0xE0) else 1
                args = body[j:j+n]; j += n
                evs.append((t, 'chan', status, bytes(args)))
        tracks.append(evs)
    return fmt, ntrk, div, tracks

fmt, ntrk, div, tracks = parse_midi(MID)
print(f"MIDI: format={fmt} tracks={ntrk} division={div} (ticks per whole note)")

TPB = 2 * div    # MIDI division = ticks per quarter; 2/4 bar = 2 quarters
print(f"ticks per 2/4 bar = {TPB}")

info = []
for ti, evs in enumerate(tracks):
    prog = None; names = []
    notes = []
    for t, kind, a, b in evs:
        if kind == 'chan':
            hi = a & 0xF0
            if hi == 0xC0: prog = b[0]
            elif hi == 0x90 and b[1] > 0: notes.append((t, b[0]))
        else:
            if a == 0x03: names.append(b.decode('latin1'))
            if a == 0x04: names.append(b.decode('latin1'))
    info.append((ti, prog, names, notes))
    print(f"  track {ti}: program={prog} names={names} note-on count={len(notes)} "
          f"range={min(n for _,n in notes) if notes else '-'}..{max(n for _,n in notes) if notes else '-'}")

# ---- 期望值（来自 XML，主源 B）----
root = etree.parse(XML).getroot()
PITCH = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
def xmidi(step, alter, octv):
    return PITCH[step] + int(alter or 0) + (int(octv) + 1) * 12

def expected(pid, m0, m1):
    sp = root.find(f"./part[@id='{pid}']")
    out = {}
    for mm in sp.findall('./measure')[m0-1:m1]:
        t = mm.get('number')
        pitches = []
        for n in mm.findall('./note'):
            if n.find('./chord') is not None:
                continue  # chord 后随音符，单独处理
            # 收集整个 chord 组
            grp = [n]
            pitches_here = []
            p = n.find('./pitch')
            if p is not None:
                pitches_here.append(xmidi(p.findtext('step'), p.findtext('alter'), p.findtext('octave')))
            # 后续 chord 音符
            sibs = n.itersiblings()
            for s in n.itersiblings():
                if s.tag != 'note': break
                if s.find('./chord') is None: break
                q = s.find('./pitch')
                if q is not None:
                    pitches_here.append(xmidi(q.findtext('step'), q.findtext('alter'), q.findtext('octave')))
            tie = n.find('./tie')
            if tie is not None and tie.get('type') == 'stop':
                continue
            pitches.extend(pitches_here)
        out[t] = sorted(pitches)
    return out

def actual(track_notes, m0, m1):
    out = defaultdict(list)
    for t, n in track_notes:
        bar = t // TPB
        meas = bar + 1
        if m0 <= meas <= m1:
            out[str(meas)].append(n)
    return {k: sorted(v) for k, v in out.items()}

pairs = [('P1', 1), ('P2', 2), ('P3', 3), ('P4', 4)]
ok = True
for pid, ti in pairs:
    exp = expected(pid, 1, 21)
    act = actual(info[ti][3], 1, 21)
    bad = []
    for m in [str(k) for k in range(1, 22)]:
        e = exp.get(m, []); a = act.get(m, [])
        if e != a:
            bad.append((m, e, a))
    print(f"\n{pid} (track {ti}): " + ("一致" if not bad else f"{len(bad)} 小节不一致"))
    for m, e, a in bad:
        print(f"   m{m}: XML={e}")
        print(f"        MIDI={a}")
    if bad: ok = False
print("\n总判定:", "全部一致" if ok else "存在差异")

