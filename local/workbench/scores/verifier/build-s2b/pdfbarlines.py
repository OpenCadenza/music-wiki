import sys
import pymupdf

p, pg, ymid = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
d = pymupdf.open(p)
page = d[pg - 1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
xs = []
for dr in page.get_drawings():
    r = dr["rect"]
    if r.width < 1.6 and r.height > 4 and r.y0 - 1 <= ymid <= r.y1 + 1:
        xs.append(round(r.x0, 1))
xs = sorted(set(xs))
print("barlines at x:", xs)
print("count:", len(xs), " gaps:", [round(b - a, 1) for a, b in zip(xs, xs[1:])])
