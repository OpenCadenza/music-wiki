"""Crop a region of the OMT Haydn engraving and overlay pitch gridlines with labels."""
import sys
from PIL import Image, ImageDraw

PATH = r'local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/haydn-III-66-ii.png'

x0, x1 = int(sys.argv[1]), int(sys.argv[2])
y0, y1 = int(sys.argv[3]), int(sys.argv[4])
out = sys.argv[5]
scale = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0

TREBLE_LINES = [(98, 'F5'), (117, 'D5'), (136, 'B4'), (155, 'G4'), (174, 'E4')]
BASS_LINES = [(331, 'A3'), (350, 'F3'), (369, 'D3'), (388, 'B2'), (407, 'G2')]
STEP = 9.5

im = Image.open(PATH).convert('RGB')
crop = im.crop((x0, y0, x1, y1))
w, h = crop.size
crop = crop.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
dr = ImageDraw.Draw(crop)
for (y, nm) in TREBLE_LINES + BASS_LINES:
    yy = (y - y0) * scale
    if 0 <= yy < crop.size[1]:
        dr.line([(0, yy), (crop.size[0], yy)], fill=(255, 0, 0), width=1)
        dr.text((4, yy - 12), nm, fill=(255, 0, 0))
        dr.text((crop.size[0] - 40, yy - 12), nm, fill=(255, 0, 0))
# octave-position helper: draw ruler on left edge for every diatonic step
for i in range(-8, 16):
    for base, names in ((174, ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5',
                               'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6', 'H', 'I', 'J',
                               'K', 'L', 'M', 'N']),
                        (407, ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
                               'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5',
                               'F5', 'G5', 'A5', 'B5'])):
        if 0 <= i < len(names):
            yy = (base - i * STEP - y0) * scale
            if 0 <= yy < crop.size[1]:
                dr.line([(0, yy), (14, yy)], fill=(0, 128, 255), width=1)
crop.save(out)
print('saved', out, crop.size)
