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
      c''4 r4 r4 | \bar "||"
    }
    \new Staff {
      \key f \major
      \time 3/4
      \clef bass
      \partial 4.
      r4. |
      c2. |
      <c' e'>4 c8 r8 r4 | \bar "||"
    }
  >>
}
