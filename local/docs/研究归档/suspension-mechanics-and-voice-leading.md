# 研究归档：对位中的挂留延留力学与声部导向机制

- **学者**：scholar-b2（接替 scholar-b）
- **选题**：对位中的挂留延留力学与声部导向机制（Suspension Mechanics and Voice-Leading Momentum）
- **中心论证**：挂留音绝非仅是局部的装饰性非和弦音，而是基于声部时钟微观相位差构建的核心对位张力发生器；它通过弱拍准备（协和）—强拍延留（重音不协和）—弱拍级进下行（势能释放）的三阶段动量闭环，打破多声部织体在块状和弦中的机械同步，并在 4–3、7–6、9–8（上方声部）与 2–3（低音声部）的空间拓扑、解决音重叠禁忌以及交响化半音和声链中驱动声部导向与终束力学。
- **状态**：`已成稿，待本批复读`

---

## 1. 实际采用的资料范围

- **权威对位法教材与理论规约（Open Music Theory）**：
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/fourthSpecies.md`：
    - 第四类切分对位法的严格律则、斜向进行、弱起准备、强拍重音不协和、弱拍单向下行级进解决；
    - 上方声部挂留（7–6、4–3、9–8）与低音声部挂留（2–3、5–6、4–5）的分类原则与力学差异；
    - 严禁连续 9–8 或 4–5 挂留以杜绝隐伏平行五八度，防范后拍五八度（After-beat Fifths/Octaves）。
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/embellishingTones.md`：
    - 挂留音（迟到）与切分音及先现音（早到）的本质力学解耦；
    - **解决音重叠禁忌（Resolution Doubling Taboo）**：除 9–8 挂留外，挂留音的解决音音高类别严禁在其他上方声部预先/同时叠置；
    - 反向延留音（Retardation）：向上级进解决的终束延留（如 7–8）。
  * `local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/voiceLeading-strict.md`：
    - 四部和声声部导向原则、倾向音必然解决律与声部交叉声学掩蔽。

- **现代学术文献与历史理论**：
  * Johannes Raiser (2018)《Beethovens Streichquartett op. 74》（ZGMTH，`local/resources/text/organized-html/beethoven-analysis-chamber/raiser-op74-galant-introduction-2018.md`，Lines 117–129）：
    - 贝多芬 Op. 74 第一乐章慢引子（Poco Adagio）mm. 18–24 的对位解构；
    - Emanuel Aloys Förster 通奏低音理论中的多重半音挂留（mehrfache Vorhaltsbildungen）与长达附点四分音符的长时值变音延留；
    - 解决和弦自身再度充当下一次属七/减七和弦挂留准备的连环悬置，以及大提琴作为挂留核心声部（Vorhaltsstimme）的功能反转。

- **底层机器可读原生谱源（Humdrum Kern）**：
  * `local/resources/scores/source-packages/humdrum/bach-370-chorales-main/bach-370-chorales-main/kern/chor096.krn`（BWV 87/7, "Jesu, meine Freude"）：
    - Lines 22–36（mm. 1–2）：女低音在 m. 1 拍 4 准备 D4，跨小节线延留至 m. 2 强拍，在低音 A 上形成四度重音挂留，弱拍下行级进解决至导音升 C4，完成典范 $V^{4-3}$ 半终止；
  * `local/resources/scores/source-packages/humdrum/bach-370-chorales-main/bach-370-chorales-main/kern/chor001.krn`（BWV 269, "Aus meines Herzens Grunde"）：
    - Lines 43–54（mm. 5–7）：第 6 小节女低音保持二分音符 G4，第 3 拍低音切入属音 D3 形成 $4–3$ 挂留并下行解决至升 F4，在第 7 小节闭合完全正格终止（PAC）；
  * `local/resources/scores/source-packages/humdrum/bach-370-chorales-main/bach-370-chorales-main/kern/chor216.krn`（BWV 60/5, "Es ist genug!"）：
    - Lines 19–39（mm. 1–4）：开篇女高音三全音全音阶跳升（A-B-C#-D#）与 m. 3 低音 9 音八度半音下行（Passus Duriusculus），与上方声部还原 D 挂留交织成极端复调张力网。

---

## 2. 正文位置与目录拓展

- **核心正文**：`content/techniques/counterpoint/suspension-mechanics-and-voice-leading.md`
- **目录实质导论**：`content/techniques/counterpoint/index.md`（开辟 techniques 轴下全新的 counterpoint 对位法顶层方向）
- **顶层索引更新**：`content/techniques/index.md`（纳入对位法方向并阐释其核心问题，将“尚未成文的方向”收敛为仅余节奏轴）

---

## 3. 谱例占位与交付状态

正文严格遵守工程纪律，在初期未编码状态下绝不使用空的 `lilypond` 围栏，全部采用包含真实作品、乐章、准确小节范围、声部编制与 GM 编号的文本规范占位：
1. **J. S. 巴赫：四部合唱《Jesu, meine Freude》BWV 87/7，mm. 1–3**（SATB 四部，GM 52）
   - 实证事实：女低音 D4-C#4 经典 4–3 挂留与属功能半终止闭合。
2. **J. S. 巴赫：四部合唱《Aus meines Herzens Grunde》BWV 269，mm. 5–7**（SATB 四部，GM 52）
   - 实证事实：女低音 G4-F#4 紧凑挂留，配合低音属音跳进达成完全正格终止（PAC）。
3. **J. S. 巴赫：四部合唱《Es ist genug!》BWV 60/5，mm. 1–4**（SATB 四部，GM 52）
   - 实证事实：三全音横向音程轮廓、低音八度半音下行（Passus Duriusculus）与高声部还原 D 挂留冲突。
4. **L. v. 贝多芬：降E大调第10弦乐四重奏 Op. 74 第一乐章 Poco Adagio，mm. 18–24**（弦乐四重奏，GM 40/40/41/42）
   - 实证事实：多重半音挂留、长时值附点四分音符延留、解决和弦连锁悬置与大提琴作为挂留核心声部的功能反转。

*交付状态*：已在 task-26 S 卡与正文中明确界定，待后续统一向谱例助手下发 R 卡进行代码编码与独立逐音核验。

---

## 4. 未解决的缺口与局限

- **当前缺口**：四处谱例均以严格规范的文本引用块占位，待后续谱例助手完成 LilyPond 2.26.0 代码交付与独立核验后做无缝替换。
- **学术局限**：本篇聚焦于四部合唱与室内乐四重奏中基于大小调与半音化体系的挂留对位力学，尚未涵盖文艺复兴早期若斯坎经文歌中的五至六部高密度复调网络（如若斯坎 JRP 原生谱源中频繁出现的下行切分重叠与兰迪尼终止），留待 counterpoint 轴后续专题拓展。
