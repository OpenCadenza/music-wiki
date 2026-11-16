\version "2.26.0"
\language "english"
\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \key f \major
      \time 3/4
      \partial 4.
      c''8-. c''8-. c''8-. |
      c''8. \grace { d''16 c'' b' c'' } f''16 c''8 a'8 c''8 e'8 |
    }
    \new Staff = "lower" {
      \key f \major
      \time 3/4
      \clef bass
      \partial 4.
      r8 r4 |
      <f a c'>2 <c g bf>4 |
    }
  >>
  \midi {}
}
