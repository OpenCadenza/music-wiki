from PIL import Image
import numpy as np, sys
sys.stdout.reconfigure(encoding="utf-8")
src = r"local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/k283.png"
a = np.array(Image.open(src).convert("L"))
dark = a < 128
for y in range(560, 1103):
    c = int(dark[y].sum())
    if c > 400:
        print(y, c)
