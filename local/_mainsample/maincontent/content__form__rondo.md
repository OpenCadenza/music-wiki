---
name: 回旋曲式
description: 主调叠句在不同插部之间反复回来，典型五部布局为 A–B–A–C–A。
---

# 回旋曲式

**结构示意**　A → B → A → C → A → 尾声（可选）

先找反复出现的主调叠句，再判断两次叠句之间各发生了什么。插部可以换调、换织体，也可以借用叠句的动机。回接常在主调的属音附近积累张力。若早先离调的插部后来也在主调重现，并形成呈示与再现的对应，就有了辨认奏鸣回旋曲式的一条线索。

## 莫扎特 K. 545 第三乐章

| 功能 | 小节 | 读谱线索 |
| --- | --- | --- |
| A 叠句 | 弱起及 1–8 | C 大调。右手 E–G 双音先在弱起重复，随后进入两句相呼应的旋律。 |
| B 插部 | 9–16 | G 大调。十六分音符的连续流动接过叠句的短动机。 |
| 第一次回接 | 17–20 | G 和弦从插部调的主和弦转为 C 大调的属功能。 |
| A 叠句 | 21–28 | C 大调，叠句开头的双音回归。 |
| C 插部 | 29–48 | 以 a 小调为中心，展开较长的对比段。 |
| 第二次回接 | 49–52 | 从 a 小调的收束转向 C 大调的属和声。 |
| A 叠句 | 53–60 | C 大调，叠句第三次出现。 |
| 尾声 | 61–73 | 在 C 大调用反复的终止型和分解和弦收束。 |

```lilypond title="莫扎特 K.545 第三乐章" location="弱起及 mm.1–16" id="k545-ab"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key c \major \set Score.tempoHideNote = ##t \tempo "Allegretto" 4 = 112 \time 2/4 \partial 1*1/4 <e'' g''>8-.\mf <e'' g''>8-. |
        \set Timing.measureLength = #1/2 \set Score.currentBarNumber = #1 <c'' e''>8-. r8 <d'' f''>8-. <d'' f''>8-. |
        <b' d''>8\p r8 c''16( d''16 e''16 c''16 |
        a'16 b'16 c''16 cs''16 d''16 e''16 f''16 d''16 |
        c''16\f b'16 a'16 g'16) <e'' g''>8-. <e'' g''>8-. |
        <c'' e''>8-. r8 <f'' a''>8-. <f'' a''>8-. |
        <b' d''>8-. r8 a''16( g''16 f''16 e''16 |
        cs''16 d''16 e''16 f''16 a'16 c''16 b'16 d''16 |
        \set Timing.measureLength = #1/4 c''8-.) r8 \bar ":|." |
        \set Timing.measureLength = #1/4 e''16\mf( fs''16 g''16) g''16( |
        \set Timing.measureLength = #1/2 \set Score.currentBarNumber = #9 a''16 g''16 fs''16 e''16) d''16-. d''16-. d''16-. d''16-. |
        e''16( d''16 c''16 b'16) e'''16( d'''16 c'''16 b''16 |
        gs''16 a''16 b''16 c'''16 e''16 fs''16 g''16 a''16 |
        g''16\p fs''16 e''16 d''16) <b'' d'''>8-. <b'' d'''>8-. |
        <g'' b''>8-. r8 <a'' c'''>8-. <a'' c'''>8-. |
        <fs'' a''>8-. r8 g''16( a''16 b''16 g''16 |
        ds''16 e''16 g''16 e''16 d''16 b'16 c''16 a'16 |
        g'8) r8 g'16 a'16 b'16 c''16 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key c \major \time 2/4 \partial 1*1/4 \oneVoice r4 |
        \set Timing.measureLength = #1/2 \oneVoice <a c'>8-. <a c'>8-. <f a>8-. r8 |
        \oneVoice <g b>8-. <g b>8-. <e g>8-. r8 |
        \oneVoice f4.( d8 |
        \oneVoice g8) r8 r4 |
        \oneVoice <a c'>8-. <a c'>8-. <d f>8-. r8 |
        \oneVoice <g b>8-. <g b>8-. <c e>8-. r8 |
        \oneVoice <f a>4. <g f'>8 |
        \set Timing.measureLength = #1/4 \oneVoice <c' e'>8-. c8-. |
        \set Timing.measureLength = #1/4 \oneVoice c'16 g'16 e'16 g'16 |
        \set Timing.measureLength = #1/2 \oneVoice b16 g'16 d'16 g'16 \clef "bass" fs16 d'16 a16 d'16 |
        \oneVoice g16 d'16 b16 d'16 b,16 g16 d16 g16 |
        \oneVoice c16 a16 e16 a16 cs16 a16 e16 a16 |
        \oneVoice d8 r8 r4 \clef "treble" |
        \oneVoice <e' g'>8-. <e' g'>8-. <c' e'>8-. r8 |
        \oneVoice <d' fs'>8-. <d' fs'>8-. <b d'>8-. r8 \clef "bass" |
        \voiceOne g4.( fs8 |
        \oneVoice g8-.) g,8-. r4 |
      }
      \new Voice {
        \voiceTwo s1*1/4 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/4 |
        s1*1/4 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        c4( d4) |
        s1*1/2 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="莫扎特 K.545 第三乐章" location="mm.17–24" id="k545-b-return"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key c \major \set Score.tempoHideNote = ##t \tempo "Allegretto" 4 = 112 \set Score.currentBarNumber = #17 \time 2/4 d''8-. r8 b'16( c''16 d''16 e''16 |
        f''8-.) r8 d''16( e''16 f''16 g''16 |
        a''8) af''8-. g''8-. fs''8-. |
        f''8-. r8 s1*1/4 \bar "" |
        \set Timing.measureLength = #1/4 <e'' g''>8-.\mf <e'' g''>8-. |
        \set Timing.measureLength = #1/2 \set Score.currentBarNumber = #21 <c'' e''>8-. r8 <d'' f''>8-. <d'' f''>8-. |
        <b' d''>8-.\p r8 c''16( d''16 e''16 c''16 |
        a'16 b'16 c''16 cs''16 d''16 e''16 f''16 d''16 |
        c''16\f b'16 a'16 g'16) <e'' g''>8-. <e'' g''>8-. |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key c \major \time 2/4 <g b>8-. g,8-. r4 |
        <g b>8-. g,8-. r4 |
        R1*1/2 |
        r2 |
        \set Timing.measureLength = #1/4 s4 |
        \set Timing.measureLength = #1/2 <a c'>8-. <a c'>8-. <f a>8-. r8 |
        <g b>8-. <g b>8-. <e g>8-. r8 |
        f4.( d8 |
        g8) r8 r4 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="莫扎特 K.545 第三乐章" location="mm.29–36" id="k545-c"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key c \major \set Score.tempoHideNote = ##t \tempo "Allegretto" 4 = 112 \set Score.currentBarNumber = #29 \time 2/4 e''16( ds''16 f''16 e''16) r4 |
        e''16( ds''16 f''16 e''16) <e'' c'''>8-. <e'' c'''>8-. |
        <c'' a''>8-. r8 <d'' b''>8-. <d'' b''>8-. |
        <b' gs''>8-.\mf r8 a''16( e''16 c''16 a'16 |
        c''16 bf'16) bf'16-. bf'16-. d''16( cs''16) cs''16-. cs''16-. |
        e''16( d''16) f''16( e''16) g''16( f''16) f''16( e''16) |
        e''16( ds''16) c'''4\sf( ds''8) |
        e''8\f r8 b''16 gs''16 e''16 d''16 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key c \major \time 2/4 \oneVoice <a c'>8-. r8 <b d'>8-. <b d'>8-. |
        \oneVoice <gs b>8-. r8 r4 |
        \oneVoice e'16( ds'16 f'16 e'16) r4 |
        \oneVoice e'16( ds'16 f'16 e'16) \clef "treble" <c' e'>4 |
        \oneVoice <d' f'>4 <e' g'>4 |
        \voiceOne a'2 |
        \oneVoice <f' a'>8 r8 <f' a'>8 r8 \clef "bass" |
        \oneVoice e16 e'16 gs16 e'16 b16 e'16 gs16 e'16 |
      }
      \new Voice {
        \voiceTwo s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        s1*1/2 |
        f'8 cs'8 d'8 e'8 |
        s1*1/2 |
        s1*1/2 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="莫扎特 K.545 第三乐章" location="mm.49–60" id="k545-c-return"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key c \major \set Score.tempoHideNote = ##t \tempo "Allegretto" 4 = 112 \set Score.currentBarNumber = #49 \time 2/4 a'8 r8 gs'16( d''16 b'16 gs'16 |
        a'8) r8 gs'16( d''16 b'16 gs'16 |
        a'16^\markup { \italic "cresc." } e''16 c''16 a'16 b'16 f''16 d''16 b'16) |
        r4\fermata <e'' g''>8-. <e'' g''>8-. |
        <c'' e''>8-. r8 <d'' f''>8-. <d'' f''>8-. |
        <b' d''>8-.\p r8 c''16( d''16 e''16 c''16 |
        a'16 b'16 c''16 cs''16 d''16 e''16 f''16 d''16 |
        c''16\f b'16 a'16 g'16) <e'' g''>8-. <e'' g''>8-. |
        <c'' e''>8-. r8 <f'' a''>8-. <f'' a''>8-. |
        <b' d''>8-. r8 a''16( g''16 f''16 e''16 |
        cs''16 d''16 e''16 f''16 a'16 c''16 b'16 d''16 |
        c''8-.) r8 b'16 f''16 d''16 b'16 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key c \major \time 2/4 a16 c'16 e'16 c'16 e16 b16 d'16 b16 |
        a16 c'16 e'16 c'16 e16 b16 d'16 b16 |
        a16 c'16 e'16 c'16 g16 d'16 f'16 d'16 |
        r4\fermata r4 |
        <a c'>8-. <a c'>8-. <f a>8-. r8 |
        <g b>8-. <g b>8-. <e g>8-. r8 |
        f4.( d8 |
        g8) r8 r4 |
        <a c'>8-. <a c'>8-. <d f>8-. r8 |
        <g b>8-. <g b>8-. <c e>8-. r8 |
        <f a>4.( <g f'>8) |
        <c' e'>8-. c8-. f16 b16 g16 b16 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```
