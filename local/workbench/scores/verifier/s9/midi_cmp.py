#!/usr/bin/env python3
"""Independent verifier: compare LilyPond-produced MIDI against authoritative MusicXML.
No third-party MIDI library; minimal SMF parser."""
import sys, struct, os
from lxml import etree

STEP = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def nm(m): return "%s%d" % (NAMES[m%12], m//12-1)

# ---------- XML ----------
def xml_notes(path, part_index, mmax):
    root = etree.parse(path).getroot()
    part = root.findall('part')[part_index]
    div = 48
    abs_t = 0.0
    out = []
    for meas in part.findall('measure'):
        try: num = int(meas.get('number'))
        except: continue
        if num > mmax: break
        cur = 0.0
        last = 0.0
        d = meas.findtext('attributes/divisions')
        if d: div = int(d)
        for el in meas:
            if el.tag == 'backup':
                cur -= float(el.findtext('duration'))/div
            elif el.tag == 'forward':
                cur += float(el.findtext('duration'))/div
            elif el.tag == 'note':
                if el.find('grace') is not None: continue
                de = el.findtext('duration')
                dur = float(de)/div if de else 0.0
                ch = el.find('chord') is not None
                if ch:
                    onset = last
                else:
                    onset = cur; last = cur; cur += dur
                if el.find('rest') is not None: continue
                p = el.find('pitch')
                if p is None: continue
                midi = 12*(int(p.findtext('octave'))+1)+STEP[p.findtext('step')]+int(p.findtext('alter') or 0)
                ties = [t.get('type') for t in el.findall('tie')]
                out.append(dict(t=abs_t+onset, midi=midi, dur=dur, num=num,
                                on=onset, tie_s='start' in ties, tie_st='stop' in ties))
        abs_t += 2.0
    # merge ties
    merged = []
    for n in out:
        if n['tie_st']:
            cand = None
            for m in reversed(merged):
                if m['midi'] == n['midi'] and abs(m['t']+m['dur']-n['t']) < 1e-6:
                    cand = m; break
            if cand is not None:
                cand['dur'] += n['dur']
                continue
        merged.append(dict(n))
    return merged

# ---------- MIDI ----------
def read_smf(path):
    data = open(path,'rb').read()
    assert data[:4] == b'MThd', "not a midi file"
    hl = struct.unpack('>I', data[4:8])[0]
    fmt, ntrk, div = struct.unpack('>HHH', data[8:14])
    pos = 8 + hl
    tracks = []
    while pos < len(data):
        if data[pos:pos+4] != b'MTrk':
            break
        ln = struct.unpack('>I', data[pos+4:pos+8])[0]
        body = data[pos+8:pos+8+ln]
        pos += 8 + ln
        tracks.append(body)
    # parse each track
    parsed = []
    for body in tracks:
        i = 0; tick = 0; running = None
        notes = []   # (on_tick, midi, dur_tick)
        open_notes = {}
        tempo = []
        while i < len(body):
            # varlen
            d = 0
            while True:
                b = body[i]; i += 1
                d = (d<<7) | (b & 0x7f)
                if not (b & 0x80): break
            tick += d
            st = body[i]
            if st == 0xFF:
                i += 1
                mt = body[i]; i += 1
                ln2 = 0
                while True:
                    b = body[i]; i += 1
                    ln2 = (ln2<<7)|(b & 0x7f)
                    if not (b & 0x80): break
                payload = body[i:i+ln2]; i += ln2
                if mt == 0x51:
                    us = (payload[0]<<16)|(payload[1]<<8)|payload[2]
                    tempo.append((tick, us))
                elif mt == 0x2F:
                    pass
                continue
            if st in (0xF0, 0xF7):
                i += 1
                ln2 = 0
                while True:
                    b = body[i]; i += 1
                    ln2 = (ln2<<7)|(b & 0x7f)
                    if not (b & 0x80): break
                i += ln2
                continue
            if st & 0x80:
                running = st; i += 1
            else:
                st = running
            hi = st & 0xF0
            if hi in (0x80, 0x90, 0xA0, 0xB0, 0xE0):
                b1 = body[i]; b2 = body[i+1]; i += 2
                if hi == 0x90 and b2 > 0:
                    open_notes.setdefault(b1, []).append(tick)
                elif hi == 0x80 or (hi == 0x90 and b2 == 0):
                    if b1 in open_notes and open_notes[b1]:
                        on = open_notes[b1].pop(0)
                        notes.append((on, b1, tick-on))
            elif hi in (0xC0, 0xD0):
                i += 1
            else:
                raise ValueError("unknown status %02x" % st)
        parsed.append(dict(notes=notes, tempo=tempo, div=div))
    return fmt, div, parsed

if __name__ == '__main__':
    xmlp = sys.argv[1]; midp = sys.argv[2]
    fmt, div, tks = read_smf(midp)
    print("SMF format=%d division=%d tracks=%d" % (fmt, div, len(tks)))
    for i,t in enumerate(tks):
        print("  track %d: %d notes, tempo %s" % (i, len(t['notes']), t['tempo']))
    names = ['violon','violoncelle','RightHand','LeftHand']
    # lilypond track order = staff order: violin, cello, pianoRH, pianoLH  (+ maybe a meta track)
    nz = [(i,t) for i,t in enumerate(tks) if t['notes']]
    print("tracks with notes:", [i for i,_ in nz])
    ok = True
    for k,(ti,t) in enumerate(nz):
        if k >= 4: break
        xn = xml_notes(xmlp, k, 21)
        got = sorted([(n[0]/div, n[1], n[2]/div) for n in t['notes']])
        exp = sorted([(n['t'], n['midi'], n['dur']) for n in xn])
        print("\n== part %d (%s): XML %d notes, MIDI %d notes" % (k, names[k], len(exp), len(got)))
        if len(exp) != len(got):
            ok = False
            print("  COUNT MISMATCH")
            ex = set((round(a,4),b,round(c,4)) for a,b,c in exp)
            gt = set((round(a,4),b,round(c,4)) for a,b,c in got)
            for x in sorted(ex-gt)[:20]: print("   only-XML", x)
            for x in sorted(gt-ex)[:20]: print("   only-MIDI", x)
        else:
            for (a,b,c),(a2,b2,c2) in zip(exp,got):
                if abs(a-a2) > 1e-3 or b != b2 or abs(c-c2) > 1e-3:
                    ok = False
                    print("   DIFF xml=(%s %s %s) midi=(%s %s %s)" % (
                        round(a,4), nm(b), round(c,4), round(a2,4), nm(b2), round(c2,4)))
        print("   =>", "IDENTICAL" if ok else "see diffs above")
