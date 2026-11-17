# 变奏：改哪个参数才叫"另一个变奏"，而不是"同一段加了花"

写变奏最常见的失败不是写错音，是写了一串"同一段加了花"——每一段都能听出是主题，但没有一段像是另一个东西。问题不在技巧，在参数：你可能把六个变奏全花在同一个参数上。

一段主题可以被改动的只有五个参数。**音值细分**（把四分音符切成十六分）、**织体与音型**（柱式换成分解、齐奏换成琶音）、**音区**（上移或下移八度）、**和声密度与调式**（加厚、简化、或整段换同名小调）、**性格**（速度、拍号、力度轮廓）。这五个里，改前两个是"加了花"，改第三、第四个是"换了一件东西"，改第五个就接近"用主题写新曲"。

下面的两首作品正好把这条界线拉出来：Op.76 六首变奏曲从头到尾没有换过调式，Op.11 第三乐章在第四变奏就把整段搬进同名小调。

## 先把骨架指出来：Op.76 的主题

D 大调，2/4，`\tempo 4 = 88`，标着 Allegro risoluto。主题十六小节，两个八小节，每一半内部反复。

右手的想法很简单：第 1 小节先由上方二度 `<fs′ a′>` 喊一声，再用三个 `<d′ fs′>` 应三下；第 2 小节同一个"喊"接的是 `<d″ fs″>`，顶音跳到 d″；第 3 小节换成下行三度链，四个十六分 `<cs″ e″>–<b′ d″>–<a′ cs″>–<g′ b′>`；第 4 小节 `<d′ fs′>–<e′ g′>–<fs′ a′>` 收在强拍上。后半（第 9 至 16 小节）把同一套话搬到 `<fs′ d″>`、`<g′ e″>`、`<e′ g′ e″>`、`<fs′ a′ fs″>` 上，第 13 小节主题回来。

左手更省：第 1 到第 6 小节是**同一小节重复六次**——`<d, d>8\sf[d d d]`，一小节一个 D 八度，正拍一个 `\sf`。第 7 小节末尾换 `<fs, fs>`，第 8 小节（第一结尾）是 `<b,, b,>4\sf <cs, cs>`。

所以骨架是三样东西：一条每小节几乎不动的低音、一个"喊—应"的两拍单元、一条三度链。**变奏能不能成立，全看这三样还在不在。**

```lilypond title="贝多芬 Op.76 六首变奏曲" location="Tema. Allegro risoluto，mm.1–16"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble
      \key d \major
      \time 2/4
      \tempo 4 = 88
      <fs' a'>8\f^\markup { \bold "Allegro risoluto." }[( <d' fs'>) <d' fs'>\staccato <d' fs'>\staccato] |
      <fs' a'>8\sf[( <d' fs'>) <d' fs'>\staccato] <d'' fs''>\staccato |
      <cs'' e''>16 <b' d''> <a' cs''> <g' b'> <fs' a'>8\staccato <e' g'>\staccato |
      <d' fs'>8\staccato <e' g'>\staccato <fs' a'>4\sf |
      <fs' a'>8\sf[( <d' fs'>) <d' fs'>\staccato <d' fs'>\staccato] |
      <fs' a'>8\sf[( <d' fs'>) <d' fs'>\staccato] <d'' fs''>\staccato |
      <cs'' e''>16 <b' d''> <a' cs''> <g' b'> <fs' a'>8\staccato <cs' e' as'>\staccato |
      <b d' b'>4\sf <a! e' a'!> |
      <fs' d''>8\sf[( <d' b'>) <d' b'>\staccato <d' b'>\staccato] |
      <g' e''>8\sf[( <e' cs''>) <e' cs''>\staccato <e' cs''>\staccato] |
      <e' g' e''>8\sf( <e' g' cs''>) <e' g' e''>8\sf( <e' g' cs''>) |
      <fs' a' fs''>8\sf( <fs' a' d''>) <fs' a' fs''>8\sf( <fs' a' d''>) |
      <fs' a'>8\sf[( <d' fs'>) <d' fs'>\staccato <d' fs'>\staccato] |
      <fs' a'>8\sf[( <d' fs'>) <d' fs'>\staccato] <d'' fs''>\staccato |
      <cs'' e''>16 <b' d''> <a' cs''> <g' b'> <fs' a'>8\staccato <e' g' cs''>\staccato |
      <d' fs' d''>4 r |
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass
      \key d \major
      \time 2/4
      <d, d>8\sf[ d d d] |
      <d, d>8\sf[ d d d] |
      <d, d>8\sf[ d d d] |
      <d, d>8\sf[ d d d] |
      <d, d>8\sf[ d d d] |
      <d, d>8\sf[ d d d] |
      <d, d>8\sf[ d d <fs, fs>] |
      <b,, b,>4\sf <cs, cs> |
      <b,, b,>8\sf[ b, b, b,] |
      <a,, a,>8\sf[ a, a, a,] |
      <a,, a,>8\sf a, <a,, a,>\sf a, |
      <d, d>8\sf d <d, d>\sf d |
      <d, d>8\sf[ d d d] |
      <d, d>8\sf[ d d d] |
      <d, d>8\sf[ d d] <a,, a,>8 |
      <d, d>4 r |
    }
  >>
  \layout { }
  \midi { }
}
```

## 第一级：只改音值——同一段加了花

第 1 变奏（第 18 至 35 小节）是标准答案。右手变成连续十六分：第 18 小节 `a″16(b″ a″ g″) fs″(g″ a″ gs″)`，第 19 小节接着 `a″(b″ a″ g″) fs″ fs‴ e‴ d‴`。左手把柱式踏板拆成分解：第 18 小节 `fs′16(a′ d′ a′ d′ a′ fs′ a′)`，第 22 小节同一串原样再来。

三样骨架里有几样还在？低音还在——左手那串分解的和弦根音仍是 f♯′、d′、g′，落在 D 大三和弦与它的属上，跟主题第 1 到 6 小节的 D 八度是同一个和声；"喊—应"的两拍单元也还在，只是每拍被切成两个八分；三度链被邻音填满了（`a″–b″–a″–g″` 里 g″ 与 g♯″ 就是原来的 f♯ 与它的上邻音）。

所以它是"同一段加了花"。判据很硬：**把变奏的十六分按两两一组并回八分，它和主题第 1 小节的节奏完全重合**；把谱例和主题上下对齐，每个强拍的落点都在同一列。这就是装饰级——骨架、时间点、和声三样全部不动，只动了最表面那一层。

```lilypond title="贝多芬 Op.76 六首变奏曲" location="Var. I，mm.18–25"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble
      \key d \major
      \time 2/4
      \tempo 4 = 88
      a''16\p\<^\markup { \bold "VAR. I." }( b'' a'' g''\! fs''\> g'' a'' gs''\! |
      a''\< b'' a'' g''!\! fs''\> fs''' e''' d'''\! |
      cs''' c''' b'' d''' a'' gs'' g'' a'' |
      g'' fs'' a'' g'' a'' g'' a'' gs'' |
      a'' b'' a'' g''! fs'' g'' a'' gs'' |
      a'' b'' a'' g''! fs'' fs''' e''' d''' |
      cs''' c''' b'' d''' a'' gs'' a'' as'' |
      b''16 cs'''! a''! b'' a'' g''! fs'' g'') |
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble
      \key d \major
      \time 2/4
      fs'16\p( a' d' a' d' a' fs' a' |
      fs' a' d' a' d' d'' cs'' b' |
      a' d'' g' d'' fs' a' e' a' |
      d' a' e' a' e' a' es' a' |
      fs'16 a' d' a' d' a' fs' a' |
      fs' a' d' a' d' d'' cs'' b' |
      a' d'' g' d'' fs' d'' fs' e'' |
      b' d'' cs'' e'' cs''[ e'']) d'( e') |
    }
  >>
  \layout { }
  \midi { }
}
```

## 第二级：改织体、音区或性格——同一句话换了嘴脸

Op.76 六个变奏里有三个动了拍号。第 3 变奏（第 52 至 70 小节）把 `\time` 改成 6/8，标 `sempre dolce`：主题那个两拍的"喊—应"在 6/8 里变成三拍单元，重音位置从每两拍一次变成每三拍一次，Allegro risoluto 的锐角被磨平。第 6 变奏（第 105 至 163 小节）改 3/4，并且标 Presto——同一首曲子的拍速从 88 变成 Presto，性格从"果断"直接跳到"急板"。Coda（第 164 至 189 小节）标 `Tempo I.`，回到 2/4 和原速。

这三段的骨架音和低音线都还在，但听感上已经是另一件事。原因是它们动的是"时间被切成什么单位"，而人耳最先锁定的就是韵律单位：一小节两拍变三拍，主题的身份证就换了一半。

判据：**变奏的每小节拍数和主题不同（或者速度标记换了档），就是这一级。** 它比装饰级高一级，因为听者不需要对比谱面就能察觉；但它还不是"换内容"——你把 6/8 的三个八分并成两组，主题的原速节奏仍然能听出来。

## 第三级：改调式——换内容

到这一步，变的不是表面，是和声骨架本身。

Op.11 第三乐章（主题是《Pria ch'io l'impegno》）给了最干净的对照。主题是 B♭ 大调（源码 `\key bf \major`），十六小节。第 4 变奏（第 66 至 81 小节）把调号换成 `\key bf \minor`，标 `Minore`；第 5 变奏（第 82 至 97 小节）换回 `\key bf \major`，标 `Maggiore`；第 7 变奏（第 114 至 129 小节）又是 `\key bf \minor`。这三处换调号的位置，都是各自前一段双纵线的下一条小节线。

主题本身长这样：钢琴右手从弱起 `bf′8 d″8 ef″8` 起，第 1 小节 `f″4 bf″4. c‴16(bf″)`；单簧管在第 4 小节末把这同一个弱起原样接过去（记谱 `c″8[e″ f″]`，实音 `bf′ d″ ef″`），从第 5 小节起主题转到管子上，钢琴右手退成 `<bf d′> <d′ f′> <bf d′>` 的伴奏音型。大提琴从第 1 小节起就是 `d8 bf f bf ef bf g bf` 的八分分解，钢琴左手是 `bf,4 r bf4 r` 的两拍脉冲。

```lilypond title="贝多芬 Op.11 钢琴三重奏第三乐章" location="Tema. Pria ch'io l'impegno，mm.1–16"
\version "2.26.0"
\language "english"

\score {
  <<
    \new Staff = "clar" {
      \set Staff.midiInstrument = "clarinet"
      % GM 71
      \transposition bf
      \clef treble
      \key c \major
      \time 4/4
      \tempo 4 = 146
      \partial 8*3 r8 r4 |
      R1 |
      R1 |
      R1 |
      r2 r8 c''8\staccato[ e''\staccato f''\staccato] |
      g''4\staccato c'''4.\sf d'''16( c''') b''8\staccato[ a''\staccato] |
      g''4\staccato e''4.\sf g''8\staccato[ f''\staccato e''\staccato] |
      d''8.( e''16) d''4\staccato r8 f''8\staccato[ e''\staccato d''\staccato] |
      c''8.( d''16) c''4\staccato r2 |
      R1 |
      r2 r8 c''8\staccato b'\staccato c''\staccato |
      d''\staccato[ g'\staccato] g''4.\sf f''8\staccato[ d''\staccato b'\staccato] |
      c''8( e'') g'4\staccato r2 |
      r4 g''4\p\staccato r a''\staccato |
      r8 g''8( c''' g'' e''4) r4 |
      r4 f''4\staccato r b''\staccato |
      c'''4\staccato r4 r8 r8 r4 |
    }
    \new Staff = "vc" {
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass
      \key bf \major
      \time 4/4
      \partial 8*3 r8 r4 |
      d8\p\staccato bf\staccato f\staccato bf\staccato ef\staccato bf\staccato g\staccato bf\staccato |
      d\staccato bf\staccato f\staccato bf\staccato d\staccato bf\staccato f\staccato bf\staccato |
      ef\staccato a\staccato f\staccato a\staccato ef\staccato a\staccato f\staccato a\staccato |
      d\staccato bf\staccato d\staccato bf\staccato d4 r |
      r4 bf4 r4 ef' |
      r4 bf r bf, |
      r f, r f |
      bf,4 <bf, f bf> <bf, f bf> r |
      ef8\p\staccato f\staccato ef\staccato f\staccato ef8\staccato f\staccato ef\staccato f\staccato |
      d f d f d f d f |
      f4\staccato a\staccato c'\staccato r |
      f4\staccato bf\staccato d'\staccato r |
      r4 d'\p\staccato r ef'\staccato |
      r8 d'8( f' d' bf4) r4 |
      r4 a4\staccato r ef'\staccato |
      d'4\staccato <bf, f bf>4 <bf, f bf>8 r8 r4 |
    }
    \new PianoStaff <<
      \new Staff = "prh" {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \clef treble
        \key bf \major
        \time 4/4
        \partial 8*3 bf'8\staccato[ d''\staccato ef''\staccato] |
        f''4\staccato bf''4.\sf c'''16( bf'') a''8\staccato g''\staccato |
        f''4\staccato d''4.\sf f''8\staccato[ ef''\staccato d''\staccato] |
        c''8.( d''16) c''4\staccato r8 ef''8\staccato[ d''\staccato c''\staccato] |
        bf'8.( c''16) bf'4 r2 |
        r8 <bf d'> <d' f'> <bf d'> r <bf ef'> <ef' g'> <bf ef'> |
        r8 <bf d'> <d' f'> <bf d'> r <bf ef'> <ef' g'> <bf ef'> |
        r8 <a ef'> <ef' f'> <a ef'> r <a ef'> <ef' f'> <a ef'> |
        <bf d'> <d' f'> <bf d'> <d' f'> <bf d'> bf'8\staccato[ a'\staccato bf'\staccato] |
        c''8\staccato f'\staccato f''4.\sf ef''8\staccato c''\staccato a'\staccato |
        bf'8( d'') f'4 r2 |
        <f a ef'>8 f' <f a ef'> f' <f a ef'> f' <f a ef'> f' |
        <f bf d'> f' <f bf d'> f' r8 bf'8\staccato[ d''\staccato ef''\staccato] |
        f''4\staccato bf''4.\sf c'''16( bf'') a''8\staccato g''\staccato |
        f''4\staccato d''4.\sf f''8\staccato[ ef''\staccato d''\staccato] |
        c''8.( d''16) c''4\staccato r8 ef''8\staccato[ d''\staccato c''\staccato] |
        bf'8.( c''16) <d' bf'>4 r8 r8 r4 |
      }
      \new Staff = "plh" {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \clef bass
        \key bf \major
        \time 4/4
        \partial 8*3 r8 r4 |
        bf,4 r bf4 r |
        bf,4 r bf4 r |
        f,4 r f4 r |
        bf,4 <bf, bf> <bf, bf> r |
        <bf,, bf,>4 r <ef, ef> r |
        <bf,, bf,> r <bf,, bf,> r |
        <f, f> r <f, f> r |
        <bf,, bf,>4 <bf,, bf,> <bf,, bf,> r |
        f,4\staccato a,\staccato c\staccato r |
        f,\staccato bf,\staccato d\staccato r |
        f,\staccato a,\staccato c\staccato r |
        f,\staccato bf,\staccato d\staccato r |
        bf,8 d f bf bf, ef g bf |
        bf, d f bf bf, d f bf |
        f, a, c f f, a, c f |
        bf,,8 bf, bf,, bf, bf,, r8 r4 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

同名小调意味着什么？主题的每个三度音与六度音降半音：原来落在 d″ 上的骨架音变成 d♭″，原来落在 g′ 上的变成 g♭′。低音线和小节数可以一字不动，但同一串低音上面现在挂着另一套和弦——原来是大三和弦的地方变成小三和弦，属和弦的导音换了方向。听者认得出的只剩轮廓。

**这就是"变奏"与"用主题写新曲"的分界线。** 越过它之后，你写的仍然可以叫变奏，但它和主题的联系已经只靠低音线与句长撑着。

## 变奏之间怎么连：两种分界法

Op.76 的两段之间是用材料连的。主题在 16 小节收住，第 17 小节不是空白——它已经开始第 1 变奏的十六分跑句（`r a″16(b″ a″ g″)`），也就是下一段的弱起。听者不会感到"换了一段"，他会觉得上一句的尾巴被接着说了下去。

Op.11 第三乐章用的是另一种分界法：**换人**。主题在第 16 小节打完双纵线，第 1 变奏（第 17 至 32 小节）整整十六小节里，单簧管一个音也没奏，大提琴也全是整小节休止——台上只剩钢琴。它不靠材料连接，靠"谁不响了"来划界。这在一台钢琴上做不到，在三重奏里是最省力的一种分段。

两种分界法可以叠用，但不能都不用：如果上一段的尾巴直接停住、下一段又从正拍重新开始、而且人声编制也没变，听者会以为中间漏了一小节。

## 不同编制，可改的参数不同

Op.76 是钢琴独奏。整首曲子里 `\key d \major` 只出现过一处，六个变奏加 Coda 全部在 D 大调——**它一个调式也没改**。它改的是音值、音型、音区、拍号、速度，也就是前两级。这不是 Beethoven 保守，是独奏这件编制的参数表就这么长：一台琴能同时给十个音，能在一瞬间换音型换音区，但它没有"换一件乐器来说"这个选项。

Op.11 第三乐章多出来两个参数。第一是**声部归属**：主题第 1 至 4 小节在钢琴右手（弱起 `bf′8 d″8 ef″8` 起），第 4 小节末单簧管把这个弱起原样接过去（记谱 `c″8[e″ f″]`，实音 `bf′ d″ ef″`），从第 5 小节起主题在管子上，钢琴右手退成 `<bf d′> <d′ f′> <bf d′>` 的伴奏音型。同一句主题，先说的人和后说的人不同，这本身就是一个变奏参数——而第 1 变奏干脆把另外两件全撤掉。

第二是**移调乐器的音色与记谱**。单簧管的谱面是 C 大调（零个升降号），另外三行是 B♭ 大调（两个降号），因为它写的是记谱音、实际低一个大二度（谱例里用 `\transposition bf` 让 MIDI 照实音出声）。换到单簧管来说，音色和音区同时变了一次，这在钢琴上是买不到的。

## 写完一段变奏，用三个问题过一遍

**一，把变奏和主题上下对齐：每个强拍的落点在同一列吗？** 在同一列、只是中间被填满了——这是装饰级，可以，但六个变奏里不能超过两段都是这个。

**二，低音线还在吗？每小节的根音、以及句末的终止式，和主题一致吗？** 在，而且调式没变——你只改了织体、音区或拍号，这是第二级。在，但调号换了（同名小调、同名大调）——这是第三级，已经越过"变奏"的中心区。

**三，如果低音线也不在了，你写的不是变奏**，是用主题的动机另写一首曲子。它可以是好曲子，但它不能算八段里的第三段——听者会在这里失去"这是同一首"的线索。

三个问题里第一个过不了，说明这段是装饰；第一个过了、第二个过了、第三个没过，说明你换的是内容；三个全过，才是一件合格的中级变奏。真正写坏的变奏，几乎都是六段全卡在第一级。
