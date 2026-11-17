\version "2.26.0"
\language "english"

\header {
  title = "Beethoven: Piano Sonata No. 26 in E-flat major, Op. 81a “Les Adieux”"
  subtitle = "I. Das Lebewohl: Adagio — Allegro · mm. 1–25"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

% 谱源：DCML piano sonata corpus (GitLab export, MS3); cross-checked with Craig Sapp kern; Noctave edition (after Clementi 1st ed.) for Adagio.

#(set-global-staff-size 17)

D = \tweak Stem.direction #DOWN \etc
U = \tweak Stem.direction #UP \etc

\score {
  \new PianoStaff \with { instrumentName = "Piano" } <<
    \new Staff = "rh" \with { midiInstrument = "acoustic grand" } <<
    { \voiceOne {
  \clef "treble" \time 2/4 \key ef \major \oneVoice \tempo "Adagio" \U <ef' g'>4 \U <bf f'>4 | % 1
  \U <g ef'>4. \U ef'16. _( [ \U af'32 ) ] | % 2
  \U g'8 [ \U g'16. _( \U df''32 ) ] \U c''8 [ \U c''16. ^\turn \U d''32 ] | % 3
  \voiceOne \U ef''8. \U c''16 \U b'8 \U g''16 ^( [ \U ef'''16 ) ] | % 4
  \U ef'''8. [ _\< \U c'''16 ] \U b''8 [ \U bf''8 ] <>\! | % 5
  \U bf''4 ~ _\sf _\> \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bf''16 [ \! \oneVoice \U bf'16 _( \voiceOne \U c''16 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U a'16 _( [ \U bf'16 ) \U af'16 ] }
  | % 6
  \oneVoice \U <bf df' e' g'>4 \U <af d'! f'>4 | % 7
  \voiceOne \U ef'!4. \U gf'16. [ \U cf''32 ] | % 8
  \U cf''8 [ \U bf'16. \U ff''32 ] \U ef''8 [ \U ef''16. \U f''32 ] | % 9

  \barNumberCheck #10
  \U gf''8. \U ef''16 \U d''8 \U df''16. ^\turn [ \U ef''32 ] | % 10
  \U ff''8. [ \U ef''32 \U df''32 ] \U cf''8 [ _\< \U <bf' ef''>8 ] \! _\>
  <>\! | % 11
  \oneVoice \U <d'! af' bf' d''!>8 r8 r16 \U <d' af' bf' d''>16 _( [ \U <ef'
    gf' bf' ef''>16 ) \U <ef' gf' bf' ef''>16 ] | % 12
  \D <f' bf' f''>8 r8 r16 \D <bf' d''>16 ^( [ \D <bf' ef''>16 ) \D <bf'
    ef''>16 ] | % 13
  \D <bf' f''>8 r8 r16 \D <bf' f''>16 ^( [ _\< \D <bf' g''!>16 \! _\> \D <af'
    af''>16 ) ] <>\! | % 14
  \D <af' af''>8 r8 r16 \D <bf' f''>16 ^( [ _\< \D <bf' g''>16 \! _\> \D <af'
    af''>16 ) ] <>\! | % 15
  r8 \D <af' af''>8 r8 \D <af' af''>8 \bar "||" % 16
  \tempo "Allegro" \break \time 2/2 \D <af' af''>2. _\f \voiceOne \U d''8 ^( [ \U g''8 ) ] | % 17
  \U g''4 \U c''8 ^( [ \U f''8 ) ] \U f''4 \U bf'8 ^( [ \U ef''8 ) ] | % 18
  \U ef''2 ^( _\sf _\> \U <af' bf' d''>4 \! \U <bf' ef''>4 | % 19

  \barNumberCheck #20
  \U f''4 \U g''4 \U af''4 \U bf''4 ) | % 20
  \oneVoice \D <g' bf' g''>4 -. -. -. _\< r4 \D <bf' bf''>4 -. -. r4 <>\! | % 21
  \D <bf'' bf'''>2. _\sf \D <bf' ~ bf'' ~>4 _\sfp | % 22
  \D <bf' bf''>2. \D <g' g''>4 ^( | % 23
  \D <f' f''>4 \D <d' d''>4 \U <cf' cf''!>4 \U <bf bf'>4 ) | % 24
  \U <bf bf'>4 -. -. _\< r4 \D <bf' bf''>4 -. -. r4 <>\! } }
    { \voiceTwo {
  \clef "treble" \time 2/4 \key ef \major s1. | % 3
  \D ef'8 [ \D <ef' fs'>8 ] \D <d' g'>8 d''8\rest | % 4
  \D ef''8 [ \D <ef'' fs''>8 \D <d'' g''>8 \D <d'' g''>8 ] | % 5
  \D d''8 [ \D ef''8 ] \tuplet 3/2 {
    \D f''!16 s16 r16 }
  g'8\rest s2 | % 7
  \U gf4. \D ef'8 | % 8
  \D ff'8 [ \D ff'8 ] \D ef'8 r8 | % 9

  \barNumberCheck #10
  \D c''!8 [ \D c''8 \D bf'8 \D bf'8 ~ ] | % 10
  \D bf'8 [ \D bf'8 \D af'8 \D ef'8 ] s2*5 \bar "||" % 16
  \time 2/2 s2. \D g'4 | % 17
  \D g'4 \D f'4 \D f'4 \D ef'4 | % 18
  \D <ef' af' bf'>2 \D d'4 \D ef'4 | % 19

  \barNumberCheck #20
  \D <f' bf'>4 \D <g' bf'>4 \D <af' bf'>4 \D bf'4 } }
  >>
    \new Staff = "lh" \with { midiInstrument = "acoustic grand" } <<
    { \voiceOne {
  \clef "bass" \time 2/4 \key ef \major \oneVoice R2 | % 1
  \U <c, c>4. \U <c ef>8 | % 2
  \U <bf, e>8 [ \U <bf, e>8 \U <a, f>8 \U <af, fs>8 ] | % 3
  \voiceOne \U g8 _( [ \U a8 ] \U b8 ) \oneVoice g,8\rest | % 4
  \clef "treble" \voiceOne \U g'8 [ \U a'8 \U b'8 \U bf'8 ] | % 5
  \U bf'4 ~ \U bf'8 r8 | % 6
  \clef "bass" \oneVoice r4 \U <bf,, bf,>4 | % 7
  \U <cf, cf>4. \D <cf gf>8 | % 8
  \D <df gf>8 [ \D <df gf>8 ] \D <cf gf>8 [ \D <bf, gf ~>8 ] | % 9

  \barNumberCheck #10
  \voiceOne \U gf8 [ \U f8 \U f8 \U ff8 ~ ] | % 10
  \U ff8 [ \U ef8 \U ef8 \U gf8 ] | % 11
  \oneVoice \U <f,! bf, f!>8 r8 r16 \U <f, bf, f>16 _( [ \U <ef, bf, ef>16 )
  \U <ef, bf, ef>16 ] | % 12
  \U <d, bf, d>8 r8 r16 \clef "treble" \U <f' af'>16 _( [ \U <ef' gf'>16 ) \U
  <ef' gf'>16 ] | % 13
  \U <d' f'>8 r8 r16 \U <d' f'>16 _( [ \U <df' ef'>16 \U <cf' ef'>16 ) ] | % 14
  \U <cf' ef'>8 r8 r16 \U <d'! f'>16 _( [ \U <df' ef'>16 \U <c'! ef'>16 ) ] | % 15
  r8 \U <c' ef'>8 r8 \U <c' ef'>8 \bar "||" % 16
  \clef "bass" \time 2/2 \D <c' ef'>2. \D <b d'>8 ^( [ \D <bf df'>8 ) ] | % 17
  \D <bf df'>4 \D <a c'>8 ^( [ \D <af cf'>8 ) ] \D <af cf'>4 \D <g bf>8 ^(
  [ \D <fs a>8 ) ] | % 18
  \D <f! af!>2. \D <ef g>4 | % 19

  \barNumberCheck #20
  \D <d f>4 \D <c ef>4 \D <bf, d>4 \D <bf, d f>4 | % 20
  \D ef,8 [ \D bf,8 \D g8 \D bf,8 ] \D ef,8 [ \D bf,8 \D g8 \D bf,8 ] | % 21
  \D f,8 [ \D bf,8 \D af8 \D bf,8 ] \D f,8 [ \D bf,8 \D af8 \D bf,8 ] | % 22
  \D g,8 [ \D bf,8 \D bf8 \D bf,8 ] \D g,8 [ \D bf,8 \D bf8 \D bf,8 ] | % 23
  \D af,8 [ \D bf,8 \D af8 \D bf,8 ] \D bf,,8 [ \D bf,8 \D f8 \D bf,8 ] | % 24
  \D ef,8 [ \D bf,8 \D g8 \D bf,8 ] \D ef,8 [ \D bf,8 \D g8 \D bf,8 ] } }
    { \voiceTwo {
  \clef "bass" \time 2/4 \key ef \major s1. | % 3
  \D g,4. s8 | % 4
  \clef "treble" \D g4. \D g'8 | % 5
  \D <f' af'!>8 [ \D <ef' g'>8 \D <d' f'>8 \D <bf d'>8 ] | % 6
  \clef "bass" s1. | % 9

  \barNumberCheck #10
  \D a,4 \D bf,8 [ \D af,8 ] | % 10
  \D g,!4 \D af,8 [ \D <gf, bf,>8 ] s16*13 \clef "treble" s16*27 \bar "||" % 16
  \clef "bass" \time 2/2 } }
  >>
  >>
  \layout { }
  \midi { }
}
