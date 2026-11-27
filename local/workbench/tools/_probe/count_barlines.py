#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Detect barlines in a rendered score page by finding columns that are dark
across the full vertical extent of a grand-staff system."""
import sys

import numpy as np
from PIL import Image

path = sys.argv[1]
im = Image.open(path).convert('L')
a = np.array(im)
h, w = a.shape
dark = a < 120
rowsum = dark.sum(axis=1)

# staff line rows: long dark rows
thr = 0.30 * w
staff_rows = [y for y in range(h) if rowsum[y] > thr]

# group consecutive rows into bands
bands = []
if staff_rows:
    start = prev = staff_rows[0]
    for y in staff_rows[1:]:
        if y - prev <= 6:
            prev = y
        else:
            bands.append((start, prev))
            start = prev = y
    bands.append((start, prev))
print('staff bands:', bands)

# group bands into systems: consecutive bands whose gap < 90 px
systems = []
if bands:
    cur = [bands[0]]
    for b in bands[1:]:
        if b[0] - cur[-1][1] < 120:
            cur.append(b)
        else:
            systems.append(cur)
            cur = [b]
    systems.append(cur)

for si, sysbands in enumerate(systems, 1):
    top = sysbands[0][0]
    bot = sysbands[-1][1]
    if len(sysbands) < 4:   # need at least 4 lines to be meaningful
        continue
    seg = dark[top:bot + 1, :]
    colsum = seg.sum(axis=0)
    need = 0.90 * seg.shape[0]
    cols = [x for x in range(w) if colsum[x] >= need]
    # cluster columns
    clusters = []
    if cols:
        s = p = cols[0]
        for x in cols[1:]:
            if x - p <= 4:
                p = x
            else:
                clusters.append((s + p) // 2)
                s = p = x
        clusters.append((s + p) // 2)
    print('system %d y=[%d,%d] bars-lines: %d -> %s'
          % (si, top, bot, len(clusters), clusters))
