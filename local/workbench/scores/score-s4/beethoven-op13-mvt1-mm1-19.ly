\version "2.26.0"
\language "english"

\header {
  title = "Beethoven: Piano Sonata No. 8 in C minor, Op. 13 “Pathétique”"
  subtitle = "I. Grave — Allegro di molto e con brio · mm. 1–19"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

% 谱源：DCML Beethoven piano sonatas corpus (GitLab export, MS3); cross-checked with Craig Sapp /beethoven-piano-sonatas kern; Noctave/Mutopia for the Grave.

#(set-global-staff-size 17)

D = \tweak Stem.direction #DOWN \etc
U = \tweak Stem.direction #UP \etc

\score {
  \new PianoStaff \with { instrumentName = "Piano" } <<
    \new Staff = "rh" \with { midiInstrument = "acoustic grand" } <<
    { \voiceOne {
  \clef "treble" \time 4/4 \key c \minor \oneVoice \tempo "Grave" \U <ef ~ g ~ c' ~>4 \U <ef g
    c'>16. \U <g c'>32 [ \U <g b d'>16. \U <g c' ef'>32 ] \U <a c' ef'>4 ^(
  _\=2( \U <b d'>8 ) \=2) r8 | % 1
  \U <b ~ d' ~ f' ~>4 \U <b d' f'>16. \U <b d' f'>32 [ \U <b d' g'>16. \U <b d'
    af'!>32 ] \U <b d' af'>4 _( ^\=2( _\=3( \U <c' ef' g'>8 ) \=2) \=3) r8 | % 2
  \U <fs' ~ a' ~ c'' ~>4 _\fp \U <fs' a' c''>16. \U <fs' a' c''>32 [ \U <fs'
    a' d''>16. \U <fs' a' ef''>32 ] \D <fs' a' ef''>4 _( _\=2( ^\=3( _\sf \U
  <d' g' d''>16 ) \=2) \=3) -. -. -. r32 \U <fs' a' c''>32 [ \U <fs' a' d''>16.
  \U <fs' a' ef''>32 ] | % 3
  \D <fs' a' ef''>4 ^( _\sf _\> \U <d' g' d''>8 [ \! _\p \U <g' c'' e''>8 ] \D
  <af'! c'' f''!>8 ) -. -. -. [ \D af''8 ~ ] _\sf \D af''32 [ \tweak
  TupletBracket.stencil ##f \tuplet 3/2 {
    \D g''64 ^( \D af''64 \D bf''64 }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D af''64 \D g''64 \D f''64 ] }
  \D ef''64 [ \D d''64 \D c''64 \D bf'64 ] \tweak TupletBracket.stencil ##f
  \tuplet 3/2 {
    \U af'64 [ \U g'64 \U f'!64 }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U ef'64 \U d'64 \U f'64 }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U af'64 \U f'64 \U d'64 ) ] }
  | % 4
  \U ef'8 -. [ _\p \U <ef' ~ ef'' ~>8 ] \U <ef' ef''>16. \D <ef' ef''>32 [ \D
  <f' f''>16. \D <g' g''>32 ] \D <g' g''>8 ^( [ \D <f' f''>16 ) ] r32 \clef
  "bass" \D f'32 _\ff \D <f af b f'>16. \D <f af b f'>32 [ \D <f af c' f'>16. \D
  <f af c' f'>32 ] | % 5
  \D <f af d' f'>8 [ _\p \clef "treble" \D <f' ~ f'' ~>8 ] \D <f' f''>16. \D <f'
    f''>32 [ \D <g' g''>16. \D <af' af''>32 ] \D <af' af''>8 ^( [ \D <g' g''>16
  ) ] r32 \U <g cs' e' g'>32 \U <a cs' e' a'!>16. \U <a cs' e' a'>32 [ \U
  <bf! cs' e' bf'!>16. \U <bf cs' e' bf'>32 ] | % 6
  \U <a d' fs' a'>8 [ \U <a' ~ a''! ~>8 ] _\p \D <a' a''>16. \D <a' a''>32 [ \D
  <b' b''!>16. \D <c''! c'''!>32 ] \D <c'' c'''>8 ^( [ \D <b' b''>16 ) ] r16 r8
  \D <b' b''>16. [ \D <c'' c'''>32 ] | % 7
  \D <cs'' cs'''>8 ^( [ \D <d'' d'''>8 ) ] r8 \D <d'' d'''>16. [ \D <ef''
    ef'''>32 ] \D <e'' e'''!>8 ^( \D <f''! f'''!>4 ) \D <f'' f'''>8 | % 8
  \D <f'' ~ f''' ~>8 ^( _\sfp \D <f'' f'''>32 [ \D ef'''!64 \D d'''64 \D f'''64
  \D ef'''64 \D d'''64 \D c'''!64 ) ] \D b''16 ^( -. [ \D b''16 -. \D <f'' b''>16
  -. -. \D <f'' b''>16 ) -. -. ] \D <ef'' c'''>8 r8 r4 | % 9

  \barNumberCheck #10
  \D c'''8 ~ ^( [ _\p \D c'''32 \D b''64 \D c'''64 ] \tweak
  TupletBracket.stencil ##f \tuplet 3/2 {
    \D d'''64 [ \D c'''64 \D bf''64 }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D af''64 \D g''64 \D bf''64 ) ] }
  \D af''16 ^( -. [ \D af''16 -. \D af''16 -. \D af''16 ) -. ] \D g''16 ^( [ \D
  ef'''16 ~ ] \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D ef'''64 [ \D d'''64 \D df'''64 }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c'''64 \D b''64 \D bf''64 ] }
  \tweak TupletBracket.stencil ##f \tuplet 7/4 {
    \D a''64*119/120 [ \D af''64*119/120 \D g''64*119/120 \D fs''64*119/120 \D
    f''64*119/120 \D e''64*119/120 \D ef''64*119/120 ] }
  \U d''128 [ \U df''128 \U c''128 \U b'128 \U bf'128 \U a'128 \U af'128 \U g'128
  \U fs'128 \U f'128 \U e'128 \U ef'128 \U d'128 \U df'128 \U c'128 \U b128 )
  ] \U af'16. ^\fermata [ _\sf \U b32 ] s1*1/1920 | % 10
  \tempo "Allegro di molto e con brio" \time 2/2 \U c'2. _\p \U <bf! e'>4 -. -. | % 11
  \U <af f'>4 -. -. \U <e' g'>4 -. -. \U <f' af'>4 -. -. \U <d' b'>4 -. -. | % 12
  \U <ef'! c''>4 -. -. \U <e' c''>2 \D <bf'! e''!>4 -. -. | % 13
  \D <af' f''>4 -. -. \D <e'' g''>4 -. -. \D <f'' af''>4 -. -. \D <d'' b''>4 -.
  -. | % 14
  \D <c'' ef''! g'' c'''>2 -. -. -. -. \D <g' b' f'' g''>2 -. -. -. -. | % 15
  \D <g' c'' ef''>2 -. -. -. \U <f' af' d''>2 -. -. -. | % 16
  \voiceOne <ef' ~ c'' ~>1 _( ^\=2( | % 17
  \oneVoice \U <ef' a' c''>2 \U <d' f' b'>2 ) \=2) | % 18
  \U <c' ef' c''>4 -. -. -. _\p \U c'2 \U <bf! e'>4 -. -. } }
    { \voiceTwo {
    \clef "treble" \time 4/4 \key c \minor s32*151 \clef "bass" s32*13 \clef
    "treble" s8*39 | % 10
    \time 2/2 s1*6 | % 16
    \D g'2 \D fs'2 } }
  >>
    \new Staff = "lh" \with { midiInstrument = "acoustic grand" } <<
    { \voiceOne {
    \clef "bass" \time 4/4 \key c \minor \U <c, ~ ef, ~ g, ~ c ~>4 ^\fp \U <c,
      ef, g, c>16. \U ef32 [ \U d16. \U c32 ] \D fs4 ^( \D g8 ) r16. \U af,32 | % 1
    \D af4 ~ ^\fp \D af16. \D af32 [ \D g16. \D f!32 ] \D ef4 ~ \D ef8 r16. \D
    ef32 -. | % 2
    \D ef'4 ~ \D ef'16. \D ef'32 [ \D d'16. \D c'32 ] \D c'4 ^( \D b16 ) -. r32
    \D ef'32 [ \D d'16. \D c'32 ] | % 3
    \D c'4 _( \D b8 [ \D <bf c' e'>8 ] \D <af c' f'!>8 ) -. -. -. r8 \U <bf,,
      bf,>4 ^\sf | % 4
    \U <ef,! ef!>16 \D <ef g bf>16 [ \D <ef g bf>16 \D <ef g bf>16 ] \D <ef g
      bf>16 [ \D <ef g bf>16 \D <ef g bf>16 \D <ef g bf>16 ] \D <ef af c'>16
    [ \D <ef af c'>16 \D <ef af c'>16 \D <ef af c'>16 ] \U <d, d>16 [ \U <d, d>16
    \U <c, c>16 \U <c, c>16 ] | % 5
    \U <b,, b,>16 \D <b, d f af>16 [ \D <b, d f af>16 \D <b, d f af>16 ] \D
    <bf, d f af>16 [ \D <bf, d f af>16 \D <bf, d f af>16 \D <bf, d f af>16 ]
    \D <bf, cs e g>16 [ \D <bf, cs e g>16 \D <bf, cs e g>16 \D <bf, cs e
      g>16 ] \U <a,, a,!>16 [ ^\ff \U <a,, a,>16 \U <g,, g,>16 \U <g,, g,>16 ] | % 6
    \U <fs,, fs,>16 \D <fs! a d'>16 [ \D <fs a d'>16 \D <fs a d'>16 ] \D
    <fs a d'>16 [ \D <fs a d'>16 \D <fs a d'>16 \D <fs a d'>16 ] \D <f af
      d'>16 [ \D <f af d'>16 \D <f af d'>16 \D <f af d'>16 ] \D <d f b>16 [ \D
    <d f b>16 \D <d f b>16 \D <d f b>16 ] | % 7
    \D <b, d af>16 [ \D <b, d af>16 \D <b, d af>16 \D <b, d af>16 ] \U <af, b,
      f>16 [ \U <af, b, f>16 \U <af, b, f>16 \U <af, b, f>16 ] \U <g, b, f>16 [
    \U <g, b, f>16 \U <g, b, f>16 \U <g, b, f>16 ] \U <af, c f>16 [ \U <af, c f>16
    \U <af, c f>16 \U <af, c f>16 ] | % 8
    \U <g, b, f>8 r8 r8 \clef "treble" \D <g' d''>16 ^( -. -. [ \D <g' d''>16 )
    -. -. ] \D <af' c''>8 r8 r4 | % 9

    \barNumberCheck #10
    r4 r8 \clef "bass" \D <f c' d'>16 -. -. -. [ \D <f c' d'>16 -. -. -. ] \D <g
      c' ef'>8 r8 \U <g, d f>8 r8 ^\fermata | % 10
    \time 2/2 \U c,8 [ \U c8 \U c,8 \U c8 ] \U c,8 [ \U c8 \U c,8 \U c8 ] | % 11
    \U c,8 [ \U c8 \U c,8 \U c8 ] \U c,8 [ \U c8 \U c,8 \U c8 ] | % 12
    \U c,8 [ \U c8 \U c,8 \U c8 ] \U c,8 [ \U c8 \U c,8 \U c8 ] | % 13
    \U c,8 [ \U c8 \U c,8 \U c8 ] \U c,8 [ \U c8 \U c,8 \U c8 ] | % 14
    \U c,8 [ \U c8 \U c,8 \U c8 ] \U d,8 [ \U d8 \U d,8 \U d8 ] | % 15
    \U ef,8 [ \U ef8 \U ef,8 \U ef8 ] \U f,8 [ \U f8 \U f,8 \U f8 ] | % 16
    \U g,8 [ \U g8 \U g,8 \U g8 ] \D af,8 [ \D af8 \D af,8 \D af8 ] | % 17
    \U fs,8 [ \U fs!8 \U fs,8 \U fs8 ] \U g,8 [ \U g8 \U g,8 \U g8 ] | % 18
    \U c,8 [ \U c8 \U c,8 \U c8 ] \U c,8 [ \U c8 \U c,8 \U c8 ] } }
  >>
  >>
  \layout { }
  \midi { }
}
