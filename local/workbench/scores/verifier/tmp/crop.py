from PIL import Image
src = r"local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/k283.png"
im = Image.open(src)
print(im.size)
# 系统1低音谱表区域（左侧 mm.1-4）
crop = im.crop((60, 250, 1200, 470)).resize((2200, 460), Image.LANCZOS)
crop.save(r"local/workbench/scores/verifier/tmp/k283_sys1_bass.png")
# 系统2低音谱表区域（mm.6-10）
crop2 = im.crop((60, 830, 2304, 1103)).resize((2200, 268), Image.LANCZOS)
crop2.save(r"local/workbench/scores/verifier/tmp/k283_sys2_bass.png")
print("ok")
