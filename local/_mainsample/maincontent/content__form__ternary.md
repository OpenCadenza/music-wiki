---
name: 三部曲式
description: 开头建立一个段落，中段形成对比，最后回归开头。复三部的各大段还可以有内部曲式。
---

# 三部曲式

**结构示意**　A → B → A 或 A′

单三部常用乐段组织三个部分。复三部则可在一个大段内部容纳二部等完整结构。区分再现二部和三部时，先找开头回归发生在哪一级。再现二部的回归仍在第二反复段内部，复三部的回归发生在中间大段完成以后。

## 莫扎特 K. 331 第二乐章

| 大段 | 调性与分界 |
| --- | --- |
| Menuetto | A 大调开头。第 1–18 小节为第一反复段，第 19–48 小节为第二反复段。第 31 小节已经带回开头主题，这次回归发生在 Menuetto 内部。 |
| Trio | D 大调开头。调号从三个升号减为两个，右手流动的八分音符与左手持续的 D 八度改变了段落性格。 |
| Menuetto D.C. | Trio 完结后，从头再奏 Menuetto，回到 A 大调。这一次回归完成整个乐章的 A–B–A。 |

先听 Menuetto 开头的倚音与强奏，再听同样的开头怎样在第二反复段内部回来。

```lilypond title="莫扎特 K.331 第二乐章" location="Menuetto，mm.1–8" id="k331-menuetto"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key a \major \time 3/4
      \set Score.tempoHideNote = ##t
      \tempo "Menuetto" 4 = 134
      \grace { cs'32[ e'] } a'2\f( e'4) |
      cs''8( d''16 b' a'4) r4 |
      e''8\p( fs''16 d'' cs''4) cs'''4-. |
      ds''4( e''4.) es''8-. |
      gs''8\>( fs'' e''! d''! cs'' b'\! |
      a' gs' e'' d'') r4 |
      b'8( a' fs'' e'') r4 |
      cs''8\f( b' g''! fs'') r4 |
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key a \major \time 3/4
      <a, a>2( <e, e>4) |
      <cs cs'>4( <a, a>4) r4 |
      r4 r4 \clef treble <a fs'>4-. |
      <b a'>4( <e' gs'>4) r4 |
      R2. |
      \clef bass e8( d' b d' b d' |
      e cs' a cs' a cs') |
      d8( b fs b fs b) |
    }
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="莫扎特 K.331 第二乐章" location="Menuetto 内部回归，mm.31–38" id="k331-return"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key a \major \time 3/4 \set Score.currentBarNumber = #31
      \set Score.tempoHideNote = ##t
      \tempo "Menuetto" 4 = 134
      \grace { cs'32[ e'] } a'2\f( e'4) |
      cs''8( d''16 b' a'4) r4 |
      e''8\p( fs''16 d'' cs''4) cs'''4-. |
      ds''4( e''4.) es''8-. |
      gs''8\>( fs'' e''! d''! cs'' b'\! |
      a' gs' e'' d'') r4 |
      b'8( a' fs'' e'') r4 |
      b'8\f( a' a'' g'') r4 |
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key a \major \time 3/4
      <a, a>2( <e, e>4) |
      <cs cs'>4( <a, a>4) r4 |
      r4 r4 \clef treble <a fs'>4-. |
      <b a'>4( <e' gs'>4) r4 |
      R2. |
      \clef bass e8( d' b d' b d' |
      e cs' a cs' a cs') |
      e8( cs' a cs' a cs') |
    }
  >>
  \layout { }
  \midi { }
}
```

Trio 的开头另起一层。弹到全段末尾的 D.C. 时，回到第一张谱例。

```lilypond title="莫扎特 K.331 第二乐章" location="Trio，mm.1–8（乐章第 49–56 小节）" id="k331-trio"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key d \major \time 3/4
      \set Score.tempoHideNote = ##t
      \tempo "Trio" 4 = 134 \voiceTwo
      <fs' a'>8\p( a <d' fs'> a <e' g'> a |
      <fs' a'> a) <d' fs'>( <cs' e'> <d' fs'> <e' g'>) |
      <fs' a'>( d' <g' b'> d' <g' cs''> e' |
      <fs' d''> a') <d' fs'>( <cs' e'> <d' fs'> <e' g'>) |
      <fs' a'>( d' <g' b'> d' <g' cs''> e' |
      <fs' d''>) a' <fs' d''> <e' cs''> <d' b'> <cs' a'> |
      <b gs'>( e' <cs' a'> e' <a' cs''> e' |
      <gs' b'> e') <fs' d''> <e' cs''> <d' b'> <cs' a'> |
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key d \major \time 3/4
      <d, d>2.~ |
      <d, d>4 r r |
      r4 r <a, a> |
      <d, d>4 \change Staff = "up" \voiceOne fs''8( e'' fs'' g'') |
      a''4( b'' cs''') |
      d'''4 \change Staff = "down" \oneVoice r4 r |
      e4 cs a, |
      e4 \change Staff = "up" \voiceOne d'''8( cs''' b'' a'') |
    }
  >>
  \layout { }
  \midi { }
}
```
