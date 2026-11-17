#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Op.74 mm.18-24：Kern vs DCML notes.tsv 对照（按 声部/拍位/音高/时值）。"""
import csv, re, sys, os

NAME = ['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B']
def fmt(m): return f"{NAME[m%12]}{m//12-1}"

PITCH = {'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}

def kern_notes(path):
    spines = None; meas = 0; beat = []; out = {}
    for line in open(path, encoding='utf-8', errors='replace'):
        line = line.rstrip('\n')
        if line.startswith('**'):
            spines = line.split('\t'); beat = [0.0]*len(spines); continue
        if line.startswith('!') or line.startswith('*'): continue
        toks = line.split('\t')
        if spines is None or len(toks) != len(spines): continue
        if toks[0].startswith('='):
            mm = re.match(r'(\d+)', toks[0][1:])
            if mm: meas = int(mm.group(1))
            beat = [0.0]*len(spines); continue
        for i, tk in enumerate(toks):
            if tk.strip() in ('', '.'): continue
            step = 0.0
            for part in tk.split(' '):
                p = part
                if p[:1] in '([': p = p[1:]
                if p.endswith(']'): p = p[:-1]
                m = re.match(r'^(\d+)(\.*)(.*)$', p)
                if not m: continue
                num = int(m.group(1)); dots = len(m.group(2)); rest = m.group(3)
                dur = 4.0/num; add = dur
                for _ in range(dots): add /= 2.0; dur += add
                step = max(step, dur)
                pm = re.match(r'^([a-gA-G]+)((?:#|-|n|X|Y)*)', rest)
                if not pm: continue
                L = pm.group(1); acc = pm.group(2)
                pc = PITCH[L[0].lower()]; n = len(L)
                octv = 4 + (n-1) if L[0].islower() else 4 - n
                for ch in acc:
                    if ch == '#': pc += 1
                    elif ch == '-': pc -= 1
                    elif ch == 'Y': pc -= 2
                out.setdefault((meas, i), []).append((round(beat[i],3), (octv+1)*12+pc, round(dur,3)))
            beat[i] += step
    return out

def dcml_notes(path):
    out = {}
    with open(path, encoding='utf-8') as f:
        rd = csv.DictReader(f, delimiter='\t')
        for r in rd:
            try: mn = int(r['mn'])
            except: continue
            if mn < 18 or mn > 24: continue
            qb = r['quarterbeats']
            qb = float(qb) if '/' not in qb else eval(qb)
            onset = 68 + (mn-18)*4
            staff = int(r['staff'])
            out.setdefault((mn, staff), []).append((round(qb-onset,3), int(r['midi']), float(r['duration_qb']), r['tied']))
    return out

def main():
    kb = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores"
    kf = kb + r"\source-packages\beethoven-score-sources\beethoven-string-quartets-main\beethoven-string-quartets-main\kern\quartet10-1.krn"
    tf = kb + r"\dcml-abc\n10op74_01.notes.tsv"
    k = kern_notes(kf)
    d = dcml_notes(tf)
    # kern spine: cello=0, viola=2, vn2=4, vn1=6 ; dcml staff: 1=vn1,2=vn2,3=viola,4=cello
    pairs = {6:1, 4:2, 2:3, 0:4}
    for spine, staff in pairs.items():
        print("="*70)
        print(f"spine {spine} <-> staff {staff}")
        for m in range(18, 25):
            kn = sorted(k.get((m, spine), []))
            dn = sorted(d.get((m, staff), []))
            # 合并同时发声的音
            def agg(lst):
                g = {}
                for b, p, dd, *_ in lst:
                    g.setdefault((b, round(float(dd),3)), []).append(p)
                return [(b, tuple(sorted(ps)), dd) for (b,dd), ps in sorted(g.items())]
            ka, da = agg(kn), agg(dn)
            if ka != da:
                print(f"  m.{m}  <-- 不一致")
                print("    Kern: " + " | ".join(f"b{b:g}:{'/'.join(fmt(p) for p in ps)}({dd:g})" for b,ps,dd in ka))
                print("    DCML: " + " | ".join(f"b{b:g}:{'/'.join(fmt(p) for p in ps)}({dd:g})" for b,ps,dd in da))
    print("\n(未列出的小节 = Kern 与 DCML 完全一致)")

if __name__ == '__main__':
    main()
