\version "2.26.0"
\language "english"
#(set-default-paper-size "a5")
\header { tagline = ##f }
\score {
  \new Staff {
    \key f \minor
    \time 3/2
    c'''2:16 c'''2:16 c'''4..:16 r16 |
    c'''1:16 |
  }
  \layout { }
}