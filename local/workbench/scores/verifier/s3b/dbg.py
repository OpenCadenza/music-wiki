from kernly import parse_kern_tokens, nm
BASE = r'E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local'
toks, kinds, labels = parse_kern_tokens(
    BASE + r'\origin_resources\downloads\2026-11-17\s3\haydn104-1.krn')
for sp, name in ((1, 'Violoncello'), (4, 'ViolinoI'), (3, 'ViolinoII'), (0, 'Contrabasso')):
    print('=== ' + name)
    for m in range(17, 33):
        ts = [t for t in toks[sp] if t['meas'] == m]
        tot = sum(t['dur'] for t in ts)
        desc = ' '.join(
            ('r' if t['pitches'][0] is None else '/'.join(nm(p) for p in t['pitches']))
            + '@%.2f[%s]' % (t['dur'], ('T' if t['ts'] else '') + ('E' if t['te'] else ''))
            for t in ts)
        print(' m%-3d onset=%7.2f sum=%.2f : %s' % (
            m, ts[0]['onset'] if ts else -1, tot, desc))
