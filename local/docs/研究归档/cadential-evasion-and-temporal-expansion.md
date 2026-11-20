# 研究归档：终止式延后与时间扩张：古典句法中的规避机制与“再来一次”技术

- **学者**：scholar-a3（接替 scholar-a2）
- **选题**：终止式延后与时间扩张：古典句法中的规避机制与“再来一次”技术（Cadential Evasion and Temporal Expansion: Avoidance Mechanics and the "One-More-Time" Technique in Classical Syntax）
- **中心论证**：在调性曲式中，完全正格终止（PAC）具有终极的闭合引力；若过早或机械按部就班地降落于第 4 或第 8 小节，将陷入“四小节超节拍方整霸权（The Tyranny of the Four-Measure Phrase）”的审美危机。维也纳古典乐派通过操控终止式的降临时间实现高阶张力管理：通过“规避终止（Evaded Cadence）”在最后一瞬以导音大跳抹消预期闭合，并触发“再来一次（One-More-Time, OMT）”变奏重跑机制（莫扎特 K. 309 III）；通过“终止弱化溢出（IAC Substitution）”以能级不足的未闭合状态触发低音级进下行连接线，引爆延续部二次高压扩张（贝多芬 Op. 2 No. 3 I）；同时严格厘清了“乐节内部扩充（Sub-phrase Expansion，如莫扎特 K. 494）”与“乐句外部扩充（Phrase Expansion）”以及“内生非标准长度（如莫扎特 K. 515）”的力学辨析界限。
- **状态**：`已成稿，第二波修订完成`

---

## 1. 实际采用的资料范围

- **Open Music Theory (OMT) 教学文献**：
  * 章节 "Internal Expansions"（内部扩充、乐节内部扩充、乐句外部扩充、规避终止、One-More-Time 技术与非标准长度辨析）；
  * 章节 "Cadence Types"（PAC、IAC、HC、Deceptive Cadence 的和声与旋律界定）；
  * 章节 "Theme Functions"（呈示、延续与终止三大曲式功能动力学）；
  * 章节 "The Sentence" 与 "The Period"（古典乐句与乐段的原型预期模型）；
- **实证总谱研读**：
  * 沃尔夫冈·阿玛多伊斯·莫扎特《C大调第9钢琴奏鸣曲》K. 309 第三乐章（Rondo: Allegretto grazioso，mm. 9–19：复合乐段大后继句、m. 15 导音大跳 A5 规避 PAC、mm. 16–19 OMT 四小节变奏重跑）；
  * 路德维希·凡·贝多芬《C大调第3钢琴奏鸣曲》Op. 2 No. 3 第一乐章（Allegro con brio，mm. 1–13：主部乐句原型在 m. 8 降落于弱 IAC、低音下行连接线、mm. 8–13 延续部五小节高八度高压拉伸）；
  * 沃尔夫冈·阿玛多伊斯·莫扎特《F大调回旋曲》K. 494（Alla breve，mm. 1–12：先行句开端基本乐念通过 m. 3 原样复述 m. 2 实现 3 小节内部扩充）；
  * 沃尔夫冈·阿玛多伊斯·莫扎特《C大调弦乐五重奏》K. 515 第一乐章（开端复合乐句内生非标准长度辨析）；
- **引证与推论纪律说明**：
  * 本文严格立足于上述实际阅读的 OMT 章节与实证总谱，严禁虚构文献页码；
  * 关于威廉·罗斯坦（William Rothstein）关于“19 世纪四小节超节拍单调霸权”的理论背景，正文中明确注明系曲式学历史溯源并依托 OMT 章节转引，不直接引证本库未收录之原著页码；
  * 终止能级落差模型、心理声学悬崖机制与终止延迟决策逻辑，均在正文明确注明为笔者的归纳推导。

---

## 2. 正文与索引位置

- **正文文件**：`content/techniques/structure/cadential-evasion-and-temporal-expansion.md`（短标题：终止式延后）
- **目录索引**：`content/techniques/structure/index.md`
- **来源与许可**：`provenance/techniques/structure/cadential-evasion-and-temporal-expansion.md`

---

## 3. 谱例状态与核验说明

正文 3 处案例中已有 2 处正式嵌入 LilyPond 代码块并通过核验，1 处保持规范文本占位：

1. **莫扎特《C大调第9钢琴奏鸣曲》K. 309，第三乐章 Rondo: Allegretto grazioso，mm. 9–19**
   - 编制与 GM 编号：钢琴双手（GM 0: acoustic grand）
   - 调性与拍号：C 大调，2/4 拍
   - 结构特征：mm. 9–12 呈示，mm. 13–15 延续冲刺，m. 15 导音大跳规避 PAC，mm. 16–19 启动 OMT 变奏重跑，m. 19 达成 I:PAC
   - 状态：**已嵌入正文并通过核验**。
2. **贝多芬《C大调第3钢琴奏鸣曲》Op. 2 No. 3，第一乐章 Allegro con brio，mm. 1–13**
   - 编制与 GM 编号：钢琴双手（GM 0: acoustic grand）
   - 调性与拍号：C 大调，4/4 拍
   - 结构特征：mm. 1–4 乐句呈示，mm. 5–8 延续冲刺，m. 8 降落为弱 IAC（高音停在三音），mm. 8–13 低音级进下行连接线触发高八度延续部 5 小节剧烈扩张，m. 13 达成强力 I:PAC
   - 状态：**已嵌入正文并通过核验**。
3. **莫扎特《F大调回旋曲》K. 494，mm. 1–12**
   - 编制与 GM 编号：钢琴双手（GM 0: acoustic grand）
   - 调性与拍号：F 大调，Alla breve 2/2 拍
   - 结构特征：先行句 mm. 1–6 中 m. 3 原样复述 m. 2 实现 3 小节内部扩充 BI，m. 6 半终止 HC；后继句 mm. 7–12 终结于完全正格终止 PAC
   - 状态：**规范文本占位**。

---

## 4. 第二波修订记录（scholar-a3）

1. **标题与 frontmatter 规范化**：增加 YAML frontmatter（`title: 终止式延后`），H1 改为短标题 `# 终止式延后`，插入单行副标题 `<p class="doc-subtitle">古典句法如何通过规避终止与“再来一次”技术实现时间维度的张力扩张？</p>`。
2. **正文文件与技术痕迹清理**：
   - 清理正文中的 markdown 内部文件名（如 `internalExpansions.md`、`themeFunctions.md`、`cadenceTypes.md`），规范转换为正式理论章节名称；
   - 删去已嵌入 LilyPond 围栏上方遗留的旧占位块（保持代码块首行属性自包含，正文更整洁）；
   - 更新跨篇链接文本为短标题（如 [《混合乐段》](hybrid-themes-and-syntax-decoupling.md)、[《海米奥拉》](../rhythm/hemiola-and-metric-conflict.md)、[《慢引子》](../../composers/beethoven/piano-sonatas/slow-introduction-integration.md)）。
3. **图表与 Mermaid 评估**：
   - 核心力学机制 Mermaid 流程图（终止能级落差与时间传动：PAC 常规闭合、IAC 弱化溢出二次点火、Evaded Cadence 假动作抹消启动 OMT）逻辑严密、直观高效，完整保留。
4. **来源与许可建立**：
   - 填写 `provenance/techniques/structure/cadential-evasion-and-temporal-expansion.md`，登记 OMT 章节与 William Rothstein 理论转引出处；2 处嵌入谱例底本记为“待补”，许可记为“未确认”。

---

## 5. 未解决的缺口与可接受的局限

- **当前缺口**：莫扎特 K. 494（mm. 1–12）仍处于规范文本占位状态，待后续谱例助手排版交付后嵌入；
- **局限**：本篇专注于核心主题内部与尾部的延后扩充，大型奏鸣曲式展开部向再现部过渡中的伪再现（False Recapitulation）与大型踏板延后留待曲式高级专题展开。
