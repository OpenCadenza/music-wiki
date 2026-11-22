# 研究归档：平行五八度

- **学者**：scholar-b4
- **选题**：平行五八度的声部独立性禁则与色彩解放（Parallel Fifths and Octaves: From Counterpoint Prohibition to Color Liberation）
- **中心论证**：平行纯五度（$P5 \to P5$）与纯八度（$P8 \to P8$）在严格对位中的禁则根植于泛音列的高度声学融合（Tonal Fusion）。两声部做同向纯音程平移时，上方线条会被下方线条的泛音场所吸附，人耳心理声学流将其合并为单一声部，导致多线条独立性瞬间坍塌（四部坍塌为三部）。然而，古典与浪漫实践系统性打破了这一教条：首先，申克式的“对位声部”与“器乐织体加倍”（如 Op. 53 开篇低音空五度脉动与和弦移位、Op. 13 快板低音八度震音脉动）建立了关键的声学分水岭；其次，“莫扎特五度”（德意增六解决中的 $d5 \to P5$）与“圆号五度”（Op. 81a 开篇自然泛音猎号呼应与阻碍终止）在古典传统中开辟了合法的声部解脱缝隙；最终，肖邦的民俗空心低音、贝多芬晚期 Op. 132 利底亚圣咏中奥尔加农式的纯音程复古，以及德彪西的印象主义音响板块，彻底将平行五度从负面语法失误解放为纯粹的现代音色画笔。
- **状态**：已成稿，完成第二轮中期复读返修

---

## 1. 实际采用的资料范围与逐小节核对记录

- **底层机器可读原生谱源（Humdrum Kern 真实路径与逐小节核对）**：
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata21-1.krn`（贝多芬 Op. 53 第一乐章 Allegro con brio）：
    - **mm. 1–4**：左手低音在极弱（$pp$）中以八分音符持续敲击大字组 $C$ 与 $G$ 的空五度（$C2+G2$），右手以小字组十度/三度音程（$C3+E3$）同步跳动；随后在 mm. 5–8 和弦整体下移大二度至降 B 和弦，左手低音为大字一组降 $B$ 与大字组 $F$（$B\flat 1+F2$）的空五度脉动，右手加入小字组 $B\flat$ 与 $D$；核实其为单一结构线条与交响化低音支架的和弦性脉动与色彩移位，而非对位声部间的平行五八度失误；
    - **m. 22**：贝多芬采用意大利增六和弦（$C\text{–}E\text{–}A\sharp$）替代德意志增六和弦，直接剔除第 5 级音，从声部根源上消除五度对偶。
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata26-1.krn`（贝多芬 Op. 81a 第一乐章 Adagio）：
    - **mm. 1–2（“告别”动机圆号五度）**：上方声部 $g \to f \to e\flat$；下方声部 $e\flat \to B\flat \to G$；大三度 $\to$ 纯五度（$B\flat\text{–}f$，上方二度级进符合隐伏五度容许条件）$\to$ 小六度（$G\text{–}e\flat$）；第二小节低音突入大字一组与大字组 $CC\text{–}C$，配合构成 C 小调阻碍终止，核实圆号自然泛音列在古典器乐中的诗学隐喻；
    - **mm. 3–6**：号角动机展开半音悬留与模进。
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata08-1.krn`（贝多芬 Op. 13 第一乐章 Allegro molto e con brio）：
    - **mm. 11–20**：快板主部左手长达十余小节的大字一组与大字组 $CC\text{–}C$ 八度震音脉动（Tremolo），核实交响化钢琴低音加倍的声学功能。
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet15-3.krn`（贝多芬 Op. 132 第三乐章 Molto adagio）：
    - **mm. 1–30**：F 利底亚调式无导音圣咏织体中四件弦乐器以纯五度、纯八度与六度为主的纯朴纵向对位与反向并置，以及第 31 小节起 D 大调“感受新力量”器乐织体对比。

- **权威理论教材（Open Music Theory）**：
  * 本地路径：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/`（章节：`motionTypes.md`、`firstSpecies.md`）：
    - 四种对位运动类型（平行、隐伏/同向、反向、斜向）的定义与层级；
    - 纯协和音程（$P1, P5, P8$）极高音响融合（Tonal Fusion）导致声部独立性坍塌的听觉心理学原理；
    - 隐伏五八度（Direct/Hidden Fifths and Octaves）的检验与过滤准则。

---

## 2. 正文位置与目录拓展

- **核心正文**：`content/techniques/counterpoint/parallel-fifths-and-octaves.md`
- **方向归属**：`techniques` 轴下的 `counterpoint` 对位方向。与 `content/techniques/counterpoint/suspension-mechanics-and-voice-leading.md`（挂留音力学）形成呼应，从横向线条独立性、声学音响融合到配器织体加倍，系统阐释西方多声部思维的技术边界与演进。

---

## 3. 谱例占位与交付状态

正文内采用符合规范的真实作品、乐章与小节范围单行普通文本占位符：
1. **贝多芬《C大调第21钢琴奏鸣曲“华德斯坦”》Op. 53 第一乐章 mm. 1–8**（低音器乐八度加倍与对位声部辨析）；
2. **贝多芬《降E大调第26钢琴奏鸣曲“告别”》Op. 81a 第一乐章 mm. 1–6**（“告别”圆号五度与隐伏五度诗学）；
3. **贝多芬《C小调第8钢琴奏鸣曲“悲怆”》Op. 13 第一乐章 mm. 11–20**（快板低音八度震音脉动与织体厚度）。

暂无需另发加急 R 卡打扰谱例助手，保持单行文本占位即可通过验证。
