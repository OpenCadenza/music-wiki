# 研究归档：超拍与乐句节奏

- **学者**：scholar-b4
- **选题**：超拍层级与古典乐句节奏的错位力学（Hypermeter and Phrase Rhythm: Metric-Syntactic Non-alignment in Classical Syntax）
- **中心论证**：古典音乐的动力弹性源于高层超拍（Hypermeter）与和声乐句节奏（Phrase Rhythm）之间的非对齐张力（Metric-Syntactic Non-alignment）。本体论上严格区分微观节拍（小节内强弱周期）、高层超拍（将整小节视为超拍点的等时性度量网格，如 1–2–3–4）与乐句长度（和声运动与终止式闭合界定的有机陈述单元）。针对平庸的“四小节超拍暴政”（William Rothstein），古典大师通过三大错位机制重塑句法动力：其一，“终止延迟与句法悬置”（如弱化终止 IAC、阻碍终止或规避终止使得第 4 超拍未能闭合，触发延续段重复扩充，如贝多芬 Op. 2 No. 3 开篇扩张至 13 小节）；其二，“小节重叠（Metric Elision: 4=1）”（前句收尾与后句起音在同一小节爆发，弱拍瞬转为强拍）；其三，“显式超拍重组”（如贝多芬 Op. 125 谐谑曲在四小节超拍与三小节超拍间自由切换）。此外，借助申克/卡普林的“重构还原检验法（Recomposition Test）”，严格区分了“内在扩充（Internal Expansion）”与“原生非对称超拍（Asymmetrical Phrase）”。
- **状态**：已成稿，待本批复读

---

## 1. 实际采用的资料范围与逐小节核对记录

- **底层机器可读原生谱源（Humdrum Kern 真实路径与逐小节核对）**：
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata03-1.krn`（贝多芬 Op. 2 No. 3 第一乐章 Allegro con brio）：
    - **mm. 1–4（呈示单元）**：mm. 1–2 基本乐思（十六分音符短颤音动机，超拍 1–2），mm. 3–4 属功能区重复基本乐思（超拍 3–4）；构成标准的 4 小节呈示单元；
    - **mm. 5–7（延续段推进）**：延续段启动，动机分裂，下属功能向属和弦推进（超拍 1–2–3）；
    - **m. 8（弱化终止与预期破灭）**：均整预期的第 8 小节（第 4 超拍）并未出现预期的 PAC，旋律在第 3 拍落在三音 $e$（形成 IAC），低音在第 3–4 拍展开下行三连音（C–G–F#–F–E–D）卸去终止冲力，造成句法悬置；
    - **mm. 9–10（延续段重读与 OMT 扩充）**：高低声部重新对唱延续段核心动机展开内在扩充；
    - **mm. 11–12（强力属准备）**：引入升 F 音离调加压；
    - **m. 13（迟到全奏闭合）**：全奏（$ff$）强奏达成迟到的 PAC，原本 8 小节乐句被和声与超拍错位扩张为 **13 小节**。

- **权威理论教材（Open Music Theory）**：
  * 本地路径：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/`（章节：`internalExpansions.md`）：
    - William Rothstein（1989）《Phrase Rhythm in Tonal Music》中“十九世纪四小节超拍暴政”的界定；
    - 内在扩充（Internal Expansion）、次乐句扩充（Sub-phrase Expansion）与规避终止（Evaded Cadence）；
    - 莫扎特 K. 309 第三乐章（回旋曲主题因 m. 15 导音逃逸导致规避终止，经 mm. 16–19 扩充至 19 小节）；
    - 莫扎特 K. 494（基本乐思内部单小节字面重复扩充）与 K. 515（5 小节原生非对称乐思）对比；
    - 重构还原检验法（Recomposition Test）：能否剔除插入单元还原为自洽 4 小节乐句作为判定扩充与否的唯一标准。

- **经典认知理论文献**：
  * Fred Lerdahl & Ray Jackendoff (1983)《A Generative Theory of Tonal Music》（GTTM）：度量规则（MPR）的等时节律预期与分组规则（GPR）的句法边界对位机制。

---

## 2. 正文位置与目录拓展

- **核心正文**：`content/techniques/rhythm/hypermeter-and-phrase-rhythm.md`
- **方向归属**：`techniques` 轴下的 `rhythm` 节奏方向。
- **与既有选题的严格分野与体系闭环**：
  * 与《海米奥拉》（`hemiola-and-metric-conflict.md`）：海米奥拉属于小节内微观脉冲或相邻两小节 3:2 的暂时二拍化对冲；本篇聚焦于跨小节的高层超节拍网格（1-2-3-4）与和声终止式之间的相位差与句法悬置；
  * 与《混合乐段》（`hybrid-themes-and-syntactic-decoupling.md`）：乐段研究聚焦于主题功能板块（题陈/延续/应答）的结构组装；本篇聚焦于时间重音流与终止预期的博弈机制。

---

## 3. 谱例占位与交付状态

正文内采用符合规范的真实作品、乐章与小节范围单行普通文本占位符：
1. **贝多芬《C大调第3钢琴奏鸣曲》Op. 2 No. 3 第一乐章 mm. 1–13**（句子型乐思弱化终止引发 13 小节巨型扩充）；
2. **莫扎特《C大调钢琴奏鸣曲》K. 309 第三乐章 mm. 1–19**（导音逃逸、规避终止与 OMT 扩充）。

暂无需另发加急 R 卡打扰谱例助手，保持单行文本占位即可通过验证。
