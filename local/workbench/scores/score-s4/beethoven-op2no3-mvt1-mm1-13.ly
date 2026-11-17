\version "2.26.0"
\language "english"

\header {
  title = "Beethoven: Piano Sonata No. 3 in C major, Op. 2 No. 3"
  subtitle = "I. Allegro con brio · mm. 1–13"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

% 谱源：DCML piano sonata corpus (GitLab export, MS3); cross-checked with Craig Sapp kern (pitch-identical for all 13 measures).

#(set-global-staff-size 17)

D = \tweak Stem.direction #DOWN \etc
U = \tweak Stem.direction #UP \etc

\score {
  \new PianoStaff \with { instrumentName = "Piano" } <<
    \new Staff = "rh" \with { midiInstrument = "acoustic grand" } <<
    { \voiceOne {
  \clef "treble" \numericTimeSignature \time 4/4 \key c \major \oneVoice \tempo "Allegro con brio" \U <c'
    e'>2 _\p \U <b d'>16 _( [ \U <c' e'>16 \U <b d'>16 \U <c' e'>16 ) ] \U <d'
    f'>8 -. -. [ \U <c' e'>8 -. -. ] | % 1
  \U <b d'>4 -. -. \U <b g'>4 -. -. r2 | % 2
  \U <d' f'>2 \U <cs' e'>16 _( [ \U <d' f'>16 \U <cs' e'>16 \U <d' f'>16 ) ]
  \U <e' g'>8 -. -. [ \U <d' f'>8 -. -. ] | % 3
  \U <c'! e'>4 -. -. \U <e' c''>4 -. -. r2 | % 4
  \voiceOne \U c''2 _\p \U b'16 ^( [ \U c''16 \U b'16 \U c''16 ) ] \U d''8 -. [
  \U b'8 -. ] | % 5
  \U g'4 \oneVoice \U <e' c''>4 _\sf \voiceOne \U b'16 ^( [ \U c''16 \U b'16 \U
  c''16 ) ] \U d''8 -. [ \U b'8 -. ] | % 6
  \oneVoice \U g'4 ^( \U c''4 \voiceOne \U d'4 \U a'4 ) | % 7
  \U d'4 ^( \U g'4 \oneVoice \U <c' e'>4 ) e'4\rest | % 8
  e'4\rest \voiceOne \U g'2 ^( _\sf \U f'4 ) | % 9

  \barNumberCheck #10
  \oneVoice \U <c' e'>4 \voiceOne \U g'2 ^( _\sf \U f'4 ) | % 10
  \oneVoice \U <g c' e'>4 r4 \U <a c' e' a'>4 r4 | % 11
  \U <g c' e' g'>4 r4 s4 r4 | % 12
  \U c'16 [ _\ff \U e'16 \U g'16 \U c''16 ] \D e'16 [ \D e''16 \D e'16 \D e''16
  ] \D e'16 [ \D g'16 \D c''16 \D e''16 ] \D g'16 [ \D g''16 \D g'16 \D g''16 ]
} }
    { \voiceTwo {
  \clef "treble" \numericTimeSignature \time 4/4 \key c \major s1*4 | % 4
  \D e'2 \D f'2 | % 5
  e'4\rest s4 \D f'2 s2 \D <c' d'>2 | % 7
  \D b2 s2. \D e'4 \D d'4 \D d'4 s4 \D e'4 \D d'4 \D d'4 } }
  >>
    \new Staff = "lh" \with { midiInstrument = "acoustic grand" } <<
    { \voiceOne {
  \clef "bass" \numericTimeSignature \time 4/4 \key c \major \oneVoice <c g>1 | % 1
  \D <g, g>4 -. -. \D <g, g>4 -. -. r2 | % 2
  <g, b>1 | % 3
  \D <c g>4 -. -. \D <c g>4 -. -. r2 | % 4
  \voiceOne g1 ~ | % 5
  \U g4 \U g2. ~ | % 6
  \U g2 \U a2 | % 7
  \oneVoice \D g4 \U g,4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D g8 \D fs8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 -. [ \D e8 -. \D d8 -. ] }
  | % 8
  s4 _\sf \voiceOne \U g2 ~ \U g4 | % 9

  \barNumberCheck #10
  \U g4 \U g2 ~ _\sf \U g4 | % 10
  \oneVoice \D g,4 \D c2 _\sf \D fs,4 | % 11
  s2 \voiceOne \U <d f! g b>4 r4 | % 12
  \oneVoice \U <c, e, g, c>4 \clef "treble" \U c'8 [ \U c'8 ] \U c'4 \U e'8 [ \U
  e'8 ] } }
    { \voiceTwo {
  \clef "bass" \numericTimeSignature \time 4/4 \key c \major s1*4 | % 4
  r4 \D c4 \D d4 \D g,4 | % 5
  r4 \D c4 \D d4 \D g,4 | % 6
  \D e4 \D c4 \D f4 \D d4 s1 | % 8
  \oneVoice \D c2 \voiceTwo \D b,16 _( [ \D c16 \D b,16 \D c16 ) ] \D d8 -. [ \D
  b,8 -. ] | % 9

  \barNumberCheck #10
  \D g,4 \D c4 \D b,16 _( [ \D c16 \D b,16 \D c16 ) ] \D d8 -. [ \D b,8 -. ] s1
  | % 11
  \oneVoice \D fs,4 \D g,2 ^\sf \voiceTwo \D <g,, g,>4 s4 \clef "treble" } }
  >>
  >>
  \layout { }
  \midi { }
}
