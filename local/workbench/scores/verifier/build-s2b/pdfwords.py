import sys
import pymupdf

p, pg = sys.argv[1], int(sys.argv[2])
d = pymupdf.open(p)
page = d[pg - 1]
out = []
for b in page.get_text("dict")["blocks"]:
    for l in b.get("lines", []):
        for s in l.get("spans", []):
            t = s["text"].strip()
            if not t:
                continue
            x, y = s["bbox"][0], s["bbox"][1]
            out.append((round(y), round(x), t))
out.sort()
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for y, x, t in out:
    print(f"y={y:4d} x={x:4d}  {t!r}")
