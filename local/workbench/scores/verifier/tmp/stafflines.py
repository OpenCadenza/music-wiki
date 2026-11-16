from PIL import Image
import numpy as np, sys
sys.stdout.reconfigure(encoding="utf-8")
src = r"local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/k283.png"
im = Image.open(src).convert("L")
a = np.array(im)
H, W = a.shape
dark = a < 128
# 系统1低音谱表：y 250..470
sub = dark[250:480, :]
rowsum = sub.sum(axis=1)
rpeaks = [(y+250, int(rowsum[y])) for y in range(len(rowsum)) if rowsum[y] > 700]
print("长横线候选（y, 暗像素数）:")
for y, c in rpeaks:
    print(f"  y={y} count={c}")
