import sys
import pymupdf

p, pg = sys.argv[1], int(sys.argv[2])
d = pymupdf.open(p)
page = d[pg - 1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
rects = []
for dr in page.get_drawings():
    r = dr["rect"]
    w, h = r.width, r.height
    if w < 1.6 and h > 8:
        rects.append(("V", round(r.x0, 1), round(r.y0, 1), round(r.y1, 1)))
    elif h < 1.6 and w > 60:
        rects.append(("H", round(r.x0, 1), round(r.y0, 1), round(r.x1, 1)))
vs = sorted({(x, y0, y1) for k, x, y0, y1 in rects if k == "V"})
hs = sorted({(y0, x0, x1) for k, x0, y0, x1 in rects if k == "H"})
print("horizontal staff lines (y, x0, x1):")
for h in hs:
    print("  ", h)
print("vertical lines (x, y0, y1): count=", len(vs))
for v in vs:
    print("  ", v)
