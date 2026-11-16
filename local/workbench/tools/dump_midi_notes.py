#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minimal SMF parser: dump note-on events as (measure.beat, track, ch, midi, name, dur_ticks).
Usage: python dump_midi_notes.py <file.mid> [start_measure] [end_measure]"""
import sys, struct

def rd_vlq(f):
    v = 0
    while True:
        b = f.read(1)[0]
        v = (v << 7) | (b & 0x7F)
        if not (b & 0x80):
            return v

def main(path, m0, m1):
    with open(path, 'rb') as f:
        head = f.read(14)
        assert head[:4] == b'MThd'
        ntrks = struct.unpack('>HHH', head[8:14])[1]
        div = struct.unpack('>H', head[12:14])[0]
        ppq = div & 0x7FFF
    tracks = []
    with open(path, 'rb') as f:
        f.seek(14)
        for ti in range(ntrks):
            hdr = f.read(8)
            assert hdr[:4] == b'MTrk', hdr
            ln = struct.unpack('>I', hdr[4:8])[0]
            data = f.read(ln)
            tracks.append(data)
    # parse events
    notes = []  # (tick, track, ch, note, vel, dur, on_tick)
    for ti, data in enumerate(tracks):
        pos = 0
        tick = 0
        pend = {}  # (ch,note) -> on_tick
        while pos < len(data):
            delta = rd_vlq(data.__class__(data[pos:]) and __import__('io').BytesIO(data[pos:]))
            # re-read properly:
            j = pos
            v = 0
            while True:
                b = data[j]; j += 1
                v = (v << 7) | (b & 0x7F)
                if not (b & 0x80): break
            delta = v
            pos = j
            tick += delta
            st = data[pos]; pos += 1
            if st == 0xFF:
                typ = data[pos]; pos += 1
                ln = rd_vlq(__import__('io').BytesIO(data[pos:])); 
                j = pos; v = 0
                while True:
                    b = data[j]; j += 1
                    v = (v << 7) | (b & 0x7F)
                    if not (b & 0x80): break
                ln = v; pos = j
                pos += ln
                continue
            if st == 0xF0 or st == 0xF7:
                j = pos; v = 0
                while True:
                    b = data[j]; j += 1
                    v = (v << 7) | (b & 0x7F)
                    if not (b & 0x80): break
                pos = j + v
                continue
            ch = st & 0x0F
            if st & 0x80:
                status = st
            else:
                status = running.get(ch, 0)
                pos -= 1
            running = running if 'running' in dir() else {}
            if (st & 0xF0) == 0x90:
                note = data[pos]; vel = data[pos+1]; pos += 2
                running[ch] = st
                if vel > 0:
                    pend[(ch, note)] = tick
                elif (ch, note) in pend:
                    on = pend.pop((ch, note))
                    notes.append((on, ti, ch, note, 0, tick - on))
            elif (st & 0xF0) == 0x80:
                note = data[pos]; pos += 2
                running[ch] = st
                if (ch, note) in pend:
                    on = pend.pop((ch, note))
                    notes.append((on, ti, ch, note, 0, tick - on))
            elif (st & 0xF0) == 0xB0:
                pos += 2
                running[ch] = st
            elif (st & 0xF0) == 0xC0:
                pos += 1
                running[ch] = st
            elif (st & 0xF0) == 0xE0:
                pos += 2
                running[ch] = st
            elif (st & 0xF0) == 0xD0:
                pos += 1
                running[ch] = st
            else:
                pos += 1
    notes.sort(key=lambda n: n[0])
    names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    for (on, ti, ch, note, vel, dur) in notes:
        beat = on / ppq
        meas = int(beat // 4)
        if m0 <= meas <= m1:
            beat_in = beat - meas * 4
            b = int(beat_in)
            frac = beat_in - b
            pos_str = f"{meas+1}.{b+1}" if frac == 0 else f"{meas+1}.{b+1:02d}"
            nm = f"{names[note % 12]}{note // 12 - 1}"
            print(f"m{meas+1:>4}.{int(beat_in*4)+1:<3} trk{ti} ch{ch+1} {note:>3} {nm:<4} dur{round(dur/ppq*4,1)}")

if __name__ == '__main__':
    path = sys.argv[1]
    m0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    m1 = int(sys.argv[3]) if len(sys.argv) > 3 else m0
    main(path, m0, m1)