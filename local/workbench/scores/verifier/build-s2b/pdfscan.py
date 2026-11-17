import sys
import pymupdf

p = sys.argv[1]
kw = sys.argv[2] if len(sys.argv) > 2 else "Poco allegretto"
d = pymupdf.open(p)
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
print("pages", d.page_count)
for i in range(d.page_count):
    t = d[i].get_text()
    if kw in t:
        print("---- page", i + 1, "----")
        print(t[:1200])
