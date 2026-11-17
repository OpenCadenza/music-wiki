import sys
import pymupdf

p = sys.argv[1]
outdir = sys.argv[2]
pages = [int(x) for x in sys.argv[3].split(",")]
zoom = float(sys.argv[4]) if len(sys.argv) > 4 else 2.0
d = pymupdf.open(p)
for pg in pages:
    page = d[pg - 1]
    pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
    path = f"{outdir}/p{pg:03d}.png"
    pix.save(path)
    print(path, pix.width, pix.height)
