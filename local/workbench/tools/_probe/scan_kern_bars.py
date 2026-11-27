#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan a Humdrum kern file and print per-measure meter/key/clef changes.

Used only for internal verification of printed-vs-continuous measure numbering.
"""
import re
import sys

path = sys.argv[1]
meter_re = re.compile(r'\*M([0-9]+/[0-9]+)')
key_re = re.compile(r'\*k\[([^\]]*)\]')

bar = 0
last_meter = None
last_key = None
out = []
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('='):
            bar += 1
            # count barlines; a spine line may be "=12" or "==" etc.
            continue
        m = meter_re.search(line)
        if m:
            if m.group(1) != last_meter:
                out.append(('M', bar + 1, m.group(1)))
                last_meter = m.group(1)
        k = key_re.search(line)
        if k:
            if k.group(1) != last_key:
                out.append(('K', bar + 1, k.group(1)))
                last_key = k.group(1)

for kind, bar_no, val in out:
    print('%s  bar %4d  %s' % (kind, bar_no, val))
print('total bars (barlines):', bar)
