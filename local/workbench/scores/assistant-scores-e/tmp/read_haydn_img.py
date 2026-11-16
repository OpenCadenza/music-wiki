"""Read pitches out of the (2-staff) OMT Haydn engraving.

Detects barlines (full-system-height verticals) and note heads (vertical dark run
whose height fits a filled notehead) inside each staff band, then maps y to pitch
using the known staff-line rows.
"""
import sys
import numpy as np
from PIL import Image

PATH = r'local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/Graphics/form/haydn-III-66-ii.png'


def load():
    a = np.array(Image.open(PATH).convert('L')) < 128
    return a


def barlines(a, y0, y1, w, frac=0.85):
    band = a[y0:y1 + 1, :]
    colsum = band.sum(axis=0)
    thr = (y1 - y0 + 1) * frac
    xs = [x for x in range(w) if colsum[x] >= thr]
    groups, cur = [], []
    for x in xs:
        if cur and x - cur[-1] > 3:
            groups.append(cur)
            cur = []
        cur.append(x)
    if cur:
        groups.append(cur)
    return [int(np.mean(g)) for g in groups]


TREBLE = ['E4', 'F4', 'G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6',
          'D6', 'E6']
BASS = ['G2', 'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4',
        'F4', 'G4']


def heads(a, y_lo, y_hi, x0, x1, bottom_line_y, names, label):
    step_px = 9.5
    out = []
    for x in range(x0, x1):
        col = a[:, x]
        y = y_lo
        while y <= y_hi:
            if col[y]:
                s = y
                while y + 1 <= y_hi and col[y + 1]:
                    y += 1
                e = y
                h = e - s + 1
                if 6 <= h <= 12:
                    out.append((x, (s + e) / 2.0))
            y += 1
    out.sort()
    clusters = []
    for (x, y) in out:
        hit = None
        for c in clusters:
            if x - c['x1'] <= 2 and abs(c['ysum'] / c['n'] - y) <= 3.5:
                hit = c
                break
        if hit:
            hit['x1'] = x
            hit['ysum'] += y
            hit['n'] += 1
        else:
            clusters.append({'x0': x, 'x1': x, 'ysum': y, 'n': 1})
    print('=== %s band y[%d..%d] ===' % (label, y_lo, y_hi))
    res = []
    for c in clusters:
        if c['x1'] - c['x0'] < 3:
            continue
        y = c['ysum'] / c['n']
        idx = int(round((bottom_line_y - y) / step_px))
        nm = names[idx] if 0 <= idx < len(names) else ('?' + str(idx))
        res.append(((c['x0'] + c['x1']) // 2, y, nm, c['x1'] - c['x0'] + 1))
    res.sort()
    for (x, y, nm, w) in res:
        print('  x=%4d y=%5.1f  %-3s  w=%d' % (x, y, nm, w))
    return res


if __name__ == '__main__':
    a = load()
    h, w = a.shape
    print('image', w, h)
    for (label, y0, y1) in (('SYS1', 90, 415), ('SYS2', 615, 945)):
        bl = barlines(a, y0, y1, w)
        print('%s barlines:' % label, bl)
