\version "2.26.0"
\language "english"
fixAll = \relative c' {
  \time 3/4
  \clef bass
  \partial 4 r4 |
  g8 b8 d8 b8 d8 b8 |
  a8 c8 d8 c8 d8 c8 |
  fs,8 a8 d8 a8 d8 a8 |
  g8 b8 d8 b8 g4 |
  \clef treble
  <c g'>2 r4 |
  <b g'>2 r4 |
  \clef bass
  <a c'>4-. <g b>4-. <fs a>4-. |
  <g b>4 r4 <e g>4 |
  r4 << { g4 c4 } \\ { d,2 } >> |
  <g b>4 g,4 r4
}
\displayLilyMusic \fixAll
