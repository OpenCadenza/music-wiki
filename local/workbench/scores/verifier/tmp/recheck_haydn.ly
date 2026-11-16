\version "2.26.0"
\language "english"

global = {
  \key g \major
  \time 2/4
  \tempo "Presto" 4 = 132
}

rightHand = \relative c' {
  \global
  \clef treble
  \partial 8 d8 |
  g8( b8 d8 g,8) |
  g4( fs8) d8 |
  a'8( c8 e8 <a, c>8) |
  <a c>4( <g b>8 b8) |
  b'8( g8 ds8 e8) |
  a8( fs8 cs8 d!8) |
  e8( g4) cs,8 |
  d4\mordent r8 \bar "||"
}

leftHand = \relative c' {
  \global
  \clef bass
  \partial 8 r8 |
  <g b>4 r8 <b d>8 |
  <a c>4 r4 |
  r4 r8 fs8 |
  g4 g,8 r8 |
  \clef treble
  g''4 r8 g8 |
  fs4 r8 fs8 |
  g4 a4 |
  \clef bass
  d,4 d,8 \bar "||"
}

\displayLilyMusic \rightHand
\displayLilyMusic \leftHand
