import sys
from pathlib import Path

def read_vlq(data, i):
    v = 0
    while True:
        b = data[i]; i += 1
        v = (v << 7) | (b & 0x7F)
        if not b & 0x80:
            return v, i

def parse(path):
    data = Path(path).read_bytes()
    idx = 8 + int.from_bytes(data[4:8], "big")
    out = []
    while idx < len(data) and data[idx:idx+4] == b"MTrk":
        tlen = int.from_bytes(data[idx+4:idx+8], "big")
        cur, end = idx + 8, idx + 8 + tlen
        tick = 0; running = None
        while cur < end:
            delta, cur = read_vlq(data, cur)
            tick += delta
            st = data[cur]
            if st & 0x80:
                cur += 1; running = st
            else:
                st = running
            if st >= 0xF0:
                if st == 0xFF:
                    cur += 1                      # meta type
                    ln, cur = read_vlq(data, cur)
                    cur += ln
                else:
                    ln, cur = read_vlq(data, cur)
                    cur += ln
                continue
            kind = st & 0xF0; ch = st & 0x0F
            if kind in (0x80, 0x90):
                p, v = data[cur], data[cur+1]; cur += 2
                if kind == 0x90 and v > 0:
                    out.append((tick, p, ch))
            elif kind in (0xA0, 0xB0, 0xE0):
                cur += 2
            elif kind in (0xC0, 0xD0):
                cur += 1
            else:
                break
        idx = cur if False else end
    return out

for f in ("fence1.mid", "fence2.mid"):
    ns = parse(f)
    from collections import Counter
    c = Counter(ch for _, _, ch in ns)
    print(f"{f}: note-on 总数 {len(ns)}  按通道 {dict(sorted(c.items()))}")
