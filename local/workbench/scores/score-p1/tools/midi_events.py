#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把两份 MIDI 展开成「十六分音位事件表」，用于逐音比对（不再只看前 8 个 note-on）。

事件 = (小节号, 小节内十六分位, 音高, 时值[十六分单位])。

用法：python midi_events.py <file.mid> [--quarters-per-bar N]
"""
import struct
import sys


def parse_smf(path):
    data = open(path, "rb").read()
    assert data[:4] == b"MThd"
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
        evs = []
        while i < len(body):
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
                    evs.append(("on", t, n))
                else:
                    evs.append(("off", t, n))
            elif st in (0xC0, 0xD0):
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
        tracks.append(evs)
    return fmt, div, tracks


def main():
    path = sys.argv[1]
    qpb = 4.0
    fmt, div, tracks = parse_smf(path)
    sixteenth = div / 4.0     # tick 数 / 十六分音符
    events = []
    for evs in tracks:
        on = {}
        for kind, t, n in evs:
            if kind == "on":
                on.setdefault(n, []).append(t)
            else:
                if on.get(n):
                    t0 = on[n].pop(0)
                    events.append((t0, n, t - t0))
    events.sort()
    if not events:
        print("no notes")
        return
    t0 = events[0][0]
    print("# %s  division=%d  十六分/小节=%d" % (path, div, int(qpb * 4)))
    print("bar  pos16  midi  dur16")
    per_bar = int(qpb * 4)
    for t, n, d in events:
        rel = (t - t0) / sixteenth
        bar = int(rel // per_bar) + 1
        pos = rel - (bar - 1) * per_bar
        # 输出排序为「小节, 音位, 音高」
    # 按小节聚合成可比对的形式
    grid = {}
    for t, n, d in events:
        rel = (t - t0) / sixteenth
        bar = int(rel // per_bar) + 1
        pos = rel - (bar - 1) * per_bar
        grid.setdefault(bar, []).append((round(pos, 3), n, round(d / sixteenth, 3)))
    for bar in sorted(grid):
        items = sorted(grid[bar])
        print("m%-3d %s" % (bar, " ".join("%d@%g(%.2f)" % (n, p, d) for p, n, d in items)))


if __name__ == "__main__":
    main()
