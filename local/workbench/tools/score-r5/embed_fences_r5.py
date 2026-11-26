#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Embed the round-5 kern excerpts (fences.json) into the three articles."""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
FENCES = json.load(io.open(os.path.join(ROOT, 'local/workbench/scores/score-c-r5/fences.json'),
                          encoding='utf-8'))

ART = {
    'variation': os.path.join(ROOT, 'content/techniques/structure/'
                              'variation-types-and-structural-transformations.md'),
    'fugue': os.path.join(ROOT, 'content/techniques/counterpoint/'
                          'fugue-in-the-sonata-cycle.md'),
    'articulation': os.path.join(ROOT, 'content/notation/'
                                 'articulation-marks-and-realization.md'),
}

# (article, mode, anchor, fence id) ; mode: before | after | replace
PLAN = [
    ('variation', 'before', '### 3. 第二变奏：轻盈点彩断奏与严格二重对位',
     'beethoven-op109-iii-mm17-32'),
    ('variation', 'replace', '第一变奏 Molto espressivo 与 第二变奏 Leggiermente',
     'beethoven-op109-iii-mm33-48'),
    ('variation', 'replace', '第五变奏 Allegro, ma non troppo，mm. 113–128',
     'beethoven-op109-iii-mm113-128'),
    ('variation', 'replace', 'Arietta: Adagio molto semplice e cantabile，mm. 1–16',
     'beethoven-op111-ii-mm1-16'),
    ('variation', 'replace', '第二变奏 L\'istesso tempo，mm. 33–48',
     'beethoven-op111-ii-mm33-48'),
    ('fugue', 'replace', '第四乐章 引子，Largo，mm. 1–14',
     'beethoven-op106-iv-mm1-14'),
    ('fugue', 'replace', '赋格呈示部，Allegro risoluto，mm. 15–48',
     'beethoven-op106-iv-mm15-48'),
    ('fugue', 'replace', '宣叙调与哀歌，Adagio ma non troppo，mm. 1–26',
     'beethoven-op110-iii-mm1-26'),
    ('fugue', 'replace', '赋格呈示部，Allegro ma non troppo，mm. 27–56',
     'beethoven-op110-iii-mm27-56'),
    ('articulation', 'replace', '第一乐章 mm. 1–8（大提琴长歌连弓与内声部八分音符分弓异步对位）',
     'beethoven-op59no1-i-mm1-8'),
    ('articulation', 'after', '完成了室内乐史上最震撼的动能骤变',
     'beethoven-op59no1-i-mm18-24'),
]


def main():
    by_art = {}
    for art, mode, anchor, fid in PLAN:
        by_art.setdefault(art, []).append((mode, anchor, fid))
    for art, jobs in by_art.items():
        path = ART[art]
        lines = io.open(path, encoding='utf-8').read().split('\n')
        out = []
        used = set()
        changed = 0
        for line in lines:
            hit = None
            for idx, (mode, anchor, fid) in enumerate(jobs):
                if idx in used:
                    continue
                if anchor in line:
                    hit = (idx, mode, fid)
                    break
            if hit is None:
                out.append(line)
                continue
            idx, mode, fid = hit
            used.add(idx)
            fence = FENCES[fid].rstrip('\n')
            if mode == 'replace':
                out.append(fence)
            elif mode == 'before':
                out.append(fence)
                out.append('')
                out.append(line)
            elif mode == 'after':
                out.append(line)
                out.append('')
                out.append(fence)
            changed += 1
        missing = [jobs[i] for i in range(len(jobs)) if i not in used]
        text = '\n'.join(out)
        io.open(path, 'w', encoding='utf-8', newline='\n').write(text)
        print('%-13s embedded %d/%d  fences now %d  missing %s'
              % (art, changed, len(jobs), text.count('```lilypond'),
                 [m[2] for m in missing] or '-'))
        if missing:
            sys.exit(1)


if __name__ == '__main__':
    main()
