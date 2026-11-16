from PIL import Image
from pathlib import Path

BASE = Path(r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb")
src = BASE / "local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/k330-ii.png"
im = Image.open(src)
out = BASE / "local/workbench/scores/verifier/tmp2"
im.crop((1750, 590, 2275, 1060)).resize((1050, 940), Image.LANCZOS).save(out / "k330ii_m8_zoom.png")
print("ok")
