"""Crop a region of the OMT Haydn engraving and overlay a full diatonic pitch ladder."""
import sys
from PIL import Image, ImageDraw

PATH = r'local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/haydn-III-66-ii.png'

x0, x1 = int(sys.argv[1]), int(sys.argv[2])
y0, y1 = int(sys.argv[3]), int(sys.argv[4])
out = sys.argv[5]
scale = float(sys.argv[6]) if len(sys.argv) > 6 else 6.0

TREBLE_BOTTOM = 174
TREBLE_NAMES = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
                'C6', 'D6']
BASS_BOTTOM = 407
BASS_NAMES = ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4',
              'F4']
STEP = 9.5

im = Image.open(PATH).convert('RGB')
crop = im.crop((x0, y0, x1, y1))
w, h = crop.size
crop = crop.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
dr = ImageDraw.Draw(crop)
CW, CH = crop.size

for base, names in ((TREBLE_BOTTOM, TREBLE_NAMES), (BASS_BOTTOM, BASS_NAMES)):
    for i, nm in enumerate(names):
        y = base - i * STEP
        yy = (y - y0) * scale
        if 0 <= yy < CH:
            fifth = i % 2 == 0
            dr.line([(0, yy), (CW, yy)], fill=(255, 160, 160) if fifth else (170, 210, 255),
                    width=1)
            dr.text((3, yy - 6), nm, fill=(200, 0, 0) if fifth else (0, 90, 180))
            dr.text((CW - 30, yy - 6), nm, fill=(200, 0, 0) if fifth else (0, 90, 180))
crop.save(out)
print('saved', out, crop.size)
