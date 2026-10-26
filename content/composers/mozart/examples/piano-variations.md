<!-- music-kb:page {"id": "page.7448a2817e8946d596b48254ec3c2dec"} -->
<!-- knowledge: composer.mozart.piano-variations -->
# 莫扎特钢琴变奏：保留的骨架与变化的动作

变奏的连续性可以通过乐句位置、低音功能和终止方向保留，而表面动作发生显著改变。本章首组证据比较 K.331 的主题和第一变奏；它们是同一变奏乐章内部的对照，尚不足以概括莫扎特所有独立变奏曲。扩充时应围绕装饰、调式、速度与结构角色加入跨作品比较，不将每首曲子另建一页。

<!-- knowledge: mozart.variation.k331.theme-to-var1 -->
## K. 331：变奏首先要有可保留的结构

### 谱例：主题开头

<!--
id: mozart.k331.theme.opening
source-version: 2.6.0
corpus-path: lilypond/MozartWA/KV331/KV331_1_1_tema/KV331_1_1_tema.ly
corpus-sha256: cad24654df590cefbb1d7a6499cbb9d6061d728dfc82d640a786fbc375be48ef
source: mutopia-mozart-k331-theme
rights: Public-Domain
-->

<!-- opusloom:example
{
  "id": "mozart.k331.theme.opening",
  "status": "published",
  "source_version": "2.6.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-mozart-k331-theme",
    "mutopia-mozart-k331-var1",
    "omt-theme-types"
  ],
  "rights": "Public-Domain",
  "source_locator": "lilypond/MozartWA/KV331/KV331_1_1_tema/KV331_1_1_tema.ly",
  "context": "主题、第一变奏和伴奏音型之间的可观察差异"
}
-->
```lilypond
\version "2.26.0"

upper = {
  \key a \major \time 6/8
  cis''8.( d''16) cis''8 e''4 e''8 |
  b'8.( cis''16) b'8 d''4 d''8 |
}

lower = {
  \clef bass \key a \major \time 6/8
  <<
    { e'4 e'8 e'4 e'8 | e'4 e'8 e'4 e'8 | }
    \\
    { a8.( b16) a8 cis'4 cis'8 | gis8.( a16) gis8 b4 b8 | }
  >>
}

\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \lower }
  >>
  \layout { }
  \midi { \tempo 8 = 112 }
}
```

### 谱例：第一变奏开头

<!--
id: mozart.k331.var1.opening
source-version: 2.6.0
corpus-path: lilypond/MozartWA/KV331/KV331_1_2_var1/KV331_1_2_var1.ly
corpus-sha256: c26846471ed7c60712c88421483db8121d3a391742b948c2782321cd07b90e41
source: mutopia-mozart-k331-var1
rights: Public-Domain
-->

<!-- opusloom:example
{
  "id": "mozart.k331.var1.opening",
  "status": "published",
  "source_version": "2.6.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-mozart-k331-theme",
    "mutopia-mozart-k331-var1",
    "omt-theme-types"
  ],
  "rights": "Public-Domain",
  "source_locator": "lilypond/MozartWA/KV331/KV331_1_2_var1/KV331_1_2_var1.ly",
  "context": "主题、第一变奏和伴奏音型之间的可观察差异"
}
-->
```lilypond
\version "2.26.0"

upper = {
  \key a \major \time 6/8
  bis'16 cis'' r cis''( bis' cis'') dis''( e'') r e''( fis'' e'') |
  e''16( b'!) r b'( ais' b') cis''( d''!) r d''( e'' d'') |
}

lower = {
  \clef bass \key a \major \time 6/8
  r8 <a e'> r r <cis' e'> r |
  r8 <gis e'> r r <b e'> r |
}

\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \lower }
  >>
  \layout { }
  \midi { \tempo 4 = 92 }
}
```

原编码 Stelios Samelis，Mutopia-2005/10/29-614 / -615，公有领域。两例使用原来的绝对音高记谱，不能把这些带八度标记的音符再套进 relative；主题左手保留原来两条同时声部。去掉版面标记、补小节线与独立 score，上述音高/时值不作重写。

### 对比

| 参数 | 主题 | 第一变奏 | 迁移建议 |
| --- | --- | --- | --- |
| 调性 | A 大调 | A 大调 | 保留 A 大调作为稳定框架 |
| 拍号 | 6/8 | 6/8 | 保留每小节两大拍、每大拍三分的复拍脉冲 |
| 右手节奏 | 附点进入、较长音符 | 十六分音符和休止切分 | 用节奏减值增加事件密度 |
| 左手 | 有旋律性的分解声部 | 分散和弦与节奏重音 | 变奏可改变伴奏语法 |
| 乐句目标 | 第 1 小节 C-sharp 等目标音 | 保留主要音区目标和终止方向 | 目标音优先于表面音数 |

### 生成流程

1. 先抽出主题的调性、拍号、乐句长度、低音骨架和主要旋律目标音。
2. 选择一个主要变奏轴，写 2 小节试验并与主题逐项对齐。
3. 检查右手、左手是否仍共同支持同一乐句功能；只保留旋律而丢失终止，不构成成功变奏。
4. 下一变奏必须有新的变化轴，避免每个变奏都只是同一分解和弦加更多音。

### 局限

两段开头不能覆盖整首变奏乐章。完整任务还要审查各变奏的节奏型分布、和声节奏、复调密度和相邻段落对比。

### 来源

- [Mutopia: K. 331 theme](https://www.mutopiaproject.org/ftp/MozartWA/KV331/KV331_1_1_tema/)：公有领域，原始语法 2.6.0。
- [Mutopia: K. 331 Variation 1](https://www.mutopiaproject.org/ftp/MozartWA/KV331/KV331_1_2_var1/)：公有领域，原始语法 2.6.0。
- [Open Music Theory: Classical theme types](https://openmusictheory.github.io/classicalThemes.html)
