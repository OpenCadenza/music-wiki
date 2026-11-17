from PIL import Image
import os

src = r"local\workbench\scores\score-s2\downloads\mozart-p12.png"
out = r"local\workbench\scores\verifier\tmp"
im = Image.open(src)

# Vn1 staff of system 2 (approx y 620..660 in the 1324x1871 page)
for name, (x0, x1) in {"vn1-s2-left": (60, 700), "vn1-s2-right": (660, 1300)}.items():
    c = im.crop((x0, 608, x1, 672))
    c = c.resize((c.width * 6, c.height * 6), Image.LANCZOS)
    p = os.path.join(out, name + ".png")
    c.save(p)
    print(p, c.size)
