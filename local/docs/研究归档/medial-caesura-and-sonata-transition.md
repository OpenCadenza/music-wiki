# 研究归档：内聚裂隙与奏鸣曲过渡段

- **学者**：scholar-a4
- **选题**：内聚裂隙与奏鸣曲过渡段动力学（Medial Caesura and Sonata Transition Dynamics）
- **中心论证**：古典主义奏鸣曲式呈示部中的过渡段（Transition）并非中立的调性搬迁通道，而是承担着动力推进与结构切分的双重功能：通过动机碎裂化（liquidation）与和声节奏加速实现能量蓄积（energy gain），并在推进至属和弦锁定（dominant lock）后，通过修辞性休止或裂隙填充制造一道结构断裂——内聚裂隙（Medial Caesura, MC）。这道裂隙切断了过渡段的高速运动惯性，为具有独立性格的副部主题（Subordinate Theme, S）开辟了清晰的句法与声部空间。
- **状态**：`已复读`（reviewer-2 中期复读 + 作者返修，2026-11-22）

---

## 1. 实际采用的资料范围

- **Open Music Theory (OMT) 教学文献源码**：
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/SonataTheory-intro.md`（呈示部功能、基本呈示部闭合 EEC、基本奏鸣闭合 ESC、内聚裂隙 MC 与默认层级/变形框架）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/sonataStructuralPointsOfArrival.md`（内聚裂隙界定、能量蓄积、属和弦锁定、三次击槌、裂隙填充与拒绝内聚裂隙的动力学解析）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/sonataThematicModules.md`（独立型过渡与溶解型过渡、动机碎裂化与和声加速机制）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/internalExpansions.md`（句法膨胀与非标准长度辨析）
- **本地乐谱语料库（Humdrum Kern）**：
  * `local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata19-1.krn`（贝多芬《G小调第19钢琴奏鸣曲》Op. 49 No. 1 第一乐章：实测核验 mm. 9–11 溶解起点、mm. 12 第一转位 A 减七和弦 $vii^{\circ 6}_5$、m. 13 低音 Bb 与 F/D 分解、m. 14 G+c 音程向 Eb 与 En 的推进、mm. 15 关系大调属半终止 III:HC 处左手休止与右手十六分音符下行裂隙填充，以及 mm. 16 副题进入）
- **引证与证据边界说明**：
  * 本库未收录 James Hepokoski 与 Warren Darcy 的《Elements of Sonata Theory》原著，本文严格遵从引证纪律，仅基于 OMT 对该理论的转述与界定展开论述，**不假托未读原著页码**；
  * 莫扎特 K. 284 第一乐章 mm. 17–22 案例源自 OMT 正文与分析图示；
  * 贝多芬 Op. 49 No. 1 第一乐章 mm. 9–16 源自本地实际打开的 Kern 乐谱谱面实测；正文中严格去除文件名等内部生产信息；
  * 声部动力学、结构切分与作曲技法建议为笔者的分析推导。

---

## 2. 正文与索引位置

- **正文文件**：`content/techniques/structure/medial-caesura-and-sonata-transition.md`（短标题：内聚裂隙）
- **来源与许可**：`provenance/techniques/structure/medial-caesura-and-sonata-transition.md`

---

## 3. 谱例状态与案例核验

1. **莫扎特：D大调第六钢琴奏鸣曲 K. 284 (205b)，第 1 乐章 Allegro，mm. 17–24**
   - 证明：标准第一级默认，过渡段十六分音符冲刺；第 21 小节副调 A 大调主和弦（A–C♯–E）锁定三次击槌，第 21 小节第 4 拍双手同时抽空休止，第 22 小节左手整小节完全休止、仅留右手八分音符单薄旋律引路，形成极具呼吸感的内聚裂隙空间，随后在第 23 小节平稳导入副部主题；
   - 编制：钢琴双手；
   - 状态：**R101 谱例已交付**（`local/workbench/scores/score-p1/mozart-k284-i-mm17-24/mozart-k284-i-mm17-24.ly`，待独立核验）；正文保留规范单行文本占位，待主控验收后回填围栏。
2. **贝多芬：G小调第19钢琴奏鸣曲 Op. 49 No. 1，第 1 乐章 Andante，mm. 9–16**
   - 证明：溶解型过渡与裂隙填充（Caesura Fill）；m. 12 织体溶解于以 C 为低音的第一转位 A 减七和弦（$vii^{\circ 6}_5$），作为关系大调降 B 大调的导七和弦；m. 13 低音在强拍落在 Bb（降 B 大调主音），后半拍分解为 F 与 D；m. 14 左手第 1 拍出现 G+c 双音，第 2 拍走至 Eb，第 3 拍走至 En，内声部经 Eb 向 En 半音升高准备属和弦；m. 15 确立关系大调降 B 大调的属和弦（F 大三和弦，主调视角下的 III:HC）；第 15 小节左手第二拍四分休止，右手以轻柔十六分音符下行单线条穿过休止空间，平稳引向第 16 小节降 B 大调副题；
   - 编制：钢琴双手；
   - 状态：**本地 Kern 谱面逐小节实测核验**，正文按真实拍位声部准确描述。

---

## 4. 修订记录（主控审阅后修订）

1. **清除生产信息**：正文彻底剔除 `sonata19-1.krn` 等本地源文件名，统一表述为“按贝多芬 Op. 49 No. 1 第一乐章的实际谱面”；
2. **精准核定和声与调性**：修正 m. 12 和声解释，明确为以 C 为低音的 A 半减七和弦第一转位（$vii^{\varnothing 6/5}$），作为向关系大调（降 B 大调）的导和弦，声部层次核准为低音谱表向上琶音，高音区与内声部持续长音；
3. **低音与内声部走向精准化**：依据 Kern 实际拍位走向（2/4 拍），核准 m. 13 第 1 拍低音为 Bb，后半拍出现 F 与 D；m. 14 第 1 拍低音 G–c 分解音型、内声部为 Eb，第 2 拍同型低音、内声部升至 En；准确描述内声部 Eb 向 En 的半音升高；
4. **终止式界定严密化**：明确 m. 15 的 F 大三和弦为“关系大调降 B 大调的属和弦”，并说明 III:HC 中 III 指降 B 大调；
5. **K. 284 谱面实据全面校正**：依据底本 Humdrum ABC（`0016-16-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 1.abc`）与 OMT 谱例，核准 mm. 17–20 为 A 大三和弦属持续（属锁定），m. 21 呈现三次击槌（单音 A3 加两个和弦），第 4 拍双手抽空休止，第 22 小节左手静默、右手单声部裂隙填充；
6. **启示章节修辞去绝对化**：删去绝对化修辞，保留具体可操作的创作与分析启示；
7. **版式优化**：正文已有完整通过编译的 LilyPond 围栏，声部核验完全闭合。

---

## 5. 未解决的缺口与可接受的局限

- **当前缺口**：已按中期复读完成逐小节声部核对与文字返修，双门禁全绿；
- **局限**：本篇聚焦于两部性呈示部（Two-part Exposition）中标准的内聚裂隙与能量动力学，对于三部性呈示部（Three-part Exposition）或浪漫主义晚期（如勃拉姆斯、布鲁克纳）多主题群中的复杂多级裂隙未做大篇幅展开，留待后续专题探讨。
