#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse musicxml2ly output of Mozart K.465 and extract movement IV mm.10-16
for each of the four staff blocks.

Handles tokens like:  \\D g'8 -. [ \\D g8 -. ]  ,  \\D g4. ^( \\D c8 )
and rests r8, grace groups skipped.
"""
import re
import sys

path = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s2\downloads\mozart-k465.ly"
lines = open(path, encoding="utf-8").read().splitlines()

# 1) split into staff blocks: a staff block starts at a line with \clef and \time 3/4;
#    movement IV starts where \time 2/4 occurs within each block.
blocks = []
cur = []
for ln in lines:
    if '\\clef' in ln and ('\\time 3/4' in ln or '\\time 2/4' in ln) and not cur:
        cur = [ln]
    elif cur:
        cur.append(ln)
    if ln.strip().startswith('}') and cur:
        blocks.append(cur)
        cur = []

print('blocks:', len(blocks))
if not blocks:
    # fallback: split on lines containing "I." markup
    sys.exit('no blocks found')

notes_re = re.compile(r"\\[DU]\s+([a-g])([',]*)([!]?)([0-9]+)(\.*)")
rest_re = re.compile(r"(?:\\[DU]\s+)?r([0-9]+)(\.*)")
time_re = re.compile(r"\\time\s+(\d+)/(\d+)")

for bi, blk in enumerate(blocks):
    # find movement IV start
    m4_line = None
    for li, ln in enumerate(blk):
        if '\\time 2/4' in ln:
            m4_line = li
            break
    if m4_line is None:
        print(f'block {bi}: no movement IV')
        continue
    text = "\n".join(blk[m4_line:])
    # strip comments
    # parse all note/rest tokens with durations
    events = []
    for m in notes_re.finditer(text):
        name, octs, acc, dur, dots = m.groups()
        d = {'1': 4.0, '2': 2.0, '4': 1.0, '8': 0.5, '16': 0.25, '32': 0.125}.get(dur)
        if d is None:
            continue
        if dots:
            d *= 1.5 if len(dots) == 1 else 1.75
        events.append((m.start(), name + octs, acc, d, False))
    for m in rest_re.finditer(text):
        dur = m.group(1)
        d = {'1': 4.0, '2': 2.0, '4': 1.0, '8': 0.5, '16': 0.25, '32': 0.125}.get(dur)
        if d is None:
            continue
        events.append((m.start(), None, '', d, True))
    events.sort(key=lambda e: e[0])
    # accumulate into bars: movement IV is 2/4 -> 2.0 quarters per bar
    qpb = 2.0
    pos = 0.0
    bar = 1
    out = []
    for (_, name, acc, d, is_rest) in events:
        if is_rest:
            pos += d
            while pos >= qpb + 1e-6:
                pos -= qpb
                bar += 1
            continue
        b = bar
        p = pos
        out.append((b, p, name, acc, d))
        pos += d
        while pos >= qpb + 1e-6:
            pos -= qpb
            bar += 1
    sel = [(b, p, n, a, d) for (b, p, n, a, d) in out if 10 <= b <= 16]
    print(f'=== block {bi} (staff {bi+1}): mm.10-16, {len(sel)} notes ===')
    for (b, p, n, a, d) in sel:
        print(f'  m{b:>2} @{p:>4.2f} {n:>5}{a} dur={d:.2f}')
