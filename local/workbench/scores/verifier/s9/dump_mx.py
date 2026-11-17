#!/usr/bin/env python3
# Verifier-side independent MusicXML dumper (mm range, all parts).
import sys, os, glob
from lxml import etree

STEP = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def midi_of(step, alter, octv):
    return 12*(int(octv)+1) + STEP[step] + int(alter or 0)

def pname(step, alter, octv):
    m = midi_of(step, alter, octv)
    return "%s%s%d" % (NAMES[m % 12], 'b' if alter and int(alter) < 0 else '', m//12 - 1)

def dump(path, m0, m1, out):
    tree = etree.parse(path)
    root = tree.getroot()
    mv = root.findtext('movement-title')
    out.write("FILE: %s\n" % os.path.basename(path))
    out.write("MOVEMENT-TITLE: %r\n" % mv)
    plist = root.find('part-list')
    parts = []
    for sp in plist:
        if sp.tag == 'score-part':
            parts.append((sp.get('id'),
                          sp.findtext('part-name'),
                          sp.findtext('.//midi-instrument/midi-program')))
    out.write("PARTS: %r\n" % (parts,))
    divisions = None
    allparts = root.findall('part')
    out.write("PART ELEMENTS: %d\n" % len(allparts))
    for part in allparts:
        pid = part.get('id')
        pname_ = dict((p[0], p[1]) for p in parts).get(pid, pid)
        measures = part.findall('measure')
        out.write("\n=== PART %s (%s): %d measures\n" % (pid, pname_, len(measures)))
        for meas in measures:
            nattr = meas.get('number')
            try:
                num = int(nattr)
            except Exception:
                continue
            if not (m0 <= num <= m1):
                continue
            div = divisions
            cur = 0.0
            last_onset = 0.0
            out.write("\n--- m.%d\n" % num)
            # measure-level attributes
            for at in meas.findall('attributes'):
                bits = []
                for tag, attr in (('divisions',''),('key',''),('time',''),('clef',''),('staves','')):
                    pass
                d = at.findtext('divisions')
                if d: div = int(d); bits.append("divisions=%s" % d)
                k = at.find('key')
                if k is not None:
                    bits.append("key fifths=%s mode=%s" % (k.findtext('fifths'), k.findtext('mode')))
                t = at.find('time')
                if t is not None:
                    bits.append("time %s/%s" % (t.findtext('beats'), t.findtext('beat-type')))
                for c in at.findall('clef'):
                    bits.append("clef staff=%s %s%s line=%s" % (c.get('number'), c.findtext('sign'), c.findtext('line'), c.findtext('clef-octave-change')))
                if bits:
                    out.write("    ATTR: %s\n" % "; ".join(bits))
            for bar in meas.findall('barline'):
                out.write("    BARLINE location=%s style=%s repeat=%s\n" % (
                    bar.get('location'), bar.findtext('bar-style'),
                    (bar.find('repeat').get('direction') if bar.find('repeat') is not None else None)))
            for el in meas:
                if el.tag == 'attributes':
                    continue
                if el.tag in ('barline',):
                    continue
                if el.tag == 'direction':
                    txt = "; ".join([w.text or '' for w in el.iter('words')])
                    snd = el.find('.//sound')
                    met = el.find('.//metronome')
                    mt = ''
                    if met is not None:
                        mt = "metronome %s=%s" % (met.findtext('.//beat-unit'), met.findtext('.//per-minute'))
                    out.write("    DIRECTION staff=%s place=%s words=%r sound_tempo=%s %s\n" % (
                        el.get('staff'), el.get('placement'), txt,
                        (snd.get('tempo') if snd is not None else None), mt))
                    continue
                if el.tag == 'sound':
                    out.write("    SOUND tempo=%s\n" % el.get('tempo'))
                    continue
                if el.tag in ('backup', 'forward'):
                    d = float(el.findtext('duration')) / (div or 48)
                    if el.tag == 'backup':
                        cur -= d
                    else:
                        cur += d
                    out.write("    %s %s\n" % (el.tag.upper(), d))
                    continue
                if el.tag != 'note':
                    continue
                grace = el.find('grace') is not None
                dur_e = el.findtext('duration')
                dur = float(dur_e)/(div or 48) if dur_e else 0.0
                ischord = el.find('chord') is not None
                rest = el.find('rest') is not None
                pitch = el.find('pitch')
                if rest:
                    p = "REST"
                elif pitch is not None and pitch.findtext('step'):
                    step = pitch.findtext('step'); alt = pitch.findtext('alter') or '0'
                    octv = pitch.findtext('octave')
                    p = "%s(%s,m%d)" % (pname(step, alt, octv), "%s%s/%s" % (step, alt, octv), midi_of(step, alt, octv))
                else:
                    up = el.find('unpitched')
                    p = "UNPITCHED %s" % (etree.tostring(up) if up is not None else '')
                typ = el.findtext('type'); dots = len(el.findall('dot'))
                stem = el.findtext('stem')
                voice = el.findtext('voice'); staff = el.findtext('staff')
                acc = el.findtext('accidental')
                arts = [a.tag for a in el.findall('notations/articulations/*')]
                slurs = [ (s.get('type'), s.get('number')) for s in el.findall('notations/slur') ]
                ties = [t.get('type') for t in el.findall('tie')] + [t.get('type') for t in el.findall('notations/tied')]
                tm = el.find('time-modification')
                tms = ''
                if tm is not None:
                    tms = "%s/%s" % (tm.findtext('actual-notes'), tm.findtext('normal-notes'))
                if grace:
                    onset = "G@%g" % cur
                elif ischord:
                    onset = "=@%g" % last_onset
                else:
                    onset = "@%g" % cur
                    last_onset = cur
                    cur += dur
                out.write("    NOTE %-9s %-22s type=%-6s dots=%d dur=%g v=%s st=%s stem=%s acc=%s arts=%s slur=%s tie=%s tm=%s\n" % (
                    onset, p, typ, dots, dur, voice, staff, stem, acc, ",".join(arts) or "-",
                    ",".join("%s%s" % s for s in slurs) or "-", ",".join(ties) or "-", tms or "-"))

if __name__ == '__main__':
    dump(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.stdout)
