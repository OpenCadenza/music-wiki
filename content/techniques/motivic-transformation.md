# 动机变形：改哪个参数还算它

一个动机被改写之后听者还认不认得出，取决于**改了几个参数**，不取决于改得多厉害。同一个动机，把八度挪开、把和弦换掉，照样是它；一旦节奏型、连断、力度一起换掉，哪怕音高一个没动，听者也会当成新材料。

下面用两个体裁把这条界线画出来：钢琴 Op.10 No.1 第一乐章开头十六小节，四重奏 Op.18 No.4 第一乐章 mm.17–24。乐队的情况放到最后一节。

```lilypond title="贝多芬 Op.10 No.1 第一乐章" location="Allegro molto e con brio，mm.1–16"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.instrumentName = "Piano"
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key c \minor \time 3/4
      \tempo "Allegro molto e con brio" 2. = 76
      <ef' g' c''>4.\f r16 g'16([ ef''8. c''16] |
      g''8.[ ef''16 c'''8. g''16] ef'''4\staccato) |
      ef'''4\staccato r4 <g' c''>4\p |
      <g' c''>2( <g' b'>4) |
      <f' af' b'>4.\f r16 b'16([ f''8. d''16] |
      b''8.[ f''16 d'''8. b''16] f'''4\staccato) |
      f'''4\staccato r4 <b' d''>4\p |
      <b' d''>2( c''4) |
      \grace { c''16[ ef''] } g''4.( f''8 ef''4 |
      d''2 c''4) |
      \grace { g'32[ c'' ef''] } g''4.( f''8 <ef'' c''>4 |
      <d'' b'>2 c''4) |
      \grace { g'32[ c'' ef''] } <g' g''>4.( <f' f''>8) <ef' ef''>4(~ |
      <ef' ef''>4 <d' d''>\staccato) <c' c''>(~ |
      <c' c''>4 <b b'>\staccato) <af af'>(~ |
      \barNumberCheck #16
      <af af'>4 <g g'>\staccato) r4 |
    }
    \new Staff = "down" {
      \set Staff.instrumentName = ""
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key c \minor \time 3/4
      <c ef g c'>4.\f r8 r4 |
      R2. |
      r4 r \clef treble <c' ef'>4\p |
      <c' ef'>2( <d' f'>4) |
      \clef bass <d f af b d'>4.\f r8 r4 |
      R2. |
      r4 r \clef treble <d' f' af'>4\p |
      <d' f' af'>2( <ef' g'>4) |
      r4 r \clef bass <ef g c'>4( |
      <f af b>2 <ef g c'>4) |
      r4 r \clef treble <ef' g'>4( |
      <f' af'>2 <ef' g'>4) |
      \clef bass r4 r <ef g c'>4( |
      <f af b>2 <ef g>4 |
      <d f>2 <c ef>4 |
      <b, d>4) r4 r4 |
    }
  >>
  \layout { }
  \midi { }
}
```

## 动机由五个参数构成

第 1 小节的动机有五个可分离的参数：

一，**音程结构**。`<ef' g' c''>4.` 一个附点四分和弦之后，接 `g'16 ef''8. c''16 | g''8. ef''16 c'''8. g''16` 的上行分解链条——十六分与附点八分交替，一路从 g′ 爬到 ef‴。

二，**节奏型**。附点四分起头，后面全是"十六分 + 附点八分"的交替。

三，**音区**。g′–ef‴，三个八度。

四，**音色**。钢琴右手，单线条。

五，**力度轮廓**。ff 起，链条一路不减，落点 `ef'''4\staccato` 仍是 ff。

## 改一个参数：还是它

第 5–6 小节是同一个动机，只把音高换了：起头和弦变成 `<f' af' b'>4.`（B 减三和弦），链条换成 `b'16 f''8. d''16 | b''8. f''16 d'''8. b''16`，落点 f‴。

节奏型一模一样，音区范围一模一样（b′–f‴，仍是三个八度），连断一模一样（全是 staccato），力度一模一样（ff）。变的只有音高与它对应的和声——而且连内部音程都被新和弦改写了：第 1 小节的 g′→ef″ 是小六度，第 5 小节的 b′→f″ 是减五度。

**改一个参数，哪怕把内部音程都按新和弦重算，动机照样成立。**

这一条有物理原因：听者记住动机靠的是轮廓——上行还是下行、在哪里跳进、落在哪个音上——不是绝对频率。移调是最弱的变形，因为它改了频率、一个轮廓点都没动。反过来也成立：想让人听出"这是新材料"，光移调没有用。第 5–6 小节整段换了一个和弦、整体上移，听起来仍然只是"刚才那句话又说了一遍，位置高一点"。

## 改两个参数：要给提示

第 13–16 小节，动机变成 `<g' g''>4.( <f' f''>8) <ef' ef''>4(...)`。这里改了两个参数：

- **音区与织体**：原来单线条，现在每个音都加八度（g′+g″、f′+f″、ef′+ef″）。
- **力度**：第 13 小节起标 `rinf.`，第 15 小节起降到 p。

其余三个（音程结构、节奏型、连断）一个没动。听者仍认得出，但要靠上下文——它紧接在第 9–12 小节的单线条版本之后出现；单独拎出来，第一耳朵可能只听到"一串加厚的和弦"。

**改两个参数还能成立，但需要上下文提示。**

## 改三个以上：那是另一个动机

第 9–12 小节的 `g''4.( f''8 ef''4 | d''2 c''4)`（前面带 `\grace{c''16 ef''}` 倚音）与第 1–2 小节看起来很像：都以附点四分起头，都在右手，都接在 ff 之后。但四个参数全换了：

- **音程结构**：从上行分解和弦改成级进下行（g″→f″→ef″→d″→c″）。
- **节奏型**：从"十六分 + 附点八分"的链条改成"附点四分 + 八分 + 四分"。
- **连断**：从 staccato 改成连奏，还加了倚音。
- **力度**：ff 改成 p。

**改三个以上，哪怕起头长得一样，它就是另一个动机。** 这里"长得像"的唯一来源是那个附点四分——一个参数不足以构成身份。

一个可操作的自检：把变形后的片段单独弹一遍，不给上下文。如果听不出它和原动机的关系，那它已经是另一个动机了，不管谱面上还有多少音是重合的。第 9–12 小节就是过不了这一关的写法——它必须靠第 13–16 小节的加厚版本、以及后面回到主材料，才被听成"中间插进来的一段"，而不是"开头的变形"。

## 三种编制，三种最便宜的改法

**钢琴：改音程和音区最便宜。** 一个人两只手，换八度、换和弦不需要任何协调成本。上面三个例子就是这么做的：第 5 小节换和弦，第 13 小节加八度。

```lilypond title="贝多芬 Op.18 No.4 第一乐章" location="Allegro ma non tanto，mm.17–24"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "violinoone" {
      \set Staff.instrumentName = "Violino I."
      \set Staff.shortInstrumentName = "Vn I"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 4/4
      \tempo 4 = 138
      \set Score.currentBarNumber = #17
      g''8( g''') g'''2 f'''4~ |
      f'''4 ef'''2 df'''4~ |
      df'''8( c''') c'''( bf'') bf''( af'') g''\staccato fs''\staccato |
      g''4 r r8 g'\p( g'' f'') |
      f''( ef'') d''\staccato c''\staccato bf'\staccato af'\staccato g'\staccato fs'\staccato |
      a'4( g') r8 g'( g'' f'') |
      f''( ef'') d''\staccato c''\staccato bf'\staccato af'!\staccato g'\staccato fs'\staccato |
      \barNumberCheck #24
      a'8( g') r16 d''16\sf( ef'' fs') a'8( g') r16 d''16\sf( ef'' fs') |
    }
    \new Staff = "violinotwo" {
      \set Staff.instrumentName = "Violino II."
      \set Staff.shortInstrumentName = "Vn II"
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 4/4
      r4 g'4\ff( a' b') |
      c''( ef' f' g') |
      af'!( ef' c' c'') |
      b'8\fp d' d' d' d' d' d' d' |
      r ef' ef' ef' ef' ef' ef' ef' |
      r8 d' d' d' d' d' d' d' |
      r ef' ef' ef' ef' ef' ef' ef' |
      r8 <g d'> <g ef'>\sf <g ef'> r <g d'> <g ef'>\sf <g ef'> |
    }
    \new Staff = "viola" {
      \set Staff.instrumentName = "Viola"
      \set Staff.shortInstrumentName = "Va"
      \set Staff.midiInstrument = "viola"
      % GM 41
      \clef alto \key c \minor \time 4/4
      r4 g\ff( a b) |
      c'( ef f g) |
      af!( ef c c') |
      b8\fp b b b b b b b |
      r c' c' c' c' c' c' c' |
      b\fp b b b b b b b |
      r c' c' c' c' c' c' c' |
      r8 b c'\sf c' r b c'\sf c' |
    }
    \new Staff = "violoncello" {
      \set Staff.instrumentName = "Violoncello"
      \set Staff.shortInstrumentName = "Vc"
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass \key c \minor \time 4/4
      ef2\ff( d |
      c bf,) |
      af,2. af,4 |
      g,8\fp g g g g g g g |
      g,8 g g g g g g g |
      g,8 g g g g g g g |
      g,8 g g g g g g g |
      g,4\staccato c\sf\staccato g,\staccato c\sf\staccato |
    }
  >>
  \layout { }
  \midi { }
}
```

**四重奏：改声部归属最便宜，改音色最贵。** 四件弦乐器音色同质，把动机交给另一个声部，听者几乎听不出"换了乐器"。Op.18 No.4 第 17–19 小节正是这个代价的证据：`g'–a'–b'` 同时出现在第二小提琴（`g'4( a' b')`）和中提琴（`g4( a b)`），相差八度、同为 ff、同为连奏——听到的是一条加厚的线条，不是两个声部。要到第 20 小节，内声部改成同音重复（第二小提琴 `b'8 d' d' d'…`、中提琴 `b8 b b…`、大提琴 `g,8 g g…`），声部才真正分开。

所以四重奏的变形靠"谁在奏 + 用什么弓法"，不靠"换乐器"。第 24 小节那句 `r8 <g d'> <g ef'>\sf <g ef'>` 是三行同时给出的重音切分——分开靠的是节奏位置，不是音色。

代价在这里：四重奏要让人听出"动机换手了"，必须同时改音区或弓法。只改声部归属，等于没改——第 17–19 小节那对八度齐奏就是证明。

**乐队：改音色最便宜，改音程最贵。** 乐队有现成的音色库，把同一个动机从弦乐交给圆号，一个音符都不用改。Op.67 第一乐章那个四音细胞在 mm.1–2 由弦乐加单簧管奏出（谱例见[动机细胞怎样决定段落边界](../composers/beethoven/symphonies/motivic-cell.md)），第 18 小节原样交给圆号：记谱 `e''8[ e'' e'' ]`，Es 调圆号实音 g′ g′ g′，节奏、音程、力度全不动，只换乐器组。反过来，在乐队里改音程的代价最高——改一个音就要重新分配整块和声。

乐队还有一条独有的便利：**音色本身就能当结构标记。** 同一个动机每次换一组乐器，听者会自动把它听成"同一件事的不同阶段"，不需要任何音高上的提示。这是钢琴和四重奏都拿不到的——钢琴只有一种音色，四重奏的四种音色差得太小。

## 判断表

想让人认出是同一个动机：

| 参数 | 可以改 | 不要动 |
| --- | --- | --- |
| 音高 / 和声 | 随便改 | — |
| 音区 | 可改，改成八度加倍也行 | — |
| 音色 / 声部归属 | 可改 | — |
| 节奏型 | 只能微调（附点去点、时值等比例缩放） | 换成另一套时值组合 |
| 连断 | 最好不动 | 断奏改连奏，必须同时给力度提示 |

想让人听成新材料：**同时改音程结构、节奏型、连断这三样**，力度与音区顺带换掉就够彻底了。

## 可以照做的四条

一，**一次只改一个参数。** 要改两个，就把第二个写成渐进的——第 13 小节先加八度，第 15 小节才降力度。

二，**音程结构是身份，其余是衣服。** 音程一换，剩下的再像也不是它。

三，**按编制选最便宜的那个参数。** 钢琴改音区，四重奏改声部，乐队改音色。

四，**改三个以上就别叫它变形。** 那是新主题，应该给它自己的呈示。
