# 把终止推迟的四种手段

终止被推迟，指的不是"这一段没有终止"，而是听者在某一拍上已经知道下一个和弦应该是什么，音乐偏不给。期待先建立，然后被拖住。可量的指标有三个：属和弦一共响了几个小节、低音从属音走到主音走了几步、主和弦第一次出现时是不是原位。这三项决定了推迟有多长、有多明显。

推迟本身不区分体裁，但落地的手段区分。同一个目标在钢琴上靠音区与重复音，在四重奏里靠声部归属，在乐队里靠加倍与人数。下面四种手段，每种都按这三档写。

## 手段一：改低音的行进方向

属和弦期待的低音是"跳到属音、钉住、然后跳回主音"。把这段低音改成级进，期待就被拉长了：听者听得出方向（在往下走），但算不准什么时候停。

**钢琴。** Op.2 No.1 第一乐章 mm.93–101。左手从 m.93 起停在 c′ 上，四个断奏四分音符一小节，力度 pp；m.95 换成 `<c' df'!>`，m.96 `<bf df'>`，m.98 `<af c'>`，m.100 `<g bf e'>`，低音一路 c′–bf–af–g 级进下行，最后在 m.101 才落到 `<f af! c'>` 的原位主和弦。八小节的推迟，全部建在一条级进低音线上。右手与此同时在做另一件事：m.95 起每小节一个三连音音型，`af'–gf'–f'`、`ef'''–df'''–c'''`、`f'–e'–d'`……中音区与高音区交替，每小节换一次，m.97 起加 `cresc.`。低音在走，高音在跳，两个方向相反，听者被拉在中间。

```lilypond title="贝多芬 Op.2 No.1 第一乐章" location="mm.93–101"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key f \minor \time 4/4 \tempo 4 = 190
      <e'' e'''>4\pp\staccato r4 r2 |
      R1 |
      r4 r8 \tuplet 3/2 { af'16([ gf' f' ] } gf'4\staccato) r4 |
      r4 r8 \tuplet 3/2 { ef'''16([ df''' c''' ] } df'''4\staccato) r4 |
      r4 r8 \crescTextCresc \tuplet 3/2 { f'16\<([ e' d' ] } e'4\staccato) r4 |
      r4 r8 \tuplet 3/2 { df'''!16([ c''' b'' ] } c'''4\staccato) r4 |
      r4 r8 \tuplet 3/2 { ef'16([ d' c' ] } d'4\staccato) r4 |
      r4 r8 \tuplet 3/2 { c'''16([ bf'' a'' ] } bf''4\staccato) r4 \! |
      f'4\f\staccato af'!\staccato c''\staccato f''\staccato |
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key f \minor \time 4/4
      c'4\pp\staccato c'\staccato c'\staccato c'\staccato |
      c'\staccato c'\staccato c'\staccato c'\staccato |
      <c' df'!>\staccato <c' df'>\staccato <c' df'>\staccato <c' df'>\staccato |
      <bf df'>\staccato <bf df'>\staccato <bf df'>\staccato <bf df'>\staccato |
      <bf c'>\staccato <bf c'>\staccato <bf c'>\staccato <bf c'>\staccato |
      <af c'>\staccato <af c'>\staccato <af c'>\staccato <af c'>\staccato |
      <af bf!>\staccato <af bf>\staccato <af bf>\staccato <af bf>\staccato |
      <g bf e'>\staccato <g bf e'>\staccato <g bf e'>\staccato <g bf e'>\staccato |
      <f af! c'>4\f r4 r2 |
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

**四重奏。** 同样的级进，四重奏只能交给大提琴一个人走完，因为它只有一条低音线。其余三件不能跟着走，只能在上面保持——于是低音的每一步都变成一次"全队停下来等它"的动作。钢琴可以用两只手把级进和音型分开，四重奏分不开：低音一走，上方三个声部就得决定是留在原和声上还是跟着换，留下或换掉，都是一次可见的选择。

**乐队。** 低音提琴与大提琴齐奏级进，大管、低音长号加倍。人数越多，级进必须写得越慢——一小节一步，甚至两小节一步。写快了会被加倍的人数和音量的堆积糊掉，听者听到的是"一片低音在动"，不是"一条线在走"。

## 手段二：换和声目标

到了该解决的那一拍，不给主和弦，给别的。最常用的是六四和弦（听起来到了、其实没关门）、下属和弦（方向偏了半步）、导音和弦（必须再走一步才到主）。

**钢琴。** 还是上面那段：m.100 的 `<g bf e'>` 不是属七和弦，是导音 e♮ 上的减三和弦。它必须再走一步才到主，等于凭空多出一小节。左手的读法也变了——从"低音在级进"变成"低音已经在 g 上停住，剩下的是导音在响"。

**四重奏。** Op.18 No.4 第一乐章 mm.130–137。这一段的低音从 m.130 起就钉在 g 上：大提琴 `g,4\staccato b,\staccato d!\staccato g\staccato`（m.130），m.132 换成 `g,4\staccato c\staccato ef\staccato g\staccato`——一个 G 大三和弦、一个 c 小三和弦，两次都从 g 起。第一小提琴在同一段时间里把 g″ 反复钉住：`b'( g'') d''!( g'') fs''( g'') f''( g'')`，每两拍一次 g″。到 m.137，主题回来了——`c'2\fp ~ c'8[\grace{d'16[(c' b])} c'8( ef' d')]`，和全曲开头 m.1 的音型一模一样。但大提琴这一小节是 `g8 r8 f8 r8 ef8 r8 d8 r8`，低音还在往下走，没有落到 c。**主题回来了，调性没回来。** 这是四重奏里最有效的一种推迟：听者认出了旋律就以为到了，其实还差一小节。主音低音要到 m.138 才落。

```lilypond title="贝多芬 Op.18 No.4 第一乐章" location="mm.130–137"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "v1" {
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 4/4 \tempo 4 = 138
      b'8( g''8) d''!8( g''8) fs''8( g''8) f''8( g''8) |
      ef''8( g''8) r4 r4 g'8( g''8) |
      c''8( g''8) ef''8( g''8) fs''8( g''8) ef''8( g''8) |
      d''8( g''8) r4 r4 g'8( g''8) |
      af'8( g''8) b'8( g''8) d''8( g''8) ef''8( g''8) |
      f''!8( g''8) d''8( g''8) b'8( g''8) af'8( g''8) |
      g'8( g''8) f'8( f''8) ef'8( ef''8) d'8( d''8) |
      c'2\fp ~ c'8[ \grace { d'16[( c' b]) } c'8( ef' d')] |
    }
    \new Staff = "v2" {
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key c \minor \time 4/4
      \repeat unfold 16 { d'16 } |
      \repeat unfold 16 { ef'16 } |
      \repeat unfold 16 { ef'16 } |
      \repeat unfold 16 { <g f'>16 } |
      \repeat unfold 16 { <g f'>16 } |
      \repeat unfold 16 { <g f'>16 } |
      b16 \repeat unfold 15 { b'16 } |
      c''8\fp g4 g4 g4 b8 |
    }
    \new Staff = "va" {
      \set Staff.midiInstrument = "viola"
      % GM 41
      \clef alto \key c \minor \time 4/4
      \repeat unfold 16 { b16 } |
      b16 b16 b16 b16 \repeat unfold 12 { c'16 } |
      \repeat unfold 16 { c'16 } |
      c'16 c'16 c'16 c'16 \repeat unfold 12 { <b d'>16 } |
      \repeat unfold 16 { <b d'>16 } |
      \repeat unfold 16 { <b d'>16 } |
      \repeat unfold 16 { <g f'>16 } |
      <g ef'>8\fp ef4 ef4 ef4 f8 |
    }
    \new Staff = "vc" {
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass \key c \minor \time 4/4
      g,4\staccato b,\staccato d!\staccato g\staccato |
      g,4 r4 r2 |
      g,4\staccato c\staccato ef\staccato g\staccato |
      g,4 r4 r2 |
      g,8 r8 b,8 r8 d8 r8 g8 r8 |
      af8 r8 b8 r8 d'8 r8 ef'8 r8 |
      f'8 r8 d'8 r8 b8 r8 af8 r8 |
      g8 r8 f8 r8 ef8 r8 d8 r8 |
    }
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

**乐队。** 换和声目标在乐队里最常用的做法是换音色：主题回来时把旋律交给木管，低音仍在属上。听者先认出"是主题"（音色变了，轮廓没变），再发现"没回家"。钢琴做不到这一点——钢琴只有一个音色，要制造"到了但没到"，只能靠音区或力度；四重奏介于两者之间，靠换声部。

## 手段三：把主和弦写成转位

主和弦出现了，但低音不是主音。六四和弦最典型：听者听见了主和弦的三个音，同时听见低音还站在五音上，于是知道还要再落一次。

**钢琴。** 六四的用处是给右手争取时间。低音在五音上，和声没关门，右手可以继续做音型（三连音、琶音、颤音）；一旦写成原位，右手就必须停，因为终止已经完成。判断标准很实际：如果右手在"主和弦"上还想继续动，低音就不要给主音。

**四重奏。** 六四必须由四件乐器分工确认：大提琴给五音，中提琴给三音，两把小提琴在上面。任何一件提前落到主音，关门就失败了——这是四重奏特有的风险，因为四个声部同时发声，一个错音就能把六四变成原位。

**乐队。** 六四通常配定音鼓的属音和铜管的长音，让"没关门"这件事由整个乐队确认。人越多，六四越稳；也越难从六四走出来，因为每一件乐器都要同时换。

## 手段四：用织体增厚把解决推后

把属和弦铺满所有声部，让听者不知道哪一下才是解决。

**钢琴。** 重复音是最便宜的做法：Op.2 No.1 第一乐章 mm.93–100 的左手，一小节四个断奏和弦，音高在变、节奏型不变。密度上去了，方向感反而模糊——听者跟不上和声，只能跟着动。

**四重奏。** 上面那段 Op.18 No.4：属音 g 同时出现在大提琴的低音和第一小提琴的每个反拍上（`b'( g'') d''!( g'')`），两件乐器把同一个音钉死在两端。主题 m.137 进来时，听者不知道该跟旋律还是跟低音——这正是推迟生效的样子。

**乐队。** 同一条属音由低音提琴、大管、定音鼓三处同时给，加铜管长音，再叠一个全体渐强。乐队版的增厚不只是音量，是**同一时刻有太多件事在说"还没到"**：低音在钉、铜管在撑、定音鼓在敲、弦乐在渐强。解决被推到最后一下，是因为前面每一下都像。

## 什么时候必须直接解决

推迟过头会失去方向。三条界线：

一，属和弦持续超过四小节而中间没有新的和声事件，就是拖。Op.2 No.1 那八小节之所以不觉得长，是因为每两小节低音动一步、每小节右手换一次音区——一直有新信息。

二，呈示部之内必须解决。副部要立住，靠的是它自己的终止；在呈示部里拖，副部就变成了一段过渡。展开部末尾可以拖，因为听者本来就在等回家。再现部之后不能再拖——那会变成第二个展开部。

三，推迟的次数要数得清。一段里连续三次"以为要到了、结果没到"，第四次就必须真的到；否则听者不再相信任何一次属和弦。

## 写完一段怎么检查

三个问题，按顺序问：

1. 属和弦持续了几小节？（钢琴 2–6、四重奏 4–8、乐队 8–16——人数越多，听者能忍受的推迟越长，因为同时发生的事更多，注意力被分散了。）
2. 低音在这几小节里走了几步？（一步都没有 = 停滞，超过四步 = 听不出方向。级进两到四步最稳。）
3. 主和弦第一次出现是原位还是转位？（是原位而你又想继续写，说明你其实不想关门，那就把低音改回五音。）

三个答案凑在一起就是这段推迟的"长度"。长度定下来，再决定用什么手段：低音级进（改方向）、六四或导音和弦（换目标）、转位（不关门）、重复与加倍（增厚）。

同一种技法在别的体裁里怎么落地，见[室内乐](../composers/beethoven/chamber/index.md)与[四重奏](../composers/beethoven/quartets/index.md)两个分支；钢琴上的对应做法见[钢琴奏鸣曲](../composers/beethoven/piano/sonatas/index.md)。
