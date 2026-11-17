"""Minimal absolute-pitch LilyPond event extractor + kern parser + comparator.

Only supports the narrow subset used by the workbench excerpts:
  absolute pitches (c' = C4), durations with dots, chords <...>, rests r/R,
  \partial, \grace (skipped), ties ~, slurs (), articulations, dynamics,
  << >> \\ for simultaneous voices, \clef, \key, \time, \tempo.
"""
import re, sys, json, collections

STEP = {'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
NAME = {0:'C',1:'C#',2:'D',3:'Eb',4:'E',5:'F',6:'F#',7:'G',8:'Ab',9:'A',10:'Bb',11:'B'}

# ---------------------------------------------------------------- lilypond
TOKEN_RE = re.compile(r"""
    (?P<comment>%[^\n]*)
  | (?P<chordopen><<|>>)
  | (?P<chord><[^<>]*>)
  | (?P<bracketopen><)
  | (?P<cmd>\\[A-Za-z][A-Za-z0-9-]*)
  | (?P<frac>\d+/\d+)
  | (?P<pitch>[a-g](?:s|f|t|qs|qf)?(?:'+|,+)?)
  | (?P<num>\d+\.*)
  | (?P<rest>[rR](?![A-Za-z]))
  | (?P<punct>[~()\[\]|.,:;!^_=])
  | (?P<ws>\s+)
  | (?P<other>.)
""", re.X)

def dur_beats(durstr):
    """durstr like '4' '4.' '8' '32' -> beats as fraction of a whole note."""
    m = re.fullmatch(r'(\d+)(\.*)', durstr)
    if not m: return None
    n = int(m.group(1)); dots = len(m.group(2))
    if n == 0: return None
    v = 1.0 / n
    add = v
    for _ in range(dots):
        add /= 2.0
        v += add
    return v

def midi_of(letter, acc, octmark):
    p = STEP[letter]
    if acc == 's': p += 1
    elif acc == 'f': p -= 1
    elif acc == 'qs': p += 0.5
    elif acc == 'qf': p -= 0.5
    elif acc == 't': p += 2
    octv = 3
    if octmark:
        if octmark[0] == "'": octv = 3 + len(octmark)
        else: octv = 3 - len(octmark)
    return 12 * (octv + 1) + p

def parse_ly(path):
    src = open(path, encoding='utf-8').read()
    # strip block comments
    src = re.sub(r'%\{.*?%\}', '', src, flags=re.S)
    events = []           # (measure_index, midi, dur_whole)
    measures = []         # per measure: list of events
    cur = []
    measure_no = 0
    i = 0
    pending_chord = False
    skip_grace = False
    partial = None
    after_partial = False
    in_chord = False
    chord_buf = []
    lineage = 0
    while i < len(src):
        m = TOKEN_RE.match(src, i)
        if not m:
            i += 1; continue
        i = m.end()
        kind = m.lastgroup
        tok = m.group(kind)
        if kind == 'ws': continue
        if kind == 'comment': continue
        if kind == 'chordopen':
            if tok == '<<': lineage += 1
            else: lineage = max(0, lineage - 1)
            continue
        if kind == 'cmd':
            c = tok[1:]
            if c == 'partial':
                # next duration is the leftover
                mm = TOKEN_RE.match(src, i)
                if mm and mm.lastgroup == 'num':
                    partial = dur_beats(mm.group('num')); i = mm.end()
                continue
            if c == 'grace': skip_grace = True; continue
            if c == 'afterGrace': skip_grace = True; continue
            if c in ('clef','key','time','tempo','markup','set','once','omit','undo','override','revert','bar','voiceOne','voiceTwo','voiceThree','voiceFour','oneVoice','relative','transpose','fixed','language','version','header','layout','midi','score','new','with','Staff','PianoStaff','StaffGroup','absolute','fermata','fz','p','pp','f','ff','mf','mp','sf','sfz'):
                continue
            continue
        if kind == 'rest':
            # duration follows
            mm = TOKEN_RE.match(src, i)
            if mm and mm.lastgroup == 'num':
                d = dur_beats(mm.group('num')); i = mm.end()
                mult = 1
                # check for R1*6
                if tok == 'R':
                    mm2 = re.match(r'\s*\*\s*(\d+)', src[i:])
                    if mm2:
                        mult = int(mm2.group(1)); i += mm2.end()
                if d and not skip_grace:
                    for _ in range(mult):
                        cur.append(('R', None, d))
                skip_grace = False
            continue
        if kind == 'chord':
            inner = tok[1:-1]
            pitches = []
            for pm in TOKEN_RE.finditer(r"[a-g](?:s|f|t|qs|qf)?(?:'+|,+)?", inner):
                t = pm.group(0)
                gm = re.fullmatch(r"([a-g])(s|f|t|qs|qf)?('+|,+)?", t)
                pitches.append(midi_of(gm.group(1), gm.group(2), gm.group(3)))
            mm = TOKEN_RE.match(src, i)
            d = None
            if mm and mm.lastgroup == 'num':
                d = dur_beats(mm.group('num')); i = mm.end()
            if d and not skip_grace:
                cur.append(('C', tuple(sorted(pitches)), d))
            skip_grace = False
            continue
        if kind == 'pitch':
            gm = re.fullmatch(r"([a-g])(s|f|t|qs|qf)?('+|,+)?", tok)
            if not gm: continue
            mid = midi_of(gm.group(1), gm.group(2), gm.group(3))
            mm = TOKEN_RE.match(src, i)
            d = None
            if mm and mm.lastgroup == 'num':
                d = dur_beats(mm.group('num')); i = mm.end()
            if d and not skip_grace:
                cur.append(('N', mid, d))
            skip_grace = False
            continue
        if kind == 'punct':
            if tok == '|':
                measures.append(cur); cur = []
                measure_no += 1
            continue
        continue
    if cur: measures.append(cur)
    return measures

# --------------------------------------------------------------------- kern
KERN_OCT = {}
def kern_pitch(tok):
    """tok like 'c#', 'cc', 'e--', 'B', 'g##' -> midi (may be float for q)."""
    m = re.fullmatch(r"([A-Ga-g])(#+|##|-+|--)?", tok)
    if not m: return None
    letter = m.group(1).lower()
    acc = m.group(2) or ''
    p = STEP[letter]
    if acc.startswith('#'): p += len(acc)
    elif acc.startswith('-'): p -= len(acc)
    base = 4 if m.group(1).islower() else 3
    # kern: c = C4, cc = C5, C = C3, CC = C2
    return 12 * (base + 1) + p

def kern_dur(tok):
    m = re.fullmatch(r"(\d+)(\.*)", tok)
    if not m: return None
    n = int(m.group(1)); dots = len(m.group(2))
    if n == 0: v = 2.0
    else: v = 1.0 / n
    add = v
    for _ in range(dots):
        add /= 2.0; v += add
    return v

def parse_kern(path, spine_filter=None):
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    data = []
    nspines = 0
    active = None
    for ln in lines:
        if ln.startswith('**'):
            data.append(ln); nspines = len(ln.split('\t')); break
    measures = []
    cur = [[] for _ in range(nspines)]
    started = False
    for ln in lines:
        if ln.startswith('!'): continue
        if ln.startswith('*'): continue
        if ln.startswith('='):
            if started:
                measures.append(cur)
                cur = [[] for _ in range(nspines)]
            started = True
            continue
        if not started: continue
        cols = ln.split('\t')
        if len(cols) != nspines: continue
        for si, c in enumerate(cols):
            if c in ('.', ''): continue
            for tok in c.split():
                tok = tok.replace('(', '').replace(')', '').replace('[', '').replace(']', '')
                tok = tok.strip('{}<>\\')
                if not tok: continue
                # kern puts the reciprocal duration FIRST: 8E, 2b, 16gg#
                pm = re.fullmatch(r"(\d+\.*)([A-Ga-g](?:#+|-+)?)", tok)
                if pm:
                    d = kern_dur(pm.group(1)); p = kern_pitch(pm.group(2))
                    if p is not None and d:
                        cur[si].append(('N', p, d))
                    continue
                # pitch first (some encoders / tiny notes)
                pm2 = re.fullmatch(r"([A-Ga-g](?:#+|-+)?)(\d+\.*)", tok)
                if pm2:
                    p = kern_pitch(pm2.group(1)); d = kern_dur(pm2.group(2))
                    if p is not None and d:
                        cur[si].append(('N', p, d))
    if started: measures.append(cur)
    return measures

def fmt(ev):
    t, p, d = ev
    if t == 'R': return f"rest/{d:g}"
    if t == 'N': return f"{NAME[int(p)%12]}{int(p)//12-1}/{d:g}"
    return "[" + "+".join(f"{NAME[int(x)%12]}{int(x)//12-1}" for x in p) + f"]/{d:g}"

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'ly':
        ms = parse_ly(sys.argv[2])
        only = sys.argv[3:] and [int(x) for x in sys.argv[3:]]
        for n, mv in enumerate(ms, 1):
            if only and n not in only: continue
            tot = sum(e[2] for e in mv)
            print(f"m{n} total={tot:g} :: " + " ".join(fmt(e) for e in mv))
    elif mode == 'kern':
        ms = parse_kern(sys.argv[2])
        rng = sys.argv[3:]
        for n, mv in enumerate(ms, 1):
            if rng and not (int(rng[0]) <= n <= int(rng[-1])): continue
            for si, sp in enumerate(mv):
                tot = sum(e[2] for e in sp)
                print(f"m{n} spine{si} total={tot:g} :: " + " ".join(fmt(e) for e in sp))
