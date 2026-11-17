import sys, os, struct, hashlib

def parse(path):
    data = open(path, 'rb').read()
    assert data[:4] == b'MThd', data[:4]
    hlen = struct.unpack('>I', data[4:8])[0]
    fmt, ntrk, div = struct.unpack('>HHH', data[8:8+6])
    pos = 8 + hlen
    tracks = []
    for t in range(ntrk):
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
    i = 0; t = 0; status = None; events = []; name = None
    while i < len(body):
        dt, i = vlq(body, i); t += dt
        b = body[i]
        if b == 0xFF:
            meta = body[i+1]; ln, j = vlq(body, i+2); payload = body[j:j+ln]
            if meta == 0x03: name = payload.decode('latin-1')
            i = j + ln; continue
        if b in (0xF0, 0xF7):
            ln, j = vlq(body, i+1); i = j + ln; continue
        if b & 0x80:
            status = b; i += 1
        hi = status & 0xF0; ch = status & 0x0F
        if hi in (0x80, 0x90, 0xA0, 0xB0, 0xE0):
            d1 = body[i]; d2 = body[i+1]; i += 2
            events.append((t, hi, ch, d1, d2))
        elif hi in (0xC0, 0xD0):
            d1 = body[i]; i += 1
            events.append((t, hi, ch, d1, None))
        else:
            i += 1
    return {'name': name, 'events': events}

def notes_of(tr, div):
    open_n = {}; notes = []
    for (t, kind, ch, d1, d2) in tr['events']:
        if kind == 0x90 and d2 and d2 > 0:
            open_n.setdefault((ch, d1), []).append(t)
        elif kind == 0x80 or (kind == 0x90 and (d2 == 0 or d2 is None)):
            st = open_n.get((ch, d1))
            if st:
                on = st.pop(0)
                notes.append((on, t, ch, d1))
    notes.sort()
    return notes

def chord_split(notes):
    """group notes with identical (onset,dur) into chords"""
    from collections import defaultdict
    g = defaultdict(list)
    for (on, off, ch, p) in notes:
        g[(on, off, ch)].append(p)
    out = []
    for (on, off, ch), ps in sorted(g.items()):
        out.append((on, off, ch, tuple(sorted(ps))))
    return out

def report(path, label):
    fmt, div, tracks = parse(path)
    print(f'### {label}  ({os.path.basename(path)})')
    print(f'sha1={hashlib.sha1(open(path,"rb").read()).hexdigest()} fmt={fmt} div={div} tracks={len(tracks)}')
    for ti, tr in enumerate(tracks):
        progs = [(t/div, d1) for (t, kind, ch, d1, d2) in tr['events'] if kind == 0xC0]
        chans = sorted({ch for (t, kind, ch, d1, d2) in tr['events'] if kind in (0x90, 0x80)})
        print(f'  track{ti} name={tr["name"]!r} program0={progs} chans={chans}')
        cs = chord_split(notes_of(tr, div))
        for (on, off, ch, ps) in cs:
            m = int(on // 4) + 1
            beat = on - (m-1)*4 + 1
            barq = on - (m-1)*4
            print(f'    m{m:3d} beat{beat:5.2f} qbar{barq:4.2f} dur={(off-on):5.2f} ch{ch} {"/".join(map(str,ps))}')
    print()

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        report(arg, arg)
