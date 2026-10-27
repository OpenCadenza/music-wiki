# 呈示部怎样真正闭合

呈示部（exposition）的收尾不是"停下来"。三件事要在同一处同时成立：低音到主音、旋律到主音、紧邻的前一拍是一个完整的属七和弦（dominant seventh）。少一件，听者就知道后面还有。半终止（half cadence）最典型的失败是只做到"停在属音上"，另外两件一件都没做到。

## 半终止：所有声部都指向 5̂，而 1̂ 一次没到

Op.10 No.1 第一乐章（c 小调，3/4）第 91–92 小节。右手是一条下行的分解和弦：第 91 小节 b♭′–g′–g′–e♭′–e♭′–b♭，第 92 小节原样低八度再来一遍，落到 b♭（B♭2）。左手这两小节整小节休止。

三个细节要一起看。

一，落点是 b♭，也就是 E♭ 的 5̂。整条线一次也没碰到 1̂。二，低音完全缺席——不是"停在属音上"，是低音根本没有进来；半终止至少还该有一个属功能的和弦在下面托着。三，节奏上没有任何收的意思：第 92 小节最后两个音是 e♭ 与 b♭，都不延长，直接接下一小节。

所以第 92 小节听起来是"话说到一半、气用完了"，不是"说完了"。这就是半终止的位置：语法上合法，功能上不闭合。

前面第 88–90 小节是那口气的积蓄。第 88 小节右手从 e♭″ 起，左手给 b♭–e♭–g（A♭ 的 6/4）；第 89 小节换成一个减七和弦（a–e♭–f♯）；第 90 小节右手冲到 g″——全段最高的音——再退回来。冲上去、退下来、然后空着手往下走，这三步是一件事。

## 第一次三条同时成立

第 93 小节左手第一次进来：\ff，b♭ 的八度在最低处，右手给 f–a♭–b♭–d′。这是完整的 B♭7：根音、三音、五音、七音四个都在。

紧接着的一小节，低音落到 e♭（E♭2），右手给 e♭ 大三和弦。低音到主音、顶音到主音、前面一拍是完整属七——三条同时成立，这是这个呈示部第一处真正的完满终止（perfect authentic cadence）。

## 为什么不停在这一处

因为一次闭合只能"证明"调性，不能"钉住"它。从第 95 小节到第 105 小节，这十小节只干一件事：把同一条终止句子重来四遍，每一遍的低音都不一样。

`dol.` 结束部主题进来之后，每一遍的低音都是同一条下行：a♭–g–f，前面垫着 e♭–b♭–a。第 99 小节把第 95 小节原样再来一遍，第 102 小节起再来一遍，第 105 小节才落到 e♭ 大三和弦，低音 e♭、顶音 e♭′。

四遍终止，低音连起来是一条 a♭–g–f 的下行线，也就是 4̂–3̂–2̂。**重复的不是"句号"，是"下行"**：每一遍都把同一条线再走一次，四遍叠起来才是"落地"这一个动作。

这是结束部（closing section）钉住新调的第一种答案：靠一条被反复走的下行低音。判据很具体——把这四遍终止的低音抄下来排成一行。如果全是 e♭，你写的是四个句号；如果连成 a♭–g–f，你写的是一个结尾。

**贝多芬 Op.10 No.1 第一乐章，mm.88–105**

```lilypond
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble
      \key c \minor
      \time 3/4
      \tempo 4 = 164
      \set Score.barNumberVisibility = #all-bar-numbers-visible
      \override Score.BarNumber.break-visibility = ##(#t #t #t)
      \set Score.currentBarNumber = #88
       ef''4\sf\staccato r8. ef'16([ bf'8. g'16] ef''4\sf\staccato) r8. c''16([ fs''8. ef''16])
 g''4.\ff^"第90小节：冲到最高再退"( ef''8) ef''8([ bf']) bf'8( g') g'( ef') ef'( bf) \clef bass bf( g) g( ef) ef( bf,)
 r4 r <f af bf d'>^"第93小节：属七齐全，低音第一次进来"\sf( <g bf ef'>) r r
 \clef treble r4 << { bf'4 bf' c''( bf') } \\ { <d' f' af'>4_\markup { \italic "dol." } <d' f' af'> <ef' g'>2 } >> r4
 r4 << { d''4 d'' f''( ef'') } \\ { <f' af'>4 <f' af'> <g' bf'>2 } >> r4
 r4 << { bf'4 bf' c''( bf') } \\ { <d' f' af'>4 <d' f' af'> <ef' g'>2 } >> r4
 r4 \clef bass << { d'4 d' f'( ef') } \\ { <f af>4\p <f af> <g bf>2 } >> r4 r4 <f af d'>4 <f af d'>
 <af d' f'>2.( <g bf ef'>4) r4 r
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass
      \key c \minor
      \time 3/4
       r4 <bf, ef g>4\staccato r r <a, ef fs a>4\staccato r r <bf, ef g bf>4\staccato r R2.^"第91–92小节：左手整小节休止" R2. <bf,, bf,>2.\ff
 << { s4 bf,2^\fp ~ bf,2. } \\ { ef,4( bf, a, af,! g, f,)^"低音下行：e♭–b♭–a，然后 a♭–g–f" } >> ef,4( g, bf, bf,, f, bf,)
 << { s4 bf,2^\fp ~ bf,2. } \\ { ef,4( bf, a, af,! g, f,) } >> ef,4( g, bf, bf,, f, bf,)
 ef,4( g, bf, bf,, f, bf,) ef,4( g, bf,)^"最后一小节：低音 e♭、顶音 e♭′" ef4 r r
    }
  >>
  \layout { }
  \midi { }
}
```

## 另一种钉法：低音根本不动

Op.2 No.1 第一乐章（f 小调，4/4）的结束部（第 41–48 小节）走另一条路。

第 41–42 小节这句话：右手第 3 拍 c♭″（用一个 d′ 的倚音顶上去），第 4 拍落到 b♭′，第 42 小节再落到 a♭′ 与 g′。左手第 1 拍 a♭、第 2 拍 a♭′，第 4 拍给一个减七和弦 d–f–a♭–c♭（也就是 b–d–f–a♭）。第 42 小节左手第 2 拍给 e♭–a♭–c′（A♭ 大三和弦的第二转位），第 4 拍给 e♭–b♭–d♭。

最后那个和弦是关键：e♭–b♭–d♭ 是属七，但缺第三音 g。它不闭合——因为缺了 g，属七不成立为主和弦的"要求"，下一小节就没有必须解决的债。

这句话在第 43–44 小节原样再来一遍，第 45–46 小节旋律高八度再来一遍（c♭‴ 起）。三遍的落点都是同一个 e♭–b♭–d♭，三遍都欠着同一个 g。

第三遍之后，欠的东西才被补上：第 47 小节左手 a♭–b♭–d♭–e♭–g，右手 d♭′–g′–e♭″，\ff。g 终于出现，属七 e♭–g–b♭–d♭ 完整了。第 48 小节落到 a♭–c′–e♭′–a♭′，右手再叠 c″–e♭″–a♭″：大三和弦，c 出现了。

闭合的这一下不在低音。第 47 小节的低音已经是 a♭，第 48 小节还是 a♭，一动不动。闭合发生在上面——欠了三遍的 g 落到 a♭，d♭ 落到 c，同时 c 把 a♭ 定成大三和弦。

所以"低音到主音"不是唯一的闭合方式。低音可以一直站在主音上，这时判据换成另一条：**属七的七音与导音必须在下一个和弦里被解决掉，而且大三度必须在主和弦里出现。**Op.2 No.1 的第 47→48 小节，两件事都做了。

**贝多芬 Op.2 No.1 第一乐章，mm.41–48**

```lilypond
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble
      \key f \minor
      \time 4/4
      \tempo 4 = 190
      \set Score.barNumberVisibility = #all-bar-numbers-visible
      \override Score.BarNumber.break-visibility = ##(#t #t #t)
      \set Score.currentBarNumber = #41
      af4^"第41小节：低音先站住"
 r4 \acciaccatura d'16 cf''4._\markup { \italic "con espressione" }( bf'8) af'2^"旋律在这里停两拍" g'4.( ef''8)
 ef''4\sf( af'4) \acciaccatura d'16 cf''4.( bf'8) af'2 g'4.( ef''8) ef''4\sf( af'4)
 \acciaccatura d''16 cf'''4.( bf''8) af''2 g''4.( ef'''8) <df'' g'' ef'''>1^"第47小节：属七补上 g"\ff\> <c'' ef'' af''>4^"第48小节：落到 a♭ 大三和弦"\!\p r4 r 
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass
      \key f \minor
      \time 4/4
       af,4 af r <d f af cf'>\staccato r4 <ef af c'!>4\staccato r <ef bf df'!>4\staccato^"属七缺三音：g 一直欠着"
 r4 <af c'>\staccato r <d f af cf'>\staccato r <ef af c'!>\staccato r <ef bf df'!>\staccato
 r4 <af c'> \clef treble r <d' f' af' cf''> r <ef' af' c''!> r <ef' bf' df''!>
 <af bf df' ef' g'>1^"a♭ 加完整的 e♭7"\ff\> <af c' ef' af'>4^"主和弦，低音 a♭ 没有动"\!\p r4 r4 
    }
  >>
  \layout { }
  \midi { }
}
```

## 一种失败写法

每两小节一个完满终止。诊断方法不是听，是抄：把每个终止的低音和顶音写下来，排成两行。

如果低音全是同一个音，你写的是一串小结尾。如果顶音全是同一个音（常见的是停在 5̂，也有停在 3̂ 的），你写的是一串意犹未尽的半句。

反过来看 Op.2 No.1 那三遍陈述：它们的低音一直是 a♭，从来没有动过，为什么不散？因为每一遍都欠着同一个 g，在 g 出现之前，任何一遍都不能被当成句号。**终止式重复本身不构成"一串结尾"，构成"一串结尾"的是重复时没有欠债。**

## 两条可以带走的规则

一，闭合前的那一拍必须是完整的属七，四个音齐全。缺三音听起来悬着，缺七音听起来还没开始。Op.10 No.1 第 93 小节与 Op.2 No.1 第 47 小节都把这个和弦给全了，而且都给在 \ff 上——力度不是装饰，它是"这一下就是要落地"的信号。

二，重复终止时，让低音走一条线，或者让上方欠一个音。两条至少选一条。都做不到，就把终止的遍数减到一遍，把省下来的长度换成前面的一句铺垫——铺垫比第四个句号有用得多。
