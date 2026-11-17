#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""dump_notes.py —— 按时间顺序落列 MIDI 全部音符（用于核对快照与逐音比对）

用法：python dump_notes.py <file.mid> [track_index]
输出：序号  音名(MIDI)  起始 tick  时长 tick
"""
import sys
import struct

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def name(p):
    return f"{NOTE_NAMES[p % 12]}{p // 12 - 1}"


def vlq(buf, i):
    v = 0
    while True:
        b = buf[i]
        i += 1
        v = (v << 7) | (b & 0x7F)
        if not b & 0x80:
            return v, i


def parse(path):
    data = open(path, "rb").read()
    assert data[:4] == b"MThd", "not MIDI"
    ntrks = struct.unpack(">H", data[10:12])[0]
    div = struct.unpack(">H", data[12:14])[0]
    ppq = div & 0x7FFF
    idx = 14
    tracks = []
    for _ in range(ntrks):
        assert data[idx:idx + 4] == b"MTrk", "bad track"
        ln = struct.unpack(">I", data[idx + 4:idx + 8])[0]
        tracks.append(data[idx + 8: idx + 8 + ln])
        idx += 8 + ln
    events = []
    for ti, tdata in enumerate(tracks):
        i = 0
        tick = 0
        run = None
        pending = []
        while i < len(tdata):
            delta, i = vlq(tdata, i)
            tick += delta
            if i >= len(tdata):
                break
            st = tdata[i]
            if st == 0xFF:
                i += 1
                i += 1
                ln, i = vlq(tdata, i)
                i += ln
                run = None
                continue
            if st in (0xF0, 0xF7):
                i += 1
                ln, i = vlq(tdata, i)
                i += ln
                run = None
                continue
            if st & 0x80:
                i += 1
                run = st
            else:
                st = run
            kind = st & 0xF0
            if kind in (0x80, 0x90):
                pitch = tdata[i]
                vel = tdata[i + 1]
                i += 2
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
        for pitch, on in pending:
            events.append((ti, on, pitch, tick))
    return events, ppq


def main():
    mid = sys.argv[1]
    trk = int(sys.argv[2]) if len(sys.argv) > 2 else None
    events, ppq = parse(mid)
    events.sort(key=lambda e: (e[0], e[1], e[2]))
    print(f"# {mid}  ppq={ppq}  notes={len(events)}")
    n = 0
    for ti, on, p, off in events:
        if trk is not None and ti != trk:
            continue
        n += 1
        print(f"{n:>3}  trk{ti}  {name(p):>4}({p:>3})  on={on:>6}  dur={off - on:>5}")


if __name__ == "__main__":
    main()