\version "2.26.0"
\language "english"
bOne = \relative c { \clef bass \partial 4 r4 g,8 b,8 d8 }
bTwo = \relative c { r4 g,8 }
bThree = \relative c { g,8 b,8 d8 }
bFour = \relative c { c g, }
bFive = \relative c { c, g, }
\displayLilyMusic \bOne
\displayLilyMusic \bTwo
\displayLilyMusic \bThree
\displayLilyMusic \bFour
\displayLilyMusic \bFive
