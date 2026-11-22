# 研究归档：减七枢纽

- **学者**：scholar-b4
- **选题**：减七和弦对称性与等音枢纽调性突变（Diminished Seventh Enharmonic Pivot and Tonal Disruption）
- **中心论证**：导减七和弦（$\text{vii}^\circ{}^7$）因其由三个小三度完全均分八度构成的轴对称结构，消除了传统和弦的唯一根音属性，具备四向等音重释为不同调性导音的自由度。贝多芬在《悲怆》奏鸣曲（Op. 13）中，既在引子（Grave）中利用减七和弦的导音与降 6 级半音夹击强化 C 小调向心凝聚力，又在展开部入口（mm. 135–139）利用 $F\sharp\text{–}A\text{–}C\text{–}E\flat$ 到 $D\sharp\text{–}F\sharp\text{–}A\text{–}C$ 的单音等音重写（$E\flat = D\sharp$），在零五度过渡下瞬间由 G 小调跨越 4 个调号单位突入 E 小调，实现核心动机的超距异调爆发；在《忧郁》（Op. 18 No. 6）中则更进一步以两声部上行全音、两声部下行大三度的交替滑动减七和弦链打破传统调性重力，开创了调性悬置的浪漫主义音响空间。
- **状态**：已按中期复读返修完成

---

## 1. 实际采用的资料范围与逐小节核对记录

- **底层机器可读原生谱源（Humdrum Kern 真实路径与逐小节核对）**：
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-piano-sonatas-main/beethoven-piano-sonatas-main/kern/sonata08-1.krn`（贝多芬 Op. 13 第一乐章 Grave 与 Allegro molto e con brio）：
    - **m. 1 第 3 拍**：低音 $F\sharp$（`4F#`），上方右手 $A\text{–}c\text{–}e\flat$（`4An 4c 4e-`），构成 C 小调属调副导七和弦（$\text{vii}^\circ{}^7/\text{V}$），在第 4 拍解决至属三和弦 $G\text{–}B\text{–}d$；
    - **m. 2 第 1 拍**：低音小字组 $A\flat$（`4A-X`），上方声部 $B\text{–}d\text{–}f$（`4Bn 4d 4f`），构成导三四和弦（$\text{vii}^\circ{}^4_3$），在第 3–4 拍逐步向主和弦第一转位（$E\flat\text{–}G\text{–}C$）消解；
    - **m. 3 第 1 拍与第 3 拍**：低音 $e\flat$ 引入 $f\sharp\text{–}a\text{–}c$（$\text{vii}^\circ{}^4_2/\text{V}$）；第 3 拍低音强音 $c$ 与旋律音 $f\sharp$（`4f# 4a 4ee-`，`fz`）形成三全音对抗，逼迫声部在第 3 拍半收敛至属和弦 $G\text{–}d\text{–}g$；
    - **m. 135**：展开部开端以慢速（Tempo primo, Grave, 4/4 拍）重回 G 小调（主调属方向），第 3 拍经过 $c\sharp$ 减七和弦（`4c#` / `4en 4g 4b-`）向 D 大调推进；
    - **m. 136**：低音 $e\flat$ 上方切入 $f\sharp\text{–}a\text{–}c$（G 小调中的 $\text{vii}^\circ{}^7/\text{V}$），第 3 拍解决至 G 小调主和弦（低音 $B\flat$，上方 $g\text{–}b\flat\text{–}d$）；
    - **m. 137**：第 1 拍低音 $e\flat$ 与右手 $f\sharp\text{–}a\text{–}c$（$fp$）再现；第 2 拍末至第 3 拍，左手滑向低音 $c$（`32cJJk`），右手旋律切入 $dd\sharp$（`32dd#JJk`），长音和弦记为 $f\sharp\text{–}a\text{–}dd\sharp$（`4f# 4a 4dd#`），$E\flat$ 音被等音重释为 E 小调导音 $D\sharp$（和弦重释为 E 小调 $\text{vii}^\circ{}^7$）；
    - **mm. 138–139**：声部向内收缩解决至 E 小调和弦，m. 138 确立 B 属三和弦准备并在延长音休止符停顿；m. 139 双小节线取消 3 个降号调号，快板以极轻（$p$）在 E 小调低音八分音符同音脉动上爆发。
  * 本地路径：`local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet06-4a.krn`（贝多芬 Op. 18 No. 6 第四乐章 La Malinconia. Adagio）：
    - **m. 9**：大提琴 $A\flat$、中提琴 $B$、第二小提琴 $f$、第一小提琴 $d$（$B$ 减七和弦，$\text{vii}^\circ{}^7$）；
    - **m. 13（$f$）**：大提琴 $E$、中提琴 $A\sharp$、第二小提琴 $g$、第一小提琴 $c\sharp$（$C\sharp$ 减七和弦）；
    - **m. 14（$p$）**：大提琴 $F\sharp$、中提琴 $c$、第二小提琴 $e\flat$、第一小提琴 $a$（$F\sharp$ 减七和弦）；
    - **m. 15（$f$）**：大提琴 $G\sharp$、中提琴 $d$、第二小提琴 $b$、第一小提琴 $f$（$G\sharp$ 减七和弦）；
    - **m. 17（$pp$）**：大提琴 $C$、中提琴 $A$、第二小提琴 $d\sharp$、第一小提琴 $f\sharp$（$D\sharp$ 减七和弦），并在 mm. 18–20 导向 B/E。

- **权威理论教材（Open Music Theory）**：
  * 本地路径：`local/resources/text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/`（章节：`appliedChords.md`、`Modulation.md`）：
    - 副导七和弦（$\text{vii}^\circ{}^7/\text{V}$）的功能定义与声部解决规范；
    - 枢纽转调（Pivot-chord Modulation）与等音转调（Enharmonic Modulation）的辨析准则。

---

## 2. 正文位置与目录拓展

- **核心正文**：`content/techniques/harmony/diminished-seventh-enharmonic-pivot.md`
- **方向归属**：`techniques` 轴下的 `harmony` 和声方向。与 `content/techniques/harmony/augmented-sixth-mechanics-and-syntactic-drift.md`（增六和弦）、`content/techniques/harmony/neapolitan-chord-structural-mutation.md`（那不勒斯和弦）以及 `content/techniques/harmony/chromatic-mediant-and-tonal-space.md`（三度调性）形成完整的古典晚期浪漫早期和声转折技法网络。

---

## 3. 谱例占位与交付状态

正文内采用符合规范的真实作品、乐章与小节范围单行普通文本占位符：
1. **贝多芬《C小调第8钢琴奏鸣曲“悲怆”》Op. 13 第一乐章 mm. 1–4**（Grave 引子减七和弦功能展开）；
2. **贝多芬《C小调第8钢琴奏鸣曲“悲怆”》Op. 13 第一乐章 mm. 135–139**（展开部等音枢纽突入 E 小调）；
3. **贝多芬《降B大调第6弦乐四重奏》Op. 18 No. 6 第四乐章 mm. 9–18**（“La Malinconia”减七和弦链式等音漫游）。

暂无需另发加急 R 卡打扰谱例助手，保持单行文本占位即可通过验证。
