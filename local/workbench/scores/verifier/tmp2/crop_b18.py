from PIL import Image
from pathlib import Path

BASE = Path(r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb")
src = BASE / "local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/beethoven_18_2.png"
im = Image.open(src)
print(im.size)
out = BASE / "local/workbench/scores/verifier/tmp2"
im.crop((950, 580, 1400, 830)).resize((1350, 750), Image.LANCZOS).save(out / "b18_2_cello_m4.png")
im.crop((1900, 60, 2285, 830)).resize((770, 1540), Image.LANCZOS).save(out / "b18_2_m8.png")
print("ok")
