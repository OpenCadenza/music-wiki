from PIL import Image
src = r"local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/k283.png"
im = Image.open(src)
im.crop((0, 600, 1200, 1103)).resize((1800, 754), Image.LANCZOS).save(r"local/workbench/scores/verifier/tmp/k283_sys2_left.png")
im.crop((1100, 600, 2304, 1103)).resize((1806, 754), Image.LANCZOS).save(r"local/workbench/scores/verifier/tmp/k283_sys2_right.png")
print("ok")
