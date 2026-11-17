#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Use MIDI time-signature meta events to locate movement IV (2/4) in the
musicxml2ly output of Mozart K.465, then dump per-track notes for mm.10-16."""
import struct
import sys


def vlq(buf, i):
    v = 0
    while True:
        b = buf[i]; i += 1
        v = (v << 7) | (b & 0x7F)
        if not (b & 0x80):
            return v, i


def parse(path):
    data = open(path, 'rb').read()
    assert data[:4] == b'MThd'
    ntrks = struct.unpack('>H', data[10:12])[0]
    div = struct.unpack('>H', data[12:14])[0]
    ppq = div & 0x7FFF
    idx = 14
    tracks = []
    for _ in range(ntrks):
        ln = struct.unpack('>I', data[idx + 4:idx + 8])[0]
        tracks.append(data[idx + 8: idx + 8 + ln])
        idx += 8 + ln
    # gather events from all tracks (time sig metas + notes with durations)
    timesig = []   # (tick, num, den)
    notes = []     # (tick, track, pitch, off_tick)
    for ti, td in enumerate(tracks):
        i = 0; tick = 0; run = None
        pending = []
        while i < len(td):
            delta, i = vlq(td, i)
            tick += delta
            if i >= len(td):
                break
            st = td[i]
            if st == 0xFF:
                mtype = td[i + 1]
                i += 2
                ln, i = vlq(td, i)
                payload = td[i:i + ln]
                i += ln
                if mtype == 0x58 and len(payload) >= 2:
                    timesig.append((tick, payload[0], 2 ** payload[1]))
                run = None
                continue
            if st in (0xF0, 0xF7):
                i += 1; ln, i = vlq(td, i); i += ln; run = None; continue
            if st & 0x80:
                i += 1; run = st
            else:
                st = run
            kind = st & 0xF0
            if kind in (0x80, 0x90):
                pitch = td[i]; vel = td[i + 1]; i += 2
                if kind == 0x90 and vel > 0:
                    pending.append((pitch, tick))
                else:
                    for k in range(len(pending) - 1, -1, -1):
                        if pending[k][0] == pitch:
                            _, on = pending.pop(k)
                            notes.append((on, ti, pitch, tick))
                            break
            elif kind in (0xA0, 0xB0, 0xE0):
                i += 2
            elif kind in (0xC0, 0xD0):
                i += 1
            else:
                break
        for pitch, on in pending:
            notes.append((on, ti, pitch, tick))
    return ppq, timesig, notes


def main():
    path = sys.argv[1]
    ppq, timesig, notes = parse(path)
    timesig.sort()
    print("ppq", ppq, "timesigs (tick, num, den):")
    for t in timesig[:20]:
        print("  ", t)
    # movement IV = first 2/4 signature after the beginning
    m4 = None
    for (tick, num, den) in timesig:
        if num == 2 and den == 4:
            m4 = tick
            break
    if m4 is None:
        sys.exit("no 2/4 time signature found")
    print("movement IV starts at tick", m4, "=", m4 / ppq, "quarters")
    # 2/4 bar = 2 quarters; m.10 starts at m4 + 9*2 quarters; m.16 ends at m4+16*2
    start = m4 + 9 * 2 * ppq
    end = m4 + 16 * 2 * ppq
    sel = [(t, ti, p, off) for (t, ti, p, off) in notes if start - 1 <= t < end]
    sel.sort()
    N = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    print("notes in mm.10-16:")
    for (t, ti, p, off) in sel:
        rel = (t - start) / ppq
        bar = int(rel // 2) + 10
        pos = rel - (bar - 10) * 2
        dur = (off - t) / ppq
        print(f"  trk{ti} bar{bar:>2} @{pos:>4.2f} {N[p % 12]}{p // 12 - 1}({p}) dur={dur:.2f}")


if __name__ == "__main__":
    main()
