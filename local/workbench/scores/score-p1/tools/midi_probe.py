#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""极简 SMF 解析：打印每个 track 的 program change 与 note-on 音高（用于校验 MIDI 实际发音）。"""
import sys
import struct


def parse(path):
    data = open(path, "rb").read()
    assert data[:4] == b"MThd", data[:4]
    hlen = struct.unpack(">I", data[4:8])[0]
    fmt, ntrk, div = struct.unpack(">HHH", data[8:14])
    pos = 8 + hlen
    tracks = []
    for _ in range(ntrk):
        assert data[pos:pos + 4] == b"MTrk"
        ln = struct.unpack(">I", data[pos + 4:pos + 8])[0]
        body = data[pos + 8:pos + 8 + ln]
        pos += 8 + ln
        i = 0
        t = 0
        status = 0
        events = []
        while i < len(body):
            # delta
            d = 0
            while True:
                b = body[i]
                i += 1
                d = (d << 7) | (b & 0x7F)
                if not b & 0x80:
                    break
            t += d
            if i >= len(body):
                break
            b = body[i]
            if b & 0x80:
                status = b
                i += 1
            st = status & 0xF0
            if st in (0x80, 0x90):
                n = body[i]
                v = body[i + 1]
                i += 2
                if st == 0x90 and v > 0:
                    events.append(("on", t, n, v))
                elif st in (0x80,) or (st == 0x90 and v == 0):
                    events.append(("off", t, n, 0))
            elif st in (0xC0, 0xD0):
                events.append(("prog", t, body[i], 0))
                i += 1
            elif st in (0xA0, 0xB0, 0xE0):
                i += 2
            elif status == 0xFF:
                mtype = body[i]
                i += 1
                ln2 = body[i]
                i += 1
                i += ln2
            else:
                i += 1
        tracks.append(events)
    return (fmt, div), tracks


def main():
    path = sys.argv[1]
    meta, tracks = parse(path)
    print("format=%d division=%d tracks=%d" % (meta[0], meta[1], len(tracks)))
    for k, ev in enumerate(tracks):
        progs = [e[2] for e in ev if e[0] == "prog"]
        ons = [e[2] for e in ev if e[0] == "on"]
        pitches = sorted(set(ons))
        print("track %d: prog=%s notes(unique)=%s first=%s" % (
            k, progs, pitches, ons[:8]))


if __name__ == "__main__":
    main()
