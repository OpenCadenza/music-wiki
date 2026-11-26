# 独奏与乐队对话

- 文章：`content/techniques/sound/mozart-concerto-solo-orchestra-dialogue.md`
- 许可：CCARH MuseData 学术用途（非 CC0；详见两表）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| W. A. Mozart (1785) | C 大调第 21 钢琴协奏曲 K.467 第二乐章总谱机器可读事实 | CCARH MuseData `k467-mvt2.md2`（全曲 13 声部 104 小节，包括长笛、双簧管 1/2、大管 1/2、圆号 1/2、钢琴、小提琴 1/2、中提琴、大提琴、低音提琴逐小节和声与配器核验） |
| Neue Mozart-Ausgabe (NMA) | Bärenreiter-Verlag, Series V, Work Group 15, Concerto Vol. 5 (1959) | 弱音器使用（*con sordini*）、大提琴与低音提琴纯拨奏（*pizzicato*）、木管长音与动力学记号（*sfp*）实证校订 |
| Donald Francis Tovey | *Essays in Musical Analysis, Vol. 3: Concertos* (Oxford University Press, 1936) | 协奏曲慢板乐章中独奏声部与管弦乐队对位对话与织体分层理论分析 |
| Charles Rosen | *The Classical Style: Haydn, Mozart, Beethoven* (The Viking Press, 1971), Chapter on Mozart Concertos | 莫扎特协奏曲慢板乐章中弱音弦乐三连音律动、独奏如歌主体与木管色彩对话动力学解析 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `mozart-k467-ii-mm1-8` | 莫扎特《C大调第21钢琴协奏曲》K.467 第二乐章 | Andante，mm. 1–8（长笛、双簧管 I、大管 I、第一/第二小提琴、中提琴、大提琴） | CCARH MuseData `k467-mvt2.md2`（Neue Mozart-Ausgabe 转录） | 据 CCARH MuseData 转写，学术用途；非 CC0 |
| `mozart-k467-ii-mm23-30` | 莫扎特《C大调第21钢琴协奏曲》K.467 第二乐章 | Andante，mm. 23–30（钢琴右手/左手、第二小提琴、中提琴、大提琴） | CCARH MuseData `k467-mvt2.md2`（Neue Mozart-Ausgabe 转录） | 据 CCARH MuseData 转写，学术用途；非 CC0 |
| `mozart-k467-ii-mm66-71` | 莫扎特《C大调第21钢琴协奏曲》K.467 第二乐章 | Andante，mm. 66–71（长笛、双簧管 I、第一/第二小提琴、钢琴右手/左手） | CCARH MuseData `k467-mvt2.md2`（Neue Mozart-Ausgabe 转录） | 据 CCARH MuseData 转写，学术用途；非 CC0 |
| `mozart-k467-ii-mm82-88` | 莫扎特《C大调第21钢琴协奏曲》K.467 第二乐章 | Andante，mm. 82–88（第一/第二小提琴、钢琴右手/左手、大提琴） | CCARH MuseData `k467-mvt2.md2`（Neue Mozart-Ausgabe 转录） | 据 CCARH MuseData 转写，学术用途；非 CC0 |

出谱与核对记录（2026-11-27，score-d）：

- 四块围栏由 md2 逐小节取音高与时长后自编码 LilyPond；`verify_pitch.py` 音高多重集核对全部一致，LilyPond barcheck 每小节时值合计无误（0 warning）。
- 钢琴左手双声部（持续音 + 三连音/八分音型）按 `<< { … } \\ { … } >>` 分声部记谱；中提琴双音在 mm.1–8 合并为单谱表内外声部。
- 试听速度 4=76 为编选值（原谱无节拍机标记），代码注释已注明。
- 底本副本：`local/origin_resources/sources/ccarh-musedata-concertos/`；可读副本 `local/resources/scores/source-packages/mozart-k467-op61-musedata/`。
- 未取得 MusicXML 的原因见同目录 `Provenance`/上文（IMSLP bot-check、PDMX 仅元数据、OpenScore 无协奏曲、MuseData 源站 WAF 拦截）。
- 正文按底本微调一处：mm.23 起第一小提琴并未完全沉默，而是退居均匀八分音符音型；第二小提琴与中提琴在独奏段以八分音符（而非三连音）延续背景律动。
