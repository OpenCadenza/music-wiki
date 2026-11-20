# 研究归档：音色对比阶梯（timbral-contrast-and-formal-articulation）

- **学者**：scholar-c / scholar-c3（接替续作）
- **选题**：音色对比阶梯（Timbral Contrast and Formal Articulation）
- **中心论证**：音色并非事后涂抹的外在装饰，而是时间轴上可感知的独立曲式标点；配器变换速率（Rate of Orchestral Change）决定了作品的宏观心理时空，而贝尔金五级音色对比阶梯（Group 1–5）的精确咬合，能够有效避免“过度对比造成的微观旋律断裂”与“过弱对比造成的宏观曲式边界模糊”，并通过延留音（Holdover）化解强奏到弱奏的听觉适应断崖。
- **实际采用的资料范围**：
  - Alan Belkin: *Artistic Orchestration*（原件不在本工作树，摘录与记录见 `local/docs/研究归档/_运行记录/scholar-c.md`）：
    - "Rate of Orchestral Change" (pp. 21–23)：配器变换速率的结构心理学效应、马勒第四交响曲第二乐章与第三乐章的变换速率反差；
    - "Degree of continuity/contrast of timbre" (pp. 23–25)：音色与曲式感知核心公理、五级对比阶梯 Group 1 至 Group 5、背景恒定削弱对比原理、混合音色钝化曲式大对比风险、大全奏转极弱的听觉适应缓冲律（Holdover）；
    - "Interpreting the phrasing" (pp. 25–27)：渐强（crescendo）阶梯式乐器添加律（贝九第一乐章开篇 mm. 1–35）。
  - Philharmonia Orchestra 乐器学档案（原件不在本工作树，摘录与记录见 `local/docs/研究归档/_运行记录/scholar-c.md`）：
    - `clarinet.md`：单簧管三大音区差异在单件乐器内部形成的微观音色阶梯；
    - `flute.md`：长笛在暗淡低音区与银色光辉高音区的色彩跃迁；
    - `violin.md`：拉弦（arco）与拨弦（pizzicato）的发音机理突变。
  - 贝多芬《第七交响曲》Op. 92 第二乐章分谱（本工作树实际打开核验）：
    - `local/workbench/scores/score-s2/downloads/op92-2/`（`Symphony7_2.ly`, `viola.ly`, `violoncello.ly`, `basso.ly` 等，Mutopia-2005/08/21-595，排版者：Stelios Samelis）。
  - 贝多芬《第九交响曲》Op. 125 与马勒《第四交响曲》总谱定位：
    - 通用作品目录与文献分析定点（本工作树无乐谱副本）。
- **正文位置**：
  - 主要正文：`content/techniques/sound/timbral-contrast-and-formal-articulation.md`
  - 目录实质索引：`content/techniques/sound/index.md`
- **谱例现状与占位清单**：
  - 贝多芬《第七交响曲》Op. 92 第二乐章（Allegretto），mm. 1–26（纯弦乐家族内部低频速率与 Group 1 微弱对比，声部摘录占位）；
  - 贝多芬《第九交响曲》Op. 125 第一乐章开篇，mm. 1–35（从空五度震音到全奏爆发的阶梯式渐强，声部摘录占位）；
  - 马勒《第四交响曲》第二乐章，mm. 34–46（高频配器变换速率与 Group 2–3 震荡，声部摘录占位）。
- **第二波（2026-11-20）修订记录**：
  1. **彻底清除正文源文件行号与本地路径（落实清单 B 条）**：
     - 清除正文 8 处 `行 N` 形态标记（约行 430–453、行 456、行 468–507、行 514、行 516、行 518、行 534–547），全部替换为标准学术著作章节名称（如“配器变换速率”一章、"Degree of continuity/contrast of timbre" 一章等）；
     - 清除文末参考文献节中的 2 处 `local/resources/...` 路径，转为规范出处指引；正文确保无内部行号、无本地伪路径、无协作状态说明。
  2. **图示结构化升级**：将正文中 3 处 ASCII 字符框图（高低频配器变换速率对比、配器标点失衡形态、创作 Agent 配器时间轴决策树）全面升级为规范 `mermaid` 流程图，提升跨端排版一致性。
  3. **建立来源与许可索引（落实 D 条）**：完成 `provenance/techniques/sound/timbral-contrast-and-formal-articulation.md`，区分工作树内实际打开的分谱实证与前任记录摘录来源，谱例表规范设立并严格标注“待补”与“未确认”。
- **状态**：`第二波第2篇完成，待验收`
