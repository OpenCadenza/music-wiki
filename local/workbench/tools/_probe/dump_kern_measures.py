#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump per-measure summary for a kern file: explicit barline number, meter,
key, and the pitch tokens of each kern spine (first N tokens)."""
import re
import sys

path = sys.argv[1]
lo = int(sys.argv[2]) if len(sys.argv) > 2 else 0
hi = int(sys.argv[3]) if len(sys.argv) > 3 else 10 ** 6

meter_re = re.compile(r'\*M([0-9]+/[0-9]+)')
key_re = re.compile(r'\*k\[([^\]]*)\]')
bar_re = re.compile(r'^=([0-9]+)')

cur = None
meter = None
key = None
columns = []  # list of per-measure token lists
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    for line in f:
        line = line.rstrip('\n')
        m = bar_re.match(line.strip().split('\t')[0])
        if m:
            cur = int(m.group(1))
            columns.append({'bar': cur, 'meter': meter, 'key': key, 'spines': []})
            continue
        if cur is None:
            mm = meter_re.search(line)
            if mm:
                meter = mm.group(1)
            kk = key_re.search(line)
            if kk:
                key = kk.group(1)
            continue
        if line.startswith('*') or line.startswith('!') or not line.strip():
            mm = meter_re.search(line)
            if mm:
                meter = mm.group(1)
                columns[-1]['meter'] = meter
            kk = key_re.search(line)
            if kk:
                key = kk.group(1)
                columns[-1]['key'] = key
            continue
        toks = line.split('\t')
        columns[-1]['spines'].append(toks)

for col in columns:
    if not (lo <= col['bar'] <= hi):
        continue
    # first data row's tokens
    first = col['spines'][0] if col['spines'] else []
    print('m.%-4d M:%-6s K:%-14s %s' % (
        col['bar'], col['meter'] or '-', col['key'] or '-',
        ' | '.join(t.strip() for t in first[:4])))
