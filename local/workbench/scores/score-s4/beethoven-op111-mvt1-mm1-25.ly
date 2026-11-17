\version "2.26.0"
\language "english"

\header {
  title = "Beethoven: Piano Sonata No. 32 in C minor, Op. 111"
  subtitle = "I. Maestoso — Allegro con brio ed appassionato · mm. 1–25"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

% 谱源：DCML piano sonata corpus (GitLab export, MS3); cross-checked with Craig Sapp kern; pickup (32nd) belongs to the opening.

#(set-global-staff-size 17)

D = \tweak Stem.direction #DOWN \etc
U = \tweak Stem.direction #UP \etc

\score {
  \new PianoStaff \with { instrumentName = "Piano" } <<
    \new Staff = "rh" \with { midiInstrument = "acoustic grand" } <<
    { \voiceOne {
  \clef "treble" \numericTimeSignature \time 4/4 \key c \minor \partial 32 \tempo "Maestoso"
  \oneVoice r32 e'8\rest c'16.\rest \U <ef' a' c'' ef''>32 \U <ef' ~ a' ~ c'' ~
    ef'' ~>4 _\sf \U <ef' a' c'' ef''>8.. [ \U <a' c''>32 ] \voiceOne \U c''8.
  ^\trill [ _\sf _\> \U b'32 \U c''32 ] <>\! | % 1
  \oneVoice \U <g' b'>8 r8 \U <ef' g' c''>8 r8 \slashedGrace { \U d'32 [ \U g'32
    \U b'32 ] } \U <d' g' d''>8 r8 r4 | % 2
  r8.. \D <af' d'' f'' af''>32 \D <af' ~ d'' ~ f'' ~ af'' ~>4 _\sf \D <af' d''
    f'' af''>8.. [ \D <d'' f''>32 ] \voiceOne \D d''4 _\sf <>\! | % 3
  \oneVoice \D <g' e''>8 r8 \D <f' c'' f''>8 r8 \slashedGrace { \U g'32 [ \U c''32
    \U e''32 ] } \D <g' c'' g''>8 r8 r4 | % 4
  e'8..\rest \D <df'' f'' bf'' df'''!>32 \D <df'' ~ f'' ~ bf'' ~ df''' ~>4
  _\sf \D <df'' f'' bf'' df'''>8.. [ \D <df'' bf''>32 ] \voiceOne \D df''4
  _\sf _\> <>\! | % 5
  \oneVoice \D <df'' ef'' bf''>8.. [ _\p \D <df'' ef'' bf''>32 ] \D <df'' ~
    ef'' ~ bf'' ~>4 \D <df'' ef'' bf''>8.. [ \D <c'' ef'' af''>32 ] \D <c''
    ef'' af''>8.. [ \D <c'' ef'' gf''>32 ] | % 6
  \D <c'' ef'' gf''>8.. [ \D <bf' ef'' gf''>32 ] \D <bf' ~ ef'' ~ gf'' ~>4
  \D <bf' ef'' gf''>8.. [ \D <a' ef'' gf''>32 ] \D <a' ef'' gf''>8.. [ \D
  <a' ef'' gf''>32 ] | % 7
  \D <a' ef'' gf''>8.. [ \D <af'! df'' f''>32 ] \D <af' ~ df'' ~ f'' ~>4 \D
  <af' df'' f''>8.. [ \D <af' cf'' f''>32 ] \D <af' cf'' f''>8.. [ \D <af'
    cf'' f''>32 ] | % 8
  \D <af' cf'' f''>8.. [ \D <af' c''! ef''>32 ] \D <af' ~ c'' ~ ef'' ~>4 \D
  <af' c'' ef''>8.. [ \D <af' c'' ef''>32 ] \D <af' c'' ef''>8.. [ \D <g'! bf'
    df''>32 ] | % 9

  \barNumberCheck #10
  \U <g' bf' df''>8.. [ \U <f' bf' df''>32 ] \U <f' bf' df''>8.. [ \U <e'
    bf' df''>32 ] \U <e' bf' df''>8 [ \U <c' f' c''>8 -. -. -. \U <c' f'
    c''>8 -. -. -. \U <c' fs' c''>8 -. -. -. ] | % 10
  \U <d'! g' b'>8 _\sf e'8\rest e'4\rest e'4\rest \voiceOne \U g'4 ^( _\p | % 11
  \U a'4 \U b'4 \U c''4 ) \oneVoice \U <ef' a' c''>8.. ^( [ \U <d' g' b'>32 ) ]
  | % 12
  \U <d' g' b'>4. _\sf e'8\rest e'4\rest \clef "bass" \voiceOne \U g4 ^( _\p | % 13
  \oneVoice \D <c fs a>4 \D <d f! b>4 \D <ef g c'>4 ) \voiceOne \U c'8.. ^( [
  \U b32 ) ] | % 14
  \oneVoice \D <d g b>2 \D <d g b>4.. \D <d g b>16 | % 15
  <d g b>1 | % 16
  \tempo "Allegro con brio ed appassionato" \break <d g b d'>1 | % 17
  \clef "treble" \U <g b d' g'>16 [ \clef "bass" \U af,16 \U g,16 \U af,16 ] \U
  g,16 [ \U af,16 \U g,16 \U af,16 ] \U g,16 [ \U af,16 \U g,16 \U af,16 ] \U g,16
  [ \U af,16 \U g,16 \U a,32 \U b,32 ] \bar ".|" % 18
  \U c4 r4 r4 r8 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g,16 [ \U a,16 \U b,16 ] }
  | % 19

  \barNumberCheck #20
  \U c4 -. \D ef4 -. \U b,4. ^\fermata _\sf \tweak TupletBracket.stencil ##f
  \tuplet 3/2 {
    \U g,16 [ \U a,16 \U b,16 ] }
  | % 20
  \U c4 -. \D ef4 -. \U b,4. _\sf \D af!8 -. | % 21
  \D g8 -. [ \D f8 -. \D ef8 -. \D d8 -. ] \D ef16 [ \D f16 \D ef16 \D d16 ] \D
  c8 [ \D af8 ^( -. ] | % 22
  \D g8 -. [ \D f8 -. \D ef8 -. \D d8 ) -. ] \D ef16 [ \D f16 \D ef16 \D d16 ]
  \D c16 [ _\< \D af16 \D bf16 \D af16 ] | % 23
  \D g16 [ \D af16 \D g16 \D f16 ] \D ef16 [ \D f16 \D ef16 \D d16 ] \D ef16 [
  \D f16 \D ef16 \D d16 ] \D c16 [ \D g16 \D f16 \D ef16 ] | % 24
  \D f16 [ \D g16 \D f16 \D ef16 ] \D d16 [ \D af16 \D g16 \D f16 ] \D g16 [ \D
  af16 \D g16 \D f16 ] \D e16 [ \D bf16 \D af16 \D g16 ] } }
    { \voiceTwo {
  \clef "treble" \numericTimeSignature \time 4/4 \key c \minor \partial 32
  s32*25 \D a'4 s1 | % 2
  s2. \U f''8. ^\trill [ \U e''32 _\> \U f''32 ] s1 | % 4
  s2. \U bf''8. ^\trill [ \U a''32 \U bf''32 ] s1*5 | % 10
  s2. c'8\rest \D c'8 | % 11
  \D <c' fs'>4 \D <d' f'>4 \D <ef' g'>4 s1 \clef "bass" r8 \D c8 s2. \D <ef a>8..
  [ \D <d g>32 ] s1*3 | % 17
  \clef "treble" s16 \clef "bass" s16*15 \bar ".|"
} }
  >>
    \new Staff = "lh" \with { midiInstrument = "acoustic grand" } <<
    { \voiceOne {
  \clef "bass" \numericTimeSignature \time 4/4 \key c \minor \partial 32
  \oneVoice \D <ef ef'>32 _\f \U <fs, fs>8.. [ \U <fs,,! fs,>32 ] \U <fs, ~
    fs ~>4 \D <fs, fs>8.. [ \D <fs ef'>32 ] \D <fs ef'>4 | % 1
  \D <g d'>8 r8 \D <c g c'>8 r8 \slashedGrace { \U b,,32 [ \U d,32 \U g,32 \U
    b,!32 \U d32 \U g32 \U b!32 ] } \U <b,, b,>8 r8 r8.. \D <af af'>32 | % 2
  \U <b, b>8.. [ _\sf \U <b,,! b,>32 ] \D <b, ~ b ~>4 \U <b, b>8.. [ \clef
  "treble" \U <b af'>32 ] \U <b af'>4 | % 3
  \clef "bass" \D <bf! df'>8 r8 \D <af c'>8 r8 \slashedGrace { \U e,32 [ \U g,32
    \U c32 \U e!32 \U g32 \U c'32 \U e'!32 ] } \U <e, e>8 r8 r8.. \D <df! df'>32
  | % 4
  \U <e, e>8.. [ \U <f, f>32 ] \U <f, ~ f ~>4 \D <f, f>8.. [ \D <f bf df'>32 ]
  \D <f bf df'>4 | % 5
  \D <gf bf df'>8.. [ \D <g! bf df'>32 ] \D <g ~ bf df' ~>4 \D <g bf
    df'>8.. [ \D <af c'>32 ] \D <af c'>8.. [ \D <a ef' gf'>32 ] | % 6
  \D <a ef' gf'>8.. [ \D <bf ef' gf'>32 ] \D <bf ~ ef' ~ gf' ~>4 \D <bf
    ef' gf'>8.. [ \D <cf' ef' gf'>32 ] \D <cf' ef' gf'>8.. [ \D <c' ef'
    gf'>32 ] | % 7
  \D <c' ef' gf'>8.. [ \D <df' f'>32 ] \D <df' ~ f' ~>4 \D <df' f'>8.. [ \D
  <d' f'>32 ] \D <d' f'>8.. [ \D <d,! d!>32 ] | % 8
  \U <d, d>8.. [ \U <ef, ef>32 ] \U <ef, ~ ef ~>4 \U <ef, ef>8.. [ \U <ef, ef>32
  ] \U <ef, ef>8.. [ \U <e, e!>32 ] | % 9

  \barNumberCheck #10
  \U <e, e>8.. [ \U <f, f>32 ] \U <f, f>8.. [ \U <g, g>32 ] \U <g, g>8 -. -. [
  \U <af, af>8 -. -. \U <af, af>8 -. -. \U <af,, af,>8 -. -. ] | % 10
  \U <g,, g,>8 \D g8 [ _\sfp \D g8 \D <g af>8 ] _\sfp \D <f af>8 [ \D <f g>8
  _\sfp \D <f g>8 \D <ef g>8 ] | % 11
  \voiceOne \U g8 [ \U g8 \U g8 \U g8 ] \U g8 [ \U g8 \U g8 \U g8 ~ ] | % 12
  \oneVoice \U <g, g>8 [ \U g,8 _\sfp \U g,8 \U <g, af,!>8 ] _\sfp \U <f, af,>8
  [ \U <f, g,>8 _\sfp \U <f, g,>8 \U <ef, g,>8 ] | % 13
  \voiceOne \U g,8 [ \U g,8 \U g,8 \U g,8 ] \U g,8 [ \U g,8 \U g,8 \U g,8 ~ ] | % 14
  \U g,8 [ \U g,8 \U g,8 \U g,8 ] \U g,8 [ \U g,8 \U g,8 \U g,8 ] | % 15
  \oneVoice \U g,,32 [ \U af,,32 \U g,,32 \U af,,32 \U g,,32 \U af,,32 \U g,,32
  \U af,,32 ] \U g,,32 [ \U af,,32 \U g,,32 \U af,,32 \U g,,32 \U af,,32 \U g,,32
  \U af,,32 ] \U g,,32 [ \U af,,32 \U g,,32 \U af,,32 \U g,,32 \U af,,32 \U g,,32
  \U af,,32 ] \U g,,32 [ \U af,,32 \U g,,32 \U af,,32 \U g,,32 \U af,,32 \U g,,32
  \U af,,32 ] | % 16
  \U g,,16 [ \U af,,16 \U g,,16 \U af,,16 ] \U g,,16 [ \U af,,16 \U g,,16 \U
  af,,16 ] \U g,,16 [ \U af,,16 \U g,,16 \U af,,16 ] \U g,,16 [ \U af,,16 \U g,,16
  \U af,,16 ] | % 17
  \U g,,16 [ \U af,,16 \U g,,16 \U af,,16 ] \U g,,16 [ \U af,,16 \U g,,16 \U
  af,,16 ] \U g,,16 [ \U af,,16 \U g,,16 \U af,,16 ] \U g,,16 [ \U af,,16 \U g,,16
  \U a,,32 \U b,,32 ] \bar ".|" % 18
  \U c,4 r4 r4 r8 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g,,16 [ \U a,,16 \U b,,16 ] }
  | % 19

  \barNumberCheck #20
  \U c,4 -. \U ef,4 -. \U b,,4. ^\fermata \tweak TupletBracket.stencil ##f
  \tuplet 3/2 {
    \U g,,16 [ \U a,,16 \U b,,16 ] }
  | % 20
  \U c,4 -. \U ef,4 -. \U b,,4. \U af,!8 -. | % 21
  \U g,8 -. [ \U f,8 -. \U ef,8 -. \U d,8 -. ] \U ef,16 [ \U f,16 \U ef,16 \U d,16
  ] \U c,8 [ \U af,8 _( -. ] | % 22
  \U g,8 -. [ \U f,8 -. \U ef,8 -. \U d,8 ) -. ] \U ef,16 [ \U f,16 \U ef,16 \U
  d,16 ] \U c,16 [ \U af,16 \U bf,16 \U af,16 ] | % 23
  \U g,16 [ \U af,16 \U g,16 \U f,16 ] \U ef,16 [ \U f,16 \U ef,16 \U d,16 ] \U
  ef,16 [ \U f,16 \U ef,16 \U d,16 ] \U c,16 [ \U g,16 \U f,16 \U ef,16 ] | % 24
  \U f,16 [ \U g,16 \U f,16 \U ef,16 ] \U d,16 [ \U af,16 \U g,16 \U f,16 ] \U
  g,16 [ \U af,16 \U g,16 \U f,16 ] \U e,16 [ \U bf,16 \U af,16 \U g,16 ] } }
    { \voiceTwo {
  \clef "bass" \numericTimeSignature \time 4/4 \key c \minor \partial 32 s4*11
  \clef "treble" s32*9 | % 3
  \clef "bass" s1*8 | % 11
  \D ef4 \D d4 \D c4 \D fs,8.. _( [ \D g,32 ) ] s1 | % 13
  \D ef,4 \D d,4 \D c,4 \D fs,,8.. _( [ \D g,,32 ) ] | % 14
  \D g,,2 \D g,,2 s1*3 \bar ".|"
} }
  >>
  >>
  \layout { }
  \midi { }
}
