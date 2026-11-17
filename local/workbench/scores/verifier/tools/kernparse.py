"""Minimal **kern reader with spine split/merge handling.

Returns measures keyed by the number of the barline that *starts* them; data
before the first barline is the pickup (measure '0').  Notes are grouped by the
staff declared with *staffN, following *^ splits and *v merges.
"""
import re, sys, collections

PITCH = re.compile(r'^[0-9.]+([a-gA-G]+)(##|#|--|-|n)?')
BASE = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
ACC = {'#': 1, '##': 2, '-': -1, '--': -2, 'n': 0, None: 0}


def pitch_of(tok):
    m = PITCH.match(tok)
    if not m:
        return None
    letters, acc = m.group(1), m.group(2)
    letter = letters[0].upper()
    octv = 3 - (len(letters) - 1) if letter == letters[0] else 4 + (len(letters) - 1)
    return (octv + 1) * 12 + BASE[letter] + ACC[acc], letters + (acc or '')


def parse(path):
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    staff_of = []
    measures = [dict(label='0', notes=collections.defaultdict(list))]
    started = False
    for ln in lines:
        if ln.startswith('**'):
            n = len(ln.split('\t'))
            staff_of = [None] * n
            started = True
            continue
        if not started or not ln.strip():
            continue
        if ln.startswith('!!!') or ln.startswith('!'):
            continue
        toks = ln.split('\t')
        if ln.startswith('*'):
            splits = [i for i, t in enumerate(toks) if t == '*^']
            merges = [i for i, t in enumerate(toks) if t == '*v']
            for i in range(len(toks)):
                if i < len(staff_of) and toks[i].startswith('*staff'):
                    m = re.match(r'\*staff(\d+)', toks[i])
                    if m:
                        staff_of[i] = int(m.group(1))
            # spine merges first (remove the following spine), right to left
            for i in reversed(merges):
                if i + 1 < len(staff_of):
                    del staff_of[i + 1]
            # then splits, right to left so indices stay valid
            for i in reversed(splits):
                if i < len(staff_of):
                    staff_of.insert(i + 1, staff_of[i])
            continue
        if toks[0].startswith('='):
            m = re.match(r'=+([0-9]+)', toks[0])
            measures.append(dict(label=m.group(1) if m else '?',
                                 notes=collections.defaultdict(list)))
            continue
        cur = measures[-1]
        for i, t in enumerate(toks):
            if i >= len(staff_of):
                break
            st = staff_of[i]
            if st is None:
                st = 1 if i else 2
            for sub in t.split():
                p = pitch_of(sub)
                if p:
                    cur['notes'][st].append(p)
    return measures


def show(path, first, last):
    for m in parse(path):
        try:
            n = int(m['label'])
        except ValueError:
            continue
        if first <= n <= last:
            print('m%-4s' % m['label'], ' | '.join(
                's%d: %s' % (st, ' '.join('%d%s' % p for p in ps))
                for st, ps in sorted(m['notes'].items())))


if __name__ == '__main__':
    show(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
