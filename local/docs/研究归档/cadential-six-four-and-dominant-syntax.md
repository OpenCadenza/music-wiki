# 研究归档：终止四六的属功能延留与终止式语法

- **短标题**：终止四六和弦
- **对应正文**：`content/techniques/harmony/cadential-six-four-and-dominant-syntax.md`
- **出处记录**：`provenance/techniques/harmony/cadential-six-four-and-dominant-syntax.md`
- **当前状态**：已成稿，待本批复读
- **学者署名**：scholar-a4
- **关联合约**：S106（task-46）

---

## 1. 核心论点与研究问题

- **中心问题**：终止四六和弦在古典终止式中究竟是独立和弦还是属延留？它何时必须出现、何时被省略，又如何重塑属七解决与终止层级？
- **核心理论发现**：
  1. **功能本质归属**：彻底纠正传统和声学将终止四六机械标记为 $I^6_4$ 的概念谬误。其低音为处于强拍或次强拍的原位属音（$\hat{5}$），上方四度音（$\hat{1}$）与六度音（$\hat{3}$）是对位上的不协和倚音，必须严格向下级进解决至导音（$4 \to 3$）与超主音（$6 \to 5$），故其本质是属功能区内部的双重倚音延留，正确标记为 $V^{6-5}_{4-3}$ 或 $Cad^6_4$；
  2. **倍加禁忌与声部时钟**：四部织体中几乎必然倍加低音属音，严禁倍加四度或六度音，以防在平行下行解决中造成平行五八度；
  3. **微观对位咬合（8–7 滑移与三全音激活）**：在六度与四度下行解决的同时，倍加低音的八度音顺势滑移至小七度（$8 \to 7$），瞬时激活属七不协和三全音，形成“前属蓄能 $\to$ 重拍阻尼延留 $\to$ 三全音向心加速 $\to$ 主和弦闭合”的两阶段动能梯级；
  4. **出现与省略的结构法则**：
     - **必须出现**：宏观结构终结（奏鸣曲式 EEC 与 ESC）、协奏曲华彩段进入点（Cadenza Entry）、复合乐段后乐句完满终止（PAC），用于最大化重音制动与闭合权威；
     - **果断省略**：轻快流动性简单半终止（Simple HC）、快速谐谑曲或微型乐节，直接采用 $ii^6 \to V$ 或 $IV \to V$，以维持前进动量，防止结构过早下锚。

---

## 2. 正文与索引位置

- **正文文件**：`content/techniques/harmony/cadential-six-four-and-dominant-syntax.md`（短标题：终止四六和弦）
- **来源与许可**：`provenance/techniques/harmony/cadential-six-four-and-dominant-syntax.md`

---

## 3. 谱例状态与案例核验

1. **莫扎特：A大调第11钢琴奏鸣曲 K. 331，第 1 乐章 Andante grazioso，mm. 1–8**
   - 证明：前乐句 m. 4 复合半终止与后乐句 m. 8 复合 PAC，展示完美的 6-5、4-3 与 8-7 声部对位解决；
   - 谱面核验：
     - m. 4：低音 E 上方打出六度 C# 与四度 A，下行解决至五度 B 与三度 G#（$V^{6-5}_{4-3}$ 半终止）；
     - m. 8：低音 E 上右手敲出 `[E–A–C#]` 重拍 $Cad^6_4$，随后四度下行至 G#、六度下行至 B、八度滑入七度 D 形成完整 $V^{8-7}_{6-5 \atop 4-3}$，最后干净收束于 A 大调原位 PAC，旋律稳稳落于主音 A；
   - 底本来源：本地 Humdrum 莫扎特奏鸣曲库 `0043-43-Piano Sonata No. 11 in A major, K 331 (300i), mvmt. 1a.abc`；
   - 状态：**规范单行文本占位**。
2. **莫扎特：C大调第16钢琴奏鸣曲 K. 545，第 1 乐章 Allegro，m. 4 与 mm. 71–75**
   - 证明：主部简单半终止省略四六 vs. 副部 EEC 强制重音终止四六拦截；
   - 谱面核验：
     - m. 4：轻盈流动，$I \to IV \to ii^6 \to V$，完全省略四六；
     - mm. 71–75：长程十六分音符狂飙后，m. 71 强拍在低音属音 D 上以重音轰出 $Cad^6_4$，随后转化为 mm. 72–74 的长属七长颤音，并在 m. 75 爆发出 G 大调原位 PAC；
   - 底本来源：本地 Humdrum 莫扎特奏鸣曲库 `0061-61-Piano Sonata No. 15 in C major, K 545, mvmt. 1.abc`；
   - 状态：**规范单行文本占位**。
3. **贝多芬：C小调第8钢琴奏鸣曲 Op. 13，第 2 乐章 Adagio cantabile，mm. 1–8**
   - 证明：慢乐章如歌主题中终止四六的情感凝聚与 PAC 平静消解；
   - 谱面核验：第 4 小节半终止四六暂歇，第 8 小节强拍在低音降 E 上爆发出浓郁的 $Cad^6_4$，旋律声部由降 E 平缓滑向降 D（七音），完美配合 6-5 与 4-3 的内部消解并达成 PAC；
   - 底本来源：本地 Humdrum 贝多芬奏鸣曲库 `beethoven-piano-sonatas-main/kern/sonata08-2.krn`；
   - 状态：**规范单行文本占位**。

---

## 4. 理论脉络与主要文献依据

- **Open Music Theory (OMT)**：
  - `cadenceTypes.md`：复合终止（Compound Cadence）、双重终止（Double Cadence）与 $V^{6-5}_{4-3}$、属七滑移定义；
  - `harmonicSyntax1.md` / `harmonicSyntax2.md`：属功能区（Dominant Zone）触发与延留机制；
- **William Caplin**：《古典曲式》（*Classical Form*, 1998），终止功能（Cadential Function）与终止四六的曲式权重分配；
- **Heinrich Schenker**：《自由对位》（*Der freie Satz*, 1935），属低音上方的对位倚音还原理论；
- **与首批 20 篇的关系与边界**：
  - 与《终止图式》（专论加兰特外声部线型公式如 Prinner）与《终止式延后》（专论规避终止与时间扩张）严格区分；
  - 正文中精准关联 short title 链接：`[《众赞歌终止式》](cadential-voice-clock-and-phase-decoupling.md)`、`[《复合乐段》](compound-period-hierarchical-syntax.md)`、`[《乐句扩展》](phrase-expansion-and-structural-skeleton.md)`、`[《终止式延后》](cadential-evasion-and-temporal-expansion.md)`。

---

## 5. 未解决的缺口与可接受的局限

- **当前缺口**：正文谱例按规范采用单行文本占位，待后续批次统一排版；
- **局限**：本文聚焦于古典乐派严格四部和声与键盘体裁，未深入探讨管弦乐全奏中跨乐器音区重叠对四度倚音泛音共鸣的声学掩蔽效应。
