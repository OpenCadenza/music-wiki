# 独奏与乐队，什么时候谁让位

Op.61 第一乐章。协奏曲的分工常被说成"独奏与伴奏"，但谱面上写的是另一回事：两方都在不停地交出与收回发言权。判断谁在说话，不看乐器有多少，看三件事——谁在动、谁在持续、谁在高处。这篇把三次交接落到小节上。

```lilypond title="贝多芬 Op.61 第一乐章" location="Allegro ma non troppo，mm.1–16"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "flauto" {
      \set Staff.instrumentName = "Flauto"
      \set Staff.shortInstrumentName = "Fl"
      \set Staff.midiInstrument = "flute"
      % GM 73
      \clef treble \key d \major \time 4/4
      \tempo "Allegro, ma non troppo" 4 = 102
      R1*16
    }
    \new Staff = "oboi" {
      \set Staff.instrumentName = "Oboi"
      \set Staff.shortInstrumentName = "Ob"
      \set Staff.midiInstrument = "oboe"
      % GM 68
      \clef treble \key d \major \time 4/4
      R1 |
      << { a''2( b'' a''4 g''2) } \\ { d''1\p( cs''2.) } >>
      <d'' fs''>4( <b' e''> <a' d''> <g' cs''> <fs' d''>) |
      <cs'' e''>4 r4 r2 |
      <e'' g''>2( <d'' fs''> |
      <g'' b''>2.\sf\>) <fs'' a''>4( |
      <e'' g''>\!\p <d'' fs''> <cs'' e''>) << { a''8 e'' } \\ { cs''4 } >> |
      <e'' g''>2( <d'' fs''>4) r4 |
      R1*7
    }
    \new Staff = "clarinetti" {
      \set Staff.instrumentName = "Clarinetti in A."
      \set Staff.shortInstrumentName = "Cl"
      \set Staff.midiInstrument = "clarinet"
      % GM 71
      \transposition a
      \clef treble \key f \major \time 4/4
      R1 |
      <a' c''>2\p( <bf' d''> |
      <g' bf'>2.) <f' a'>4( <bf' d''> <a' c''> <g' bf'> <f' a'>) |
      <e' g'>4 r4 r2 |
      <g' bf'>2( <f' a'> |
      <bf' d''>2.\sf\>) <a' c''>4\!( |
      <g' bf'>\p <f' a'> <e' g'>) <e' g'>4 |
      <g' bf'>2( <f' a'>4) r4 |
      R1*5 |
      <a'' c'''>1\f~ |
      <a'' c'''>4 a''4( f'' d'') |
    }
    \new Staff = "fagotti" {
      \set Staff.instrumentName = "Fagotti"
      \set Staff.shortInstrumentName = "Fg"
      \set Staff.midiInstrument = "bassoon"
      % GM 70
      \clef bass \key d \major \time 4/4
      R1 |
      << { d'1\p~ d'2. } \\ { d'1~ d'2. } >>
      <d d'>4( <g b> <fs a> <e g> <d fs>) |
      << { a4 } \\ { a4 } >> r4 r2 |
      << { a1~ a1\sf\>~ a4\p a a } \\ { a1~ a1~ a4 a a } >>
      <a cs'>4 |
      <a cs'>2( <a d'>4) r4 |
      R1*7
    }
    \new Staff = "corni" {
      \set Staff.instrumentName = "Corni in D."
      \set Staff.shortInstrumentName = "Co"
      \set Staff.midiInstrument = "french horn"
      % GM 60
      \transposition d
      \clef treble \key c \major \time 4/4
      R1*16
    }
    \new Staff = "trombe" {
      \set Staff.instrumentName = "Trombe in D."
      \set Staff.shortInstrumentName = "Tb"
      \set Staff.midiInstrument = "trumpet"
      % GM 56
      \transposition d
      \clef treble \key c \major \time 4/4
      R1*16
    }
    \new Staff = "timpani" {
      \set Staff.instrumentName = \markup \column { "Timpani" "in D.A." }
      \set Staff.shortInstrumentName = "Ti"
      \set Staff.midiInstrument = "timpani"
      % GM 47
      \clef bass \key c \major \time 4/4
      d4\p d d d |
      d4 r r2 |
      R1 |
      r2 r4 d4\p |
      g,4 g, g, g, |
      g,4 r r2 |
      R1 |
      r4 g,4\p g, g, |
      d g, d r |
      R1*7
    }
    \new Staff = "violinoprincipale" {
      \set Staff.instrumentName = \markup \column { "Violino" "principale" }
      \set Staff.shortInstrumentName = "Vn pr"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key d \major \time 4/4
      R1*16
    }
    \new Staff = "violinoone" {
      \set Staff.instrumentName = "Violino I."
      \set Staff.shortInstrumentName = "Vn I"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key d \major \time 4/4
      R1*9 |
      ds'8\p r ds' r ds' r ds' r |
      cs'1\f |
      R1 |
      b'1\f~ |
      b'2\p( a' g' fs') |
      e'2~ e'8( d' cs' b) |
    }
    \new Staff = "violinotwo" {
      \set Staff.instrumentName = "Violino II."
      \set Staff.shortInstrumentName = "Vn II"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key d \major \time 4/4
      R1*10 |
      g1\f |
      ds'8\p r ds' r ds' r ds' r |
      g'1\f~ |
      g'2\p( fs' e' d') |
      b1 |
    }
    \new Staff = "viola" {
      \set Staff.instrumentName = "Viola"
      \set Staff.shortInstrumentName = "Va"
      \set Staff.midiInstrument = "viola"
      % GM 41
      \clef alto \key d \major \time 4/4
      R1*10 |
      e1\f |
      ds'8\p r ds' r ds' r ds' r |
      cs'1\f~ |
      cs'2\p( d' a1) |
      g1 |
    }
    \new Staff = "violoncello" {
      \set Staff.instrumentName = "Violoncello"
      \set Staff.shortInstrumentName = "Vc"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass \key d \major \time 4/4
      R1*10 |
      a,8\f r a, r a, r a, r |
      R1 |
      a,8\f r a, r a, r a, r |
      a,4\p a, r b, |
      r cs r d |
      r4 g, r2 |
    }
    \new Staff = "basso" {
      \set Staff.instrumentName = "Basso"
      \set Staff.shortInstrumentName = "Cb"
      \set Staff.midiInstrument = "contrabass"
      % GM 43
      \clef bass \key d \major \time 4/4
      R1*10 |
      a,8\f r a, r a, r a, r |
      R1 |
      a,8\f r a, r a, r a, r |
      a,4\p a, r b, |
      r cs r d |
      r4 g, r2 |
    }
  >>
  \layout { }
  \midi { }
}
```

## 乐队先开口，但不是全乐队

第 1 小节只有定音鼓：四拍 d，p。其余十二行全部休止。

第 2 小节双簧管进来，a″–b″–a″–g″（`a''2 b'' a''4 g''2`）；单簧管与大管在下面配和声，三件木管都标 p dolce。长笛、圆号、小号仍休止，全部弦乐也休止。

弦乐一直等到第 10 小节才进：第一小提琴 `ds'8 r ds' r ds' r ds' r`（p），第 11 小节 `cs'1`（f）。也就是说，乐队呈示部的前九小节，真正在说话的只有三件木管加一个定音鼓。

再往后数，乐队是分好几批到齐的：长笛与小号一直等到第 28 小节才第一次发声（长笛 `f''2\ff`，小号记谱 `<c' c''>`）。整个乐队凑齐的时候，呈示部已经过去了三分之一。

这个开头值得记下来：**乐队自己先让位。** 全奏是后面的事，第 1 小节只留给一件打击乐器——先把"这里很轻"写进配器，再让主题进来。

## 独奏进来时说的不是主题

乐队呈示部走到第 88 小节收尾。最后两小节已经在往薄里走：第 87 小节只剩大提琴与低音提琴，`a4 g e cs`；第 88 小节弦乐给一个上行三音 g″–e″–cs″ 作引子，然后交出去。

独奏小提琴在第 89 小节第 2 拍进——第 1 拍是四分休止 `r4`。

它说的不是双簧管第 2 小节那条线。第 89 小节独奏写的是 a′–cs″–e″，三个四分音符，每个前面带一个十六分倚音；第 90 小节接着 g″–a″–cs‴–e‴；第 91 小节落到 g‴。连起来是一条 A–C♯–E–G 的上行琶音，从 a′ 一直升到 g‴，是 D 大调的属七和弦。

主题一个音都不重合。所以独奏的第一次发言是**另起材料**，不是接主题。

更值得注意的是它进来时乐队在做什么。第 89 小节弦乐四行各按一个音：第一小提琴 g′、第二小提琴 g、中提琴 e、大提琴与低音提琴 a,。合起来是 A–E–G，**没有三音**。独奏的琶音第一个音就是 cs——它把乐队缺的那个音补上了。

这是协奏曲最经济的一种写法：乐队按住一个不完整的和弦，独奏进来把缺口填满。两边都没有让位，也都没有打架。

## 乐队退到什么程度

独奏进来之后，乐队分四步退。下面这九小节只留六行——独奏、四部弦乐、单簧管——四步在谱面上直接数得出来。

```lilypond title="贝多芬 Op.61 第一乐章" location="mm.88–96"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "clarinetti" {
      \set Staff.instrumentName = \markup \column { "Clarinetti" "in A." }
      \set Staff.shortInstrumentName = "Cl"
      \set Staff.midiInstrument = "clarinet"
      % GM 71
      \transposition a
      \clef treble \key f \major \time 4/4
      \set Score.currentBarNumber = #88
      \tempo 4 = 102
      R1 |
      R1 |
      R1 |
      <bf' e''>4\f r r2 |
      <bf' e''>4\f r r2 |
      <bf' e''>4\p r4 r2 |
      R1*3
    }
    \new Staff = "violinoprincipale" {
      \set Staff.instrumentName = \markup \column { "Violino" "principale" }
      \set Staff.shortInstrumentName = "Vn pr"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key d \major \time 4/4
      \override TupletNumber.transparent = ##t
      \override TupletBracket.transparent = ##t
      R1 |
      r4 \appoggiatura a16 a'4 \appoggiatura cs'16 cs''4 \appoggiatura e'16 e''4 |
      \appoggiatura g'16 g''4 \appoggiatura a'16 a''4 \appoggiatura cs''16 cs'''4 \appoggiatura e''16 e'''4 |
      \barNumberCheck #91
      \appoggiatura g''16 g'''2\sf~ \tuplet 3/2 { g'''8([ fs''' e'''] d'''[ e''' cs''']) } |
      \appoggiatura g''16 g'''2\sf~ \tuplet 3/2 { g'''8([ fs''' e'''] d'''[ e''' cs''']) g'''\p([ fs''' e'''] d'''[ e''' cs'''] d'''[ b'' cs'''] a''[ b'' g'']
      a''[ fs'' g''] e''[ fs'' d''] e''[ cs'' d''] b'[ cs'' a'] b'[ g' a'] fs'[ g' e'] fs'[ d' e'] cs'[ d' b]
      cs'[ a b] gs[ b a] gs[ b a] gs[ b a]) } |
      \barNumberCheck #97
    }
    \new Staff = "violinoone" {
      \set Staff.instrumentName = "Violino I."
      \set Staff.shortInstrumentName = "Vn I"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key d \major \time 4/4
      r4 g''4\p( e'' cs'') |
      g'1~ |
      g'1 |
      g'4\f r r2 |
      g'4\f r r2 |
      g'4\p r r2 |
      R1*3
    }
    \new Staff = "violinotwo" {
      \set Staff.instrumentName = "Violino II."
      \set Staff.shortInstrumentName = "Vn II"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key d \major \time 4/4
      r4 g'4\p( e' cs') |
      g1~ |
      g1 |
      cs'4\f r r2 |
      cs'4\f r r2 |
      cs'4\p r r2 |
      R1*3
    }
    \new Staff = "viola" {
      \set Staff.instrumentName = "Viola"
      \set Staff.shortInstrumentName = "Va"
      \set Staff.midiInstrument = "viola"
      % GM 41
      \clef alto \key d \major \time 4/4
      r4 e'4\p( cs' g) |
      e1~ |
      e1 |
      e4\f r r2 |
      e4\f r r2 |
      e4\p r r2 |
      R1*3
    }
    \new Staff = "violoncello" {
      \set Staff.instrumentName = "Violoncello"
      \set Staff.shortInstrumentName = "Vc"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass \key d \major \time 4/4
      a,1~ |
      a,1~ |
      a,1 |
      a,4\f r r2 |
      a,4\f r r2 |
      a,4\p r r2 |
      R1*3
    }
  >>
  \layout { }
  \midi { }
}
```


**第一步，木管、圆号、小号、定音鼓全部停手。** 第 89 小节这七行都是整小节休止（这一例里只截到单簧管那一行），一直到第 91 小节单簧管才回来一下（`<bf' e''>4`，记谱，A 调单簧管实音 g′–cs″）。

**第二步，弦乐从"声部"缩成"持续音"。** 第 89 小节第一小提琴写的是 `g'1~`，连到第 90 小节的 `g'1`——整两小节只有一个音。第二小提琴 g、中提琴 e、大提琴 a, 同样各按两小节。四行弦乐合成一个静止的和弦，谁都不动。

**第三步，连持续音也不给了。** 第 91 小节起，弦乐每小节只在第 1 拍给一个四分音符和弦（第一小提琴 g′、第二小提琴 cs′、中提琴 e、大提琴 a,），后三拍全空：`g'4\f r r2`。第 92、93 小节重复同样的写法。

**第四步，全停。** 第 94–96 小节，除独奏以外的十二行全部整小节休止——这一例截到的五行从第 94 小节起全空。独奏一个人跑完那串三连音，乐队一声不出。大管要到第 97 小节才回来。

所以答案是：**先留持续音，再缩成一拍一下，最后全停三小节。** 四步的次序不能倒：乐队全停会让独奏失去音准参照，乐队满编会把独奏淹掉；先给参照、再收参照、最后撤走，独奏才有一段完全归自己的时间。

## 两边同时说话靠什么分开

分开靠三样，但三样不是同时起作用的。

第 89 小节，音区几乎没分开：独奏第一个音 a′（A4）就在第一小提琴 g′（G4）上方一个大二度，贴着乐队的顶音进来。这时分开两方的是**动与不动**——乐队按着和弦不动，独奏在往上爬。两小节之内它爬到 g″–a″–cs‴–e‴，自己离开了那个和弦。

到第 91 小节，三样才一起用上：

- **音区。** 独奏在 g‴（G6），乐队最高音是第一小提琴的 g′（G4），第二小提琴 cs′、中提琴 e、大提琴 a, 全在下面。整整两个八度。
- **节奏。** 乐队只占第 1 拍，独奏占后三拍，而且是三连音（`\tuplet 3/2 { g'''8([ fs''' e'''] d'''[ e''' cs''']) }`）。一个是点，一个是流。
- **力度。** 乐队标 f，独奏标 sf 之后转 p。两边都写 f，会被听成一个整体，所以独奏的强音单独用 sf 标。

三条里最省力的是音区。第 91 小节只要把独奏放在 g‴，后面两条不写也分得开；反过来，音区重合时，节奏和力度写得再细也只是补救。

## 记谱调：三种调号，一个实音调

看谱面第一行的调号就能读出移调关系：弦乐两个升号（D 大调），单簧管一个降号（F 大调），圆号与小号没有升降号（C 大调）。三种调号，实音全落在 D 大调上。

- 单簧管 in A：`\key f \major` + `\transposition a`。第 2 小节记谱 `<a' c''>`，实音 f♯′–a′。
- 圆号 in D：`\key c \major` + `\transposition d`。
- 小号 in D：`\key c \major` + `\transposition d`。

定音鼓虽然也记 C 大调，但它不是移调乐器，不写 `\transposition`——它的记谱音就是实音。

这一条最容易出错：**记谱调按乐器写，实音调按作品写。** 漏掉 `\transposition`，播放时整条声部会整体移调，而谱面上看不出任何异常。

## 一个反例：全奏开场为什么不管用

如果第 1 小节就让全乐队砸一个主和弦，后面独奏进来时，听者会把它当成"少了一件乐器的乐队"，
而不是"另一个人开始说话"。原因很简单：全奏已经把所有音区占满了，独奏没有留下可以进入的位置。

Op.61 的做法正好相反：**开场先把位置空出来**。第 1 小节只给定音鼓，第 2 小节木管进来，
弦乐一直留到第 10 小节。空出来的不只是音区，还有"谁在说话"这件事本身——独奏后来能在同一片空地上开口，
靠的是开头就没有把这块地占满。

这条对写作的直接用处是：**协奏曲的第一小节，决定的是"留白在哪里"，不是"气势有多大"。**
把全奏写满，独奏就只能盖在上面；留出空白，独奏才能站进去。

## 可以照做的四条

一，**开场先决定谁不在。** 第 1 小节只给定音鼓，比"全奏加弱音器"更省，也更清楚。

二，**独奏第一次进来可以不接主题。** 换材料反而把两方分开；接主题会被听成"乐队少了一件乐器"。

三，**独奏进来时给乐队一个不完整的和弦。** 缺的那个音由独奏补，两边都不用让。

四，**退让分四步：停手 → 持续音 → 一拍一下 → 全停。** 按次序退，独奏始终有参照；一步退到底，它会悬空。
