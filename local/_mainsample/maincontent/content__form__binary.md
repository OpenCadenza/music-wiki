---
name: 二部曲式
description: 两个主要段落完成一次调性走向，第二段可以在内部带回开头材料。
---

# 二部曲式

**结构示意**　A ∥ B，或 A ∥ B–A′

古典小步舞曲常用两组反复标出二部曲式。先听第一段在哪里终止，再听第二段如何走向全曲主调。如果开头主题在第二段内部回到主调，便形成再现二部。末尾只重复第一段的收束音型时，要继续检查开头主题是否也回来了。

## 莫扎特《C 大调小步舞曲》K. 15f

第 1–8 小节是第一反复段。右手开头两次弹出 E–G–C–B，第 7 小节出现 F♯，第 8 小节由 G 低音支撑 G 大三和弦，在属调收住。第 9–18 小节另起十六分音符的音型，经过几次半音变化，最后两小节以 G–C 低音和上声部 C 收回主调。开头的 E–G–C–B 乐句没有在第二段回归，这里是连续型单纯二部。

```lilypond title="莫扎特 K.15f《C 大调小步舞曲》" location="全曲，mm.1–18" id="k15f"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key c \major \time 3/4
      \set Score.tempoHideNote = ##t
      \tempo 4 = 108
      \repeat volta 2 {
        e''8 g'' c''4 b' |
        e''8 g'' c''4 b' |
        c''8 d'' e'' f'' g''16 a'' b'' c''' |
        g''4 f'' e'' |
        <c'' e''>8. g''16 <d'' fs''>8. a''16 g''8. b''16 |
        a''8. b''16 c'''8. a''16 b''4 |
        e''8. c''16 b'8. g''16 a'8. fs''16 |
        <b' d'' g''>2 r4 |
      }
      \repeat volta 2 {
        a'16 cs'' e'' g'' g'' e'' cs'' a' r4 |
        s16 cs'' e'' g'' g'' e'' cs'' a' r4 |
        s8 <g'' bf''>8 <f'' a''> <e'' g''> <d'' f''> <cs'' e''> |
        <d'' f''>2 <ef'' fs''>4 |
        << { g''8 a'' g'' f'' e'' d'' } \\ { d''4 r4 g'4 } >> |
        << { e''4 c'' g'' } \\ { g'2 e''4 } >> |
        a'8. f''16 c''8. f''16 d''8. g''16 |
        e''8. g''16 f''8. a''16 g''4 |
        a''8. f''16 e''8. c''16 d''8. b'16 |
        c''2 r4^\fermata |
      }
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key c \major \time 3/4
      \repeat volta 2 {
        c16 d e f g8 f g16 f e d |
        c16 d e f g4 g, |
        << { c'8 b c' d' e'16 f' d' e' } \\ { c4 r r } >> |
        << { e'4 d' c' } \\ { g2. } >> |
        c2 b,4 |
        fs8. g16 a8. fs16 g4 |
        c4 d d, |
        g,4 b,8 d g4 |
      }
      \repeat volta 2 {
        << { s2 bf4 } \\ { a,2 bf,4 } >> |
        << { a16 s16 s8 s4 bf4 } \\ { a,2 bf,4 } >> |
        << { a8 s8 s2 } \\ { a,4 cs a, } >> |
        d4 d' c'! |
        b!4 g b |
        c'4 r r |
        f4 a b |
        << { c'4 r r } \\ { c8. e16 d8. f16 e8. c16 } >> |
        f4 g g, |
        c4 g, c_\fermata |
      }
    }
  >>
  \layout { }
  \midi { }
}
```
