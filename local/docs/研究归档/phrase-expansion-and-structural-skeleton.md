# 研究归档：单乐句内部扩展与结构骨架判定

- **短标题**：乐句扩展
- **对应正文**：`content/techniques/structure/phrase-expansion-and-structural-skeleton.md`
- **出处记录**：`provenance/techniques/structure/phrase-expansion-and-structural-skeleton.md`
- **当前状态**：已成稿，待本批复读
- **学者署名**：scholar-a4
- **关联合约**：S105（task-40）

---

## 1. 核心论点与研究问题

- **中心问题**：古典句法如何通过内部扩展（internal expansion）、终止回避与模进追加把 4/8 小节乐句拉长，同时保持可还原的骨架；如何严格区分“内部扩展”与“开启新乐句”？
- **核心理论发现**：
  1. **结构时空拓扑**：严格区分外部扩展（Prefix 与 Suffix/Codetta/属音驻留，发生在乐句边界之外）与内部扩展（植入在基本乐念、延续句或终止冲刺内部）；
  2. **三重内部扩展机制**：
     - **乐节插值（Sub-phrase Interpolation）**：在基本乐念内部插入动机回声，拉长起步单元（如莫扎特 K. 494 前乐句 m. 3 对 m. 2 的回声重复）；
     - **延续部模进追加（Sequential Expansion in Continuation）**：通过模进梯级与和声延留（Prolongation），将前属和弦或属和弦向终止式冲刺的跑道大幅拉长；
     - **终止回避/弱化与 OMT 机制（Evaded Cadence / IAC & One More Time）**：预期 PAC 在着陆点落空或弱化为 IAC，引发延续句变奏重跑（如贝多芬 Op. 2 No. 3 第一乐章主部拉伸至 13 小节，莫扎特 K. 309 第三乐章后继句拉伸至 11 小节）；
  3. **“内部扩展”与“开启新乐句”的三重判定准则**：
     - **终极终止目标的唯一性**：整个扩展段落内部无任何合法独立的结构终止式，所有动能完全收束于同一个未竟终极目标；
     - **句法起动功能的缺失**：拉伸段仅重述延续/终止材料，绝无新的基本乐念（basic idea）呈示，和声陈述不具备乐句起步功能；
     - **罗斯坦的重构还原测试（Rothstein's Recomposition Test）**：剪除插值与 OMT 循环后，乐句可无缝还原为严整自然的 4/8 小节标准原型（Basic Phrase）；
  4. **理论反例对照**：内生非标准长度（Inherent Irregularity，如莫扎特 K. 515 开篇 5 小节复合基本乐念）不可剔除还原，与人为施加的内部扩展截然不同。

---

## 2. 正文与索引位置

- **正文文件**：`content/techniques/structure/phrase-expansion-and-structural-skeleton.md`（短标题：乐句扩展）
- **来源与许可**：`provenance/techniques/structure/phrase-expansion-and-structural-skeleton.md`

---

## 3. 谱例状态与案例核验

1. **莫扎特：F大调回旋曲 K. 494，Allegretto，mm. 1–6**
   - 证明：乐节内部插值与动机回声扩展（Sub-phrase interpolation by motivic echo）；
   - 谱面核验：第 1–2 小节呈示 2 小节基本乐念，第 3 小节弱拍琶音以回声形态完整复述第 2 小节，导致 basic idea 扩展至 3 小节，随后第 4–6 小节为 3 小节对比乐念并收束于半终止；剔除第 3 小节可严丝合缝还原为标准 4 小节（2+2）前乐句；
   - 底本来源：本地 OMT 谱例与核验语料；
   - 状态：**规范单行文本占位**。
2. **贝多芬：C大调第3钢琴奏鸣曲 Op. 2 No. 3，第 1 乐章 Allegro con brio，mm. 1–13**
   - 证明：8 小节标准乐句因终止弱化（IAC）与低音连接句引发延续部变奏重跑（拉长至 13 小节 PAC 闭合）；
   - 谱面核验：
     - mm. 1–4：C 大调主和弦呈示 2 小节基本乐念，属和弦 2 小节移位复述；
     - mm. 5–8：延续句启动，动机碎裂为 1 小节，低音驱动引向 m. 8 终止式；
     - m. 8：低音落在 C，旋律落在三音 E 弱化为 IAC；左手后半拍出现下行六连音连接线条（`c–g–f#–fn–e–d`）重新激活延续部；
     - mm. 9–13：延续部变奏重跑，左手移位、减七加压、强奏阻尼，直至第 13 小节拍头在 ff 齐奏中达成真正的 PAC，净扩展 5 个小节；
   - 底本来源：本地 Humdrum 贝多芬奏鸣曲库 `beethoven-piano-sonatas-main/kern/sonata03-1.krn`；
   - 状态：**规范单行文本占位**。
3. **莫扎特：C大调第7钢琴奏鸣曲 K. 309，第 3 乐章 Allegretto grazioso，mm. 9–19**
   - 证明：大后继句在第 15–16 小节遭遇终止回避（Evaded Cadence），通过 OMT 变奏重跑拉伸至 11 小节 PAC 闭合；
   - 谱面核验：
     - mm. 9–12：复合基本乐念 4 小节；
     - mm. 13–15：初次延续与终止冲刺；
     - mm. 15–16：高声部导音 B 颤音大跳至 A5，低音拒绝落稳原位主和弦，PAC 被彻底抹消；
     - mm. 16–19：启动 OMT 机制，以更华丽加花重跑 mm. 13–15 并于第 19 小节强力达成 PAC，净扩展 3 小节；
   - 底本来源：本地 Humdrum 莫扎特奏鸣曲库 `0033-33-Piano Sonata No. 7 in C major, K 309 (284b), mvmt. 3.abc`；
   - 状态：**规范单行文本占位**。

---

## 4. 理论脉络与主要文献依据

- **William Rothstein**：《调性音乐中的乐句节奏》（*Phrase Rhythm in Tonal Music*, 1989），第三章 "Techniques of Phrase Expansion"；
- **William Caplin**：《古典曲式》（*Classical Form*, 1998），外部扩展与内部扩展、基本乐念与延续功能界定；
- **Janet Schmalfeldt**：《变成为过程》（*In the Process of Becoming*, 2011），"One More Time"（OMT）三阶段句法动力学模型；
- **Open Music Theory (OMT)**：
  - `internalExpansions.md`：乐节插值、乐句扩展、重构还原测试与非标准长度对比；
  - `externalExpansions.md`：前缀（Prefix）与后缀（Suffix / Codetta / Standing on the dominant）；
  - `thematicStructureInTheClassicalStyle.md`：古典风格主题结构总论；
- **与首批 20 篇的关系与边界**：
  - 与《终止式延后》（专论终止式本身的规避力学）和《复合乐段》（专论宏观 16 小节双层嵌套）严格区分；
  - 正文中精准关联 short title 链接：`[《终止式延后》](cadential-evasion-and-temporal-expansion.md)`、`[《复合乐段》](compound-period-hierarchical-syntax.md)`、`[《模进与句法》](sequence-mechanics-and-syntactic-functions.md)`。

---

## 5. 未解决的缺口与可接受的局限

- **当前缺口**：正文谱例按规范采用单行文本占位，待后续批次统一排版；
- **局限**：本文聚焦于维也纳古典乐派钢琴与室内乐核心乐句，未深入涉及 19 世纪晚期浪漫主义交响乐中极度松散、无调性骨架的连环瓦解现象。
