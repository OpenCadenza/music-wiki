# 研究归档：混合乐段与古典主题句法的多维解耦

- **学者**：scholar-a2（接替 scholar-a）
- **选题**：混合乐段与古典主题句法的多维解耦（Hybrid Themes and Syntax Decoupling in Classical Form）
- **中心论证**：维也纳古典乐派通过复合基础乐念（CBI）将旋律动机设计（Melodic Design）与曲式和声功能（Harmonic/Formal Function）彻底解耦：动机上借鉴先行句的“基本乐念 + 对比乐念”提供丰富的歌唱色彩，和声上借鉴呈示句的“主和弦对位延长”去除中途终止的泄力；由此衍生的四类混合乐段绝非机械分类，而是作曲家针对抒情句读、纯和声共鸣、无阻断冲刺与一体化大弧线等不同表现压力下的力学平衡方案。
- **状态**：`已成稿，待本批复读`

---

## 1. 实际采用的资料范围

- **Open Music Theory (OMT) 教学文献源码**：
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/hybridThemes.md`（四类经典混合乐段结构、CBI 概念界定与四部核心实证案例分析）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/themeFunctions.md`（呈示、先行、延续、终止与后继三大时序阶段的核心曲式功能界定）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/sentence.md`（原型乐句的呈示与延续动力机制：碎裂、清算、加速）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/period.md`（原型乐段的双终止问答构架）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/classicalThemes.md` 与 `internalExpansions.md`（古典主题内部扩充与非标准长度辨析）
- **学术研究专论与来源卡**：
  * `local/resources/catalog/parts/text/sources/caplin-gjerdingen.md`（Caplin 与 Gjerdingen 来源卡）
  * `local/resources/text/caplin-gjerdingen/caplin-2015-prinner-cadence-guide.md` 与原件文献（William E. Caplin 2015《Harmony and Cadence in Gjerdingen's "Prinner"》：论证加兰特延续图式的非终止属性、低音变异转正格终止条件，以及延续功能与纯粹终止功能的严格和声界分）
- **引证与推论纪律说明**：
  * 本地未收录 William E. Caplin《Classical Form》专著全书，本文严格遵循引证纪律，**不假托任何未读原著页码**；
  * 概念界定来自上述实际阅读的 OMT 篇章与 Caplin 2015 论文；
  * 谱例小节、和声级数与声部织体严格依据谱面显示；
  * 动机解耦的“力学本质”、“动能蓄积与释放天平”以及四类混合乐段的创作决策对照，在正文中明确注明为笔者的分析推导。

---

## 2. 正文与索引位置

- **正文文件**：`content/techniques/structure/hybrid-themes-and-syntax-decoupling.md`
- **层级目录索引**：`content/techniques/structure/index.md`（已收录并阐述本篇核心音乐问题）

---

## 3. 谱例占位与待交付清单

正文 4 处案例均规范采用标准文本引用块占位，明确作品、作品号、乐章、小节范围、调性、拍号、声部编制与 GM 程序号，完全规避空 lilypond 围栏风险。已准备向谱例助手提交 R 卡需求：

1. **莫扎特：C大调第16钢琴奏鸣曲 K. 330 (300h)，第 2 乐章 Andante cantabile，mm. 1–8**  
   - 证明：混合类型 1（先行句 mm. 1–4 弱半终止 + 延续句 mm. 5–8 碎裂清算直达 V:PAC）；  
   - 编制：钢琴双手（GM 0: Acoustic Grand Piano）；  
   - 调性/拍号：F 大调，3/4 拍；状态：**已由 assistant-scores-d 交付并核验通过，已正式嵌入正文**。
2. **海顿：G大调弦乐四重奏 Hob. III:66 (Op. 77 No. 1)，第 2 乐章 Adagio，mm. 1–8**  
   - 证明：混合类型 2（先行句 mm. 1–4 弱半终止 + 纯粹扩充终止和声进行 mm. 5–8 $I^6 - ii^6_5 - V - I$，无延续碎裂标记）；  
   - 编制：弦乐四重奏（第一小提琴 GM 40、第二小提琴 GM 40、中提琴 GM 41、大提琴 GM 42）；  
   - 调性/拍号：降 E 大调，2/4 拍；状态：文本占位，待交付。
3. **贝多芬：c小调第7小提琴奏鸣曲 Op. 30 No. 2，第 3 乐章 Scherzo: Allegro molto，mm. 1–8**  
   - 证明：混合类型 3（CBI mm. 1–4 主和弦对位延长无终止 + 延续句 mm. 5–8 模进碎裂急促闭合）；  
   - 编制：小提琴与钢琴（小提琴 GM 40、钢琴 GM 0）；  
   - 调性/拍号：C 大调，3/4 拍；状态：文本占位，待交付。
4. **贝多芬：G大调第2弦乐四重奏 Op. 18 No. 2，第 4 乐章 Allegro molto，mm. 1–8**  
   - 证明：混合类型 4（大提琴独奏 CBI mm. 1–4 无终止 + 四重奏全奏后继句 mm. 5–8 重构 CI 达成 I:PAC）；  
   - 编制：弦乐四重奏（第一小提琴 GM 40、第二小提琴 GM 40、中提琴 GM 41、大提琴 GM 42）；  
   - 调性/拍号：G 大调，2/4 拍；状态：文本占位，待交付。

---

## 4. 未解决的缺口与可接受的局限

- **当前缺口**：4 处谱例处于文本占位状态，待谱例编码助手交付并经核验通过后嵌入真实 lilypond 围栏；
- **局限**：本篇专注于 8 小节紧凑型基础主题（Tight-knit Themes）的微观解耦机制，尚未深入拓展至大型奏鸣曲式副部主题中的 16 小节大混合结构（如扩大乐句或三倍乐段），留待后续高阶结构专题展开。
