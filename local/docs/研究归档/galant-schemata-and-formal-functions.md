# 研究归档：加兰特图式在古典句法中的曲式功能整合

- **学者**：scholar-a
- **选题**：加兰特图式在古典句法中的曲式功能整合（Galant Schemata and Formal Functions in Classical Syntax）
- **中心论证**：加兰特图式作为外声部对位骨架，其弱终止感为呈示句的主和弦延长提供了动力基础；延续句则通过图式的“时值压缩”与“节拍碎裂”引发和声节奏倍增，将线性势能注入正格终止式；贝多芬等作曲家更通过外声部对位重构与调性枢纽突破了图式的程式化边界。
- **状态**：`已成稿，待本批复读`

---

## 1. 实际采用的资料范围

- **Open Music Theory (OMT) 教学文献**：
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/schemataOpensAndCloses.md`（Meyer、Prinner 等开端与收束图式外声部音级骨架）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/schemataContinuationPatterns.md`（Fonte、Monte、Ponte 等延续图式与模进路径）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/schemata-improv.md`（加兰特图式与古典句型结合、Passo Indietro、Fast Prinner 时值压缩）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/sentence.md`（William Caplin 古典句型结构与延续句五大特征：碎裂、融解、模进、表面与和声节奏加速）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/schemataSummary.md`（加兰特图式外声部音级总览）
- **学术期刊论文**：
  * `local/resources/text/organized-html/beethoven-analysis-chamber/raiser-op74-galant-introduction-2018.md`（Johannes Raiser 2018 发表于 ZGMTH，实证考察 Emanuel Aloys Förster 1805 和弦坐落理论、Gjerdingen 图式模型在贝多芬 Op. 74 Poco Adagio 慢引子中的创造性解构与 10-8-6 对位模型）
- **特别说明**：Caplin 与 Gjerdingen 专著未在本地找到全文，本文不假托任何未读的原著名词与页码，相关理论概念均严格落脚于上述实际读过的 OMT 篇章与 Raiser 论文；关于图式终结力与曲式功能结合机制的推导，在正文中明确注明为“我据此推断”。

---

## 2. 正文位置

- 主要正文：`content/techniques/structure/galant-schemata-and-formal-functions.md`
- 目录索引：`content/techniques/structure/index.md`

---

## 3. 谱例交付与嵌入清单

正文已正式嵌入 3 处自包含 LilyPond 2.26.0 谱例（代码来自资料助手与 Mutopia/Humdrum/OMT 权威来源交付，具有完整 title 与 location 属性，GM 编号齐全，通过本地编译验证；待谱例助手独立核验完成）：
1. **海顿：G大调第42钢琴奏鸣曲 Hob. XVI:27，第 3 乐章 Presto，mm. 1–8**  
   - 证明：Meyer 呈示句（mm. 1–4）+ Passo Indietro 碎裂延续（mm. 5–6）+ 终止停顿（mm. 7–8）；
   - 交付文件：`local/resources/scores/haydn-hob-xvi-27/haydn-hob-xvi-27-mvt3-mm1-8.ly`（编制：Piano，GM 0）；
2. **莫扎特：G大调第5钢琴奏鸣曲 K. 283 (189h)，第 1 乐章 Allegro，mm. 1–10**  
   - 证明：原型古典句型的 4 小节呈示 + 6 小节延续扩展、动机融解与正格终止式；
   - 交付文件：`local/resources/scores/mozart-k283/mozart-k283-mvt1-mm1-10.ly`（编制：Piano，GM 0）；
3. **贝多芬：降E大调第10弦乐四重奏“竖琴” Op. 74，第 1 乐章 Poco Adagio，mm. 1–9**  
   - 证明：慢引子开端模型的全休止、低音 G 减七和弦转位（调性枢纽）及 10-8-6 反向对位模型；
   - 交付文件：`local/resources/scores/beethoven-op74/beethoven-op74-mvt1-mm1-9-adagio.ly`（编制：弦乐四重奏，GM 40/40/41/42）。

---

## 4. 未解决的缺口与可接受的局限

- **当前缺口**：正文谱例代码已完全嵌入并全库 validate 通过，待谱例助手出具最终独立核验报告；
- **局限**：本篇专注于呈示与延续功能的动力整合，未全面展开加兰特图式在大型奏鸣曲式副部主题或小三部曲式中段（Contrasting Middle）中的全貌，留待后续拓展篇章深入。
