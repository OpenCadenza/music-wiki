<!-- music-kb:page {"id": "page.da330e2ea6ef45ee8c7c7e893d5bfa5e"} -->
<!-- knowledge: form.concerto.solo-tutti-duty -->
# 巴洛克到古典协奏曲的独奏/合奏职责

协奏曲中的“独奏”到底只是音量焦点，还是结构角色？比较Vivaldi《春》RV 269第一乐章的开场全奏与Mozart《A大调钢琴协奏曲》K. 488第一乐章的钢琴首次进入，可以看到职责的变化。Vivaldi让全奏以高度一致的口号和重复音型建立稳固参照，独奏随后从这一参照中出走；Mozart仍以乐队全奏建立主题库，但钢琴进入后可以接管、装饰并改写这一主题，在乐句、和声和音色上都获得作曲性，而不只是演奏华彩。

这一变化不是简单的“巴洛克竞争”到“古典合作”。MIT OpenCourseWare把巴洛克协奏曲的基本组织概括为tutti与独奏的争辩或对话，并指出ritornello可以拆成短语、改变顺序与组合；研究Mozart与古典协奏曲的统计论文也把重点放在独奏部分的数量和主题质量提升，以及它与sonata features的汇合。两类材料共同支持“职责更细分”，而不是只支持“风格更抒情”。

| 观察轴 | Vivaldi, RV 269第一乐章 | Mozart, K. 488第一乐章 |
| --- | --- | --- |
| 谁先定义材料 | 完整弦乐组共同陈述开场 | 乐队先陈述主题群；钢琴到第67小节后才第一次进入 |
| 谁改变调性/句法推进 | 独奏段承担离开固定参照的运动，全奏提供回返标记 | 独奏进入后重述并改写已出现的旋律，乐队可回应或退为支撑 |
| 主题是否属于单一角色 | 齐奏轮廓、重复音型和低音共同构成材料 | 钢琴能占有乐队的主题，材料归属不再固定 |
| 结束机制 | 收束回归tutti和主调；Vivaldi标出的“cadenza”与其后古典惯例不同 | cadenza可由无实质准备、短准备或长准备引出；其结束与收尾全奏的边界需逐乐章核对 |
| 结构关键词 | ritornello、episode、tutti | 双呈示逻辑、sonata functions、solo cadence、closing ritornello |

## 巴洛克：先建立集体的“路标”

Vivaldi开场不是“第一小提琴演奏，其他弦乐伴奏”的单线分工。第一小提琴给出跳跃、级进和下行的旋律轮廓；第二小提琴、中提琴和大提琴以不同音区重复其节奏或和声锚点，使整组弦乐听起来像一个共同动作。全奏因此既是旋律陈述，也是节拍、调性和材料的记忆装置。

MIT的ritornello教学说明区分了开头、完整或缩短的中间全奏以及收尾。独奏并不随意离开：它在全奏已经建立的音级和节奏上展开，再走到新音区、新调或新的乐器化动作。重要的是返回时认路。全奏不必每次保持同一长度；它作为模块可以被拆分、缩短或重排，但主调与材料的锚点让听者知道偏离和返回。

### 谱例一：RV 269开场的共同陈述

下列四声部取自Mutopia的LilyPond工程，只保留第一乐章第1–4小节。前四小节的原谱为E大调、4/4拍，并有八分音符弱起。代码按四声部重新整理，没有加入后续birdsong独奏或转调段。

<!-- opusloom:example
{
  "id": "vivaldi.rv269.opening-tutti",
  "status": "draft",
  "source_version": "2.12.3",
  "target_version": "2.26.0",
  "compile": "score",
  "midi": false,
  "requires": [],
  "sources": [
    "mutopia-vivaldi-spring",
    "mit-ocw-baroque-concerto"
  ],
  "rights": "Vivaldi composition public domain; encoding CC BY-SA 3.0, maintainer Anonymous (smailliw) as credited in source header, Mutopia id301. Adapted excerpt retains attribution and share-alike; original expressive texts and figured-bass staff omitted.",
  "source_locator": "Vivaldi, The Four Seasons, Spring RV 269, I, mm.1-4; Mutopia spring1a.ly, spring1b.ly, spring1c.ly, spring1d.ly",
  "context": "Original 2.12.3 syntax and old-relative option retained. Pickup plus four full measures from violin I, violin II, viola and cello; original key/meter/pitches/durations retained, text dynamics/tempo and figured bass omitted.",
  "origin_files": [
    {
      "file": "spring1a.ly",
      "sha256": "85a13422f89ea3edba39ee84076588c9b05b34c833fc3a99f1a222b10c3a9271"
    },
    {
      "file": "spring1b.ly",
      "sha256": "807acc2cb88208b1a8af4c6460feebc53e696ac97b56e5dd0129586f8d567291"
    },
    {
      "file": "spring1c.ly",
      "sha256": "bd1cb46276e8b0f5020a0d0701d7b464f126686f9dc7e12a49334cb0b42336bf"
    },
    {
      "file": "spring1d.ly",
      "sha256": "21b6ca9cd81bfa53006e4299f34e9c229bac40445f31df0a66df46af91a570a2"
    }
  ]
}
-->
```lilypond
#(ly:set-option 'old-relative)
\version "2.12.3"

violinOne = \relative e'' {
  \clef violin
  \key e \major
  \time 4/4
  \partial 8 e8
  gis8[ gis] gis[ fis16 e] b'4. b16 a |
  gis8[ gis] gis[ fis16 e] b'4. b16 a |
  gis8 a16 b a8 gis fis dis b e |
  gis8[ gis] gis[ fis16 e] b'4. b16 a |
}

violinTwo = \relative e'' {
  \clef violin
  \key e \major
  \time 4/4
  \partial 8 b8
  e8 e e e gis4. gis16 fis |
  e8 e e e gis4. gis16 fis |
  e8 fis16 gis fis8 e dis4 r8 b |
  e8 e e e gis4. gis16 fis |
}

viola = \relative e' {
  \clef alto
  \key e \major
  \time 4/4
  \partial 8 gis8
  b8 b b b e,4. gis16 a |
  b8 b b b e,4. gis16 a |
  b8 b cis cis fis,4 r8 gis |
  b8 b b b e,4. gis16 a |
}

cello = \relative e {
  \clef bass
  \key e \major
  \time 4/4
  \partial 8 e8
  e4 e e e |
  e4 e e e |
  e8[ e] a,[ ais] b4 r8 e |
  e4 e e e |
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Violino I" } { \violinOne }
    \new Staff \with { instrumentName = "Violino II" } { \violinTwo }
    \new Staff \with { instrumentName = "Viola" } { \viola }
    \new Staff \with { instrumentName = "Violoncello" } { \cello }
  >>
  \layout { }
}
```

第一小提琴在第1–2小节以G♯重复后转向B和A，第3小节用A–B–A和F♯–D♯–B–E下行连通到第二层；第二小提琴在相同节拍上重复E并走向G♯，中提琴提供内部三度/跳进，大提琴以E持续与A–A♯–B的低音变化托住。这里“共同”不等于齐奏同音：四个声部在分工中形成同一和声与节奏动作。这个局部事实支持代码旁的结构判断；后续独奏段的程度仍需阅读全谱，未由四小节自动证明。

## 古典：独奏可以成为主题的作者之一

K. 488第一乐章先让乐队陈述主题，钢琴到第67小节才进入。若把首66小节理解为“前奏”，会漏掉一个要点：全奏已经呈现了钢琴随后必须参与解释的材料。钢琴进入后采用与乐队开场相近的跳进、邻音和回落轮廓，却把连续伴奏改写为分解和弦、音阶、双音或更自由的声部组合。独奏从“主题被给你”转为“主题在这里被重新说法”。

MTO 2025年的cadenza研究补充了后段结构：中晚期18世纪的独奏写作扩张，cadenza不再只是偶发装饰；全奏可为其准备，cadenza的结束又牵动收尾全奏。由此，独奏在乐章中持续取得形式角色，cadenza只是最显眼的一次。但这段研究同时强调形态范围很大，短小装饰和长的幻想式段落都存在，不能用Mozart一个例子统一时代。

### 谱例二：K. 488的主题移交

下面把相隔很久的两段并列：乐队第一小提琴第1–4小节与钢琴右手第67–70小节。两行并排是为了比较旋律职责，**不是连续演奏的谱面**。为控制篇幅，省略配器、左手和声以及中间全部连接。

<!-- opusloom:example
{
  "id": "mozart.k488.theme-handover",
  "status": "published",
  "source_version": "2.18.2",
  "target_version": "2.26.0",
  "compile": "score",
  "midi": false,
  "requires": [],
  "sources": [
    "mutopia-mozart-k488",
    "mts-maliniak-greenberg-concerto",
    "mto-maliniak-classical-cadenza"
  ],
  "rights": "Original work public domain; short excerpts from Mutopia's public-domain LilyPond score.",
  "source_locator": "Mozart, Piano Concerto No.23 in A major, K.488, I, violin I mm.1-4 and piano RH mm.67-70",
  "context": "Original 2.18.2 syntax. Non-contiguous violin I mm1-4 and piano RH mm67-70 shown in parallel for comparison, not simultaneous performance; original relative anchors retained; left hand, orchestra context, dynamics and intervening66bars omitted.",
  "origin_files": [
    {
      "file": "violin-i.ily",
      "sha256": "a6db2ca084bebbe87aa8ee6f625ee51338753946fa4a38009846049bbf184c47"
    },
    {
      "file": "piano.ily",
      "sha256": "654ce8a85e0e4c79ce133392054306d64eac4598694316dd77586b2c898869ea"
    }
  ]
}
-->
```lilypond
\version "2.18.2"

orchestralTheme = \relative c'' {
  \key a \major
  \time 4/4
  e2( cis) |
  d4.( fis8) b,( d) gis,( b) |
  a4( gis fis e) |
  e4.( gis16 fis) e4 r4 |
}

pianoEntry = \relative c' {
  \key a \major
  \time 4/4
  e'2( cis2) |
  d4. fis8 b,( d) gis,( b) |
  a4 <gis e>( <fis d> <e cis>) |
  <e cis>4.( <gis e>16 <fis d>) <e cis>4 r4 |
}

\score {
  <<
    \new Staff \with { instrumentName = "Vln. I, mm. 1-4" }
    { \orchestralTheme }
    \new Staff \with { instrumentName = "Piano RH, mm. 67-70" }
    { \pianoEntry }
  >>
  \layout { }
}
```

两行共享E–C♯、D–F♯、B–D–G♯–B的旋律骨架与四分/八分节奏，但钢琴在第三小节把单线条改写为和弦，在第四小节以C♯—E双音和回音式十六分音符明确演奏者的发声职责。乐队可直接呈现一个可共同记忆的轮廓；钢琴则能在同轮廓上增加技术动作与音色层次，之后再与乐队交换回应。

## 跨段职责表

| 段落问题 | Vivaldi式ritornello | Mozart式古典协奏 |
| --- | --- | --- |
| 开场谁建立主调 | 全奏；分子可拆开但仍保持集体身份 | 全奏先呈示主题群；独奏可稍后参与 |
| 独奏首次进入 | 从共享材料的固定参照走向新音型/新调 | 常与主题或sonata功能相连，而不只是“开始独奏秀” |
| 中间全奏 | 缩短、重排，提示返回和新的调性位置 | 与sonata exposition/development/recap的需求结合 |
| 独奏华彩 | 全奏框架中的延长或离开；Vivaldi“cadenza”标签语境不同 | cadenza的全奏准备可无、可短、可长；持续与收尾边界须逐乐章核对 |
| 最终收束 | 回到tutti与主调 | 独奏、cadenza与收尾全奏共同完成终止职责 |

## 可迁移的写作流程

1. 写开场前先定一张“职责合同”：主题、副题、调性偏移、终止和收束分别允许谁首先说出、谁可改写。
2. 把ritornello拆成短模块，不以整段复制为唯一返回。每次回归写清保留项，例如低音、动机头、终止型或音色。
3. 让独奏进入时产生至少两个新关系：接管既有材料、改变伴奏层、引出新的和声方向，或在终止中承担更具体的作用。
4. 若使用cadenza，先写没有cadenza也能闭合的骨架，再决定cadenza是延长最后协和、重述主题还是打开另一层。这样可检查cadenza是否真的改变乐句功能。
5. 完成后分别读全奏骨架、独奏线与总谱配器。只看一条旋律会把“独奏”误写成音更高的乐队第一小提琴。

## 反例与证据边界

- 巴洛克独奏者并非整场都与乐队分开。历史上的独奏键盘手可为全奏弹continuo，独奏小提琴也可参与第一小提琴组；具体作品要读分谱与传统。
- “tutti总是稳定、独奏总是转调”只是有用的入口，不是定律。某些tutti也会改变调性或内部结构；判断错误应在作品层修正。
- 古典协奏曲不是把sonata form铺在ritornello上就自动成立。独奏进入、材料质量和收束共同参与；Maliniak与Greenberg的研究正是将这看成逐步汇合。
- Vivaldi少数作品标有“cadenza”，但MTO研究指出它没有古典协奏曲cadenza的固定意义；不能凭同名词直接连续性。
- K. 488第1–4与第67–70小节的支持只说明材料和演奏职责的变化；中段调性计划、完整cadenza位置与结尾仍须按全谱核对。

## 来源

- MIT OpenCourseWare, Michael Goetjen, [Baroque Concerto](https://ocw.mit.edu/courses/21m-011-introduction-to-western-music-fall-2024/pages/week-6-recitation-6a-listening-reading-goetjen/)，21M.011 Fall 2024。
- Omer Maliniak, [The Classical Concerto First-Movement Cadenza](https://mtosmt.org/issues/mto.25.31.3/mto.25.31.3.maliniak.html)，*Music Theory Online* 31.3 (2025)，§0.3–0.4、§2.5–2.6、§3.7–3.9。
- Omer Maliniak and Yoel Greenberg, [Follow the Solo](https://doi.org/10.1093/mts/mtac009)，*Music Theory Spectrum* 44.2 (2022)，摘要级阅读。
- Mutopia, [La Primavera / Spring](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=301)与[Mozart K.488](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2229)。

示例目前为`draft`。Vivaldi保留old-relative，convert-ly无法自动迁移到目标2.26.0，须人工迁移并逐声部核对音高、弱起与时值后才可考虑发布。主代理需合并来源表，复审Vivaldi第1–4小节的四声部与Mozart两个非连续片段，再决定发布状态。
