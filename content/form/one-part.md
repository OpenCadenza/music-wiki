---
name: 一部曲式
description: 一个完整乐段承担全曲的结构，内部可以有多个乐句、对比和终止扩充。
---

# 一部曲式

**结构示意**　A（起始材料 → 继续 → 终止）

先找全曲最终的终止，再回听中间有没有足以自成一部的段落。一个动机可以多次出现，一个乐段也可以换拍或换音型。判断要看这些变化在推动同一个终止，还是各自建立了新的段落任务。

## 莫扎特《C 大调行板》K. 1a

第 1–2 小节在 3/4 拍中重复带颤音的短音型。第 3–4 小节换成 E–F–F♯–G 的上行开头，仍然落到带颤音的 F。第 5 小节转入 2/4，连续的级进与分解和弦把音乐送向第 10 小节的 C 大调终止。把第 5 小节前后连起来听，可以听见开头四次陈述积累的动能如何转化成一句收束。

```lilypond title="莫扎特 K.1a《C 大调行板》" location="全曲，mm.1–10" id="k1a"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key c \major \time 3/4
      \set Score.tempoHideNote = ##t
      \tempo "Andante" 4 = 67
      g'8 c''16 g' g'4 f'\trill |
      g'8 c''16 g' g'4 f'\trill |
      e'16 f' fs' g' g'4 f'\trill |
      e'16 f' fs' g' g'4 f'\trill |
      \time 2/4
      \acciaccatura f'8 e'8 d'16 c' \acciaccatura e'8 d'8 c'16 b |
      c'16 e' c'8 \clef bass c'16 g bf8 |
      bf4 a8 g16 f |
      e16 c' g bf \acciaccatura bf8 a8 g16 f |
      e4 d |
      c4 r4 \bar "|."
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key c \major \time 3/4
      c'8 e'16 c' d'4 g |
      c'8 e'16 c' d'4 g |
      c'4 b g |
      c'4 b g |
      \time 2/4
      c'8 a f g |
      c8 c e c |
      r8 f d bf, |
      c8 e, f,4 |
      g,2 |
      c,4 r4
    }
  >>
  \layout { }
  \midi { }
}
```
