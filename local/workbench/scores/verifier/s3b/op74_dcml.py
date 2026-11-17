"""Op.74 双源交叉核对：kern 与 DCML notes.tsv 的 mm.6-9 逐音比对"""
import csv
from kernly import parse_kern_tokens, kern_stream2, kern_measure_onsets, nm

BASE = r'E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local'
OP74 = BASE + r'\resources\scores\source-packages\beethoven-score-sources\beethoven-string-quartets-main\beethoven-string-quartets-main\kern\quartet10-1.krn'
TSV = BASE + r'\resources\scores\dcml-abc\n10op74_01.notes.tsv'

toks, kinds, labels = parse_kern_tokens(OP74)
rows = list(csv.DictReader(open(TSV, encoding='utf-8'), delimiter='\t'))
staff2spine = {1: 6, 2: 4, 3: 2, 4: 0}
names = {1: 'Vln I', 2: 'Vln II', 3: 'Viola', 4: 'Vc'}

print('=== Op.74 m.6–9: kern vs DCML notes.tsv 逐音 ===')
for st in (1, 2, 3, 4):
    sp = staff2spine[st]
    all_t = toks[sp]
    mo = kern_measure_onsets(all_t)
    base = mo[6]
    kt = [dict(t, onset=round(t['onset'] - base, 6)) for t in all_t if 6 <= t['meas'] <= 9]
    kev = kern_stream2(kt)
    # DCML：mc 6..9，quarterbeats 起点相对 mc6（dcml mc6 起点 = 20）
    d = {}
    for r in rows:
        if r['staff'] != str(st):
            continue
        mc = int(r['mc'])
        if not (6 <= mc <= 9):
            continue
        pos = float(__import__('fractions').Fraction(r['quarterbeats'])) - 20.0
        d.setdefault(round(pos, 6), []).append(
            (int(r['midi']), float(__import__('fractions').Fraction(r['duration_qb'])),
             r['name'], r['tied']))
    kd = {round(e['onset'], 6): (sorted(e['pitches']), round(e['dur'], 6))
          for e in kev if any(p is not None for p in e['pitches'])}
    ok = True
    for p in sorted(set(kd) | set(d)):
        k = kd.get(p)
        dd = d.get(p)
        if k is None or dd is None:
            print(f'  [{names[st]}] 起点 {p}: kern={k} dcml={dd}  ← 单侧缺失')
            ok = False
            continue
        kpit, kdur = k
        dpit = sorted(x[0] for x in dd)
        ddur = sum(x[1] for x in dd)   # 和弦内多音同时值
        ddur = max(x[1] for x in dd)
        if kpit != dpit or abs(kdur - ddur) > 1e-6:
            print(f'  [{names[st]}] 起点 {p}: kern={[nm(x) for x in kpit]}/{kdur}  '
                  f'dcml={[nm(x) for x in dpit]}/{ddur}  ← 差异')
            ok = False
    print(f'  [{names[st]}] {"✓ 两源一致" if ok else "有差异"}（kern {len(kd)} 起点 / dcml {len(d)} 起点）')

print('\n=== 文章校勘点（DCML midi 值）===')
for r in rows:
    if int(r['mc']) == 7 and r['staff'] == '4':
        print(f"  m.7 Vc: {r['name']}{r['octave']} midi={r['midi']} dur={r['duration_qb']}  ← 应为 Bb2 / 46")
    if int(r['mc']) == 6 and r['staff'] == '2':
        print(f"  m.6 VlnII: {r['name']}{r['octave']} midi={r['midi']} dur={r['duration_qb']}")
    if int(r['mc']) == 6 and r['staff'] == '3' and r['name'] == 'Cb':
        print(f"  m.6 Vla: {r['name']}{r['octave']} midi={r['midi']} dur={r['duration_qb']}")
    if int(r['mc']) == 9 and r['staff'] == '1':
        print(f"  m.9 VlnI: {r['name']}{r['octave']} midi={r['midi']} qb={r['quarterbeats']} d={r['duration_qb']} tie={r['tied']}")
