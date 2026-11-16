\version "2.26.0"
\language "english"
aOne = \relative c { g }
aTwo = \relative c { g, }
aThree = \relative c { g' }
aFour = \relative c' { g b d b d b }
aFive = \relative c' { g b d b g }
aSix = \relative c { g b d b d b }
aSeven = \relative c'' { c g, }
\displayLilyMusic \aOne
\displayLilyMusic \aTwo
\displayLilyMusic \aThree
\displayLilyMusic \aFour
\displayLilyMusic \aFive
\displayLilyMusic \aSix
\displayLilyMusic \aSeven
