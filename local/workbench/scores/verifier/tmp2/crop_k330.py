from PIL import Image
from pathlib import Path

BASE = Path(r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb")
src = BASE / "local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/k330-ii.png"
im = Image.open(src)
print(im.size)
out = BASE / "local/workbench/scores/verifier/tmp2"
im.crop((30, 600, 800, 1060)).resize((1540, 920), Image.LANCZOS).save(out / "k330ii_m5_zoom.png")
im.crop((1150, 60, 2275, 520)).resize((1800, 736), Image.LANCZOS).save(out / "k330ii_m4_zoom.png")
print("ok")
