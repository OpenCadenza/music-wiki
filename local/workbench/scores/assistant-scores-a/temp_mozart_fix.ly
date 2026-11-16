\version "2.26.0"
\language "english"

global = {
  \key g \major
  \time 3/4
  \tempo "Allegro" 4 = 120
}

rightHand = \relative c'' {
  \global
  \clef treble
  \partial 4 d8.(\p b16) |
  d4 r4 g,4 |
  fs4 r4 a'8.( fs16) |
  a4 r4 c,4 |
  b4 r4 g'8.(\f fs16) |
  fs8( e8) e4 g8.( e16) |
  e8( d8) d4 g8.( d16) |
  d4-.\p d4-. d4-. |
  d16( e fs g a b c d c b a g) |
  fs16( e d c b d b g a c a fs) |
  g4 r4 \bar "||"
}

leftHand = \relative c {
  \global
  \clef bass
  \partial 4 r4 |
  g8(\p b d b d b) |
  a8( c d c d c) |
  fs,8( a d a d a) |
  g8( b d b) g4\f |
  \clef treble
  <c' g'>2\fp r4 |
  <b g'>2\fp r4 |
  \clef bass
  <a c'>4-.\p <g b>4-. <fs a>4-. |
  <g b>4 r4 <e g>4 |
  r4 << { g4 c4 } \\ { d,2 } >> |
  <g b>4 g,4 r4 \bar "||"
}

\score {
  \new PianoStaff <<
    \new Staff = "upper" { \rightHand }
    \new Staff = "lower" { \leftHand }
  >>
  \midi { }
}
