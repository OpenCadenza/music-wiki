"""Compare a LilyPond excerpt (split into named voice blocks) against a **kern
source, per measure and per staff: pitch multiset, duration multiset, and an
explicit octave-offset histogram (which reveals whole-register errors).

usage:
  python cmp_staff.py <src.krn> <excerpt.ly> <staffMapJSON> <lo> <hi>

staffMapJSON maps staff number -> list of .ly variable names, e.g.
  {"1": ["rhUpper","rhLower","rhThird"], "2": ["lhUpper","lhLower"]}
"""
import sys, re, json, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kern2

STEP = {'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
NAME = {0:'C',1:'C#',2:'D',3:'Eb',4:'E',5:'F',6:'F#',7:'G',8:'Ab',9:'A',10:'Bb',11:'B'}

TOKEN_RE = re.compile(r"""
    (?P<comment>%[^\n]*)
  | (?P<simul><<|>>)
  | (?P<vsep>\\\\)
  | (?P<chord><(?![<])[^<>]*>)
  | (?P<cmd>\\[A-Za-z][A-Za-z0-9-]*)
  | (?P<pitch>[a-g](?:s|f|t|qs|qf)?(?:'+|,+)?(?![a-z]))
  | (?P<num>\d+\.*)
  | (?P<rest>[rR](?![A-Za-z]))
  | (?P<punct>[~()\[\]|.,:;!^_=])
  | (?P<ws>\s+)
  | (?P<other>.)
""", re.X)

SHARP_ORDER = ['f', 'c', 'g', 'd', 'a', 'e', 'b']
FLAT_ORDER = ['b', 'e', 'a', 'd', 'g', 'c', 'f']
MAJOR_SHARPS = {'c': 0, 'g': 1, 'd': 2, 'a': 3, 'e': 4, 'b': 5, 'fs': 6, 'cs': 7}
MAJOR_FLATS = {'f': 1, 'bf': 2, 'ef': 3, 'af': 4, 'df': 5, 'gf': 6, 'cf': 7}
KEYSIG = {}          # letter -> -1/0/+1 default accidental


def set_key(tonic, mode):
    KEYSIG.clear()
    if mode == 'major':
        if tonic in MAJOR_SHARPS:
            for L in SHARP_ORDER[:MAJOR_SHARPS[tonic]]:
                KEYSIG[L] = 1
        elif tonic in MAJOR_FLATS:
            for L in FLAT_ORDER[:MAJOR_FLATS[tonic]]:
                KEYSIG[L] = -1
    else:                                      # minor: relative major
        order = ['a', 'e', 'b', 'fs', 'cs', 'gs', 'ds', 'as']
        rel = {'a': 'c', 'e': 'g', 'b': 'd', 'fs': 'a', 'cs': 'e',
               'gs': 'b', 'ds': 'fs', 'as': 'cs'}
        if tonic in rel:
            set_key(rel[tonic], 'major')


def detect_key(src):
    m = re.search(r'\\key\s+([a-g](?:s|f)?)\s+\\(major|minor)', src)
    if m:
        set_key(m.group(1), m.group(2))
    return KEYSIG


def midi_of(letter, acc, om):
    p = STEP[letter]
    if acc is None and KEYSIG:
        acc = {1: 's', -1: 'f'}.get(KEYSIG.get(letter, 0))
    if acc == 's': p += 1
    elif acc == 'f': p -= 1
    elif acc == 'qs': p += 0.5
    elif acc == 'qf': p -= 0.5
    elif acc == 't': p += 2
    o = 3
    if om:
        o = 3 + len(om) if om[0] == "'" else 3 - len(om)
    return 12 * (o + 1) + p

def dur_of(s):
    m = re.fullmatch(r'(\d+)(\.*)', s)
    if not m: return None
    n = int(m.group(1)); dots = len(m.group(2))
    if n == 0: return None
    v = 1.0 / n; add = v
    for _ in range(dots):
        add /= 2.0; v += add
    return v

def parse_block(src):
    """return list of measures; each measure = list of ('N',midi,dur) / ('R',None,dur)"""
    measures, cur = [], []
    i, skip_grace, in_aftergrace = 0, False, False
    while i < len(src):
        m = TOKEN_RE.match(src, i)
        if not m:
            i += 1; continue
        i = m.end(); k = m.lastgroup; t = m.group(k)
        if k in ('ws', 'comment', 'simul', 'vsep'):
            continue
        if k == 'punct':
            if t == '|':
                measures.append(cur); cur = []
            continue
        if k == 'cmd':
            c = t[1:]
            if c == 'grace':
                # skip the grace note AND anything up to its end (notes are single)
                skip_grace = True
            elif c == 'partial':
                mm = re.match(r'\s*(\d+\.*)', src[i:])
                if mm: i += mm.end()
            elif c in ('afterGrace',):
                in_aftergrace = True
            continue
        if k == 'rest':
            mm = re.match(r'\s*(\d+\.*)', src[i:])
            d = None
            if mm:
                d = dur_of(mm.group(1)); i += mm.end()
            mult = 1
            if t == 'R':
                mm2 = re.match(r'\s*\*\s*(\d+)', src[i:])
                if mm2:
                    mult = int(mm2.group(1)); i += mm2.end()
            if d and not in_aftergrace:
                if mult > 1:
                    for k in range(mult):
                        cur.append(('R', None, d))
                        if k < mult - 1:
                            measures.append(cur); cur = []
                else:
                    cur.append(('R', None, d))
            skip_grace = False
            continue
        if k == 'chord':
            ps = [midi_of(mm.group(1), mm.group(2), mm.group(3))
                  for mm in re.finditer(r"([a-g])(s|f|t|qs|qf)?('+|,+)?", t[1:-1])]
            mm = re.match(r'\s*(\d+\.*)', src[i:])
            d = None
            if mm: d = dur_of(mm.group(1)); i += mm.end()
            if d and not skip_grace and not in_aftergrace:
                cur.append(('C', tuple(sorted(ps)), d))
            skip_grace = False
            continue
        if k == 'pitch':
            gm = re.fullmatch(r"([a-g])(s|f|t|qs|qf)?('+|,+)?", t)
            mid = midi_of(gm.group(1), gm.group(2), gm.group(3))
            mm = re.match(r'\s*(\d+\.*)', src[i:])
            d = None
            if mm: d = dur_of(mm.group(1)); i += mm.end()
            if d and not skip_grace and not in_aftergrace:
                cur.append(('N', mid, d))
            skip_grace = False
    if cur: measures.append(cur)
    return measures

def split_vars(text):
    """extract `name = { ... }` blocks (brace-balanced)."""
    out = collections.OrderedDict()
    for m in re.finditer(r'^\s*([A-Za-z][A-Za-z0-9_]*)\s*=\s*\{', text, re.M):
        name = m.group(1)
        start = m.end() - 1
        depth = 0; i = start
        while i < len(text):
            ch = text[i]
            if ch == '{': depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0: break
            i += 1
        out[name] = text[start + 1:i]
    return out

def nm(p):
    return '%s%d' % (NAME[int(p) % 12], int(p) // 12 - 1)

def expansions(ev):
    """flatten chord events into (midi,dur) pairs; rests skipped"""
    res = []
    for t, p, d in ev:
        if t == 'N': res.append((p, d))
        elif t == 'C':
            for x in p: res.append((x, d))
    return res

def main():
    main_args(sys.argv[1], sys.argv[2], json.loads(sys.argv[3]),
              int(sys.argv[4]), int(sys.argv[5]))

def main_args(krn, ly, smap, lo, hi):
    text = open(ly, encoding='utf-8').read()
    detect_key(text)
    blocks = split_vars(text)
    ly_meas = {k: parse_block(v) for k, v in blocks.items()}

    src = kern2.parse(krn)
    srcby = {}
    for m in src:
        try: n = int(m['label'])
        except ValueError: continue
        srcby[n] = m['onsets']

    print(f"== {os.path.basename(ly)}  vs  {os.path.basename(krn)} ==\n")
    for staff_key, varnames in smap.items():
        st = int(staff_key)
        # build per-measure combined events from the listed variables
        comb = {}
        for v in varnames:
            if v not in ly_meas:
                print(f"  !! variable not found: {v}"); continue
            for n, mv in enumerate(ly_meas[v], 1):
                comb.setdefault(n, []).extend(mv)
        for n in range(lo, hi + 1):
            a = expansions(comb.get(n, []))
            b = []
            for d, ps in srcby.get(n, {}).get(st, []):
                for x in ps:
                    if d: b.append((x, d))
            A = collections.Counter(a); B = collections.Counter(b)
            SA = set(x for x, _ in a); SB = set(x for x, _ in b)
            totA = sum(d for _, d in a); totB = sum(d for _, d in b)
            ok = 'OK  ' if A == B else 'DIFF'
            sok = 'OK  ' if SA == SB else 'SET!'
            print(f"[{ok}/{sok}] m{n} staff{st}  ly={totA:g} kern={totB:g}")
            if SA != SB:
                miss = sorted(SB - SA); extra = sorted(SA - SB)
                if miss:  print('        kern-only pitches: ' + ', '.join(nm(x) for x in miss))
                if extra: print('        ly-only   pitches: ' + ', '.join(nm(x) for x in extra))
                continue
            if A != B:
                onlyA = A - B; onlyB = B - A
                if onlyA: print('        only-in-ly  : ' + ', '.join(f'{nm(p)}/{d:g}' for (p, d) in sorted(onlyA.elements())))
                if onlyB: print('        only-in-kern: ' + ', '.join(f'{nm(p)}/{d:g}' for (p, d) in sorted(onlyB.elements())))
                pca = collections.Counter(p % 12 for p, _ in a)
                pcb = collections.Counter(p % 12 for p, _ in b)
                if pca == pcb:
                    off = collections.Counter(int(p) - int(q) for p, q in zip(sorted(x for x, _ in a), sorted(x for x, _ in b)))
                    print('        pitch-classes MATCH but octaves differ; offsets:', dict(off))
        print()

if __name__ == '__main__':
    main()
