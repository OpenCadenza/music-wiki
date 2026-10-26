<!-- music-kb:page {"id": "page.4b49e66df680594788f4a1f19cf8abe5"} -->
<!-- knowledge: composer.beethoven.workflow.sketch-to-voices -->
# 从草稿轮廓到独立声部

检索词：Beethoven 贝多芬 草稿 sketch revision 创作过程 修订 复调 polyphony 版本 autograph critical edition。范围：创作和记谱方法；不提供任一作品的草稿复原。

贝多芬研究中的“草稿”并非一种统一文件。Lockwood 区分零散草稿、写作中的总谱和正式手稿，也区分很短的概念草稿与较长的连续草稿。它们之间可能来回工作。对创作 agent 有用的迁移，是将局部材料、整段连续性与最终声部实现分开处理；这条工作方法是本库的建议，不是对贝多芬每一次创作顺序的历史断言。[Lockwood，Sources of Knowledge](https://www.bu.edu/beethovencenter/i-sources-of-knowledge-of-beethovens-compositional-procedures/)

## 先写出能比较的两种方案

指定一条不可丢失的关系，例如上行四度后级进回落。A 只记录该关系。B 保留轮廓，却以低音进入、上声部对答和终止目标把它写成段落。不要只给 A 增加八度和力度就声称完成了发展。

<!-- opusloom:example {"id": "beethoven.model.sketch-to-voices", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["beethoven-lockwood-procedures", "beethoven-henle-sonatas-commentary"], "rights": "Original teaching model by this knowledge-base batch; no Beethoven notes or manuscript transcription reproduced.", "source_locator": "Self-authored A/B model. Source readings motivate separation of conceptual sketch and voice realization, not these pitches.", "context": "原创两方案：概念轮廓与双声部实现。不是贝多芬风格鉴定，也不是历史草稿。"} -->
```lilypond
\version "2.26.0"
\language "english"
idea = \relative c' {
  \key c \minor \time 4/4
  c4 f ef d | c2 r2 |
}
upper = \relative g' {
  \key c \minor \time 4/4
  g2 af4 g | f4 bf af g |
  g4 c bf af | f4 d ef2 |
}
lower = \relative c {
  \key c \minor \time 4/4
  c4 f ef d | bf2 g |
  ef4 af g f | g2 c, |
}
\score { \new Staff \with { instrumentName = "A" } { \idea } \layout {} }
\score {
  \new PianoStaff <<
    \new Staff \with { instrumentName = "B" } { \upper }
    \new Staff { \clef bass \lower }
  >>
  \layout {}
}
```

A 的 c–f–ef–d 在 B 的第1小节低声部出现。B 第2小节高声部换为 f–bf–af–g，保留上行四度和回落，低音却另写支撑。第4小节用低音 G→C 与高声部 D→E♭收束。第二次进入改变了音级和声部位置；连续性来自同一轮廓，而不是照搬相同伴奏。这个短例只说明如何实现和比较关系，不能证明这是贝多芬的原作手法，也没有展示完整奏鸣曲的调性过程。

## 双谱表不是两只手各一条旋律

Henle 1975/76 年前言强调，音符在谱表间的分布、休止与符干可显示主调和复调的交融。对 LilyPond 写作者，声部身份应先于左右手划分；实际多声部同谱表时保留独立时值和休止，必要时用 Voice 与跨谱表。此处 B 为便于辨认而每谱表一声部，没有模拟原作的复杂记谱。[Henle，PREFACE，印刷VI](https://www.henle.de/media/21/33/94/1697725799/9032-1697725799-sync.pdf)

## 原作证据与新作决策分开保存

引用真实片段时，先确定作品、版本、乐章、小节和声部，再决定省略什么。Beethoven-Haus 的学术版综合不同来源，并在校勘说明中交代差异；“网上有一份谱”不能替代这些定位。下载的现代编码与历史作品也可能具有不同许可。[Beethoven-Haus，Edition works](https://www.beethoven.de/en/studies)

对于新作，一轮修订只解决一个可听见的问题：动机是否还可识别，推进是否到达计划的和声目标，声部进入是否遮住主线。把保留方案和弃用方案各留一条理由即可。不要无休止比较每个音符，也不要将自编方案标为“复原贝多芬创作过程”。

相邻检索：奏鸣曲的局部推进应查相应钢琴／交响曲文章；变奏的参数控制应查变奏文章。该页是工作方法入口，不代替体裁与时期证据。

导航：[创作流程概述](index.md)。
