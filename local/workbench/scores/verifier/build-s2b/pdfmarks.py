import sys
import pymupdf

p = sys.argv[1]
lo, hi = int(sys.argv[2]), int(sys.argv[3])
d = pymupdf.open(p)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
for i in range(lo - 1, min(hi, d.page_count)):
    page = d[i]
    toks = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for s in l.get("spans", []):
                t = s["text"].strip()
                if t:
                    toks.append((round(s["bbox"][1]), round(s["bbox"][0]), t))
    marks = [t for t in toks if len(t[2]) == 1 and t[2] in "ABCDEFGHIJKLMNOP"]
    nums = [t for t in toks if t[2].isdigit() and t[1] < 60]
    print(f"page {i+1}: marks={marks}  leftnums={nums}")
