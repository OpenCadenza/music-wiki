#!/usr/bin/env python3
"""Verifier: structural comparison of the .ly source against authoritative MusicXML.
Parses the LilyPond subset actually used in the file (absolute pitches, chords,
durations+dots, articulations, slurs, ties, \\grace) and the MusicXML measures,
then reports per-measure / per-voice differences."""
import sys, re
from fractions import Fraction
from lxml import etree

STEP = {'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
FLAT = {'f':-1,'s':1}
NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def lymidi(name, sharps, flats, octadj):
    base = STEP[name] + sharps*1 + flats*(-1)
    octv = 3 + octadj           # c' = C4
    return 12*(octv+1) + base

def nm(m): return "%s%d" % (NAMES[m%12], m//12-1)

# ---------------- LilyPond ----------------
def strip_comments(s):
    return re.sub(r'%[^\n]*', '', s)

def parse_voice(body):
    """returns list of measures; each measure = list of events dicts"""
    meas = [[]]
    i = 0
    tok = re.compile(r'''
        (?P<grace>\\grace)
      | (?P<cmd>\\[a-zA-Z]+)
      | (?P<chordopen><)
      | (?P<chordclose>>)
      | (?P<pitch>[a-g](?:ff|ss|es|is|f|s)?)
      | (?P<num>\d+)
      | (?P<dot>\.)
      | (?P<art>[-^_][-.>+!|]?)
      | (?P<lparen>\()
      | (?P<rparen>\))
      | (?P<tilde>~)
      | (?P<bar>\|)
      | (?P<brace>\{|\})
      | (?P<ws>\s+)
    ''', re.X)
    cur_dur = None; cur_dots = 0
    in_chord = False; chord = []
    grace = False
    pending = None
    def flush():
        nonlocal pending
        if pending is not None:
            meas[-1].append(pending)
            pending = None
    pos = 0
    n = len(body)
    while pos < n:
        m = tok.match(body, pos)
        if not m:
            pos += 1
            continue
        pos = m.end()
        g = m.lastgroup
        v = m.group()
        if g == 'ws': continue
        if g == 'grace':
            grace = True
            continue
        if g == 'cmd':
            if v == '\\clef': pass
            if v in ('\\tenuto', '\\accent', '\\staccato', '\\marcato'):
                if pending is None: pending = dict()
                arts = pending.setdefault('args', set())
                arts.add({'\\tenuto':'tenuto','\\accent':'accent','\\staccato':'staccato','\\marcato':'marcato'}[v])
            continue
        if g == 'brace': continue
        if g == 'bar':
            flush()
            meas.append([])
            continue
        if g == 'chordopen':
            in_chord = True; chord = []
            continue
        if g == 'chordclose':
            in_chord = False
            pending = dict(pitches=sorted(chord), dur=cur_dur, dots=cur_dots,
                           args=set(), slur_s=False, slur_e=False,
                           tie_s=False, grace=grace, dur_given=None)
            grace = False
            continue
        if g == 'pitch':
            name = v[0]
            s = 1 if v[1:] in ('s','is') else 0
            f = 1 if v[1:] in ('f','es') else 0
            octadj = 0
            while pos < n and body[pos] in ("'", ','):
                octadj += 1 if body[pos] == "'" else -1
                pos += 1
            m2 = tok.match(body, pos) if pos < n else None
            dur = None; dots = 0
            # duration digits immediately following
            mm = re.match(r'(\d+)', body[pos:])
            if mm:
                dur = int(mm.group(1)); pos += len(mm.group(1))
                while pos < n and body[pos] == '.':
                    dots += 1; pos += 1
            midi = lymidi(name, s, f, octadj)
            if in_chord:
                chord.append(midi)
            else:
                if dur is not None:
                    cur_dur = dur; cur_dots = dots
                pending = dict(pitches=[midi], dur=dur if dur is not None else cur_dur,
                               dots=dots if dur is not None else cur_dots,
                               args=set(), slur_s=False, slur_e=False,
                               tie_s=False, grace=grace, dur_given=(dur is not None))
                grace = False
            continue
        if g == 'art':
            if pending is None: pending = dict(pitches=[], dur=None, dots=0, args=set(),
                                               slur_s=False, slur_e=False, tie_s=False,
                                               grace=False, dur_given=None)
            a = {'-.':'staccato', '->':'accent', '-':'tenuto', '-.': 'staccato'}
            if v == '-.': pending['args'].add('staccato')
            elif v == '->': pending['args'].add('accent')
            elif v == '-': pending['args'].add('tenuto')
            elif v == '--': pending['args'].add('tenuto')
            continue
        if g == 'lparen':
            if pending is None: pending = dict(pitches=[], dur=None, dots=0, args=set(),
                                               slur_s=False, slur_e=False, tie_s=False,
                                               grace=False, dur_given=None)
            pending['slur_s'] = True
            continue
        if g == 'rparen':
            if pending is not None: pending['slur_e'] = True
            continue
        if g == 'tilde':
            if pending is not None: pending['tie_s'] = True
            continue
    flush()
    return meas

# ---------------- MusicXML ----------------
def xml_measures(path, part_index, mmax):
    root = etree.parse(path).getroot()
    part = root.findall('part')[part_index]
    div = 48
    out = {}
    for meas in part.findall('measure'):
        try: num = int(meas.get('number'))
        except: continue
        if num > mmax: break
        d = meas.findtext('attributes/divisions')
        if d: div = int(d)
        cur = Fraction(0); last = Fraction(0)
        evs = []
        opengrace = 0
        for el in meas:
            if el.tag == 'backup':
                cur -= Fraction(int(el.findtext('duration')), div)
            elif el.tag == 'forward':
                cur += Fraction(int(el.findtext('duration')), div)
            elif el.tag == 'note':
                de = el.findtext('duration')
                dur = Fraction(int(de), div) if de else Fraction(0)
                ch = el.find('chord') is not None
                grace = el.find('grace') is not None
                if not ch:
                    onset = cur
                    if not grace:
                        last = cur; cur += dur
                else:
                    onset = last
                if el.find('rest') is not None:
                    if not ch:
                        evs.append(dict(onset=onset, pitches=[], rest=True, dur=dur,
                                        dots=len(el.findall('dot')), typ=el.findtext('type'),
                                        args=set(), tie_s=False, slur_s=False, slur_e=False, grace=grace))
                    continue
                p = el.find('pitch')
                midi = 12*(int(p.findtext('octave'))+1)+STEP[p.findtext('step').lower()]+int(p.findtext('alter') or 0)
                arts = set(a.tag for a in el.findall('notations/articulations/*'))
                sl = [s.get('type') for s in el.findall('notations/slur')]
                ti = [t.get('type') for t in el.findall('tie')]
                if ch:
                    e = evs[-1]
                    e['pitches'].append(midi); e['args'] |= arts
                    e['slur_s'] |= ('start' in sl); e['slur_e'] |= ('stop' in sl)
                    e['tie_s'] |= ('start' in ti)
                    e['pitches'].sort()
                else:
                    evs.append(dict(onset=onset, pitches=[midi], rest=False, dur=dur,
                                    dots=len(el.findall('dot')), typ=el.findtext('type'),
                                    args=arts, tie_s=('start' in ti),
                                    slur_s=('start' in sl), slur_e=('stop' in sl), grace=grace))
        out[num] = evs
    return out

# ---------------- compare ----------------
def norm_ly(meas):
    """convert parsed ly measure events to onset-based events, dropping global/clef noise"""
    res = []
    t = Fraction(0)
    for e in meas:
        if 'pitches' not in e or e.get('dur') is None:
            continue
        d = Fraction(1, e['dur']) * (2 - Fraction(1, 2**e['dots']))
        res.append(dict(onset=t, pitches=sorted(e['pitches']), dur=d, dots=e['dots'],
                        args=set(e['args']), tie_s=e['tie_s'], slur_s=e['slur_s'],
                        slur_e=e['slur_e'], grace=e['grace']))
        if not e ['grace']:
            t += d
    return res

if __name__ == '__main__':
    lyrics = open(sys.argv[1], encoding='utf-8').read()
    xmlp = sys.argv[2]
    mmax = 21
    bodies = {}
    for name in ('violin', 'cello', 'pianoRH', 'pianoLH'):
        m = re.search(r'^%s\s*=\s*\{(.*?)^\}' % name, lyrics, re.S | re.M)
        if not m:
            print("!! cannot find voice", name); continue
        bodies[name] = m.group(1)
    # merge multi-line: pianoRH contains \global
    order = [('violin',0), ('cello',1), ('pianoRH',2), ('pianoLH',3)]
    nbad = 0
    for name, pi in order:
        body = strip_comments(bodies[name])
        body = body.replace('\\global', '')
        meas = parse_voice(body)
        xm = xml_measures(xmlp, pi, mmax)
        print("\n===== %s : ly measures parsed = %d, xml = %d" % (name, len(meas)-1, len(xm)))
        for i in range(1, mmax+1):
            ly = norm_ly(meas[i]) if i < len(meas) else []
            xl = xm.get(i, [])
            # compare ignoring grace in xml (kept) and in ly (kept)
            A = [(e['onset'], tuple(e['pitches']), e['dur'], e['dots'], tuple(sorted(e['args'])),
                  e['tie_s'], e['slur_s'], e['slur_e']) for e in ly]
            B = [(e['onset'], tuple(sorted(e['pitches'])), e['dur'], e['dots'], tuple(sorted(e['args'])),
                  e['tie_s'], e['slur_s'], e['slur_e']) for e in xl]
            if A != B:
                nbad += 1
                print("  m.%d DIFF" % i)
                for k in range(max(len(A), len(B))):
                    a = A[k] if k < len(A) else None
                    b = B[k] if k < len(B) else None
                    if a != b:
                        def fmt(x):
                            if x is None: return "--"
                            return "@%s %s dur=%s dots=%d args=%s tie=%s slurS=%s slurE=%s" % (
                                x[0], [nm(p) for p in x[1]], x[2], x[3], x[4], x[5], x[6], x[7])
                        print("     ly : %s" % fmt(a))
                        print("     xml: %s" % fmt(b))
        print("  => %s" % ("ALL MEASURES IDENTICAL" if nbad == 0 else "%d differing measure(s) total so far" % nbad))
