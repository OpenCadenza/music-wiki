# 研究归档：管弦乐织体中的音响平面与分层机制

- **学者**：scholar-c
- **选题**：管弦乐织体中的音响平面与分层机制（Planes of Tone Layering）
- **中心论证**：配器的实质并非在声部写定后机械指派音色，而是利用音响平面理论，通过控制音区距离、起音包络、泛音结构与节奏密度，构建前景旋律、背景运动与背景共鸣的三层听觉场景，从声学机制上规避声学遮蔽并防止织体塌陷为同质沉重全奏。
- **实际采用的资料范围（严格限制在本地真实研读文献）**：
  - Alan Belkin: *Artistic Orchestration* (`local/resources/text/ocr/alan-belkin/bk-O-O/bk-O-O.md`)：
    - "Preliminary Considerations" (pp. 3–11，第 101–220 行)：管弦乐各家族特性、木管异质三音区、古典/里姆斯基-科萨科夫式交错（overlapping）与包围（enclosure）手法（第 161–172 行）；
    - "Planes of Tone" (pp. 39–44，第 760–877 行)：音响平面的界定；单焦点听觉注意力边界（第 785 行）；最高声部感知优先级（第 707 行）；前景凸显条件（第 809–811 行）；平面内融合条件、平面间区分条件；运动平面的 4 种形态（第 821–845 行）与共鸣平面的声学特征；
    - "Contrapuntal Orchestration" & "The Tutti" (pp. 46–50，第 895–959 行)：对位配器平衡、起奏强化（marking entries）、持续尾音（trailers）防干涩（第 915–920 行）、全奏独立家族型与要素分配型织体。
  - Philharmonia Orchestra 乐器学档案 (`local/resources/text/organized-html/philharmonia/instruments/`)：
    - `horn.md`：圆号在中景作为谐和填充（Harmonic filling）与管弦乐长音粘合剂的核心功能；
    - `oboe.md`：双簧管的频段特征（233 Hz – 1.6 kHz）、高穿透力及其在木管和弦中的破坏融合变数。
- **正文位置**：
  - 主要正文：`content/techniques/sound/planes-of-tone-layering.md`
  - 目录实质索引：`content/techniques/sound/index.md`
- **谱例现状与占位清单**：
  - 贝多芬《第五交响曲》Op.67 第二乐章（Andante con moto），mm. 205–218（大管前景旋律 + 弦乐轻跳反复音伴奏，声部摘录占位）；
  - 勃拉姆斯《第三交响曲》Op.90 第三乐章（Poco allegretto），mm. 1–12（大提琴歌唱性前景 + 小提琴摇摆琶音伴奏 + 圆号/管乐长音和声垫，声部摘录占位）；
  - 瓦格纳《纽伦堡的名歌手》序曲，mm. 42–50（管乐庄严和弦旋律 + 弦乐疾速音阶跑动动能平面，声部摘录占位）；
  - 谱例制作流水线：已由 lead 派发给专职谱例助手 `assistant-scores-b` 执行（关联 `task-6`），当前在正文中以文本引用块规范占位，不采用空 `lilypond` 围栏，确保构建脚本零报错。
- **引证与工程校验修正记录（根据 lead 审查意见）**：
  1. 剔除未经本地建档的外部心理学文献（Bregman）引用，论证全面收敛并扎根于 Belkin 原文（第 785、707、809–811 行）；
  2. 修正里姆斯基-科萨科夫手法表述为“贝尔金所述的古典/里姆斯基-科萨科夫式做法”（第 161–172 行），避免拔高为定律；
  3. 将 3 处占位块统一调整为普通文本块，经 `node scripts/validate-content.mjs` 实测，本篇正文与索引全部零报错通过。
- **状态**：`已成稿，待本批复读`
