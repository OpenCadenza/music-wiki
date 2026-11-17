from PIL import Image
import numpy as np, sys

src = sys.argv[1] if len(sys.argv) > 1 else r"local\workbench\scores\score-s2\downloads\mozart-p12.png"
im = Image.open(src).convert("L")
a = np.array(im)
h, w = a.shape
dark = a < 128

# staff line rows detected earlier: pick the system 1 band
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
print("systems:", systems)

band = systems[int(sys.argv[2]) if len(sys.argv) > 2 else 0]
y0, y1 = band
sub = dark[y0 - 5:y1 + 6, :]
colcount = sub.sum(axis=0)
# a barline spans nearly the whole system height (multiple staves) -> tall dark column
cand = [x for x in range(w) if colcount[x] > (y1 - y0) * 0.55]
# cluster
cl = []
for x in cand:
    if cl and x - cl[-1][-1] <= 3:
        cl[-1].append(x)
    else:
        cl.append([x])
centers = [int(np.mean(c)) for c in cl]
print("system %d y=%s height=%d" % (y0, band, y1 - y0))
print("tall columns (barlines / staff-start):", centers)
print("count:", len(centers))
