\version "2.26.0"
\language "english"

\header {
  title = "Symphony No. 5 in C minor, Op. 67"
  subtitle = "II. Andante con moto — mm. 1–9（摘录：弦乐四声部）"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

% 摘录说明：主题由中提琴与大提琴齐奏呈示（mm.1–7，弱起八分），
% 第一、第二小提琴于 m.8 第三拍进入（对题/伴奏层）。

global = {
  \key af \major
  \time 3/8
  \tempo "Andante con moto" 4. = 92
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  \partial 8 r8 |
  % m.1-7 休止
  R4.*7 |
  % m.8
  r8 r8 af'16.\p( c''32) |
  % m.9
  ef''4.\f |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  \partial 8 r8 |
  R4.*7 |
  % m.8
  r8 r8 ef'16.\p( c'32) |
  % m.9
  bf4.\f |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  \partial 8 ef16.(\p af32) |
  % m.1
  c'8-. c'16.( bf32) af16.( c'32) |
  % m.2
  f8~ f16.( a32) bf16.( c'32) |
  % m.3
  df'16.( c'32) bf16.( df'32) g16.( bf32) |
  % m.4
  e16.( g32) c'8~ c'16. bf32 |
  % m.5
  a16.( f32) bf8. df'16 |
  % m.6
  g16.( ef32) af!8 af16.( c'32) |
  % m.7
  ef'4. |
  % m.8
  c'8 r8 <ef c'>16.( <ef af>32) |
  % m.9
  <ef g>4. |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  \partial 8 ef16.(\p af32) |
  % m.1
  c'8-. c'16.( bf32) af16.( c'32) |
  % m.2
  f8~ f16.( a32) bf16.( c'32) |
  % m.3
  df'16.( c'32) bf16.( df'32) g16.( bf32) |
  % m.4
  e16.( g32) c'8~ c'16. bf32 |
  % m.5
  a16.( f32) bf8. df'16 |
  % m.6
  g16.( ef32) af!8 af16.( c'32) |
  % m.7
  ef'4. |
  % m.8
  c'8 r8 <ef c'>16.( <ef af>32) |
  % m.9
  <ef g>4. |
}

\score {
  <<
    \new Staff \with { instrumentName = "Violino I" } \violinoI
    \new Staff \with { instrumentName = "Violino II" } \violinoII
    \new Staff \with { instrumentName = "Viola" } \viola
    \new Staff \with { instrumentName = "Violoncello" } \violoncello
  >>
  \layout { }
  \midi { }
}
