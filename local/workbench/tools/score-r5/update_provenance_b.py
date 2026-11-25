# -*- coding: utf-8 -*-
"""更新 B 组各篇 provenance 的「谱例」表（score-b）。"""

NOTE = ("\n> 谱例均由本项目从 MusicXML 逐音转写为 LilyPond（自写转换器 `local/workbench/scores/score-b/tools/mxl2ly.py`），"
        "八度映射经 MIDI 实测校准（`c'` = 中央 C）。只截取论证所需片段，不构成完整乐谱的再分发。\n")

TABLES = {}

TABLES[r"provenance\ensembles\voice-viola-and-piano.md"] = """## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `brahms-op91no1-mm1-13` | 勃拉姆斯《两首歌曲》Op. 91 No. 1 | Adagio espressivo，mm.1–13（含弱起小节） | OpenScore Lieder MXL `op91-1-Gestillte-Sehnsucht.mxl` | CC0-1.0 / 公有领域 |
| `brahms-op91no1-mm14-25` | 勃拉姆斯《两首歌曲》Op. 91 No. 1 | Adagio espressivo，mm.14–25 | 同上 | CC0-1.0 / 公有领域 |
| `brahms-op91no2-mm1-10` | 勃拉姆斯《两首歌曲》Op. 91 No. 2 | Andante con moto，mm.1–10 | OpenScore Lieder MXL `op91-2-Geistliches-Wiegenlied.mxl` | CC0-1.0 / 公有领域 |
| `brahms-op91no2-mm26-46` | 勃拉姆斯《两首歌曲》Op. 91 No. 2 | Andante con moto，mm.26–46 | 同上 | CC0-1.0 / 公有领域 |
"""

TABLES[r"provenance\techniques\structure\autobiographical-narrative-and-quartet-form.md"] = """## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `smetana-sq1-i-mm1-16` | 斯美塔那《E 小调第一弦乐四重奏“我的一生”》第一乐章 | Allegro vivo appassionato，mm.1–16 | OpenScore StringQuartets MXL `smetana-sq1-from-my-life.mxl` | CC0-1.0 / 公有领域 |
| `smetana-sq1-i-mm31-46` | 同上 第一乐章 | Allegro vivo appassionato，mm.31–46 | 同上 | CC0-1.0 / 公有领域 |
| `smetana-sq1-iv-mm1-24` | 同上 第四乐章 | Vivace，mm.1–24 | 同上 | CC0-1.0 / 公有领域 |
| `smetana-sq1-iv-mm25-49` | 同上 第四乐章 | Vivace，mm.25–49 | 同上 | CC0-1.0 / 公有领域 |

> 底本细节：正文称 mm.1–16 的背景震音为「附点十六分音符」，OpenScore 底本记为一梁八分音符震音（`<tremolo>1</tremolo>`）；谱例按底本出谱，两处口径差异留待正文复核。
"""

TABLES[r"provenance\techniques\rhythm\folk-idiom-and-rhythmic-vitality.md"] = """## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `dvorak-op96-i-mm1-16` | 德沃夏克《F 大调第 12 弦乐四重奏“美国”》Op. 96 第一乐章 | Allegro ma non troppo，mm.1–16 | OpenScore StringQuartets MXL `dvorak-op96-american.mxl` | CC0-1.0 / 公有领域 |
| `dvorak-op96-i-mm44-52` | 同上 第一乐章 | Allegro ma non troppo，mm.44–52 | 同上 | CC0-1.0 / 公有领域 |
| `dvorak-op96-iii-mm1-28` | 同上 第三乐章 | Molto vivace，mm.1–28 | 同上 | CC0-1.0 / 公有领域 |
| `dvorak-op96-iii-mm49-60` | 同上 第三乐章 | Poco meno mosso，mm.49–60 | 同上 | CC0-1.0 / 公有领域 |

> 底本细节：第一乐章 mm.2–5 的第一小提琴与 mm.7–14 的中提琴在底本中以两音震音记谱（MuseScore `<tremolo type="start">` 成对，`actual-notes=2`），谱例按 `\\repeat tremolo` 还原为两音震音。
"""

TABLES[r"provenance\techniques\sound\debussy-vocal-planes-of-tone.md"] = """## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `debussy-ariettes2-mm1-17` | 德彪西《被遗忘的抒情调》No. 2《泪洒我心》 | mm.1–17 | OpenScore Lieder MXL `ariettes-2-Il-pleure.mxl` | CC0-1.0 / 公有领域 |
| `debussy-ariettes2-mm47-56` | 同上 No. 2 | mm.47–56 | 同上 | CC0-1.0 / 公有领域 |
| `debussy-ariettes4-mm1-16` | 德彪西《被遗忘的抒情调》No. 4《木马》 | mm.1–16 | OpenScore Lieder MXL `ariettes-4-Paysages-belges.mxl` | CC0-1.0 / 公有领域 |
| `debussy-ariettes4-mm78-90` | 同上 No. 4 | mm.78–90 | 同上 | CC0-1.0 / 公有领域 |
"""

TABLES[r"provenance\techniques\structure\romantic-song-cycle-macrostructure.md"] = """## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `schumann-op48no1-mm1-13` | 舒曼《诗人之恋》Op. 48 No. 1 | Langsam, zart，mm.1–13 | OpenScore Lieder MXL `op48-01_Im_wunderschönen_Monat_Mai.mxl` | CC0-1.0 / 公有领域 |
| `schumann-op48no1-mm23-26` | 同上 No. 1 | mm.23–26（末小节停在升 C 属七，不解决） | 同上 | CC0-1.0 / 公有领域 |
| `schumann-op48no8-mm31-38` | 舒曼《诗人之恋》Op. 48 No. 8 | mm.31–38 | OpenScore Lieder MXL `op48-08_Und_wüssten-s_die_Blumen.mxl` | CC0-1.0 / 公有领域 |
| `schumann-op48no12-mm20-30` | 舒曼《诗人之恋》Op. 48 No. 12 | mm.20–30（钢琴后奏） | OpenScore Lieder MXL `op48-12_Am_leuchtenden_Sommermorgen.mxl` | CC0-1.0 / 公有领域 |
| `schumann-op48no16-mm52-67` | 舒曼《诗人之恋》Op. 48 No. 16 | mm.52–67 | OpenScore Lieder MXL `op48-16_Die_alten-_bösen_Lieder.mxl` | CC0-1.0 / 公有领域 |

> 底本细节：No. 1 与 No. 8 的 MXL 把弱起小节编号为 m.0，本表与谱例一律按**印刷小节号**（弱起＝m.1）标注。
"""

TABLES[r"provenance\ensembles\orchestra-to-string-quartet-reduction.md"] = """## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `haydn-op51-intro-mm1-4` | 海顿《十字架上的临终七言》Op. 51 引子 | Maestoso ed Adagio，mm.1–4 | OpenScore StringQuartets MXL `haydn-op51-seven-last-words.mxl` | CC0-1.0 / 公有领域 |
| `haydn-op51-intro-mm5-8` | 同上 引子 | Maestoso ed Adagio，mm.5–8 | 同上 | CC0-1.0 / 公有领域 |
| `haydn-op51-sonata1-mm1-6` | 同上 第 1 首奏鸣曲 | Largo，mm.1–6 | 同上 | CC0-1.0 / 公有领域 |
| `haydn-op51-sonata1-mm37-44` | 同上 第 1 首奏鸣曲 | Largo，mm.37–44 | 同上 | CC0-1.0 / 公有领域 |
"""

TABLES[r"provenance\notation\articulation-marks-and-realization.md"] = """## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `beethoven-op18no1-i-mm1-4` | 贝多芬《F 大调第一弦乐四重奏》Op. 18 No. 1 第一乐章 | Allegro con brio，mm.1–4 | OpenScore StringQuartets MXL `String_Quartet_No.1,_Op.18_No.1` | CC0-1.0 / 公有领域 |
| 占位（未出谱） | 贝多芬《F 大调第七弦乐四重奏》Op. 59 No. 1 第一乐章 | mm.1–8、mm.18–24 | 本地 CCARH MuseData kern `quartet07-1.krn`（仅核对，未转写） | 公有领域（据 CCARH MuseData 转写，学术用途） |
| `beethoven-op135-iii-mm1-12`（关联引用） | 贝多芬《F 大调第十六弦乐四重奏》Op. 135 第三乐章 | Lento assai, cantante e tranquillo，mm.1–12 | 已有编译谱例，见 `content/ensembles/string-quartet-acoustic-role-differentiation.md` | 公有领域（据 CCARH MuseData 转写，学术用途） |
"""

TABLES[r"provenance\notation\transposing-instruments-notation-and-sounding-pitch.md"] = """## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `mozart-k550-i-mm18-20-horns` | 莫扎特《g 小调第四十交响曲》K.550 第一乐章（两支圆号，写记谱音） | Molto allegro，mm.18–20 | OpenScore K.550 第一乐章 MusicXML 转写体（`k550-i-openscore-raw.musicxml`，Part 6 `Corno in B.` / Part 7 `Corno in G.`）；与 CCARH MuseData md2 `k550-mvt1.md2` 逐音对照一致 | 公有领域；OpenScore 转写体许可待确认（未写 CC0） |
| `beethoven-op92-ii-mm1-10`（关联引用） | 贝多芬《A 大调第七交响曲》Op. 92 第二乐章 | mm.1–10 | 关联 `content/techniques/sound/timbral-contrast-and-formal-articulation.md` 已编译谱例 | 公有领域 / Mutopia 转写 |
| 占位（未出谱） | 贝多芬《C 大调第一交响曲》Op. 21 第二乐章 | mm.1–15 | 本地 CCARH MuseData md2 `beethoven-op21-ii-sym1.md2`（Part 3 `Clarinetti 1, 2 in C`）；本轮只完成声部核对，未转写为 LilyPond | 公有领域（据 CCARH MuseData 转写，学术用途） |

> K.550 一段：本谱例只出两支圆号（`\\transposition bf` / `\\transposition g`，写记谱音），用于「记谱音 ↔ 实音」对照；同一段落在总谱全奏中的完整语境见 `content/techniques/sound/mozart-k550-syntax-and-orchestration.md` 的 `mozart-k550-i-mm16-24` 块。
"""


def main():
    for path, table in TABLES.items():
        text = open(path, encoding="utf-8").read()
        idx = text.find("## 谱例")
        if idx < 0:
            print("SKIP no section:", path)
            continue
        head = text[:idx]
        new = head + table
        if "> 谱例均由本项目" not in head and "> 谱例均由本项目" not in table:
            new = new.rstrip("\n") + "\n" + NOTE
        open(path, "w", encoding="utf-8", newline="\n").write(new)
        print("OK", path)


if __name__ == "__main__":
    main()
