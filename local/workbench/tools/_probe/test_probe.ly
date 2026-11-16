\version "2.24.0"
\language "english"

\header {
  title = "Probe Minimum Test"
  composer = "Resource Assistant"
}

melody = \relative c' {
  \tempo 4 = 120
  \set Staff.midiInstrument = #"acoustic grand"
  c4 d e f | g2 c2 \bar "|."
}

\score {
  \new Staff {
    \melody
  }
  \layout { }
  \midi { }
}
