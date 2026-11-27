# 和声节奏

- 文章：`content/techniques/harmony/harmonic-rhythm-and-syntactic-pacing.md`
- 许可：待确认（详见两表）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| Open Music Theory (OMT) | v1 legacy source，章节 "The sentence" (sentence.md)、"Harmonic syntax - the idealized phrase" (harmonicSyntax1.md)、"Harmonic syntax - prolongation" (harmonicSyntax2.md) 与 "Thematic Function" (themeFunctions.md) | 和声节奏（Harmonic Rhythm）与表面节奏/超拍的解耦定义、延续句五大特征中和声加速（Harmonic Acceleration）的理论界定、主功能延留与终止功能和声密度压缩机制 |
| William Caplin | *Classical Form* (1998), Chapter 1 "A Formal Hierarchy" & Chapter 2 "The Sentence"; *Analyzing Classical Form* (2013) | 句型呈示句到延续句的和声加速阶梯（2小节→1小节→半小节）、属音驻留（Standing on the Dominant / 和声减速制动）的曲式与心理力学理论依据 |
| Humdrum 贝多芬奏鸣曲库 | `beethoven-piano-sonatas-main/kern/sonata01-1.krn`（Beethoven Piano Sonata No. 1 in F minor, Op. 2 No. 1） | 第一乐章 mm. 1–8 曼海姆火箭呈示句与延续句指数级和声加速逐小节实据核验（m. 7 前两拍 $i^6$，第 4 拍击出 $ii^{\circ 6}$；m. 8 第 2 拍落属和弦，第 3 拍休止符延长记号达成 HC）；展开部再现准备段 mm. 81–101 属音持续音（C2 与 C3 交替）踏板驻留制动与叹息融解逐小节实据核验 |
| Humdrum 莫扎特奏鸣曲库 | `0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc`（Derived from sonata15-1.krn） | 第一乐章 mm. 1–4 阿尔贝蒂低音快速表面节奏与主功能宽广和声节奏解耦、mm. 5–8 延续句逐小节和声更迭、mm. 9–14 过渡段半小节和声加速冲刺内聚裂隙逐小节实据核验 |
| Humdrum 莫扎特奏鸣曲库 | `0013-13-Piano Sonata No. 5 in G major, K 283 (189h), mvmt. 1.abc`（Derived from sonata05-1.krn） | 第一乐章 mm. 1–10 句型基本乐思双重邻音和弦延留、mm. 5–6 模进断片与 mm. 7–8 赫米奥拉和声加速至 PAC（终止图式收束）逐小节实据核验 |
| Humdrum 莫扎特奏鸣曲库 | `0052-52-Piano Sonata No. 12 in F major, K 332 (300k), mvmt. 1.abc`（Derived from sonata12-1.krn） | 第一乐章 mm. 1–12 歌唱性主部慢和声节奏（mm. 1–4 每小节更迭一次）、mm. 13–22 号角小步舞曲织体 vs. mm. 23–40 D 小调狂飙风格过渡段爆发（表面十六分音符与模进和声密集加速对撞）逐小节实据核验 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `beethoven-op2no1-i-mm1-8` | 贝多芬《F小调第1钢琴奏鸣曲》Op. 2 No. 1 第一乐章 | Allegro，弱起 + mm. 1–8 | 据 CCARH MuseData 转写（`beethoven-piano-sonatas-main/kern/sonata01-1.krn`）；底本 \*MM240 为四分音符值，2/2 谱表记 2 = 120；开头 1 拍弱起（c′）以 `\partial 4` 保留 | 学术用途（CCARH 2002–2005，非 CC0） |
| `mozart-k545-i-mm1-14` | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 | Allegro，mm. 1–14（表面节奏与和声节奏解耦：mm. 1–4 十六分音符阿尔贝蒂低音 vs. 近静止的主功能，mm. 5–8 以 1 小节为步长更迭，mm. 9–14 提速到半小节一换并在 m. 12 撞半终止） | CCARH Humdrum Kern（`sonata15-1.krn` → hum2abc 转出的 ABC，`local/resources/scores/source-packages/humdrum/mozart-sonatas/0061-…mvmt. 1.abc`）；音高多重集已与 DCMLab 莫扎特奏鸣曲语料 `notes/K545-1.notes.tsv` 逐小节回比对一致（mm. 1–14，230 音全对）；左手谱号按底本：mm. 1–4 高音谱号，m. 5 末拍起换低音谱号 | 据 CCARH 转写，学术用途（非 CC0）；DCMLab 语料（CC BY-NC-SA 4.0）仅作核对 |
| `mozart-k545-i-mm5-8`（关联引用） | 莫扎特《C大调第15钢琴奏鸣曲》K. 545 第一乐章 | Allegro，mm. 5–8 —— 与本篇 `mozart-k545-i-mm1-14` 的 mm. 5–8 **重叠 4 小节** | 该片段在《终止∫普林纳与结构收束》篇以 Prinner 原型单独出谱：`content/techniques/structure/cadential-prinner-and-structural-closure.md` | 同左 |
| `beethoven-op2no1-i-mm81-101` | 贝多芬《F小调第1钢琴奏鸣曲》Op. 2 No. 1 第一乐章 | Allegro，展开部末端 mm. 81–101 | 据 CCARH MuseData 转写（`beethoven-piano-sonatas-main/kern/sonata01-1.krn`）；属音持续音段底本记 C2 与 C3 交替的八分音符分解脉动，mm.93–94 为断奏四分音符 | 学术用途（CCARH 2002–2005，非 CC0） |

- **重叠说明**：`mozart-k545-i-mm1-14` 与本库既有的 `mozart-k545-i-mm5-8` 在 mm. 5–8 重叠。前者需要 mm. 1–4 的静止主功能作对照、才看得出「表面节奏 vs 和声节奏」的解耦与随后逐级加速，故按「同一作品不同片段、不同用途」各自保留，没有为对齐而复制整段，也没有改动后者。两块的 `id`、所在正文与用途不同，各自独立。
