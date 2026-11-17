#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract per-voice notes within a bar range from a LilyPond-generated MIDI,
converting ticks to (bar, position-in-bar, pitch, duration-beats).

Usage: python extract_midi_bars.py <mid> <ppq_quarters_per_bar> <partial_quarters> <bar0> <bar1>
  e.g. 3/8 meter -> quarters_per_bar = 1.5 ; partial = 0.5 (eighth note anacrusis)
Bars are 1-based; bar0/bar1 inclusive. Outputs one line per note:
  trk<track> bar<bar> @<pos_in_bar_quarters> p<pitch> dur<quarters>
"""
import sys
import struct


def vlq(buf, i):
    v = 0
    while True:
        b = buf[i]
        i += 1
        v = (v << 7) | (b & 0x7F)
        if not (b & 0x80):
            return v, i


def parse(path):
    data = open(path, 'rb').read()
    assert data[:4] == b'MThd', 'not MIDI'
    ntrks = struct.unpack('>H', data[10:12])[0]
    div = struct.unpack('>H', data[12:14])[0]
    ppq = div & 0x7FFF
    idx = 14
    tracks = []
    for _ in range(ntrks):
        assert data[idx:idx + 4] == b'MTrk', 'bad track'
        ln = struct.unpack('>I', data[idx + 4:idx + 8])[0]
        tracks.append(data[idx + 8: idx + 8 + ln])
        idx += 8 + ln
    events = []  # (track_index, tick_on, pitch, tick_off)
    for ti, tdata in enumerate(tracks):
        i = 0
        tick = 0
        run = None
        pending = []  # (pitch, tick_on)
        while i < len(tdata):
            delta, i = vlq(tdata, i)
            tick += delta
            if i >= len(tdata):
                break
            st = tdata[i]
            if st == 0xFF:
                i += 1; i += 1
                ln, i = vlq(tdata, i); i += ln; run = None; continue
            if st in (0xF0, 0xF7):
                i += 1; ln, i = vlq(tdata, i); i += ln; run = None; continue
            if st & 0x80:
                i += 1; run = st
            else:
                st = run
            kind = st & 0xF0
            if kind in (0x80, 0x90):
                pitch = tdata[i]; vel = tdata[i + 1]; i += 2
                if kind == 0x90 and vel > 0:
                    pending.append((pitch, tick))
                else:
                    for k in range(len(pending) - 1, -1, -1):
                        if pending[k][0] == pitch:
                            _, on = pending.pop(k)
                            events.append((ti, on, pitch, tick))
                            break
            elif kind in (0xA0, 0xB0, 0xE0):
                i += 2
            elif kind in (0xC0, 0xD0):
                i += 1
            else:
                break
        for pitch, on in pending:  # unterminated
            events.append((ti, on, pitch, tick))
    return events, ppq


def name(p):
    N = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return f"{N[p % 12]}{p // 12 - 1}"


def main():
    mid = sys.argv[1]
    qpb = float(sys.argv[2])      # quarter beats per bar
    partial = float(sys.argv[3])  # anacrusis length in quarters
    b0 = int(sys.argv[4])
    b1 = int(sys.argv[5])
    events, ppq = parse(mid)
    # m.1 starts after the anacrusis (partial) of `partial` quarter beats.
    m1_start = partial * ppq
    start_tick = m1_start + (b0 - 1) * qpb * ppq
    end_tick = m1_start + b1 * qpb * ppq
    sel = [e for e in events if start_tick - 1 <= e[1] < end_tick - 1 and e[2] >= 0]
    # sort by track then tick
    sel.sort(key=lambda e: (e[0], e[1], e[2]))
    # group by track
    by_trk = {}
    for ti, on, p, off in sel:
        by_trk.setdefault(ti, []).append((on, p, off))
    print(f"# {mid}  ppq={ppq}  bars {b0}-{b1}  (quarterbeats per bar={qpb}, partial={partial})")
    for ti in sorted(by_trk):
        print(f"## track {ti} (midi ch {ti + 1})")
        for on, p, off in by_trk[ti]:
            rel = (on - m1_start) / ppq
            bar = int(rel // qpb) + 1
            pos = rel - (bar - 1) * qpb
            dur = (off - on) / ppq
            print(f"  bar{bar:>2} @{pos:>4.2f} {name(p):>4}({p}) dur={dur:.2f}")


if __name__ == "__main__":
    main()
