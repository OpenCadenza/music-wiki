"""核验用 MIDI 转储：按通道列出 (起始拍, 音高, 时值)，并按小节分组。
用法: python midi_dump.py <mid> [每小节拍数]
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def nm(p):
    return f"{NAMES[p % 12]}{p // 12 - 1}"


def read_vlq(data, i):
    v = 0
    while True:
        b = data[i]
        i += 1
        v = (v << 7) | (b & 0x7F)
        if not b & 0x80:
            return v, i


def parse(path):
    data = Path(path).read_bytes()
    if data[:4] != b"MThd":
        raise SystemExit("not midi")
    hlen = int.from_bytes(data[4:8], "big")
    divisions = int.from_bytes(data[12:14], "big")
    idx = 8 + hlen
    tracks = []
    while idx < len(data) and data[idx:idx + 4] == b"MTrk":
        tlen = int.from_bytes(data[idx + 4:idx + 8], "big")
        cur, end = idx + 8, idx + 8 + tlen
        tick = 0
        running = None
        events = []
        while cur < end:
            delta, cur = read_vlq(data, cur)
            tick += delta
            status = data[cur]
            if status & 0x80:
                cur += 1
                running = status
            else:
                status = running
            if status >= 0xF0:
                # meta / sysex
                if status == 0xFF:
                    cur += 1  # meta type
                    mlen, cur = read_vlq(data, cur)
                    cur += mlen
                else:
                    slen, cur = read_vlq(data, cur)
                    cur += slen
                continue
            kind = status & 0xF0
            ch = status & 0x0F
            if kind in (0x80, 0x90):
                pitch, vel = data[cur], data[cur + 1]
                cur += 2
                if kind == 0x90 and vel > 0:
                    events.append((tick, "on", pitch, ch))
                else:
                    events.append((tick, "off", pitch, ch))
            elif kind in (0xA0, 0xB0, 0xE0):
                cur += 2
            elif kind in (0xC0, 0xD0):
                cur += 1
            else:
                break
        tracks.append(events)
        idx = end
    return tracks, divisions


def notes_of(events, divisions):
    sounding = {}
    out = []
    for tick, kind, pitch, ch in events:
        if kind == "on":
            sounding.setdefault((pitch, ch), []).append(tick)
        else:
            lst = sounding.get((pitch, ch))
            if lst:
                start = lst.pop(0)
                out.append((start / divisions, (tick - start) / divisions, pitch, ch))
    for (pitch, ch), lst in sounding.items():
        for start in lst:
            out.append((start / divisions, 1.0, pitch, ch))
    out.sort()
    return out


def main():
    path = sys.argv[1]
    beat = float(sys.argv[2]) if len(sys.argv) > 2 else 4.0
    offset = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
    tracks, divisions = parse(path)
    print(f"文件 {path}  divisions={divisions}  轨数={len(tracks)}")
    allnotes = []
    for ti, ev in enumerate(tracks):
        ns = notes_of(ev, divisions)
        if not ns:
            continue
        chs = sorted({n[3] for n in ns})
        print(f"  track{ti}: {len(ns)} 音  channels={chs} 范围 {nm(min(n[2] for n in ns))}({min(n[2] for n in ns)})"
              f"-{nm(max(n[2] for n in ns))}({max(n[2] for n in ns)})")
        for n in ns:
            allnotes.append((ti,) + n)
    print("\n按小节分组（每小节 %.0f 拍，弱起 %.2f 拍）:" % (beat, offset))
    by_meas = {}
    for ti, st, du, p, ch in allnotes:
        if st < offset:
            meas = 0
        else:
            meas = int((st - offset) // beat) + 1
        by_meas.setdefault((meas, ti), []).append((st, du, p))
    for (meas, ti) in sorted(by_meas):
        items = sorted(by_meas[(meas, ti)])
        txt = " ".join(f"{nm(p)}({p})@{o:g}+{du:g}" for o, du, p in items)
        label = "弱起" if meas == 0 else f"m.{meas}"
        print(f"  {label:>4} track{ti}: {txt}")


if __name__ == "__main__":
    main()
