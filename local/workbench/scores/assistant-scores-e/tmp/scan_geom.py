"""Locate staff bands (5-line groups) and barlines inside a scanned score page region."""
import sys
import numpy as np
from PIL import Image

path = sys.argv[1]
y0 = int(sys.argv[2])
y1 = int(sys.argv[3])
x0 = int(sys.argv[4])
x1 = int(sys.argv[5])

im = Image.open(path).convert('L')
a = np.array(im)
sub = a[y0:y1, x0:x1] < 110
h, w = sub.shape
rowsum = sub.sum(axis=1)
cand = [i for i in range(h) if rowsum[i] > w * 0.45]
groups = []
cur = []
for r in cand:
    if cur and r - cur[-1] > 4:
        groups.append(cur)
        cur = []
    cur.append(r)
if cur:
    groups.append(cur)
lines = [y0 + int(np.mean(g)) for g in groups]
print('staff lines (abs y):', lines)
bands = []
i = 0
while i + 4 < len(lines) + 1 and i + 4 <= len(lines) - 1:
    bands.append((lines[i], lines[i + 4]))
    i += 5
print('bands:', bands)

for (b0, b1) in bands:
    band = (a[b0 - 3:b1 + 4, x0:x1] < 110).sum(axis=0)
    thr = (b1 - b0 + 7) * 0.85
    xs = [x for x in range(w) if band[x] >= thr]
    gs = []
    cur = []
    for x in xs:
        if cur and x - cur[-1] > 4:
            gs.append(x0 + int(np.mean(cur)))
            cur = []
        cur.append(x)
    if cur:
        gs.append(x0 + int(np.mean(cur)))
    print('band y%d-%d barlines(abs x): %s' % (b0, b1, gs))
