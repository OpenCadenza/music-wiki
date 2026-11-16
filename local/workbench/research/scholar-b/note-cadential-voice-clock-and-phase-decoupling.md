# 研究笔记：巴赫众赞歌终止式的声部时钟与相位解耦机制

> 研究者：scholar-b2  
> 日期：2026-11-16  
> 目标文章：`content/composers/bach/chorale/cadential-voice-clock-and-phase-decoupling.md`  
> 目录导论：`content/composers/index.md`、`content/composers/bach/index.md`、`content/composers/bach/chorale/index.md`  
> 关联任务：task-34（S 卡）

---

## 1. 实际阅读的资料与谱源定位

### A. 理论教材与分析文献
1. **Open Music Theory (OMT)**：
   - `cadenceTypes.md`：
     * 正格终止（PAC / IAC）、半终止（HC）、阻碍终止（Deceptive Cadence）与弗里吉亚终止（Phrygian Half Cadence）的形式化界定；
     * 终止的核心功能：和声张力到达顶峰后向稳定态的坍缩与结构标点；
   - `embellishingTones.md`：
     * 先现音（Anticipation, ANT）：提前于和声变换发声的非和弦音，专用于乐句与大型曲式边界；
     * 挂留音（Suspension, SUS）：滞后于和声变换的非和弦音，制造强拍重音摩擦；
   - `fourthSpecies.md`：
     * 终止式的终极声部走向：上方声部 $do-ti-do$（带 7–6 挂留）或低音 $re-do$（带 2–3 挂留）。

### B. 机器可读底层谱源（Humdrum Kern）
1. `local/resources/scores/source-packages/humdrum/bach-370-chorales-main/bach-370-chorales-main/kern/chor001.krn`（BWV 269，G大调）：
   - Lines 35–41（mm. 3–4）：女高音在第 3 小节第 3 拍后半拍提前进入八分音符 $A4$（`8a`），先于强拍半终止属和弦到达，构成标准的先现音时钟先到；
2. `local/resources/scores/source-packages/humdrum/bach-370-chorales-main/bach-370-chorales-main/kern/chor002.krn`（BWV 347，A大调/E半终止）：
   - Lines 41–48（mm. 3–4）：女低音在第 3 小节第 3 拍以二分音符切入 $E4$（`[2e`），跨小节线延留至第 4 小节强拍（`4e]`），在低音属音 $B2$ 上制造 $4–3$ 挂留，延迟整整一拍至第 2 拍才解决至升 $D4$（`4d#`）；
3. `local/resources/scores/source-packages/humdrum/bach-370-chorales-main/bach-370-chorales-main/kern/chor010.krn`（BWV 38/6，a小调/弗里吉亚）：
   - Lines 87–93（mm. 12–13）：女高音在第 13 小节下拍便以全音符 $E4$（`1e;`）提前落地锚定，持续整整 4 拍；下方三声部在其下方完成导七和弦—阻碍三和弦—E大调主和弦的二次对位收束；
4. `local/resources/scores/source-packages/humdrum/bach-370-chorales-main/bach-370-chorales-main/kern/chor021.krn`（BWV 153/5，a小调）：
   - Lines 39–43（mm. 3–4）：第 4 小节下拍 a 小调完全正格终止，声部精确记录为低音 $A2$、次中音 $A3$、女低音 $C4$、女高音 $A4$；五音 $E$ 被彻底省略，形成“三倍根音 + 单三音”的极致留白配置。

---

## 2. 三维事实辨析：资料说了什么、谱面显示什么、自己如何推导

### A. 资料与教材规约（Rules）
- 传统四部和声教材往往要求和弦“完整”（四音齐全：根、三、五、七），但在终止式中允许省略五音；
- 规则禁止平行五八度、禁止反向五八度、要求导音（第 7 级）必须上行解决至主音（第 1 级）、要求下属七和弦或属七和弦的第七音必须下行级进解决至三音。

### B. 谱面实际显示什么（Score Evidence）
1. **时钟先到：`chor001.krn` mm. 3–4**：
   - 谱面确切记录：m. 3 拍 3 期间，Bass 为 G，Tenor 为 d，Alto 为 g；Soprano 原为附点四分音符 g（`4.g`），但在拍 3 的后半拍突然切入 `8a`！
   - 下一小节 m. 4 拍 1 即为半终止的 D 大调属和弦（Bass=D, Tenor=d, Alto=f#, Soprano=a）；
   - Soprano 的 A 音比其他三个声部**提前了整整半个四分音符拍位**到达！
2. **时钟滞后：`chor002.krn` mm. 3–4**：
   - 谱面确切记录：m. 4 拍 1，Bass 已经踩下属音 $B2$（`4B`），Soprano 踩在 $G\sharp 4$（`4g#`），Tenor 保持 $B3$；
   - 此时 Alto 保持由前一小节延留下来的 $E4$（`4e]`），在强拍构成尖锐的四度不协和；
   - 直到拍 2，Alto 才下行半音解决至导音升 $D4$（`4d#`）；Soprano 则在拍 2 降至 $F\sharp 4$；
   - 在拍 3，全四部才同时落入带延长记号的 E 大调和弦。Alto 故意“迟到了一整拍”！
3. **旋律锚定与底层多步调性漂移：`chor010.krn` mm. 12–13**：
   - Soprano 在 m. 13 整个小节只有唯一一个音：全音符 $E4$（`1e;`）；
   - 下方三声部的时钟完全独立运作：拍 1 为升 G 减三和弦第一转位（`4GG# 4B 4d]`），拍 2 为 a 小调三和弦（`4AA 4A 4c`），拍 3–4 才落地至 E 大调（`2EE; 2G#X; 2B;`）；
   - 旋律与和声彻底解耦：旋律早已在终点等候，而底层和声经历了二次转折才最终到达。
4. **终止留白与三倍根音：`chor021.krn` mm. 3–4**：
   - m. 4 落地和弦：低音 $A2$（`2.AA;`）、次中音 $A3$（`2.A;`）、女高音 $A4$（`2.a;`）、女低音 $C4$（`2.c;`）；
   - 为什么五音 $E$ 绝不能出现？
     * 若次中音从 m. 3 拍 4 的导音 $G\sharp 3$ 跳向 $E3$，则导音未解决，破坏声部导向；
     * 若女低音从 m. 3 拍 4 的属七音 $D4$ 跳向 $E4$，则七音未下行解决，严重违规；
     * 若女高音由 $B4$ 跳向 $E4$ 或 $E5$，则旋律线失去了平滑的级进落音。
     * 因此，**线性声部导向的独立性与严密性，彻底压倒了垂直和弦音完整的静态偏好**！

### C. 理论归纳：巴赫众赞歌终止声部时钟四相模型（The 4-Phase Cadential Clock Model）

```
阶段 1: 触发与时值紧缩 (Metric Diminution)
  └─► 低音声部从四分音符提速为八分音符折返或跳进，充当终止发令枪；
阶段 2: 旋律先到锚定 (Early Arrival / Anticipation)
  └─► 女高音通过先现音提前半拍落入目标音，或以全音符提前锚定终束；
阶段 3: 内声部延迟解决 (Suspension & Delayed Phase)
  └─► 女低音/次中音保持 4–3 或 7–6 挂留，故意滞后半拍至一拍，维系前行张力；
阶段 4: 根音落地与声学留白 (Acoustic Clearance / Triple Root)
  └─► 延长记号降临，严格遵循倾向音解决，省略五音，以三倍根音+单三音消除混响浑浊。
```

---

## 3. 对现代创作与生成式 Agent 的启示

1. **规避“四声部同时刹车”的呆板死穴**：
   在自动化合唱生成中，切忌让 SATB 四个声部在小节强拍垂直同步进入终止主和弦。必须引入**声部时钟解耦机制**：让旋律声部先现（提前半拍）或内声部挂留（滞后半拍），使终止呈现为波浪式的交错到达。
2. **终止落地“五音留白”法则（The Incomplete Triad Rule at Cadences）**：
   在评估或生成终止式时，不要对“缺少五音的和弦”进行扣分。相反，当导音与七音均遵循严格声部导向时，必须优先接受“三倍根音 + 单三音”的完美终结形态。
3. **低音脉冲倍增器（Bass Momentum Injector）**：
   在终止前倒数第二小节，将低音节奏细分密度提高一倍（从四分音符切换为八分音符），利用低音的时值紧缩（Diminution）形成强大的终止向心引力。
