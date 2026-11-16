\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 11 in F minor, Op. 95 “Serioso”"
  subtitle = "I. Allegro con brio — mm. 1–8"
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
  \f
  % m.1
  f'16 g'16 af'16 g'16 f'8-. ef'8-. df'8-. c'8-. d'8-. e'8-. |
  % m.2
  f'4 r2. |
  % m.3
  r8 r16 c''16 c'''4 c'''8 r16 c'''16 c''4 |
  % m.4
  c''8 r16 c''16 c'8 r16 c'16 c''8 r16 c''16 c'''8 r16 c''16 |
  % m.5
  c'''8 r16 c''16 c'4 r2 |
  % m.6
  r4 df''2.~ |
  % m.7
  \p df''2 gf''2 |
  % m.8
  b'2. df''4 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  \f
  % m.1
  f'16 g'16 af'16 g'16 f'8-. ef'8-. df'8-. c'8-. d'8-. e'8-. |
  % m.2
  f'4 r2. |
  % m.3
  g4 r8 r16 g16 af4 r8 r16 af16 |
  % m.4
  g8 r16 e'16 f'8 r16 f'16 e'8 r16 g'16 af'8 r16 af'16 |
  % m.5
  g'8 r16 c'16 c'4 r2 |
  % m.6
  r4 bf'2.~ |
  % m.7
  \p bf'2 gf'2 |
  % m.8
  f'1 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  \f
  % m.1
  f16 g16 af16 g16 f8-. ef8-. df8-. c8-. d8-. e8-. |
  % m.2
  f4 r2. |
  % m.3
  e4 r8 r16 e16 f4 r8 r16 f16 |
  % m.4
  e8 r16 g16 af8 r16 af16 g8 r16 e'16 f'8 r16 f'16 |
  % m.5
  e'8 r16 c'16 c4 r2 |
  % m.6
  r4 gf'2. |
  % m.7
  \p df'2 bf2 |
  % m.8
  b1 |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  \f
  % m.1
  f,16 g,16 af,16 g,16 f,8-. ef,8-. df,8-. c,8-. d,8-. e,8-. |
  % m.2
  f,4 r2. |
  % m.3
  c4 r8 r16 c16 c4 r8 r16 c16 |
  % m.4
  c8 r16 c16 f8 r16 f16 c8 r16 c16 f,8 r16 f,16 |
  % m.5
  c,8 r16 c16 c4 r2 |
  % m.6
  gf16 af16 bf16 af16 gf8 f8 ef8 df8 ef8 f8 |
  % m.7
  \p gf1 |
  % m.8
  af1 |
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
