\version "2.26.0"
\language "english"
\score {
  \new Staff {
    \time 3/8
    \partial 8 c8 |
    d4. | e4. | f4. | g4. | a4. |
  }
  \layout { \context { \Score \override BarNumber.break-visibility = #all-visible } }
}
