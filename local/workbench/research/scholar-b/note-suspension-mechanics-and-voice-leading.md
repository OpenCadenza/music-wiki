# 研究笔记：对位中的挂留延留力学与声部导向机制

> 研究者：scholar-b2（接替 scholar-b）  
> 日期：2026-11-16  
> 目标文章：`content/techniques/counterpoint/suspension-mechanics-and-voice-leading.md`  
> 目录导论：`content/techniques/counterpoint/index.md`  
> 关联任务：task-26（S 卡）

---

## 1. 实际阅读的资料与谱源定位

本课题围绕复调对位中的时间错位与声部导向核心机制展开，直接结合教材规约、理论文献与底层机器可读原生谱源（Humdrum Kern）：

### A. 权威对位教材与理论规约
1. **Open Music Theory (OMT)**：
   - `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/fourthSpecies.md`：
     * 第四类对位法（Fourth-Species Counterpoint）的严格律则：二声部通过半音符跨小节线切分延留，形成斜向进行（Oblique Motion）；
     * 挂留音三阶段闭环：弱拍准备（Preparation，协和） $\to$ 强拍挂留（Suspension，重音不协和） $\to$ 弱拍级进下行解决（Resolution，协和）；
     * 上方声部挂留分类：`7–6`、`4–3`、`9–8`；
     * 低音声部挂留分类：`2–3`、`5–6`、`4–5`（其中 `2–3` 为核心低音不协和挂留）；
     * 禁用连续的 `9–8` 或 `4–5` 挂留（避免第一类对位中的平行五八度），警惕“后拍五八度”（After-beat Fifths/Octaves）；
     * 终束规约：低音必为 $re-do$（2-1级），上方声部以 $do-ti$ 构成 `7–6` 挂留，或低音以 `2–3` 挂留解决。
   - `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/embellishingTones.md`：
     * 挂留音（Suspension）与切分音（Syncopation）及先现音（Anticipation）的本质区别：先现音是“早到”，挂留音是“迟到”；
     * **解决音重叠禁忌（Resolution Doubling Taboo）**：“除 9–8 挂留外，解决音的音高类别绝不可在挂留音发声的同时出现在其他任何上方声部中”；
     * 反向延留音（Retardation）：向上级进解决的延留音（常见于终束导音上行至主音，如 7–8）。
   - `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/voiceLeading-strict.md`：
     * 四部和声声部导向原则、倾向音（Tendency Tones）必然解决律与声部交叉声学掩蔽。

2. **现代学术分析文献**：
   - Johannes Raiser (2018)《Beethovens Streichquartett op. 74: Der erste Satz und Emanuel Aloys Försters 'Anleitung zum Generalbaß'》（ZGMTH，`local/resources/text/organized-html/beethoven-analysis-chamber/raiser-op74-galant-introduction-2018.md`）：
     * Lines 117–129：贝多芬 Op. 74 第一乐章慢引子（Poco Adagio）mm. 18–24 的对位解构；
     * 指出贝多芬突破传统自然音图式，引入高度不协和的“多重半音挂留”（mehrfache Vorhaltsbildungen）与长达附点四分音符时值的半音延留；
     * 解决和弦自身再度充当下一次属七/减七和弦的挂留准备（连锁悬置）；
     * 大提琴在引子末尾反转成为承担挂留的核心声部（Vorhaltsstimme）。

### B. 机器可读原生谱源（Humdrum Kern）
1. **J. S. 巴赫 370 首四部合唱（Humdrum `bach-370-chorales-main`）**：
   - `chor096.krn`（BWV 87/7, "Jesu, meine Freude", d小调）：
     * Lines 22–36（mm. 1–2）：女低音（Alto）在第 1 小节第 4 拍发声 D4（四分音符，与下属和弦协和），跨小节线延留至第 2 小节强拍，与低音 A3 构成减/纯四度重音不协和挂留；在第 2 拍弱拍下行级进解决至升 C4（导音），构成主调属和弦（$V^{4-3}$），驱动半终止收束。
   - `chor001.krn`（BWV 269, "Aus meines Herzens Grunde", G大调）：
     * Lines 43–54（mm. 5–7）：女低音在第 6 小节前两拍持续保持 G4（二分音符），第 3 拍低音进入属音 D3，G4 与 D3 碰撞形成明晰的 `4–3` 挂留，并在弱拍下行解决至升 F4，严丝合缝闭合完全正格终止（PAC）。
   - `chor216.krn`（BWV 60/5, "Es ist genug!", A大调）：
     * Lines 19–39（mm. 1–4）：开篇女高音（Soprano）以三个连续全音大二度跳升（A4-B4-C#5-D#5，构成三全音轮廓），第 2 小节以重音顿挫在减五度/增四度音响上；
     * 第 3 小节低音展开长达 9 个音级的八度半音阶下行（$C\sharp \to B \to A \to G\sharp \to F\sharp \to E \to D \to C\sharp \to B$），低音声部与上方持续音密集交错，第 4 拍女高音还原 D（`4ddnX`）以挂留不协和刺破和声，最终在第 4 小节释放至主和弦。

---

## 2. 事实三维辨析：资料说了什么、谱面显示什么、自己如何推导

### A. 资料与教材规约说了什么（Theory & Rules）
- **时序三阶段**：准备必须协和、挂留必须处于强拍或重音拍位、解决必须下行级进；
- **音程类型学**：上方声部对低音为 7–6、4–3、9–8；低音挂留为 2–3；
- **严禁提前叠置解决音**：除 9–8 外，严禁在其他上方声部中预先包含解决音。若高音区已有解决音，挂留音的下行解决将失去“发现新音”的声学必要性，且在发声瞬间会形成极度混浊的同名音小二度/九度干扰。

### B. 谱面实际显示什么（Score Evidence）
1. **巴赫《Jesu, meine Freude》BWV 87/7（`chor096.krn`）**：
   - 谱面确切记录：
     * m. 1 拍 4：Bass=A, Tenor=d, Alto=d, Soprano=f（d小调 i 级和弦）；Alto 的音高为 D4；
     * m. 2 拍 1：Bass 走向 A3，Tenor 跳向 A3（随后带 Bb 经过音），Soprano 跳向高音 E5；而 Alto **原封不动延留 D4**！
     * 在拍 1 上，低音是 A，上方音是 A、D、E。D 与 A 构成四度，属于不协和音程；
     * m. 2 拍 2：Alto 下行半步级进至 C#4，与低音 AA2 构成大三度，与 Soprano 的 E 构成纯五度，完成标准的 A 大调属三和弦构建。
2. **巴赫《Aus meines Herzens Grunde》BWV 269（`chor001.krn`）**：
   - 谱面确切记录：
     * m. 6 拍 1–2：Alto 为二分音符 `2g`；Bass 在拍 1 为 BB、拍 2 为 C；
     * m. 6 拍 3：Bass 坚决切入属音 D3（`4D`）；此时 Alto 仍保持 G4，与 D3 形成四度摩擦；
     * 紧随其后在拍 3 的后半拍/拍位内，Alto 级进下行至 `4f#`（升F4），与 Soprano 的 A4 汇合，将紧张的属和弦能量导入 m. 7 的主音 G。
3. **巴赫《Es ist genug!》BWV 60/5（`chor216.krn`）**：
   - 谱面记录了突破常规的极端对位：
     * 旋律打破“下行解决”的平滑预期，直接以包含三全音的全音阶攀升呈示；
     * 第 3 小节低音以十六分与八分音符实施长达一个八度的半音阶下行，高音区与中音区通过切分挂留音与下行半音形成多重摩擦网络；
     * 挂留不仅发生在单一声部，而是多声部在相位差上的连续推挤。
4. **贝多芬 Op. 74 Poco Adagio（Raiser 2018 分析，Kern `quartet10-1.krn`）**：
   - 慢引子 mm. 18–24 中，贝多芬将巴赫式的四部挂留提升为交响化的四重奏声学摩擦：
     * 解决音不再落入协和三和弦，而是解决到带有减七度或增六度特征的紧张和弦；
     * 低音声部（大提琴）从被动承受挂留的基座，转化为主动延留挂留音的核心旋律线。

### C. 自己的理论推导与归纳（Synthesis & Theoretical Insights）

1. **挂留音的本质：声部微观时间错位（Phase Shift Engine）**
   - 音乐如果只有垂直对齐的柱式和弦（Block Chords），听觉会迅速产生疲劳，因为所有声部在同一时钟节拍上重置；
   - 挂留音的力学本质是**打破均质时钟**：当和声列车驶入下一站时，故意将一个声部“扣留在旧车站”，制造强烈的结构拉扯力；当它在弱拍终于“赶上列车”时，和声的重力势能才得以释放。
2. **音程类型的力学阶梯**：
   - `4–3 挂留`：**功能性王者**。4度到3度直接定义了三和弦的色彩属性（尤其在属和弦上，4度延留主音，解决至导音，直接触发终止力学）；
   - `7–6 挂留`：**线性推进者**。7度到6度的解决具有天然的顺畅感，最适合组织长线条的连续下行模进链（Sequential Chains）；
   - `9–8 挂留`：**纯净共鸣的重置**。9度到8度是从极度扩张收缩至同音八度，赋予听觉一种神圣、肃穆的归宿感；
   - `2–3 低音挂留`：**重力颠覆者**。常规挂留是“上方悬挂”，低音挂留是“地基塌陷”。低音自身承担不协和延留并在弱拍下坠，打破低音稳固常态，产生巨大的下沉张力。
3. **解决音重叠禁忌的声学机理（Acoustic Masking）**：
   - 为何古典规约严禁在其他上方声部预置解决音？
     * 声学上，若上方声部已存在解决音 $X$，而挂留声部延留的是 $X+1$ 或 $X+2$，此时在强拍听到的不仅是挂留张力，而是两个声部之间未经缓冲的小二度或大七度粗糙摩擦；
     * 心理声学上，解决音的预先出现会削弱弱拍“到达新音”的惊喜感与释然感。

---

## 3. 对现代创作与生成式 Agent 的启示

1. **摆脱“块状和弦（Block Chords）”的死穴**：
   - 许多 AI 音乐生成模型生成的伴奏织体往往缺乏生命力，根源就在于声部垂直切片的绝对同步；
   - 引入挂留对位管道：为特定声部注入 1/2 或 1/4 拍的时钟相位差（Phase Shift），强制实施“弱拍准备 $\to$ 强拍挂留 $\to$ 弱拍解决”，立即使织体获得巴洛克式的复调流动性。
2. **终止式强化公式（The Cadential Suspension Pattern）**：
   - 在任何正格终止（PAC）或半终止（HC）前夕，严格配置属和弦的 $4–3$ 挂留，使主音在属和弦强拍形成挂留延留，再于弱拍解决至导音，这是构建权威古典终束感不可或缺的物理开关。
3. **低音动态化策略（Bass Inversion & Suspension）**：
   - 不要将低音仅作为根音跳进的工具；适度引入 $2–3$ 低音挂留，让低音参与复调歌唱，赋予和声从地基深处发出的律动张力。

---

## 4. 实施规划

- 编写实质目录导论：`content/techniques/counterpoint/index.md`；
- 编写核心学术正文：`content/techniques/counterpoint/suspension-mechanics-and-voice-leading.md`；
- 撰写研究归档：`local/docs/研究归档/suspension-mechanics-and-voice-leading.md`；
- 创建成稿 A 卡；
- 运行工程校验 `node scripts/validate-content.mjs`；
- 向 lead 汇报交付成果。
