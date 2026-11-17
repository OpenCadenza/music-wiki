\version "2.26.0"
\language "english"

% TEST A: cross-voice numbered slur \=1( / \=1)
testA = {
  \key e \major \time 3/4
  <<
    \new Voice = "a" { \voiceOne e4\=1( e2 }
    \new Voice = "b" { \voiceTwo s4 <cs, cs>4 <c, c>4\=1) }
  >>
}

% TEST B: re-voice so the slur is intra-voice (kern's voicing)
testB = {
  \key e \major \time 3/4
  <<
    \new Voice = "a" { \voiceOne s4 e2 }
    \new Voice = "b" { \voiceTwo e4( <cs, cs>4 <c, c>4) }
  >>
}

\score {
  \new Staff { \clef bass \testA \bar "|." \testB \bar "|." }
}