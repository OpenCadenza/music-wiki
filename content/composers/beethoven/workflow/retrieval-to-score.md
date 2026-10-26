<!-- music-kb:page {"id": "page.b63030b7442351d8a05258497eae376d"} -->
<!-- knowledge: composer.beethoven.workflow.retrieval-to-score -->
# 把检索结果落实为12小节钢琴练习

<!-- aliases: Beethoven composition workflow, composing with examples, 原创练习, 模仿, 缩减, 终止, ABC, LilyPond -->

先把创作要求拆成时期、体裁、编制、曲式、材料操作五项，再选择相关正文。每次只取当前需要的1–3节；谱例要连同前后解释一起读。下面展示一次有限的使用流程，不声称已通过对照实验证明创作能力提高。

## 把分析转成当前乐谱的约束

| 当前问题 | 阅读位置与采用的知识 ID | 转成可以核对的操作 |
| --- | --- | --- |
| 材料如何保持身份 | [动机](../techniques/index.md)，`composer.beethoven.motivic-development` | 先写D–E–A–G与短短长长节奏，记录保留项，再做一次缩减 |
| 声部怎样接过材料 | [晚期钢琴](../piano/sonatas/index.md)，`composer.beethoven.piano.late` | 第3小节让低声部低两个八度模仿，第9小节原形回归；不因此称为赋格 |
| 密度如何改变 | 同页Op.109教学模型 | 第5小节前四音改成八分音符，续接F–E；这里保留起音顺序，不宣称整段和声保持 |
| 结尾能否说明白 | [和声与曲式](../techniques/index.md)，`composer.beethoven.harmony-form` | 末两小节明确写G7–C，给出B4→C5、F5→E5与低音G2→C2 |

这些是本练习的设计选择。文献提供具体作品分析和观察问题，不曾共同提出以下旋律。历史作品的分析不能直接证明新作有相同风格。

## 完整的12小节原创练习

<!-- opusloom:example {"id": "beethoven.model.composition-probe-12-bars", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["beethoven-boss-op10-1", "beethoven-ofcarcik-2020", "warburton-op109-2018", "beethoven-igoa-functional-harmony"], "rights": "项目原创12小节钢琴练习；没有转录贝多芬作品或现代谱例。", "source_locator": "原创练习；采用本库动机、声部进入、密度与和声目标的教学问题，而非上述文献的原谱音符。", "context": "D–E–A–G动机、低声部模仿、音值缩减、原形回归和末两小节根位G7–C；不是奏鸣曲、赋格或贝多芬风格认证。"} -->
```lilypond
\version "2.26.0"
\language "english"

global = {
  \key c \major
  \time 4/4
}

rightTop = {
  \global
  \tempo "Moderato" 4 = 88
  % 1: motive D-E-A-G, short-short-long-long
  d'8 e'8 a'4 g'2 |
  % 2: continuation
  f'4 e'4 d'2 |
  % 3: accompaniment while left hand imitates bar 1
  c''2 a'2 |
  % 4: answer-like continuation
  f'4 e'4 d'2 |
  % 5: density transformation; the four motive pitches return as eighths
  d'8 e'8 a'8 g'8 f'4 e'4 |
  % 6-8: sequence-like continuation, then a measured pause in motion
  g'8 a'8 d''4 c''2 |
  e'8 f'8 b'4 a'2 |
  g'2 f'2 |
  % 9-10: motive returns, then its earlier continuation
  d'8 e'8 a'4 g'2 |
  f'4 e'4 d'2 |
  % 11-12: soprano F5 resolves to E5
  f''1 |
  e''1 |
}

rightInner = {
  \global
  s1*10 |
  % B4 resolves upward to C5
  b'1 |
  c''1 |
}

rightMiddle = {
  \global
  s1*10 |
  % D5 moves to G4; completes the G7-to-C triad voice leading
  d''1 |
  g'1 |
}

leftHand = {
  \global
  \clef bass
  % 1-2: harmonic support for the initial gesture
  d,1 |
  g,1 |
  % 3: same motive and rhythm as bar 1, two octaves lower
  d,8 e,8 a,4 g,2 |
  % 4-10: harmonic floor under the continuing material
  c,2 g,2 |
  d,1 |
  g,1 |
  a,1 |
  g,1 |
  d,1 |
  g,1 |
  % 11-12: dominant seventh to tonic
  g,1 |
  c,1 |
}

\score {
  \new PianoStaff \with { instrumentName = "Piano" } <<
    \new Staff = "right" <<
      \new Voice { \voiceOne \rightTop }
      \new Voice { \voiceTwo \rightInner }
      \new Voice { \voiceThree \rightMiddle }
    >>
    \new Staff = "left" \leftHand
  >>
  \layout { }
}
```

第1小节右手提出动机；第3小节左手以相同音级和节奏进入，右手改为较长的支撑音。第5小节压短动机，6–8小节接续；第9小节回归。第11–12小节的三个右手声部依次为F5→E5、B4→C5、D5→G4，左手G2→C2。谱面可追踪导音和七音的解决；内部声部在结尾交叉，因此不把它当作严格四部和声或可倒转对位范本。

前十小节低音以单音为主，和弦功能并未处处填满；这是检验材料操作与明确结尾的短练习。它没有奏鸣曲呈示部的调性布局、完整赋格的应答/对题/插部，也未模拟历史钢琴。若任务要求“晚期贝多芬奏鸣曲”，完成这12小节还远远不够。

导航：[创作流程概述](index.md)。
