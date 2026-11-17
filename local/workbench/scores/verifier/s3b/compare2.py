"""逐音比对 v2：把 kern / lily 都归一成“发声事件”（同起点和弦合并、tie 合并），
再按起点对齐比较音高集合与时值。

用法: python compare2.py [tag]
"""
import sys
from kernly import (parse_kern_tokens, kern_stream2, kern_measure_onsets, ly_parse, ly_stream, nm)

BASE = r'E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local'
LY = r'E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s3'

WORKS = [
    dict(tag='BWV1050',
         kern=BASE + r'\origin_resources\downloads\2026-11-17\s3\bwv1050-1.krn',
         ly=LY + r'\bach-bwv1050-mvt1-mm1-9-tutti.ly', m0=1, m1=9,
         map=[('flauto', 8), ('violinoPrincipale', 7), ('violinoRipieno', 6),
              ('viola', 5), ('violoncello', 4), ('violone', 3),
              ('cembaloUpper', 2), ('cembaloLower', 0)],
         extra_spines=[]),
    dict(tag='Haydn104',
         kern=BASE + r'\origin_resources\downloads\2026-11-17\s3\haydn104-1.krn',
         ly=LY + r'\haydn-hob-i-104-mvt1-mm17-32-strings.ly', m0=17, m1=32,
         map=[('violinOne', 4), ('violinTwo', 3), ('viola', 2), ('cello', 1), ('bass', 0)],
         extra_spines=[(5, 'Timpani'), (6, 'Tromba2'), (7, 'Tromba1'), (8, 'Corno2'),
                       (9, 'Corno1'), (10, 'Fagotto2'), (11, 'Fagotto1'),
                       (12, 'Clar2'), (13, 'Clar1'), (14, 'Oboe2'), (15, 'Oboe1'),
                       (16, 'Flauto2'), (17, 'Flauto1')]),
    dict(tag='Op74',
         kern=BASE + r'\resources\scores\source-packages\beethoven-score-sources\beethoven-string-quartets-main\beethoven-string-quartets-main\kern\quartet10-1.krn',
         ly=LY + r'\beethoven-op74-mvt1-mm6-9-adagio.ly', m0=6, m1=9,
         map=[('violinOne', 6), ('violinTwo', 4), ('viola', 2), ('cello', 0)],
         extra_spines=[]),
]


def run(work):
    toks, kinds, labels = parse_kern_tokens(work['kern'])
    if labels and len(labels) != len(kinds):
        labels = None
    lys, vardefs = ly_parse(work['ly'])
    m0, m1 = work['m0'], work['m1']
    print('=' * 80)
    print(f"[{work['tag']}]  kern 声部: {labels}")
    print(f"  小节范围: m.{m0}–m.{m1}")
    grand_ok = True
    for lvar, sp in work['map']:
        all_t = toks[sp]
        mo = kern_measure_onsets(all_t)
        base = mo.get(m0, 0.0)
        kt = [dict(t, onset=round(t['onset'] - base, 8))
              for t in all_t if m0 <= t['meas'] <= m1]
        kev = kern_stream2(kt)
        lev = lys.get(lvar)
        if lev is None:
            print(f'  !! 缺少变量 {lvar}')
            grand_ok = False
            continue
        levs, lbars, partials = ly_stream(lev)
        # ly 事件：同起点合并
        lyev = {}
        for pos, midi, dur, bar in levs:
            lyev.setdefault(round(pos, 6), []).append((midi, round(dur, 6)))
        kd = {round(e['onset'], 6): (sorted(e['pitches']), round(e['dur'], 6))
              for e in kev if any(p is not None for p in e['pitches'])}
        allpos = sorted(set(kd) | set(lyev))
        # 只保留至少一侧有音的起点
        allpos = [p for p in allpos if kd.get(p) or lyev.get(p)]
        miss, bad_pitch, bad_dur, tiesplit = [], [], [], []
        for p in allpos:
            kp = kd.get(p)
            lp = lyev.get(p)
            if kp is None:
                tiesplit.append(p)
                continue
            if lp is None:
                miss.append(p)
                continue
            kpit, kdur = kp
            lpit = sorted(x[0] for x in lp)
            ldur = max(x[1] for x in lp)
            if kpit != lpit:
                bad_pitch.append((p, kpit, lpit))
            elif abs(kdur - ldur) > 1e-6:
                bad_dur.append((p, kdur, ldur))
        # 小节边界：kern 各小节起点（m0+1..m1）应出现在 .ly 的小节线位置里
        km = kern_measure_onsets(kt)
        exp = sorted(km[m] for m in range(m0 + 1, m1 + 1) if m in km)
        bar_ok = all(any(abs(v - e) < 1e-6 for v in lbars) for e in exp)
        bar_msg = ([] if bar_ok else
                   [f'kern 小节起点 {e:g} 无对应 .ly 小节线' for e in exp
                    if not any(abs(v - e) < 1e-6 for v in lbars)])
        tot_k = round(exp[-1] + 4.0, 6) if exp else 0
        if abs(lbars[-1] - tot_k) > 1e-6:
            bar_ok = False
            bar_msg.append(f'末小节线 .ly={lbars[-1]:g} kern={tot_k:g}')
        n_ok = not (miss or bad_pitch or bad_dur)
        print(f"  [{lvar}] kern {len(kev)} 事件 / ly {len(lyev)} 起点 → "
              f"{'✓ 完全一致' if n_ok else '✗'}"
              + (f"; .ly 多出起点(tie 拆分) {len(tiesplit)} 处: {[f'{x:g}' for x in tiesplit]}" if tiesplit else '')
              + ('' if bar_ok else f'; 小节线问题 {bar_msg}'))
        if miss:
            print(f'      .ly 缺少起点: {[f"{x:g}" for x in miss]}')
        for p, a, b in bad_pitch[:12]:
            print(f'      起点 {p:g}: kern={[nm(x) for x in a]}  ly={[nm(x) for x in b]}')
        for p, a, b in bad_dur[:12]:
            print(f'      起点 {p:g}: 时值 kern={a} ly={b}')
        grand_ok = grand_ok and n_ok and bar_ok
    # 管乐/铜管/定音鼓在范围内是否有音
    if work['extra_spines']:
        print('  --- 非弦乐声部在范围内发声情况 ---')
        for sp, lab in work['extra_spines']:
            kt = [t for t in toks[sp] if m0 <= t['meas'] <= m1]
            real = [t for t in kt if any(m is not None for m in t['pitches'])]
            print(f"    {lab:10s}: 有音符的 token 数 = {len(real)}"
                  + (f"  → 小节 {sorted(set(t['meas'] for t in real))}" if real else '  → 全区休止'))
    print(f"  ⇒ {work['tag']} 结论: {'一致' if grand_ok else '存在差异'}")
    return grand_ok


if __name__ == '__main__':
    only = sys.argv[1].lower() if len(sys.argv) > 1 else None
    for w in WORKS:
        if only and only not in w['tag'].lower():
            continue
        run(w)
