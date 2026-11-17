from PIL import Image
import sys, os

src = r"local\workbench\scores\score-s2\downloads\mozart-p12.png"
out = r"local\workbench\scores\verifier\tmp"
os.makedirs(out, exist_ok=True)
im = Image.open(src)
W, H = im.size
print("size", W, H)

# 4 systems on the page; crop each system band generously
bands = [(120, 330), (600, 830), (1050, 1280), (1480, 1720)]
for i, (y0, y1) in enumerate(bands):
    c = im.crop((60, y0, W - 40, y1))
    scale = 3
    c = c.resize((c.width * scale, c.height * scale), Image.LANCZOS)
    p = os.path.join(out, "p12-sys%d.png" % (i + 1))
    c.save(p)
    print(p, c.size)
