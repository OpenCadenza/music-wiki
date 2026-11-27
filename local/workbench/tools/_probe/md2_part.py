#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Print one part's measures from a MuseData stage-2 (.md2) file.

Usage: python md2_part.py <file> <part-substring> <lo> <hi>
Prints, for each measure in [lo,hi]: the raw note/rest records (compactly).
"""
import re
import sys

path, needle, lo, hi = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])

lines = open(path, 'r', encoding='utf-8', errors='replace').read().split('\n')

# locate part blocks by the "data: part N of M" header
starts = []
for i, line in enumerate(lines):
    if line.startswith('data: part '):
        starts.append(i)

# find the part whose nearby header block contains the instrument name
chosen = None
for idx, s in enumerate(starts):
    begin = starts[idx - 1] + 1 if idx > 0 else 0
    header = '\n'.join(lines[max(begin, s - 12):s + 1])
    if needle.lower() in header.lower():
        chosen = (s, starts[idx + 1] if idx + 1 < len(starts) else len(lines))
        break

if not chosen:
    print('part not found:', needle)
    sys.exit(1)

s, e = chosen
cur = None
records = []
for line in lines[s:e]:
    m = re.match(r'^measure\s+(\d+)\s*$', line)
    if m:
        cur = int(m.group(1))
        records.append([cur, []])
        continue
    if cur is None:
        continue
    t = line.rstrip()
    if not t or t.startswith('*') or t.startswith('P ') or t.startswith('$') or t.startswith('&'):
        continue
    records[-1][1].append(t)

for num, recs in records:
    if not (lo <= num <= hi):
        continue
    print('m.%d:' % num)
    for r in recs:
        print('   ', r)
