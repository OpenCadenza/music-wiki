import pymupdf
d=pymupdf.open("beethoven-op14-1-mvt1-mm1-16.pdf")
print("pages",d.page_count)
pg=d[0]
pix=pg.get_pixmap(dpi=150)
pix.save("preview-op14-1.png")
print("saved",pix.width,"x",pix.height)
