# 两件乐器的平等不是各写一半，是谁在什么时候让位

小提琴奏鸣曲里的"平等"常被当成配器问题——好像两件乐器各分到等量的旋律、等量的小节，就算平等了。谱面上真正的平等是另一件事：谁先说、说几小节、另一件什么时候进来、进来以后是跟着走还是另起一条线、两件同时响的时候靠什么错开。这些都是可以量出来的参数，写在音符、休止和力度记号里。Op.47《克罗采》第一乐章把这几件事摆得很清楚，Op.30 No.2 第一乐章则给出一年前的做法，两个并排看，分工的变化就露出来了。

## 一、开头：小提琴独奏四小节，钢琴第 5 小节进

```lilypond title="贝多芬 Op.47 第一乐章" location="Adagio sostenuto，mm.1–12"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "violin" {
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key a \major \time 3/4 \tempo 4 = 32
      <a e' cs'' a''>4\f^\markup { \bold "Adagio sostenuto." }( <d'' fs''>\p <b' d''>)
      <gs' b'>4( <e' e''>4. <d' gs'>8)
      <cs' a'>4 <b fs' d''> <b gs' d''>
      << { d''4( cs''8) } \\ { <a e'>4. } >> r8 r4
      R2. R2. R2.
      r4 f''4_\markup { \italic "cresc." } <g! d' b' f''>4
      << { f''4( e''8) } \\ { <c' g' c''>4. } >> r8 r4
      r4 a''4_\markup { \italic "cresc." } <b fs'! ds'' a''>
      <e' b' a''>4( gs''2) ~
      gs''4( a''4. c''8\sf)
    }
    \new PianoStaff <<
      \new Staff = "pianoRH" {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \clef treble \key a \major \time 3/4
        R2. R2. R2. R2.
        <a' cs'' e'' a''>4\fp( <f' a' d'' f''> <d' a' d''>)
        << { b'4 <gs' e''>4.( gs'8) } \\ { <d' a'>4 ~ d'8[ b( e' d')] } >>
        a'4\staccato_\markup { \italic "cresc." }( <d' d''>4\staccato <d' d''>\staccato)
        <d' fs'! a' d''>4\p ~ <d' g' d''>8 r r4
        r4 <g' e''>4\staccato_\markup { \italic "cresc." }( <a' e''>4\staccato)
        << { e''4( ds''8) } \\ { a'4. } >> r8 r4
        r4 <b d'! gs'!>4\p <b c' gs'>4 ~
        <a c' gs'>( <a c' a'>) <a c' d'>4\sf
      }
      \new Staff = "pianoLH" {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \clef bass \key a \major \time 3/4
        R2. R2. R2. R2.
        <a,, a,>4\fp( <d, d> <f, f>)
        << { e2 \stemDown e4 } \\ { e,4. s8 s4 } >>
        << { c'8.( b16) a8([ a b c']) c'4( b8) } \\ { f2 fs4 g4. } >> r8 r4
        r4 <c' e'>4\staccato( <c' e'>\staccato)
        <b fs'!>4. r8 r4
        r4 e,4 e,(
        f,) <f,, f,>( <fs,, fs,>)
      }
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

第 1 小节只有小提琴。它拉的是 `<a e' cs'' a''>`——a、e′、c♯″、a″，一个 A 大三和弦的四个音，力度 f。同一小节第三拍换成 `<b' d''>` 时力度已经降到 p。四小节之内，小提琴没有给出一个单音的旋律，给的全是和弦与双音。

这四小节不是平铺，而是有方向的。把每小节的最高音抓出来排成一行：m.1 的 a″，m.2 的 e″（`<e' e''>4.`），m.3 的 d″（`<b fs' d''>`），m.4 的 c♯″（`d''4( cs''8)`）。一条下行的顶线，四小节掉了整整一个小六度；同时厚度也在减——m.1 是四音和弦，m.2、m.3 换成双音，m.4 的顶声只剩 d″ 到 c♯″ 两个音的来回。独奏的四小节因此有开头、有过程、有落点，不是一个等待对方进来的引子。

钢琴的谱面在前四小节是四行 `R2.`，一行一个空小节。真正的进入在第 5 小节：`<a' cs'' e'' a''>4\fp`——同一个 A 大三和弦，音域从 a′ 到 a″，比小提琴那个窄了两个八度，力度是 fp（先强，立刻收）。

第 5 到 7 小节，小提琴全休止（`R2. R2. R2.`），钢琴一个人说三小节：`<f' a' d'' f''>`、`<d' a' d''>`、`<gs' e''>`、`a'4\staccato( <d' d''> <d' d''>)`。第 8 小节小提琴回来，第一拍是休止，第二拍才进 `f''4`。

所以开头的分配是 4 + 3 + 一起，不是各四小节。谁独奏、独奏几小节，是写谱时定下的结构参数。

## 二、进入以后：另起一条线，不是跟着

钢琴第 5 小节的进入容易被听成"伴奏接上了"，谱面上看不是。三条证据。

音区。小提琴第 1 小节的和弦跨 a 到 a″，三个八度；钢琴第 5 小节是 a′ 到 a″，一个八度。同一个和弦被压进中音区，高音区空出来——空出来是给第 8 小节小提琴回来用的。

节奏型。小提琴 mm.1–3 是一小节三个和弦块（四分音符），钢琴 m.5 也是三个（`4 4 4`），看起来一致；但 m.6 起钢琴变成 `b'4 <gs' e''>4.( gs'8)`，右手拖长音，左手 `<d' a'>4 ~ d'8[ b( e' d')]` 走八分音符。到 m.7 变成 `a'4\staccato(<d' d''>4\staccato <d' d''>\staccato)`，全是断奏。三小节里换了两次句法，这不是伴奏的做法。

力度。小提琴 m.1 内部从 f 掉到 p；钢琴 m.5 的 fp 是"打一下再收"；m.7 起标 cresc.。两件乐器的力度曲线从一开始就错开，谁也不跟谁的呼吸。

## 三、快板主题归小提琴，钢琴给骨架

```lilypond title="贝多芬 Op.47 第一乐章" location="Presto，mm.18–26"
\version "2.26.0"
\language "english"

\score {
  \new StaffGroup <<
    \new Staff = "violin" {
      \set Staff.midiInstrument = "violin"
      % GM 40
      \clef treble \key a \minor \time 4/4 \tempo 2 = 142
      \partial 4 e''4( f''2.\sf^\markup { \bold "Presto." })
      a'4 gs'4\staccato e'\staccato e'\staccato gs'\staccato
      a'4\staccato e'\staccato e'\staccato a'\staccato b'\staccato e'\staccato e'\staccato b'\staccato
      c''4\staccato_\markup { \italic "cresc." } a'\staccato a'\staccato c''\staccato
      c''\staccato a'\staccato a'\staccato c''\staccato d''1_\markup { \italic "rallent." }
      <g d' b' g''>1\sf
    }
    \new PianoStaff <<
      \new Staff = "pianoRH" {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \clef treble \key a \minor \time 4/4
        \partial 4 r4 <a d' f'>2.\sf
        <a d'>4 <gs b e'>4 r r2
        <c' e' g'>4 r r2
        <gs b e'>4 r r2 <c' e' g'>4_\markup { \italic "cresc." } r r2
        <c' e' g'>4 r <c' e' g'> r
        <b d' g'>4_\markup { \italic "rallent." } r r2
        <g b d' g'>4\sf r r2
      }
      \new Staff = "pianoLH" {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \clef bass \key a \minor \time 4/4
        \partial 4 r4 <d, d>2.\sf
        <f, f>4 <e, e>4 r r2
        a,4 r r2
        <e, e>4 r r2 <a,, a,>4_\markup { \italic "cresc." } r r2
        <a,, a,>4 r <a,, a,> r
        <g,, g,>4_\markup { \italic "rallent." } r r2
        <g,, g,>4\sf r r2
      }
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
```

快板从第 18 小节的弱起开始，主题在小提琴：`e''4( f''2.\sf)`。同一小节钢琴是 `\partial 4 r4 <a d' f'>2.\sf`——一个 a–d′–f′ 的和弦，不是主题。

第 19 小节起，小提琴是一串断奏四分音符：`a' gs' e' e' gs'`，然后 `a' e' e' a'`、`b' e' e' b'`、`c'' a' a' c''`。钢琴同时是"和弦 + 长休止"：`<a d'>4 <gs b e'>4 r r2`、`<c' e' g'>4 r r2`，每个和弦后面空两拍。

这就是分工：小提琴给主题的音高序列，钢琴给拍点与和声骨架。第 25 小节的小提琴 `d''1`（rallent.）和第 26 小节的 `<g d' b' g''>1\sf` 是这段的收口，钢琴在同样的位置给 `<b d' g'>4\sf` 与 `<g,, g,>4\sf`——三行谱同一个 G 大三和弦。

## 四、主题换手时改了什么

主题第一次到钢琴手上是第 27 小节：`e''4\p( <f' f''>2.\sf) <d' a'>4\staccato <e' gs'>4\staccato`。

对照小提琴第 18 小节的 `e''4( f''2.\sf) a'4 gs'4\staccato`，改了三个地方：

一，单音变双音。小提琴的 `f''` 在钢琴上是 `<f' f''>`，加了低八度。

二，断奏的单线变和弦。小提琴的 `a'`、`gs'` 在钢琴上是 `<d' a'>`、`<e' gs'>`——a′ 补成了 d′–a′，g♯′ 补成了 e′–g♯′。旋律音没动（a′ 还在，g♯′ 还在），但每个音底下多了三度或四度。

三，力度记号跟着走。sf 保留在同一个位置。

所以"平等"不等于"复制"：同一个主题换手，作曲家不动旋律音，动的是每个音配几个音。这既是配器，也是让位——小提琴把主题让出来的时候，钢琴接过去的不是原封不动的句子，而是加厚过的一个版本。

## 五、同时说话时靠什么不打架

两件乐器从第 8 小节起真正同时响。避免打架靠三样，都能在谱面上指出来。

第一，起拍轮流让。第 8 小节小提琴第一拍是 `r4`，钢琴第一拍给 `<d' fs'! a' d''>`；到第 9 小节反过来，小提琴第一拍是 `f''4`，钢琴第一拍是 `r4`。两件乐器在相邻两小节里交替占第一拍，谁也不在对方的强拍上撞。

第二，一长一短。第 11 小节小提琴是 `<e' b' a''>4( gs''2)`——一个 gs″ 撑两拍多，加连线接到下一小节；钢琴同一小节的右手是 `r4 <b d'! gs'!>4\p <b c' gs'>4 ~`，两次发音。同一拍位上，一件在拖，一件在点。

第三，音区分层。小提琴的持续音落在 a″–gs″，钢琴右手和弦的顶音到 e″ 为止，左手在 `<d, d>`、`<a,, a,>`、`<g,, g,>` 这些低音上。中间那一层（c′–e″）归钢琴右手，上面那一层（f″–a″）归小提琴。两件乐器共用同一个和声，但不在同一个八度里说话。

## 六、跟 Op.30 No.2 比一年之差

Op.30 No.2 第一乐章（C 小调，四分音符 138）的做法完全不同。第 1 小节钢琴就把主题说完整：`g'2.\p( ef'16 f' g' ef' c'4\staccato)`。小提琴的谱面是八个 `R1`——整整八小节不响。第 9 小节小提琴接过主题：`g''2.\p( ef''16 f'' g'' ef'' c''4\staccato)`，除了高一个八度，一个音都没改。

一年之后的 Op.47 换了一套分工。开头是小提琴独奏四小节，钢琴进来说的是**另一个材料**；快板主题归小提琴，钢琴给和弦；主题换手时（m.27）要重新配重。Op.30 No.2 是"同一材料先后陈述、另一件原样接过去"，Op.47 是"各持不同材料、换手时改写"。

前者靠 1:1 的移交取得平等，后者靠时机的分配取得平等。具体到写法上：如果想让两件乐器听上去平等，可以先决定三件事——谁先开口、独奏几小节、对方进来时给的是主题还是和声。这三件事定了，配器只是把它们落到音符上。

## 三条可以带走的规则

一，独奏的时长要能被数出来，而且要和后面的段落长度成比例。Op.47 的 Adagio 开头是 4（小提琴）+ 3（钢琴）+ 一起，两个数字都短，但都可以在小节线上数清。写的时候先定这两个数，再定音符。

二，另一件乐器进来时，别让它重复先开口那件刚说过的东西。Op.47 的钢琴在第 5 小节给的是同一个和弦、不同的音区、不同的节奏型；同一材料也可以用，但要换一个参数（音区、句法、力度，至少一个）。

三，主题换手时改密度，不改轮廓。单音加八度、单线补成和弦，都是加法；反过来，把和弦拆成单音也行。轮廓一改，听者就认不出这是同一个主题，换手也就失去了意义。

同体裁的其它分工方式，见[四重奏](../quartets/index.md)与[钢琴奏鸣曲](../piano/sonatas/index.md)两个分支；本分支的编制与移调问题见[室内乐](index.md)。
