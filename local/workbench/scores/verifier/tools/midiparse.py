"""Minimal SMF parser: absolute-tick note events per track, tempo map, time sigs."""
import struct, sys


def _vlq(data, i):
    v = 0
    while True:
        b = data[i]
        i += 1
        v = (v << 7) | (b & 0x7F)
        if not b & 0x80:
            return v, i


def parse(path):
    raw = open(path, 'rb').read()
    assert raw[:4] == b'MThd', path
    hlen = struct.unpack('>I', raw[4:8])[0]
    fmt, ntrk, div = struct.unpack('>HHH', raw[8:14])
    pos = 8 + hlen
    tracks = []
    for _ in range(ntrk):
        assert raw[pos:pos + 4] == b'MTrk', (path, pos)
        tlen = struct.unpack('>I', raw[pos + 4:pos + 8])[0]
        body = raw[pos + 8:pos + 8 + tlen]
        pos += 8 + tlen
        tracks.append(_parse_track(body, div))
    return {'format': fmt, 'division': div, 'tracks': tracks}


def _parse_track(body, div):
    i = 0
    tick = 0
    status = None
    events = []
    while i < len(body):
        delta, i = _vlq(body, i)
        tick += delta
        if body[i] == 0xFF:
            mtype = body[i + 1]
            i += 2
            ln, i = _vlq(body, i)
            payload = body[i:i + ln]
            i += ln
            if mtype == 0x51 and ln == 3:
                events.append(('tempo', tick, int.from_bytes(payload, 'big')))
            elif mtype == 0x58:
                events.append(('timesig', tick, payload[0], payload[1]))
            continue
        if body[i] in (0xF0, 0xF7):
            i += 1
            ln, i = _vlq(body, i)
            i += ln
            continue
        b = body[i]
        if b & 0x80:
            status = b
            i += 1
        hi = status & 0xF0
        ch = status & 0x0F
        if hi in (0x80, 0x90, 0xA0, 0xB0, 0xE0):
            d1, d2 = body[i], body[i + 1]
            i += 2
            events.append((hex(hi), tick, ch, d1, d2))
        elif hi in (0xC0, 0xD0):
            d1 = body[i]
            i += 1
            events.append((hex(hi), tick, ch, d1))
        else:
            raise ValueError('bad status %x' % status)
    return events


if __name__ == '__main__':
    for p in sys.argv[1:]:
        m = parse(p)
        print(p, 'fmt', m['format'], 'div', m['division'], 'tracks', len(m['tracks']))
        for ti, tr in enumerate(m['tracks']):
            ons = [e for e in tr if e[0] == '0x90' and e[4] > 0]
            ts = [e for e in tr if e[0] == 'tempo' or e[0] == 'timesig']
            last = max((e[1] for e in tr), default=0)
            print('  track', ti, 'events', len(tr), 'noteons', len(ons),
                  'lasttick', last, 'timesig/tempo', ts[:6])
