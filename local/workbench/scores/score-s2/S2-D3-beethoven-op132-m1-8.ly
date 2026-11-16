\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 15 in A minor, Op. 132"
  subtitle = "I. Assai sostenuto — mm. 1–8"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

global = {
  \key a \minor
  \time 2/2
  \tempo "Assai sostenuto" 4 = 110
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.1
  \pp r1 |
  % m.2
  r1 |
  % m.3
  ds'2 e'2 |
  % m.4
  c''2 b'2 |
  % m.5
  gs''2 a''2 |
  % m.6
  b''2 c'''2 |
  % m.7
  c'''2 b''2 |
  % m.8
  ds''2 e''4 f''4 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.1
  \pp r1 |
  % m.2
  r2 b2 |
  % m.3
  a2 gs2 |
  % m.4
  <a fs'>2 gs'2 |
  % m.5
  d'2 c'2 |
  % m.6
  f'2 <e' c''>2 |
  % m.7
  a'2 gs'2 |
  % m.8
  f'4 fs'4 gs'4 <d' d''>4 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.1
  \pp r1 |
  % m.2
  a2 gs2 |
  % m.3
  c'2 b2 |
  % m.4
  ds2 e2 |
  % m.5
  b'2 c''2 |
  % m.6
  d'2 c'2 |
  % m.7
  fs2 gs2 |
  % m.8
  a2 gs4 <gs b>4 |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  % m.1
  \pp gs,2 a,2 |
  % m.2
  f2 e2 |
  % m.3
  r1 |
  % m.4
  r1 |
  % m.5
  f2 e2 |
  % m.6
  gs,2 a,2 |
  % m.7
  ds,2 e,2 |
  % m.8
  c2 b,4 b,4 |
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
