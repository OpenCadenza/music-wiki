\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 11 in F minor, Op. 95 “Serioso”"
  subtitle = "I. Allegro con brio — mm. 19–24"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

global = {
  \key f \minor
  \time 4/4
  \tempo "Allegro con brio" 4 = 120
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.19
  \f f'16 g'16 af'16 g'16 f'4 gf'16 af'16 bf'16 af'16 gf'4 |
  % m.20
  \ff g'16 af'16 bf'16 c''16 df''16 ef''16 df''16 c''16 bf'16 c''16 bf'16 af'16 g'16 f'16 ef'16 df'16 |
  % m.21
  \p c'8 af'8 af''4 af''4 gf''4 |
  % m.22
  f''4 df''8 c''8 bf'2~ |
  % m.23
  bf'4 af'4 g'4 af'4 |
  % m.24
  af'1 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.19
  \f f'16 g'16 af'16 g'16 f'4 gf'16 af'16 bf'16 af'16 gf'4 |
  % m.20
  \ff g'16 af'16 bf'16 c''16 df''16 ef''16 df''16 c''16 bf'16 c''16 bf'16 af'16 g'16 f'16 ef'16 df'16 |
  % m.21
  \p c'4 c'4 df'8 ef'8 |
  % m.22
  f'4 gf'8 af'8 bf'4 ef'4~ |
  % m.23
  ef'2.~ ef'4 |
  % m.24
  f'4 af4 f'4 af4 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.19
  \f f16 g16 af16 g16 f4 gf16 af16 bf16 af16 gf4 |
  % m.20
  \ff g16 af16 bf16 c'16 df'16 ef'16 df'16 c'16 bf16 c'16 bf16 af16 g16 f16 ef16 df16 |
  % m.21
  \p c4 af4 bf8 c'8 |
  % m.22
  df'1~ |
  % m.23
  df'2.~ c'4 |
  % m.24
  df4~ \tuplet 3/2 { df8 f8 gf8 } af4~ \tuplet 3/2 { af8 c'8 df'8 } |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  % m.19
  \f f,16 g,16 af,16 g,16 f,4 gf,16 af,16 bf,16 af,16 gf,4 |
  % m.20
  \ff g,16 af,16 bf,16 c16 df16 ef16 df16 c16 bf,16 c16 bf,16 af,16 g,16 f,16 ef,16 df,16 |
  % m.21
  \p c,4 r2. |
  % m.22
  df4 ef8 f8 gf2~ |
  % m.23
  gf4 af4 a4 af4 |
  % m.24
  af4 r2. |
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
