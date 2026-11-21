# 研究归档：加兰特图式在古典句法中的曲式功能整合

- **学者**：scholar-a3（接替 scholar-a2 / scholar-a）
- **选题**：加兰特图式在古典句法中的曲式功能整合（Galant Schemata and Formal Functions in Classical Syntax）
- **中心论证**：加兰特图式作为外声部对位骨架，其弱终止感为呈示句的主和弦延长提供了动力基础；延续句则通过图式的“时值压缩”与“节拍碎裂”引发和声节奏倍增，将线性势能注入正格终止式；贝多芬等作曲家更通过外声部对位重构与调性枢纽突破了图式的程式化边界。
- **状态**：`已成稿，第二波修订完成`

---

## 1. 实际采用的资料范围

- **Open Music Theory (OMT) 教学文献**：
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/schemataOpensAndCloses.md`（Meyer、Prinner 等开端与收束图式外声部音级骨架）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/schemataContinuationPatterns.md`（Fonte、Monte、Ponte 等延续图式与模进路径）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/schemata-improv.md`（加兰特图式与古典句型结合、Passo Indietro、Fast Prinner 时值压缩）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/sentence.md`（William Caplin 古典句型结构与延续句五大特征：碎裂、融解、模进、表面与和声节奏加速）
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/schemataSummary.md`（加兰特图式外声部音级总览）
- **学术期刊论文与理论文献**：
  * `local/resources/text/organized-html/beethoven-analysis-chamber/raiser-op74-galant-introduction-2018.md`（Johannes Raiser 2018 发表于 ZGMTH，实证考察 Emanuel Aloys Förster 1805 和弦坐落理论、Gjerdingen 图式模型在贝多芬 Op. 74 Poco Adagio 慢引子中的创造性解构与 10-8-6 对位模型）
  * William E. Caplin 2015《Harmony and Cadence in Gjerdingen's "Prinner"》（界定加兰特线性延续图式的对位本质、非终止属性与延续功能，论证向完全正格终止转化的低音变异条件；注：该文与专著全书在本工作树无独立本地全文副本，基于学术转引与既有研究归档记录）
- **特别说明**：Caplin 与 Gjerdingen 专著全书未在本地收录，本文不假托任何未读原著页码，相关理论概念均严格落脚于上述实际读过的 OMT 篇章、Raiser 论文与 Caplin 2015 论文；关于图式终结力与曲式功能结合机制的推导，在正文中明确注明为“笔者据此推断”。

---

## 2. 正文与索引位置

- **正文文件**：`content/techniques/structure/galant-schemata-and-formal-functions.md`（短标题：加兰特图式）
- **目录索引**：`content/techniques/structure/index.md`
- **来源与许可**：`provenance/techniques/structure/galant-schemata-and-formal-functions.md`

---

## 3. 谱例状态与核验说明

正文 3 处谱例此前经谱例专职助手核验发现偏差后，已全部完成校勘修正并正式嵌入 LilyPond 代码块，格式与音乐核验全绿通过：

1. **海顿：G大调第42钢琴奏鸣曲 Hob. XVI:27，第 3 乐章 Presto，mm. 1–8**  
   - 证明：Meyer 呈示句（mm. 1–4）+ Passo Indietro 碎裂延续（mm. 5–6）+ 终止停顿（mm. 7–8）；  
   - 编制：Piano（GM 0: acoustic grand），调性/拍号：G 大调，2/4 拍；  
   - 状态：**已嵌入正文并通过核验**。
2. **莫扎特：G大调第5钢琴奏鸣曲 K. 283 (189h)，第 1 乐章 Allegro，mm. 1–10**  
   - 证明：原型古典句型的 4 小节呈示 + 6 小节延续扩展、动机融解与正格终止式；  
   - 编制：Piano（GM 0: acoustic grand），调性/拍号：G 大调，3/4 拍；  
   - 状态：**已嵌入正文并通过核验**。
3. **贝多芬：降E大调第10弦乐四重奏“竖琴” Op. 74，第 1 乐章 Poco Adagio，mm. 1–9**  
   - 证明：慢引子开端模型的全休止、低音 G 减七和弦转位（调性枢纽）及 10-8-6 反向对位模型；  
   - 编制：弦乐四重奏（第一小提琴 GM 40: violin、第二小提琴 GM 40: violin、中提琴 GM 41: viola、大提琴 GM 42: cello），调性/拍号：降 E 大调，2/2 拍；  
   - 状态：**已嵌入正文并通过核验**。

---

## 4. 第二波修订记录（scholar-a3）

1. **标题与 frontmatter 规范化**：增加 YAML frontmatter（`title: 加兰特图式`），H1 改为短标题 `# 加兰特图式`，插入单行副标题 `<p class="doc-subtitle">加兰特图式如何作为外声部对位骨架深度整合进古典曲式功能？</p>`。
2. **归档过期纠偏（清单 #6）**：
   - 彻底删除原归档中 3 处谱例“交付核验未通过，重编码中”的过期陈述，与正文现行且已编译通过的三道 LilyPond 围栏对齐。
3. **姊妹篇深度协同**：
   - 与刚提交的《混合乐段》（`hybrid-themes-and-syntax-decoupling.md`）保持理论话语一致，在二、2 节补充并深化 William E. Caplin（2015）关于 Prinner 线性延续图式非终止属性的论述（缺乏向原位属音的跳进，本质为延续功能而非封闭终止），指出乐段收束要么要求低音变异、要么脱离图式切入专门终止进行；
   - 更新文末跨篇链接文本，使用短标题 [《混合乐段》](hybrid-themes-and-syntax-decoupling.md)。
4. **图表评估**：
   - 全文核查无旧 ASCII 字符画图；现有小节结构划分、对位骨架音级公式与完整实证谱例已极为清晰，无需画蛇添足加 Mermaid 图。
5. **来源与许可建立**：
   - 填写 `provenance/techniques/structure/galant-schemata-and-formal-functions.md`，登记 OMT 章节、Johannes Raiser 2018 论文以及 William E. Caplin 2015 论文出处；3 处谱例底本记为“待补”，许可记为“未确认”。
6. **差异复读修正（第二轮）**：
   - 审慎校正 Caplin 2015 论文转述用语，改“专门指出”为客观陈述“据卡普林对 Prinner 的辨析（见研究归档所列 Caplin 2015 论文）”，并明确标注该文在本地工作树无独立全文副本的引证状态；
   - 修正案例 2 莫扎特 K. 283 前 4 小节实证分析：纠正原先将阿尔贝蒂分解低音误称“声部延留与对位延留和弦”的偏差，实打实按谱面明确为连续经过式属七和弦转位低音（$G \to A \to F\sharp \to G$）与轻快琶音伴奏织体（$I - V^4_3 - V^6_5 - I$）；
   - 更新 §四 跨专题互链块，将旧长标题全面更新为短标题[《挂留音》]与[《半音挂留》]。

---

## 5. 未解决的缺口与可接受的局限

- **当前缺口**：3 处谱例已全部嵌入并通过核验，正文本篇无谱例缺口；
- **局限**：本篇专注于呈示与延续功能的动力整合，未全面展开加兰特图式在大型奏鸣曲式副部主题或小三部曲式中段（Contrasting Middle）中的全貌，留待后续拓展篇章深入。
