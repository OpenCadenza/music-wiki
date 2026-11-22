# 研究归档：调式交替

- **学者**：scholar-b4
- **选题**：同主音大小调借用与色彩句法（Modal Mixture and Color Syntax in Classical Harmony）
- **中心论证**：同主音大小调借用（Modal Mixture / Borrowing）是古典主义至早期浪漫主义在维系单一调性中心前提下拓展和声色彩幅度的最核心机制。其声学物理基石在于同主音大小调共享相同的 $\hat{1}, \hat{5}, \hat{4}$ 纯音程骨架，其最关键的动量源泉在于降 6 级音（$\flat\hat{6}$）对属音（$\hat{5}$）所产生的强力向下半音倾泻引力。严格区分“借和弦”与“转调”：只要目标和弦缺乏确立新调地位的结构性终止式（PAC/HC），所有借用和弦（如 $\text{iv}, \flat\text{VI}, \flat\text{III}, \flat\text{VII}, \text{ii}^{\circ 7}$）均严格被主调的自然功能区（如 $[\text{S4}], [\text{Tx-6}]$）所吸收，主音引力中心自始至终未发生实质偏移。贝多芬的创作实践表明，调式交替既能在局部提供强烈的光影阴暗对比（如 Op. 13 慢乐章 mm. 41–51 降 a 小调突变与大三度光辉复苏），又能在尾声充当阻碍终止与戏剧性蓄能的宏大断崖（如 Op. 2 No. 3 尾声 mm. 218–232 的 $\flat\text{VI}$ 级和弦），更能在宏观奏鸣再现部中充当远关系三度调性平滑重返主调的“调性枢纽”（如 Op. 53 再现部 mm. 196–206 A 大调经 A 小调无缝回归 C 大调）。
- **状态**：已成稿，待本批复读

---

## 1. 实际采用的资料范围与逐小节核对记录

- **底层机器可读原生谱源（Humdrum Kern 真实路径与逐小节核对）**：
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata08-2.krn`（贝多芬 Op. 13 第二乐章 Adagio cantabile）：
    - **m. 41**：主调降 A 大调（$A\flat$ major）中，第一插部收束后，低音击出大字一组 $A\flat$，三连音伴奏突然引入小三度降音 $c\flat$ 与 $e\flat$（同主音降 a 小调小主和弦 $\text{i} = A\flat\text{–}C\flat\text{–}E\flat$），旋律于 $a\flat \to c\flat \to b\flat \to a\flat$ 间哀伤回旋；
    - **mm. 48–50**：降 a 小调内声部引入含减五度与降六级音的导和弦，并在 m. 50 凝聚为属七和弦 $E\flat^7$；
    - **m. 51**：强拍高声部在一片静谧（$p$）中轻柔敲出还原大三度音 $c\natural$（C-natural），低音同步降落在降 A 大调主和弦上，完成从同主音小调深渊向明亮大调神圣升华的经典调式复苏。
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata03-1.krn`（贝多芬 Op. 2 No. 3 第一乐章 Allegro con brio）：
    - **m. 218**：快板尾声（Coda）十六分音符分解琶音奔涌而下，和声收束于 G 大调纯属和弦（$V$）；
    - **mm. 219–224（降六级阻碍突变）**：出人意料地未解决至 C，而是在强音（$ffp$）中轰然敲下低音 $A\flat$（连音线保持）与右手 $c\text{–}e\flat\text{–}a\flat\text{–}c$——借用 c 小调的降六级大三和弦 $\flat\text{VI}$（$A\flat$ major triad）；低音 $A\flat$ 持续长达 6 小节，右手在降 A 大调三和弦分解音型中静止回旋，制造惊心动魄的戏剧悬念；
    - **mm. 225–232**：低音平滑滑向导七和弦，并于 m. 232 顺利交接给原调终止四六和弦 $I^6_4$ 与华彩段（Cadenza）。
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata21-1.krn`（贝多芬 Op. 53 第一乐章 Allegro con brio）：
    - **mm. 196–201**：再现部第二主题在远关系 A 大调（VI 级）呈现，随后半终止停顿；
    - **mm. 202–203**：第 202 小节强拍伴奏与旋律的三音 $c\sharp$ 骤然降为自然音 $c\natural$，乐句毫无滞涩地切换入 A 小调（a minor，同主音交替）；
    - **mm. 204–206**：由于 A 小调自然音列与主调 C 大调完全共用，低音顺势在 m. 204 滑向属音 $G$，于 mm. 205–206 天衣无缝地在主调 C 大调上重组再现第二主题。

- **权威理论教材（Open Music Theory）**：
  * 本地路径：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/`（章节：`modalMixture.md`、`appliedChords.md`、`Modulation.md`）：
    - 同主音大小调借用的声学概念与音阶基础；
    - 借和弦（Modal Mixture）与结构转调（Modulation）的严格判界：以目标调是否出现 PAC/IAC/HC 为唯一标准；
    - 罗马数字与功能低音标记规约：未改变根音时保留原级数并修改和弦性质（如 $\text{iv}$ 标记为 $[\text{S4}]$ 代替 $\text{S4}$），改变根音时前加变音记号（如 $\flat\text{VI}$ 标记为 $[\text{Tx-6}]$）；
    - 皮卡迪三度（Picardy Third）的历史演进与小调神圣升华意义。

---

## 2. 正文位置与目录拓展

- **核心正文**：`content/techniques/harmony/modal-mixture-and-color-syntax.md`
- **方向归属**：`techniques` 轴下的 `harmony` 和声方向。
- **与既有选题的严格分野与体系闭环**：
  * 与《那不勒斯和弦》（`neapolitan-chord-structural-mutation.md`）：那不勒斯和弦专论降 II 级原位/六和弦变异及其作为专职下属准备的半音叹息；本篇聚焦于同主音自然音阶借用体系本身；
  * 与《增六和弦》（`augmented-sixth-mechanics-and-syntactic-drift.md`）：增六和弦专论双向半音反向扩张锁定属音的特殊音程力学；本篇聚焦于三和弦/七和弦常规三度叠置下的调式光影折射；
  * 与《三度调性》（`chromatic-mediant-and-tonal-space.md`）：三度调性专论跨越乐段与宏观奏鸣调区的独立调性空间迁徙；本篇聚焦于乐句内部的调式色彩借用（无新调终止式，主音中心保持）。

---

## 3. 谱例占位与交付状态

正文内采用符合规范的真实作品、乐章与小节范围单行普通文本占位符：
1. **贝多芬《C小调第8钢琴奏鸣曲“悲怆”》Op. 13 第二乐章 mm. 41–51**（同主音降 a 小调突变、导和弦加压与大调光彩复苏）；
2. **贝多芬《C大调第3钢琴奏鸣曲》Op. 2 No. 3 第一乐章 mm. 218–232**（快板尾声降六级大三和弦 $\flat\text{VI}$ 阻碍终止代换与戏剧蓄势）；
3. **贝多芬《C大调第21钢琴奏鸣曲“华德斯坦”》Op. 53 第一乐章 mm. 196–206**（再现部远关系 A 大调经同主音 A 小调交替回归 C 大调的枢纽调解）。

暂无需另发加急 R 卡打扰谱例助手，保持单行文本占位即可通过验证。
