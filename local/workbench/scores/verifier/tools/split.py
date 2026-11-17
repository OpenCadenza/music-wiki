from PIL import Image
import os

out = r"local\workbench\scores\verifier\tmp"
for i in (1, 2):
    im = Image.open(os.path.join(out, "sys%d.png" % i))
    W, H = im.size
    for j, (x0, x1) in enumerate([(0, W // 2 + 100), (W // 2 - 100, W)]):
        c = im.crop((x0, 0, x1, H))
        # downscale slightly to keep file readable but legible
        c = c.resize((int(c.width * 0.62), int(c.height * 0.62)), Image.LANCZOS)
        p = os.path.join(out, "sys%d-%s.png" % (i, "ab"[j]))
        c.save(p)
        print(p, c.size)
