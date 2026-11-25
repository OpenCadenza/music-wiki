#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Round-5 excerpt batch: build every candidate fence body and compile it.

Run:  python build_all.py [id ...]
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
RAW = os.path.join(ROOT, 'local', 'workbench', 'scores', 'score-a-r5', 'raw')
OUT = os.path.join(ROOT, 'local', 'workbench', 'scores', 'score-a-r5', 'out')
LILYPOND = r'E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe'
EMIT = os.path.join(ROOT, 'local', 'workbench', 'tools', 'score-a-r5', 'emit.py')
PY = sys.executable

STRINGS = [
    {'id': 'P1', 'var': 'violinOne', 'clef': 'treble', 'gm': 'violin'},
    {'id': 'P2', 'var': 'violinTwo', 'clef': 'treble', 'gm': 'violin'},
    {'id': 'P3', 'var': 'viola', 'clef': 'alto', 'gm': 'viola'},
    {'id': 'P4', 'var': 'cello', 'clef': 'bass', 'gm': 'cello'},
]

SPECS = {
    # ---------------- 1. Haydn Op.76 No.3 II ----------------
    'haydn-op76no3-ii-mm21-28': {
        'source': 'haydn-op76no3.musicxml', 'segment': 1, 'from': 21, 'to': 28,
        'tempo': '\\tempo "Poco adagio, cantabile" 4 = 56',
        'comment': ['海顿 Op.76 No.3《皇帝》第二乐章，第一变奏（第二小提琴执掌定旋律）。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'haydn-op76no3-ii-mm41-48': {
        'source': 'haydn-op76no3.musicxml', 'segment': 1, 'from': 41, 'to': 48,
        'tempo': '\\tempo "Poco adagio, cantabile" 4 = 56',
        'comment': ['海顿 Op.76 No.3《皇帝》第二乐章，第二变奏（大提琴执掌定旋律）。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'haydn-op76no3-ii-mm72-79': {
        'source': 'haydn-op76no3.musicxml', 'segment': 1, 'from': 72, 'to': 79,
        'tempo': '\\tempo "Poco adagio, cantabile" 4 = 56',
        'comment': ['海顿 Op.76 No.3《皇帝》第二乐章，第三变奏后半：半音阶深渊（passus duriusculus）。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    # ---------------- 3. Debussy Op.10 ----------------
    'debussy-op10-i-mm1-8': {
        'source': 'debussy-op10.musicxml', 'segment': 0, 'from': 1, 'to': 8,
        'tempo': '\\tempo "Animé et très décidé" 4 = 132',
        'comment': ['德彪西 g 小调弦乐四重奏 Op.10 第一乐章，循环动机原型与弗里几亚二级音。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'debussy-op10-i-mm25-32': {
        'source': 'debussy-op10.musicxml', 'segment': 0, 'from': 25, 'to': 32,
        'tempo': '\\tempo "Animé et très décidé" 4 = 132',
        'comment': ['德彪西 Op.10 第一乐章，全音阶渗透与音响平面分层。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'debussy-op10-iii-mm1-8': {
        'source': 'debussy-op10.musicxml', 'segment': 2, 'from': 1, 'to': 8,
        'tempo': '\\tempo "Andantino doucement expressif" 8 = 84',
        'comment': ['德彪西 Op.10 第三乐章，加弱音器的降 D 大调循环主题。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'debussy-op10-iii-mm28-35': {
        'source': 'debussy-op10.musicxml', 'segment': 2, 'from': 28, 'to': 35,
        'tempo': '\\tempo "Andantino doucement expressif" 8 = 84',
        'comment': ['德彪西 Op.10 第三乐章，摘除弱音器后的等音偏转与节拍提速。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    # ---------------- 7. Schubert lieder ----------------
    'schubert-d957no4-mm1-8': {
        'source': 'schubert-d957-04.musicxml', 'segment': 0, 'from': 1, 'to': 8,
        'tempo': '\\tempo "Mässig" 4 = 60',
        'comment': ['舒伯特《小夜曲》D.957/4，钢琴拨奏音型前奏与人声进入。',
                    '据 OpenScore Lieder（CC0-1.0）MXL 核对后自编码摘录；人声声部按原谱记谱音高。'],
        'parts': [
            {'id': 'P1', 'var': 'voice', 'clef': 'treble', 'gm': 'choir aahs'},
            {'id': 'P2', 'var': 'pianoUpper', 'clef': 'treble', 'gm': 'acoustic grand', 'staff': '1'},
            {'id': 'P2', 'var': 'pianoLower', 'clef': 'bass', 'gm': 'acoustic grand', 'staff': '2'},
        ],
    },
    'schubert-d911no1-mm71-82': {
        'source': 'schubert-d911-01.musicxml', 'segment': 0, 'from': 71, 'to': 82,
        'tempo': '\\tempo "Mässig" 4 = 66',
        'comment': ['舒伯特《晚安》D.911/1，D 大调爱情幻境与不变步伐节律。',
                    '据 OpenScore Lieder（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': [
            {'id': 'P1', 'var': 'voice', 'clef': 'treble', 'gm': 'choir aahs'},
            {'id': 'P2', 'var': 'pianoUpper', 'clef': 'treble', 'gm': 'acoustic grand', 'staff': '1'},
            {'id': 'P2', 'var': 'pianoLower', 'clef': 'bass', 'gm': 'acoustic grand', 'staff': '2'},
        ],
    },
    'schubert-d911no5-mm1-8': {
        'source': 'schubert-d911-05.musicxml', 'segment': 0, 'from': 1, 'to': 8,
        'tempo': '\\tempo "Mässig" 4 = 66',
        'comment': ['舒伯特《菩提树》D.911/5，三连音树叶沙沙声前奏与圆号号角动机。',
                    '据 OpenScore Lieder（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': [
            {'id': 'P1', 'var': 'voice', 'clef': 'treble', 'gm': 'choir aahs'},
            {'id': 'P2', 'var': 'pianoUpper', 'clef': 'treble', 'gm': 'acoustic grand', 'staff': '1'},
            {'id': 'P2', 'var': 'pianoLower', 'clef': 'bass', 'gm': 'acoustic grand', 'staff': '2'},
        ],
    },
    'schubert-d911no5-mm45-52': {
        'source': 'schubert-d911-05.musicxml', 'segment': 0, 'from': 45, 'to': 52,
        'tempo': '\\tempo "Mässig" 4 = 66',
        'comment': ['舒伯特《菩提树》D.911/5，第三段严冬风雪中的织体异化。',
                    '据 OpenScore Lieder（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': [
            {'id': 'P1', 'var': 'voice', 'clef': 'treble', 'gm': 'choir aahs'},
            {'id': 'P2', 'var': 'pianoUpper', 'clef': 'treble', 'gm': 'acoustic grand', 'staff': '1'},
            {'id': 'P2', 'var': 'pianoLower', 'clef': 'bass', 'gm': 'acoustic grand', 'staff': '2'},
        ],
    },
    # ---------------- 8. Mozart K.421 ----------------
    'mozart-k421-i-mm1-8': {
        'source': 'mozart-k421.musicxml', 'segment': 0, 'from': 1, 'to': 8,
        'tempo': '\\tempo "Allegro" 4 = 120',
        'comment': ['莫扎特 d 小调第 15 弦乐四重奏 K.421 第一乐章，主部主题与八度下落动机。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'mozart-k421-i-mm25-32': {
        'source': 'mozart-k421.musicxml', 'segment': 0, 'from': 25, 'to': 32,
        'tempo': '\\tempo "Allegro" 4 = 120',
        'comment': ['莫扎特 K.421 第一乐章，F 大调副部的双小提琴对话与内声部十六分音符织体。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'mozart-k421-ii-mm1-8': {
        'source': 'mozart-k421.musicxml', 'segment': 1, 'from': 1, 'to': 8,
        'tempo': '\\tempo "Andante" 4 = 60',
        'comment': ['莫扎特 K.421 第二乐章，F 大调西西里行板主题的四部交错对位。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'mozart-k421-ii-mm36-43': {
        'source': 'mozart-k421.musicxml', 'segment': 1, 'from': 36, 'to': 43,
        'tempo': '\\tempo "Andante" 4 = 60',
        'comment': ['莫扎特 K.421 第二乐章，降 III 级（降 A 大调）阴影侵入的对比段。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    # ---------------- 9. Schubert D.810 II ----------------
    'schubert-d810-ii-mm1-8': {
        'source': 'schubert-d810.musicxml', 'segment': 1, 'from': 1, 'to': 8,
        'tempo': '\\tempo "Andante con moto" 4 = 60',
        'comment': ['舒伯特 d 小调第 14 弦乐四重奏 D.810《死与少女》第二乐章，达克提尔圣咏主题前段。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'schubert-d810-ii-mm49-56': {
        'source': 'schubert-d810.musicxml', 'segment': 1, 'from': 49, 'to': 56,
        'tempo': '\\tempo "Andante con moto" 4 = 60',
        'comment': ['舒伯特 D.810 第二乐章，变奏 II：大提琴高音区哀歌主调。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'schubert-d810-ii-mm73-80': {
        'source': 'schubert-d810.musicxml', 'segment': 1, 'from': 73, 'to': 80,
        'tempo': '\\tempo "Andante con moto" 4 = 60',
        'comment': ['舒伯特 D.810 第二乐章，变奏 III：狂暴全奏与断奏三连音。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'schubert-d810-ii-mm97-104': {
        'source': 'schubert-d810.musicxml', 'segment': 1, 'from': 97, 'to': 104,
        'tempo': '\\tempo "Andante con moto" 4 = 60',
        'comment': ['舒伯特 D.810 第二乐章，变奏 IV：转入 G 大调的空灵圣咏。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    # ---------------- 10. Brahms Op.51 No.1 ----------------
    'brahms-op51no1-i-mm11-18': {
        'source': 'brahms-op51no1.musicxml', 'segment': 0, 'from': 11, 'to': 18,
        'tempo': '\\tempo "Allegro" 2 = 76',
        'comment': ['勃拉姆斯 c 小调第一弦乐四重奏 Op.51 No.1 第一乐章，主部尾声的四部合唱经文歌。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'brahms-op51no1-i-mm35-42': {
        'source': 'brahms-op51no1.musicxml', 'segment': 0, 'from': 35, 'to': 42,
        'tempo': '\\tempo "Allegro" 2 = 76',
        'comment': ['勃拉姆斯 Op.51 No.1 第一乐章，降 E 小调副部：中提琴脉冲踏板与四部密集和声。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'brahms-op51no1-iv-mm1-12': {
        'source': 'brahms-op51no1.musicxml', 'index_from': 510, 'index_to': 521,
        'tempo': '\\tempo "Allegro" 2 = 92',
        'comment': ['勃拉姆斯 Op.51 No.1 第四乐章，四部同度圣咏起句与紧凑和声对位。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录；',
                    '该 MXL 第三、四乐章连续编号，此处 mm.1–12 对应源文件印刷小节号 145–156。'],
        'parts': STRINGS,
    },
    'brahms-op51no1-iv-mm71-80': {
        'source': 'brahms-op51no1.musicxml', 'index_from': 580, 'index_to': 589,
        'tempo': '\\tempo "Allegro" 2 = 92',
        'comment': ['勃拉姆斯 Op.51 No.1 第四乐章，大提琴属踏板音上方的三声部圣咏合唱。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录；',
                    '此处 mm.71–80 对应源文件印刷小节号 215–224。'],
        'parts': STRINGS,
    },
}

# ---------------- 2. Haydn Hob.I:104 I ----------------
HAYDN_WOOD = [
    {'id': 'P1', 'var': 'fluteOne', 'clef': 'treble', 'gm': 'flute'},
    {'id': 'P3', 'var': 'oboeOne', 'clef': 'treble', 'gm': 'oboe'},
    {'id': 'P5', 'var': 'clarinetOne', 'clef': 'treble', 'gm': 'clarinet'},
    {'id': 'P7', 'var': 'bassoonOne', 'clef': 'bass', 'gm': 'bassoon'},
]
HAYDN_STRINGS4 = [
    {'id': 'P14', 'var': 'violinOne', 'clef': 'treble', 'gm': 'violin'},
    {'id': 'P15', 'var': 'violinTwo', 'clef': 'treble', 'gm': 'violin'},
    {'id': 'P16', 'var': 'viola', 'clef': 'alto', 'gm': 'viola'},
    {'id': 'P17', 'var': 'cello', 'clef': 'bass', 'gm': 'cello'},
]
SPECS.update({
    'schubert-d911no5-mm25-32': {
        'source': 'schubert-d911-05.musicxml', 'segment': 0, 'from': 25, 'to': 32,
        'tempo': '\\tempo "Mässig" 4 = 66',
        'comment': ['舒伯特《菩提树》D.911/5，第二段同主音小调（e 小调）的阴沉转折。',
                    '据 OpenScore Lieder（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': [
            {'id': 'P1', 'var': 'voice', 'clef': 'treble', 'gm': 'choir aahs'},
            {'id': 'P2', 'var': 'pianoUpper', 'clef': 'treble', 'gm': 'acoustic grand', 'staff': '1'},
            {'id': 'P2', 'var': 'pianoLower', 'clef': 'bass', 'gm': 'acoustic grand', 'staff': '2'},
        ],
    },
    'haydn-op76no3-ii-mm81-88': {
        'source': 'haydn-op76no3.musicxml', 'segment': 1, 'from': 81, 'to': 88,
        'tempo': '\\tempo "Poco adagio, cantabile" 4 = 56',
        'comment': ['海顿 Op.76 No.3《皇帝》第二乐章，第四变奏起点的阻碍式和声截击与高八度重现。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'debussy-op10-iii-mm107-114': {
        'source': 'debussy-op10.musicxml', 'segment': 2, 'from': 107, 'to': 114,
        'tempo': '\\tempo "Andantino doucement expressif" 8 = 84',
        'comment': ['德彪西 Op.10 第三乐章尾声，重戴弱音器后的色彩消融。',
                    '据 OpenScore StringQuartets（CC0-1.0）MXL 核对后自编码摘录。'],
        'parts': STRINGS,
    },
    'haydn-hob1-104-i-adagio-mm1-2': {
        'source': 'haydn104-mvt1.musicxml', 'segment': 0, 'from': 1, 'to': 2,
        'tempo': '\\tempo "Adagio" 4 = 44',
        'comment': ['海顿 D 大调第 104 交响曲第一乐章，慢引子开篇：空五度号角齐奏（木管与弦乐齐奏，无三音）。',
                    '据 MuseData/CCARH 转写本（kern / MusicXML）核对后自编码摘录，学术用途。'],
        'parts': HAYDN_WOOD + HAYDN_STRINGS4,
    },
    'haydn-hob1-104-i-adagio-mm3-8': {
        'source': 'haydn104-mvt1.musicxml', 'segment': 0, 'from': 3, 'to': 8,
        'tempo': '\\tempo "Adagio" 4 = 44',
        'comment': ['海顿 Hob.I:104 第一乐章慢引子，D 小调悲叹与 F 大调全奏突袭（管乐声部从略）。',
                    '据 MuseData/CCARH 转写本（kern / MusicXML）核对后自编码摘录，学术用途。'],
        'parts': [{'id': 'P7', 'var': 'bassoonOne', 'clef': 'bass', 'gm': 'bassoon'}] + HAYDN_STRINGS4,
    },
    'haydn-hob1-104-i-adagio-mm9-16': {
        'source': 'haydn104-mvt1.musicxml', 'segment': 0, 'from': 9, 'to': 16,
        'tempo': '\\tempo "Adagio" 4 = 44',
        'comment': ['海顿 Hob.I:104 第一乐章慢引子，半音阶攀升与属音锁定（弦乐声部）。',
                    '据 MuseData/CCARH 转写本（kern / MusicXML）核对后自编码摘录，学术用途。'],
        'parts': HAYDN_STRINGS4,
    },
    # ---------------- 4. Mozart K.550 I ----------------
    'mozart-k550-i-mm1-14': {
        'source': 'mozart-k550-i.musicxml', 'segment': 0, 'from': 1, 'to': 14,
        'tempo': '\\tempo "Molto allegro" 2 = 88',
        'comment': ['莫扎特 g 小调第 40 交响曲 K.550 第一乐章，主部主题（弦乐）的陈述—延续—终止句法。',
                    '据 OpenScore 转写体核对后自编码摘录；该底本许可待确认，仅作学术引用。'],
        'parts': [
            {'id': 'P8', 'var': 'violinOne', 'clef': 'treble', 'gm': 'violin'},
            {'id': 'P9', 'var': 'violinTwo', 'clef': 'treble', 'gm': 'violin'},
            {'id': 'P10', 'var': 'viola', 'clef': 'alto', 'gm': 'viola'},
            {'id': 'P11', 'var': 'cello', 'clef': 'bass', 'gm': 'cello'},
        ],
    },
    'mozart-k550-i-mm138-149': {
        'source': 'mozart-k550-i.musicxml', 'segment': 0, 'from': 138, 'to': 149,
        'tempo': '\\tempo "Molto allegro" 2 = 88',
        'comment': ['莫扎特 K.550 第一乐章，属准备段木管与弦乐的一小节交替下行对话。',
                    '据 OpenScore 转写体核对后自编码摘录；该底本许可待确认，仅作学术引用。'],
        'parts': [
            {'id': 'P3', 'var': 'flute', 'clef': 'treble', 'gm': 'flute'},
            {'id': 'P1', 'var': 'oboeOne', 'clef': 'treble', 'gm': 'oboe'},
            {'id': 'P8', 'var': 'violinOne', 'clef': 'treble', 'gm': 'violin'},
            {'id': 'P9', 'var': 'violinTwo', 'clef': 'treble', 'gm': 'violin'},
            {'id': 'P10', 'var': 'viola', 'clef': 'alto', 'gm': 'viola'},
            {'id': 'P11', 'var': 'cello', 'clef': 'bass', 'gm': 'cello'},
        ],
    },
    'mozart-k550-i-mm16-24': {
        'source': 'mozart-k550-i.musicxml', 'segment': 0, 'from': 16, 'to': 24,
        'tempo': '\\tempo "Molto allegro" 2 = 88',
        'comment': ['莫扎特 K.550 第一乐章，主部群全奏爆发与 B♭ 调、G 调双圆号合流（圆号按记谱音写，带移调声明）。',
                    '据 OpenScore 转写体核对后自编码摘录；该底本许可待确认，仅作学术引用。'],
        'parts': [
            {'id': 'P3', 'var': 'flute', 'clef': 'treble', 'gm': 'flute'},
            {'id': 'P1', 'var': 'oboeOne', 'clef': 'treble', 'gm': 'oboe'},
            {'id': 'P2', 'var': 'clarinetOne', 'clef': 'treble', 'gm': 'clarinet'},
            {'id': 'P5', 'var': 'bassoon', 'clef': 'bass', 'gm': 'bassoon'},
            {'id': 'P6', 'var': 'hornOne', 'clef': 'treble', 'gm': 'french horn'},
            {'id': 'P7', 'var': 'hornTwo', 'clef': 'treble', 'gm': 'french horn'},
            {'id': 'P8', 'var': 'violinOne', 'clef': 'treble', 'gm': 'violin'},
            {'id': 'P9', 'var': 'violinTwo', 'clef': 'treble', 'gm': 'violin'},
            {'id': 'P10', 'var': 'viola', 'clef': 'alto', 'gm': 'viola'},
            {'id': 'P11', 'var': 'cello', 'clef': 'bass', 'gm': 'cello'},
        ],
    },
})

KEYTIME = {'haydn-op76no3-ii-mm21-28': ('g major', '2/2'), 'haydn-op76no3-ii-mm41-48': ('g major', '2/2'), 'haydn-op76no3-ii-mm72-79': ('g major', '2/2'), 'debussy-op10-i-mm1-8': ('g minor', '4/4'), 'debussy-op10-i-mm25-32': ('g minor', '4/4'), 'debussy-op10-iii-mm1-8': ('df major', '6/8'), 'debussy-op10-iii-mm28-35': ('cs minor', '3/8'), 'schubert-d957no4-mm1-8': ('d minor', '3/4'), 'schubert-d911no1-mm71-82': ('d major', '2/4'), 'schubert-d911no5-mm1-8': ('e major', '3/4'), 'schubert-d911no5-mm45-52': ('e major', '3/4'), 'mozart-k421-i-mm1-8': ('d minor', '4/4'), 'mozart-k421-i-mm25-32': ('d minor', '4/4'), 'mozart-k421-ii-mm1-8': ('f major', '6/8'), 'mozart-k421-ii-mm36-43': ('f major', '6/8'), 'schubert-d810-ii-mm1-8': ('g minor', '2/2'), 'schubert-d810-ii-mm49-56': ('g minor', '2/2'), 'schubert-d810-ii-mm73-80': ('g minor', '2/2'), 'schubert-d810-ii-mm97-104': ('g major', '2/2'), 'brahms-op51no1-i-mm11-18': ('c minor', '3/2'), 'brahms-op51no1-i-mm35-42': ('c minor', '3/2'), 'brahms-op51no1-iv-mm1-12': ('c minor', '2/2'), 'brahms-op51no1-iv-mm71-80': ('c minor', '2/2'), 'haydn-hob1-104-i-adagio-mm1-2': ('d minor', '4/4'), 'haydn-hob1-104-i-adagio-mm3-8': ('d minor', '4/4'), 'haydn-hob1-104-i-adagio-mm9-16': ('d minor', '4/4'), 'mozart-k550-i-mm1-16': ('g minor', '2/2'), 'mozart-k550-i-mm16-24': ('g minor', '2/2')}

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    want = sys.argv[1:]
    ok, bad = [], []
    for ex_id, spec in SPECS.items():
        if want and ex_id not in want:
            continue
        spec = dict(spec)
        if ex_id in KEYTIME:
            spec['key'], spec['time'] = KEYTIME[ex_id]
        spec['source'] = os.path.join(RAW, spec['source'])
        spec_path = os.path.join(OUT, ex_id + '.json')
        with open(spec_path, 'w', encoding='utf-8', newline='\n') as f:
            json.dump(spec, f, ensure_ascii=False, indent=2)
        ly = os.path.join(OUT, ex_id + '.ly')
        r = subprocess.run([PY, EMIT, spec_path, ly], capture_output=True, text=True)
        if r.returncode != 0:
            bad.append((ex_id, 'emit failed', r.stderr.strip().splitlines()[-1:]))
            continue
        r2 = subprocess.run([LILYPOND, '-dno-print-pages', '-o',
                             os.path.join(OUT, ex_id), ly],
                            capture_output=True, text=True)
        msgs = [ln for ln in (r2.stdout + r2.stderr).splitlines()
                if 'warning' in ln or 'error' in ln or 'Success' in ln]
        if 'Success' in (r2.stdout + r2.stderr):
            ok.append((ex_id, msgs))
        else:
            bad.append((ex_id, 'compile failed', msgs[-4:]))
    for ex_id, msgs in ok:
        print('OK   ', ex_id, '' if not msgs or msgs == ['Success: compilation successfully completed'] else msgs[:3])
    for ex_id, why, msgs in bad:
        print('FAIL ', ex_id, why, msgs)
