\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 14 in C-sharp minor, Op. 131"
  subtitle = "I. Adagio ma non troppo e molto espressivo — mm. 6–11"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

global = {
  \key cs \minor
  \time 2/2
  \tempo "Adagio ma non troppo e molto espressivo" 4 = 69
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  \p
  % m.6
  a'4 es'4 fs'4 a'4 |
  % m.7
  g'4 es'2 es''4 |
  % m.8
  fs''2 e''4 ds''4~ |
  % m.9
  ds''4 fs''4 e''4 e''4~ |
  % m.10
  e''4 ds''2 e''4~ |
  % m.11
  e''2. d''4 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  \p
  % m.6
  d'2. cs'4 |
  % m.7
  b4 d'4 cs'4 b4 |
  % m.8
  a4 b4 cs'4 bs4 |
  % m.9
  ds'4 gs2 gs'4 |
  % m.10
  bs'2 cs''4 b'4 |
  % m.11
  as'4 cs''4 b'4 a4 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  \p
  % m.6
  r1 |
  % m.7
  r1 |
  % m.8
  r2. gs4 |
  % m.9
  bs2 cs'2 |
  % m.10
  a2. gs4 |
  % m.11
  fs4 a4 gs4 fs4 |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  \p
  % m.6
  r1 |
  % m.7
  r1 |
  % m.8
  r1 |
  % m.9
  r1 |
  % m.10
  r1 |
  % m.11
  r1 |
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
