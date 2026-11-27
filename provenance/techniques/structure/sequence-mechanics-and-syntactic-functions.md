# 模进与句法

- 文章：`content/techniques/structure/sequence-mechanics-and-syntactic-functions.md`
- 许可：待确认（详见两表）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| Open Music Theory (OMT) | v1 legacy source，章节 "Harmonic syntax - prolongation"、"Sonata form – development"、"Galant Schemata – continuation patterns" 与 "Sonata Theory – modules" | 模进模型（Model）与移位（Copy）机制、D2/A2 分类、展开部核心行动区（CAZ）模进驱动、Fonte/Monte 模式及过渡段模进功能的理论依据 |
| Humdrum 贝多芬奏鸣曲库 | `beethoven-piano-sonatas-main/kern/sonata01-1.krn`（Beethoven Piano Sonata No. 1 in F minor, Op. 2 No. 1） | 第一乐章展开部 mm. 49–80 结构性模进（大模型跨调移位、副题动机上移二度、连续碎裂与属音驻留制动）声部实据核验 |
| Humdrum 莫扎特奏鸣曲库 | `0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc`（Derived from sonata15-1.krn） | 第一乐章展开部 mm. 29–42 模进直接替代真正展开（g 小调至 d 小调模型移位、下行二度 D2 低音链与下属调再现标点）声部实据核验 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `beethoven-op2no1-i-mm49-80` | 贝多芬《F小调第1钢琴奏鸣曲》Op. 2 No. 1 第一乐章 | Allegro，展开部 mm. 49–80 | 据 CCARH MuseData 转写（`beethoven-piano-sonatas-main/kern/sonata01-1.krn`）；底本 \*MM240 为四分音符值，谱表为 2/2，故记 2 = 120 | 学术用途（CCARH 2002–2005，非 CC0） |
| `mozart-k545-i-mm29-42` | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 | Allegro，展开部 mm. 29–42（4/4） | CCARH Humdrum Kern（`sonata15-1.krn` → hum2abc 转出的 ABC，`local/resources/scores/source-packages/humdrum/mozart-sonatas/0061-…mvmt. 1.abc`）；排版为本项目自编码 LilyPond 摘录；音高多重集已与 DCMLab《莫扎特钢琴奏鸣曲》语料 `notes/K545-1.notes.tsv`（MS3 转录） 逐小节回比对一致 | 据 CCARH 转写，学术用途（非 CC0） |
