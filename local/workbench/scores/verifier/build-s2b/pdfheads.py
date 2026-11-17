import sys
import pymupdf

p, pg = sys.argv[1], int(sys.argv[2])
y0, y1 = float(sys.argv[3]), float(sys.argv[4])
x0, x1 = float(sys.argv[5]), float(sys.argv[6])
d = pymupdf.open(p)
page = d[pg - 1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
heads = []
for dr in page.get_drawings():
    r = dr["rect"]
    if 2.0 < r.width < 7.0 and 1.5 < r.height < 6.0 and y0 <= (r.y0 + r.y1) / 2 <= y1 and x0 <= r.x0 <= x1:
        heads.append((round(r.x0, 1), round((r.y0 + r.y1) / 2, 2), round(r.width, 1), round(r.height, 1)))
heads.sort()
print("notehead candidates (x, ycenter, w, h):")
for h in heads:
    print("  ", h)
