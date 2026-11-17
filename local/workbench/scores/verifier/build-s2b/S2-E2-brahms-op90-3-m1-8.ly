\version "2.26.0"
\language "english"

\header {
  title = "Symphony No. 3 in F major, Op. 90"
  subtitle = "III. Poco allegretto — mm. 1–8（摘录：大管长音层 + 大提琴主题）"
  composer = "Johannes Brahms (1833–1897)"
  tagline = ##f
}

% 摘录说明（依据 espace-midi/J.F. Lucarelli LilyPond 底本核对）：
% 圆号（Corno I/II）在 mm.1–23 为全休止（源码：\partial 8 r8 R4. * 23，Mark A 在 m.23）；
% 该段中低音区共鸣长音层实际由大管（Fagotti）自 m.1 起承担，单簧管自 m.13 进入。
% 本摘录交付 m.1–8 的大管长音层与大提琴主题。

global = {
  \key c \minor
  \time 3/8
  \tempo "Poco allegretto" 4. = 100
}

fagotto = {
  \global
  \clef bass
  \set Staff.midiInstrument = "bassoon"
  \partial 8 r8 |
  % m.1
  c4\p r8 |
  % m.2
  f4 r8 |
  % m.3
  c4 r8 |
  % m.4
  f4 r8 |
  % m.5
  b,4 r8 |
  % m.6
  c4 r8 |
  % m.7
  af'4 r8 |
  % m.8
  g8 c bf |
}

violoncello = {
  \global
  \clef tenor
  \set Staff.midiInstrument = "cello"
  \partial 8 c16.( d32) |
  % m.1
  ef4.( |
  % m.2
  g16.( f32) d8) c16.( d32) |
  % m.3
  ef4.( |
  % m.4
  bf'16.( af32) d8) d16.( ef32) |
  % m.5
  f4 af16.( g32) |
  % m.6
  ef4 g16.( f32) |
  % m.7
  c8.( d32 c) b16[( c]) |
  % m.8
  d8( ef8 e8) |
}

\score {
  <<
    \new Staff \with { instrumentName = "Fagotto" } \fagotto
    \new Staff \with { instrumentName = "Violoncello" } \violoncello
  >>
  \layout { }
  \midi { }
}
