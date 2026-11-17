from PIL import Image
import numpy as np, os

src = r"local\workbench\scores\score-s2\downloads\mozart-p12.png"
out = r"local\workbench\scores\verifier\tmp"
os.makedirs(out, exist_ok=True)
im = Image.open(src).convert("L")
a = np.array(im)
h, w = a.shape
dark = (a < 128).sum(axis=1)
# staff lines: rows with a long run of dark pixels
rows = [i for i in range(h) if dark[i] > w * 0.35]
print("staff-line rows:", rows)

# cluster rows into staves (consecutive rows within 20px)
groups = []
for r in rows:
    if groups and r - groups[-1][-1] <= 6:
        groups[-1].append(r)
    else:
        groups.append([r])
print("staff groups (y0,y1):", [(g[0], g[-1]) for g in groups])

# cluster staves into systems (gap > 40px)
systems = []
for g in groups:
    y0, y1 = g[0], g[-1]
    if systems and y0 - systems[-1][1] <= 60:
        systems[-1] = (systems[-1][0], y1)
    else:
        systems.append((y0, y1))
print("systems:", systems)

for i, (y0, y1) in enumerate(systems, 1):
    pad_top, pad_bot = 45, 20
    c = im.crop((55, max(0, y0 - pad_top), w - 35, min(h, y1 + pad_bot)))
    sc = 4
    c = c.resize((c.width * sc, c.height * sc), Image.LANCZOS)
    p = os.path.join(out, "sys%d.png" % i)
    c.save(p)
    print(p, c.size)
