# 研究归档：Prinner 图式的终止化变异与正格闭合机制

- **短标题**：终止图式
- **对应正文**：`content/techniques/structure/cadential-prinner-and-structural-closure.md`
- **出处记录**：`provenance/techniques/structure/cadential-prinner-and-structural-closure.md`
- **当前状态**：已成稿，待本批复读
- **学者署名**：scholar-a4
- **关联合约**：S103（task-27）

---

## 1. 核心论点与研究问题

- **中心问题**：加兰特 Prinner 图式如何通过低音变异与终止四六和弦插入转化为结构性正格终止？
- **核心理论发现**：
  1. **原型 Prinner 的非终止属性**：外声部 $\hat{6}-\hat{5}-\hat{4}-\hat{3}$ 与 $\hat{4}-\hat{3}-\hat{2}-\hat{1}$ 平行级进，Stage 3 低音为经过性 $\hat{2}$，缺乏原位属和弦（Root-position V）向原位主和弦（I）的根音跳进（$\hat{5} \to \hat{1}$）。在卡普林古典句法体系中，它纯粹承担“延续句（Continuation）”的动力展开功能，无法独立终结乐段；
  2. **终止化重构的三重工程**：
     - **低音变异（Bass Mutation）**：低音在走过 Stage 1–2 后，脱离级进轨道直接大跳至属音 $\hat{5}$，建立原位属和弦权威；
     - **终止四六和弦插入（Cadential 6/4 Insertion）**：低音落在属音时，强拍插入 $I^6_4$（即 $V^{6-5}_{4-3}$），将高音声部下行动能吸纳为四度与六度不协和挂留音，并在随后的属七和弦中释放解决；
     - **节拍重塑与强拍 PAC**：终止四六重音加压，下个小节强拍双手坚决落于原位主和弦（$\hat{5} \to \hat{1}$），高音由 $\hat{2}$ 级进落于主音 $\hat{1}$，达成完全正格终止（PAC）；
  3. **功能融合与紧缩（Functional Fusion & Compression）**：延续句的动机展开与终止单元的和声收束被压缩进同一个 4 小节图式内，实现紧凑高效的句法结构。

---

## 2. 正文与索引位置

- **正文文件**：`content/techniques/structure/cadential-prinner-and-structural-closure.md`（短标题：终止图式）
- **来源与许可**：`provenance/techniques/structure/cadential-prinner-and-structural-closure.md`

---

## 3. 谱例状态与案例核验

1. **莫扎特：C大调第15钢琴奏鸣曲 K. 545，第 1 乐章 Allegro，mm. 5–8**
   - 证明：原型 Prinner 作为纯粹延续句的典型实据；
   - 谱面核验：mm. 1–4 呈示句后，mm. 5–8 右手以连续十六分音符跑动冲出，首音由 A4（$\hat{6}$）、G4（$\hat{5}$）、F4（$\hat{4}$）下行至 E4（$\hat{3}$）；左手低音清晰级进 $F \to E \to D \to C$（$\hat{4}-\hat{3}-\hat{2}-\hat{1}$）。第 8 小节末尾无和声终止感，直接冲入第 9 小节副调过渡段；
   - 底本来源：本地 Humdrum mozart-sonatas 库 `0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc`；
   - 编制：钢琴双手；
   - 状态：**规范单行文本占位**。
2. **莫扎特：G大调第5钢琴奏鸣曲 K. 283 (189h)，第 1 乐章 Allegro，mm. 5–10**
   - 证明：终止化 Prinner（Cadential Prinner）实现完全正格终止的典范；
   - 谱面核验：mm. 5–6 右手核心音为 e2（$\hat{6}$）与 d2（$\hat{5}$），低音为 C（$\hat{4}$）与 B（$\hat{3}$）；mm. 7–8 十六分音符展开后，低音脱离 A 音（$\hat{2}$），在 m. 9 坚决跳向属音 D（$\hat{5}$，持续八分音符震音）；右手在强拍形成终止四六和弦延留（`fedc BdBG AcAF`）并解决至属七；m. 10 强拍双手坚决落于原位主和弦（高音 G4 即 $\hat{1}$，低音 $G_2$ 即 $\hat{1}$），达成完全正格终止（PAC）；
   - 底本来源：本地 Humdrum mozart-sonatas 库 `0013-13-Piano Sonata No. 5 in G major, K 283 (189h), mvmt. 1.abc`；
   - 编制：钢琴双手；
   - 状态：**规范单行文本占位**。
3. **莫扎特：A大调第11钢琴奏鸣曲 K. 331，第 1 乐章 Andante grazioso，mm. 1–8**
   - 证明：乐段前句原型 Prinner（弱半终止）与后句终止化 Prinner（强拍 PAC）的直接对称对照；
   - 谱面核验：前句 mm. 3–4 低音沿 $D \to C\sharp \to B \to A$ 级进，形成弱半终止；后句 mm. 7–8 低音跳入属音 E（$\hat{5}$），强拍插入终止四六并解决至属七，m. 8 强拍坚决落于原位主和弦，达成 PAC；
   - 编制：钢琴双手；
   - 状态：**规范单行文本占位**。

---

## 4. 理论脉络与主要文献依据

- **William E. Caplin (2015)**：
  - 《Harmony and Cadence in Gjerdingen’s “Prinner”》（Markus Neuwirth & Pieter Bergé 编《What Is a Cadence?》, pp. 17–58）：系统界定了原型 Prinner 的非终止性、低音变异机制与终止四六和弦插入条件；
- **Open Music Theory (OMT)**：
  - `schemataOpensAndCloses.md` 与 `cadenceTypes.md`：图式原型与复合/双重终止式分类；
- **与首批 20 篇《加兰特图式》的边界区隔**：
  - 严格避开首批选题；《加兰特图式》宏观探讨多类图式与古典三大曲式功能的全局对应，本文专注 Prinner 这一单一图式的和声微观力学蜕变，解构其如何打破级进惯性并转化为正格终止；
  - 正文中精准关联 short title 链接：`[《加兰特图式》](galant-schemata-and-formal-functions.md)`、`[《复合乐段》](compound-period-hierarchical-syntax.md)`。

---

## 5. 未解决的缺口与可接受的局限

- **当前缺口**：正文谱例按规范采用单行文本占位，待后续批次统一排版；
- **局限**：本文聚焦于大调语境中标准的 Prinner 向正格终止的转化，对于小调语境中涉及减七和弦与降六级低音的变异图式形态未作全面铺开，留待小调对位专题研究。
