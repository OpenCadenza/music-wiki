\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 10 in E-flat major, Op. 74 “Harp”"
  subtitle = "I. Poco Adagio — mm. 18–24"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

global = {
  \key ef \major
  \time 2/2
  \tempo "Poco Adagio" 2 = 72
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.18
  \p cf''2 d'4. ef'8 |
  % m.19
  ef'4. ff'8 ff'4. f'8 |
  % m.20
  f'4. gf'8 gf'4. g'8 |
  % m.21
  g'4. af'8 af'4. a'8 |
  % m.22
  a'4. bf'8 bf'4. cf''8 |
  % m.23
  cf''4. c''8 df''2~ |
  % m.24
  df''4. d''8 d''4. ef''8 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.18
  \p cf'1~ |
  % m.19
  cf'1 |
  % m.20
  df'1 |
  % m.21
  df'4. ef'8 f'4. gf'8 |
  % m.22
  gf'4. g'8 df'4. cf'8 |
  % m.23
  ef'2 e'2~ |
  % m.24
  e'4. f'8 <bf f'>4. <bf ef'>8 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.18
  \p af1~ |
  % m.19
  af1 |
  % m.20
  bf1 |
  % m.21
  bf4. cf'8 cf'4. c'8 |
  % m.22
  c'4. df'8 ff'4. ef'8 |
  % m.23
  r4 gf4 g2~ |
  % m.24
  g4. af8 af4. g8 |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  % m.18
  r1 |
  % m.19
  r1 |
  % m.20
  r1 |
  % m.21
  \p af,2 d,4. ef,8 |
  % m.22
  ef2 g,4. af,8 |
  % m.23
  gf2 a,4. bf,8 |
  % m.24
  bf,2 bf,4. ef8 |
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
