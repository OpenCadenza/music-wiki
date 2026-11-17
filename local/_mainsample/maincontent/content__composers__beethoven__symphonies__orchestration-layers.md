# 配器分层：谁在加倍谁

一段全奏里，十几个声部同时发声，听者实际听到的只有三层：最上面一条、最下面一条、中间最响的那一块。
其余声部要么在加倍，要么在填空。判断配器好坏，有一个很硬的指标——**把总谱上每个音追问一遍"为什么给它"，
答不出音区、音色或呼吸的理由，那次分配就是习惯动作。**

Op.92 第七交响曲的引子（Poco sostenuto）第一小节就是一次极端的分层实验：所有声部同时砸一个 A 大调，
但每一层拿到的音完全不同。

```lilypond title="贝多芬 Op.92 第一乐章" location="Poco sostenuto，mm.1–8"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "flauti" {
      \set Staff.instrumentName = "Flauto"
      \set Staff.midiInstrument = "flute"
      % GM 73
      
      \clef treble \key a \major \time 4/4
  % m.1
  <cs''' a'''>4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  <b'' e'''>4 \f \staccato r r2
  % m.4
  R1
  % m.5
  <cs''' e'''>4 \f \staccato r r2
  % m.6
  << { a''2 ^ \p ( e''4 a'' ) a''1 ^ \fp ( b''2 c'''2 ) } \\ { R1 d'''4 \staccato \f r4 r2 R1 } >>
    }
    \new Staff = "oboi" {
      \set Staff.instrumentName = "Oboe"
      \set Staff.midiInstrument = "oboe"
      % GM 68
      
      \clef treble \key a \major \time 4/4
  % m.1
  << { a''2 ^ \fp ( e'' cs'' fs'' ) e''1 ^ \fp ~ e''4 ( fs''8 e'' ) e''4 ( fs''8 e'' ) e''1 ^ \fp ~ e''8 ( d'' cs'' d'' e'' fs'' g'' e'' ) } \\ { cs''4 \f \staccato a'4 \rest a'2 \rest R1 R1 R1 R1 R1 } >>
  % m.7
  << { d''1 ~ d''2 ( e''4 g'' ) } \\ { d''2 \fp ( a' b' c'' ) } >>
    }
    \new Staff = "clarinetti" {
      \set Staff.instrumentName = "Clarinetto in A"
      \set Staff.midiInstrument = "clarinet"
      % GM 71
      \transposition a
      \clef treble \key c \major \time 4/4
  % m.1
  <e'' c'''>4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  << { g''2 ( d'' g' f'' ) e''1 ^ \fp ~ e''8 ( d'' c'' d'' e'' f'' g'' e'' ) f''4 f'2. ~ f'2 ( g'4 bf' ) } \\ { g''2 \fp d'' g' f'' e''4 \f \staccato r4 r2 r2 e'4 \rest c''4 c'' \fp f'2 ( c'4 d'2 ef'2 ) } >>
    }
    \new Staff = "fagotti" {
      \set Staff.instrumentName = "Fagotto"
      \set Staff.midiInstrument = "bassoon"
      % GM 70
      
      \clef bass \key a \major \time 4/4
  % m.1
  <a cs'>4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  <gs b>4 \f \staccato r r2
  % m.4
  R1
  % m.5
  <g, g>4 \f \staccato r r2
  % m.6
  R1
  % m.7
  <d d'>2 \fp ( <a, a>
  % m.8
  <f, d> <e, g> )
    }
    \new Staff = "corni" {
      \set Staff.instrumentName = "Corno in A"
      \set Staff.midiInstrument = "french horn"
      % GM 60
      \transposition a
      \clef treble \key c \major \time 4/4
  % m.1
  <c' c''>4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  <g g'>4 \f \staccato r4 r2
  % m.4
  R1
  % m.5
  << { c''2 ( g' c' c'' ) c''1 bf'2 bf' c''4 } \\ { c''2 \fp ( g' c' c'' ) c''1 \fp bf'2 bf' c''4 } >>
    }
    \new Staff = "trombe" {
      \set Staff.instrumentName = "Tromba in D"
      \set Staff.midiInstrument = "trumpet"
      % GM 56
      \transposition d
      \clef treble \key c \major \time 4/4
  % m.1
  <g' g''>4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  << { d''4 \staccato } \\ { d''4 \f } >> r4 r2
  % m.4
  R1
  % m.5
  <g' g''>4 \f \staccato r4 r2
  % m.6
  R1
  % m.7
  <g' g''>4 \f \staccato r4 r2
  % m.8
  R1
    }
    \new Staff = "timpani" {
      \set Staff.instrumentName = "Timpani"
      \set Staff.midiInstrument = "timpani"
      % GM 47
      
      \clef bass \key c \major \time 4/4
  % m.1
  a,4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  e4 \f \staccato r4 r2
  % m.4
  R1
  % m.5
  a,4 \f \staccato r4 r2
  % m.6
  R1
  % m.7
  a,4 \f \staccato r4 r2
  % m.8
  R1
    }
    \new Staff = "violinoone" {
      \set Staff.instrumentName = "Violino I"
      \set Staff.midiInstrument = "violin"
      % GM 40
      
      \clef treble \key a \major \time 4/4
  % m.1
  <a e' cs'' a''>4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  <e' b' e''>4 \f \staccato r r2
  % m.4
  R1
  % m.5
  <a e' cs'' a''>4 \f \staccato r4 r2
  % m.6
  R1
  % m.7
  <d' a' a''>4 \f \staccato r a'4 \p r
  % m.8
  b' r c'' r
    }
    \new Staff = "violinotwo" {
      \set Staff.instrumentName = "Violino II"
      \set Staff.midiInstrument = "violin"
      % GM 40
      
      \clef treble \key a \major \time 4/4
  % m.1
  <a e' cs'' a''>4 \f \staccato r4 r2
  % m.2
  cs'1 \p
  % m.3
  <e' b' e''>4 \f \staccato r r2
  % m.4
  b1 \p
  % m.5
  <a e' cs'' a''>4 \f \staccato r4 r2
  % m.6
  <a e'>1 \p
  % m.7
  <d' a' a''>4 \f \staccato r d'4 \p r
  % m.8
  d' r c' r
    }
    \new Staff = "viola" {
      \set Staff.instrumentName = "Viola"
      \set Staff.midiInstrument = "viola"
      % GM 41
      
      \clef alto \key a \major \time 4/4
  % m.1
  <a e' a'>4 \f \staccato r4 r2
  % m.2
  a1 \p
  % m.3
  <gs b e'>4 \f \staccato r r2
  % m.4
  gs1 \p
  % m.5
  <g e' a'>4 \f \staccato r4 r2
  % m.6
  g1 \p
  % m.7
  <fs a d'>4 \f \staccato r a4 \p r
  % m.8
  g4 r g r
    }
    \new Staff = "cello" {
      \set Staff.instrumentName = "Violoncello"
      \set Staff.midiInstrument = "cello"
      % GM 42
      
      \clef bass \key a \major \time 4/4
  % m.1
  a,4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  gs,4 \f \staccato r r2
  % m.4
  R1
  % m.5
  g,4 \f \staccato r r2
  % m.6
  R1
  % m.7
  fs,4 \f \staccato r fs4 \p r
  % m.8
  f r e r
    }
    \new Staff = "basso" {
      \set Staff.instrumentName = "Basso"
      \set Staff.midiInstrument = "contrabass"
      % GM 43
      
      \clef bass \key a \major \time 4/4
  % m.1
  a,4 \f \staccato r4 r2
  % m.2
  R1
  % m.3
  gs,4 \f \staccato r r2
  % m.4
  R1
  % m.5
  g,4 \f \staccato r r2
  % m.6
  R1
  % m.7
  fs,4 \f \staccato r fs4 \p r
  % m.8
  f r e r
    }
  >>
  \layout { }
  \midi { }
}
```

## 谁拿了哪个音

从低往高数这一小节：

- **大提琴与低音提琴同度齐奏 `a,`**。整段最重的一次加倍给在最低音上，而且给的是单音，
  不是八度。低音区越厚，上面的层次越容易分清。
- **大管给 `<a cs'>`**，只有根音与三音，两个音都在低音区。它没有往上加八度，
  所以这一层听起来是"根音的重量"而不是"和弦"。
- **中提琴给 `<a e' a'>`**，三个音，跳过了三音。它填的是五度框架，不是完整和弦。
- **第一小提琴与第二小提琴给完全相同的 `<a e' cs'' a''>`**。这是全段唯一一次"整块加倍"：
  两个声部十三个音完全重合，音量翻了一档，代价是这两条线在这一小节里没有区别。
- **长笛给 `<cs''' a'''>`**，只拿最高的两个音，把和弦的顶端再抬一个八度。
- **双簧管给 `a''2`**，落在与小提琴同一音区，但它不是和弦的一击，而是一条长音线的起点。

这段的关键不在"用了多少人"，而在**省略**：中提琴少一个三音，大管只给两个音，长笛只给两个音，
低音只给单音。层次是靠"每一层缺什么"分开的，不是靠加人。把中提琴补成完整三和弦、
把大管加上八度，这段立刻糊成一片。

## 木管不是"加厚的弦乐"

同一个和弦，弦乐与木管的写法在这段里完全相反：

- 弦乐是 `f` + 断奏，一个和弦打在第 1 拍上，然后立刻放掉，后面三拍全空。
- 木管是 `f` 起音后马上 `fp`，把音**留住**，接着往下走。

双簧管的 `a''2` 之后接的是 `e''`、`cs''`、`fis''`——四个音分别落在和弦音上，
连起来是一条以和弦音为骨架的长线。它不是旋律，是"和声的余响被拉长了"。
同样，单簧管与小提琴在同一小节里走的是同一个和声，但一个是断奏的点，一个是延留的线。

这条差别直接决定写什么：**要让和声响一下，用弦乐短音；要让和声留一片，用木管长音。**
两者别倒过来——弦乐拉长音会失去起音的力量，木管奏断奏短音会失去音色的圆润。

## 定音鼓只钉一个音

这一小节定音鼓只给 `a,`，一个音，与低音同度。第 3 小节换成 `e`。
整段里只有它不随和声的完整形态变化——不管上面叠了几个音，它只钉主音和属音。

作用是把小节边界钉住。乐队全奏时，听者容易失去"拍子在哪"的定位，定音鼓给的正是这个定位，
而不是和声。写的时候要记住：定音鼓在和声上几乎不承担信息，它的任务是时间。

## 第 3 小节：换音，不换配器

第 3 小节是属和弦：第一小提琴与第二小提琴 `<e' b' e''>`，中提琴 `<gs b e'>`，
大提琴与低音提琴 `gs,`，长笛 `<b'' e'''>`，大管 `<gs b>`。

**声部一个没换，音区一个没换，只有音级变了。** 第 1 小节的第一小提琴是
`<a e' cs'' a''>`，第 3 小节是 `<e' b' e''>`——同样四根弦的位置、同样的断奏、同样的力度。

这是全段最值得学的一条：**段内保持配器不变，只换和声。** 听者会把两次全奏听成"同一件事在推进"；
如果第 3 小节换一批乐器、换一批音区，同样的和声进行会被听成两件事，段落感就散了。

反过来也成立：想让人听出"换段了"，最省力的办法不是改和声，是改配器。

## 定音鼓那个 a 什么时候变成五音

第 5 小节和声转到 A7：第一小提琴仍是 `<a e' cs'' a''>`，中提琴改成 `<g e' a'>`——
它在原来的 A 和弦里塞进一个 `g`，也就是小七度。低音走到 `g,`，成为七音在低声部。

注意分工：**第一小提琴给的是三和弦，中提琴给的是加了七度的版本。** 两个声部在同一小节里
对同一个和声给出不同的完整度，听感上就是"上面干净、中间有张力"。

第 7 小节落到 D 大调：第一小提琴 `<d' a' a''>`，中提琴 `<fs a d'>`，大提琴 `fs,`。
和声换了，声部一个没换，音区一个没换——还是"换音不换配器"。

**定音鼓只在 `a,` 与 `e` 之间切换。** 第 1 小节敲主音 `a,`，第 3 小节敲属和弦的根音 `e`，
第 5 小节回到 `a,`；第 7 小节和声已经走到 D 大调，它仍然敲 `a,`——这时 `a` 从主音变成了五音。

同一个音，功能换了，音没换。这是定音鼓在古典乐队里的基本用法：**它标记调性的两极（主与属），
不标记和弦的完整形态。** 决定色彩的三音与七音，交给木管和弦乐去说。

由此得到一条可操作的规则：给持续声部选音时，挑那个在整段每一处和声里都合法的音级
（主音或五音），不撞任何七音与导音。找到之后，这个声部不必逐小节跟着和声改，
它自己就成了一条持续线，同时把段落钉在原地。

反过来，如果让定音鼓去敲三音或七音，它就变成了和声的复述，既失去独立功能，
也失去了"这里没变"的参照。

## 四条可以照做的规则

一，**最重的加倍给最低音。** 低音厚了，上面才分得开；低音薄而上面厚，听感是悬空的。

二，**每层都要缺一个音。** 中提琴跳过三音、大管只给根音加三音——缺口就是层次。
全员给完整和弦，等于只有一层。

三，**短音与长音分给不同的组。** 弦乐给点，木管给线；倒过来两样都失效。

四，**钉时间的声部不要跟和声走。** 定音鼓只重复主音与属音，它的价值在稳定，不在变化。
