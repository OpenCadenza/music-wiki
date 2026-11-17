import sys, struct

def parse(path):
    data = open(path, 'rb').read()
    assert data[:4] == b'MThd', data[:4]
    hlen = struct.unpack('>I', data[4:8])[0]
    fmt, ntrk, div = struct.unpack('>HHH', data[8:8+6])
    pos = 8 + hlen
    tracks = []
    for t in range(ntrk):
        assert data[pos:pos+4] == b'MTrk', (t, data[pos:pos+4])
        tlen = struct.unpack('>I', data[pos+4:pos+8])[0]
        body = data[pos+8:pos+8+tlen]
        pos += 8 + tlen
        tracks.append(parse_track(body, div))
    return fmt, div, tracks

def vlq(body, i):
    val = 0
    while True:
        b = body[i]; i += 1
        val = (val << 7) | (b & 0x7f)
        if not b & 0x80:
            return val, i

def parse_track(body, div):
    i = 0
    t = 0
    status = None
    events = []
    name = None
    while i < len(body):
        dt, i = vlq(body, i)
        t += dt
        b = body[i]
        if b == 0xFF:
            meta = body[i+1]
            ln, j = vlq(body, i+2)
            payload = body[j:j+ln]
            if meta == 0x03:
                name = payload.decode('latin-1')
            i = j + ln
            continue
        if b in (0xF0, 0xF7):
            ln, j = vlq(body, i+1)
            i = j + ln
            continue
        if b & 0x80:
            status = b
            i += 1
        hi = status & 0xF0
        ch = status & 0x0F
        if hi in (0x80, 0x90, 0xA0, 0xB0, 0xE0):
            d1 = body[i]; d2 = body[i+1]; i += 2
            if hi in (0x80, 0x90):
                events.append((t, hi, ch, d1, d2))
        elif hi in (0xC0, 0xD0):
            d1 = body[i]; i += 1
            if hi == 0xC0:
                events.append((t, hi, ch, d1, None))
        else:
            i += 1
    return {'name': name, 'events': events}

def dump(path):
    fmt, div, tracks = parse(path)
    print(f'format={fmt} division={div} tracks={len(tracks)}')
    for ti, tr in enumerate(tracks):
        print(f'--- track {ti} name={tr["name"]!r} events={len(tr["events"])}')
        # collect notes with on/off pairing
        notes = []
        open_n = {}
        for (t, kind, ch, d1, d2) in tr['events']:
            if kind == 0x90 and d2 and d2 > 0:
                open_n.setdefault((ch, d1), []).append(t)
            elif kind == 0x80 or (kind == 0x90 and (d2 == 0 or d2 is None)):
                st = open_n.get((ch, d1))
                if st:
                    on = st.pop(0)
                    notes.append((on, t, ch, d1, d2))
        for (on, off, ch, pitch, vel) in notes:
            q0 = on / div; q1 = off / div
            m = int(q0 // 4) + 1
            b = q0 - (m-1)*4 + 1
            print(f'm{m:3d} qb={q0:7.2f} beat={b:5.2f} dur={q1-q0:5.2f} ch={ch} pitch={pitch:3d} vel={vel}')

if __name__ == '__main__':
    dump(sys.argv[1])
