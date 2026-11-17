import sys
import pymupdf

p, pg = sys.argv[1], int(sys.argv[2])
d = pymupdf.open(p)
page = d[pg - 1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# long horizontal staff lines
staffs = []
for dr in page.get_drawings():
    r = dr["rect"]
    if r.height < 1.6 and r.width > 400:
        staffs.append((round(r.y0, 1), round(r.x0, 1), round(r.x1, 1)))
staffs.sort()
print("staff lines:", staffs)

# group into staves of 5
ys = [s[0] for s in staffs]
print("n lines", len(ys))
