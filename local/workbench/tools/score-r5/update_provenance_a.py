#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rewrite the 谱例 tables of the ten A-group provenance files with the new fence ids."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
PROV = os.path.join(ROOT, 'provenance')

OSQ = 'OpenScore StringQuartets（CC0-1.0）%s 自编码摘录'
OSL = 'OpenScore Lieder（CC0-1.0）%s 自编码摘录'
MD104 = 'MuseData/CCARH kern 与 OpenScore 转写体 MusicXML 比对后自编码'
K550S = 'OpenScore 转写体 MusicXML（许可待确认）核对后自编码'

HAYDN76 = '海顿《C大调弦乐四重奏》Op.76 No.3 第二乐章'
DEB1 = '德彪西《g小调弦乐四重奏》Op.10 第一乐章'
DEB3 = '德彪西《g小调弦乐四重奏》Op.10 第三乐章'
D810T = '舒伯特《d小调第14弦乐四重奏“死与少女”》D.810 第二乐章'
K421_1 = '莫扎特《d小调第15弦乐四重奏》K.421 第一乐章'
K421_2 = '莫扎特《d小调第15弦乐四重奏》K.421 第二乐章'
BR1 = '勃拉姆斯《C小调第一弦乐四重奏》Op.51 No.1 第一乐章'
BR4 = '勃拉姆斯《C小调第一弦乐四重奏》Op.51 No.1 第四乐章'
H104 = '海顿《D大调第104交响曲》Hob.I:104 第一乐章'
K550T = '莫扎特《G小调第四十交响曲》K.550 第一乐章'

ROWS = {
    'techniques/counterpoint/cantus-firmus-variation-and-conversational-counterpoint': [
        ('`haydn-op76no3-ii-mm1-20`（关联引用）', HAYDN76, 'Poco adagio, cantabile，mm.1–20（谱例收录于《弦乐四重奏》）',
         OSQ % '`sq20428156.mxl`', 'CC0-1.0'),
        ('`haydn-op76no3-ii-mm21-28`', HAYDN76, 'Poco adagio, cantabile，mm.21–28', OSQ % '`sq20428156.mxl`', 'CC0-1.0'),
        ('`haydn-op76no3-ii-mm41-48`', HAYDN76, 'Poco adagio, cantabile，mm.41–48', OSQ % '`sq20428156.mxl`', 'CC0-1.0'),
        ('`haydn-op76no3-ii-mm72-79`', HAYDN76, 'Poco adagio, cantabile，mm.72–79', OSQ % '`sq20428156.mxl`', 'CC0-1.0'),
        ('`haydn-op76no3-ii-mm81-88`', HAYDN76, 'Poco adagio, cantabile，mm.81–88', OSQ % '`sq20428156.mxl`', 'CC0-1.0'),
    ],
    'techniques/structure/slow-introduction-and-allegro-transition': [
        ('`haydn-hob1-104-i-adagio-mm1-2`', H104, 'Adagio，mm.1–2（木管与弦乐齐奏）', MD104, '据 CCARH MuseData 转写，学术用途'),
        ('`haydn-hob1-104-i-adagio-mm3-8`', H104, 'Adagio，mm.3–8（弦乐四部＋第一大管）', MD104, '据 CCARH MuseData 转写，学术用途'),
        ('`haydn-hob1-104-i-adagio-mm9-16`', H104, 'Adagio，mm.9–16（弦乐四部）', MD104, '据 CCARH MuseData 转写，学术用途'),
        ('`haydn-hob1-104-i-mm17-31`（关联引用）', H104, 'Allegro，mm.17–32（源编号 17–31，收录于《管弦乐音色转型》）',
         MD104, '据 CCARH MuseData 转写，学术用途'),
        ('`haydn-hob1-104-i-mm32-39`（关联引用）', H104, 'Allegro，mm.33–40（源编号 32–39，收录于《管弦乐音色转型》）',
         MD104, '据 CCARH MuseData 转写，学术用途'),
    ],
    'techniques/sound/debussy-quartet-timbre-and-harmonic-color': [
        ('`debussy-op10-i-mm1-8`', DEB1, 'Animé et très décidé，mm.1–8', OSQ % '`sq8661306.mxl`', 'CC0-1.0'),
        ('`debussy-op10-i-mm25-32`', DEB1, 'Animé et très décidé，mm.25–32', OSQ % '`sq8661306.mxl`', 'CC0-1.0'),
        ('`debussy-op10-iii-mm1-8`', DEB3, 'Andantino doucement expressif，mm.1–8', OSQ % '`sq8661306.mxl`', 'CC0-1.0'),
        ('`debussy-op10-iii-mm28-35`', DEB3, 'Andantino doucement expressif，mm.28–35', OSQ % '`sq8661306.mxl`', 'CC0-1.0'),
        ('`debussy-op10-iii-mm107-114`', DEB3, 'Andantino doucement expressif，mm.107–114', OSQ % '`sq8661306.mxl`', 'CC0-1.0'),
    ],
    'techniques/sound/mozart-k550-syntax-and-orchestration': [
        ('`mozart-k550-i-mm1-14`', K550T, 'Molto allegro，mm.1–14（弦乐主部主题）', K550S, '学术用途（底本许可待确认）'),
        ('`mozart-k550-i-mm16-24`', K550T, 'Molto allegro，mm.16–24（全奏＋B♭/G 双圆号）', K550S, '学术用途（底本许可待确认）'),
        ('`mozart-k550-i-mm138-149`', K550T, 'Molto allegro，mm.138–149（属准备木管与弦乐交替）', K550S, '学术用途（底本许可待确认）'),
    ],
    'techniques/sound/schubert-lieder-piano-role': [
        ('`schubert-d957no4-mm1-8`', '舒伯特《小夜曲》D.957 No.4', 'Mässig，mm.1–8', OSL % '`lc5004835.mxl`', 'CC0-1.0'),
        ('`schubert-d911no5-mm1-8`', '舒伯特《菩提树》D.911 No.5', 'Mässig，mm.1–8', OSL % '`lc5016466.mxl`', 'CC0-1.0'),
        ('`schubert-d911no1-mm71-82`', '舒伯特《晚安》D.911 No.1', 'Mässig, in gehender Bewegung，mm.71–82', OSL % '`lc5015378.mxl`', 'CC0-1.0'),
        ('`schubert-d911no5-mm25-32`', '舒伯特《菩提树》D.911 No.5', 'Mässig，第二段 e 小调转折，mm.25–32', OSL % '`lc5016466.mxl`', 'CC0-1.0'),
        ('`schubert-d911no5-mm45-52`', '舒伯特《菩提树》D.911 No.5', 'Mässig，第三段冬季风暴，mm.45–52', OSL % '`lc5016466.mxl`', 'CC0-1.0'),
    ],
    'techniques/counterpoint/mozart-quartet-conversational-counterpoint': [
        ('`mozart-k421-i-mm1-8`', K421_1, 'Allegro moderato，mm.1–8', OSQ % '`sq7294793.mxl`', 'CC0-1.0'),
        ('`mozart-k421-i-mm25-32`', K421_1, 'Allegro moderato，mm.25–32', OSQ % '`sq7294793.mxl`', 'CC0-1.0'),
        ('`mozart-k421-ii-mm1-8`', K421_2, 'Andante（西西里行板），mm.1–8', OSQ % '`sq7294793.mxl`', 'CC0-1.0'),
        ('`mozart-k421-ii-mm36-43`', K421_2, 'Andante（西西里行板），mm.36–43', OSQ % '`sq7294793.mxl`', 'CC0-1.0'),
    ],
    'techniques/structure/schubert-d810-variation-movement': [
        ('`schubert-d810-ii-mm1-8`', D810T, 'Andante con moto，mm.1–8', OSQ % '`sq7397765.mxl`', 'CC0-1.0'),
        ('`schubert-d810-ii-mm49-56`', D810T, 'Andante con moto，mm.49–56', OSQ % '`sq7397765.mxl`', 'CC0-1.0'),
        ('`schubert-d810-ii-mm73-80`', D810T, 'Andante con moto，mm.73–80', OSQ % '`sq7397765.mxl`', 'CC0-1.0'),
        ('`schubert-d810-ii-mm97-104`', D810T, 'Andante con moto，mm.97–104', OSQ % '`sq7397765.mxl`', 'CC0-1.0'),
    ],
    'techniques/sound/brahms-string-quartet-chorale-texture': [
        ('`brahms-op51no1-i-mm11-18`', BR1, 'Allegro，mm.11–18', OSQ % '`sq7108150.mxl`', 'CC0-1.0'),
        ('`brahms-op51no1-i-mm35-42`', BR1, 'Allegro，mm.35–42', OSQ % '`sq7108150.mxl`', 'CC0-1.0'),
        ('`brahms-op51no1-iv-mm1-12`', BR4, 'Allegro，mm.1–12（源文件连续编号 145–156）', OSQ % '`sq7108150.mxl`', 'CC0-1.0'),
        ('`brahms-op51no1-iv-mm71-80`', BR4, 'Allegro，mm.71–80（源文件连续编号 215–224）', OSQ % '`sq7108150.mxl`', 'CC0-1.0'),
    ],
}


def rewrite(path, rows):
    with open(path, encoding='utf-8') as f:
        lines = f.read().split('\n')
    try:
        h = next(i for i, ln in enumerate(lines) if ln.strip() == '## 谱例')
    except StopIteration:
        raise SystemExit('no 谱例 section in ' + path)
    i = h + 1
    while i < len(lines) and not lines[i].startswith('|'):
        i += 1
    if i + 1 >= len(lines):
        raise SystemExit('no table in ' + path)
    header, sep = lines[i], lines[i + 1]
    j = i + 2
    while j < len(lines) and lines[j].startswith('|'):
        j += 1
    new = [header, sep] + ['| %s | %s | %s | %s | %s |' % row for row in rows]
    lines[i:j] = new
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))
    print('rewrote', os.path.relpath(path, ROOT))


if __name__ == '__main__':
    for slug, rows in ROWS.items():
        rewrite(os.path.join(PROV, slug + '.md'), rows)
