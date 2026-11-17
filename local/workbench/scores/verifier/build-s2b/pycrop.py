import sys
import pymupdf

# usage: pycrop.py <pdf> <out.png> <page> <x0> <y0> <x1> <y1> [zoom]
p, out, pg = sys.argv[1], sys.argv[2], int(sys.argv[3])
x0, y0, x1, y1 = (float(v) for v in sys.argv[4:8])
zoom = float(sys.argv[8]) if len(sys.argv) > 8 else 6.0
d = pymupdf.open(p)
page = d[pg - 1]
clip = pymupdf.Rect(x0, y0, x1, y1)
pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom), clip=clip)
pix.save(out)
print(out, pix.width, pix.height)
