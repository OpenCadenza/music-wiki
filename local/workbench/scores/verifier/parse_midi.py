"""Minimal MIDI parser: extract note (onset_ticks, dur_ticks, pitch) and header divisions/tempo."""
import struct, sys

PATH = sys.argv[1] if len(sys.argv) > 1 else "lp-build.mid"

def read_vlq(d, i):
    v = 0
    while True:
        b = d[i]; i += 1
        v = (v << 7) | (b & 0x7F)
        if not (b & 0x80):
            return v, i

data = open(PATH, "rb").read()
assert data[:4] == b"MThd", data[:4]
hlen = struct.unpack(">I", data[4:8])[0]
fmt, ntrks, div = struct.unpack(">HHH", data[8:14])
print(f"fmt={fmt} ntracks={ntrks} divisions(ticks/quarter)={div}")
pos = 8 + hlen
tracks = []
tempos = []
for t in range(ntrks):
    assert data[pos:pos+4] == b"MTrk", data[pos:pos+4]
    tlen = struct.unpack(">I", data[pos+4:pos+8])[0]
    body = data[pos+8:pos+8+tlen]
    pos += 8 + tlen
    i = 0; tick = 0; running = None
    notes = {}; pending = {}
    events = []
    while i < len(body):
        dt, i = read_vlq(body, i)
        tick += dt
        b = body[i]
        if b == 0xFF:
            i += 1
            meta = body[i]; i += 1
            ln, i = read_vlq(body, i)
            payload = body[i:i+ln]; i += ln
            if meta == 0x51 and ln == 3:
                us = (payload[0] << 16) | (payload[1] << 8) | payload[2]
                tempos.append((tick, us))
            elif meta == 0x2F:
                break
            continue
        if b in (0xF0, 0xF7):
            i += 1
            ln, i = read_vlq(body, i); i += ln
            continue
        if b & 0x80:
            status = b; i += 1; running = status
        else:
            status = running
        hi = status & 0xF0
        if hi in (0x80, 0x90):
            pitch = body[i]; vel = body[i+1]; i += 2
            key = pitch
            if hi == 0x90 and vel > 0:
                pending.setdefault(key, []).append(tick)
            else:
                if pending.get(key):
                    on = pending[key].pop(0)
                    events.append((on, tick - on, pitch))
            continue
        if hi in (0xA0, 0xB0, 0xE0):
            i += 2; continue
        if hi in (0xC0, 0xD0):
            i += 1; continue
        raise ValueError(f"bad status {status:#x}")
    tracks.append(events)

allnotes = sorted([e for tr in tracks for e in tr], key=lambda x: (x[0], x[2]))
print(f"tempo events (tick, us/qn): {tempos}")
if tempos:
    us = tempos[0][1]
    print(f"  -> BPM = {60_000_000/us:.2f} quarter-notes/min")

def q(ticks): return ticks / div

print(f"total notes: {len(allnotes)}")
spans = sorted(set((n[0], n[0]+n[1]) for n in allnotes))
length_q = q(max(s[1] for s in spans))
print(f"total length = {length_q:g} quarter notes = {length_q/3:g} measures (3/4)")
print()
for m in range(1, 9):
    lo = (m-1)*3*div
    hi = m*3*div
    inmeas = [n for n in allnotes if lo <= n[0] < hi]
    print(f"--- MIDI measure {m} (ticks {lo}..{hi}) ---")
    for on, dur, pitch in inmeas:
        st = q(on - lo)
        d = q(dur)
        pcs = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
        octv = pitch//12 - 1
        nm = f"{pcs[pitch%12]}{octv}"
        tag = " GRACE/SHORT" if d < 0.2 else ""
        print(f"   @{st:<6g} dur={d:<6.4g} {nm}{tag}")