# 只有两个乐章时，结构重量往哪里挪

Op.90 是贝多芬中期最短的奏鸣曲之一，只有两个乐章：e 小调的第一乐章，E 大调的回旋曲。四乐章奏鸣曲里，第一乐章与末乐章之间靠小步舞曲或谐谑曲隔开，那一段的功能是卸力——速度放慢，句法打碎，让听者从第一乐章的张力里退出来，再走进末乐章。Op.90 把这一段砍掉了，于是重量必须重新分配：第一乐章要自己把张力花完，第二乐章要同时承担"慢"与"收"。

两个乐章的基本参数先摆出来。第一乐章 3/4 拍，四分音符 156，标记"Mit Lebhaftigkeit und durchaus mit Empfindung und Ausdruck"（活泼地，且始终带着感情与表情）。第二乐章 2/4 拍，四分音符 72，标记"Nicht zu geschwind und sehr singbar vorgetragen"（不要太快，要非常歌唱地奏出）。速度比大约 2.2 比 1。这个比例并不悬殊，但两乐章之间没有任何过渡段落：第一乐章一停，第二乐章就开口。

## 一、前十五小节：张力自己花掉

```lilypond title="贝多芬 Op.90 第一乐章" location="mm.1–15"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble
      \key e \minor
      \time 3/4
      \tempo 4 = 156
      \override Score.MetronomeMark.transparent = ##t
      % m.1：弱起和弦 g–b–e′–g′，e 小三和弦第一转位
      \partial 4 <g b e' g'>8\f^\markup { \large "Mit Lebhaftigkeit und durchaus mit Empfindung und Ausdruck" } r
      << { g'4.( fs'8) } \\ { <g b e'>2 } >> <g e'>8 r <a fs' a'>8 r8 r4 <fs' a'>4\p
      <fs' a'>4.( g'8) <fs' a'>4\staccato( <g' b'>\staccato) r4 <b d' g' b'>8\f r8
      << { b'4.( a'8) } \\ { <b d' g'>2 } >> <b g'>8 r <cs' as' cs''>8 r r4 <as' cs''>4\p
      <as' cs''>4.( b'8) <as' cs''>4\staccato( <b' d''>\staccato) r4
      % m.8 起：动机被拆成单音，逐级下落
      d''4~ d''4( g'' e'' d'' c''!) c''~ c''( a'') c''(~ c'' b') b'(~ b' g'_\markup { \italic "dimin." }) g'(~ g' e')
      % m.14–15：只剩一条线，落在延长记号上
      \new Voice { e'4~ e'4\pp^\markup { \italic "ritard." } \change Staff = "down" \stemUp g4 e <ds b>2^\fermata }
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass
      \key e \minor
      \time 3/4
      \partial 4 <e, e>8\f r <e, e>2 <e, e>8 r <d, d>8 r r4 d'4\p <c' d'>4. <b d'>8 <a c'>4\staccato( <g b>4\staccato) r4
      <g, g>8\f r <g, g>2 <g,, g,>8 r <fs,, fs,>8 r r4 \clef treble fs'4 <e' fs'>4. <d' fs'>8
      <cs' e'>4\staccato( <b d'>4\staccato) r4 r << { <b g'>2.~ g'2 fs'4~ fs'2 } \\ { d'2 e'4~ <a e'>2 ef'4( d'2) } >>
      \clef bass \new Voice { fs'4( g'2 g4 e2 e'4 c'2) c4~ \stemDown <c, c>2. <b,, b,>2_\fermata }
    }
  >>
  \layout { }
  \midi { }
}
```

弱起是一个八分音符和弦 g–b–e′–g′，e 小三和弦的第一转位，强奏。第 1 至 2 小节，右手 g′ 附点四分音符落到 f♯′，左手在 e 与 b 上站住；同一小节后半，高音换成 f♯–a′ 的音型，力度降到 p。第 3 至 4 小节是答句，和弦换成 b–d′–g′，G 大三和弦的第一转位——根音从 e 上移三度到 g；第 4 小节右手出现 a♯–c♯，把 G 的稳定推开，指向 f♯。第 5 至 7 小节是同一句话的第二次陈述，音区更高，收在 b′–a′ 上。

第 8 小节起，主题不再成句。右手把四小节的单元拆成单音：d″–g″–e″–d″–c♮″，一路往下掉，每两拍换一次落点，力度从 f 经 dim. 到 pp。第 14 至 15 小节只剩一条线，右手越过谱表进到低音区，停在 b 与 d♯ 的延长记号上。

这就是第一乐章维持张力的办法：不靠新主题，靠减法。四小节的单元在 mm.1–7 里出现两次，第三次不出现，改成同一条轮廓的碎片；单元长度从四小节缩到两拍，音区从 g″ 掉到 e′，最后只剩一个延长记号。张力没有被解决，只是被放空了。

## 二、同名大调的影子：m.32 与 m.51

e 小调到 E 大调只差一个音：g 还是 g♯。第一乐章对这个 g♯ 极为吝啬。前十五小节里一个 g♯ 也没有；整章里 g♯ 出现的时候，几乎都带着任务，从不作为色彩停留。

m.32 是 d″–g♯″–b″–d‴，一个完整的 g♯ 小三和弦，落在 f 上，四小节之后就被后面的材料推走。m.51 更近一步：右手在 g♯–b 上方先给出 e″，记作 `<gs' b' e''!>`，这是 E 大三和弦的第一转位，g♯ 在低音；紧接着同一个 g♯–b 上方换成 e♭″（等于 d♯″），和弦变成 g♯ 小三和弦。两个和弦共用 g♯ 与 b，只差一个音，一个大三度，一个小三度，交替出现，力度 pp，还带断奏。

E 大调在第一乐章里始终是这个身份：借来的颜色，亮一拍就还回去。第一乐章最后收在 e 小调——末小节 `e,4 r4` 之前是 g–e–b 的 e 小三和弦，没有皮卡第三度。

## 三、第二乐章为什么必须换到同名大调

```lilypond title="贝多芬 Op.90 第二乐章" location="mm.1–15"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble
      \key e \major
      \time 2/4
      \tempo 4 = 72
      \override Score.MetronomeMark.transparent = ##t
      % m.1：叠句开口，旋律 e′–f♯′–g♯′–b′–a′–g♯′–f♯′
      \partial 8 << { e'16\p^\markup { \large "Nicht zu geschwind und sehr singbar vorgetragen." }( fs'
      gs'4 b'8 a' gs' fs') fs'8\staccato( gs'\staccato) a'8([ cs'' b' fs'] <b e' gs'>4) } \\
      { s8 e'16 b e' b gs' b fs' b e' b ds' b ds' b e' b e' b e' b fs' b ds' b s4 } >> r8
      e''16( fs'' <gs' gs''>4 <b' b''>8 <a' a''> <gs' gs''> <fs' fs''>) <fs' fs''>8\staccato( <gs' gs''>\staccato)
      <a' a''>8_\markup { \italic "cresc." }([ <cs'' cs'''> <b' b''>]) <ds'' ds'''>8\p\staccato
      <e'' e'''>4\staccato r8 b'8( as'4 e'' ds''4.) a'!8( gs'4 d''4 cs''4.) cs''8_\markup { \italic "cresc." }( bs'8 cs'')
      <cs' e' a'>8\staccato( <b! e' gs'>\staccato)
      << { gs'8( fs'4) fs'8 fs'([ b' as' b'] e'4) } \\ { <as e'>4 <a e'>4 <a ds'>8\p ds'4 ds'8 s4 } >> r8
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass
      \key e \major
      \time 2/4
      \partial 8 r8 <e, e>8\p r r4 <b,, b,>8 r r4 <cs, cs>8 r <ds, ds> <b,, b,> <e, e>16 gs b a gs a gs fs
      e16 b b, b e b b, b ds b b, b ds b es b fs b a b gs[ b] <b, fs>[ a] <e gs> b gs e ds b fs ds cs as fs cs fs, as fs cs
      b,16 b fs ds b, b cs a! b, gs e b, e, gs e b, a, a e cs a, e a, e gs, e a, e a, e b,! e cs e cs e c e c e
      b,16 fs b, <fs a> b, <fs a> b, <fs a>
    }
  >>
  \layout { }
  \midi { }
}
```

叠句一开口就是 e′–f♯′–g♯′–b′–a′–g♯′–f♯′。第三个音是 g♯——第一乐章欠了整章的那个音，在这里是旋律的第三个音，毫不迟疑。右手分成两层：上层是这条旋律，下层是十六分音符，下方音固定停在 b 上，上方音在 e′、g♯′、f♯′、d♯′ 之间换，每拍一次；左手只给 e 与 b 的低音。句尾落在 `<b e′ g♯′>` 上，b 在低音，E 大三和弦的第二转位。

所以第二乐章换到同名大调不是为了对比，是为了结账：第一乐章把 g♯ 藏起来，第二乐章一开口就把它放在最显眼的位置。同一个主音，换一种三度。这不是转调，是同名大小调的替换，调性中心一动没动。

## 四、末乐章的速度与织体怎么接住第一乐章留下的重量

第一乐章的速度是 156，第二乐章是 72。只看速度，第二乐章像慢乐章；但它的织体不是慢乐章的织体。右手下层的十六分音符从 m.1 起就不断，一小节八次，音型只换音高不换节奏；旋律每小节只用三到五个音，附点与连线的比重很大。慢的是旋律，动的是内声部。

这个搭配解决了两乐章方案最难的一处：末乐章不能真的慢下来，否则整首曲子没有终点；也不能快起来，否则第一乐章留下的重量没处放。办法是把"动"交给内声部，把"静"交给旋律。十六分音符提供匀速，旋律提供呼吸；速度写着 72，耳朵听到的密度却接近慢乐章。

叠句的反复承担同样的功能。回旋曲靠叠句回来维持长度，而叠句的材料与 m.1 完全一样，不做发展：同样的旋律，同样的十六分音符摆动，同样的 `<b e′ g♯′>` 收尾。第一乐章用减法把张力花掉，第二乐章用重复把时间填满——两种相反的手法，各自负责一半的结构重量。

同名小调在这个乐章里只出现一次，在 m.150 一带：两个小节，之后就被推到 C 大调去。e 小调在这里不是回家，是路过；它短到只能提醒听者第一乐章是什么调。

## 五、代价的另一面

砍掉一个乐章不只省时间，也改变了两端的关系。四乐章里，末乐章可以放肆：前面已经把话说尽，最后一段只需要跑起来。两乐章里没有这个余地——第二乐章是整首曲子的最后一句话，它必须同时是慢乐章和终曲。

收益在这里：没有任何一段是"过场"。Op.90 的第一乐章没有一个可以用作独立乐章的段落，它从 m.1 的弱起和弦一路推到 m.15 的延长记号，中间没有一次重复到可以抽出来单演；第二乐章同样没有一段是纯粹的过渡，连 m.150 那两小节同名小调也只是路过，不留段落感。整首曲子只有两个封闭的盒子，每个盒子里的材料都必须承重。

代价也很清楚：听者没有喘气的地方。第一乐章结束在 e 小调的强奏上，第二乐章紧接着在 E 大调上开口，中间隔的只是换调的那一个音。这不是贝多芬常用的手法——他通常更愿意给听众一个缓慢的转身。Op.90 把这个转身省掉了，换成一次同名大小调的直换。

## 小结

两乐章方案把结构重量分成两半。第一乐章承担"快"与"重"：主题在 mm.1–7 陈述两次，第 8 小节起被拆成碎片，第 14–15 小节放空到一个延长记号上；同名大调的 g♯ 只在 m.32 与 m.51 露头，每次都被立刻收回，末小节仍旧收在 e 小三和弦。第二乐章承担"慢"与"收"：同名大调一开口就把 g♯ 放在旋律第三音，右手十六分音符提供匀速，叠句反复提供长度。

被砍掉的谐谑曲并没有消失，它的两个功能被拆开了：一半变成第一乐章 m.14–15 的延长记号，那是"暂停"；一半变成第二乐章右手的十六分音符，那是"不推进的动"。
