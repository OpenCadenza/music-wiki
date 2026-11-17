#!/usr/bin/env python3
"""Verifier: structural comparison of the .ly source against authoritative MusicXML.
Independent LilyPond-subset parser (absolute pitches, chords, durations+dots,
articulations, slurs, ties, \\grace, rests) vs MusicXML measures."""
import sys, re
from fractions import Fraction
from lxml import etree

STEP = {'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
def nm(m):
    if m is None: return 'REST'
    return "%s%d" % (NAMES[m%12], m//12-1)

ARTMAP = {'-.':'staccato', '->':'accent', '--':'tenuto', '-':'tenuto',
          '\\tenuto':'tenuto', '\\accent':'accent', '\\staccato':'staccato'}

def strip_ly(s):
    s = re.sub(r'%[^\n]*', '', s)                 # comments
    s = re.sub(r'\\mark\s*\\markup\s*\{[^}]*\}', '', s)   # \mark \markup {...}
    s = re.sub(r'\\clef\s+[a-zA-Z]+', '', s)      # \clef treble etc.
    s = re.sub(r'\\set\s+\S+\s*=\s*\S+', '', s)   # \set ...
    s = re.sub(r'"[^"]*"', '', s)                 # strings
    return s

TOK = re.compile(r'''
    (?P<grace>\\grace)
  | (?P<cmd>\\[a-zA-Z]+)
  | (?P<chordopen><)
  | (?P<chordclose>>)
  | (?P<pitch>[a-g](?:ff|ss|es|is|f|s)?(?![a-zA-Z]))
  | (?P<rest>r)
  | (?P<num>\d+)
  | (?P<dot>\.)
  | (?P<art>[-^_][-.>+!|]?)
  | (?P<lparen>\()
  | (?P<rparen>\))
  | (?P<tilde>~)
  | (?P<bar>\|)
  | (?P<brace>[{}])
''', re.X)

def parse_voice(body):
    measures = [[]]
    cur = None
    collecting = None      # list of pitches while inside <>
    grace = False
    grace_brace = 0
    pos, n = 0, len(body)
    def fin():
        nonlocal cur
        if cur is not None:
            measures[-1].append(cur); cur = None
    while pos < n:
        m = TOK.match(body, pos)
        if not m:
            pos += 1; continue
        pos = m.end(); g = m.lastgroup; v = m.group()
        if g == 'grace':
            grace = True; continue
        if g == 'brace':
            if v == '{' and grace: grace_brace += 1
            elif v == '}' and grace_brace:
                grace_brace -= 1
                if grace_brace == 0: grace = False
            continue
        if g == 'cmd':
            a = ARTMAP.get(v)
            if a:
                if cur is None: cur = dict(pitches=[], dur=None, dots=0, args=set(),
                                           slur_s=False, slur_e=False, tie_s=False, grace=False)
                cur['args'].add(a)
            continue
        if g == 'chordopen':
            fin(); collecting = []; continue
        if g == 'chordclose':
            cur = dict(pitches=sorted(collecting), dur=None, dots=0, args=set(),
                       slur_s=False, slur_e=False, tie_s=False, grace=grace)
            collecting = None; continue
        if g == 'pitch':
            name = v[0]
            s = 1 if v[1:] in ('s','is') else 0
            f = 1 if v[1:] in ('f','es') else 0
            octadj = 0
            while pos < n and body[pos] in ("'", ','):
                octadj += 1 if body[pos] == "'" else -1
                pos += 1
            midi = 12*(4+octadj) + STEP[name] + s - f
            if collecting is not None:
                collecting.append(midi)
            else:
                fin()
                cur = dict(pitches=[midi], dur=None, dots=0, args=set(),
                           slur_s=False, slur_e=False, tie_s=False, grace=grace)
            continue
        if g == 'rest':
            fin()
            cur = dict(pitches=[], rest=True, dur=None, dots=0, args=set(),
                       slur_s=False, slur_e=False, tie_s=False, grace=False)
            continue
        if g == 'num':
            if cur is None: cur = dict(pitches=[], dur=None, dots=0, args=set(),
                                       slur_s=False, slur_e=False, tie_s=False, grace=False)
            cur['dur'] = int(v); continue
        if g == 'dot':
            if cur is not None: cur['dots'] += 1
            continue
        if g == 'art':
            a = ARTMAP.get(v)
            if a:
                if cur is None: cur = dict(pitches=[], dur=None, dots=0, args=set(),
                                           slur_s=False, slur_e=False, tie_s=False, grace=False)
                cur['args'].add(a)
            continue
        if g == 'lparen':
            if cur is not None: cur['slur_s'] = True
            continue
        if g == 'rparen':
            if cur is not None: cur['slur_e'] = True
            continue
        if g == 'tilde':
            if cur is not None: cur['tie_s'] = True
            continue
        if g == 'bar':
            fin(); measures.append([]); continue
    fin()
    return measures

def ly_events(meas_events):
    out = []
    t = Fraction(0)
    last_dur = None
    for e in meas_events:
        d = e['dur']
        if d is None:
            d = last_dur if last_dur is not None else 4
        else:
            last_dur = d
        val = Fraction(4, d) * (2 - Fraction(1, 2**e['dots']))
        out.append(dict(onset=t, pitches=e['pitches'], rest=e.get('rest', False),
                        dur=val, dots=e['dots'], args=set(e['args']),
                        tie_s=e['tie_s'], slur_s=e['slur_s'], slur_e=e['slur_e'],
                        grace=e['grace']))
        if not e['grace']: t += val
    return out

XMLSTEP = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
def xml_events(path, pi, mmax):
    root = etree.parse(path).getroot()
    part = root.findall('part')[pi]
    div = 48
    res = {}
    for meas in part.findall('measure'):
        try: num = int(meas.get('number'))
        except: continue
        if num > mmax: break
        d = meas.findtext('attributes/divisions')
        if d: div = int(d)
        cur = Fraction(0); last = Fraction(0); evs = []
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
                    if not grace: last = cur; cur += dur
                else: onset = last
                if el.find('rest') is not None:
                    if not ch:
                        evs.append(dict(onset=onset, pitches=[], rest=True, dur=dur,
                                        dots=len(el.findall('dot')), args=set(),
                                        tie_s=False, slur_s=False, slur_e=False, grace=grace))
                    continue
                p = el.find('pitch')
                midi = 12*(int(p.findtext('octave'))+1)+XMLSTEP[p.findtext('step')]+int(p.findtext('alter') or 0)
                arts = set(a.tag for a in el.findall('notations/articulations/*'))
                arts = set(('tenuto' if a=='detached-legato' else a) for a in arts)
                sl = [s.get('type') for s in el.findall('notations/slur')]
                ti = [t.get('type') for t in el.findall('tie')]
                if ch:
                    e = evs[-1]
                    e['pitches'].append(midi); e['args'] |= arts
                    e['slur_s'] |= ('start' in sl); e['slur_e'] |= ('stop' in sl)
                    e['tie_s'] |= ('start' in ti); e['pitches'].sort()
                else:
                    evs.append(dict(onset=onset, pitches=[midi], rest=False, dur=dur,
                                    dots=len(el.findall('dot')), args=arts,
                                    tie_s=('start' in ti), slur_s=('start' in sl),
                                    slur_e=('stop' in sl), grace=grace))
        res[num] = evs
    return res

def key(e):
    return (e['onset'], tuple(sorted(e['pitches'])), e['rest'], e['dur'], e['dots'],
            tuple(sorted(e['args'])), e['tie_s'], e['slur_s'], e['slur_e'], e['grace'])

def fmt(e):
    return "@%s %s%s dur=%s dots=%d args=%s tie=%s slur=%s/%s grace=%s" % (
        e['onset'], 'REST' if e['rest'] else [nm(p) for p in e['pitches']],
        '', e['dur'], e['dots'], sorted(e['args']), e['tie_s'],
        e['slur_s'], e['slur_e'], e['grace'])

if __name__ == '__main__':
    src = open(sys.argv[1], encoding='utf-8').read()
    xmlp = sys.argv[2]
    mmax = int(sys.argv[3]) if len(sys.argv) > 3 else 21
    total_bad = 0
    for name, pi in (('violin',0), ('cello',1), ('pianoRH',2), ('pianoLH',3)):
        m = re.search(r'^%s\s*=\s*\{(.*?)^\}' % name, src, re.S | re.M)
        body = strip_ly(m.group(1)).replace('\\global', '')
        meas = parse_voice(body)
        xm = xml_events(xmlp, pi, mmax)
        print("\n===== %s: ly measures %d / xml measures %d" % (name, len(meas)-1, len(xm)))
        bad = 0
        for i in range(1, mmax+1):
            A = [key(e) for e in ly_events(meas[i-1])] if i-1 < len(meas) else []
            B = [key(e) for e in xm.get(i, [])]
            if A != B:
                bad += 1
                print("  m.%d  DIFFERENT" % i)
                la = ly_events(meas[i-1]) if i-1 < len(meas) else []
                xb = xm.get(i, [])
                for k in range(max(len(la), len(xb))):
                    a = la[k] if k < len(la) else None
                    b = xb[k] if k < len(xb) else None
                    if a is None or b is None or key(a) != key(b):
                        print("     ly : %s" % (fmt(a) if a else '--'))
                        print("     xml: %s" % (fmt(b) if b else '--'))
        print("  => %s" % ("IDENTICAL (all %d measures)" % mmax if bad == 0 else "%d measure(s) differ" % bad))
        total_bad += bad
    print("\nTOTAL differing measures: %d" % total_bad)

