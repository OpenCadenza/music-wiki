"""kern -> per-onset events (onset = one data line), grouped by staff.

Prints, per measure and per staff: ordered list of 'pitch/dur' with chords as
<P+Q>/dur, so pitch AND duration can be compared with a LilyPond excerpt.
"""
import re, sys, collections

BASE = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
NAME = {0:'C',1:'C#',2:'D',3:'Eb',4:'E',5:'F',6:'F#',7:'G',8:'Ab',9:'A',10:'Bb',11:'B'}
NOTE = re.compile(r'^(\d+\.*)?([a-gA-G]+)(##|#|--|-|n)?')

def pitch_of(tok):
    m = NOTE.match(tok)
    if not m:
        return None
    letters, acc = m.group(2), m.group(3)
    letter = letters[0].upper()
    octv = 3 - (len(letters) - 1) if letters[0].isupper() else 4 + (len(letters) - 1)
    semis = {'#': 1, '##': 2, '-': -1, '--': -2, 'n': 0, None: 0}[acc]
    return (octv + 1) * 12 + BASE[letter] + semis

def dur_of(tok):
    m = re.match(r'^(\d+)(\.*)', tok)
    if not m:
        return None
    n = int(m.group(1)); dots = len(m.group(2))
    v = 2.0 if n == 0 else 1.0 / n
    add = v
    for _ in range(dots):
        add /= 2.0; v += add
    return v

def _runs(idx):
    out = []
    for i in idx:
        if out and i == out[-1][-1] + 1:
            out[-1].append(i)
        else:
            out.append([i])
    return out


def parse(path):
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    staff_of = []
    measures = []
    cur = None
    started = False
    for ln in lines:
        if ln.startswith('**'):
            staff_of = [None] * len(ln.split('\t'))
            started = True
            continue
        if not started or not ln.strip():
            continue
        if ln.startswith('!'):
            continue
        toks = ln.split('\t')
        if ln.startswith('*'):
            for i, t in enumerate(toks):
                if t.startswith('*staff') and i < len(staff_of):
                    staff_of[i] = int(re.match(r'\*staff(\d+)', t).group(1))
            # a *^ pair is undone by a consecutive run of *v marks: the run
            # collapses to its leftmost spine (keep first, drop the rest).
            vidx = [i for i, t in enumerate(toks) if t == '*v']
            for run in _runs(vidx):
                for i in reversed(run[1:]):
                    if i < len(staff_of):
                        del staff_of[i]
            for i in reversed([i for i, t in enumerate(toks) if t == '*^']):
                if i < len(staff_of):
                    staff_of.insert(i + 1, staff_of[i])
            continue
        if toks[0].startswith('='):
            m = re.match(r'=+([0-9]+)', toks[0])
            cur = collections.defaultdict(list)
            measures.append(dict(label=m.group(1) if m else '?', onsets=cur))
            continue
        if cur is None:
            continue
        for i, t in enumerate(toks):
            if i >= len(staff_of):
                break
            st = staff_of[i]
            if st is None:
                st = 1
            if t.strip() in ('.', ''):
                continue
            toks = t.split()
            if re.match(r'^[0-9.]*[rR]', toks[0]):
                cur[st].append((None, ()))
                continue
            dur = None; ps = []
            for sub in toks:
                if re.match(r'^[0-9.]*[rR]', sub):
                    continue
                core = re.sub(r'[^0-9A-Ga-g#.-]', '', sub)
                core = re.sub(r'[rR]', '', core)
                d = dur_of(core)
                if d is not None and dur is None:
                    dur = d
                p = pitch_of(core)
                if p is not None:
                    ps.append(p)
            if ps:
                cur[st].append((dur, tuple(sorted(ps))))
    return measures

def nm(p):
    return '%s%d' % (NAME[p % 12], p // 12 - 1)

def show(path, lo, hi):
    for m in parse(path):
        try:
            n = int(m['label'])
        except ValueError:
            continue
        if not (lo <= n <= hi):
            continue
        for st in sorted(m['onsets']):
            ev = m['onsets'][st]
            tot = sum((d or 0) for d, _ in ev)
            parts = []
            for d, ps in ev:
                if not ps:
                    parts.append('r/%g' % (d or 0))
                elif len(ps) == 1:
                    parts.append('%s/%g' % (nm(ps[0]), d or 0))
                else:
                    parts.append('<%s>/%g' % ('+'.join(nm(x) for x in ps), d or 0))
            print('m%-4d staff%d tot=%g :: %s' % (n, st, tot, ' '.join(parts)))

if __name__ == '__main__':
    show(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
