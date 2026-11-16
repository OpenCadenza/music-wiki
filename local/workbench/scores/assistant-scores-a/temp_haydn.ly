\version "2.26.0"
\include "nederlands.ly"

m_right = \relative c' {
  \partial 8 d8
  g8( b d g,)
  g4( fis8) d
  a'( c e <a, c>)
  <a c>4( <g b>8 b)
  b'( g dis e)
  a( fis cis d!)
  e8( g4) cis,8
  d4 r8
}
m_left = \relative c' {
  \partial 8 r8
  <g b>4 r8 <b d>
  <a c>4 r
  r r8 fis
  g4 g,8 r
  \clef treble
  g''4 r8 g
  fis4 r8 fis
  g4 a
  \clef bass
  d,4 d,8
}

t_right = \relative c'' {
  \partial 8 d8
  g8( b8 d8 g,8)
  g4( fis8) d8
  a'( c8 e8 <a, c>8)
  <a c>4( <g b>8 b8)
  b'( g8 dis8 e8)
  a8( fis8 cis8 d!8)
  e8( g4) cis,8
  d4 r8
}
t_left = \relative c' {
  \partial 8 r8
  <g b>4 r8 <b d>8
  <a c>4 r4
  r4 r8 fis8
  g4 g,8 r8
  \clef treble
  g'4 r8 g8
  fis4 r8 fis8
  g4 a4
  \clef bass
  d,4 d,8
}

\score {
  <<
    \new Staff = "m_rh" { \m_right }
    \new Staff = "m_lh" { \m_left }
    \new Staff = "t_rh" { \t_right }
    \new Staff = "t_lh" { \t_left }
  >>
  \midi { }
}
