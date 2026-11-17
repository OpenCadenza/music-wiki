import struct, sys

def read_vlq(b, i):
    v = 0
    while True:
        c = b[i]; i += 1
        v = (v << 7) | (c & 0x7F)
        if not c & 0x80:
            return v, i

def parse(path):
    b = open(path, "rb").read()
    assert b[:4] == b"MThd", b[:4]
    hlen = struct.unpack(">I", b[4:8])[0]
    fmt, ntrk, div = struct.unpack(">HHH", b[8:14])
    i = 8 + hlen
    tracks = []
    for t in range(ntrk):
        assert b[i:i + 4] == b"MTrk"
        ln = struct.unpack(">I", b[i + 4:i + 8])[0]
        body = b[i + 8:i + 8 + ln]
        i += 8 + ln
        ev = []
        j = 0
        tme = 0
        status = None
        while j < len(body):
            d, j = read_vlq(body, j)
            tme += d
            c = body[j]
            if c & 0x80:
                status = c
                j += 1
            else:
                pass
            if status == 0xFF:
                meta = body[j]; j += 1
                ln2, j = read_vlq(body, j)
                data = body[j:j + ln2]; j += ln2
                ev.append((tme, ("meta", meta, data)))
            elif status in (0xF0, 0xF7):
                ln2, j = read_vlq(body, j)
                j += ln2
            else:
                hi = status & 0xF0
                ch = status & 0x0F
                n = 1 if hi in (0xC0, 0xD0) else 2
                data = body[j:j + n]; j += n
                ev.append((tme, (hi, ch, data)))
        tracks.append(ev)
    return fmt, div, tracks

div = None
path = sys.argv[1] if len(sys.argv) > 1 else r"local\workbench\scores\verifier\build-k465\S2-K1-mozart-k465-4-m10-16.mid"
fmt, div, tracks = parse(path)
print("format", fmt, "divisions", div, "tracks", len(tracks))
Q = div  # ticks per quarter

tnames = []
for ti, ev in enumerate(tracks):
    name = ""
    t0 = 0
    ts = None
    tp = None
    notes = []
    on = {}
    for tme, e in ev:
        if e[0] == "meta":
            if e[1] == 0x03:
                name = e[2].decode("latin-1")
            elif e[1] == 0x51 and tp is None:
                tp = int.from_bytes(e[2], "big")
            elif e[1] == 0x58 and ts is None:
                ts = (e[2][0], 2 ** e[2][1])
        elif e[0] == 0x90 and e[2][1] > 0:
            on[(e[1], e[2][0])] = tme
        elif e[0] == 0x80 or (e[0] == 0x90 and e[2][1] == 0):
            k = (e[1], e[2][0])
            if k in on:
                notes.append((on[k], e[2][0], tme - on[k]))
                del on[k]
    notes.sort()
    tnames.append((name, notes, ts, tp))
    print("\ntrack %d  name=%r  timesig=%s  tempo_us=%s  notes=%d" % (ti, name, ts, tp, len(notes)))

print("\n=== notes per track with bar@beat (bar = 1-based, 2/4) ===")
for ti, (name, notes, ts, tp) in enumerate(tnames):
    print("\n-- track %d %r --" % (ti, name))
    for st, p, du in notes:
        bar = st // (2 * Q) + 1
        beat = (st % (2 * Q)) / Q
        print("  bar%-2d @%.2f  midi=%-3d dur=%.3g q" % (bar, beat, p, du / Q))
