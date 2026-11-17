\version "2.26.0"
\language "english"

\header {
  title = "Symphony No. 7 in A major, Op. 92"
  subtitle = "II. Allegretto — mm. 1–26（摘录：中提琴/大提琴/低音提琴；Vn I/II 全休止）"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

% 摘录说明：mm.1–26 的固定音型由中提琴、大提琴与低音提琴在中低音区奏出，
% 第一、第二小提琴在此段全休止（m.27 起才以高八度承接）；
% 本摘录取 mm.1–26（mm.19–26 为 pp 重复，音型与 mm.11–18 相同）。

global = {
  \key a \minor
  \time 2/4
  \tempo "Allegretto" 4 = 76
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  R2*26 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  R2*26 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.1-2
  R2 | R2 |
  % m.3
  e4\p e8 e8 |
  % m.4
  e4 e4 |
  % m.5
  e4 e8 e8 |
  % m.6
  e4 e4 |
  % m.7
  e4 e8 <d fs>8 |
  % m.8
  <e g>4 <e g>4 |
  % m.9
  <d g>4 <c g>8 <d g>8 |
  % m.10
  <e g>4 r4 |
  % m.11
  g4 g8 a8 |
  % m.12
  b4 b4 |
  % m.13
  fs4 fs8 gs8 |
  % m.14
  a4 a4 |
  % m.15
  e4 e8 e8 |
  % m.16
  e4 e4 |
  % m.17
  e4 <e fs>8 <e gs>8 |
  % m.18
  <e a>4 r4 |
  % m.19
  g4\pp g8 a8 |
  % m.20
  b4 b4 |
  % m.21
  fs4 fs8 gs8 |
  % m.22
  a4 a4 |
  % m.23
  e4 e8 e8 |
  % m.24
  e4 e4 |
  % m.25
  e4 <e fs>8 <e gs>8 |
  % m.26
  <e a>4 r4 |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  % m.1-2
  R2 | R2 |
  % m.3
  c4\p c8 c8 |
  % m.4
  b,4 b,4 |
  % m.5
  b,4 b,8 b,8 |
  % m.6
  c4 c4 |
  % m.7
  c4 c8 c8 |
  % m.8
  c4 c4 |
  % m.9
  b,4 a,8 b,8 |
  % m.10
  c4 r4 |
  % m.11
  e4 e8 e8 |
  % m.12
  ds4 ds4 |
  % m.13
  d!4 d8 d8 |
  % m.14
  cs4 c4 |
  % m.15
  c4 c8 c8 |
  % m.16
  b,4 c4 |
  % m.17
  b,4 b,8 b,8 |
  % m.18
  c4 r4 |
  % m.19
  e4\pp e8 e8 |
  % m.20
  ds4 ds4 |
  % m.21
  d!4 d8 d8 |
  % m.22
  cs4 c4 |
  % m.23
  c4 c8 c8 |
  % m.24
  b,4 c4 |
  % m.25
  b,4 b,8 b,8 |
  % m.26
  c4 r4 |
}

contrabass = {
  \global
  \clef bass
  \set Staff.midiInstrument = "contrabass"
  % m.1-2
  R2 | R2 |
  % m.3
  a,4\p a,8 a,8 |
  % m.4
  gs,4 gs,4 |
  % m.5
  e,4 e,8 e,8 |
  % m.6
  a,4 a,4 |
  % m.7
  a,4 a,8 a,8 |
  % m.8
  a,4 a,4 |
  % m.9
  g,4 g,8 g,8 |
  % m.10
  c4 r4 |
  % m.11
  c4 c8 c8 |
  % m.12
  b,4 b,4 |
  % m.13
  b,4 b,8 b,8 |
  % m.14
  a,4 a,4 |
  % m.15
  a,4 a,8 a,8 |
  % m.16
  gs,4 a,4 |
  % m.17
  e,4 e,8 e,8 |
  % m.18
  a,4 r4 |
  % m.19
  c4\pp c8 c8 |
  % m.20
  b,4 b,4 |
  % m.21
  b,4 b,8 b,8 |
  % m.22
  a,4 a,4 |
  % m.23
  a,4 a,8 a,8 |
  % m.24
  gs,4 a,4 |
  % m.25
  e,4 e,8 e,8 |
  % m.26
  a,4 r4 |
}

\score {
  <<
    \new Staff \with { instrumentName = "Violino I" } \violinoI
    \new Staff \with { instrumentName = "Violino II" } \violinoII
    \new Staff \with { instrumentName = "Viola" } \viola
    \new Staff \with { instrumentName = "Violoncello" } \violoncello
    \new Staff \with { instrumentName = "Contrabass" } \contrabass
  >>
  \layout { }
  \midi { }
}
