# 民族语汇与节奏

- 文章：`content/techniques/rhythm/folk-idiom-and-rhythmic-vitality.md`
- 许可：CC0（详见两表）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| OpenScore String Quartets 语料库 | `local/workbench/scores/score-r3/downloads/dvorak-op96/dvorak-op96-american.mxl` | 德沃夏克《F大调第12弦乐四重奏“美国”》Op. 96 第一乐章 mm. 1–52（风笛织体、中提琴五声第一主题、苏格兰切分、持续低音、第 44 小节五声第二主题）与第三乐章全 196 小节（3/4 拍 Molto vivace，双重三部曲式，mm. 1–28 诙谐跳跃与高音区绯红唐纳雀鸟鸣点彩、mm. 49–60 F 小调 Trio 主题时值扩增与哀歌沉思变形）的机器可读 MusicXML 底本实证 |
| 德沃夏克书信与斯皮尔维尔创作档案 | 1893 年爱荷华州斯皮尔维尔创作记录与北美林间鸟鸣临摹研究 | 德沃夏克吸收美洲黑人灵歌、原住民音乐与波希米亚本土民族民间音乐语汇、记录北美绯红唐纳雀鸣叫并注入四重奏织体的文献背景支持 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `dvorak-op96-i-mm1-16` | 德沃夏克《F 大调第 12 弦乐四重奏“美国”》Op. 96 第一乐章 | Allegro ma non troppo，mm.1–16 | OpenScore StringQuartets MXL `dvorak-op96-american.mxl` | CC0-1.0 / 公有领域 |
| `dvorak-op96-i-mm44-52` | 同上 第一乐章 | Allegro ma non troppo，mm.44–52 | 同上 | CC0-1.0 / 公有领域 |
| `dvorak-op96-iii-mm1-28` | 同上 第三乐章 | Molto vivace，mm.1–28 | 同上 | CC0-1.0 / 公有领域 |
| `dvorak-op96-iii-mm49-60` | 同上 第三乐章 | Poco meno mosso，mm.49–60 | 同上 | CC0-1.0 / 公有领域 |

> 底本细节：第一乐章 mm.2–5 的第一小提琴与 mm.7–14 的中提琴在底本中以两音震音记谱（MuseScore `<tremolo type="start">` 成对，`actual-notes=2`），谱例按 `\repeat tremolo` 还原为两音震音。

> 谱例均由本项目从 MusicXML 逐音转写为 LilyPond（自写转换器 `local/workbench/scores/score-b/tools/mxl2ly.py`），八度映射经 MIDI 实测校准（`c'` = 中央 C）。只截取论证所需片段，不构成完整乐谱的再分发。
