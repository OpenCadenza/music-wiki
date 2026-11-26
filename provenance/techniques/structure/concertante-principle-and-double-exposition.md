# 协奏原则

- 文章：`content/techniques/structure/concertante-principle-and-double-exposition.md`
- 许可：CCARH MuseData 学术用途（非 CC0；详见两表）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| W. A. Mozart (1785) | C 大调第 21 钢琴协奏曲 K.467 第一乐章总谱机器可读事实 | CCARH MuseData `k467-mvt1.md2`（16 声部，逐小节核验 mm. 1–74 乐队呈示部五段式利都奈罗、mm. 74–90 钢琴独立华彩引子 Eingang 与持续长颤音、mm. 91–140 主部接管与离调） |
| Ludwig van Beethoven (1806) | D 大调小提琴协奏曲 Op. 61 第一乐章总谱机器可读事实 | CCARH MuseData `op61-mvt1.md2`（13 声部，逐小节核验 mm. 1–89 乐队利都奈罗定音鼓节奏动机、木管四部赞美诗、m. 10 第一小提琴 D# 突变异化、mm. 89–100 独奏小提琴分解八度飞跃切入） |
| James Hepokoski & Warren Darcy | *Elements of Sonata Theory* (Oxford University Press, 2006), Chapter 19 "Type 5 Sonata: The Concerto" | 第五类奏鸣曲式理论、双重呈示部（R1/S1）调性自足性与独奏离调、EEC 概念支撑 |
| Donald Francis Tovey | *Essays in Musical Analysis, Vol. 3: Concertos* (Oxford University Press, 1936) | 协奏原则中全奏体制性陈述与独奏个体戏剧性对话关系论述 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `mozart-k467-i-mm1-8` | 莫扎特《C 大调第二十一钢琴协奏曲》K.467 第一乐章 | Allegro maestoso，mm. 1–8（定音鼓、双簧管 I/II、大管 I、圆号 I、小号 I、第一小提琴、大提琴/低音提琴） | CCARH MuseData `k467-mvt1.md2`（Neue Mozart-Ausgabe 转录） | 据 CCARH MuseData 转写，学术用途；非 CC0 |
| `mozart-k467-i-mm74-91` | 莫扎特《C 大调第二十一钢琴协奏曲》K.467 第一乐章 | Allegro maestoso，mm. 74–91（独奏钢琴右手/左手；m. 80–83 长颤音按原谱 tr 记号标记） | CCARH MuseData `k467-mvt1.md2`（Neue Mozart-Ausgabe 转录） | 据 CCARH MuseData 转写，学术用途；非 CC0 |
| `beethoven-op61-i-mm1-18` | 贝多芬《D 大调小提琴协奏曲》Op. 61 第一乐章 | Allegro ma non troppo，mm. 1–18（定音鼓、双簧管 I、大管 I、第一/第二小提琴、中提琴、大提琴） | CCARH MuseData `op61-mvt1.md2`（Breitkopf & Haertel 全集，Fran Bennion 1996/2002） | 据 CCARH MuseData 转写，学术用途；非 CC0 |

出谱与核对记录（2026-11-27，score-d）：

- 三块围栏均由 md2 逐小节取音高与时长后自编码 LilyPond，不用 md2 原文；`verify_pitch.py` 对每块做音高多重集核对，全部一致；LilyPond barcheck 每小节时值合计无误（0 warning）。
- 底本副本与取得信息：`local/origin_resources/sources/ccarh-musedata-concertos/`；可读副本 `local/resources/scores/source-packages/mozart-k467-op61-musedata/`。
- 试听速度 4=120 为编选值（原谱无节拍机标记），代码注释已注明，不冒充作曲家标记。
- 未取得 MusicXML：IMSLP 文件页与 `/images/` 直链返回 bot-check；PDMX 固定包仅含元数据（MusicXML 在 1.9GB 的 `mxl.tar.gz`，未整包下载）；OpenScore 只有 StringQuartets 与 Lieder；Mutopia 无协奏曲；bitbucket 的 MuseData 现由 WAF 拦截（405 + 人机验证）。
- 正文与底本冲突按底本修正：第一小提琴 m.1 音型为 C4–G3–C4–E4（原写 c1–e1–c1）；管乐号角在 mm.7–8、动机为 C–C–C–D 与 E–F–E–D（原写 mm.5–8、g1–g1–g1–c2）；独奏引子起于 m.74 第 1 拍（原写第 2 拍）。
