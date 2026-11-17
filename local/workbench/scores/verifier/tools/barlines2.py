from PIL import Image
import numpy as np, sys

src = sys.argv[1] if len(sys.argv) > 1 else r"local\workbench\scores\score-s2\downloads\mozart-p12.png"
sysi = int(sys.argv[2]) if len(sys.argv) > 2 else 0
im = Image.open(src).convert("L")
a = np.array(im)
h, w = a.shape
dark = a < 140

rows = [i for i in range(h) if dark[i].sum() > w * 0.35]
groups = []
for r in rows:
    if groups and r - groups[-1][-1] <= 6:
        groups[-1].append(r)
    else:
        groups.append([r])
systems = []
for g in groups:
    y0, y1 = g[0], g[-1]
    if systems and y0 - systems[-1][1] <= 60:
        systems[-1] = (systems[-1][0], y1)
    else:
        systems.append((y0, y1))
y0, y1 = systems[sysi]
# individual staves within the system: regroup rows
staves = []
for g in groups:
    if y0 - 8 <= g[0] <= y1 + 8:
        if staves and g[0] - staves[-1][-1] <= 20:
            staves[-1].extend(g)
        else:
            staves.append(list(g))
print("system %d (y %d..%d), staves:" % (sysi, y0, y1), [(s[0], s[-1]) for s in staves])

masks = []
for s in staves:
    top, bot = s[0] - 3, s[-1] + 3
    if bot - top < 15:
        continue
    sub = dark[top:bot, :]
    col = sub.sum(axis=0)
    masks.append(col >= (bot - top) * 0.85)
print("usable staves:", len(masks))
agg = np.sum(masks, axis=0)
cand = [x for x in range(w) if agg[x] >= max(2, len(masks) - 1)]
cl = []
for x in cand:
    if cl and x - cl[-1][-1] <= 4:
        cl[-1].append(x)
    else:
        cl.append([x])
centers = [int(np.mean(c)) for c in cl]
print("barline candidates:", centers)
print("spacings:", [centers[i + 1] - centers[i] for i in range(len(centers) - 1)])
