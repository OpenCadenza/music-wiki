#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""S1 谱例核验：Kern 源 vs LilyPond .ly 逐音 / 逐时值 / 拍位对照。

Kern 采用「每 spine 独立时钟」读法（null 记号表示延续，不推进），
这是 Humdrum 的本来语义，也能解释本语料中若干不满小节的编码。
"""
import re, sys, os

PITCH = {'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
NAME = ['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B']

def fmt(m):
    return 'r' if m is None else f"{NAME[m%12]}{m//12-1}"

# ---------------- Kern ----------------
def parse_kern_token(tok):
    """返回 list of (midi|None, dur, is_rest, tie) —— 和弦记为多条。"""
    t = tok.strip()
    if t in ('', '.'):
        return None
    res = []
    for part in t.split(' '):
        p = part
        tie = ''
        while p and p[0] in '([':
            if p[0] == '[':
                tie = 'start'
            p = p[1:]
        if p.endswith(']'):
            tie = 'stop' if not tie else 'both'
            p = p[:-1]
        m = re.match(r'^(\d+)(\.*)(.*)$', p)
        if not m:
            continue
        num = int(m.group(1)); dots = len(m.group(2)); rest = m.group(3)
        dur = 4.0 / num
        add = dur
        for _ in range(dots):
            add /= 2.0
            dur += add
        pm = re.match(r'^([a-gA-G]+)((?:#|-|n|X|Y)*)', rest)
        if not pm:
            res.append((None, dur, rest.strip().startswith('r'), tie))
            continue
        letters = pm.group(1); acc = pm.group(2)
        pc = PITCH[letters[0].lower()]
        n = len(letters)
        octv = 4 + (n - 1) if letters[0].islower() else 4 - n
        for ch in acc:
            if ch == '#': pc += 1
            elif ch == '-': pc -= 1
            elif ch == 'Y': pc -= 2
        res.append(((octv + 1) * 12 + pc, dur, False, tie))
    return res or None

def parse_kern(path):
    spines = None
    meas = 0
    freeze = False
    beat = []          # 每 spine 独立时钟
    out = {}
    for line in open(path, encoding='utf-8', errors='replace'):
        line = line.rstrip('\n')
        if line.startswith('**'):
            spines = line.split('\t')
            beat = [0.0] * len(spines)
            continue
        if line.startswith('!'):
            continue
        if line.startswith('*'):
            continue
        toks = line.split('\t')
        if spines is None or len(toks) != len(spines):
            continue
        if toks[0].startswith('='):
            mm = re.match(r'(\d+)', toks[0][1:])
            if mm:
                meas = int(mm.group(1)); freeze = False
            else:
                freeze = True
            beat = [0.0] * len(spines)
            continue
        if freeze:
            continue
        for i, tk in enumerate(toks):
            r = parse_kern_token(tk)
            if r is None:
                continue
            midi, dur, is_rest, tie = r
            if not is_rest:
                out.setdefault((meas, i), []).append((round(beat[i], 3), midi, dur, tie))
            beat[i] += dur
    return out

# ---------------- LilyPond ----------------
def ly_pitch(tok):
    m = re.match(r"^([a-g])(f{1,2}|s{1,2}|n)?([',]*)$", tok)
    if not m:
        return None
    pc = PITCH[m.group(1)]
    acc = m.group(2) or ''
    if acc.startswith('f'): pc -= len(acc)
    elif acc.startswith('s'): pc += len(acc)
    marks = m.group(3) or ''
    octv = 3 + marks.count("'") - marks.count(',')
    return (octv + 1) * 12 + pc

def parse_ly(path):
    src = open(path, encoding='utf-8').read()
    src = re.sub(r'%[^\n]*', '', src)
    tm = re.search(r'\\time\s+(\d+)/(\d+)', src)
    timesig = (int(tm.group(1)), int(tm.group(2))) if tm else (4, 4)
    barlen = 4.0 * timesig[0] / timesig[1]
    blocks = {}
    for m in re.finditer(r'^([A-Za-z][A-Za-z0-9]*)\s*=\s*\{(.*?)^\}', src, re.S | re.M):
        blocks[m.group(1)] = m.group(2)
    blocks.pop('global', None)
    res = {}
    for name, body in blocks.items():
        body = re.sub(r'"[^"]*"', ' ', body)
        body = re.sub(r'\\[A-Za-z]+', ' ', body)
        out = []
        for bar in body.split('|'):
            bar = bar.strip()
            if not bar:
                continue
            beat = 0.0
            events = []
            merged, acc, inchord = [], '', False
            for tk in bar.split():
                if tk.startswith('<') and not inchord:
                    inchord = True; acc = tk
                    if tk.endswith('>'):
                        merged.append(acc); inchord = False; acc = ''
                    continue
                if inchord:
                    acc += ' ' + tk
                    if tk.endswith('>'):
                        merged.append(acc); inchord = False; acc = ''
                    continue
                merged.append(tk)
            for tk in merged:
                tie = '~' in tk
                m = re.match(r'^<?([^0-9]*)>?(\d+)(\.*)', tk)
                if not m:
                    continue
                ptext = m.group(1)
                num = int(m.group(2)); dots = len(m.group(3))
                dur = 4.0 / num
                add = dur
                for _ in range(dots):
                    add /= 2.0
                    dur += add
                if ptext.strip().startswith('r'):
                    beat += dur
                    continue
                pm = re.findall(r"[a-g](?:f{1,2}|s{1,2}|n)?[',]*", ptext)
                pitches = sorted(p for p in (ly_pitch(x) for x in pm) if p is not None)
                if pitches:
                    events.append((round(beat, 3), pitches, round(dur, 3), tie))
                beat += dur
            out.append((round(beat, 3), events))
        res[name] = out
    return res, barlen, timesig

def main():
    base = os.path.dirname(os.path.abspath(__file__)) + r"\.."
    kb = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\source-packages"
    chor = kb + r"\humdrum\bach-370-chorales-main\bach-370-chorales-main\kern"
    q74 = kb + (r"\beethoven-score-sources\beethoven-string-quartets-main"
                r"\beethoven-string-quartets-main\kern\quartet10-1.krn")
    jobs = [
        ("bwv0269-mm03-04-anticipation.ly", chor+r"\chor001.krn", 3, 2, {'soprano':3,'alto':2,'tenor':1,'bass':0}),
        ("bwv0269-mm05-07-pac.ly",          chor+r"\chor001.krn", 5, 3, {'soprano':3,'alto':2,'tenor':1,'bass':0}),
        ("bwv0347-mm03-04-suspension.ly",   chor+r"\chor002.krn", 3, 2, {'soprano':3,'alto':2,'tenor':1,'bass':0}),
        ("bwv038-6-mm12-13-picardy.ly",     chor+r"\chor010.krn",12, 2, {'soprano':3,'alto':2,'tenor':1,'bass':0}),
        ("bwv153-5-mm03-04-no-fifth.ly",    chor+r"\chor021.krn", 3, 2, {'soprano':3,'alto':2,'tenor':1,'bass':0}),
        ("bwv087-7-mm01-03-suspension.ly",  chor+r"\chor096.krn", 1, 3, {'soprano':3,'alto':2,'tenor':1,'bass':0}),
        ("bwv060-5-mm01-04-tritone.ly",     chor+r"\chor216.krn", 1, 4, {'soprano':3,'alto':2,'tenor':1,'bass':0}),
        ("op74-mvt1-mm18-24-adagio.ly",     q74, 18, 7, {'violinOne':6,'violinTwo':4,'viola':2,'cello':0}),
    ]
    total = 0
    for lyf, kf, m0, nb, vmap in jobs:
        print("="*72)
        print(f"### {lyf}  vs  {os.path.basename(kf)}  m.{m0}..{m0+nb-1}")
        k = parse_kern(kf)
        ly, barlen, ts = parse_ly(os.path.join(base, lyf))
        ndiff = 0
        for vname, spine in vmap.items():
            lybars = ly.get(vname, [])
            if len(lybars) != nb:
                print(f"  [!] {vname}: .ly 小节数 {len(lybars)} != 期望 {nb}")
            for idx in range(min(nb, len(lybars))):
                m = m0 + idx
                kk = [(round(b,3), p, round(d,3)) for (b,p,d,t) in k.get((m, spine), [])]
                beatend, lyevs = lybars[idx]
                lk = [(b, tuple(ps), d) for (b, ps, d, t) in lyevs]
                same = (abs(beatend - barlen) < 1e-6 and len(kk) == len(lk)
                        and all(a[0]==b[0] and a[2]==b[2] and len(b[1])==1 and a[1]==b[1][0]
                                for a,b in zip(kk,lk)))
                if not same:
                    ndiff += 1
                    print(f"  [DIFF] {vname} m.{m}")
                    print("     Kern: " + " | ".join(f"b{b:g}:{fmt(p)}({d:g})" for b,p,d in kk))
                    print("     .ly : " + " | ".join(f"b{b:g}:{'/'.join(fmt(x) for x in ps)}({d:g})" for b,ps,d in lk)
                          + ("" if abs(beatend-barlen)<1e-6 else f"   <<小节合计 {beatend:g}/{barlen:g}>>"))
        total += ndiff
        print(f"  --> 差异小节: {ndiff}")
    print("\n总计差异小节:", total)

if __name__ == '__main__':
    main()
