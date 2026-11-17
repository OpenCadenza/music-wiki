\version "2.26.0"
\language "english"

\header {
  title = "Symphony No. 5 in C minor, Op. 67"
  subtitle = "I. Allegro con brio — mm. 1–8（摘录：弦乐四声部）"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

% 摘录说明：命运动机由弦乐四声部齐奏呈示（mm.1–5），
% mm.6–8 为低弦延续与高音新动机的接续；mm.1–8 以弦乐四声部为主，
% 木管/铜管仅有局部模仿（本摘录从略，只取弦乐层）。

global = {
  \key c \minor
  \time 2/4
  \tempo "Allegro con brio" 4 = 108
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.1
  r8 g'8\ff[ g' g'] |
  % m.2
  ef'2\fermata |
  % m.3
  r8 f'8[ f' f'] |
  % m.4
  d'2~ |
  % m.5
  d'2\fermata |
  % m.6
  R2 |
  % m.7
  R2 |
  % m.8
  r8 ef''8\p[ ef'' ef''] |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.1
  r8 g'8\ff[ g' g'] |
  % m.2
  ef'2\fermata |
  % m.3
  r8 f'8[ f' f'] |
  % m.4
  d'2~ |
  % m.5
  d'2\fermata |
  % m.6
  r8 g'8\p[ g' g'] |
  % m.7
  ef'2~ |
  % m.8
  ef'2~ |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.1
  r8 g8\ff[ g g] |
  % m.2
  ef2\fermata |
  % m.3
  r8 f8[ f f] |
  % m.4
  d2~ |
  % m.5
  d2\fermata |
  % m.6
  R2 |
  % m.7
  r8 af'8\p[ af' af'] |
  % m.8
  g'2~ |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  % m.1
  r8 g,8\ff[ g, g,] |
  % m.2
  ef,2\fermata |
  % m.3
  r8 f,8[ f, f,] |
  % m.4
  d,2~ |
  % m.5
  d,2\fermata |
  % m.6
  R2 |
  % m.7
  c'2\p~ |
  % m.8
  c'2~ |
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
