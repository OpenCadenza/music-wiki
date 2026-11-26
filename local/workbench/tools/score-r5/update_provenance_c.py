#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update the three provenance files' 谱例 tables for the round-5 kern excerpts."""
import io
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', '..', '..', '..'))
LIC = '据 CCARH MuseData 转写，学术用途'
KERN30 = 'CCARH Humdrum Kern `sonata30-3.krn`'
KERN32 = 'CCARH Humdrum Kern `sonata32-2.krn`'
KERN29 = 'CCARH Humdrum Kern `sonata29-4.krn`'
KERN31 = 'CCARH Humdrum Kern `sonata31-3.krn`'
KERN07 = 'CCARH Humdrum Kern `quartet07-1.krn`'
OP109 = '贝多芬《E大调第30钢琴奏鸣曲》Op. 109 第三乐章'
OP111 = '贝多芬《c小调第32钢琴奏鸣曲》Op. 111 第二乐章'
OP106 = '贝多芬《降B大调第29钢琴奏鸣曲“槌子键琴”》Op. 106 第四乐章'
OP110 = '贝多芬《降A大调第31钢琴奏鸣曲》Op. 110 第三乐章'
OP59 = '贝多芬《F大调第七弦乐四重奏》Op. 59 No. 1 第一乐章'


def row(fid, work, loc, src):
    return '| `%s` | %s | %s | %s | %s |' % (fid, work, loc, src, LIC)


VARIATION = os.path.join(ROOT, 'provenance/techniques/structure/'
                               'variation-types-and-structural-transformations.md')
FUGUE = os.path.join(ROOT, 'provenance/techniques/counterpoint/'
                           'fugue-in-the-sonata-cycle.md')
ARTIC = os.path.join(ROOT, 'provenance/notation/'
                           'articulation-marks-and-realization.md')


def patch(path, pairs):
    text = io.open(path, encoding='utf-8').read()
    for old, new in pairs:
        if old not in text:
            raise SystemExit('MISS in %s:\n%s' % (os.path.basename(path), old[:120]))
        text = text.replace(old, new, 1)
    io.open(path, 'w', encoding='utf-8', newline='\n').write(text)
    print('patched', os.path.basename(path))


patch(VARIATION, [
    ('| 占位（未出谱） | %s | 主题 Gesangvoll, mit innigster Empfindung，mm. 1–16 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP109, KERN30),
     '| `beethoven-op109-iii-mm1-8`（关联引用） | %s | 主题 Gesangvoll, mit innigster Empfindung，mm. 1–8 | %s；谱例见 `content/techniques/harmony/augmented-sixth-mechanics-and-syntactic-drift.md` | %s |'
     % (OP109, KERN30, LIC)),
    ('| 占位（未出谱） | %s | 第一变奏与第二变奏，mm. 17–48 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP109, KERN30),
     row('beethoven-op109-iii-mm17-32', OP109,
         'Variation I: Molto espressivo，mm.17–32（底本 kern 连续编号 mm.17–35，含反复第二结尾）',
         KERN30) + '\n' +
     row('beethoven-op109-iii-mm33-48', OP109,
         'Variation II: Leggiermente，mm.33–48（底本 kern 连续编号 mm.36–51）',
         KERN30)),
    ('| 占位（未出谱） | %s | 第五变奏 Allegro, ma non troppo，mm. 113–128 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP109, KERN30),
     row('beethoven-op109-iii-mm113-128', OP109,
         'Variation V: Allegro, ma non troppo，mm.113–128（底本 kern 连续编号 mm.120–135）',
         KERN30)),
    ('| 占位（未出谱） | %s | Arietta: Adagio molto semplice e cantabile，mm. 1–16 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP111, KERN32),
     row('beethoven-op111-ii-mm1-16', OP111,
         'Arietta: Adagio molto semplice e cantabile，mm.1–16（底本 kern 连续编号 mm.1–18，含反复第二结尾）',
         KERN32)),
    ('| 占位（未出谱） | %s | 第二变奏 L\'istesso tempo，mm. 33–48 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP111, KERN32),
     row('beethoven-op111-ii-mm33-48', OP111,
         "Variation II: L'istesso tempo，mm.33–48（底本 kern 连续编号 mm.36–54）",
         KERN32)),
])

patch(FUGUE, [
    ('| 占位（未出谱） | %s | 引子，Largo，mm. 1–14 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP106, KERN29),
     row('beethoven-op106-iv-mm1-14', OP106, 'Largo，mm.1–14', KERN29)),
    ('| 占位（未出谱） | %s | 赋格呈示部，Allegro risoluto，mm. 15–48 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP106, KERN29),
     row('beethoven-op106-iv-mm15-48', OP106,
         'Allegro risoluto，mm.15–48', KERN29)),
    ('| 占位（未出谱） | %s | 宣叙调与哀歌，Adagio ma non troppo，mm. 1–26 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP110, KERN31),
     row('beethoven-op110-iii-mm1-26', OP110,
         'Adagio ma non troppo — Arioso dolente，mm.1–26（12/16 自 m.8 起）', KERN31)),
    ('| 占位（未出谱） | %s | 赋格呈示部，Allegro ma non troppo，mm. 27–56 | %s | 据 CCARH 转写，学术用途（单行文本占位） |'
     % (OP110, KERN31),
     row('beethoven-op110-iii-mm27-56', OP110,
         'Fuga: Allegro ma non troppo，mm.27–56（含 m.27 末尾哀歌和弦→6/8 赋格起句）', KERN31)),
])

patch(ARTIC, [
    ('| 占位（未出谱） | %s | mm.1–8、mm.18–24 | 本地 CCARH MuseData kern `quartet07-1.krn`（仅核对，未转写） | 公有领域（据 CCARH MuseData 转写，学术用途） |'
     % OP59,
     row('beethoven-op59no1-i-mm1-8', OP59,
         'Allegro，mm.1–8（大提琴主题与内声部八分音符分弓）', KERN07) + '\n' +
     row('beethoven-op59no1-i-mm18-24', OP59,
         'Allegro，mm.18–24（ff 爆发后的断音与休止撕裂）', KERN07)),
    ('> 谱例均由本项目从 MusicXML 逐音转写为 LilyPond（自写转换器 `local/workbench/scores/score-b/tools/mxl2ly.py`），八度映射经 MIDI 实测校准（`c\'` = 中央 C）。只截取论证所需片段，不构成完整乐谱的再分发。',
     '> 谱例均由本项目从 MusicXML 或 Humdrum Kern 逐音转写为 LilyPond：MusicXML 见 `local/workbench/tools/score-r5/mxl2ly.py`，Kern 见 `local/workbench/tools/score-r5/kern2ly.py`（转换结果另以编译 MIDI 的音高集合逐谱表回比对 kern 模型）。八度映射经 MIDI 实测校准（`c\'` = 中央 C）。只截取论证所需片段，不构成完整乐谱的再分发。'),
])
