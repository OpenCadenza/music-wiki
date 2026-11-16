from PIL import Image
import numpy as np
import sys

src = sys.argv[1]
im = Image.open(src).convert('L')
a = np.array(im)
h, w = a.shape
dark = a < 128

# find horizontal staff lines: rows with long dark runs
rowsum = dark.sum(axis=1)
cand = [i for i in range(h) if rowsum[i] > w * 0.5]
print('candidate staff-line rows:', cand)

# group consecutive rows
groups = []
cur = [cand[0]] if cand else []
for r in cand[1:]:
    if r - cur[-1] <= 2:
        cur.append(r)
    else:
        groups.append(cur)
        cur = [r]
if cur:
    groups.append(cur)
staff_lines = [int(np.mean(g)) for g in groups]
print('staff line y positions:', staff_lines)

# barlines: within each staff band, columns that are dark across the band
if len(staff_lines) >= 5:
    bands = []
    i = 0
    while i + 4 < len(staff_lines) + 1 and i + 4 <= len(staff_lines) - 1:
        band = (staff_lines[i] - 2, staff_lines[i + 4] + 2)
        bands.append(band)
        i += 5
    print('bands:', bands)
    for (y0, y1) in bands:
        col = dark[y0:y1 + 1, :].sum(axis=0)
        thr = (y1 - y0 + 1) * 0.9
        cols = [x for x in range(w) if col[x] >= thr]
        # group
        gs = []
        cur = [cols[0]] if cols else []
        for x in cols[1:]:
            if x - cur[-1] <= 2:
                cur.append(x)
            else:
                gs.append(int(np.mean(cur)))
                cur = [x]
        if cur:
            gs.append(int(np.mean(cur)))
        print('barlines for band', (y0, y1), ':', gs)
