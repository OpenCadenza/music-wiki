"""补充证据：tie 清册、音域、cemba2 是否被 cemba3 覆盖、BWV mm.1-9 是否有 tie"""
from kernly import (parse_kern_tokens, kern_stream2, kern_measure_onsets,
                    ly_parse, ly_stream, nm)

BASE = r'E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local'
LY = r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s3'

HAY = BASE + r'\origin_resources\downloads\2026-11-17\s3\haydn104-1.krn'
BWV = BASE + r'\origin_resources\downloads\2026-11-17\s3\bwv1050-1.krn'
OP74 = BASE + r'\resources\scores\source-packages\beethoven-score-sources\beethoven-string-quartets-main\beethoven-string-quartets-main\kern\quartet10-1.krn'

# ---------- 1. tie 清册 ----------
def tie_inventory(path, spines, m0, m1, tag):
    toks, kinds, labels = parse_kern_tokens(path)
    print(f'--- [{tag}] kern 中的 tie（mm.{m0}-{m1}）---')
    total = 0
    for sp, name in spines:
        ts = [t for t in toks[sp] if m0 <= t['meas'] <= m1]
        mo = kern_measure_onsets(toks[sp])
        base = mo[m0]
        items = []
        for i, t in enumerate(ts):
            if t['ts']:
                nxt = next((u for u in ts[i + 1:] if u['pitches'] == t['pitches']), None)
                items.append((t['meas'], round(t['onset'] - base, 2),
                              '/'.join(nm(p) for p in t['pitches']), t['dur'],
                              (nxt['meas'], round(nxt['onset'] - base, 2)) if nxt else None))
        print(f'  {name:16s}: {len(items)} 处 tie')
        for it in items:
            print(f'      m.{it[0]} @{it[1]:<6g} {it[2]:10s} dur={it[3]:g} → '
                  + (f'm.{it[4][0]} @{it[4][1]:g}' if it[4] else '?'))
        total += len(items)
    print(f'  合计 {total} 处\n')


tie_inventory(BWV, [(8, 'Flauto'), (7, 'VlnPrinc'), (6, 'VlnRip'),
                    (5, 'Viola'), (4, 'Vc'), (3, 'Violone'),
                    (2, 'Cemba3/Upper'), (0, 'Cemba1/Lower')], 1, 9, 'BWV1050')
tie_inventory(HAY, [(4, 'Vln I'), (3, 'Vln II'), (2, 'Va'), (1, 'Vc'), (0, 'Cb')],
              17, 32, 'Haydn104')
tie_inventory(OP74, [(6, 'Vln I'), (4, 'Vln II'), (2, 'Va'), (0, 'Vc')], 6, 9, 'Op74')

# ---------- 2. .ly 音域 ----------
print('--- .ly 音域（MIDI 事件）---')
for tag, ly, mapv in [
    ('BWV1050', LY + r'\bach-bwv1050-mvt1-mm1-9-tutti.ly', None),
    ('Haydn104', LY + r'\haydn-hob-i-104-mvt1-mm17-32-strings.ly', None),
    ('Op74', LY + r'\beethoven-op74-mvt1-mm6-9-adagio.ly', None)]:
    lys, vardefs = ly_parse(ly)
    print(f'  [{tag}]')
    allm = []
    for var in [v for v in lys if v != 'global']:
        ev, bars, part = ly_stream(lys[var])
        if not ev:
            continue
        ms = [e[1] for e in ev]
        allm += ms
        print(f'    {var:20s} {nm(min(ms)):5s} – {nm(max(ms)):5s}  ({min(ms)}–{max(ms)})  {len(ms)} 音')
    print(f'    全体: {nm(min(allm))} – {nm(max(allm))}, 共 {len(allm)} 音')

# ---------- 3. cemba2 是否被 cemba3/cemba1 覆盖 ----------
print('\n--- BWV1050: kern 三行大键琴 mm.1-9 逐小节音集 ---')
toks, kinds, labels = parse_kern_tokens(BWV)
for m in range(1, 10):
    s = {}
    for sp in (0, 1, 2):
        ts = [t for t in toks[sp] if t['meas'] == m]
        pit = set()
        for t in ts:
            for p in t['pitches']:
                if p is not None:
                    pit.add(p)
        s[sp] = pit
    cov = (s[1] <= (s[0] | s[2]))
    print(f'  m.{m}: cemba1={sorted(nm(x) for x in s[0])}  cemba2={sorted(nm(x) for x in s[1])}  '
          f'cemba3={sorted(nm(x) for x in s[2])}  cemba2⊆(cemba1∪cemba3)? {cov}')
