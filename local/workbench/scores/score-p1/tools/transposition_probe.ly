\version "2.26.0"
\language "english"

% 语义探针：c'' 在四种 \transposition 下的实际发声音高（看 MIDI）
\score {
  <<
    \new Staff { \set Staff.midiInstrument = "clarinet" \transposition bf c''1 }
    \new Staff { \set Staff.midiInstrument = "clarinet" \transposition bes c''1 }
    \new Staff { \set Staff.midiInstrument = "clarinet" \transposition e c''1 }
    \new Staff { \set Staff.midiInstrument = "clarinet" \transposition a c''1 }
    \new Staff { \set Staff.midiInstrument = "clarinet" \transposition e' c''1 }
    \new Staff { \set Staff.midiInstrument = "clarinet" \transposition a' c''1 }
    \new Staff { \set Staff.midiInstrument = "clarinet" c''1 }
  >>
  \layout { }
  \midi { }
}
