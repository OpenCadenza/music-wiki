\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff {
      \key f \major
      \time 3/4
      \partial 4.
      c''8-.( c''-. c''-.) |
      c''2. |
      \partial 4. c''4 r8 | \bar "||"
    }
    \new Staff {
      \key f \major
      \time 3/4
      \clef bass
      \partial 4.
      r4. |
      c2. |
      \partial 4. <c' e'>4 c8 | \bar "||"
    }
  >>
}
