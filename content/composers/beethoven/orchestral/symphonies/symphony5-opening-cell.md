<!-- music-kb:page {"id": "page.fc56b08aac395b099ac23a3da657908b"} -->
<!-- knowledge: composer.beethoven.symphony5.opening-cell -->
# 第五交响曲开场：停顿怎样把短单元分成 P0/P1/P0

<!-- aliases: Symphony No.5, 第五交响曲, Op.67, opening, 开场, short-short-short-long, P0, P1, fermata, 停顿, Mutopia -->

Hepokoski 把第一乐章开头分成多个尺度：第 1–5 小节先有两个被延长并停顿的手势，第 5–21 小节展开 P1 后又被停顿截断，第 22–24 小节让 P0 在其他音阶位置返回，第 25 小节起才形成更宽阔的过渡。这个描述比“主题就是前四音”准确，因为它同时保留连续、停顿和返回。[Hepokoski, *MTO* 16.2 (2010), §14–15](https://mtosmt.org/issues/mto.10.16.2/mto.10.16.2.hepokoski.php)。

Eastman 的导读补充全曲尺度：短单元后来缩成两音乃至一音问答，第三乐章材料在不间断过渡中被重新组织，C 大调终章加入长号、低音大管和短笛，使音响范围突然扩大。两种材料互补：一个定义局部主题格式，另一个说明乐章重量和边界。[Symphony No.5](https://www.esm.rochester.edu/beethoven/symphony-no-5/)。

## 原谱定位

下面的短例取自 Mutopia 根据 Augener’s Edition 制作的第五交响曲第一乐章钢琴缩编，只截第 1–5 小节。它保留和弦重复、两处 fermata 和短音引向长音的节奏关系；它不是原管弦乐配器，代码不能证明具体乐器分工。

<!-- opusloom:example
{
  "id": "beethoven.symphony5.opening",
  "status": "published",
  "source_version": "2.18.2",
  "target_version": "2.26.0",
  "compile": "score",
  "midi": false,
  "requires": [],
  "sources": [
    "mutopia-beethoven-symphony5-m1",
    "beethoven-eastman-fifth",
    "hepkoski-fifth-p0-p1"
  ],
  "rights": "Original work public domain; short reduction transcribed from Mutopia's public-domain LilyPond source.",
  "source_locator": "Beethoven, Symphony No. 5 in C minor, Op.67, I, mm.1-5; Mutopia id 497; Mutopia-2015/01/17-497; LilyPond 2.18.2; source Augener’s Edition; Magnus Lewis-Smith piano reduction, mvt01-allegroconbrio.ly",
  "context": "Mutopia piano-reduction excerpt mm1-5, original 2.18.2 pitch syntax and correct 2/4 meter. Pedal, dynamics, repeat wrapper and layout removed; fermatas and ties retained. Not original orchestration."
}
-->
```lilypond
\version "2.18.2"
\include "english.ly"

upper = \relative g' {
  \clef treble
  \key c \minor
  \time 2/4
  r8 <g g,> <g g,> <g g,> |
  ef2\fermata |
  r8 <f f,> <f f,> <f f,> |
  d2 ~ |
  d\fermata |
}

lower = \relative g, {
  \clef bass
  \key c \minor
  \time 2/4
  r8 g g g |
  <ef ef'>2\fermata |
  r8 f f f |
  <d d'>2 ~ |
  <d d'>\fermata |
}

\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \lower }
  >>
  \layout { }
}
```

## 逐音与迁移

第 1 小节先有八分休止，再叠三次 G 八度，第 2 小节落到 E♭并停；第 3–5 小节从 F 重复开始，最终滑到 D 并再次停。首小节本身是完整 2/4，乐句起势不等于记谱上的不完全小节。最重要的关系是“连续动作被一个大停顿打断”，而不是某四个绝对音高。

迁移时先写出短促动作，再决定停顿在哪里切断它；接着改变随后的音高位置和句法长度，最后检查旧单元返回时是否改变了前文解释。若只复制同一节奏而保留原音高、配器和段落位置，得到的是重复；若所有层同时变化，则难以听出发展。

## 适用边界

- “命运敲门”是接受史和传记解释。谱面目前支持的事实是短音型、重复、移位和停顿。
- 反复出现的附点、三连音或短—短—短—长也可能属于时代共享语汇。确认动机关系至少要有轮廓、节拍位置或和声功能中的两项对应。
- 该代码只核对前五小节的钢琴缩编。发展、再现、跨乐章和《英雄》判断来自 Hepokoski 与 Eastman 所标位置，不以短例冒称全曲分析。
