"""Per-voice pitch range (and bar totals) for an excerpt .ly, key-aware."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cmp_staff as C

NAME = C.NAME
RANGES = {
    'violinOne': ('Vn1', 55, 96),      # G3..C8 (limit stated G3)
    'violinTwo': ('Vn2', 55, 96),
    'viola': ('Va', 48, 84),           # C3..C6
    'cello': ('Vc', 36, 84),           # C2..C6
    'rhUpper': ('Pf(RH)', 21, 108), 'rhLower': ('Pf(RH)', 21, 108),
    'rhThird': ('Pf(RH)', 21, 108),
    'lhUpper': ('Pf(LH)', 21, 108), 'lhLower': ('Pf(LH)', 21, 108),
    'violoncello': ('Vc', 36, 84),
}


def nm(p):
    return '%s%d' % (NAME[int(p) % 12], int(p) // 12 - 1)


def main(path):
    text = open(path, encoding='utf-8').read()
    C.detect_key(text)
    blocks = C.split_vars(text)
    print('file:', os.path.basename(path), ' keysig:', dict(C.KEYSIG))
    print('%-10s %-8s %-9s %-9s %-9s %s' % ('var', 'staff', 'lowest', 'highest', 'notes', 'totals/measure'))
    for name, body in blocks.items():
        ms = C.parse_block(body)
        if not ms:
            continue
        ps = []
        for mv in ms:
            for t, p, d in mv:
                if t == 'N':
                    ps.append(p)
                elif t == 'C':
                    ps.extend(p)
        if not ps:
            print('%-10s %-8s (all rests)' % (name, ''))
            continue
        label = RANGES.get(name, ('?', 0, 127))[0]
        lo, hi = min(ps), max(ps)
        rlo, rhi = RANGES.get(name, ('?', 0, 127))[1:]
        flag = '' if (lo >= rlo and hi <= rhi) else '   <== OUT OF RANGE'
        print('%-10s %-8s %-9s %-9s %-9d %s%s' % (
            name, label, nm(lo), nm(hi), len(ps),
            ','.join('%g' % round(sum(e[2] for e in mv if e[0] != 'R'), 4) for mv in ms), flag))
        print('           allowed %s..%s' % (nm(rlo), nm(rhi)))


if __name__ == '__main__':
    for p in sys.argv[1:]:
        main(p)
