from PIL import Image
import numpy as np, sys
sys.stdout.reconfigure(encoding="utf-8")
src = r"local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/k283.png"
a = np.array(Image.open(src).convert("L"))
dark = a < 128
sub = dark[860:1080, :]
rowsum = sub.sum(axis=1)
peaks=[(y+860,int(rowsum[y])) for y in range(len(rowsum)) if rowsum[y]>600]
print("系统2长横线:", peaks)
