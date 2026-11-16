\version "2.26.0"
\language "english"
fixOne = \relative c' { g8 b8 d8 b8 d8 b8 | a8 c8 d8 c8 d8 c8 | fs,8 a8 d8 a8 d8 a8 | g8 b8 d8 b8 g4 }
fixTwo = \relative c' { g8 b8 d8 b8 d8 b8 | a8 c8 d8 c8 d8 c8 | fs,8 a8 d8 a8 d8 a8 | g8 b8 d8 b8 g4 | <c g'>2 r4 | <b g'>2 r4 }
\displayLilyMusic \fixOne
\displayLilyMusic \fixTwo
