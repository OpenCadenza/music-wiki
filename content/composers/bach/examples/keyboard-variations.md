<!-- music-kb:page {"id": "page.1814f02b620149b58858c6e2660332d3"} -->
<!-- knowledge: composer.bach.keyboard-variations -->
# 巴赫键盘变奏：和声骨架与表面织体

键盘变奏可以保留低音与和声方向，同时重新组织前景节奏和声部关系。本章目前以《哥德堡变奏曲》的 Aria 与第一变奏为可核对的首组材料；这足以区分“保留和声框架”和“逐音装饰原旋律”，不能据此代表巴赫全部变奏作品。进一步扩充应比较更多变奏的卡农、舞曲和自由织体，以同一组结构问题组织正文，而不是增加逐曲页面。

<!-- knowledge: bach.variation.bwv988.aria-to-var1 -->
## BWV 988：变奏保留什么，改变什么

主题和第一变奏的关系要通过多个层次核对。低音功能、乐句边界和调性布局通常比表层旋律更容易保持；节奏密度、分解方式、重音与声部交换则提供变化。仅把主题移植成十六分音符会得到装饰，却未必形成有结构的变奏。

### 主题开头

<!--
id: bach.bwv988.aria.opening
source-version: 2.16.1
corpus-path: lilypond/BachJS/BWV988/bwv-988-aria/bwv-988-aria.ly
corpus-sha256: f86adfb84573bc7775fe48750f7ee9b6df2adf2fcc5e32fb52c09e589c9e12af
source: mutopia-bach-bwv988
rights: CC-BY-SA-3.0
-->

<!-- opusloom:example
{
  "id": "bach.bwv988.aria.opening",
  "status": "published",
  "source_version": "2.16.1",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-bach-bwv988",
    "bach-digital"
  ],
  "rights": "CC-BY-SA-3.0",
  "source_locator": "lilypond/BachJS/BWV988/bwv-988-aria/bwv-988-aria.ly",
  "context": "主题和第一变奏的低音骨架与节奏表面"
}
-->
```lilypond
\version "2.16.1"
upper = \relative c'' {
  \time 3/4 \key g \major
  g'4 g4( a8.\prallmordent) b16 |
}
lower = {
  \clef bass \time 3/4 \key g \major
  <<
    { g2. }
    \\
    { r4 b2 }
    \\
    { r2 d'4 }
  >>
}
\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \lower }
  >>
  \layout { }
  \midi { }
}
```

### 第一变奏开头

<!--
id: bach.bwv988.var1.opening
source-version: 2.16.1
corpus-path: lilypond/BachJS/BWV988/bwv-988-v01/bwv-988-v01.ly
corpus-sha256: 24fcef149fc4ac2b562020f7db2c38084bee0c47c73adec9cea7134d1aa18b5c
source: mutopia-bach-bwv988
rights: CC-BY-SA-3.0
-->

<!-- opusloom:example
{
  "id": "bach.bwv988.var1.opening",
  "status": "published",
  "source_version": "2.16.1",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-bach-bwv988",
    "bach-digital"
  ],
  "rights": "CC-BY-SA-3.0",
  "source_locator": "lilypond/BachJS/BWV988/bwv-988-v01/bwv-988-v01.ly",
  "context": "主题和第一变奏的低音骨架与节奏表面"
}
-->
```lilypond
\version "2.16.1"

upper = \relative c'' {
  \time 3/4 \key g \major
  g16 fis g8 ~ g16 d e fis g a b cis |
}

lower = \relative c {
  \clef bass \time 3/4 \key g \major
  g8[ b'16 a16 b8 g8 g,8 g'8] |
}

\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \lower }
  >>
  \layout { }
  \midi { }
}
```

原编码 JD Erickson，Mutopia-2013/01/22-979 / -980，CC BY-SA 3.0。Aria 例保留第1小节上声部 G5 和低声部 G3、B3、D4 的逐步叠入；第一变奏例保留第1小节的旋律及低声部。去除版面和跨谱表宏、补独立上下文；不是用单个 G 低音代替原三条重叠线。说明与改编按 CC BY-SA 4.0 分发。

### 对应关系

| 层 | Aria | Variation 1 | 检查方式 |
| --- | --- | --- | --- |
| 调性与低音中心 | G 音开始 | 低音仍以 G 为锚点 | 对齐乐句起点和低音功能 |
| 表层节奏 | 四分音符、附点装饰 | 十六分音符流动 | 比较每拍事件数，不只看音数 |
| 旋律身份 | G5重复与装饰性推进 | 从G4开始的邻音、折返和流动音型 | 不声称第一变奏旋律是Aria旋律的逐音派生 |
| 变奏策略 | 低音和声方案的起点 | 保留整体低音/和声方案，改变表层 | 音符更密不自动等于主题旋律严格减值；需全段对照 |

### 生成规则

1. 先固定变奏的低音功能和乐句长度，再写表层节奏。
2. 每一变奏选择有限的变化轴，例如节奏密度、音型方向、声部交换或音区；不要同时重写所有参数。
3. 每个变奏保留至少一个跨段可识别标记，并在计划中写明该标记。
4. 最后回到主题时核对低音和终止，不依据“听起来像”直接声称再现。

### 局限

这里只比较开头，不能推出整套 30 段变奏的统一设计。完整作品还要检查每一变奏的体裁类型、卡农间隔、装饰音、双键盘分配和终止安排。谱面与听觉分析优先于任何单一动机关系。

### 来源

- [Mutopia: Goldberg Aria](https://www.mutopiaproject.org/ftp/BachJS/BWV988/bwv-988-aria/)
- [Mutopia: Goldberg Variation 1](https://www.mutopiaproject.org/ftp/BachJS/BWV988/bwv-988-v01/)
- [Bach Digital](https://www.bach-digital.de/)：作品和来源控制。
