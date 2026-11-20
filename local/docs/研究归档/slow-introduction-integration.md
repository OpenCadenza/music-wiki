# 研究归档：慢引子

- **学者**：scholar-a2（原创），scholar-a3（续作对齐）
- **选题**：慢引子（Slow Introduction Integration in Beethoven's Piano Sonatas）
- **中心论证**：在海顿/莫扎特的古典常规中，慢引子（Slow Introduction）作为置于奏鸣曲本体之外的“辅助模块（Auxiliary Module）”，大多扮演外在“门厅（Antechamber）”与装饰性前奏的角色，进入快板后便功成身退。贝多芬在钢琴奏鸣曲中发动了彻底的结构革命：通过“动机母体化与时值压缩”将慢引子转化为快板主部的主题基因库，通过“跨越曲式边界的暴力内嵌”在呈示部末尾、展开部与尾声处原速召回慢引子冻结时间流，并通过核心和声矛盾（减七和弦、阻碍终止、半音阶下行）实现全乐章的调性全息统摄；实证考察其在 Op. 13《悲怆》（早期突入式）、Op. 81a《告别》（中期全息泛化式）与 Op. 111（晚期复调母体式）中的深刻演进。
- **状态**：`已完成第一波审查与对齐（H1 短标题、副标题、frontmatter、无行号与伪路径、消除内部代号、复核拍号一致性、清理 GM 编号、补齐 provenance 表）`

---

## 1. 实际采用的资料范围

- **Open Music Theory (OMT) 教学文献源码（工作树真实存在）**：
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/SonataTheory-intro.md`（奏鸣曲理论导论、Auxiliary Modules 引子辅助模块定位、Defaults 默认级与 Deformations 形变界定）；
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/sonataThematicModules.md`（引子与主部模块功能与展开部戏剧推进）；
- **实证总谱与 Humdrum Kern 语料库（工作树真实存在）**：
  * `local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata08-1.krn`：贝多芬 Op. 13 第一乐章开端 Grave（mm. 1–10）及快板第一主题裂变衔接（mm. 11–19）逐音对位实证；
  * `local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata26-1.krn`：贝多芬 Op. 81a 第一乐章 Adagio（mm. 1–16）“Le-be-wohl”下行三音级阻碍终止与 Allegro（mm. 17–25）动机泛化实证；
  * `local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata32-1.krn`：贝多芬 Op. 111 第一乐章 Maestoso（mm. 1–16）减七度大跳、半音阶下行与 Allegro（mm. 19–25）赋格化主题裂变实证；
- **转引与前任研究摘录说明（当前工作树无本地独立副本）**：
  * Johannes Raiser (2018) 关于贝多芬慢引子加兰特图式与减七和弦声部坐落的理论分析；
  * Lewis Lockwood 关于贝多芬单行草稿到手稿定稿中动机浓缩过程的研究；
  * Eastman School of Music 关于 18 世纪交响与奏鸣曲慢引子 Topical states 的分析；
  * 洛桑联邦理工学院（DCML）和声标注数据集中关于 Op. 111 第一乐章单一 4/4 拍号与和声演进的判定；
- **引证与推论纪律说明**：
  * 本文严格立足于上述实际阅读的 OMT 章节、Kern 语料库与前任记录，严禁虚构文献页码与行号；
  * 慢引子的辅助模块界定与形变理论忠实依据 OMT 体系；
  * 谱例小节、节拍、调号与声部织体严格依据 Kern 谱源；
  * 关于慢引子动机母体化、暴力内嵌的时间冻结效应，以及早、中、晚期三大范式的创作决策对照，在正文中明确注明为笔者的分析推导。

---

## 2. 正文与索引位置

- **专题正文**：`content/composers/beethoven/piano-sonatas/slow-introduction-integration.md`
- **归档对应**：本归档（`local/docs/研究归档/beethoven-slow-introduction-integration.md`）对应上述正文文章（保留既有文件名，未新建重复归档）。
- **跨篇自然链接**：正文有机呼应此前篇目：[《混合乐段》](../../../techniques/structure/hybrid-themes-and-syntax-decoupling.md)（紧凑型微观解耦 vs 宏观引子解耦）、[《海米奥拉》](../../../techniques/rhythm/hemiola-and-metric-conflict.md)（双重附点与极端切分对节拍引力的撕裂），以及[《挂留音》](../../../techniques/counterpoint/suspension-mechanics-and-voice-leading.md)（Op. 111 中慢引子减七大跳向严密二重赋格对位的蜕变）。消除了一切内部角色代号。

---

## 3. 谱例现状

正文 3 处案例均已完成自包含 LilyPond 围栏嵌入并校验通过：

1. **贝多芬：c小调第8钢琴奏鸣曲“悲怆” Op. 13，第一乐章 Grave - Allegro di molto e con brio，mm. 1–19**
   - 谱例 id：`beethoven-op13-i-mm1-19`
   - 定位：`Grave，mm.1–19`
   - 编制：钢琴双手（Acoustic Grand Piano，已清除 GM 0 编号）
   - 调性/拍号：c 小调，Grave 4/4 拍 $\rightarrow$ Allegro 2/2 拍；现况：已完成自包含 LilyPond 围栏嵌入并校验通过。
2. **贝多芬：降E大调第26钢琴奏鸣曲“告别” Op. 81a，第一乐章 Adagio - Allegro，mm. 1–25**
   - 谱例 id：`beethoven-op81-i-mm1-25`
   - 定位：`Adagio，mm.1–25`
   - 编制：钢琴双手（Acoustic Grand Piano，已清除 GM 0 编号）
   - 调性/拍号：降 E 大调，Adagio 2/4 拍 $\rightarrow$ Allegro 2/2 拍；现况：已完成自包含 LilyPond 围栏嵌入并校验通过。
3. **贝多芬：c小调第32钢琴奏鸣曲 Op. 111，第一乐章 Maestoso - Allegro con brio ed appassionato，mm. 1–25**
   - 谱例 id：`beethoven-op111-i-mm1-25`
   - 定位：`Maestoso，mm.1–25`
   - 编制：钢琴双手（Acoustic Grand Piano，已清除 GM 0 编号）
   - 调性/拍号：c 小调，全乐章为单一 4/4 拍（Maestoso 4/4 拍 $\rightarrow$ Allegro 4/4 拍，速度加快而拍号不变，无 2/2 残留）；现况：已完成自包含 LilyPond 围栏嵌入并校验通过。

---

## 4. 待解决缺口与后续

- 正文内跨篇引用已规范为短标题链接，消除对内部角色代号 `scholar-b2` 的提及；
- 谱例信息块已清理 GM 编号，只保留乐器名称；
- 全乐章拍号与谱面数据已完成双重复核。
