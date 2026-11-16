#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minimal SMF parser: dump note-on events: measure, track, ch, midi, name, dur.
Usage: python dump_midi_notes.py <file.mid> [start_measure] [end_measure]"""
import sys

def rd_vlq(buf, pos):
    v = 0
    while True:
        b = buf[pos]; pos += 1
        v = (v << 7) | (b & 0x7F)
        if not (b & 0x80):
            return v, pos

def u16(b):
    return int.from_bytes(b, 'big')

def main(path, m0, m1):
    with open(path, 'rb') as f:
        data = f.read()
    assert data[:4] == b'MThd', data[:4]
    ntrks = u16(data[10:12])
    ppq = u16(data[12:14])
    pos = 14
    tracks = []
    for _ in range(ntrks):
        assert data[pos:pos+4] == b'MTrk'
        ln = u16(data[pos+4:pos+8])
        tracks.append(data[pos+8:pos+8+ln])
        pos += 8 + ln

    notes = []
    for ti, trk in enumerate(tracks):
        p = 0
        tick = 0
        pend = {}
        running = {}
        while p < len(trk):
            d, p = rd_vlq(trk, p)
            tick += d
            st = trk[p]; p += 1
            if st == 0xFF:
                p += 1
                ln, p = rd_vlq(trk, p)
                p += ln
                continue
            if st in (0xF0, 0xF7):
                ln, p = rd_vlq(trk, p)
                p += ln
                continue
            ch = st & 0x0F
            if st & 0x80:
                status = st
            else:
                status = running.get(ch, 0)
                p -= 1
            kind = status & 0xF0
            if kind == 0x90:
                note = trk[p]; vel = trk[p+1]; p += 2
                running[ch] = status
                if vel > 0:
                    pend[(ch, note)] = tick
                elif (ch, note) in pend:
                    on = pend.pop((ch, note))
                    notes.append((on, ti, ch, note, tick - on))
            elif kind == 0x80:
                note = trk[p]; p += 2
                running[ch] = status
                if (ch, note) in pend:
                    on = pend.pop((ch, note))
                    notes.append((on, ti, ch, note, tick - on))
            elif kind == 0xB0:
                p += 2; running[ch] = status
            elif kind == 0xC0:
                p += 1; running[ch] = status
            elif kind == 0xE0:
                p += 2; running[ch] = status
            elif kind == 0xD0:
                p += 1; running[ch] = status
            else:
                p += 1
        for (ch, note), on in pend.items():
            notes.append((on, ti, ch, note, tick - on))

    notes.sort(key=lambda n: (n[0], n[1], n[3]))
    names = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    for (on, ti, ch, note, dur) in notes:
        beat = on / ppq
        meas = int(beat // 4)
        if not (m0 <= meas + 1 <= m1):
            continue
        beat_in = beat - meas * 4
        sub = int(beat_in * 4) + 1
        nm = f"{names[note % 12]}{note // 12 - 1}"
        q = dur / ppq
        ds = f"{q:g}q" if abs(q - round(q)) < 1e-6 else f"{q:.2f}q"
        print(f"m{meas+1:>4}.{sub:<3} trk{ti} ch{ch+1} {note:>3} {nm:<5} dur {ds}")

if __name__ == '__main__':
    path = sys.argv[1]
    m0 = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    m1 = int(sys.argv[3]) if len(sys.argv) > 3 else m0
    main(path, m0, m1)