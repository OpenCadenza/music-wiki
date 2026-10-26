<!-- music-kb:page {"id": "page.3bdbdedacb125df8854b3b735d80bf9f"} -->
<!-- knowledge: composer.beethoven.symphony.cell-compression -->
# 短单元压缩：从第五交响曲到《英雄》的反例

<!-- aliases: cell compression, 短单元, 碎片化, liquidation, Eroica, 英雄, Symphony No.3, Symphony No.5, motive, 动机 -->

短动机是否能统一整部交响曲，取决于它是否改变句法位置、配器密度、调性路线或乐章连接。只重复一个节奏标签，不足以说明结构动力。

| 观察尺度 | 第五交响曲 | 《英雄》Op.55 |
| --- | --- | --- |
| 起始材料 | 三个短音接长音的口号式单元，随即停顿 | 琶音轮廓转入半音下行，主题内部已有调性和音级紧张 |
| 扩张方式 | 复制、移位、碎片化、全奏化与声部交接 | 主题多次带渐强配器出现；发展部引入远关系材料与假返回 |
| 结构问题 | P0/P1/P0 和第三至第四乐章的连续连接 | 假返回、再现中的主题改变、长尾声继续发展 |
| 不能推出 | 每次相似音型都带同一叙事含义 | 四乐章都可还原为一套唯一情节 |

第五的证据来自 Hepokoski 的局部主题格式和 Eastman 的全曲导航；《英雄》的证据来自 Eastman 对第一乐章和四乐章段落的导读。后者是院校教育材料对结构和接受的解释，不等于作曲家已经确认的标题程序。

## 原创模型

下面三行完全自编。A 只展示可复述单元；B 保留第一拍并增加后续方向；C 缩短单元、抽掉中间音符，用留白制造继续期待。它把“材料如何发展”拆成可重写的操作，不冒充原作片段。

<!-- opusloom:example
{
  "id": "beethoven.model.cell-compression",
  "status": "published",
  "source_version": "2.26.0",
  "target_version": "2.26.0",
  "compile": "score",
  "midi": false,
  "requires": [],
  "sources": [
    "beethoven-eastman-fifth",
    "hepkoski-fifth-p0-p1",
    "omt-sonata-exposition"
  ],
  "rights": "Self-authored teaching model; no Beethoven melody is reproduced.",
  "source_locator": "New two-bar models illustrating cell presentation, continuation, and liquidation after the readings by Hepokoski and Eastman",
  "context": "自编模型：同一A–A–A–G单元在完整陈述、扩张和碎片化三种状态下如何改变句法。"
}
-->
```lilypond
\version "2.26.0"
\language "english"

cell = \relative a' {
  \key c \major
  \time 4/4
  a16[ a a g] f2 e8[ d] |
  c2 r2 |
}

continuation = \relative a' {
  \key c \major
  \time 4/4
  a16[ a a g] f2 e8[ d] |
  c2 d4 e |
}

liquidation = \relative a' {
  \key c \major
  \time 4/4
  a8 r r a g4 r |
  f8 r r4 r2 |
}

\score {
  <<
    \new Staff \with { instrumentName = "A: cell" } { \cell }
    \new Staff \with { instrumentName = "B: continue" } { \continuation }
    \new Staff \with { instrumentName = "C: fragment" } { \liquidation }
  >>
  \layout { }
}
```

B完整保留A的第一小节，第二小节由C长音续接D–E；C把A–A–G及后续F拆散为起音与休止，改变连续性与句法任务。写作时应逐项记录移走了哪一层：轮廓、节奏、低音、配器或终止。所有层同时变化，听者只会听到新材料；任何一层都不变，发展容易变成无目标复制。

## 迁移与检查

1. 先判断开场建立的是句法、和声问题还是纯节奏标签。
2. 每次变化都指出具体层和目的：复制、继续、碎片化、全奏压力，还是改变调性路线。
3. 检查返回是否完成先前未完成的关系。若主题返回时配器、调性或句法全未改变，不能只凭“它回来了”宣称解决。
4. 允许乐章边界参与意义：第五第三/第四乐章的不间断连接说明，速度和调式切换也能进入结构层。

《英雄》提醒我们不要把所有贝多芬动机都写成“先短后扩”：它的开场主题内部已经包含较长动作和张力。模型也不能证明具体配器、发展部长度或叙事意图。

## 来源

- James Hepokoski, “Formal Process, Sonata Theory, and the First Movement of Beethoven's ‘Tempest’ Sonata,” *Music Theory Online* 16.2 (2010), §14–15：[文章](https://mtosmt.org/issues/mto.10.16.2/mto.10.16.2.hepokoski.php)。
- Eastman School of Music：[第五交响曲](https://www.esm.rochester.edu/beethoven/symphony-no-5/)与[第三交响曲“Eroica”](https://www.esm.rochester.edu/beethoven/symphony-no-3/)。
- Open Music Theory：[Sonata form – thematic modules](https://openmusictheory.github.io/sonataThematicModules.html)。
- Mutopia Project：[第五交响曲第一乐章](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=497)，Augener’s Edition 谱的钢琴缩编，公有领域。
