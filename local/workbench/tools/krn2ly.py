#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert selected columns/measures of a Humdrum **kern file to LilyPond note strings (english, absolute).

Usage: python krn2ly.py <file.krn> <col1,col2,...> <m0> <m1>
Prints per selected column a token stream with ' | ' at barlines.
Handles chords, ties ([ ]), slurs (( )) and rests.
"""
import sys, re

IGNORE_OCT = False

def parse_kern_token(tok):
    t = tok.strip()
    if not t or t == '.':
        return None
    m = re.match(r'^[\[({<>]?(\d+)(\.*)([A-Ga-g]+)([#\-n]*)([,\']*)(.*)$', t)
    if not m:
        return None
    dur, dots, letters, acc, octs, rest = m.groups()
    dur = dur + dots
    n = len(letters)
    base = letters[0]
    name = base.lower()
    for a in acc:
        if a == '-':
            name += 'f'
        elif a == '#':
            name += 's'
        elif a == 'n':
            pass
    offset = 0 if IGNORE_OCT else (octs.count("'") - octs.count(","))
    if base.islower():
        # kern c = C4 -> LilyPond c' (1 apostrophe); n letters -> C4+(n-1)
        lily_octs = n + offset
    else:
        # kern C = C3 -> LilyPond c (0); n letters -> C3-(n-1)
        lily_octs = offset - (n - 1)
    name = name + ("'" * lily_octs if lily_octs > 0 else "," * (-lily_octs))
    return {'dur': dur, 'name': name,
            'tie_start': '[' in rest, 'tie_stop': ']' in rest,
            'sl_start': '(' in rest, 'sl_stop': ')' in rest}

def main(path, cols, m0, m1):
    global IGNORE_OCT
    IGNORE_OCT = (len(sys.argv) > 5 and sys.argv[5] == 'ignore-oct')
    lines = open(path, encoding='utf-8', errors='replace').read().splitlines()
    out = {c: [] for c in cols}
    cur = 0
    for line in lines:
        if not line.strip():
            continue
        if line.startswith('!!') or line.startswith('!!!') or line.startswith('*') or line.startswith('!'):
            continue
        if line.startswith('='):
            mm = re.match(r'=(\d+)', line)
            if mm:
                cur = int(mm.group(1))
                if m0 <= cur <= m1:
                    for c in cols:
                        out[c].append('|')
            continue
        if not (m0 <= cur <= m1):
            continue
        toks = line.split('\t')
        for c in cols:
            if c >= len(toks):
                continue
            raw = toks[c].strip()
            if not raw or raw == '.':
                continue
            parts = [p for p in raw.split() if p and p != '.']
            if not parts:
                continue
            parsed = [parse_kern_token(p) for p in parts]
            parsed = [p for p in parsed if p]
            if not parsed:
                # maybe a rest token like "4r" / "8.r"
                rm = re.match(r'^(\d+)(\.*)r', parts[0])
                if rm:
                    out[c].append('r' + rm.group(1) + rm.group(2))
                continue
            notes = [p for p in parsed if p['name']]
            dur = parsed[0]['dur']
            if len(notes) == 1:
                n = notes[0]
                s = n['name'] + n['dur']
                if n['tie_start']:
                    s += '~'
                out[c].append(s)
            else:
                body = ' '.join(n['name'] for n in notes)
                s = '<' + body + '>' + dur
                if notes[0]['tie_start']:
                    s += '~'
                out[c].append(s)
    for c in cols:
        print(f"%%% COL {c} %%%")
        buf = ''
        for t in out[c]:
            if t == '|':
                buf = buf.rstrip() + ' |\n'
            else:
                buf += t + ' '
        print(buf)

if __name__ == '__main__':
    path = sys.argv[1]
    cols = [int(x) for x in sys.argv[2].split(',')]
    m0 = int(sys.argv[3]); m1 = int(sys.argv[4])
    main(path, cols, m0, m1)





