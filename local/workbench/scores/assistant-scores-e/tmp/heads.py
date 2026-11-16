"""Detect note heads in a monochrome score image given staff-line y positions.

Reads image, for a given staff band and x-window, finds vertical dark runs whose
height matches a note head, clusters them and prints (x, y, diatonic step).
"""
import sys
import numpy as np
from PIL import Image

STEP_NAMES_TREBLE = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']
STEP_NAMES_BASS = ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4']


def runs(col, y0, y1):
    out = []
    start = None
    for y in range(y0, y1 + 1):
        if col[y]:
            if start is None:
                start = y
        else:
            if start is not None:
                out.append((start, y - 1))
                start = None
    if start is not None:
        out.append((start, y1))
    return out


def main():
    path = sys.argv[1]
    band_top = int(sys.argv[2])      # y of bottom staff line of upper staff
    step_px = float(sys.argv[3])     # px per diatonic step
    names = STEP_NAMES_TREBLE if sys.argv[4] == 'treble' else STEP_NAMES_BASS
    ytop = int(sys.argv[5]); ybot = int(sys.argv[6])
    x0 = int(sys.argv[7]); x1 = int(sys.argv[8])
    im = Image.open(path).convert('L')
    a = np.array(im) < 128
    heads = []
    for x in range(x0, x1):
        col = a[:, x]
        for (s, e) in runs(col, ytop, ybot):
            hgt = e - s + 1
            if 6 <= hgt <= 13:
                heads.append((x, (s + e) / 2.0, hgt))
    # cluster by proximity
    heads.sort()
    clusters = []
    for (x, y, h) in heads:
        placed = False
        for c in clusters:
            if abs(c['x1'] - x) <= 2 and abs(c['y'] - y) <= 3:
                c['x1'] = x
                c['ys'].append(y)
                placed = True
                break
        if not placed:
            clusters.append({'x0': x, 'x1': x, 'y': y, 'ys': [y]})
    print('--- detected head candidates (x_center, y_center, step/pitch) ---')
    for c in clusters:
        w = c['x1'] - c['x0'] + 1
        y = float(np.median(c['ys']))
        idx = int(round((band_top - y) / step_px))
        nm = names[idx] if 0 <= idx < len(names) else '?%d' % idx
        print('x=%4d y=%6.1f w=%2d step=%+d %s' % ((c['x0'] + c['x1']) // 2, y, w, idx, nm))


if __name__ == '__main__':
    main()
