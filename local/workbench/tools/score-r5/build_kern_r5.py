#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Build the round-5 kern->LilyPond excerpts for score-c.

Writes one .ly per excerpt under local/workbench/scores/score-c-r5/ and a
fences JSON with the full ```lilypond``` blocks for embedding.

Bottom-text measure numbering follows the printed (刊本) numbers used in the
articles; the kern file numbers repeated second endings as extra measures, so
the `kern range` in each fence comment records the raw kern measures.

Usage: python build_kern_r5.py [only-id ...]
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
KERN = os.path.join(
    ROOT, 'local/resources/scores/source-packages/beethoven-score-sources')
SONATAS = os.path.join(KERN, 'beethoven-piano-sonatas-main',
                       'beethoven-piano-sonatas-main', 'kern')
QUARTETS = os.path.join(KERN, 'beethoven-string-quartets-main',
                        'beethoven-string-quartets-main', 'kern')
OUT = os.path.join(ROOT, 'local/workbench/scores/score-c-r5')

COMMENT = ['据 CCARH MuseData（CCARH）转写，学术用途。']

PIANO = [
    {'var': 'upper', 'staff': 1, 'clef': 'treble', 'gm': 'acoustic grand',
     'label': 'RH', 'prefix': 'rh'},
    {'var': 'lower', 'staff': 2, 'clef': 'bass', 'gm': 'acoustic grand',
     'label': 'LH', 'prefix': 'lh'},
]
QUARTET = [
    {'var': 'violinI', 'staff': 1, 'clef': 'treble', 'gm': 'violin',
     'label': 'VlnI', 'prefix': 'vlnI'},
    {'var': 'violinII', 'staff': 2, 'clef': 'treble', 'gm': 'violin',
     'label': 'VlnII', 'prefix': 'vlnII'},
    {'var': 'viola', 'staff': 3, 'clef': 'alto', 'gm': 'viola',
     'label': 'Vla', 'prefix': 'vla'},
    {'var': 'cello', 'staff': 4, 'clef': 'bass', 'gm': 'cello',
     'label': 'Vc', 'prefix': 'vc'},
]


def kern_note(kern_range, printed):
    return ('底本 kern 连续编号 %s（反复第二结尾另计小节）；此处按刊本印刷号 %s 标注。'
            % (kern_range, printed))


SPECS = [
    {
        'id': 'beethoven-op109-iii-mm17-32',
        'kern': os.path.join(SONATAS, 'sonata30-3.krn'),
        'from': 17, 'to': 35, 'staves': PIANO,
        'title': '贝多芬 第30钢琴奏鸣曲 Op.109 第三乐章',
        'location': 'Variation I: Molto espressivo，mm.17–32',
        'tempo_text': 'Molto espressivo',
        'kern_labels': True,
        'extra_comment': kern_note('mm.17–35', 'mm.17–32'),
    },
    {
        'id': 'beethoven-op109-iii-mm33-48',
        'kern': os.path.join(SONATAS, 'sonata30-3.krn'),
        'from': 36, 'to': 51, 'staves': PIANO,
        'title': '贝多芬 第30钢琴奏鸣曲 Op.109 第三乐章',
        'location': 'Variation II: Leggiermente，mm.33–48',
        'tempo_text': 'Leggiermente',
        'kern_labels': True,
        'extra_comment': kern_note('mm.36–51', 'mm.33–48'),
    },
    {
        'id': 'beethoven-op109-iii-mm113-128',
        'kern': os.path.join(SONATAS, 'sonata30-3.krn'),
        'from': 120, 'to': 135, 'staves': PIANO,
        'title': '贝多芬 第30钢琴奏鸣曲 Op.109 第三乐章',
        'location': 'Variation V: Allegro, ma non troppo，mm.113–128',
        'tempo_text': 'Allegro, ma non troppo',
        'kern_labels': True,
        'extra_comment': kern_note('mm.120–135', 'mm.113–128'),
    },
    {
        'id': 'beethoven-op111-ii-mm1-16',
        'kern': os.path.join(SONATAS, 'sonata32-2.krn'),
        'from': 1, 'to': 18, 'staves': PIANO,
        'title': '贝多芬 第32钢琴奏鸣曲 Op.111 第二乐章',
        'location': 'Arietta: Adagio molto semplice e cantabile，mm.1–16',
        'tempo_text': 'Adagio molto semplice e cantabile',
        'kern_labels': True,
        'extra_comment': kern_note('mm.1–18', 'mm.1–16'),
    },
    {
        'id': 'beethoven-op111-ii-mm33-48',
        'kern': os.path.join(SONATAS, 'sonata32-2.krn'),
        'from': 36, 'to': 54, 'staves': PIANO,
        'title': '贝多芬 第32钢琴奏鸣曲 Op.111 第二乐章',
        'location': "Variation II: L'istesso tempo，mm.33–48",
        'tempo_text': "L'istesso tempo",
        'kern_labels': True,
        'extra_comment': kern_note('mm.36–54', 'mm.33–48'),
    },
    {
        'id': 'beethoven-op106-iv-mm1-14',
        'kern': os.path.join(SONATAS, 'sonata29-4.krn'),
        'from': 1, 'to': 14, 'staves': PIANO,
        'title': '贝多芬 第29钢琴奏鸣曲 Op.106 第四乐章',
        'location': 'Largo，mm.1–14',
        'tempo_text': 'Largo',
    },
    {
        'id': 'beethoven-op106-iv-mm15-48',
        'kern': os.path.join(SONATAS, 'sonata29-4.krn'),
        'from': 15, 'to': 48, 'staves': PIANO,
        'title': '贝多芬 第29钢琴奏鸣曲 Op.106 第四乐章',
        'location': 'Allegro risoluto，mm.15–48',
        'tempo_text': 'Allegro risoluto',
    },
    {
        'id': 'beethoven-op110-iii-mm1-26',
        'kern': os.path.join(SONATAS, 'sonata31-3.krn'),
        'from': 1, 'to': 26, 'staves': PIANO,
        'title': '贝多芬 第31钢琴奏鸣曲 Op.110 第三乐章',
        'location': 'Adagio ma non troppo — Arioso dolente，mm.1–26',
        'tempo_text': 'Adagio ma non troppo',
    },
    {
        'id': 'beethoven-op110-iii-mm27-56',
        'kern': os.path.join(SONATAS, 'sonata31-3.krn'),
        'from': 27, 'to': 56, 'staves': PIANO,
        'title': '贝多芬 第31钢琴奏鸣曲 Op.110 第三乐章',
        'location': 'Fuga: Allegro ma non troppo，mm.27–56',
        'tempo_text': 'Allegro ma non troppo',
    },
    {
        'id': 'beethoven-op59no1-i-mm1-8',
        'kern': os.path.join(QUARTETS, 'quartet07-1.krn'),
        'from': 1, 'to': 8, 'staves': QUARTET,
        'title': '贝多芬 第7弦乐四重奏 Op.59 No.1 第一乐章',
        'location': 'Allegro，mm.1–8',
        'tempo_text': 'Allegro',
    },
    {
        'id': 'beethoven-op59no1-i-mm18-24',
        'kern': os.path.join(QUARTETS, 'quartet07-1.krn'),
        'from': 18, 'to': 24, 'staves': QUARTET,
        'title': '贝多芬 第7弦乐四重奏 Op.59 No.1 第一乐章',
        'location': 'Allegro，mm.18–24',
        'tempo_text': None,
    },
]


def main():
    sys.path.insert(0, HERE)
    import kern2ly

    only = set(sys.argv[1:])
    os.makedirs(OUT, exist_ok=True)
    cache = {}
    fences = {}
    for spec in SPECS:
        if only and spec['id'] not in only:
            continue
        path = spec['kern']
        if path not in cache:
            cache[path] = kern2ly.load(path)
        piece = cache[path]
        comment = COMMENT + ([spec['extra_comment']]
                             if spec.get('extra_comment') else [])
        body = kern2ly.emit(piece, dict(spec, comment=comment))
        lines = body.split('\n')
        code = '\n'.join(lines[1:]) if lines[0].startswith('```') else body
        ly = os.path.join(OUT, spec['id'] + '.ly')
        open(ly, 'w', encoding='utf-8', newline='\n').write(code + '\n')
        fence = body + '\n```'
        fences[spec['id']] = fence
        os.makedirs(os.path.join(OUT, 'specs'), exist_ok=True)
        with open(os.path.join(OUT, 'specs', spec['id'] + '.json'), 'w',
                  encoding='utf-8', newline='\n') as fh:
            json.dump(dict(spec, comment=comment), fh, ensure_ascii=False, indent=1)
        print('%-34s %5d bytes' % (spec['id'], len(code)))
    with open(os.path.join(OUT, 'fences.json'), 'w', encoding='utf-8',
              newline='\n') as fh:
        json.dump(fences, fh, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
