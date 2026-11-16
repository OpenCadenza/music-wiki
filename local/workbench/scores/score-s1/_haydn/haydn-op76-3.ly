\version "2.26.0"
% automatically converted by musicxml2ly from E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s1\_haydn\haydn-op76-3.mxl
\pointAndClickOff

%% additional definitions required by the score:
hideNote =
  \tweak Dots.transparent ##t
  \tweak NoteHead.transparent ##t
  \tweak NoteHead.no-ledgers ##t
  \tweak Stem.transparent ##t
  \tweak Accidental.transparent ##t
  \tweak Rest.transparent ##t
  \tweak TabNoteHead.transparent ##t \etc

D = \tweak Stem.direction #DOWN \etc
U = \tweak Stem.direction #UP \etc


%% additional macros required by the score:
"fz sempre" = #(make-dynamic-script ""fz sempre"")
"p dolce" = #(make-dynamic-script ""p dolce"")

\header {
  title = \markup \normal-text \normalsize \fontsize #5.207
  "String Quartet in C major"
  subtitle = \markup \normal-text \normalsize \fontsize #2.120
  "Hob.III:77, Op.76 No.3"
  composer = \markup \normal-text \normalsize "Joseph Haydn"
  copyright = \markup \normal-text \normalsize \fontsize #-1.705
  "OpenScore (CC0)"
  "work-number" = "Hob.III:77, Op.76 No.3"
  "work-title" = "String Quartet in C major, Hob.III:77, Op.76 No.3"
  "id: copyright" = "OpenScore (CC0)"
  "id: composer" = "Joseph Haydn"
  "id: arranger" =
  "Transcribed fTranscribed by mozbadel from the IMSLP file(s) at https://imslp.org/wiki/Special:ReverseLookup/28079"
  "id: software" = "MuseScore Studio 4.7.4"
  "id: encoding-date" = "2026-09-05"
  "id: source" = "http://musescore.com/user/37221589/scores/20428156"
}
#(set-global-staff-size 13.657322834645669)
\paper {
  paper-width = 21.01\cm
  paper-height = 29.69\cm
  top-margin = 1.5\cm
  bottom-margin = 1.5\cm
  left-margin = 1.5\cm
  right-margin = 1.51\cm
  indent = 1.62\cm
}
\layout {
  \context {
    \Staff
    printKeyCancellation = ##f
  }
  \context {
    \Score
    doubleRepeatBarType = ":|.|:"
    autoBeaming = ##f
  }
}
PartPOneVoiceOne = \relative g'' {
  \repeat volta 2 {
    \repeat volta 2 {
      \repeat volta 2 {
        \clef "treble" \time 4/4 \key c \major \partial 8 \oneVoice \D g8
        ^\markup \fontsize #6.578 "I. " ^\markup \fontsize #4.088 \bold Allegro
        _\f \D e4 ( \D f8 ) -. [ \D d8 -. ] \D c4 -. r8 \U g8 -. _\p | % 1
        \U e8 -. [ \U a8 -. \U g8 -. \U fis8 -. ] \U g4 r8 \D d'8 | % 2
        \D e8 \D g4 \D f4 \D e16 ^\trill [ \D d16 ] \D e8 -. [ \D c'8 -. ] _\f | % 3
        \U d,,8 -. r8 \U <g, g'>8 -. r8 \U <c e>4 r4 \break | % 4
        R1 | % 5
        r4 r16. \U g'32 [ \U a16. \U b32 ] \D c16. [ \D d32 \D e16. \D f32 ] \D
        g8 [ \D c8 ] | % 6
        \D b8 ( [ \D a8 ] \D g8 ) [ \D c,8 ] \U b8 ( [ \U a8 ] \D g16. ) [ \D g'32
        \D e16. \D c32 ] \break | % 7
        \D b16. [ _\fz \D c32 \D d16. \D e32 ] \D f16. [ \D e32 \D f16. \D a32 ]
        \D e16. [ \D g32 \D d16. \D f32 ] \D c16. [ \D g'32 \D e16. \D c32 ] | % 8
        \D b16. [ _\fz \D c32 \D d16. \D e32 ] \D f16. [ \D e32 \D f16. \D a32 ]
        \D e16. [ \D g32 \D d16. \D f32 ] \D c16. [ \D g'32 \D e16. \D c32 ]
        \break | % 9

        \barNumberCheck #10
        \D b16. [ _\fz \D c32 \D d16. \D e32 ] \D f16. [ \D g32 \D a16. \D b32 ]
        \D c16. [ \D d32 \D e16. \D f32 ] \D g16. [ \D g32 \D g16. \D g32 ] | % 10
        \D g16. [ \D g32 \D g16. \D g32 ] \D g16. [ \D g32 \D g16. \D g32 ] \D g16.
        [ \D g32 \D g16. \D g32 ] \D g16. [ \D g32 \D g16. \D g32 ] \pageBreak | % 11
        \D g16. [ \D g,32 \D g'16. \D g,32 ] \D g'16. [ \D g,32 \D g'16. \D g,32
        ] \D g'4 r4 | % 12
        r4 r8 \D d8 \D b4 ( \D c8 ) -. [ \D a8 -. ] | % 13
        \D b8 \D d4 \D c4 \D b16 ^\trill [ \D a16 ] \D b8 [ \D a8 ~ ] | % 14
        \D a8 [ \D g16 ^\trill \D fis16 ] \D g8 [ \D f8 ~ ] \D f8 [ \D e16
        ^\trill \D dis16 ] \D e8 [ \D d8 ] \break | % 15
        \D cis2 \D c4 \D e8 ( [ \D c8 ) ] | % 16
        \D b4 \D d8 ( [ \D b8 ) ] \D g'4. ( \D a16 [ \D g16 ) ] | % 17
        \U fis8 [ \U d,8 ] r8 \D d''8 -. \D b8. ( ^\trill [ \D a32 \D b32 ) ] \D
        c8 ( -. [ \D b8 ) -. ] \break | % 18
        \D g8 ( [ \D b8 ) ] \D a8 -. [ \D b8 -. ] \D gis8. ( ^\trill [ \D fis32
        \D gis32 ) ] \D a8 [ \D g32 ( \D fis32 \D e32 \D fis32 ) ] | % 19

        \barNumberCheck #20
        \D g8 -. [ \D d32 ( \D cis32 \D b32 \D cis32 ) ] \D d8 [ \D g8 -. ] \D
        fis8. ( ^\trill [ _\fz \D e32 \D fis32 ) ] \D g8 ( -. [ \D g8 ) -. ]
        \break | % 20
        \D fis8. ( ^\trill [ _\fz \D e32 \D fis32 ) ] \D g8 ( -. [ \D g8 ) -. ]
        \D fis8. ( ^\trill [ _\fz \D e32 \D fis32 ) ] \D g8 ( -. [ \D b8 ) -. ]
        | % 21
        \tweak TupletBracket.stencil ##f \tuplet 6/4 {
          \D c16 ( [ _\ff \D a16 \D fis16 \D d16 \D c16 \D a16 ) ] }
        \tweak TupletBracket.stencil ##f \tuplet 6/4 {
          \D fis!16 ( [ \D a16 \D c16 \D d16 \D fis16 \D a16 ) ] }
        \D c8 r8 r8 \U <g, ~ b>8 ( _\p | % 22
        \voiceOne \U a4. \U b8 ) \U c4 \oneVoice r8 \D e8 -. _\fz \break | % 23
        \D cis4 ( \D d8 ) [ \D c8 -. ] \U ais4 ( \U b8 ) [ \U a8 -. ] _\fz | % 24
        \U fis4 ( \D g8 ) [ \D e'8 ] _\fz \U g,4 ( \U a8 ) [ \U fis8 -. ] | % 25
        \U g4 _\f r8 \U g8 \U fis8 -. [ \U c'8 -. \U b8 -. \U a8 -. ] \pageBreak
        | % 26
        \D g8 -. [ \D b8 -. \D d8 -. \D g8 -. ] \D fis8 ( [ \D c'8 \D b8 \D a8 )
        ] | % 27
        \D g8 [ \D b16 \D d16 ] \D g16 [ \D fis16 \D e16 \D d16 ] \D c16 ( [ \D
        d,16 ) \D c'16 ( \D d,16 ) ] \D c'16 ( [ \D d,16 ) \D c'16 ( \D d,16 ) ]
        \break | % 28
        \D bes'16 ( [ _\fz \D d,16 ) \D bes'16 ( \D d,16 ) ] \D bes'16 ( [ \D d,16
        ) \D bes'16 ( \D d,16 ) ] \D c'16 ( [ \D d,16 ) \D c'16 ( \D d,16 ) ] \D
        c'16 ( [ \D d,16 ) \D c'16 ( \D d,16 ) ] | % 29

        \barNumberCheck #30
        \D bes'16 [ _\ff \D g16 \D bes16 \D d16 ] \D g16 [ \D d16 \D bes16 \D g16
        ] \D as16 [ \D d16 \D f!16 \D d16 ] \D as'!16 [ \D f16 \D d16 \D as16 ]
        \break | % 30
        \D g16 [ \D bes16 \D es16 \D g16 ] \D as,16 [ \D d16 \D f16 \D as!16 ]
        \D g,16 [ \D bes16 \D es16 \D g16 ] \D as,16 [ \D d16 \D f16 \D as16 ] | % 31
        \D g16 [ \D es16 \D as16 \D f16 ] \D g16 [ \D es16 \D as16 \D f16 ] \D g8
        r8 r4 | % 32
        r2 r4 r8 \D bes,,8 _\p \break | % 33
        \U g4 ( \U as8 [ \U f8 ) ] \U es4. ( \U f8 | % 34
        \U g4. \U as8 \D bes4. \U as8 ) | % 35
        \U g4. ( _\pp \D bes8 ) \U g4. ( \D bes8 ) | % 36
        \U g2 ~ \U g8 ( [ \U fis8 \U a!8 \U fis8 ) ] \break | % 37
        \U g4 _\f r8 \U g8 \U fis8 -. [ \U c'8 -. \U b!8 -. \U a8 -. ] | % 38
        \D g8 -. [ \D b8 -. \D d8 -. \D g8 -. ] \D fis8 ( [ \D c'8 \D b8 \D a8 )
        ] \pageBreak | % 39

        \barNumberCheck #40
        \D g16 ( [ \D a32 \D b32 ] \D c32 [ \D d32 \D e32 \D fis32 ) ] \D g16 [
        \D fis16 \D e16 \D d16 ] \D c16 [ \D d,,16 \D c''16 \D d,,16 ] \D c''16
        [ \D d,,16 \D c''16 \D d,,16 ] | % 40
        \D b''16 [ \D d,,16 \D b''16 \D d,,16 ] \D b''16 [ \D d,,16 \D b''16 \D
        d,,16 ] \D c''16 [ \D d,,16 \D c''16 \D d,,16 ] \D c''16 [ \D d,,16 \D
        c''16 \D d,,16 ] \break | % 41
        \D b''16 [ \D d,,16 \D b''16 \D d,,16 ] \D c''16 [ \D d,,16 \D c''16 \D
        d,,16 ] \D b''16 [ \D d,,16 \D b''16 \D d,,16 ] \D c''16 [ \D d,,16 \D
        c''16 \D d,,16 ] | % 42
        \D b''16 [ \D g16 \D b16 \D d16 ] \D g8 [ \D b,,8 ] \D c8. ( ^\trill [
        \D b32 \D c32 ) ] \D d8 ( -. [ \D <a fis'>8 ) -. ] \alternative {
          \volta 1 {
            \once \override Score.VoltaBracket.text = \markup "1." \D <b g'>8 -.
            [ \D <d a'>8 -. \D <g b>8 -. \D <d d'>8 -. ] \D <g b>8 r8 r4 \break
            r8 \D d8 -. _\p \D b4 -. r8 \D d'8 -. \D b4 -. r8 \D d,8 -. [ \D b8
            -. \D e8 -. ] \D c8 -. [ \D f!8 -. \D d8 -. ] }
          \volta 2 {
            \once \override Score.VoltaBracket.text = \markup "2." | % 43
            \D b8 -. [ \D g'8 \D d8 -. ] \D a'8 \D g8 -. [ \D b8 \D d,8 -. ] \D
            d'8 \D g,4 \D b4 r4 }
        }
      }
      \repeat volta 2 {
        | % 44
        r4 r16. \U d,,32 [ _\p \U e16. \U fis32 ] \U g16. [ \U a32 \U b16. \U c32
        ] \D d8 r8 \break | % 45
        r16. \U f,!32 [ _\f \U e16. \U d32 ] \U c16. [ \U e32 \U a16. \U c32 ]
        \D e16. ( [ \D dis32 ) \D e16. ( \D dis32 ) ] \D e8 r8 | % 46
        r16. \U e,32 [ \U fis16. \U gis32 ] \D a16. [ \D b32 \D c16. \D d32 ] \D
        e16. ( [ \D dis32 \D e16. \D dis32 ) ] \D e16. ( [ \D dis32 \D e16. \D
        dis32 ) ] \break | % 47
        \D e16. ( [ \D dis32 \D e16. \D dis32 ] \D e16. [ \D dis32 \D e16. \D
        dis32 ) ] \D e16. ( [ \D dis32 \D e16. \D dis32 ) ] \D e8 -. [ \D f!8 -.
        ] _\p | % 48
        \D d4 -. r8 \D e8 -. \D c4 -. r8 \D bes'8 -. | % 49

        \barNumberCheck #50
        \D g4 -. r8 \D a8 _\f \D f4 ( \D g8 ) -. [ \D e8 -. ] \pageBreak | % 50
        \D d16 ( [ \D cis16 \D d16 \D e16 ) ] \D f8 -. [ \D g8 -. ] \D e4 ( \D f8
        ) -. [ \D d8 -. ] | % 51
        \D c!8 -. [ \D d8 -. \D e8 -. \D g,8 -. ] \U e8 ( [ \U a8 \U g8 \U fis8
        ) ] | % 52
        \U g4 r8 \U g8 \U f!8 ( [ \U bes8 \U a8 \U gis8 ) ] | % 53
        \U a4 r8 \U a8 \D gis8 ( [ \D f'8 \D e8 \D d8 ) ] \break | % 54
        \D c8 ( [ \D a8 \D b8 \D c8 ) ] \U b8 ( [ \U gis8 \U a8 \U b8 ) ] | % 55
        \D c8 ( [ \D cis8 \D d8 \D e8 ) ] \D f8 ( [ \D g8 \D a8 ) \D a8 -. ] | % 56
        \D g4. \D c8 ~ \D c8 [ \D b16 \D a16 ] \D b8 [ \D bes8 ] | % 57
        \D a4. \D d8 ~ \D d8 [ \D c16 \D b!16 ] \D c8 [ \D c8 ] \break | % 58
        \D b4. \D e8 ~ \D e8 [ \D dis16 \D cis16 ] \D dis8 [ \D c8 ] | % 59

        \barNumberCheck #60
        \D a4 ( \D b8 [ \D g8 ) ] \D a8 ( [ \D fis8 \D g8 \D e8 ) ] | % 60
        \D dis4 ( \D e8 ) [ \D ais,8 ] \U b8 ( [ \U ais8 ] \D b8 ) [ \D c'!8 ]
        _\p \break | % 61
        \D a8. ( ^\trill [ \D g32 \D a32 ) ] \D b8 ( [ \D g8 ] \D a8 [ \D fis8
        \D g8 \D e8 ) ] | % 62
        \D dis4 ( \D e8 ) [ \D ais,8 ] \U b8 ( [ \U ais8 \U b8 \U ais8 ) ]
        \break | % 63
        \U b8 ( [ \U ais8 \U b8 \U ais8 ) ] \D b4 ( \D b'8 ) \D b,8 _\f | % 64
        \U gis4 ( \U a!8 ) [ \U fis8 ] \U e16 [ \U fis16 \U gis16 \U a16 ] \D b8
        [ \D e8 ] | % 65
        \D dis8 \D fis4 _\fz \D dis16 [ \D b16 ] \D e16 [ \D fis16 \D gis16 \D a16
        ] \D b8 [ \D gis16 \D e16 ] \pageBreak | % 66
        \D dis8 \D fis4 _\fz \D dis16 [ \D b16 ] \D e8 \D e4 _\fz \D gis16 [ \D
        e16 ] | % 67
        \D dis16. [ \D e32 \D fis16. \D gis32 ] \D a16. [ \D fis32 \D a16. \D
        fis32 ] \D e16. [ \D fis32 \D gis16. \D a32 ] \D b16. [ \D gis32 \D b16.
        \D gis32 ] \break | % 68
        \D a16. [ \D cis32 \D gis16. \D b32 ] \D fis16. [ \D a32 \D fis16. \D
        dis32 ] \D e8 \D b'4 _\fz \D gis16 [ \D e16 ] | % 69

        \barNumberCheck #70
        \D fis16. [ \D a32 \D fis16. \D dis32 ] \D b16. [ \D dis32 \D fis16. \D
        dis32 ] \D e8 \D e4 _\fz \D gis16 [ \D e16 ] \break | % 70
        \D dis16. [ \D e32 \D fis16. \D gis32 ] \D a16. [ \D fis32 \D a16. \D
        fis32 ] \D e16. [ \D fis32 \D gis16. \D a32 ] \D b16. [ \D gis32 \D b16.
        \D gis32 ] | % 71
        \D a16. [ \D cis32 \D gis16. \D b32 ] \D fis16. [ \D a32 \D fis16. \D
        dis32 ] \D e8 \D b'4 _\fz \D gis16 [ \D e16 ] \break | % 72
        \D fis16. [ \D a32 \D fis16. \D dis32 ] \D b16. [ \D dis32 \D fis16. \D
        dis32 ] \D e8 \D e4 _\fz \D b'8 | % 73
        \U b,,8 \D a''4 _\fz \D fis16 [ \D dis16 ] \D e8 \D e4 _\fz \D b'8 _\p | % 74
        \D b,4 ( \D c8 ) [ \D a8 ] \U g16 ( [ \U fis16 \U g16 \U a16 ) ] \D b8 [
        \D e8 ] \break | % 75
        \D dis8 \D fis4 \D dis16 [ \D b16 ] \D e8 \D g4 \D e8 _\pp | % 76
        \D b4 ( \D c8 ) [ \D a8 ] \U g16 ( [ \U fis16 \U g16 \U a16 ) ] \D b8 [
        \slashed { \U dis!8 ( } {} \D e8 ) ] | % 77
        \D b8 [ \slashed { \U dis8 ( } {} \D e8 ) ] \D b8 [ \slashed { \U dis8 (
          } {} \D e8 ) ] \D b8 [ \slashed { \U dis8 ( } {} \D e8 ) -. ] \D b8 [
        \D g'8 -. ] _\f | % 78
        \D e4 ( \D f!8 ) -. [ \D d8 -. ] \D c4 -. r8 \U g8 -. _\p \pageBreak | % 79

        \barNumberCheck #80
        \U e8 -. [ \U a8 -. \U g8 -. \U fis8 -. ] \U g4 r8 \D d'8 | % 80
        \D e8 \D g4 \D f!4 \D e16 ^\trill [ \D d16 ] \D e8 [ \D c'8 -. ] _\f | % 81
        \U d,,8 -. r8 \U g,8 -. \U g'8 r8 \U c,4 \U e4 r4 | % 82
        R1 | % 83
        \break r4 r16. \U g32 [ \U a16. \U b32 ] \D c16. [ \D d32 \D e16. \D f32
        ] \D g8 [ \D c8 ] | % 84
        \D b8 ( [ \D a8 ] \D g8 ) [ \D c,8 ] \U b8 ( [ \U a8 ] \D g16. ) [ \D g'32
        \D e16. \D c32 ] | % 85
        \D b16. [ _\fz \D c32 \D d16. \D e32 ] \D f16. [ \D e32 \D f16. \D a32 ]
        \D e16. [ \D g32 \D d16. \D f32 ] \D c16. [ \D g'32 \D e16. \D c32 ]
        \break | % 86
        \D b16. [ _\fz \D c32 \D d16. \D e32 ] \D f16. [ \D e32 \D f16. \D a32 ]
        \D e16. [ \D f32 \D g16. \D a32 ] \D bes16. [ \D a32 \D bes16. \D d32 ]
        | % 87
        \D a16. [ \D c32 \D g16. \D bes32 ] \D f16. [ \D c'32 \D a16. \D f32 ]
        \D e16. [ \D f32 \D g16. \D a32 ] \D bes16. [ \D a32 \D bes16. \D g32 ]
        \break | % 88
        \D f16. [ \D a32 \D e16. \D g32 ] \D d16. [ \D a'32 \D g16. \D f32 ] \D
        e16. [ \D g32 \D d16. \D f32 ] \D c16. [ \D g'32 \D f16. \D e32 ] | % 89

        \barNumberCheck #90
        \D d16. [ \D f32 \D a16. \D g32 ] \D f16. [ \D e32 \D d16. \D c32 ] \U g4
        r8 \D g'8 \break | % 90
        \D e8. ( ^\trill [ \D d32 \D e32 ) ] \D f8 ( -. [ \D d8 ) -. ] \D c8 ( [
        \D e8 ) ] \D d8 -. [ \D e8 -. ] | % 91
        \D cis8. ( ^\trill [ \D b32 \D cis32 ) ] \D d8 [ \D c32 ( \D b32 \D a32
        \D b32 ) ] \U c8 [ \U g32 ( \U fis32 \U e32 \U fis32 ) ] \D g8 [ \D g'8
        ] \pageBreak | % 92
        \D a4 ^\trill \D b4 ^\trill \D c4 ( ^\trill \grace { \U b16 [ } {}
        \grace { \U c16 ) ] } {} \D d8 -. [ \D e8 -. ] | % 93
        \tweak TupletBracket.stencil ##f \tuplet 6/4 {
          \D f16 [ \D d16 \D b16 \D g16 \D b16 \D d16 ] }
        \tweak TupletBracket.stencil ##f \tuplet 6/4 {
          \D f16 [ \D d16 \D b16 \D g16 \D b16 \D d16 ] }
        \D f8 r8 r8 ^\fermata \D e,8 _\p \break | % 94
        \D d4. ( \D e8 ) \D f4 r8 \D a8 -. _\fz | % 95
        \D fis4 ( \D g8 ) [ \D f8 -. ] _\f \D dis4 ( \D e8 ) [ \D d8 -. ] _\fz | % 96
        \D b4 ( \D c8 ) [ \D a'8 -. ] _\fz \D c,4 ( \D d8 ) [ \D b8 -. ] \break
        | % 97
        \D c4 _\f r8 \D c8 \D b8 -. [ \D f'8 -. \D e8 -. \D d8 -. ] | % 98
        \D c8 -. [ \D e8 -. \D g8 -. \D c8 -. ] \D b8 -. [ \D f'8 -. \D e8 -. \D
        d8 -. ] | % 99

        \barNumberCheck #100
        \D c8 [ \D e8 \D g8 \D e8 ] \D d8 ( [ \D a'8 \D g8 \D f8 ) ] \break | % 100
        \D e16 [ \D g16 \D e16 \D g16 ] \D e16 [ \D g16 \D e16 \D c16 ] \D b16 [
        \D c16 \D d16 \D e16 ] \D f16 [ \D a16 \D g16 \D f16 ] | % 101
        \D e8 [ \D c8 \D a8 \D f8 ] \D e8 [ \D c'8 ] \U g,,8 [ \U b8 ] | % 102
        \U c16 [ \U fis16 \U a16 \U b16 ] \D c16 [ \D fis!16 \D a16 \D b16 ] \D
        c8. ^\fermata [ \D a16 ] \D c8 r8 ^\fermata \break | % 103
        \U g,,16 [ \U g'16 \U b16 \U d16 ] \D f!16 [ \D g16 \D b16 \D d16 ] \D f8.
        ^\fermata [ \D d16 ] \D f16 r16 ^\fermata \D g,8 _\p | % 104
        \D e4 -. ^\markup \fontsize #4.088 \bold "la seconda volta più presto" r8
        \D f8 -. \D d4 -. r8 \D e8 -. | % 105
        \D c4 -. r8 \D cis8 -. \D d4 -. r8 \D e8 -. | % 106
        \D f4 -. r8 \D gis8 -. \D a4 -. r4 \pageBreak | % 107
        \grace { \U e,16 ( [ } {} \grace { \U g16 ] } {} \D c4 ) r4 \grace { \U
          d,16 ( [ } {} \grace { \U f16 ] } {} \D b4 ) r4 | % 108
        \U c,2 ( \D es'2 | % 109

        \barNumberCheck #110
        \D c2 \D c'2 ) | % 110
        \D fis,2 ( \D es2 | % 111
        \D c2 \U a!2 ) | % 112
        \D a'2 r2 | % 113
        \U g,2. \U f8 ( [ \U d8 ) ] \break | % 114
        \U c4 _\f r8 \D c'8 \D b8 -. [ \D f'8 -. \D e8 -. \D d8 -. ] | % 115
        \D c8 -. [ \D e8 -. \D g8 -. \D c8 -. ] \D b8 -. [ \D f'8 -. \D e8 -. \D
        d8 -. ] | % 116
        \D c8 -. [ \D e8 -. \D g8 -. \D c8 -. ] \D b16 [ \D g16 \D b16 \D g16 ]
        \D b16 [ \D g16 \D b16 \D g16 ] \break | % 117
        \D c8 [ \D c8 \D c8 \D c8 ] \D b16 [ \D g16 \D b16 \D g16 ] \D b16 [ \D
        g16 \D b16 \D g16 ] | % 118
        \D c8 [ \D c8 \D c8 \D e,,8 ] \D f8. ( ^\trill [ \D e32 \D f32 ) ] \D g8
        ( -. [ \D b,8 ) -. ] \alternative {
          \volta 1 {
            \once \override Score.VoltaBracket.text = \markup "1." \D c8 -. [ \D
            f8 -. ] \D e8 [ \D c'32 ( \D b32 \D a32 \D b32 ) ] \D c4 r8 \D g8 -.
            _\p \break \D e4 -. r8 \U g,8 -. \U e4 -. r8 \D g'8 -. \D e4 -. r4 r2
          }
          \volta 2 {
            \once \override Score.VoltaBracket.text = \markup "2." | % 119

            \barNumberCheck #120
            \D c8 -. [ \D f8 -. ] \D e8 -. [ \D c'32 ( \D b32 \D a32 \D b32 ) ]
            \D c4 -. \D b,4 -. \D g'4 | % 120
            \D c,4 -. \D e4 r4 r4 r8 \bar "|."
          }
        }
      }
      \pageBreak \time 2/2 \key g \major \U g,4. ( ^\markup \fontsize #6.578
      "II." ^\markup \fontsize #4.088 \bold "Poco adagio; cantabile" _\"p dolce"
      \U a8 \D b4 \U a4 \D c4 \D b4 ) \U a8 ( [ \U fis8 ] \U g4 ) \D e'4 ( \D d4
      \D c4 \D b4 ) \U a4 ( \U b8 [ \U g8 ) ] \D d'2 \U g,4. ( \U a8 \D b4 \U a4
      \D c4 \D b4 ) \U a8 ( [ \U fis8 ] \U g4 ) \D e'4 ( \D d4 \break \D c4 \D b4
      ) \U a4 ( \U b8 [ \U g8 ) ] \D d'2 \U a4 ( \D b4 \U a8 [ \U fis8 ] \U d4 )
      \D c'4 ( \D b4 \U a8 [ \U fis8 ] \U d4 ) \D d'4 ( \D c4 \D b4. ) \D b8 \D
      cis4 \D cis8 ( [ \D d8 ) ] \D d2 ^\fermata \D g4. ( _\fz \D fis8 \D fis8 [
      \D e8 ] \D d4 ) \D e4. ( _\fz \D d8 \break \D d8 [ \D c8 ] \D b4 ) \U a4.
      ( _\p \D b16 [ \D c16 ) ] \D d8 ( [ \D e8 \D c8 \D a8 ) ] \U g4 \slashed {
        \U b8 ( } {} \U a8 [ \U g8 ) ] \U g2 \D g'4. ( _\fz \D fis8 \D fis8 [ \D
      e8 ] \D d4 ) \D e4. ( _\fz \D d8 \D d8 [ \D c8 ] \D b4 ) \U a4. ( _\p \D b16
      [ \D c16 ) ] \D d8 ( [ \D e8 \D c8 \D a8 ) ] \U g4 ( \slashed { \U b8 } {}
      \U a8 [ \U g8 ) ] \U g2 \bar "||"
      \break \time 2/2 \U b,16 -. [ ^\markup \fontsize #5.422 "Var. I" _\markup
      \italic "sempre piano" \U d16 -. \U g16 -. \U b16 -. ] \D d16 -. [ \D g16
      -. \D fis16 -. \D e16 -. ] \D d16 -. [ \D g16 -. \D b16 -. \D g16 -. ] \D
      fis16 -. [ \D d,16 -. \D fis'16 -. \D g16 -. ] \D gis16 ( [ \D a16 \D c16
      \D fis,16 ) ] \D a16 ( [ \D g16 \D b16 \D d,16 ) ] \D d16 ( [ \D c16 \D e16
      \D c16 ) ] \U ais16 ( [ \U b16 \U fis16 \U g16 ) ] r16 \D g'16 ( [ \D d'16
      \D c16 ) ] \D fis,16 ( [ \D c'16 \D ais!16 \D b16 ) ] \pageBreak r16 \D e,16
      ( [ \D b'16 \D a16 ) ] \D d,16 ( [ \D a'16 \D fis16 \D g16 ) ] r16 \D c,16
      ( [ \D g'16 \D fis16 ) ] \D a16 ( [ \D g16 \D b16 \D g16 ) ] \D fis16 [ \D
      a16 \D cis16 \D d16 ] \U d,,16 [ \U e16 \U c!16 \U d16 ] \U b16 -. [ \U d16
      -. \U g16 -. \U b16 -. ] \D d16 -. [ \D g16 -. \D fis16 -. \D e16 -. ] \D
      d16 -. [ \D g16 -. \D b16 -. \D g16 -. ] \D fis16 -. [ \D d,16 -. \D fis'16
      -. \D g16 -. ] \D gis16 ( [ \D a16 \D c16 \D fis,16 ) ] \D a16 ( [ \D g16
      \D b16 \D d,16 ) ] \break \D d16 ( [ \D c16 \D e16 \D c16 ) ] \U ais16 ( [
      \U b16 \U fis16 \U g16 ) ] r16 \D g'16 ( [ \D d'16 \D c16 ) ] \D fis,16 (
      [ \D c'16 \D ais!16 \D b16 ) ] r16 \D e,16 ( [ \D b'16 \D a!16 ) ] \D d,16
      ( [ \D a'16 \D fis16 \D g16 ) ] r16 \D c,16 ( [ \D g'16 \D fis16 ) ] \D a16
      ( [ \D g16 \D b16 \D g16 ) ] \D fis16 [ \D a16 \D cis16 \D d16 ] \D d,4 \U
      d,16 ( [ \U fis16 \U d'16 \U fis,16 ) ] \U d16 ( [ \U g16 \U d'16 \U g,16
      ) ] \break \U d16 -. [ \U fis16 -. \U a16 -. \U cis16 -. ] \D d16 -. [ \D
      fis16 -. \D a16 -. \D d16 -. ] \D a16 [ \D fis16 \D d16 \D fis16 ] \D g16
      [ \D d16 \D b16 \D g16 ] \U d16 [ \U fis16 \U a16 \U cis16 ] \D d16 [ \D
      fis16 \D a16 \D d16 ] \D b,16 [ \D d16 \D g16 \D b16 ] \D d,,16 [ \D a''16
      \D fis16 \D d,16 ] \U e16 [ \U g16 \U b16 \U e16 ] \D g16 [ \D b16 \D g16
      \D e16 ] \U a,,16 [ \U cis16 \U e16 \U g16 ] \D cis!16 [ \D e16 \D g16 \D
      g,16 ] \break \U fis16 [ \U d'16 \U a16 \U fis16 ] \U d16 [ \U e16 \U c!16
      \U d16 ] \U b16 [ \U d16 \U g16 \U b16 ] \U d16 [ \U g16 \U b,,16 \U g'16
      ] \U c,16 [ \U g'16 \U e'16 \U g,16 ] \U b,16 [ \U g'16 \U d'16 \U g,16 ]
      \U c,16 [ \U e16 \U g16 \U c16 ] \U e16 [ \U g16 \U b,,16 \U g'16 ] \U a,16
      [ \U c16 \U d16 \U fis16 ] \D g16 [ \D b16 \D d16 \D g16 ] \U c,,16 [ _\p
      \U d16 \U fis16 \U a16 ] \D c16 [ \D fis16 \D g16 \D a16 ] \break \D b,16
      [ \D g'16 \D c,16 \D g'16 ] \U e,16 [ \U g'16 \U cis,,16 \U e'16 ] \U d,16
      [ \U g16 \U b16 \U d16 ] \U d,16 [ \U c'!16 \U fis16 \U c16 ] \D b16 [ \D
      g'16 \D d16 \D b16 ] \U g16 [ \U d16 \U b16 \U d16 ] \tweak
      TupletBracket.stencil ##f \tuplet 6/4 {
        \U g,16 ( [ \U b16 \U d16 \U g16 \U b16 \U d16 ) ] }
      \U g16 [ \U b,16 \U b,16 \U g'16 ] \U c,16 [ \U g'16 \U e'16 \U g,16 ] \U
      b,16 [ \U g'16 \U d'16 \U g,16 ] \U c,16 [ \U e16 \U g16 \U c16 ] \U e16 [
      \U g16 \U b,,16 \U g'16 ] \pageBreak \U a,16 [ \U c16 \U d16 \U fis16 ] \D
      g16 [ \D b16 \D d16 \D g16 ] \U c,,16 [ _\p \U d16 \U fis16 \U a16 ] \D c16
      [ \D fis16 \D g16 \D a16 ] \D b,16 [ \D g'16 \D c,16 \D g'16 ] \U e,16 [
      \U g'16 \U cis,,16 \U e'16 ] \U d,16 [ \U g16 \U b16 \U d16 ] \U d,16 [ \U
      c'!16 \U fis16 \U c16 ] \D b16 [ \D g'16 \D d16 \D b16 ] \U g8 r8 \bar
      "||"
      \break \time 4/4 r8 ^\markup \fontsize #5.422 "Var. II" \U d'8 ( [ _\p \U
      b8 \U fis8 ) ] \U g8 \D g'4 ( \D fis8 ) r8 \D e4 \D d8 ~ \D d8 \D c4 ( \D
      b8 ) r8 \D cis4 ( \D d8 ) \D e8 \D fis4 ( \D g8 ) \D d'8 \D c!4 ( \D b8 ~
      ) \break \D b8 [ \D a8 ] \D g16 ( [ \D fis16 \D e16 \D d16 ) ] r8 \U d8 (
      [ \U b8 \U fis8 ) ] \U g8 \D g'4 ( \D fis8 ) r8 \D e4 \D d8 ~ \D d8 \D c4
      ( \D b8 ) r8 \D cis4 ( \D d8 ) \D e8 \D fis4 ( \D g8 ) \D d'8 \D c!4 ( \D
      b8 ~ ) \break \D b8 [ \D a8 ] \D g16 ( [ \D fis16 \D e16 \D d16 ) ] r8 \D
      d4 ( \D cis8 ) \D d8 ( [ \D fis8 \D a8 \D fis8 ) ] \D d8 \D e4 \D d8 ~ \D
      d8 [ \D c!8 ( \D b8 \D a8 ) ] \U gis16 ( [ \U a16 \U b16 \U a16 ) ] \D c16
      ( [ \D b16 \D e16 \D d16 ) ] \break \D cis16 ( [ \D d16 \D e16 \D d16 ) ]
      \D g!16 ( [ \D fis16 \D a16 \D g16 ) ] \D b4 \D a16 ( [ \D g16 \D fis16 \D
      g16 ) ] \D g4 ( \D fis4 ) \slashed { \U fis8 ( } {} \D e16 ) ( [ \D dis16
      \D e16 \D g16 ) ] \D cis,8 [ \D d8 ~ ] \D d8 \D c!4 ( \D b8 ) \slashed {
        \U d8 ( } {} \D c16 ) ( [ \D b16 \D c16 \D e16 ) ] \U ais,8 [ \U b8 ~ ]
      \pageBreak \D b8 \U a!4 ( \U g8 ) \D e'16 ( [ \D dis16 \D e16 \D dis16 ]
      \D e8 [ \D d16 \D c16 ) ] \D b8 ( [ \D a8 \D c8 \D e8 ) ] \U g,4 ( \U fis4
      ) \U g4 r4 \slashed { \U fis'8 ( } {} \D e16 ) ( [ \D dis16 \D e16 \D g16
      ) ] \D cis,8 [ \D d8 ~ ] \break \D d8 \D c!4 ( \D b8 ) \slashed { \U d8 (
        } {} \D c16 ) ( [ \D b16 \D c16 \D e16 ) ] \U ais,8 [ \U b8 ~ ] \D b8 \U
      a!4 ( \U g8 ) \D e'16 ( [ \D dis16 \D e16 \D dis16 ] \D e8 [ \D d16 \D c16
      ) ] \D b8 ( [ \D a8 \D c8 \D e8 ) ] \U g,4 ( \U fis4 ) \U g4 r4 \bar "||"
      \break \time 2/2 r8 ^\markup \fontsize #5.422 "Var. III" \U e8 ( [ _\p \U
      b8 \U cis8 ) ] \U d8 \U g4 \U fis8 \U e8 \U a4 \U g8 \U c,4 ( \U b4 ) \U
      gis'8 ( [ \U a8 \U fis8 \U g8 ) ] \U e8 ( [ \U fis8 \U dis8 \U e8 ) ] \U c8
      \U cis4 \U a8 \U d!2 r2 \break r8 \D g'4 \D fis8 r8 \D a4 \D g8 \D fis8 \D
      e'4 \D d4 \D c!4 \D b8 ~ \D b8 \D a4 \D g8 ~ \D g16 ( [ \D fis16 \D g16 \D
      fis16 ) ] \D g8 [ \voiceOne \D g,8 ] \U d'2 \oneVoice r2 \pageBreak R1 | % 69

      \barNumberCheck #70
      R1 | % 70
      R1 | % 71
      r2 \D b!8 ( [ \D c8 \D cis8 \D d8 ~ ) ] \break \D d8 \D c!4 \D b8 \D c8 (
      [ \D b8 \D bes8 \D a8 ) ] \U g8 -. [ \U g8 ( \U fis8 \U f8 ) ] \U e8 ( [
      \U g8 \U fis8 \U a8 ) ] \D g8 ( [ \D b8 \D c8 \D e8 ) ] \U g,4 ( \U fis4 )
      \U g4 r4 \D b8 ( [ \D c8 \D cis8 ) \D d8 ~ ] \break \D d8 \D c!4 \D b8 \D
      c8 ( [ \D b8 \D bes8 \D a8 ) ] \U g8 -. [ \U g8 ( \U fis8 \U f8 ) ] \U e8
      ( [ \U g8 \U fis8 \U a8 ) ] \D g8 ( [ \D b8 \D c8 \D e8 ) ] \U g,4 ( \U
      fis4 ) \U g4 r4 \bar "||"
      \break \time 2/2 \U g4. ( ^\markup \fontsize #5.422 "Var. IV" _\p \U a8 )
      \D b4 ( \U a4 \D c4 \D b4 ) \U a8 ( [ \U fis8 ] \U g4 ) \D e'4 ( \D d4 \D
      c4 \D b4 ) \U a4 ( \U b8 [ \U g8 ) ] \D d'2 \D g4. ( _\p \D a8 \D b4 \D a4
      \D c4 \D b4 ) \D a8 ( [ \D fis8 ] \D g4 ) \D e'4 ( \D d4 \pageBreak \D c4
      \D b4 ) \D a4 ( \D b8 [ \D g8 ) ] \D d'2 \D a4 ( \D b4 \D a8 [ \D fis8 ]
      \D d4 ) \D c'4 ( \D b4 \D a8 [ \D fis8 ] \D d4 ) \D d'4 ( \D c4 \D b4. \D
      b8 ) \D cis4 \D cis8 ( [ \D d8 ) ] \break \D d2 \D g4. ( \D fis8 \D fis8 [
      \D e8 ] \D d4 ) \D e4. ( \D d8 \D d8 [ \D c!8 ] \D b4 ) \D a4. ( _\fz \D b16
      [ \D c16 ) ] \D d8 ( [ \D e8 \D c8 \D a8 ) ] \D g4 ( \slashed { \U b8 \=2(
        } {} \D a8. \=2) [ \D g16 ) ] \break \D g8 ( [ \D a16 \D b16 ] \D c16 [
      \D d16 \D e16 \D fis16 ) ] \D g4. ( \D fis8 \D fis8 [ \D e8 ] \D d4 ) \D e4.
      ( \D d8 \D d8 [ \D c8 ] \D b4 ) \D a4. ( _\fz \D b16 [ \D c16 ) ] \D d8 (
      [ \D e8 \D c8 \D a8 ) ] \D g4 ( \slashed { \U b8 \=2( } {} \D a8. \=2) [
      \D g16 ) ] \break \D g2 ~ \D g4. \D f8 ( _\pp \D e2 ) \D d2 ~ \D d8 \D c4
      \D b4 \U a8 ( -. [ \U a8 -. \U a8 ) -. ] \after 2 _\> \after 2 \! a1
      ^\fermata _\< <>\! b1 ^\fermata _\pp \bar "|."
      \pageBreak \time 3/4 \key c \major \D c4 ^\markup \fontsize #6.578
      "III. Menuetto" ^\markup \fontsize #4.088 \bold Allegro _\f \D b4 ( \D c4
      ) \D e4 \U g,2 ( \D c4 ) \U d,2 ( \U a'4 ) \U g,4. \U a'8 ( [ \U g8 \U f8
      ) ] \U f4 ( \U e4 ) \D c'4 \D b4 ( \D c4 ) \D e4 \U f,4 ( \U e4 ) \D a8 (
      [ \D c8 ) ] \D e4 ( \D d4 ) \D g4 -. \D fis4 ( \D g4 \D a4 ) \break \D gis4
      ( \D a4 ) \D c8 ( [ \D a8 ) ] \D g!2 \D a8 ( [ \D fis8 ) ] \D g4 r4 \D fis16
      ( [ \D g8. ) ] \D cis,16 ( [ \D d8. ) ] \U ais16 ( [ \U b8. ) ] \U fis16 (
      [ \U g8. ) ] \U d2 \U g4 \U a4 \D a8 ( [ \D b8 \D c8 \D d8 ) ] \D c4 ( \D
      b4 ) \D b'4 -. \D g4 -. \D d4 -. \D b4 -. \break \U g2 \D d'8 ( [ \D b8 )
      ] \slashed { \U b8 ( } {} \U a4 ) \U a8 ( [ \U g8 \U a8 \U b8 ) ] \U g4 r4
    }
    \repeat volta 2 {
      \D d'4 _\f \D cis4 ( \D d4 ) \D f!4 \D c!4 ( \D b4 ) \D g'4 ~ \D g4 \D es4
      \D f4 ~ \D f4 \D d4 \D es4 ~ \D es4 \D d4 \D c4 ~ \D c4 \D b4 \U g4 _\p \U
      fis4 ( \U g4 ) \U d4 \break \U es4 ( \U d4 ) \U g4 \U fis4 ( \U g4 ) \U d4
      \U es4 ( \U d4 ) \U f!4 \U e!4 ( \U f4 ) r4 r4 r4 \D c'4 _\f \D b4 ( \D c4
      ) \D e4 \U g,2 ( \D c4 ) \U d,2 ( \U a'4 ) \U g,4. \U a'8 ( [ \U g8 \U f8
      ) ] \U f4 ( \U e4 ) r4 \break r4 r4 \D c'4 ~ \D c4 \D b4 r4 r4 r4 \D d4 ~
      \D d4 \D cis4 \D f4 \D e4 ( \D f4 \D a4 ) \D bes4 ( \D a4 \D f4 ) \D a4 (
      \D g4 ) \D c4 \D b!4 ( \D c4 \D d4 ) \D cis4 ( \D d4 ) \D f8 ( [ \D d8 ) ]
      \D c!2 \D d8 ( [ \D b8 ) ] \pageBreak \D c4 r4 \D b16 ( [ \D c8. ) ] \D
      fis,16 ( [ \D g8. ) ] \D dis16 ( [ \D e8. ) ] \D b16 ( [ \D c8. ) ] \U g2
      \D c4 \D d4 \D d8 ( [ \D e8 \D f8 \D g8 ) ] \D f4 ( \D e4 ) \D e'4 -. \D c4
      -. \D g4 -. \D e4 -. \D c2 \D g'8 ( [ \D e8 ) ] \slashed { \U e8 ( } {} \D
      d4 ) \D d8 ( [ \D c8 \D d8 \D e8 ) ] \D c4 r4 ^\fermata }
    <>^\markup Fine \break \repeat volta 2 {
      \time 3/4 \U e,4 ^\markup \fontsize #5.422 Trio _\p \D c'2 ( \U a4 ) \U f2
      ( \U d4 ) \U b4 \U b8 ( [ \U c8 \U d8 \U e8 ) ] \U c4 ( \U a4 ) \U e'4 \D
      c'2 ( \U a4 ) \U f2 ( \U e4 ) \U dis4 \U dis8 ( [ \U e8 \U fis8 \U dis8 )
      ] \U e4 r4 }
    \repeat volta 2 {
      \U e4 \D c'2 ( \U a4 ) \U f2 ( \U d4 ) \break \U bes4 \U a8 ( [ \U cis8 \U
      e8 \U g8 ) ] \break \U f4 ( \U d4 ) \U d4 _\f \D d'2 ( \D b!4 ) \U gis2 (
      \U e4 ) \U a2 ( \U e4 ) \U c4 ( \U b4 \U a4 ) \U gis4 ( \U b4 \U dis4 ) \U
      e4 ( \U gis4 \D b4 ) \D e2. ~ \D e2 ^\fermata \U e,4 _\pp \D cis'2 ( \U a4
      ) \U e4 r4 \U e4 \break \D d'2 ( \D b4 ) \U e,4 r4 \U e4 ( \D e'4 \D cis4
      \U a4 \D fis'4 \D d4 \D b4 ) \U a2. ( \U gis4 ) r4 \U e4 \D cis'2 ( \U a4
      ) \U e4 r4 \U e4 \D d'2 ( \D b4 ) \U e,4 r4 \U e4 \D e'4 ( \D cis4 \U a4 )
      \pageBreak \D fis'4 ( \D d4 \D b4 ) \U a2 \slashed { \U cis8 ( } {} \D b4
      ) \U a4 r4 \U e4 _\p \D c'!2 ( \U a4 ) \U f!2 ( \U d4 ) \U b4 \U b8 ( [ \U
      c8 \U d8 \U e8 ) ] \U c4 ( \U a4 ) \U e'4 \D c'2 ( \U a4 ) \U f2 \U a,4 (
      \U c4 \U d4 \U b4 ) \U a4 r4 }
    <>^\markup "Menuetto D.C. " \pageBreak \time 2/2 \key es \major \D es'4 -.
    ^\markup \fontsize #6.578 "IV. Finale" ^\markup \fontsize #4.088 \bold
    Presto _\f \D c'4 \D g'4 r4 \D d,4 -. \D b'4 \D as'4 r4 \D es,4 \D c'4 \D g'4
    r4 r4 \D c4 _\p \D b2 ( \D c4 ) \D d4 \D es2 ( \D d4 ) -. r4 \D c4 _\f r4 \D
    e,,4 \D c'4 \D bes'!4 r4 \D f,4 \D c'4 \D as'!4 r4 r4 \D f4 _\p \D e2 ( \D f4
    ) \D g4 \break \D as2 ( \D g4 ) \D c,4 \D f2 ( \D es4 ) \D c4 \D des2 ( \D f4
    \D as4 ) \D c,2 ( \D b2 ) \D es,4 -. _\f \D c'4 \D g'4 r4 \D d,4 -. \D b'4
    \D as'4 r4 \D es,4 -. \D c'4 \D g'4 r4 r8 \D g8 [ \D es8 \D c8 ] \break
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D b8 [ \D as'8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f8 [ \D es8 \D d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D c8 [ \D g'8 \D f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D d8 \D c8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D b8 [ \D as'8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f8 [ \D es8 \D d8 ] }
    \D c8 ( [ \D g'8 \D c8 \D bes!8 ) ] \D bes8 ( [ \D as8 ) \D as8 ( \D g8 ) ]
    \D g8 ( [ \D f8 ) \D f8 ( \D es8 ) ] \D es8 ( [ \D d8 ) ] \D d2 \D es8 ( [
    \D c8 ) ] \break \D d,4 _\f \D b'4 \D g'4 r4 \D es,4 \D c'4 \D g'4 r4 \D d,4
    \D b'4 \D g'4 r4 \D es,4 \D c'4 \D g'4 r4 \D d,4 \D b'4 \D g'4 r4 r2 r2 r4
    \D es4 \pageBreak \D d2 ( \D es4 \D f4 ) \D g2 ( \D f2 \D es2 \D e2 ) \D f2
    ( \D g4 \D as4 ) \D bes2 ( _\fz \D as4 \D g4 ) \voiceOne \D f2 ( \oneVoice
    \D g4 \D es!4 ) \D es2 ( \D d4 \D f4 ) _\p \D e2 ( \D f4 \D g4 ) \D as2 ( \D
    g2 ) \break \D f2 ( \D g4 \D as4 ) \D bes2 ( \D as4 ) \D c4 _\fz \D d,2 ( \D
    es4 ) \D bes'4 \D f2 ( \D g4 ) r4 r2 r4 \D bes4 \D f2 ( \D g4 ) r4 \break r2
    r4 \D es4 \D d2 ( \D es4 \D f4 ) \D g2 ( \D f2 ) \D es2 ( \D des2 ) \D c2 (
    \D bes2 ) \U as2 ( \D bes4 \D ces4 ) \break bes1 ~ \D bes2. \U as4 ~ \U as4
    \U g2 ( \U f4 ) \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D bes'8 [ _\f \D g8 \D f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D d8 \D c8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U as8 \U g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U f8 [ \U es8 \U d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U es8 ( [ \U d8 \U es8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g8 ( [ \U fis8 \U g8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 ( [ \U a8 \U bes8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 ( [ \D d8 \D es8 ) ] }
    \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f8 [ \D b8 \D d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D c8 [ \D bes8 \D as!8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D f8 \D e8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f8 [ \D g8 \D es8 ] }
    \D d4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 ( [ \U a8 \U bes8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D c8 ( [ \D bes8 \D c8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D d8 ( [ \D c8 \D d8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D c8 ( \D b8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U c8 ) [ \U a8 \U f8 -. ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U es8 -. [ \U f8 -. \U a8 -. ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D c8 -. [ \D d8 -. \D es8 -. ] }
    \pageBreak \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f8 -. [ \D d8 ( \D cis8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D d8 ) [ \D bes8 -. \D a8 -. ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D bes8 -. [ \D c8 -. \D d8 -. ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 -. [ \D e8 -. \D f8 -. ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 -. [ \D es!8 ( \D d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 ) [ \D f8 -. \D g8 -. ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as8 -. [ \D f8 ( \D e8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f8 ) [ \D g8 -. \D as8 -. ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 ( [ \D as8 \D g8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D c8 ( [ \D d8 \D c8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f,8 ( [ \D g8 \D a8 ) ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D bes8 [ \D bes,8 \D d8 ] }
    \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D f8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as8 [ \D f8 \D es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D d8 [ \D es8 \D f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D fis8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D c,8 [ \D d8 \D e8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f!8 [ \D g8 \D as8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D bes,8 [ \D c8 \D d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D f8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as8 [ \D as8 \D as8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D g8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as8 [ \D as8 \D as8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D g8 \D g8 ] }
    \break \D c4 r4 \U f,,4 \U d'4 r4 \U es,4 \U es'4 r4 r2 \tweak
    TupletBracket.stencil ##f \tuplet 3/2 {
      \D f8 [ \D g8 \D as8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D f8 \D es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D d8 [ \D c8 \D bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as8 [ \U g8 \U f8 ] }
    \U es4 r4 r2 \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D f'8 [ \D g8 \D as8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D f8 \D es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D d8 [ \D c8 \D bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as8 [ \U g8 \U f8 ] }
    \U es4 r4 \D bes'4 \D g'4 r4 \D c,4 \D as'4 r4 \D d,,4 \D bes'4 \D as'4 r4
    \break \D es,4 \D bes'4 \D g'4 r4 \D as,4 \D c4 \D f4 r4 \U bes,,4 \U g'4 \U
    es'4 r4 \U bes,4 \U f'4 \U d'4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2
    {
      \U es,8 [ \U d8 \U es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g8 [ \U fis8 \U g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U a8 \U bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g8 [ \U fis8 \U g8 ] }
    \pageBreak \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as!8 [ \D c8 \D bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as8 [ \U g8 \U f!8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U es8 [ \U d8 \U f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as8 [ \U f8 \U d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U es8 [ _\p \U d8 \U es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g8 [ \U fis8 \U g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U a8 \U bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g8 [ \U fis8 \U g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as!8 [ \D ces8 \D bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as8 [ \U ges8 \U f!8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U es8 [ \U d8 \U f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as8 [ \U f8 \U d8 ] }
    \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U es8 [ \U d8 \U es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as8 [ \U f8 \U d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U es8 [ \U d8 \U es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as8 [ \U f8 \U d8 ] }
    \U es4 -. r4 \U g4 -. r4 \alternative {
      \volta 1 {
        \once \override Score.VoltaBracket.text = \markup "1." \U es4 -. r4 r2 }
      \volta 2 {
        \once \override Score.VoltaBracket.text = \markup "2." \U es4 -. r4 r4
        \D es'4 _\f }
    }
  }
  \D d2 ( \D es4 \D f4 ) \D g4 r4 r4 \D f4 \D es2 ( \D f4 \D g4 ) \break \D as2
  ( \D c2 ) \D bes2. ( \D as8 [ \D g8 ) ] \D f2 ( \D ges4 \D es4 ) \D es2 ( \D d4
  \D bes4 ) _\p \U a2 ( \D bes4 ) \D f'4 \D ges2 ( \D f4 ) \D bes,4 \U a2 ( \D
  bes4 ) \D f'4 \D ges2 ( \D f4 ) r4 \break R1 | % 84
  R1 | % 85
  R1 | % 86
  R1 | % 87
  \break r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ _\f \D bes8 \D as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D ges8 [ \D f8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \U as4 ( \D des4 \D c4 \D ges'4 ) r4 \D bes,4 ( \U a4 \D es'4 ) \U f,4 ( \D
  des'4 \U f,4 ) \D f'4 \D as!2 ( \D g4 ) \D f8 ( -. [ \D d!8 ) -. ] \pageBreak
  \U g,4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g'8 [ \D f8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D g8 \D as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D as8 \D bes8 ] }
  \D c4 \D c,8 ( [ \D c'8 ) ] \D bes4 \D bes,8 ( [ \D bes'8 ) ] \D as4 \tweak
  TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D g8 \D as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D as8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D bes8 \D c8 ] }
  \D f,4 \D bes2 \D as4 \break \D g4 \tweak TupletBracket.stencil ##f \tuplet 3/2
  {
    \D es8 [ \D d8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D es8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D f8 \D g8 ] }
  \D as2 \D des2 \D c4 r4 r2 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D es8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D des8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D as8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D es8 \D des!8 ] }
  \break \D c4 r4 r2 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des'8 [ \D es8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D des8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D as8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D es8 \D des!8 ] }
  \D c4 r4 r2 \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D des8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as8 [ \U g8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D c8 \D des8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D des8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D bes8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U as8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 [ \U g8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U f8 \U es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d!8 [ \U es8 \U f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U es8 [ \U d8 \U c8 ] }
  \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 ( [ \U a8 \U bes8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d8 ( [ \U cis8 \U d8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 [ \U e8 \U f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as!8 [ \U g8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U fis8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U a8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D d8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis!8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g,8 [ \U fis8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U b8 [ \U a8 \U b8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D d8 [ \D cis8 \D d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f!8 [ \D e8 \D f8 ] }
  \pageBreak \D es!4 r4 r2 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D f8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D es8 \D d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D b8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D d8 [ \D c8 \D d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D f8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D es8 \D d8 ] }
  \D c4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c'8 ( [ \D d8 \D c8 ) ] }
  \break \D b4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 ( [ \D c8 \D bes8 ) ] }
  \D as!4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 ( [ \D as8 \D g8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 ( [ \D g8 \D f8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D e8 ( [ \D f8 \D g8 ) ] }
  \D f4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 ( [ \D c8 \D bes8 ) ] }
  \D a4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 ( [ \D bes8 \D as8 ) ] }
  \D g4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 ( [ \D g8 \D f8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 ( [ \D f8 \D es8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D d8 ( [ \D es8 \D f8 ) ] }
  \D es4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 ( [ \D as8 \D g8 ) ] }
  \break \D f4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 ( [ \D f8 \D es8 ) ] }
  \D d4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 ( [ \D d8 \D c8 ) ] }
  \D b4 -. \D d4 -. \D es4 -. \D f4 -. \D es,4 -. \D c'4 \D g'4 r4 \D d,4 -. \D
  b'4 \D as'4 r4 \D es,4 -. \D c'4 \D g'4 r4 r4 \D c4 -. _\p \D b2 ( \D c4 ) \D
  d4 -. | % 121
  \D es2 ( \D d4 ) -. r4 \break | % 122
  \D c4 -. _\f r4 \D e,,4 -. \D c'4 \D bes'!4 r4 | % 123
  \D f,4 -. \D c'4 \D as'4 r4 r4 \D f4 _\p | % 124
  \D e2 ( \D f4 ) \D g4 | % 125
  \D as2 ( \D g4 ) \D c,4 -. | % 126
  \D f2 ( \D es4 ) \D c4 -. | % 127
  \D des2 ( \D f4 \D as4 ) | % 128
  \D c,2 ( \D b2 ) | % 129

  \barNumberCheck #130
  r2 r4 \D c4 _\p \pageBreak | % 130
  \D des2 ( \D f4 \D as4 ) | % 131
  \D c,2 ( \D b2 ) | % 132
  r2 r4 \D c4 _\pp | % 133
  \D des2 ( \D f4 \D as4 ) | % 134
  \D bes,2 ( \D es4 \D ges4 ) | % 135
  \U as,4 ( \D des8 [ \D f8 ) ] \U ges,4 ( \D c8 [ \D es8 ) ] | % 136
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 ( [ _\f \D c8 \D des8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 ( [ \D e8 \D f8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 ( [ \D g!8 \D as8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 ( [ \D e8 \D f8 ) ] }
  \break | % 137
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D ges8 -. [ \D bes8 -. \D as8 -. ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D ges8 [ \D f8 \D es!8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D ges8 [ \D es8 \D c8 ] }
  | % 138
  \D des4 r4 r4 \D as'4 | % 139

  \barNumberCheck #140
  \grace { \U g!32 ( [ } {} \grace { \U as32 } {} \grace { \U bes32 ] } {} \D as2
  ) \D d,!2 \break | % 140
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 ( [ \D d8 \D es8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D ges8 ( [ \D f8 \D ges8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 ( [ \D a8 \D bes8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D ges8 ( [ \D f8 \D ges8 ) ] }
  | % 141
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as!8 -. [ _\fz \D ces8 -. \D bes8 -. ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D ges8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D d8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D f8 \D d8 ] }
  | % 142
  \D es4 r4 r4 \D bes'4 \break | % 143
  \grace { \U a32 ( [ } {} \grace { \U bes32 } {} \grace { \U c32 ] } {} \D bes2
  ) \D e,2 | % 144
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 ( [ \D e8 \D f8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 ( [ \D g8 \D as8 ) ] }
  \D c4 r4 | % 145
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c,8 ( [ \D b8 \D c8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g'8 ( [ \D fis8 \D g8 ) ] }
  \D c4 r4 \pageBreak | % 146
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c,8 ( [ \D b8 \D c8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g'8 ( [ \D fis8 \D g8 ) ] }
  \D c4 r4 | % 147
  \D f,!4 \D d'4 r4 \D es,4 \D c'4 r4 | % 148
  \D d,4 \D b'4 r4 \D es,4 \D c'4 r4 \break | % 149

  \barNumberCheck #150
  \D d,4 \D b'4 r4 \D es,4 \D c'4 r4 | % 150
  \D d,4 -. \D b'4 r4 r4 ^\fermata \bar "||"
  \key c \major \D c,4 _\p | % 151
  \D b2 ( \D c4 ) \D d4 | % 152
  \D e2 ( \D d4 ) r4 | % 153
  r2 r4 \D d4 | % 154
  \D cis2 ( \D d4 ) \D e4 \break | % 155
  \D f2 ( \D e4 ) r4 | % 156
  r2 r4 \D a4 _\f | % 157
  \D gis2 ( \D a4 ) \D f4 | % 158
  \D g!2 ( \D f4 ) \D a4 | % 159

  \barNumberCheck #160
  \D b,2 ( \D c4 ) \D a'4 | % 160
  \D b,2 ( \D c4 ) \D c'4 | % 161
  \D b2 ( \D c4 ) \D g4 | % 162
  \D d2 ( \D e4 ) r4 \break | % 163
  r2 r4 \D g4 | % 164
  \D d2 ( \D e4 ) r4 | % 165
  r2 r4 \D c'4 | % 166
  \D b2 ( \D c4 \D d4 ) | % 167
  \D e2 ( \D d2 | % 168
  \D c2 \D bes2 ) | % 169

  \barNumberCheck #170
  \D a2 ( \D g2 ) \pageBreak | % 170
  \D f2. ( \D g8 [ \D as8 ) ] | % 171
  g1 ~ | % 172
  \D g2. \D f4 ~ | % 173
  \D f4 \D e2 ( \D d4 ) | % 174
  \D c4 r4 r2 \break | % 175
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D d8 [ \D e8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D e8 [ \D d8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U b8 [ \U a8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 [ \U e8 \U d8 ] }
  | % 176
  \U c4 r4 r2 | % 177
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D d''8 [ \D e8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D e8 [ \D d8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D b8 [ \D a8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D e8 \D d8 ] }
  | % 178
  \D c4 r4 \D bes4 \D e4 r4 \break | % 179

  \barNumberCheck #180
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D f8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D f8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D fis8 [ \D fis8 \D fis8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D fis8 [ \D fis8 \D fis8 ] }
  | % 180
  \D g4 r4 \U d,4 \U b'4 r4 | % 181
  \U e,4 \U c'4 r4 r4 \D c'4 | % 182
  \D b2 ( \D c4 \D d4 ) \break | % 183
  \D e4 r4 r4 \D c,4 | % 184
  \D b2 ( \D c4 \D d4 ) | % 185
  \D e4 -. r4 \D e4 -. \D g4 r4 | % 186
  \D c,4 -. \D e4 r4 \U e,4. \U c'4. \U e,8 \U c'8 | % 187
  \U e,4 \U c'4 d4\rest d2\rest \bar "|."
}

PartPOneVoiceTwo = \relative c'' {
  \repeat volta 2 {
    \repeat volta 2 {
      \repeat volta 2 {
        \clef "treble" \time 4/4 \key c \major \partial 8 s8*33 \break s1*3
        \break s1*2 \break s1*2 \pageBreak s1*4 \break | % 15
        \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
        ##t c8 ^\turn s4*9 \break s1*2 \break s1*2 | % 22
        \D g8 [ \D fis16 \D e16 ] \D fis8 [ \D gis8 ] \D a4 s4 \break s1*3
        \pageBreak s1*2 \break s1*2 \break s1*3 \break s1*4 \break s1*2
        \pageBreak s1*2 \break s1*2 \alternative {
          \volta 1 {
            \once \override Score.VoltaBracket.text = \markup "1." s1 \break
            s8*15 }
          \volta 2 {
            \once \override Score.VoltaBracket.text = \markup "2." }
        }
      }
      \repeat volta 2 {
        \break s8*9 \break s1*3 \pageBreak s1*4 \break s1*4 \break s1*3 \break
        s1*2 \break s1*3 \pageBreak s1*2 \break s1*2 \break s1*2 \break s1*3
        \break s1*4 \pageBreak s1*4 \break s1*3 \break s1*2 \break s1*2 \break
        s1*2 \pageBreak s1*2 \break s1*2 | % 96
        \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
        ##t c8 ^\turn s4 \break s1*3 \break s1*3 \break s1*4 \pageBreak s1*7
        \break s1*3 \break s1*2 \alternative {
          \volta 1 {
            \once \override Score.VoltaBracket.text = \markup "1." s1 \break
            s1*2 }
          \volta 2 {
            \once \override Score.VoltaBracket.text = \markup "2." \bar "|."
          }
        }
      }
      \pageBreak \time 2/2 \key g \major s1 \hideNote r2 \hideNote r8 \tweak
      Stem.transparent ##t \tweak transparent ##t a8 ^\turn s4*13 \break
      \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
      ##t a8 ^\turn s4*25 \break s2*13 \bar "||"
      \break \time 2/2 s2*5 \pageBreak s1*3 \break s1*3 \break s1*3 \break s1*3
      \break s1*3 \pageBreak s2*5 \bar "||"
      \break \time 4/4 s2*7 \break s1*4 \break s1*3 \break s1*3 \pageBreak s1*3
      \break s2*7 \bar "||"
      \break \time 2/2 s2*9 \break s1*2 \hideNote r2. \hideNote r8 \U cis8 \D
      fis,2 \hideNote r2 \pageBreak s1*4 \break s1*4 \break s2*7 \bar "||"
      \break \time 2/2 s2*5 \hideNote r2 \hideNote r8 \tweak Stem.transparent
      ##t \tweak transparent ##t a8 ^\turn s4*13 \pageBreak \hideNote r2
      \hideNote r8 \tweak Stem.transparent ##t \tweak transparent ##t a'8 ^\turn
      s4*17 \break s1*4 \break s1*4 \break s1*5 \bar "|."
      \pageBreak \time 3/4 \key c \major s2*13 \break s1*6 \break s1*2 }
    \repeat volta 2 {
      s2*11 \break s2*15 \break s2*15 \pageBreak s2*13 }
    \break \repeat volta 2 {
      \time 3/4 s1*6 }
    \repeat volta 2 {
      s4*7 \break s2. \break s4*33 \break s4*33 \pageBreak s1*8 }
    s4 \pageBreak \time 2/2 \key es \major s1*7 \break s1*6 \break s1*4 \break
    s1*4 \pageBreak s1*5 \tweak Stem.transparent ##t \tweak transparent ##t e4
    \tweak Stem.transparent ##t \tweak transparent ##t f4 ^\turn ^\markup " ♮"
    \hideNote r2 s1*3 \break s1*6 \break s1*6 \break s1*5 \break s1*3 \pageBreak
    s1*3 \break s1*3 \break s1*4 \break s1*3 \break s1*3 \pageBreak s1*3 \break
    s1*2 \alternative {
      \volta 1 {
        \once \override Score.VoltaBracket.text = \markup "1." s1 }
      \volta 2 {
        \once \override Score.VoltaBracket.text = \markup "2." }
    }
  }
  s1*3 \break s1*8 \break s1*4 \break s1*5 \pageBreak s1*4 \break s1*4 \break
  s1*3 \break s1*3 \break s1*3 \pageBreak s1*3 \break s1*4 \break s1*6 \break
  s1*8 \pageBreak s1*7 \break s1*3 \break s1*3 \break s1*3 \pageBreak s1*3
  \break s4*7 \bar "||"
  \key c \major s4*17 \break s1*8 \break s1*7 \pageBreak s1*5 \break s1*4 \break
  s1*4 \break s1*5 \bar "|."
}

PartPTwoVoiceOne = \relative d'' {
  \repeat volta 2 {
    \repeat volta 2 {
      \repeat volta 2 {
        \clef "treble" \time 4/4 \key c \major \partial 8 \oneVoice \D d8 _\f \U
        g,4 ( \U a8 ) -. [ \U <g, f'>8 -. ] \U <g e'>4 -. r8 \U g8 -. _\p | % 1
        \U c8 -. [ \U e8 -. \U d8 -. \U c8 -. ] \U b4 r8 \D b'8 | % 2
        \D c8 ( [ \D bes8 \D a8 \D b8 ) ] \D c4 r8 \U c,8 -. _\f | % 3
        \U c8 -. r8 \U <g f'>8 -. r8 \U <g e'>4 r4 \break | % 4
        r4 r16. \U g32 [ \U a16. \U b32 ] \U c16. [ \U d32 \U e16. \U f32 ] \U g8
        [ \U g8 ] | % 5
        \U e4 ( \U f8 ) -. [ \U d8 -. ] \U c4 -. r8 \D c'8 ~ | % 6
        \D c8 [ \D f8 ] \D e8 r8 r8 \U c,4 \U <e c'>8 \break | % 7
        \U <d b'>4. _\fz \U d8 -. \U e8 -. [ \U f8 -. \U g8 -. \U <e c'>8 -. ] | % 8
        \U <d b'>4. _\fz \U d8 -. \U e8 -. [ \U f8 -. \U g8 -. \U <e c'>8 -. ]
        \break | % 9

        \barNumberCheck #10
        \U <d b'>4. _\fz \U f8 -. \U g8 -. [ \U f8 -. ] \D e16. [ \D g'32 \D f16.
        \D e32 ] | % 10
        \D d16. [ \D a'32 \D g16. \D f32 ] \D e16. [ \D g32 \D f16. \D e32 ] \D
        d16. [ \D a'32 \D g16. \D f32 ] \D e16. [ \D g32 \D f16. \D e32 ]
        \pageBreak | % 11
        \D d16. [ \D g32 \D e16. \D g32 ] \D d16. [ \D g32 \D e16. \D g32 ] \D d4
        r4 | % 12
        r4 r8 \D fis8 \D g4 ( \D a8 ) -. [ \D fis8 -. ] | % 13
        \D g8 ( [ \D f!8 \D e8 \D fis8 ) ] \D g8 ( [ \D d8 \D g8 \D fis8 ) ] | % 14
        \D b,8 ( [ \D cis16 \D dis16 ] \D e8 ) [ \D d8 ] \U g,8 [ \U a16 ( \U b16
        ] \U c8 ) [ \U g8 ] \break | % 15
        \U g2 \U a4 \D c8 [ \D a8 ~ ] | % 16
        \U a8 [ \U d,8 ( \U g8 ) \U d'8 ] \D cis4 ( \D e8 ) [ \D cis8 ] | % 17
        \D d4 r8 \D b'8 -. \D gis8. ( ^\trill [ \D fis32 \D gis32 ) ] \D a8 ( -.
        [ \D fis8 ) -. ] \break | % 18
        \D g!8. ( [ \D a32 \D g32 ) ] \D fis8 [ \D d8 ~ ] \D d16 [ \D f16 \D e16
        \D d16 ] \D c8 [ \D c8 ( ] | % 19

        \barNumberCheck #20
        \D b8 [ \D bes8 ) ] \D a16. [ \D d32 \D d16. \D d32 ] \D d16. [ \D d32
        \D d16. \D d32 ] \D d16. [ \D d32 \D d16. \D d32 ] \break | % 20
        \D d16. [ \D d32 \D d16. \D d32 ] \D d16. [ \D d32 \D d16. \D d32 ] \D d16.
        [ \D d32 \D d16. \D d32 ] \D d8 -. [ \D d8 -. ] | % 21
        \U <d, d'>4 _\ff \U <d c'>8 [ \U <d c'>8 ] \U <d c'>8 r8 r8 \U e8 _\p | % 22
        \U c4 ( \U d8 ) [ \U b8 ] \U a8 [ \U e'8 \U a8 \U b8 -. ] \break | % 23
        \U a4. \U g8 -. _\fz \U fis4. \U e8 -. _\fz | % 24
        \U d4. \U g,8 _\fz \U b4 ( \U c8 ) [ \U a8 -. ] | % 25
        \U b16 [ _\f \U <b d>16 \U <b d>16 \U <b d>16 ] \U <b d>16 [ \U <b d>16
        \U <b d>16 \U <b d>16 ] \U <c d>16 [ \U <c d>16 \U <c d>16 \U <c d>16 ]
        \U <c d>16 [ \U <c d>16 \U <c d>16 \U <c d>16 ] \pageBreak | % 26
        \U <b d>16 [ \U <b d>16 \U <b d>16 \U <b d>16 ] \U <b d>16 [ \U <b d>16
        \U <b d>16 \U <b d>16 ] \U <c d>16 [ \U <c d>16 \U <c d>16 \U <c d>16 ]
        \U <c d>16 [ \U <c d>16 \U <c d>16 \U <c d>16 ] | % 27
        \U <b d>16 [ \U <d b'>16 \U <d b'>16 \U <d b'>16 ] \U <d b'>16 [ \U <d
          b'>16 \U <d b'>16 \U <d b'>16 ] \U <d a'>16 [ \U <d a'>16 \U <d a'>16
        \U <d a'>16 ] \U <d a'>16 [ \U <d a'>16 \U <d a'>16 \U <d a'>16 ] \break
        | % 28
        \U <d bes'>16 [ _\fz \U <d bes'>16 \U <d bes'>16 \U <d bes'>16 ] \U <d
          bes'>16 [ \U <d bes'>16 \U <d bes'>16 \U <d bes'>16 ] \U <d a'>16 [ \U
        <d a'>16 \U <d a'>16 \U <d a'>16 ] \U <d a'>16 [ \U <d a'>16 \U <d a'>16
        \U <d a'>16 ] | % 29

        \barNumberCheck #30
        \U <d bes'>16 [ _\ff \U <d bes'>16 \U <d bes'>16 \U <d bes'>16 ] \U <d
          bes'>16 [ \U <d bes'>16 \U <d bes'>16 \U <d bes'>16 ] \U <as' bes>16 [
        \U <as bes>16 \U <as bes>16 \U <as bes>16 ] \U <f bes>16 [ \U <f bes>16
        \U <f bes>16 \U <f bes>16 ] \break | % 30
        \U <g bes>16 [ \U <g bes>16 \U <g bes>16 \U <g bes>16 ] \U <f bes>16 [
        \U <f bes>16 \U <f bes>16 \U <f bes>16 ] \U <g bes>16 [ \U <g bes>16 \U
        <g bes>16 \U <g bes>16 ] \U <f bes>16 [ \U <f bes>16 \U <f bes>16 \U <f
          bes>16 ] | % 31
        \U g16 [ \U bes16 \U bes,!16 \U as'16 ] \U g16 [ \U bes16 \U bes,16 \U
        as'16 ] \U g8 r8 r4 | % 32
        r2 r4 r8 \U d8 _\p \break | % 33
        \U es8 ( [ \U bes8 \U c8 \U as8 ) ] \U bes4 ( \U c8 [ \U as8 ) ] | % 34
        \U g8 ( [ \U bes8 \U des8 \U c8 ) ] \U des4 ( \U c4 ) | % 35
        des1 ( _\pp | % 36
        \U d!2 ) \U c2 \break | % 37
        \U b!16 [ _\f \U <b d>16 \U <b d>16 \U <b d>16 ] \U <b d>16 [ \U <b d>16
        \U <b d>16 \U <b d>16 ] \U <c d>16 [ \U <c d>16 \U <c d>16 \U <c d>16 ]
        \U <c d>16 [ \U <c d>16 \U <c d>16 \U <c d>16 ] | % 38
        \U <b d>16 [ \U <d b'>16 \U <d b'>16 \U <d b'>16 ] \U <d b'>16 [ \U <d
          b'>16 \U <d b'>16 \U <d b'>16 ] \U <d c'>16 [ \U <d c'>16 \U <d c'>16
        \U <d c'>16 ] \U <d c'>16 [ \U <d c'>16 \U <d c'>16 \U <d c'>16 ]
        \pageBreak | % 39

        \barNumberCheck #40
        \U <d b'>16 [ \U <d b'>16 \U <d b'>16 \U <d b'>16 ] \U <d b'>16 [ \U <d
          b'>16 \U <d b'>16 \U <d b'>16 ] \U a'8 ( -. [ \U a8 ) -. ] \U a8. (
        ^\trill [ \U g32 \U a32 ) ] | % 40
        \U b8 [ \U g,8 ] r8 \U g32 ( [ \U a32 \U b32 \U c32 ) ] \U d8 ( -. [ \U
        a'8 ) -. ] \U a8. ( ^\trill [ \U g32 \U a32 ) ] \break | % 41
        \U b8 [ \U <d, b'>8 ] r8 \U <d a'>8 r8 \U <d b'>8 r8 \U <d a'>8 | % 42
        \U <d b'>8 [ \U <d b'>8 ] r8 \D b'8 \D c8. ( ^\trill [ \D b32 \D c32 ) ]
        \D d8 ( -. [ \D c8 ) -. ] \D b8 -. [ \D c8 -. ] \D b8 -. [ \D fis'8 -. ]
        \D g4 r4 \break r8 \U fis,!8 -. _\p \U g4 -. r8 \D fis'!8 -. \D g4 -. r8
        \U fis,!8 -. [ \U g8 -. \U gis8 -. ] \U a8 -. [ \U ais8 -. \U b8 -. ] }
      | % 43
      \D b8 -. [ \D c8 -. ] \D b8 -. [ \D fis'8 -. ] \D g4 -. r4 \repeat volta 2
      {
        | % 44
        r2 r4 r8 \U d,8 _\f \break | % 45
        \U b4 ( \U c8 ) -. [ \U a8 -. ] \U gis8 ( [ \U b8 \U e8 \U f!8 ) ] | % 46
        \U d4 ( \U e8 [ \U c8 ) ] \U b4 ( \U d8 [ \U c8 ) ] \break | % 47
        \U b4 ( \U d8 [ \U c8 ) ] \U b4 r8 \D d'8 -. _\p | % 48
        \D b4 -. r8 \D c8 -. \U a4 -. r8 \D g'!8 -. | % 49

        \barNumberCheck #50
        \D e4 -. r8 \D cis8 _\f \D d4 ( \D e8 ) -. [ \D cis8 -. ] \pageBreak | % 50
        \D d4 r8 \D b8 \D c!4 ( \D d8 ) -. [ \D b8 -. ] | % 51
        \U c8 -. [ \U f,8 -. ] \U e4 -. r2 | % 52
        r4 r8 \D a'8 ~ \D a16 [ \D f16 \D d8 ] r4 | % 53
        r4 r8 \D b'!8 ~ \D b16 [ \D gis16 \D d8 ( ] \D c8 [ \D b8 ) ] \break | % 54
        \U a8 \U dis,4 \U dis8 \U e8 ( [ \U b8 \U c8 \U d8 ) ] | % 55
        \U e8 [ \U e8 ( \U f8 \U cis'8 ) ] \D d8 ( [ \D e8 \D f8 ) \D f8 ~ ] | % 56
        \D f8 [ \D e16 \D d16 ] \D e8 [ \D fis8 ] \D g4 r8 \D g8 ~ | % 57
        \D g8 [ \D f!16 \D e16 ] \D f8 [ \D gis8 ] \D a4 r8 \D a8 ~ \break | % 58
        \D a8 [ \D g!16 \D fis16 ] \D g8 [ \D ais8 ] \D b4. \D a8 | % 59

        \barNumberCheck #60
        \D fis4 ( \D g8 [ \D e8 ) ] \D fis8 ( [ \D dis8 \D e8 \D b8 ) ] | % 60
        \U a4 ( \U ais8 ) [ \U e'16 \U e,16 ] \U fis8 ( [ \U g8 ] \D fis8 ) [ \D
        a'!8 ] _\p \break | % 61
        \D fis8. ( ^\trill [ \D e32 \D fis32 ) ] \D g8 ( [ \D e8 ] \D fis8 [ \D
        dis8 \D e8 \D b8 ) ] | % 62
        \U a4 ( \U ais8 ) [ \U e'16 \U e,16 ] \U fis8 ( [ \U g8 \U fis8 \U g8 )
        ] \break | % 63
        \U fis8 ( [ \U g8 \U fis8 \U g8 ) ] \U fis4 r4 | % 64
        \U gis,4 ( _\f \U e'4 \U a,4 ) \U dis4 \U g,!4. \U e'4. \U e8 | % 65
        \U dis8 \U fis4 _\fz \U dis16 [ \U b16 ] \U e16 [ \U fis16 \U gis16 \U a16
        ] \U b8 [ \U gis16 \U e16 ] \pageBreak | % 66
        \U dis8 \U fis4 _\fz \U dis16 [ \U b16 ] \U e8 \U e4 _\fz \U gis16 [ \U
        e16 ] | % 67
        \U dis16. [ \U e32 \U fis16. \U gis32 ] \U a16. [ \U fis32 \U a16. \U
        fis32 ] \U e16. [ \U fis32 \U gis16. \U a32 ] \U b16. [ \U gis32 \U b16.
        \U gis32 ] \break | % 68
        \U a16. [ \U cis32 \U gis16. \U b32 ] \U fis16. [ \U a32 \U fis16. \U
        dis32 ] \U e8 \D b'4 _\fz \U gis16 [ \U e16 ] | % 69

        \barNumberCheck #70
        \U fis16. [ \U a32 \U fis16. \U dis32 ] \U b16. [ \U dis32 \U fis16. \U
        dis32 ] \U e8 \U e4 _\fz \U gis16 [ \U e16 ] \break | % 70
        \U dis16. [ \U e32 \U fis16. \U gis32 ] \U a16. [ \U fis32 \U a16. \U
        fis32 ] \U e16. [ \U fis32 \U gis16. \U a32 ] \U b16. [ \U gis32 \U b16.
        \U gis32 ] | % 71
        \U a16. [ \U cis32 \U gis16. \U b32 ] \U fis16. [ \U a32 \U fis16. \U
        dis32 ] \U e8 \D b'4 _\fz \U gis16 [ \U e16 ] \break | % 72
        \U fis16. [ \U a32 \U fis16. \U dis32 ] \U b16. [ \U dis32 \U fis16. \U
        dis32 ] \U e8 \U e4 _\fz \D b'8 | % 73
        \U b,8 \U a'4 _\fz \U fis16 [ \U dis16 ] \U e8 \U e4 _\fz \U e16 ( [ _\p
        \U fis16 ) ] | % 74
        \U g4 ( \U a8 ) [ \U fis8 ] \U e16 ( [ \U dis16 \U e16 \U fis16 ) ] \U g8
        [ \U g8 ] \break | % 75
        \U fis8 ( [ \U a8 ] \U c!8 [ \U a16 \U fis16 ) ] \U g8 \D b4 \U e,16 ( [
        _\pp \U fis16 ) ] | % 76
        \U g4 ( \U a8 ) [ \U fis8 ] \U e16 ( [ \U dis16 \U e16 \U fis16 ) ] \U g8
        [ \U g8 ] | % 77
        \U g8 r8 \U g8 r8 \U g8 r8 \D g8 [ \D d'!8 -. ] _\f | % 78
        \U g,4 ( \U a8 ) -. [ \U g,8 -. ] \U f'8 \U g,4 -. \U e'4 r8 \U g,8 -.
        _\p \pageBreak | % 79

        \barNumberCheck #80
        \U c8 -. [ \U e8 -. \U d8 -. \U c8 -. ] \U b4 r8 \D b'8 | % 80
        \D c8 ( [ \D bes8 \D a8 \D b8 ) ] \D c4 r8 \U c,8 -. _\f | % 81
        \U c8 -. r8 \U g8 -. \U f'8 r8 \U g,4 \U e'4 r4 | % 82
        r4 r16. \U g,32 [ \U a16. \U b32 ] \U c16. [ \U d32 \U e16. \U f32 ] \U
        g8 [ \U g8 ] \break | % 83
        \U e4 ( \U f8 ) -. [ \U d8 -. ] \U c4 -. r8 \D c'8 ~ | % 84
        \D c8 [ \D f8 ] \D e8 r8 r8 \U c,4 \U e8 \U c'8 | % 85
        \U d,4. _\fz \U b'4. \U d,8 -. \U e8 -. [ \U f8 -. ] \U g8 -. [ \U e8 -.
        ] \U c'8 \break | % 86
        \U d,4. _\fz \U b'4. \D b8 -. \U bes8 -. [ \U a8 -. \U g8 -. \U g8 -. ]
        | % 87
        \D a8 -. [ \D bes8 -. \D c8 -. \D c8 -. ] \D bes4 ( \U g8 ) [ \U e8 ]
        \break | % 88
        \U f8 [ \U g8 \U a8 \U d,8 ] \U e8 -. [ \U f8 -. ] \U g4 -. | % 89

        \barNumberCheck #90
        \U a2 \U d,4 r8 \D e'8 \break | % 90
        \D cis8. ( ^\trill [ \D b32 \D cis32 ) ] \D d8 ( -. [ \D b8 ) -. ] \D c8.
        ( [ \D d32 \D c32 ) ] \U b8 [ \U g8 ~ ] | % 91
        \U g16 [ \U bes16 \U a16 \U g16 ] \U f8 [ \U f8 ( ] \U e8 [ \U es8 ] \D
        d8 ) [ \D g'8 ( ] \pageBreak | % 92
        \D fis4 \D f4 \D e8. [ \D f32 \D e32 ] \D d8 ) [ \D c8 ] | % 93
        \U d,8 \U b'8 r8 \U d,8 \U b'8 r8 \U d,8 \U b'8 r8 r8 ^\fermata \D c8 ~
        _\p \break | % 94
        \D c8 [ \D b16 \D a16 ] \D b8 [ \D cis8 ] \D d4 r8 \D e8 -. _\f | % 95
        \D d4. \D c!8 \D b4. \U a8 _\fz | % 96
        \U g4. \U c,8 _\fz \U e4 ( \U f8 ) [ \U d8 -. ] \break | % 97
        \U c16 [ _\f \U e16 \U c16 \U e16 \U c16 \U e16 \U c16 ] \U e16 \U c16 [
        \U e16 \U c16 \U e16 \U c16 \U e16 \U c16 ] \U e16 \U d16 [ \U f16 \U d16
        \U f16 \U d16 \U f16 \U d16 ] \U f16 \U d16 [ \U f16 \U d16 \U f16 \U d16
        \U f16 \U d16 ] \U f16 | % 98
        \U e16 [ \U e16 \U e16 \U e16 ] \U c16 [ \U e16 \U c16 \U e16 \U c16 \U
        e16 \U c16 ] \U e16 \U d16 [ \U f16 \U d16 \U f16 \U d16 \U f16 \U d16 ]
        \U f16 \U d16 [ \U f16 \U d16 \U f16 \U d16 \U f16 \U d16 ] \U f16 | % 99

        \barNumberCheck #100
        \U e4 r8 \D d'32 ( [ \D c32 \D b32 \D c32 ) ] \D b8 ( [ \D f'8 \D e8 \D
        d8 ) ] \break | % 100
        \D c4 r8 \D f32 ( [ \D e32 \D d32 \D e32 ) ] \D d8 [ \D b8 \D b8 \D b8 ]
        | % 101
        \U c8 [ \U g8 ] \U a8 \D c4 \U e,8 [ \U f8 \U d8 ] | % 102
        \U c2 \D fis'4. ^\fermata r8 ^\fermata \break | % 103
        \U g,,2 \U f'!2 \D d'4. ^\fermata \D f4. \D e8 _\p | % 104
        \D c4 -. r8 \D d8 -. \U g,4 -. r8 \D c8 -. | % 105
        \U e,4 -. r8 \U e8 -. \U f4 -. r8 \D cis'8 -. | % 106
        \D d4 -. r8 \D e8 -. \D f4 -. r4 \pageBreak | % 107
        \grace { \U g,,16 ( } {} \U g'4 ) r4 \grace { \U g,16 ( } {} \U g'4 ) r4
        | % 108
        \U as,2 ( \D c'2 | % 109

        \barNumberCheck #110
        \U as2 \D as'!2 ) | % 110
        \D es2 ( \D c2 | % 111
        \U a!2 \U fis2 ) | % 112
        \D c'2 r2 | % 113
        \U e,!2 ( \U f4 ) \U d4 \break | % 114
        \U e16 [ _\f \U e16 \U e16 \U e16 ] \U c16 [ \U e16 \U c16 \U e16 \U c16
        \U e16 \U c16 ] \U e16 \U d16 [ \U f16 \U d16 \U f16 \U d16 \U f16 \U d16
        ] \U f16 \U d16 [ \U f16 \U d16 \U f16 \U d16 \U f16 \U d16 ] \U f16 | % 115
        \U e16 [ \U e16 \U e16 \U e16 ] \U c16 [ \U e16 \U c16 \U e16 \U c16 \U
        e16 \U c16 ] \U e16 \U d16 [ \U f16 \U d16 \U f16 \U d16 \U f16 \U d16 ]
        \U f16 \U d16 [ \U f16 \U d16 \U f16 \U d16 \U f16 \U d16 ] \U f16 | % 116
        \U e16 [ \U e16 \U c'16 \U e,16 \U c'16 \U e,16 ] \U c'16 \U e,16 [ \U
        c'16 \U e,16 \U c'16 \U e,16 \U c'16 \U e,16 ] \U c'16 \D f8 -. [ \D f8
        -. ] \D f8. ( ^\trill [ \D e32 \D f32 ) ] \break | % 117
        \D e8 [ \D e8 ] \D e8. ( ^\trill [ \D d32 \D e32 ) ] \D f8 [ \D f8 ] \D
        f8. ( ^\trill [ \D e32 \D f32 ) ] | % 118
        \D e8 [ \D e8 \D e8 \D e8 ] \D f8. ( ^\trill [ \D e32 \D f32 ) ] \D g8 (
        -. [ \D f,8 ) -. ] \U e8 -. [ \U b'8 -. ] \D c8 -. [ \D f8 -. ] \D e4 r8
        \D b8 -. _\p \break \D c4 -. r8 \U b,8 -. \U c4 -. r8 \D b'8 -. \D c4 -.
        r4 r2 }
      | % 119

      \barNumberCheck #120
      \U e,8 -. [ \U b'8 -. ] \D c8 -. [ \D d8 -. ] \D f8 \D c4 -. \D e4 \U d,4
      -. \U b'4 | % 120
      \U e,4 -. \U c'4 r4 r4 r8 \bar "|."
      \pageBreak \time 2/2 \key g \major \U b,4. ( _\"p dolce" \U d8 \U g4 \U
      fis4 \U a4 \U g4 ) \U c,4 ( \U b4 ) \D c'4 ( \D b4 \U fis4 \U g4 ) \U e2 (
      \U d2 ) \U b4. ( \U d8 \U g4 \U fis4 \U a4 \U g4 ) \U c,4 ( \U b4 ) \D c'4
      ( \D b4 \break \U fis4 \U g4 ) \U e2 ( \U d2 ) \U fis4 ( \U g4 \U fis4 ) r4
      \U fis4 ( \U g4 \U fis4 ) r4 \D b4 ( \U a4 \U g2. ) \U g8 ( [ \U fis8 ) ]
      \U fis2 ^\fermata \U g,4. _\fz \U g'4. \U g8 \U g8. ( [ \U a16 ) ] \D b4
      \D c4. ( _\fz \D b8 ) \break \U fis4 ( \U g4 ) \U fis4. _\p \U g16 ( [ \U
      a16 ) ] \U g4 ( \U e8 [ \U a8 ) ] \U g4 ( \U fis4 ) \U g2 \U g,4. _\fz \U
      g'4. \U g8 \U g8. ( [ \U a16 ) ] \D b4 \D c4. ( _\fz \D b8 ) \U fis4 ( \U
      g4 ) \U fis4. ( _\p \U g16 [ \U a16 ) ] \U g4 ( \U e8 [ \U a8 ) ] \U g4 (
      \U fis4 ) \U g2 \bar "||"
      \break \time 2/2 \U g4. ( \U a8 ) \D b4 ( \U a4 \D c4 \D b4 ) \U a8 ( [ \U
      fis8 ] \U g4 ) \D e'4 ( \D d4 \pageBreak \D c4 \D b4 ) \U a4 ( \U b8 [ \U
      g8 ) ] \D d'2 \U g,4. ( \U a8 ) \D b4 ( \U a4 \D c4 \D b4 ) \break \U a8 (
      [ \U fis8 ] \U g4 ) \D e'4 ( \D d4 \D c4 \D b4 ) \U a4 ( \U b8 [ \U g8 ) ]
      \D d'2 \U a4 ( \D b4 ) \break \U a8 ( [ \U fis8 ] \U d4 ) \D c'4 ( \D b4 )
      \U a8 ( [ \U fis8 ] \U d4 ) \D d'4 ( \D c4 ) \D b4. \D b8 \D cis4 \D cis8
      ( [ \D d8 ) ] \break \D d2 \D g4. ( _\fz \D fis8 ) \D fis8 ( [ \D e8 ] \D
      d4 ) \D e4. ( _\fz \D d8 ) \D d8 ( [ \D c8 ] \D b4 ) \U a4. ( _\p \D b16 [
      \D c16 ) ] \break \D d8 ( [ \D e8 \D c8 \D a8 ) ] \U g4 ( \slashed { \U b8
        \=2( } {} \U a8 \=2) [ \U g8 ) ] \U g4 r4 \D g'4. ( _\fz \D fis8 \D fis8
      [ \D e8 ] \D d4 ) \D e4. ( _\fz \D d8 \pageBreak \D d8 [ \D c8 ] \D b4 )
      \U a4. ( _\p \D b16 [ \D c16 ) ] \D d8 ( [ \D e8 \D c8 \D a8 ) ] \U g4 (
      \slashed { \U b8 \=2( } {} \U a8. \=2) [ \U g16 ) ] \U g4 r4 \bar "||"
      \break \time 4/4 \U b,4. ( _\p \U c8 \U d4 \U c4 ) \U fis4 ( \U g4 \U fis8
      \U a4 \U g8 ) \U g4 ( \U fis4 \U e4 \U d4 ) \U fis4 ( \U g4 \break \U fis4
      ) r4 \U b,4. ( \U c8 ) \U d4 ( \U c4 \U fis4 \U g4 ) \U fis8 ( \U a4 \U g8
      ) \U g4 ( \U fis4 \U e4 \U d4 ) \U fis4 ( \U g4 \break \U fis4 ) r4 \U fis4
      ( \U g4 ) \U fis2 \U fis4 ( \U g4 ) \U fis2 \U a,4 ( \U fis'4 \U a,4 ) \U
      d4 \break \U g,2 \U d'2 \U g4. ( \D b8 ) \D b4 ( \U a4 ) \D b4 ( \U a4 \U
      g4 \U fis4 ) \U g4. ( \U fis8 \pageBreak \U e4 \U d4 ) \D c'16 ( [ \D b16
      \D c16 \D b16 ] \D c8 [ \D b16 \D a16 ) ] \U g4 ( \U e8 [ \U c8 ] \U b4 \U
      c4 ) \U b4 r4 \D b'4 ( \U a4 \break \U g4 \U fis4 ) \U g4. ( \U fis8 \U e4
      \U d4 ) \D c'16 ( [ \D b16 \D c16 \D b16 ] \D c8 [ \D b16 \D a16 ) ] \U g4
      ( \U e8 [ \U c8 ] \U b4 \U c4 ) \U b4 r4 \bar "||"
      \break \time 2/2 r2 R1 | % 61
      \U fis'8 _\p \D e'4 \D d4 \D c4 \D b8 ~ \D b8 \U a4 \U g4 \U g4 \U g8 \U
      fis2 r8 \U e8 ( [ \U b8 \U cis8 ) ] \break d1 ~ \U d8 \D c'4 \U b16 ( [ \U
      a16 ) ] \U gis8 ( [ \U a8 \U fis8 \U g8 ) ] \U e8 ( [ \U fis8 \U dis8 \U e8
      ) ] \U c8 \U cis4 \U a8 \U d2 \U fis4 ( \U g4 ) \pageBreak \U fis4 r4 \U a4
      ( \U g4 \U fis4 ) r4 \U d4 ( \U fis4 ) \U g2 ~ \U g8 [ \U bes8 ( \U a8 \U
      g8 ) ] \U fis2 \U e4. ( \U d8 ) \break \U gis8 ( [ \U a8 \U fis8 \U g8 ) ]
      r2 r2 r8 \U e8 ( [ \U d8 \U fis8 ) ] r8 \U e4 ( \U c8 \U b4 \U c4 ) \U b4
      r4 \U e4. ( \U d8 ) \break \U gis8 ( [ \U a8 \U fis8 \U g8 ) ] r2 r2 r8 \U
      e8 ( [ \U d8 \U fis8 ) ] r8 \U e4 ( \U c8 \U b4 \U c4 ) \U b4 r4 \bar "||"
      \break \time 2/2 \U b4 ( _\p \U cis4 \U d2 ) \U a'4 ( \U g4 ) \U dis4 ( \U
      e4 ) \U g8. ( [ \U a16 ] \D b4 ) \U e,8. ( [ \U fis16 ) ] \U g2 \U g4 \U
      fis2 \D b4 ( _\p \D cis4 \D d2 ) \D a'4 ( \D g4 ) \D dis4 ( \D e4 ) \D g8.
      ( [ \D a16 ] \D b4 ) \pageBreak \D e,8. ( [ \D fis16 ] \D g2 ) \D g4 \D
      fis2 \D fis4 ( \D g4 \D fis4 ) r4 \D e8 ( [ \D fis8 \D g8 ) \D g8 -. ] \D
      fis4 r4 r8 \D b4 \D a8 ~ \D a8 [ \D d,8 ( \D g8 \D fis8 ] \D e8 [ \D g8 \D
      fis8 \D e8 ) ] \break \D fis2 \D g8 ( [ \D a8 \D b8 ) \D d8 ~ ] \D d8 \D c4
      \D b8 \D e,8 ( [ \D fis8 \D g8 \D gis8 ) ] \D a4 ( \D g!2 ) \D fis8 ( [ \D
      g16 \D a16 ) ] \D g4 \D e8 ( [ \D a8 ) ] \D g4 ( \D fis4 ) \break \D g4 r4
      \D b8 ( [ \D c8 \D ais8 \D b8 ) ] \D gis8 ( [ \D a!8 \D fis8 \D g8 ) ] \D
      g4. ( \D f8 ) \D e8 ( [ \D fis!8 \D g8 \D fis8 ) ] \D e4 \D d4 ~ \D d8 [
      \D b8 ( \D c8 \D e8 ] \D b4 ) \slashed { \U d8 ( } {} \D c4 ) \break \D b4.
      ( \D c8 ) \D d8 ( [ \D cis8 \D d8 ) \D d8 ] \D d4 ( _\pp \D c!2 \U b8 [ \U
      a8 ) ] \U g2 ( \U fis8 ) \U fis8 ( -. [ \U fis8 -. \U fis8 ) -. ] \after 2
      _\> \after 2 \! fis1 ^\fermata _\< <>\! g1 ^\fermata _\pp \bar "|."
      \pageBreak \time 3/4 \key c \major r4 R2. | % 1
      \U e4 -. _\f \U e4 -. r4 \U a,4 -. \U a4 -. r4 \U g2. ~ \U g4 r4 r4 R2. | % 6
      r4 r4 \U a'4 \D c4 ( \D b4 ) \D d4 -. \U d,2 \D e'4 -. \break \U e,2 \D e'8
      ( [ \D c8 ) ] \D b2 \D c8 ( [ \D a8 ) ] \D b4 -. \U d,4 -. \U d4 -. \U d4
      -. \U d4 -. \U d4 -. \U d4 -. \U d4 -. \U d4 -. \U fis4 -. \U fis4 -. \U
      fis4 -. \U g2 \D g'4 -. \D d4 -. \D b4 -. \U g4 -. \break \U d2 r4 \U fis2.
      ( \U g4 ) r4 }
    \repeat volta 2 {
      r4 R2. | % 21
      r4 r4 \U g4 _\f \U as2. \U g2. \U fis2. \U g2 \U d4 _\p \U es4 ( \U d4 )
      \U b4 \break \U c4 ( \U b4 ) \U d4 \U es4 ( \U d4 ) \U b4 \U c4 ( \U b4 )
      \U d4 \U cis4 ( \U d4 ) r4 R2. | % 32
      R2. | % 33
      \U e!4 -. _\f \U e4 -. r4 \U a,4 -. \U a4 -. r4 \U g2. ~ \U g4 r4 \U e'4
      \break \U dis4 ( \U e4 \U g4 ) \U f2 \U f4 \U e4 ( \U f4 \U a4 ) \U g2 \D
      d'4 \D cis4 ( \D d4 \D f4 ) \D g4 ( \D f4 \D d4 ) \D f4 ( \D e4 ) \D c4 \D
      d4 ( \D e4 \D d4 ) \D e4 ( \D f4 ) \D a8 ( [ \D f8 ) ] \D e2 \D f8 ( [ \D
      d8 ) ] \pageBreak \D c4 -. \U e,4 -. \U e4 -. \U e4 -. \U e4 -. \U e4 -.
      \U e4 -. \U e4 -. \D c'4 -. \D b2. -. \D c4 r4 \D c'4 -. \D g4 -. \D e4 -.
      \D c4 -. \U g2 r4 \D b2. ( \D c4 ) r4 ^\fermata }
    \break \repeat volta 2 {
      \time 3/4 r4 R2. | % 57
      R2. | % 58
      \U gis,2. ( _\p \U a4 ) r4 r4 R2. | % 61
      R2. | % 62
      \U a2. ( \U gis4 ) r4 }
    \repeat volta 2 {
      r4 R2. | % 65
      R2. | % 66
      \break \U g!2 \U g'8 ( [ \U e8 ) ] \break \U d4 r4 r4 R2. | % 69

      \barNumberCheck #70
      R2. | % 70
      r4 r4 \U a4 _\f \U dis2. \U e2. ~ \U e2. ~ \U e2. ~ \U e2 ^\fermata r4 \U
      e2. _\pp R2. | % 78
      \break \U e2. R2. | % 80
      \U cis4 ( \U e4 \U a4 ) \U b,4 ( \U d4 \U fis4 ) \U cis2. ( \U b4 ) r4 r4
      \U e2. ~ \U e2. ~ \U e2. ~ \U e2. \U a,4 ( \U e'4 \U a4 ) \pageBreak \U b,4
      ( \U d4 \U fis4 ) \U cis2 ( \U d4 ) \U cis4 r4 r4 R2. | % 93
      R2. | % 94
      \U gis2. ( _\p \U a4 ) r4 r4 R2. | % 97
      \U bes2 \U a4 ~ \U a4 ( \U b!4 \U gis4 ) \U a4 r4 }
    \pageBreak \time 2/2 \key es \major \U es'4 _\f \U c'4 r4 \D f4 r4 \D es4 r4
    r4 \D c4 _\p \D d2 ( \D c4 ) \D g'4 \D fis2 ( \D g4 ) -. r4 \D c,4 _\f \D g'4
    r4 \D c,4 \D g'4 r4 \D c,4 \D as'4 r4 r4 \D c,4 _\p \D des2 ( \D c4 ) \D c4
    \break \D b2 ( \D c2 ) \D d!2 ( \D c4 ) r4 des,1 \U es!2 ( \U f2 ) \U es4
    _\f \U c'4 r4 \D f4 -. r4 \D es4 -. r4 r2 \break \U d,2 ( \U b'2 \U es,4 )
    \U c'4 \U g4 \U d2 \U b'2 \voiceOne \U c2 ~ \oneVoice c1 ~ c1 \break \D d,4
    _\f \D b'4 \D g'4 r4 \D es,4 \D c'4 \D g'4 r4 \D d,4 \D b'4 \D g'4 r4 \D es,4
    \D c'4 \D g'4 r4 \D d,4 \D b'4 \D g'4 r4 r4 \U g,4 \U fis2 ( \U g4 \U a4 )
    \pageBreak \D bes4 ( \U as!4 \U g4 \U f!4 ) \U es4 \D bes'4 \U as4 -. \U as4
    -. g1 \U as2 ( \D bes4 \D c4 ) \D des2 ( _\fz \D c4 \D bes4 ) \U as4 \D c2
    \D c4 \D bes4 r4 r2 R1 | % 29

    \barNumberCheck #30
    r4 \D f'2 _\p \D es4 ~ \break \D es4 \D d4 ( \D e4 \D f4 ) \D g2 ( \D f4 )
    \U as,!4 \U as8 -. [ \U bes8 -. \U as8 -. \U bes8 -. ] \U g8 -. [ \U bes8 -.
    \U g8 -. \U bes8 -. ] \U as8 -. [ \U bes8 -. \U as8 -. \U bes8 -. ] \U g8 -.
    [ \U bes8 -. \U g8 -. \U bes8 -. ] \U as8 [ \U bes8 \U as8 \U bes8 ] \U g8 [
    \U bes8 \U g8 \U bes8 ] \U as8 [ \U bes8 \U as8 \U bes8 ] \U g8 [ \U bes8 \U
    g8 \U bes8 ] \break \U as8 [ \U bes8 \U as8 \U bes8 ] \U g8 [ \U bes8 \U g8
    \U bes8 ] \U as8 [ \U bes8 \U as8 \U bes8 ] \U g4 ( \U as4 ) \D bes2 ( \U as2
    ) \U g4 -. \U g4 ( \U as4 \D bes4 ) \D c4 -. \U es,4 ( \U f4 \U g4 ) as1 ~
    \break \U as2 ( \U g4 \U f4 ) \U es4 ( \U des4 \U c4 ) \U f4 ~ \U f4 \U es2
    ( \U d!4 ) \D es4 _\f \D bes'4 \D g'4 r4 \U as,,4 -. \U d4 r4 \U g,4 -. \U
    es'4 r4 r2 \break \U f4 -. \U c'4 r4 \D f,4 -. \D es'4 r4 \U f,4 -. \U d'4 r4
    r2 a1 _\fz \pageBreak as!1 _\fz \U g4 -. r4 r2 r4 \D es'2 \D d4 ~ \break \D
    d4 \D c2 \D bes4 ~ \D bes4 \U as2 \U g4 \tweak TupletBracket.stencil ##f
    \tuplet 3/2 {
      \U f8 [ \U f8 \U f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g8 [ \U g8 \U g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U f8 [ \U f8 \U f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g8 [ \U g8 \U g8 ] }
    \break \U as4 r4 \U as4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g'8 [ \D as8 \D bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as8 [ \D g8 \D f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D d8 \D c8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U as8 \U g8 ] }
    \U f4 r4 r2 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g'8 [ \D as8 \D bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as8 [ \D g8 \D f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D d8 \D c8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U as8 \U g8 ] }
    \break \U f2 ( \U g4 \U as4 ) \D bes4 r4 \U es,4 \U es'4 r4 \U es,4 \U es'4
    r4 \D bes4 \D f'4 r4 \break \D bes,4 \D g'4 r4 \D as,4 \D c4 \D f4 r4 \U
    bes,,4 \U g'4 \U es'4 r4 \U bes,4 \U f'4 \U d'4 r4 \U bes,2 ( \U des2 )
    \pageBreak \U c2 ( \U as2 ) \U g2 ( _\p \U des'2 ) ces1 \break \U bes4 ( \U
    ces4 \U bes4 \U ces4 ) \U bes4 -. r4 \U bes4 -. r4 \U g4 -. r4 r2 }
  \U g4 -. r4 r4 \U g'4 _\f \U f2 ( \U g4 \U as4 ) \D bes4 r4 r4 \U as4 \U g2 (
  \U as4 \D bes4 ) \break \D c2 \D as'2 ~ \D as2 \D g4 \D f8 ( [ \D es8 ) ] \D
  es2. ( \D c4 ) \D c2 ( \D bes4 ) \U f4 _\p \U ges2 ( \U f4 ) \D bes4 \U a2 (
  \D bes4 ) \U f4 \U ges2 ( \U f4 ) \D bes4 \U a2 ( \D bes4 ) r4 \break r4
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ _\f \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as!8 [ \U g!8 \U f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U es8 [ \U d8 \U c8 ] }
  \U bes4 ( \U es4 \U d4 ) \U as'4 \U g2 ( \U as4 \D bes4 ) \D c2 ( \D bes4 \U g4
  ) \break \U as4 ( \U es4 \U f4 \U ges4 ) \U as2 ( \U ges2 \U f2 \U es2 ) \U
  des2 ( \U c4 ) \D c'4 \D b2 ( \D c4 \D d!4 ) \pageBreak \D es2 ( \D d2 ) \D c2
  ( \D d4 \D e4 ) \D f2 ( \D es!2 ~ ) \D es4 \tweak TupletBracket.stencil ##f
  \tuplet 3/2 {
    \D d8 [ \D c8 \D d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D d8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D es8 \D f8 ] }
  \break \D bes,4 r4 r4 \D es4 ~ \D es4 \D as4 \D bes4 \D es,8. [ \D bes'16 ]
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D des8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D g8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D des!8 \D c8 ] }
  \D bes4 r4 r2 \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c'8 [ \D des8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D g8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D des!8 \D c8 ] }
  \D bes4 r4 r4 \U es,4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c'8 [ \D des8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as8 [ \U g8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D c8 \D des8 ] }
  \break \D c4 r4 r2 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D des8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D bes8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U as8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 [ \U g8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U f8 \U es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d!8 [ \U es8 \U f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U es8 [ \U d8 \U c8 ] }
  \break \U bes4 \D f''2 _\fz \U f,4 \U g4 \D g'2 _\fz \U es,4 \U d4 \D d''2
  _\fz \D d,4 \pageBreak \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D f8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D es8 \D d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D b8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D d8 [ \D c8 \D d8 ] }
  \D es4 r4 r2 r2 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U es,8 ( [ \U d8 \U es8 ) ] }
  \break \U f4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 ( [ \U f8 \U g8 ) ] }
  \U as4 -. \D bes4 -. \U as4 -. \D bes4 -. \U as4 -. \tweak
  TupletBracket.stencil ##f \tuplet 3/2 {
    \U d,8 ( [ \U c8 \U d8 ) ] }
  \U es4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 ( [ \U es8 \U f8 ) ] }
  \U g4 -. \U as4 -. \U g4 -. \U as4 -. \U g4 -. \tweak TupletBracket.stencil
  ##f \tuplet 3/2 {
    \D es'8 ( [ \D f8 \D es8 ) ] }
  \break \D d4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 ( [ \D d8 \D c8 ) ] }
  \D b4 -. \U fis4 -. \U g4 -. \D b4 -. \D c4 -. \D d4 -. \D es4 -. r4 \D f4 -.
  r4 \D es4 -. r4 r4 \D c4 -. _\p \D d2 ( \D c4 ) \D g'4 -. | % 121
  \D fis2 ( \D g4 ) -. r4 \break | % 122
  \D c,4 -. _\f \D g'4 r4 \D c,4 -. \D g'4 r4 | % 123
  \D c,4 \D as'4 r4 r4 \D c,4 _\p | % 124
  \D des2 ( \D c4 ) \D c4 | % 125
  \D b2 ( \D c2 ) | % 126
  \D d!2 ( \D c4 ) r4 | % 127
  des,1 ( | % 128
  \U es!2 \U f2 ) | % 129

  \barNumberCheck #130
  R1 | % 130
  \pageBreak des1 ( _\p | % 131
  \U es2 \U f2 ) | % 132
  R1 | % 133
  des1 ~ _\pp | % 134
  \U des2 \U ges2 ( | % 135
  \U f2 \U es2 ) | % 136
  as,1 _\f f'1 \break | % 137
  \U c2. _\fz \U es2. \U as,4 | % 138
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U des8 ( [ \U c8 \U des8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 ( [ \U e8 \U f8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as8 ( [ \U g8 \U as8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U es8 ( [ \U f8 \U es8 ) ] }
  | % 139

  \barNumberCheck #140
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d!8 -. [ \U es8 -. \U f8 -. ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 [ \U ges8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D bes8 \D ces8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D ces8 [ \D bes8 \D as8 ] }
  \break | % 140
  \U ges4 \U ges2 \U ges4 | % 141
  \U d!2. _\fz \U f2. \U bes,4 | % 142
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U es8 ( [ \U d8 \U es8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U ges8 ( [ \U f8 \U ges8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 ( [ \U a8 \U bes8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 ( [ \U g8 \U f8 ) ] }
  \break | % 143
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U e8 -. [ \U f8 -. \U g8 -. ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U as!8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D c8 \D des8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  | % 144
  \U as4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 ( [ \U e8 \U f8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as8 ( [ \U g8 \U as8 ) ] }
  | % 145
  \D c4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 ( [ \U b8 \U c8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g'8 ( [ \U fis8 \U g8 ) ] }
  \pageBreak | % 146
  \D c4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 ( [ \U b8 \U c8 ) ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g'8 ( [ \U fis8 \U g8 ) ] }
  | % 147
  \U g,4 r4 \D fis''4 r4 | % 148
  \D g4 r4 \D fis4 r4 \break | % 149

  \barNumberCheck #150
  \D g4 r4 \D fis4 r4 | % 150
  \D g4 r4 r4 ^\fermata \bar "||"
  \key c \major \U g,4 _\p | % 151
  g1 ~ | % 152
  \U g4 ( \U fis4 \U g4 ) r4 | % 153
  r2 r4 \U a4 | % 154
  a1 ~ \break | % 155
  \U a4 ( \U gis4 \U a4 ) r4 | % 156
  r2 r4 \D f'4 _\f | % 157
  \D e2 ( \D f4 ) \U a,4 | % 158
  \D bes2 ( \U a4 ) r4 | % 159

  \barNumberCheck #160
  \U f2 ( \U e!4 ) r4 | % 160
  \U f2 ( \U e8 ) -. [ \U g8 -. \U e8 -. \U g8 -. ] | % 161
  \U f8 -. [ \U g8 -. \U f8 -. \U g8 -. ] \U e8 -. [ \U g8 -. \U e8 -. \U g8 -.
  ] | % 162
  \U f8 -. [ \U g8 -. \U f8 -. \U g8 -. ] \U e8 -. [ \U g8 -. \U e8 -. \U g8 -.
  ] \break | % 163
  \U f8 [ \U g8 \U f8 \U g8 ] \U e8 [ \U g8 \U e8 \U g8 ] | % 164
  \U f8 [ \U g8 \U f8 \U g8 ] \U e8 [ \U g8 \U e8 \U g8 ] | % 165
  \U f8 [ \U g8 \U f8 \U g8 ] \D e8 [ \D c'8 \D e8 \D g8 ] | % 166
  \D f8 [ \D g8 \D f8 \D g8 ] \D e4 ( \D f4 ) | % 167
  \D g2 ( \D f2 ) | % 168
  \D e4 -. \D e4 ( \D f4 \D g4 ) | % 169

  \barNumberCheck #170
  \D a4 -. \D c,4 ( \D d4 \D e4 ) \pageBreak | % 170
  f1 ~ | % 171
  \D f2 \D e4 ( \D d4 ) | % 172
  \D c4 ( \D bes4 \U a4 ) \D d4 ~ | % 173
  \D d4 \D c2 ( \D b!4 ) | % 174
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D e8 [ \D f8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D e8 \D d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D b8 \D a8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U f8 \U e8 ] }
  \break | % 175
  \U d4 r4 r2 | % 176
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D e'8 [ \D f8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D e8 \D d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D b8 \D a8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U f8 \U e8 ] }
  | % 177
  \U d2 ( \U e4 \U f4 ) | % 178
  \U g4 r4 \D c4 r4 \break | % 179

  \barNumberCheck #180
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D c8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D c8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D c8 \D c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D c8 \D c8 ] }
  | % 180
  \D e4 r4 \U f,4 \U d'4 r4 | % 181
  \U e,4 \U c'4 r4 r4 \D e4 | % 182
  \D f2 ( \D e4 \D b'4 ) \break | % 183
  \D c4 r4 r4 \U g,4 | % 184
  \U as2 ( \U g4 \U f4 ) | % 185
  \U e4 -. r4 \U e4 -. \U c'4 r4 | % 186
  \D c4 -. \D e4 r4 \U e,4. \U c'4. \U e,8 \U c'8 | % 187
  \U e,4 \U c'4 r4 r2 \bar "|."
}

PartPTwoVoiceTwo = \relative a' {
  \repeat volta 2 {
    \repeat volta 2 {
      \repeat volta 2 {
        \clef "treble" \time 4/4 \key c \major \partial 8 s8*33 \break s1*3
        \break s1*2 \break s1*2 \pageBreak s1*4 \break s1*3 \break s1*2 \break
        s1*3 \break s1*3 \pageBreak s1*2 \break s1*2 \break s1*3 \break s1*4
        \break s1*2 \pageBreak s1*2 \break s1*3 \break s8*15 }
      \repeat volta 2 {
        \break s8*9 \break s1*3 \pageBreak s1*4 \break s1*4 \break s1*3 \break
        s1*2 \break s1*3 \pageBreak s1*2 \break s1*2 \break s1*2 \break s1*3
        \break s1*4 \pageBreak s1*4 \break s1*3 \break s1*2 \break s1*2 \break
        s1*2 \pageBreak s1*2 \break s1*3 \break s1*3 \break s1*3 \break s1*4
        \pageBreak s1*7 \break s1*3 \break s1*3 \break s1*2 }
      \bar "|."
      \pageBreak \time 2/2 \key g \major s1*5 \break s1*7 \break s2*13 \bar "||"
      \break \time 2/2 s2*5 \pageBreak | % 22
      \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
      ##t a8 ^\turn s4*9 \break s1 | % 26
      \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
      ##t a8 ^\turn s4*5 \break s1*3 \break s1*3 \break s1*3 \pageBreak s2*5
      \bar "||"
      \break \time 4/4 s2*7 \break s1*4 \break s1*3 \break s1*3 \pageBreak s1*3
      \break s2*7 \bar "||"
      \break \time 2/2 s2*9 \break s1*4 \pageBreak s1*4 \break s1*4 \break s2*7
      \bar "||"
      \break \time 2/2 s2*13 \pageBreak s1*5 \break s1*4 \break s1*4 \break s1*5
      \bar "|."
      \pageBreak \time 3/4 \key c \major s2*13 \break s1*6 \break s1*2 }
    \repeat volta 2 {
      s2*11 \break s2*15 \break s2*15 \pageBreak s2*13 }
    \break \repeat volta 2 {
      \time 3/4 s1*6 }
    \repeat volta 2 {
      s4*7 \break s2. \break s4*33 \break s4*33 \pageBreak s1*8 }
    s4 \pageBreak \time 2/2 \key es \major s1*7 \break s1*6 \break s1 \hideNote
    r2 \D es4 r4 s1*2 \break s1*4 \pageBreak s1*9 \break s1*6 \break s1*6 \break
    s1*5 \break s1*3 \pageBreak s1*3 \break s1*3 \break s1*4 \break s1*3 \break
    s1*3 \pageBreak s1*3 \break s1*3 }
  s1*3 \break s1*8 \break s1*4 \break s1*5 \pageBreak s1*4 \break s1*4 \break
  s1*3 \break s1*3 \break s1*3 \pageBreak s1*3 \break s1*4 \break s1*6 \break
  s1*8 \pageBreak s1*7 \break s1*3 \break s1*3 \break s1*3 \pageBreak s1*3
  \break s4*7 \bar "||"
  \key c \major s4*17 \break s1*8 \break s1*7 \pageBreak s1*5 \break s1*4 \break
  s1*4 \break s1*5 \bar "|."
}

PartPThreeVoiceOne = \relative g' {
  \repeat volta 2 {
    \repeat volta 2 {
      \repeat volta 2 {
        \clef "alto" \time 4/4 \key c \major \partial 8 \oneVoice \D g8 _\f \D c4
        ( \D d8 ) -. [ \D b8 -. ] \D c4 -. r8 \D d,8 -. _\p | % 1
        \U g,8 -. [ \U c8 -. \U b8 -. \U a8 -. ] \U g4 r8 \D g'8 | % 2
        \D e4 ( \D f8 ) -. [ \D d8 -. ] \D c4 r8 \U g8 -. _\f | % 3
        \U a8 -. r8 \D <b d>8 -. r8 \D <c e>4 r8 \U g8 \break | % 4
        \U e4 ( \U f8 ) -. [ \U d8 -. ] \U c4 -. r8 \D e'8 -. | % 5
        \D c4 ( \U d8 ) -. [ \U g,8 -. ] \U e4 -. r16. \U c32 [ \U d16. \U e32 ]
        | % 6
        \U f16. [ \U g32 \U a16. \U b32 ] \D c8 [ \D c8 ~ ] \D c8 [ \D f8 \D e8
        \D <g, g'>8 ] \break | % 7
        \D <g f'>4. _\fz \U b8 -. \D c8 -. [ \D d8 -. \D e8 -. \D g8 -. ] | % 8
        \D <g, f'>4. _\fz \U b8 -. \D c8 -. [ \D d8 -. \D e8 -. \D g8 -. ]
        \break | % 9

        \barNumberCheck #10
        \D <g, f'>4. _\fz \D d'8 -. \D e8 -. [ \D d8 -. ] \D c16. [ \D e32 \D d16.
        \D c32 ] | % 10
        \D b16. [ \D f'32 \D e16. \D d32 ] \D c16. [ \D e32 \D d16. \D c32 ] \D
        b16. [ \D f'32 \D e16. \D d32 ] \D c16. [ \D e32 \D d16. \D c32 ]
        \pageBreak | % 11
        \U b16. [ \U g32 \U c16. \U g32 ] \U b16. [ \U g32 \U c16. \U g32 ] \U b4
        r8 \D d8 | % 12
        \U b4 ( \U c8 ) -. [ \U a8 -. ] \U g4 r8 \D d''8 | % 13
        \D b4 ( \D c8 ) -. [ \D a8 -. ] \D g4. \D dis8 | % 14
        \D e4. \U b8 \D c4. \D d!8 \break | % 15
        \D e2 \D d2 ~ | % 16
        \D d4 \D g,8 ( [ \D g'8 ) ] \D g4 \D e4 | % 17
        \D fis4 r4 r4 r8 \D c'8 \break | % 18
        \D b8 ( [ \D cis8 ) ] \D d8 [ \D d8 ] \D b8. ( ^\trill [ ^\markup " ♮"
        \D a32 \D b32 ) ] \D c8 [ \D a8 ] | % 19

        \barNumberCheck #20
        \D b8 [ \D g8 ] \D fis8 [ \D d8 ] \D a'8. ( ^\trill [ _\fz \D g32 \D a32
        ) ] \D g8 ( -. [ \D g8 ) -. ] \break | % 20
        \D a8. ( ^\trill [ _\fz \D g32 \D a32 ) ] \D g8 ( -. [ \D g8 ) -. ] \D a8.
        ( ^\trill [ _\fz \D g32 \D a32 ) ] \D g8 ( -. [ \D g8 ) -. ] | % 21
        \D a4 _\ff \D <d, a'>8 [ \D <d a'>8 ] \D <d a'>8 r8 r4 | % 22
        r2 r4 r8 \D g8 ~ _\fz \break | % 23
        \D g8 [ \D fis16 _\p \D e16 ] \D fis8 [ \D e8 ~ ] _\fz \D e8 [ _\p \D d16
        \D cis16 ] \D d8 [ \D c16 \D b16 ] | % 24
        \U a8 [ \U b16 \U a16 ] \U g8 [ \U g8 ] _\fz \U g4 ( \U fis8 ) [ \U c'8
        ] | % 25
        \U b16 [ _\f \U g16 \U g16 \U g16 ] \U g16 [ \U g16 \U g16 \U g16 ] \U d16
        [ \U a'16 \U a16 \U a16 ] \U a16 [ \U a16 \U a16 \U a16 ] \pageBreak | % 26
        \U b16 [ \U g16 \U g16 \U g16 ] \U g16 [ \U g16 \U g16 \U g16 ] \U d16 [
        \U a'16 \U a16 \U a16 ] \U a16 [ \U a16 \U a16 \U a16 ] | % 27
        \D b16 [ \D g'16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D fis16
        [ \D fis16 \D fis16 \D fis16 ] \D fis16 [ \D fis16 \D fis16 \D fis16 ]
        \break | % 28
        \D g16 [ _\fz \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D
        fis16 [ \D fis16 \D fis16 \D fis16 ] \D fis16 [ \D fis16 \D fis16 \D fis16
        ] | % 29

        \barNumberCheck #30
        \D g16 [ _\ff \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D
        f!16 [ \D f16 \D f16 \D f16 ] \U bes,16 [ \U bes16 \U bes16 \U bes16 ]
        \break | % 30
        \D es16 [ \D g16 \D g16 \D bes16 ] \D bes16 [ \D as16 \D as16 \D f16 ]
        \D es16 [ \D g16 \D g16 \D bes16 ] \D bes16 [ \D as16 \D as16 \D f16 ] | % 31
        \D g8 -. [ \D bes8 -. \D bes8 -. \D bes8 -. ] \D bes8 r8 r4 | % 32
        r4 r8 \U bes,8 _\p \U g4 ( \U as8 [ \U f8 ) ] \break | % 33
        \U es4. \U d8 \U es8 \D es'!4 \D d8 | % 34
        \D es4 ( \U bes8 [ \U as8 ) ] \U g4 ( \U as4 ) | % 35
        \U bes4. ( _\pp \U g8 \U bes4. \U g8 ) | % 36
        \U b!2 \U a!2 \break | % 37
        \U g16 [ _\f \U g16 \U g16 \U g16 ] \U g16 [ \U g16 \U g16 \U g16 ] \U d16
        [ \U a'16 \U a16 \U a16 ] \U a16 [ \U a16 \U a16 \U a16 ] | % 38
        \U b16 [ \U g16 \U g16 \U g16 ] \U g16 [ \U g16 \U g16 \U g16 ] \U d16 [
        \U a'16 \U a16 \U a16 ] \U a16 [ \U a16 \U a16 \U a16 ] \pageBreak | % 39

        \barNumberCheck #40
        \D b16 [ \D b16 \D d16 \D d16 ] \U g,16 [ \U g16 \U b16 \U b16 ] \U c16
        [ \U c16 \U a16 \U a16 ] \U d,8 [ \U d'32 ( \U c32 \U b32 \U a32 ) ] | % 40
        \D g8 [ \D b'8 ] \D b8. ( ^\trill [ \D a32 \D b32 ) ] \D a8 [ \D d,8 ] r8
        \U d32 ( [ \U c32 \U b32 \U a32 ) ] \break | % 41
        \D g8 [ \D g'8 ] r8 \D fis8 r8 \D g8 r8 \D fis8 | % 42
        \D g8 [ \D g8 ] r8 \U b,8 \U c8. ( ^\trill [ \U b32 \U c32 ) ] \D d8 (
        -. [ \D d8 ) -. ] \D d8 -. [ \D fis8 -. ] \D g8 -. [ \D c,16 ( \D a16 )
        ] \U b4 r8 \D d8 -. _\p \break \U b4 -. r8 \D d'8 -. \D b4 -. r8 \D d,8
        -. \U b4 -. r4 r4 r8 }
      | % 43
      \D d8 -. [ \D fis8 -. ] \D g8 -. [ \D c,16 \D a16 ] \U b4 r8 \D d8 _\p
      \repeat volta 2 {
        | % 44
        \U b4 ( \U c8 ) -. [ \U a8 -. ] \U g4 r8 \U b8 _\f \break | % 45
        \U gis4 ( \U a8 ) -. [ \U dis,8 -. ] \U e8 ( \U gis!4 \D d'!8 ) | % 46
        \U b4 ( \U c8 [ \U a8 ) ] \U gis4 ( \U b8 [ \U a8 ) ] \break | % 47
        \U gis4 ( \U b8 [ \U a8 ) ] \U gis4 r4 | % 48
        r8 \D d'8 -. _\p \U b4 -. r8 \D e8 -. \D c4 -. | % 49

        \barNumberCheck #50
        r8 \D g'8 -. \D e4 -. r8 \D bes'8 [ _\f \D g8 \D a8 ] \pageBreak | % 50
        \D f4 r4 r8 \D a8 [ \D f8 \D g8 ~ ] | % 51
        \D g8 [ \D b8 -. ] \D c8 -. [ \D d,8 -. ] \U g,4 r8 \D c8 | % 52
        \D b8 ( [ \D e8 \D d8 \D cis8 ) ] \D d4 r8 \D d8 | % 53
        \D c!8 ( [ \D f8 \D e8 \D dis8 ) ] \D e4 r8 \U e,8 \break | % 54
        \U dis8 ( [ \U c'8 \U b8 \U a8 ] \U e8 ) [ \U f'!8 ( \U e8 \U d!8 ) ] | % 55
        \U c8 ( [ \U bes8 \U a8 \U g8 ) ] \D f8 ( [ \D e8 \D d8 ) \D d''8 ] | % 56
        \D b!4 ( \D c8 ) -. [ \D a8 -. ] \D g4 r8 \D e'8 | % 57
        \D cis8. ( ^\trill [ \D b32 \D cis32 ) ] \D d8 ( -. [ \D b8 ) -. ] \D a4
        r8 \D fis'8 \break | % 58
        \D dis8. ( ^\trill [ \D cis32 \D dis32 ) ] \D e8 ( -. [ \D c8 ) -. ] \D
        b4 \D b,16 -. [ \D b'16 -. \D b,16 -. \D b'16 -. ] | % 59

        \barNumberCheck #60
        \D b,16 -. [ \D b'16 -. \D b,16 -. \D b'16 -. ] \D b,16 [ \D b'16 \D b,16
        \D b'16 ] \D b,16 [ \D b'16 \D b,16 \D b'16 ] \D b,8 [ \D g'8 ] | % 60
        \D fis4 ( \D g8 ) [ \D g16 \D e16 ] \D dis8 ( [ \D e8 ] \D dis8 ) [ \D b16
        -. _\p \D b'16 -. ] \break | % 61
        \D b,16 -. [ \D b'16 -. \D b,16 -. \D b'16 -. ] \D b,16 [ \D b'16 \D b,16
        \D b'16 ] \D b,16 [ \D b'16 \D b,16 \D b'16 ] \D b,8 [ \D g'8 ] | % 62
        \D fis4 ( \D g8 ) [ \D g16 \D e16 ] \D dis8 ( [ \D e8 \D dis8 \D e8 ) ]
        \break | % 63
        \D dis8 ( [ \D e8 \D dis8 \D e8 ) ] \D dis4 r4 | % 64
        r4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ | % 65
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ \pageBreak | % 66
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ | % 67
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ \break | % 68
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ | % 69

        \barNumberCheck #70
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ \break | % 70
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ | % 71
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ \break | % 72
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 ~ _\fz \U b'4 ~ | % 73
        \U e,4 \U b'4 \U e,2 _\fz \U b'2 \U e,4 _\fz \U b'4 | % 74
        \U e,8 [ _\p \U e'8 \U e8 \U e8 ] \U e,8 [ \U e'8 \U e8 \U e8 ] \break | % 75
        \U e,8 [ \U e'8 \U e8 \U e8 ] \U e,8 [ \U e'8 \U e8 \U e8 ] | % 76
        \U e,8 [ _\pp \U e'8 \U e8 \U e8 ] \U e,8 [ \U e'8 \U e8 \U e8 ] | % 77
        \D e8 r8 \D e8 r8 \D e8 r8 \D e8 [ \D g8 -. ] _\f | % 78
        \D c4 ( \D d8 ) -. [ \D b8 -. ] \D c4 -. r8 \D d,8 -. _\p \pageBreak | % 79

        \barNumberCheck #80
        \U g,8 -. [ \U c8 -. \U b8 -. \U a8 -. ] \U g4 r8 \D g'8 | % 80
        \D e4 ( \D f8 ) -. [ \D d8 -. ] \D c4 r8 \U g8 -. _\f | % 81
        \U a8 -. r8 \D b8 -. \D d8 r8 \D c4 \D e4 r8 \U g,8 | % 82
        \U e4 ( \U f8 ) -. [ \U d8 -. ] \U c4 -. r8 \D e'8 \break | % 83
        \D c4 ( \U d8 ) -. [ \U g,8 -. ] \U e4 -. r16. \U c32 [ \U d16. \U e32 ]
        | % 84
        \U f16. [ \U g32 \U a16. \U b32 ] \D c8 [ \D c8 ~ ] \D c8 [ \D f8 ] \D e8
        [ \D g,8 ] \D g'8 | % 85
        \D g,4. _\fz \D f'4. \U b,8 -. \D c8 -. [ \D d8 -. ] \D e8 -. [ \D g,8
        -. ] \D g'8 \break | % 86
        \D g,4. _\fz \D f'4. \D f8 -. \D g8 -. [ \D f8 -. \D e8 -. \D e8 -. ] | % 87
        \D f8 -. [ \D g8 -. \D a8 -. \D f8 -. ] \D g4 ( \D e4 ) \break | % 88
        \D d8 [ \D e8 \D f8 \D b,8 ] \U c8 [ \U d8 \U e8 \U e,8 ] | % 89

        \barNumberCheck #90
        \U f4. ( \U fis8 \U g4 ) r4 \break | % 90
        r4 r8 \D f'8 \D e8 ( [ \D fis8 ) ] \D g8 -. [ \D g8 -. ] | % 91
        \D e8. ( ^\trill [ ^\markup " ♮" \D d32 \D e32 ) ] \D f!8 [ \D d8 ] \D e8
        [ \D c8 ] \U b8 [ \U b8 ] \pageBreak | % 92
        \U c8. ( ^\trill [ \U b32 \U c32 ) ] \D d8. ( ^\trill [ \D c32 \D d32 )
        ] \D e8 [ \D c'8 \D b8 \D c8 ] | % 93
        \D d8 r8 \D g,,8 \D f'8 r8 \D g,8 \D f'8 r8 r8 ^\fermata \D a8 _\p
        \break | % 94
        \D f4 ( \D g8 ) [ \D e8 ] \D d8 [ \D a'8 ] \D d8 [ \D c8 ~ ] _\fz | % 95
        \D c8 [ \D b16 \D a16 ] \D b8 [ \D a8 ~ ] _\fz \D a8 [ \D g16 \D fis16 ]
        \D g8 [ \D f16 \D e16 ] | % 96
        \D d8 [ \D e16 \D d16 ] \D c8 [ \D c8 -. ] _\fz \D c4 ( \D b8 ) [ \D f'8
        -. ] \break | % 97
        \D e16 [ _\f \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D g16
        [ \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] | % 98
        \D g16 [ \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D g16 [
        \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] | % 99

        \barNumberCheck #100
        \D g4 r8 \D f32 ( [ \D e32 \D d32 \D e32 ) ] \D f8 -. [ \D b8 -. \D b8
        -. \D b8 -. ] \break | % 100
        \D c4 r8 \D g8 \D f8 [ \D f8 \D d8 \D d8 ] | % 101
        \D e4 r4 r8 \D c8 [ \D d8 \D f8 ] | % 102
        \D fis2. ^\fermata r4 ^\fermata \break | % 103
        \U g,2. ^\fermata \U d'2. r8 ^\fermata r8 | % 104
        r8 \D g8 -. _\p \D e4 -. r8 \D f8 -. \D d4 -. | % 105
        r8 \D e8 -. \D c4 -. r8 \D cis8 -. \D d4 -. | % 106
        r8 \D e8 -. \D f4 -. r8 \D gis8 -. \D a4 -. \pageBreak | % 107
        r4 \grace { \U e,16 ( [ } {} \grace { \U g16 ] } {} \D c4 ) r4 \grace {
          \U d,16 ( [ } {} \grace { \U f16 ] } {} \U b4 ) | % 108
        r4 \U c,2 \D es'4 ~ | % 109

        \barNumberCheck #110
        \D es4 \D c2 \D c'4 ~ | % 110
        \D c4 \D fis,2 \D es4 ~ | % 111
        \D es4 \D c2 \U a!4 ~ | % 112
        \U a4 \D a'2 r4 | % 113
        \D c,2 ( \D b4 ) \D d4 \U b4 \break | % 114
        \D c16 [ _\f \D g'16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D
        g16 [ \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] | % 115
        \D g16 [ \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D g16 [
        \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] | % 116
        \D g8 [ \D e8 \D c8 \D e'8 ] \D d8 ( -. [ \D d8 ) -. ] \D d8. ( ^\trill
        [ \D c32 \D d32 ) ] \break | % 117
        \D c8 [ \D c8 ] \D c8. ( ^\trill [ \D b32 \D c32 ) ] \D d8 [ \D d8 ] \D
        d8. ( ^\trill [ \D c32 \D d32 ) ] | % 118
        \D c8 [ \D e,8 \D g8 \D e8 ] \D f8. ( ^\trill [ \D e32 \D f32 ) ] \D g8
        ( -. [ \D d8 ) -. ] \D e8 -. [ \D d8 -. ] \U c8 -. [ \U g8 -. ] \U d'8
        \U g,4 \U e'4 r4 \break r8 \D g8 -. _\p \D e4 -. r8 \U g,8 -. \U e4 -. r8
        \D g'8 -. [ \D e8 -. \D f8 -. ] \D d8 -. [ \D e8 -. \D c8 -. \D d8 -. ]
      }
      | % 119

      \barNumberCheck #120
      \D e8 -. [ \D d8 -. ] \U c8 -. [ \U g8 -. ] \U d'8 \U g,4 -. \U e'4 \U g,4
      -. \U d'4 | % 120
      \U g,4 -. \U e'4 r4 r4 r8 \bar "|."
      \pageBreak \time 2/2 \key g \major \U g,4 _\"p dolce" r4 r2 \D d'4 ( -. \D
      d4 ) -. \U fis,8 ( [ \U a8 ] \U g4 ) r2 \U a4 ( \U b4 \D e4 \U g,4 ) \U
      fis2 ( \U g4 ) r4 r2 \D d'4 ( -. \D d4 ) -. \U fis,8 ( [ \U a8 ] \U g4 ) r2
      \break \U a4 ( \U b4 \D e4 \U g,4 ) \U fis2 \D d'4 \D d4 \D d4 r4 \U a4 (
      \U g8 [ \U b8 ) ] \D d4 r4 \D d4 ( \D e8 [ \D fis8 ] \D g4 ) \U g,4 \D e'4
      \D e8 ( [ \D d8 ) ] \D d2 ^\fermata \U g,2 _\fz \U d'2 \D e8. ( [ \D fis16
      ) ] \D g4 \D g4. _\fz \D g8 \break \D d4 -. \D a'4 \D d,4 -. \D b'4 \D d,2
      _\p \U g,4 ( \D e'8 [ \D c8 ) ] \U b4 ( \slashed { \U d8 } {} \D c4 ) \U b2
      \U g2 _\fz \U d'2 \D e8. ( [ \D fis16 ) ] \D g4 \D g4. _\fz \D g8 \D d4 -.
      \D a'4 \D d,4 -. \D b'4 \D d,2 _\p \U g,4 ( \D e'8 [ \D c8 ) ] \U b4 (
      \slashed { \U d8 } {} \D c4 ) \U b2 \bar "||"
      \break \time 2/2 r2 R1 | % 21
      R1 | % 22
      \pageBreak R1 | % 23
      R1 | % 24
      R1 | % 25
      \break R1 | % 26
      R1 | % 27
      R1 | % 28
      \break R1 | % 29

      \barNumberCheck #30
      R1 | % 30
      R1 | % 31
      \break R1 | % 32
      R1 | % 33
      R1 | % 34
      \break R1 | % 35
      R1 | % 36
      R1 | % 37
      \pageBreak R1 | % 38
      R1 | % 39

      \barNumberCheck #40
      r2 \bar "||"
      \break \time 4/4 r2 r2 \U d,2 ~ _\p \U d4 \U g4 r2 r2 \U d2 ~ \break \U d4
      r4 r2 r2 \U d2 ~ \U d4 \U g4 r2 r2 \U d2 ~ \break \U d4 r4 \U d2 ~ d1 ~ \U
      d2 \U d4 ( \U a'4 \U fis4 ) \break \U g2 ( \U e2 ) \U d2 r2 R1 | % 53
      \pageBreak r2 \U fis4. ( _\fz \U g16 [ \U a16 ) ] \U b8 ( [ \U c8 ) ] \U
      c,4 \U c'4 \U d,2 \U g4 r4 r2 \break R1 | % 57
      r2 \U fis4. ( _\fz \U g16 [ \U a16 ) ] \U b8 ( [ \U c8 ) ] \U c,4 \U c'4
      \U d,2 \U g4 r4 \bar "||"
      \break \time 2/2 \D g'4. ( _\p \D a8 ) \D b4 ( \D a4 \D c4 \D b4 ) \D a8 (
      [ \D fis8 ] \D g4 ) \D e'4 ( \D d4 \D c4 \D b4 ) \D a4 ( \D b8 [ \D g8 ) ]
      \D d'2 \D g,4. ( \D a8 ) \break \D b4 ( \D a4 \D c4 \D b4 ) \D a8 ( [ \D
      fis8 ] \D g4 ) \D e'4 ( \D d4 \D c4 \D b4 ) \D a4 ( \D b8 [ \D g8 ) ] \D
      d'2 \D a4 ( \D b4 ) \pageBreak \D a8 ( [ \D fis8 ) ] \D d4 \D c'4 ( \D b4
      ) \D a8 ( [ \D fis8 ) ] \D d4 \D d'4 ( \D c4 ) \D b4. \D b8 \D cis4 \D cis8
      ( [ \D d8 ) ] \D d2 \D g4. ( \D fis8 \break \D fis8 [ \D e8 ] \D d4 ) \D e4.
      ( \D d8 \D d8 [ \D c8 ] \D b4 ) \D a4. ( _\fz \D b16 [ \D c16 ) ] \D d8 (
      [ \D e8 \D c8 \D a8 ) ] \D g4 ( \slashed { \U b8 \=2( } {} \D a8. \=2) [
      \D g16 ) ] \D g8 ( [ \D a16 \D b16 ] \D c16 [ \D d16 \D e16 \D fis16 ) ]
      \D g4. ( \D fis8 \break \D fis8 [ \D e8 ] \D d4 ) \D e4. ( \D d8 \D d8 [
      \D c8 ] \D b4 ) \D a4. ( _\fz \D b16 [ \D c16 ) ] \D d8 ( [ \D e8 \D c8 \D
      a8 ) ] \D g4 ( \slashed { \U b8 \=2( } {} \D a8. \=2) [ \D g16 ) ] \D g4 r4
      \bar "||"
      \break \time 2/2 \U g,2 ~ _\p \U g4 \U fis2 \U g4 \U fis4 ( \U e4 \D c'4
      \U b4 ) \D c4 ( \D d4 ) \D e2 \D d4 r4 \D g2 ~ _\p \D g4 \D fis2 \D g4 \D
      fis4 ( \D e4 \D c'4 \D b4 ) \pageBreak \D c4 ( \D d4 ) \D e2 \D fis,4 r4
      \D d'4 ( \D cis4 ) \D d4 ( \D c!8 [ \D b8 ) ] \D a4 ( \D g8 [ \D cis8 ) ]
      \D d4. ( \D c!8 ) \D b8 ( [ \D gis8 \D a8 \D fis8 ) ] \D g!8 ( [ \D a8 \D
      b8 \D a8 ) ] \D g8 ( [ \D b8 \D a8 \D g8 ) ] \break \D a4 r4 \D d8 ( [ \D
      c8 \D b8 ) \D b8 ] \D c8 -. [ \D e8 ( \D fis8 ) \D g8 ~ ] \D g8 [ \D g,16
      ( \D a16 \D b8 \D e,8 ) ] \D e8 ( [ \D fis8 \D g8 \D fis8 ) ] \D e4 \D d4
      ~ \D d8 \D g4 \D e'8 \D b4 \slashed { \U d8 ( } {} \D c4 ) \break \D b4 r4
      \D e4. \D d8 ~ \D d8 \D c4 \D b8 \D ais8 ( [ \D b8 \D c8 \D gis8 ) ] \D a!8
      ( [ \D dis,8 \D e8 \D fis8 ) ] \D g8 [ \D g8 ( \D fis8 \D a8 ) ] \D g8 ( [
      \D b8 \D e,8 \D c'8 ) ] \D d,!8 ( [ \D g8 \D fis8 ) \D fis8 ] \break
      \voiceOne \U g8 \hideNote r8 \hideNote r8 \hideNote r8 \oneVoice \D f8 ( [
      \D e8 \D f8 \D b,8 ) ] \D c8 ( [ _\pp \D d8 \D e8 \D fis!8 ) ] \D g8 ( [
      \D fis8 \D g8 \D f8 ) ] \D e4 \D d4 \D c8 [ \D c8 ( -. \D es8 \D c8 -. \D
      es8 \D c8 ) -. ] \D es8 c1 ^\fermata _\< \after 2 _\> \after 2 \! es1 <>\!
      b1 ^\fermata _\pp d1 \bar "|."
      \pageBreak \time 3/4 \key c \major r4 R2. | % 1
      \D c4 -. _\f \D c4 -. r4 \U f,4 -. \U f4 -. r4 \U d2 \D d'4 ~ \D d4 \D c4
      r4 r4 r4 \D c4 \U b4 ( \D c4 ) \D e4 -. \U a,4 ( \U b4 ) \D g'4 -. \D a4 (
      \D b4 \D a4 ) \break \D b4 ( \D c4 \D a4 ) \D d2 \D d,4 \D g4 -. \U b,4 -.
      \U b4 -. \U b4 -. \U b4 -. \U b4 -. \U b4 -. \U b4 -. \U b4 -. \D c4 -. \D
      c4 -. \U a4 -. \D d2 r4 R2. | % 17
      \break R2. | % 18
      \D c2. ( \U b4 ) r4 }
    \repeat volta 2 {
      r4 R2. | % 21
      R2. | % 22
      R2. | % 23
      r4 r4 \D c4 ~ _\f \D c4 \D d4 \D es8 [ \D c8 ] \D g'2 \U b,4 _\p \D c4 (
      \U b4 ) r4 \break r4 r4 \U b4 \D c4 ( \U b4 ) r4 R2. | % 30
      r4 r4 \U b4 \D c4 ( \U b4 ) r4 R2. | % 33
      \D c4 -. _\f \D c4 -. r4 \U f,4 -. \U f4 -. r4 \U d2 \D d'4 ~ \D d4 \D c4
      r4 \break r4 r4 \D c4 \D d2 r4 r4 r4 \D d4 \D e2 r4 r4 r4 \D f4 \D e4 ( \D
      f4 \D a4 ) \D d,4 ( \D e4 ) \D g4 \U g,2 \D a'4 \U a,2 \U d,4 \U g2.
      \pageBreak \U g4 -. \U g4 -. \U g4 -. \U g4 -. \U g4 -. \U g4 -. \U g4 -.
      \U g4 -. \D e'4 -. \D f2 \D d4 \D g4 r4 r4 R2. | % 53
      R2. | % 54
      \D f2. ( \D e4 ) r4 ^\fermata }
    \break \repeat volta 2 {
      \time 3/4 r4 R2. | % 57
      R2. | % 58
      \U e,2. ~ _\p \U e4 r4 r4 R2. | % 61
      R2. | % 62
      \U fis2. ( \U e4 ) r4 }
    \repeat volta 2 {
      r4 R2. | % 65
      R2. | % 66
      \break \U e2 \U a4 \break \U a4 r4 r4 R2. | % 69

      \barNumberCheck #70
      r4 r4 \U gis4 _\f \D e'2 ( \D c4 ) \U a4 ( \U b4 \U c8 [ \U a8 ) ] \D e'4
      r4 r4 R2. | % 74
      \U e,2. ~ \U e2 ^\fermata r4 \D cis'2. _\pp R2. | % 78
      \break \U b2. R2. | % 80
      R2. | % 81
      R2. | % 82
      R2. | % 83
      R2. | % 84
      r4 r4 \U e,4 \D cis'2 ( \U a4 ) \U e4 r4 \U e4 \D d'2 ( \U b4 ) \U e,4 r4
      r4 \pageBreak r4 r4 \U fis4 \U e2 ( \U gis4 ) \U a4 r4 r4 R2. | % 93
      R2. | % 94
      \U e2. ~ _\p \U e2 r4 R2. | % 97
      \U f!2 ( \U fis4 ) \U e2. ~ \U e4 r4 }
    \pageBreak \time 2/2 \key es \major \D es'4 _\f \D c'4 r4 \D d,4 \D b'4 r4
    \D es,4 \D c'4 r4 r4 \D g4 _\p \D as2 ( \D g4 ) \D b4 \D c2 ( \D b4 ) -. r4
    \D c4 _\f r4 \D g4 r4 \D f4 r4 r4 \D as4 _\p \D bes2 ( \D as4 ) \D e4 \break
    \D f2 ( \D es!2 ) \U b2 ( \D c4 ) \U g4 as1 \D c2 ( \D d!2 ) \U g,4 _\f \U
    es'4 r4 \D d4 -. \D b'4 r4 \D es,4 -. \D c'4 r4 r2 \break \D f,2 ( \D es2 )
    \D f2 ( \D es4 \D e4 ) \D f4 ( \D g4 \D as4 \D g4 ) \D f2 ( \D fis2 ) \break
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g,8 [ _\f \U b8 \U d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D fis8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g,8 [ \U c8 \U es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D fis8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g,8 [ \U b8 \U d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D fis8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g,8 [ \U c8 \U es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D fis8 \D g8 ] }
    \U g,4 r4 r2 R1 | % 21
    \pageBreak r2 r4 \D c4 \U bes2 ( \D c4 \D d4 ) \D es2 ( \D des2 ) \D c2 ( \U
    bes4 \U as4 ) \U g2 ( _\fz \U as4 \U bes4 ) \D c2. \D f4 \D f2. \D as4 _\p
    \D g2 ( \D as4 \D e4 ) \D f4 ( \D d4 \D es!4 \D g4 ) \break \D bes4 ( \D as4
    \D g4 \D f4 ) \D e2 \D f2 ~ \D f2 \D es!4 \U es,4 \U d2 ( \U es4 ) \D bes''4
    \D f2 ( \D g4 ) \U es,4 \U d2 ( \U es4 ) \D bes''4 \break \D f2 ( \D g4 ) r4
    r2 r4 \D c,4 \U bes2 ( \D c4 \D d4 ) \D es4 -. \D es4 ( \D f4 \D g4 ) \D as4
    -. \D c,4 ( \D d4 \D e4 ) f1 ~ \break \D f2 ( \D es!4 \D d4 ) \D es2. ( \D c4
    \U bes2. \U as4 ) \U es4 _\f \U g4 r4 \U as4 -. r4 \U bes4 -. r4 r2 \break
    \D es4 -. r4 \D c'4 -. r4 \D bes4 -. \D d,4 -. \D es4 -. \D f4 -. c1 _\fz es1
    \pageBreak d1 _\fz \D es4 -. r4 \D f4 -. r4 \D g4 -. r4 r2 \break R1 | % 54
    R1 | % 55
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes,8 [ \U bes8 \U bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U bes8 \U bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U bes8 \U bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U bes8 \U bes8 ] }
    \break \U as4 r4 \U bes4 r4 \U es,4 r4 r4 \D es'4 \D d2 ( \D es4 \D f4 ) \D
    g4 r4 r4 \D es4 \break \D d2 ( \D es4 \D f4 ) \D g4 r4 \U des,4 r4 \U c4 r4
    \U d!4 r4 \break \U es4 r4 \U as4 r4 \U bes4 r4 \U bes4 r4 \U g2. ( \U bes4
    ) \pageBreak \U as2 ( \U f2 ) \U g2. ( _\p \U bes4 ) \U as2 ( \U f2 ) \break
    \U g4 ( \U f4 \U g4 \U f4 ) \U g4 -. r4 \U bes4 -. r4 \U bes4 -. r4 r2 }
  \U bes4 -. r4 r2 r2 r4 \D c4 _\f \U bes2 ( \D c4 \D d4 ) \D es4 r4 r4 \D des4
  \break \D c4 ( \U bes4 \U as4 \U g4 ) \U f4 \D f'4 ( \D g4 \D as8 [ \D bes8 )
  ] c1 \D f,2. \D d4 _\p \D es2 ( \D d4 ) r4 r2 r4 \D d4 \D es2 ( \D d4 ) r4 R1
  | % 83
  \break R1 | % 84
  R1 | % 85
  r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ _\f \D f8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as8 [ \U g8 \U f8 ] }
  \U es4 ( \U as4 \U g4 \D des'4 ) \break \D c2 ( \D des4 \D es4 ) \D f2 ( \D es2
  \D des2 \D c2 ) \U bes2 ( \U as4 ) r4 r2 r4 \D f'4 \pageBreak \D es2 ( \D f4
  \D g4 ) \D as2 ( \D g2 ) \D f2 ( \D g4 \D as4 ) \D bes4 r4 r4 \U bes,4 ~
  \break \U bes4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g'8 [ \D f8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D g8 \D as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D as8 \D bes8 ] }
  \D c4 \D es,2 \D es4 \D c4 \D es4 \D c2 \D es2 \D as,4 \D as'4 \D bes,2 \D g'2
  \D as4 \D bes4 \break \D c4 \D c,2 \D es2 \D as,4 \D as'4 \D bes,2 \D g'2 \D
  as4 \D bes4 \D es,4 \D c'4 \D g4 \D as4 \tweak TupletBracket.stencil ##f
  \tuplet 3/2 {
    \D des,8 [ \D c8 \D bes8 ] }
  \break \D c4 \D g'4 \D as4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des,8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D des8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D des8 [ \D c8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as8 [ \U bes8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U as8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 [ \U g8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U f8 \U es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d!8 [ \U es8 \U f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U as8 \U a8 ] }
  \break \U bes4 \D as'!2 _\fz \D d,4 \D es4 \D es'2 _\fz \U bes,4 \U g4 \D f'2
  _\fz \D g4 ~ \pageBreak \D g4 \D b4 \D c4 \tweak TupletBracket.stencil ##f
  \tuplet 3/2 {
    \D f,8 [ \D b8 \D f8 \D b8 \D f8 ] }
  \D b8*2/3 \D es,4 \D c'4 \D b4 \D c4 \tweak TupletBracket.stencil ##f \tuplet 3/2
  {
    \D f,8 [ \D b8 \D f8 \D b8 \D f8 ] }
  \D b8*2/3 \D es,4 \D c'4 \D b4 \D c4 \tweak TupletBracket.stencil ##f \tuplet 3/2
  {
    \U c,8 ( [ \U b!8 \U c8 ) ] }
  \break \D d4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D e8 ( [ \D d8 \D e8 ) ] }
  \D f4 -. \D e4 -. \D f4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 ( [ \D f8 \D e8 ) ] }
  \D f4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes,8 ( [ \U a8 \U bes8 ) ] }
  \D c4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D d8 ( [ \D c8 \D d8 ) ] }
  \D es!4 -. \D d4 -. \D es4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 ( [ \D es8 \D d8 ) ] }
  \D es4 -. r4 \break r2 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 ( [ \D f8 \D es8 ) ] }
  \D d4 -. \U g,4 -. \D g'4 -. \D g4 -. \D es4 -. \D c'4 r4 \D d,4 -. \D b'4 r4
  \D es,4 -. \D c'4 r4 r4 \D g4 -. _\p \D as2 ( \D g4 ) \D b4 -. | % 121
  \D c2 ( \D b4 ) -. r4 \break | % 122
  \D c4 -. _\f r4 \D g4 -. r4 | % 123
  \D f4 -. r4 r4 \D as4 _\p | % 124
  \D bes2 ( \D as4 ) \D e4 | % 125
  \D f2 ( \D es!2 ) | % 126
  \U b2 ( \D c4 ) \U g4 | % 127
  as1 ( | % 128
  \U g2 \D d'2 ) | % 129

  \barNumberCheck #130
  R1 | % 130
  \pageBreak as1 ( _\p | % 131
  \U g2 \D d'2 ) | % 132
  R1 | % 133
  as1 ( _\pp | % 134
  bes1 | % 135
  \D des2 \D c2 ) | % 136
  des1 _\f \break | % 137
  ges,1 _\fz | % 138
  \U f2 ( \U es2 ) | % 139

  \barNumberCheck #140
  \U f4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D d'!8 -. [ \D es8 -. \D f8 -. ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D ges8 \D as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D as8 [ \D ges8 \D f8 ] }
  \break | % 140
  \D es4 \U bes2 \U bes4 | % 141
  \U as4 \D ces2 _\fz \U f,4 | % 142
  \U ges2 ( \U f2 ) \break | % 143
  \U g!4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D e'8 -. [ \D f8 -. \D g8 -. ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D as8 \D bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D as8 \D g8 ] }
  | % 144
  c,1 ~ ( as'1 | % 145
  c,1 ~ ) g'1 ~ \pageBreak | % 146
  c,1 g'1 | % 147
  \U b,4 r4 \D c4 r4 | % 148
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U b8 \U d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g,8 [ \U b8 \U d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis8 \D g8 ] }
  \break | % 149

  \barNumberCheck #150
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g,8 [ \U b8 \U d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g,8 [ \U c8 \U es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis8 \D g8 ] }
  | % 150
  \U g,4 r4 r4 ^\fermata \bar "||"
  \key c \major \D e'4 _\p | % 151
  \D f2 ( \D e4 ) \D f4 | % 152
  \D e4 ( \D c'4 \D b4 ) r4 | % 153
  r2 r4 \D f4 | % 154
  \D g2 ( \D f4 ) \D g4 \break | % 155
  \D f4 ( \D d'4 \D cis4 ) r4 | % 156
  R1 | % 157
  r2 r4 \D f,4 _\f | % 158
  \D e2 ( \D f4 ) r4 | % 159

  \barNumberCheck #160
  \D d2 ( \D e4 ) r4 | % 160
  \D d2 ( \D e4 ) r4 | % 161
  r2 r4 \D c'!4 | % 162
  \D b2 ( \D c4 ) \D c,4 \break | % 163
  \D d2 ( \D e4 ) \D c'4 | % 164
  \D b2 ( \D c4 ) \D c,4 | % 165
  \D d2 ( \D e4 ) r4 | % 166
  r2 r4 \D a4 | % 167
  \D g2 ( \D a4 \D b4 ) | % 168
  \D c4 -. \D c4 ( \D d4 \D e4 ) | % 169

  \barNumberCheck #170
  \D f4 -. \D a,4 ( \D b4 \D cis4 ) \pageBreak | % 170
  d1 ~ | % 171
  \D d2 \D c!4 ( \D b4 ) | % 172
  \D c2. \D a4 | % 173
  \D g2. \D f4 | % 174
  \D e4 r4 r4 \D c'4 \break | % 175
  \D b2 ( \D c4 \D d4 ) | % 176
  \D e4 r4 r4 \D c4 | % 177
  \D b2 ( \D c4 \D d4 ) | % 178
  \D e4 r4 \D c4 r4 \break | % 179

  \barNumberCheck #180
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f,8 [ \D f8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f8 [ \D f8 \D f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es8 [ \D es8 \D es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D c8 \D c8 ] }
  | % 180
  \D c4 r4 \U g4 r4 | % 181
  \D c4 r4 r4 \D g'4 | % 182
  \D as2 ( \D g4 \D f4 ) \break | % 183
  \D e4 r4 r4 \D e4 | % 184
  \D f2 ( \D e4 \D b'4 ) | % 185
  \D c4 -. r4 \U g,4 -. \U e'4 r4 | % 186
  \U g,4 -. \U e'4 r4 \U g,4. \U e'4. \U g,8 \U e'8 | % 187
  \U g,4 \U e'4 r4 r2 \bar "|."
}

PartPThreeVoiceTwo = \relative a' {
  \repeat volta 2 {
    \repeat volta 2 {
      \repeat volta 2 {
        \clef "alto" \time 4/4 \key c \major \partial 8 s8*33 \break s1*3 \break
        s1*2 \break s1*2 \pageBreak s1*4 \break s1*3 \break s1*2 \break s1*3
        \break s1*3 \pageBreak s1*2 \break s1*2 \break s1*3 \break s1*4 \break
        s1*2 \pageBreak s1*2 \break s1*3 \break s8*15 }
      \repeat volta 2 {
        \break s8*9 \break s1*3 \pageBreak s1*4 \break s1*4 \break s1*3 \break
        s1*2 \break s1*3 \pageBreak s1*2 \break s1*2 \break s1*2 \break s1*3
        \break s1*4 \pageBreak s1*4 \break s1*3 \break s1*2 \break s1*2 \break
        s1*2 \pageBreak s1*2 \break s1*3 \break s1*3 \break s1*3 \break s1*4
        \pageBreak s1*7 \break s1*3 \break s1*3 \break s1*2 }
      \bar "|."
      \pageBreak \time 2/2 \key g \major s1*5 \break s1*7 \break s2*13 \bar "||"
      \break \time 2/2 s2*5 \pageBreak s1*3 \break s1*3 \break s1*3 \break s1*3
      \break s1*3 \pageBreak s2*5 \bar "||"
      \break \time 4/4 s2*7 \break s1*4 \break s1*3 \break s1*3 \pageBreak s1*3
      \break s2*7 \bar "||"
      \break \time 2/2 s2*5 | % 62
      \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
      ##t a8 ^\turn s4*5 \break s1*2 | % 66
      \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
      ##t a8 ^\turn s4*5 \pageBreak s1*4 \break s1*4 \break s2*7 \bar "||"
      \break \time 2/2 s2*13 \pageBreak s1*5 \break s1*4 \break s1*4 \break | % 99

      \barNumberCheck #100
      \D g,8 ( [ \oneVoice \D b8 \D d8 \D e8 ) ] s2*9 \bar "|."
      \pageBreak \time 3/4 \key c \major s2*13 \break s1*6 \break s1*2 }
    \repeat volta 2 {
      s2*11 \break s2*15 \break s2*15 \pageBreak s2*13 }
    \break \repeat volta 2 {
      \time 3/4 s1*6 }
    \repeat volta 2 {
      s4*7 \break s2. \break s4*33 \break s4*33 \pageBreak s1*8 }
    s4 \pageBreak \time 2/2 \key es \major s1*7 \break s1*6 \break s1*4 \break
    s1*4 \pageBreak s1*9 \break s1*6 \break s1*6 \break s1*5 \break s1*3
    \pageBreak s1*3 \break s1*3 \break s1*4 \break s1*3 \break s1*3 \pageBreak
    s1*3 \break s1*3 }
  s1*3 \break s1*8 \break s1*4 \break s1*5 \pageBreak s1*4 \break s1*4 \break
  s1*3 \break s1*3 \break s1*3 \pageBreak s1*3 \break s1*4 \break s1*6 \break
  s1*8 \pageBreak s1*7 \break s1*3 \break s1*3 \break s1*3 \pageBreak s1*3
  \break s4*7 \bar "||"
  \key c \major s4*17 \break s1*8 \break s1*7 \pageBreak s1*5 \break s1*4 \break
  s1*4 \break s1*5 \bar "|."
}

PartPFourVoiceOne = \relative b {
  \repeat volta 2 {
    \repeat volta 2 {
      \repeat volta 2 {
        \clef "bass" \time 4/4 \key c \major \partial 8 \oneVoice \D b8 _\f \D c4
        ( \D f,8 ) -. [ \D g8 -. ] \U c,4 -. r8 \U b8 -. _\p | % 1
        \U c8 -. [ \U a8 -. \U d8 -. \U d8 -. ] \U g,4 r4 | % 2
        r2 r4 r8 \D e'8 -. _\f | % 3
        \D f8 -. r8 \D g8 -. r8 \U c,4 r8 \D e8 \break | % 4
        \U c4 ( \U d8 ) -. [ \U g,8 -. ] \U e4 -. r4 | % 5
        R1 | % 6
        r4 r16. \U c32 [ \U d16. \U e32 ] \U f16. [ \U g32 \U a16. \U b32 ] \U c8
        [ \U c8 ] \break | % 7
        \U <c, ~ c' ~>2 _\fz \U <c c'>8 r8 r4 | % 8
        \U <c ~ c' ~>2 _\fz \U <c c'>8 r8 r4 \break | % 9

        \barNumberCheck #10
        \U <c ~ c' ~>2 _\fz \U <c c'>8 r8 r4 | % 10
        \D g'16. [ \D g'32 \D a16. \D b32 ] \D c8 r8 \D g,16. [ \D g'32 \D a16.
        \D b32 ] \D c8 r8 \pageBreak | % 11
        \U g,16. [ \U g32 \U g16. \U g32 ] \U g16. [ \U g32 \U g16. \U g32 ] \U
        g4 r8 \D b'8 | % 12
        \D g4 ( \D a8 ) -. [ \D d,8 -. ] \D g4 r4 | % 13
        R1 | % 14
        r2 r4 r8 \U bes,8 \break | % 15
        \U a4 ( \U bes8 ) -. [ \U g8 -. ] \U fis2 | % 16
        \U g4 ( \U b!8 ) [ \U g8 ] \U e8 [ \U e'8 \U cis8 \U a8 ] | % 17
        \D d16 [ \D d'16 \D d,16 \D d'16 ] \D d,16 [ \D d'16 \D d,16 \D d'16 ]
        \D d,16 [ \D d'16 \D d,16 \D d'16 ] \D d,16 [ \D d'16 \D d,16 \D d'16 ]
        \break | % 18
        \D d,16 [ \D d'16 \D d,16 \D d'16 ] \D d,16 [ \D d'16 \D d,16 \D d'16 ]
        \D d,16 [ \D d'16 \D d,16 \D d'16 ] \D d,16 [ \D d'16 \D d,16 \D d'16 ]
        | % 19

        \barNumberCheck #20
        \D d,16 [ \D d'16 \D d,16 \D d'16 ] \D d,8 [ \D b'8 ] \D c8. ( ^\trill [
        _\fz \D b32 \D c32 ) ] \D b8 ( -. [ \D b8 ) -. ] \break | % 20
        \D c8. ( ^\trill [ _\fz \D b32 \D c32 ) ] \D b8 ( -. [ \D b8 ) -. ] \D c8.
        ( ^\trill [ _\fz \D b32 \D c32 ) ] \D b8 ( -. [ \D g8 ) -. ] | % 21
        \D fis4 _\ff \U fis,!8 [ \U fis8 ] \U fis8 r8 r4 | % 22
        R1 | % 23
        \break r2 r4 r8 \U c'8 ~ _\fz | % 24
        \U c8 [ \U b16 _\p \U a16 ] \U b8 [ \U cis8 ] _\fz \D d2 | % 25
        \U g,8 [ _\f \U g'8 ] r8 \U g,16 ( [ \U b16 ) ] \D d8 [ \D fis'8 ] r8 \D
        fis8 \pageBreak | % 26
        \D g8 [ \D g,,8 ] r8 \U g16 ( [ \U b16 ) ] \D d8 [ \D fis'8 ] r8 \D fis8
        | % 27
        \D g8 [ \D g,,8 ] r8 \U g16 ( [ \U b16 ) ] \D d8 -. [ \D fis8 -. \D a8
        -. \D fis8 -. ] \break | % 28
        \D g,8 -. [ _\fz \D g'8 -. \D bes8 -. \D g8 -. ] \U d,8 -. [ \U fis'8 -.
        \U a8 -. \U fis8 -. ] | % 29

        \barNumberCheck #30
        \D g16 [ _\ff \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D
        d16 [ \D d16 \D d16 \D d16 ] \D d16 [ \D d16 \D d16 \D d16 ] \break | % 30
        \D es16 [ \D es16 \D es16 \D es16 ] \D d16 [ \D d16 \D d16 \D d16 ] \D
        es16 [ \D es16 \D es16 \D es16 ] \D d16 [ \D d16 \D d16 \D d16 ] | % 31
        \D es8 -. [ \D d8 -. \D es8 -. \D d8 -. ] \D es8 r8 r8 \U bes8 _\p | % 32
        \U g4 ( \U as8 [ \U f8 ) ] \U es2 ~ \break | % 33
        \U es4. \U bes'8 \U g4 ( \U as8 [ \U f8 ) ] | % 34
        es1 ~ | % 35
        es1 _\pp | % 36
        d!1 \break | % 37
        \U g8 [ _\f \U g'8 ] r8 \U g,16 ( [ \U b!16 ) ] \D d8 [ \D fis'8 ] r8 \D
        fis8 | % 38
        \D g8 [ \D g,,8 ] r8 \U g32 ( [ \U a32 \U b32 \U c32 ) ] \D d8 [ \D fis'8
        ] r8 \D fis8 \pageBreak | % 39

        \barNumberCheck #40
        \D g8 [ \D g,,8 ] r8 \U g32 ( [ \U a32 \U b32 \U c32 ) ] \D d8 [ \D fis'8
        ] \D fis8. ( ^\trill [ \D e32 \D fis32 ) ] | % 40
        \D g8 [ \D g8 ] \D g8. ( ^\trill [ \D fis32 \D g32 ) ] \D fis8 [ \D fis8
        ] \D fis8. ( ^\trill [ \D e32 ) \D fis32 ] \break | % 41
        \D g8 [ \D g8 ] r8 \D fis8 r8 \D g8 r8 \D fis8 | % 42
        \D g8 [ \D g8 ] r8 \D b,8 \D c8. ( ^\trill [ \D b32 \D c32 ) ] \D d8 (
        -. [ \D d,8 ) -. ] \D g8 -. [ \D d8 -. ] \D g8 -. [ \D d8 -. ] \U g,4 r8
        \U fis8 -. _\p \break \U g4 -. r8 \D fis'!8 -. \D g4 -. r8 \U fis,!8 -.
        \U g4 -. r4 r4 r8 }
      | % 43
      \D g'8 -. [ \D d8 -. ] \D g8 -. [ \D d8 -. ] \U g,4 r8 \D b'8 _\p \repeat
      volta 2 {
        | % 44
        \D g4 ( \D a8 ) -. [ \D d,8 -. ] \U b4 r4 \break | % 45
        e,1 ~ _\f | % 46
        e1 ~ \break | % 47
        \U e2. r4 | % 48
        r8 \D b''8 -. _\p \D gis4 -. r8 \D c8 -. \D a4 -. | % 49

        \barNumberCheck #50
        r8 \D e'8 -. \D cis4 -. r2 \pageBreak | % 50
        r2 r4 r8 \D g8 _\f | % 51
        \D e8 [ \D f16 \D d16 ] \U c8 -. [ \U b8 -. ] \U c4 r8 \D d8 | % 52
        \U g,4 r4 r4 r8 \D e'8 | % 53
        \U a,4 r4 r2 \break | % 54
        r4 r8 \U a8 \U gis8 ( [ \U d'8 \U c8 \U b8 ) ] | % 55
        \U a8 ( [ \U g!8 \U f8 \U e8 ) ] \U d4 r4 | % 56
        R1 | % 57
        R1 | % 58
        \break R1 | % 59

        \barNumberCheck #60
        r2 r4 r8 \U b'8 | % 60
        \U c,16 -. [ \U c'16 -. \U c,16 -. \U c'16 -. ] \U c,16 [ \U c'16 \U c,16
        \U c'16 ] \U b2 \break | % 61
        r2 r4 r8 \U b8 _\p | % 62
        \U c,16 -. [ \U c'16 -. \U c,16 -. \U c'16 -. ] \U c,16 [ \U c'16 \U c,16
        \U c'16 ] \U b2 ( \break | % 63
        \U b2. ) r4 | % 64
        \U e,2 ( _\fz \U b'2 \U e,2 _\fz \U b'2 | % 65
        \U e,2 ) _\fz \U b'2 \U e,2 ( _\"fz sempre" \U b'2 \pageBreak | % 66
        \U e,2 \U b'2 \U e,2 \U b'2 | % 67
        \U e,2 ) \U b'2 \U e,2 ( \U b'2 \break | % 68
        \U e,2 \U b'2 \U e,2 ) \U b'2 | % 69

        \barNumberCheck #70
        \U e,2 ( \U b'2 \U e,2 \U b'2 \break | % 70
        \U e,2 ) \U b'2 \U e,2 ( \U b'2 | % 71
        \U e,2 \U b'2 \U e,2 ) \U b'2 \break | % 72
        \U e,2 ( \U b'2 \U e,2 \U b'2 | % 73
        \U e,2 ) \U b'2 \U e,2 ( \U b'2 | % 74
        \U e,2 ) _\p \U b'2 r2 \break | % 75
        R1 | % 76
        R1 | % 77
        r2 r4 r8 \D b'8 -. _\f | % 78
        \D c4 ( \D f,8 ) -. [ \D g8 -. ] \U c,4 -. r8 \U b8 -. _\p \pageBreak | % 79

        \barNumberCheck #80
        \U c8 -. [ \U a8 -. \U d8 -. \U d8 -. ] \U g,4 r4 | % 80
        r2 r4 r8 \D e'8 -. _\f | % 81
        \D f8 -. r8 \D g8 -. r8 \U c,4 r8 \D e8 | % 82
        \U c4 ( \U d8 ) -. [ \U g,8 -. ] \U e4 -. r4 \break | % 83
        R1 | % 84
        r4 r16. \U c32 [ \U d16. \U e32 ] \U f16. [ \U g32 \U a16. \U b32 ] \U c8
        [ \U c8 ] | % 85
        \U c,2 ~ _\fz \U c'2 ~ \U c,8 \U c'8 r8 r4 \break | % 86
        \U c,2 ~ _\fz \U c'2 ~ \U c,2 \U c'2 | % 87
        \U c,2 \U c'2 \U cis,2 _\fz \break | % 88
        \U d4 r4 r2 | % 89

        \barNumberCheck #90
        r2 \U g16 [ \U g'16 \U g,16 \U g'16 ] \U g,16 [ \U g'16 \U g,16 \U g'16
        ] \break | % 90
        \U g,16 [ \U g'16 \U g,16 \U g'16 ] \U g,16 [ \U g'16 \U g,16 \U g'16 ]
        \U g,16 [ \U g'16 \U g,16 \U g'16 ] \U g,16 [ \U g'16 \U g,16 \U g'16 ]
        | % 91
        \U g,16 [ \U g'16 \U g,16 \U g'16 ] \U g,16 [ \U g'16 \U g,16 \U g'16 ]
        \U g,16 [ \U g'16 \U g,16 \U g'16 ] \U g,16 [ \U g'16 \U g,16 \U g'16 ]
        \pageBreak | % 92
        \U g,16 [ \U g'16 \U g,16 \U g'16 ] \U g,16 [ \U g'16 \U g,16 \U g'16 ]
        \U g,16 [ \U g'16 \U g,16 \U g'16 ] \U g,16 [ \U g'16 \U g,16 \U g'16 ]
        | % 93
        \U g,8 r8 \U g8 r8 \U g8 r8 r8 ^\fermata r8 \break | % 94
        R1 | % 95
        r2 r4 r8 \D f'8 ~ _\fz | % 96
        \D f8 [ \D e16 _\p \D d16 ] \D e8 [ \D fis8 ] _\fz \D g4 \U g,4 \break | % 97
        \U c4 _\f r8 \U c,16 [ \U c'16 ] \D g8 [ \D b'8 ] r8 \D c32 ( [ \D b32
        \D a32 \D b32 ) ] | % 98
        \U c8 [ \U c,,8 ] r8 \U c16 [ \U c'16 ] \D g8 [ \D b'8 ] r8 \D c32 ( [
        \D b32 \D a32 \D b32 ) ] | % 99

        \barNumberCheck #100
        \D c16 [ \D c16 \D c16 \D c16 ] \D c16 [ \D c16 \D c16 \D c16 ] \D c16 [
        \D c16 \D c16 \D c16 ] \D c16 [ \D c16 \D c16 \D c16 ] \break | % 100
        \D c16 [ \D c16 \D c16 \D c16 ] \D c16 [ \D c16 \D c16 \D c16 ] \D c16 [
        \D c16 \D c16 \D c16 ] \D c16 [ \D c16 \D c16 \D c16 ] | % 101
        \D c8 [ \D e,8 \D f8 \D a8 ] \U g8 [ \U g8 \U g8 \U g,8 ] | % 102
        \U a2. ^\fermata r4 ^\fermata \break | % 103
        \U b2. ^\fermata r8 ^\fermata r8 | % 104
        r8 \D e'8 -. _\p \D c4 -. r8 \D d8 -. \D g,4 -. | % 105
        r8 \D c8 -. \D e,4 -. r8 \D e8 -. \D f4 -. | % 106
        r8 \D cis'8 -. \D d4 -. r8 \D e8 -. \D f4 -. \pageBreak | % 107
        r4 \grace { \U g,,16 ( } {} \D g'4 ) r4 \grace { \U g,32 ( } {} \D g'4 )
        | % 108
        r4 \U as,2 \D c'4 ~ | % 109

        \barNumberCheck #110
        \D c4 \D as2 \D as'!4 ~ | % 110
        \D as4 \D es2 \D c4 ~ | % 111
        \D c4 \D a!2 \D fis4 ~ | % 112
        \D fis4 \D c'2 r4 | % 113
        g,1 \break | % 114
        \U c4 _\f r8 \U c,16 [ \U c'16 ] \D g8 [ \D b'8 ] r8 \D c32 ( [ \D b32
        \D a32 \D b32 ) ] | % 115
        \U c8 [ \U c,,8 ] r8 \U c16 [ \U c'16 ] \D g8 [ \D b'8 ] r8 \D c32 ( [
        \D b32 \D a32 \D b32 ) ] | % 116
        \D c16 [ \D g'16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D g16
        [ \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \break | % 117
        \D g16 [ \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] \D g16 [
        \D g16 \D g16 \D g16 ] \D g16 [ \D g16 \D g16 \D g16 ] | % 118
        \D c,8 [ \D c8 \D c8 \D e,8 ] \D f8. ( ^\trill [ \D e32 \D f32 ) ^\trill
        ] \D g8 ( -. [ \D g8 ) -. ] \U c,8 -. [ \U g8 -. \U c8 -. \U g8 -. ] \U
        c,4 r4 \break r8 \D b''8 -. _\p \D c4 -. r8 \U b,8 -. \U c4 -. r8 \D b'8
        -. [ \D c8 -. \D a8 -. ] \D b8 -. [ \D g8 -. \D a8 -. \D fis8 -. ] }
      | % 119

      \barNumberCheck #120
      \U c8 -. [ \U g8 -. \U c8 -. \U g8 -. ] \U c,4 -. \U g'4 -. | % 120
      \U c,4 -. r4 r4 r8 \bar "|."
      \pageBreak \time 2/2 \key g \major \D g''4 _\"p dolce" r4 r2 \D fis4 ( \D
      g4 ) \D d4 \U g,4 r2 \D d'4 ( \D g4 \U c,4 \U cis4 ) \D d2 ( \D g4 ) r4 r2
      \D fis4 ( \D g4 ) \D d4 \U g,4 r2 \break \D d'4 ( \D g4 \U c,4 \U cis4 )
      \D d2 \D d4 \D d4 \D d4 r4 \D d4 \D d4 \D d4 r4 \U b4 ( \U c8 [ \U d8 ) ]
      \D e2 \U a,4 \U a4 \D d2 ^\fermata \D b'4. _\fz \D b8 \D c4 \D g4 \U c,4.
      _\fz \D g'8 \break \D d4 \D g4 \U c,2 _\p \U b4 ( \U c4 \D d4 ) \D d4 -.
      \U g,2 \D b'4. _\fz \D b8 \D c4 \D g4 \U c,4. _\fz \D g'8 \D d4 \D g4 \U
      c,2 _\p \U b4 ( \U c4 \D d4 ) \D d4 -. \U g,2 \bar "||"
      \break \time 2/2 r2 R1 | % 21
      R1 | % 22
      \pageBreak R1 | % 23
      R1 | % 24
      R1 | % 25
      \break R1 | % 26
      R1 | % 27
      R1 | % 28
      \break R1 | % 29

      \barNumberCheck #30
      R1 | % 30
      R1 | % 31
      \break R1 | % 32
      R1 | % 33
      R1 | % 34
      \break R1 | % 35
      R1 | % 36
      R1 | % 37
      \pageBreak R1 | % 38
      R1 | % 39

      \barNumberCheck #40
      r2 \bar "||"
      \break \time 4/4 \D g'4. ( _\p \D a8 ) \D b4 ( \D a4 \D c4 \D b4 ) \D a8 (
      [ \D fis8 ] \D g4 ) \D e'4 ( \D d4 \D c4 \D b4 ) \D a4 ( \D b8 [ \D g8 ) ]
      \break \D d'2 \D g,4. ( \D a8 \D b4 \D a4 ) \D c4 ( \D b4 \D a8 [ \D fis8
      ] \D g4 ) \D e'4 ( \D d4 \D c4 \D b4 ) \D a4 ( \D b8 [ \D g8 ) ] \break \D
      d'2 \D a4 ( \D b4 ) \D a8 ( [ \D fis8 ) ] \D d4 \D c'4 ( \D b4 ) \D a8 ( [
      \D fis8 ) ] \D d4 \D d'4 ( \D c4 ) \break \D b4. \D b8 \D cis4 \D cis8 ( [
      \D d8 ) ] \D d2 \D g4. ( \D fis8 \D fis8 [ \D e8 ] \D d4 ) \D e4. ( \D d8
      \pageBreak \D d8 [ \D c8 ] \D b4 ) \D a4. ( _\fz \D b16 [ \D c16 ) ] \D d8
      ( [ \D e8 \D c8 \D a8 ) ] \D g4 ( \slashed { \U b8 \=2( } {} \D a8. \=2) [
      \D g16 ) ] \D g8 ( [ \D a16 \D b16 ] \D c16 [ \D d16 \D e16 \D fis16 ) ]
      \D g4. ( \D fis8 \break \D fis8 [ \D e8 ] \D d4 ) \D e4. ( \D d8 \D d8 [
      \D c8 ] \D b4 ) \D a4. ( _\fz \D b16 [ \D c16 ) ] \D d8 ( [ \D e8 \D c8 \D
      a8 ) ] \D g4 ( \slashed { \U b8 \=2( } {} \D a8. \=2) [ \D g16 ) ] \D g4
      \U g,4 \bar "||"
      \break \time 2/2 r2 R1 | % 61
      R1 | % 62
      R1 | % 63
      R1 | % 64
      \break R1 | % 65
      R1 | % 66
      R1 | % 67
      r2 r8 \D d''8 ( _\p \D c16 [ \D b16 \D a16 \D g16 ) ] \pageBreak \D d4 r16
      \D d16 ( [ \D fis16 \D a16 ) ] \D d8 ( [ \D dis8 \D e8 \D cis8 ) ] \D d!4.
      \D c!4 \D b4 \D a8 ~ \D a8 [ \D d,8 \D g8 \D fis8 ] \U e8 [ \U es8 \U es,!8
      \U es'8 ] \D d4 \U d,4 r2 \break r2 \D a''8 ( [ \D gis8 \D g8 \D fis8 ) ]
      \D e8 ( [ \D e'8 \D dis8 \D d8 ) ] \D cis4 \D c4 \D b8 ( [ \D gis8 \D a8
      \D c,8 ) ] \D d2 \D g!4 r4 r2 \break r2 \D a8 ( [ \D gis8 \D g8 \D fis8 )
      ] \D e8 ( [ \D e'8 \D dis8 \D d8 ) ] \D cis4 \D c4 \D b8 ( [ \D gis8 \D a8
      \D c,8 ] \D d2 ) \D g!4 \U g,4 \bar "||"
      \break \time 2/2 \D e'2 ( _\p \D d2 \D dis4 \D e4 ) \U b4 ( \D e4 \U c4 \D
      g'4 ) \D a4 ( \D g4 ) \D c4 ( \D cis4 ) \D d4 \D d,4 \D e'2 ( _\p \D d2 \D
      dis4 \D e4 ) \D b4 ( \D e4 ) \D c4 ( \D g'4 \pageBreak \D a4 \D g4 ) \D c,4
      ( \D cis4 ) d1 ~ d1 ~ d1 ~ d1 \break \clef "tenor" \D d4 ( \D e16 [ \D fis16
      \D g16 \D a16 ) ] \D b8 ( [ \D a8 \D g8 ) \D g8 ] \D g2 \clef "bass" \D c,4
      ( \D b4 ) \D a4 \D e'8 ( [ \D d8 ] \D cis4 \D c4 ) \D b4 ( \D c4 \D d4 )
      \D d,4 \break \D g4 r4 r2 r2 \D ais8 ( [ \D b8 \D c8 \D gis8 ) ] \D a!8 (
      [ \D dis,8 \D e8 \D d8 ) ] \U cis8 ( [ \U a8 \U c8 \U d,8 ) ] \U b'8 ( [
      \U gis8 \U a8 \U c8 ) ] \D d2 \break g1 ~ g1 ~ _\pp \D g2 ~ \U g8 [ \U g,8
      ( -. \U g'8 \U g,8 -. \U g'8 \U g,8 ) -. ] \U g'8 g,1 ^\fermata _\< \after
      2 _\> \after 2 \! g'1 <>\! g,1 ^\fermata _\pp g'1 \bar "|."
      \pageBreak \time 3/4 \key c \major r4 R2. | % 1
      \D c4 -. _\f \D c4 -. r4 \D f,4 -. \D f4 -. r4 \U b,4 \U b4 \U b4 \U c2 r4
      r4 r4 \D a'4 \D gis4 ( \D a4 ) \D c4 -. \D fis,4 ( \D g!4 ) \D b4 -. \D c4
      ( \D b4 \D c4 ) \break \D d4 ( \D c4 \D a4 ) \D d2 \D d,4 \D g4 -. \D g4
      -. \D g4 -. \D g4 -. \D g4 -. \D g4 -. \D g4 -. \D g4 -. \D g4 -. \D g4 -.
      \D g4 -. \D g4 -. \D g2 \U fis,16 ( [ \U g8. ) ] \U ais16 ( [ \U b8. ) ]
      \U cis16 ( [ \U d8. ) ] \D fis16 ( [ \D g8. ) ] \break \D b2 r4 \D d,2. (
      \D g4 ) r4 }
    \repeat volta 2 {
      r4 r4 r4 \D g4 _\f \D as4 ( \D g4 ) \D es4 \D c'2 \D d,4 \D b'!2 \U c,4 \D
      as'2. \D g2 r4 r4 r4 \U g,4 _\p \break \U fis4 ( \U g4 ) r4 r4 r4 \U g4 \U
      fis4 ( \U g4 ) r4 r4 r4 \U g4 \U as4 ( \U g4 ) r4 R2. | % 33
      \D c'4 -. _\f \D c4 -. r4 \D f,4 -. \D f4 -. r4 \U b,4 -. \U b4 -. \U b4
      -. \U c2 \D c'4 \break \D b4 ( \D c4 \D e4 ) \D g,2 \D d'4 \D cis4 ( \D d4
      \D f4 ) \D a,2 r4 r4 r4 \D d4 \D cis4 ( \D d4 \D f4 ) \D b,4 ( \D c!4 ) \D
      e,4 \D f4 ( \D e4 \D f4 ) \D g4 ( \D f4 \D d4 ) \D g2. \pageBreak \U c,4
      -. \U c4 -. \U c4 -. \U c4 -. \U c4 -. \U c4 -. \U c4 -. \U c4 -. \U c4 -.
      \U c4 -. \U c4 -. \U c4 -. \U c2 \U b16 ( [ \U c8. ) ] \D dis16 ( [ \D e8.
      ) ] \D fis16 ( [ \D g8. ) ] \D b16 ( [ \D c8. ) ] \D e2 r4 \U g,,2. ( \U c4
      ) r4 ^\fermata }
    \break \repeat volta 2 {
      \time 3/4 r4 R2. | % 57
      R2. | % 58
      \D e2. ( _\p \U a,4 ) r4 r4 R2. | % 61
      R2. | % 62
      \U b2. ( \U e,4 ) r4 }
    \repeat volta 2 {
      r4 R2. | % 65
      R2. | % 66
      \break \U cis'2. ( \break \D d2 ) r4 r4 r4 \U d,4 _\f \D d'2. \U c2. \U f,2.
      \U e2. ~ \U e2. ~ \U e2. ~ \U e2 ^\fermata r4 \D a'2. _\pp R2. | % 78
      \break \D gis2. R2. | % 80
      \D a2. \D d,2. \D e2. ~ \D e4 ( \D d4 \U b4 ) \U a4 r4 r4 R2. | % 86
      \U gis4 r4 r4 R2. | % 88
      \U cis,2. ( \pageBreak \U d2. \U e2. ) \U a4 r4 r4 R2. | % 93
      R2. | % 94
      \D e'2. ( _\p \U a,4 ) r4 r4 R2. | % 97
      \D d2 ( \D dis4 ) \D e2. ( \U a,4 ) r4 }
    \pageBreak \time 2/2 \key es \major \U c,4 _\f \U c'4 r4 \U c,4 \U c'4 r4 \U
    c,4 \U c'4 r4 r4 \D es'4 _\p \D f2 ( \D es4 ) r4 R1 | % 4
    \D es,4 _\f r4 \D e4 r4 \D f4 r4 r2 R1 | % 7
    \break R1 | % 8
    r2 r4 \D es4 _\p f1 g1 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U c,,8 [ _\f \U es8 \U g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U c8 [ \U b8 \U c8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U c,8 [ \U f8 \U as8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U c8 [ \U b8 \U c8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U c,8 [ \U es8 \U f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g8 [ \U a8 \U b8 ] }
    \U c4 r4 \break c'1 ~ \D c2. r4 R1 | % 16
    R1 | % 17
    \break R1 | % 18
    \tweak TupletBracket.stencil ##f \tweak TupletBracket.direction #UP \tuplet 3/2
    {
      \U g,8 [ _\f \U b8 \U d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D fis8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U g,8 [ \U c8 \U es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D g8 [ \D fis8 \D g8 ] }
    \U g,4 r4 r2 R1 | % 21
    \pageBreak r2 r4 \D as'4 \D g2 ( \D as4 \D bes4 ) \D c2 ( \D bes2 ) \D as2 (
    \D g4 \D f4 ) \D e2 ( _\fz \D f4 \D g4 ) \D as!2 ( \D a2 ) bes1 ~ bes1 ~ _\p
    bes1 ~ \break bes1 ~ bes1 ~ \D bes2 ( \D es,4 ) r4 r2 r4 \U es,4 \U d2 ( \U
    es4 ) r4 r2 r4 \U es4 \break \U d2 ( \U es4 ) r4 r2 r4 \D as'4 \D g2 ( \D as4
    \D bes4 ) \D c2 ( \D bes2 ) \D as2 ( \D g2 ) \D f4 r4 r4 \U es,4 \break \U d2
    ( \U es4 \U f4 ) \U g2 ( \U as2 \U bes2 ) \D bes'2 \D es,4 _\f r4 \D f4 -. r4
    \D g4 -. r4 r2 \break \U as,4 -. r4 \U a4 -. r4 \U bes4 -. r4 r2 bes1 _\fz
    \pageBreak bes1 _\fz \D es4 -. r4 \D es4 -. r4 \D es4 -. r4 r2 \break R1 | % 54
    R1 | % 55
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D d8 [ \D d8 \D d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D es8 \D es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D d8 [ \D d8 \D d8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D es8 \D es8 ] }
    \break \U as,4 r4 \U bes4 r4 es,1 ( es1 as1 es1 g1 \break es1 ) as1 \tweak
    TupletBracket.stencil ##f \tuplet 3/2 {
      \D des8 [ \D es8 \D f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D des8 \D c8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U bes8 [ \U as8 \U g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U f8 [ \U es8 \U des!8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U c8 [ \U es8 \U as8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U c8 [ \U b8 \U c8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U d,!8 [ \U f8 \U bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D d!8 [ \D d8 \D d8 ] }
    \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U es,8 [ \U g8 \U bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D es8 [ \D es8 \D es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \U as,8 [ \U c8 \U es8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D as8 [ \D as8 \D as8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D bes,8 [ \D es8 \D g8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D bes8 [ \D bes8 \D bes8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D bes,8 [ \D d8 \D f8 ] }
    \tweak TupletBracket.stencil ##f \tuplet 3/2 {
      \D bes8 [ \D bes8 \D bes8 ] }
    es,1 ~ \pageBreak es1 es,1 ~ es1 ~ \break es1 ~ \U es4 r4 \U es4 -. r4 \U es4
    -. r4 r2 }
  \U es4 -. r4 r2 r2 r4 \D as'4 _\f \D g2 ( \D as4 \D bes4 ) \D c4 r4 r4 \D bes4
  \break \D as4 ( \D g4 \D f4 \D es4 ) \D d4 ( \D d'4 \D es4 \D es,4 ) \D as2 (
  \D a2 ) bes1 r2 r4 \U d,,4 \U es2 ( \U d4 ) r4 r2 r4 \U d4 \U es2 ( \U d4 ) \D
  es'4 _\f \break \D d2 ( \D es4 \D f4 ) \D g2 ( \D f4 ) \U bes,4 \U es,2 ( \U f4
  \U g4 ) \U as2 ( \D es'4 ) r4 \break R1 | % 88
  R1 | % 89

  \barNumberCheck #90
  R1 | % 90
  r2 r4 \U as,4 \U g2 ( \U a4 \U b4 ) \pageBreak \U c2 r2 R1 | % 94
  R1 | % 95
  r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes!8 [ \U a8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c8 [ \U bes8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d8 [ \U c8 \U d8 ] }
  \break \D es4 \U es,8 ( [ \U es'8 ) ] \D des4 \U des,!8 ( [ \U des'8 ) ] \U c4
  \U c,8 ( [ \U c'8 ) ] \U g4 \U g'8 ( [ \U g,8 ) ] as1 ~ as1 ~ \break as1 ~ as1
  ~ \U as4 r4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U es'8 \U g,8 \U es'8 \U g,8 ] }
  \U es'8*2/3 \break \U as,4 \U es'4 r4 r4 \tweak TupletBracket.stencil ##f
  \tuplet 3/2 {
    \U g,8 [ \U es'8 \U g,8 \U es'8 \U g,8 ] }
  \U es'8*2/3 \U as,4 \U es'4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as,8 [ \U bes8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U as8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f8 [ \U g8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U f8 \U es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d!8 [ \U es8 \U f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U as8 \U a8 ] }
  \break \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U bes8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U bes8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U bes8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U bes8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U bes8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U bes8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U bes8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U bes8 [ \U bes8 \U bes8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U b8 [ \U b8 \U b8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U b8 [ \U b8 \U b8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U b8 [ \U b8 \U b8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U b8 [ \U b8 \U b8 ] }
  \pageBreak \U c4 r4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g'8 [ \D g8 \D g8 ] }
  \U c,4 r4 r4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g'8 [ \D g8 \D g8 ] }
  \U c,4 r4 r2 \break r2 r4 \U c4 -. \D f4 -. \U c4 -. \D f4 -. r4 r2 r4 \U bes,4
  -. \D es4 -. \U bes4 -. \D es4 -. \U g,4 ( \break \D g'4 ) \U g,4 ( \D g'4 )
  \U g,4 ( \D g'4 ) \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U f,8 [ \U g8 \U f8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U es8 [ \U f8 \U es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d8 [ \U es8 \U d8 ] }
  \U c4 -. \U c'4 r4 \U c,4 -. \U c'4 r4 \U c,4 -. \U c'4 r4 r4 \D es'4 -. _\p
  \D f2 ( \D es4 ) r4 | % 121
  R1 | % 122
  \break \D es,4 -. _\f r4 \D e4 -. r4 | % 123
  \D f4 -. r4 r2 | % 124
  R1 | % 125
  R1 | % 126
  r2 r4 \D es4 _\p | % 127
  f1 ( | % 128
  g1 ) | % 129

  \barNumberCheck #130
  R1 | % 130
  \pageBreak f1 ( _\p | % 131
  g1 ) | % 132
  R1 | % 133
  f,1 ( _\pp | % 134
  ges1 | % 135
  as1 ) | % 136
  des,1 _\f \break | % 137
  des1 _\fz | % 138
  \D des'2 ( \U ces2 ) | % 139

  \barNumberCheck #140
  bes1 \break | % 140
  es,1 | % 141
  es1 _\fz | % 142
  \D es'2 ( \D des2 ) \break | % 143
  c1 | % 144
  \U f,4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D f'8 ( [ \D e8 \D f8 ) ] }
  \U f,4 -. \D f'4 -. | % 145
  \U e,4 -. \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D e'!8 ( [ \D d!8 \D e8 ) ] }
  \U e,4 -. \D e'4 -. \pageBreak | % 146
  \U es,!4 \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D es'!8 ( [ \D d8 \D es8 ) ] }
  \U es,4 \D es'4 | % 147
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D b8 [ \D d8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c,8 [ \D es8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis8 \D g8 ] }
  | % 148
  \U g,4 r4 r2 \break | % 149

  \barNumberCheck #150
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g8 [ \U b8 \U d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis8 \D g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U g,8 [ \U c8 \U es8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D fis8 \D g8 ] }
  | % 150
  \U g,4 r4 r4 ^\fermata \bar "||"
  \key c \major \D c'4 _\p | % 151
  \D d2 ( \D c4 ) \D b4 | % 152
  \D c2 ( \D g4 ) r4 | % 153
  r2 r4 \D d'4 | % 154
  \D e2 ( \D d4 ) \D cis4 \break | % 155
  \D d2 ( \D a4 ) r4 | % 156
  R1 | % 157
  r2 r4 \D d4 _\f | % 158
  \D cis2 ( \D d4 ) r4 | % 159

  \barNumberCheck #160
  \D g,2 ( \D c!4 ) r4 | % 160
  \D g2 ( \D c4 ) r4 | % 161
  R1 | % 162
  r2 r4 \U c,4 \break | % 163
  \U b2 ( \U c4 ) r4 | % 164
  r2 r4 \U c4 | % 165
  \U b2 ( \U c4 ) r4 | % 166
  r2 r4 \D f'4 | % 167
  \D e2 ( \D f4 \D g4 ) | % 168
  \D a2 ( \D g2 | % 169

  \barNumberCheck #170
  \D f2 \D e2 ) \pageBreak | % 170
  \D d4 r4 r4 \U c,4 | % 171
  \U b2 ( \U c4 \D d4 ) | % 172
  \D e2 \D f2 | % 173
  \D g2 \U g,2 | % 174
  c1 ( \break | % 175
  c1 f1 | % 176
  c1 e1 | % 177
  c1 ) f1 | % 178
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D bes8 [ \D c8 \D d8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D c8 [ \D bes8 \D a8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \D g8 [ \D f8 \D e8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U d8 [ \U c8 \U bes!8 ] }
  \break | % 179

  \barNumberCheck #180
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U a8 [ \U a8 \U a8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U a8 [ \U a8 \U a8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as8 [ \U as8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U as8 [ \U as8 \U as8 ] }
  | % 180
  \U g4 r4 \U g4 r4 | % 181
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U e8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c8 [ \U b8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U e8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c8 [ \U b8 \U c8 ] }
  | % 182
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U f8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c8 [ \U b8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U c'8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U c'8 \U c8 ] }
  \break | % 183
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U e8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c8 [ \U b8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U e8 \U g8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c8 [ \U b8 \U c8 ] }
  | % 184
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U f8 \U as8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c8 [ \U b8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U c'8 \U c8 ] }
  \tweak TupletBracket.stencil ##f \tuplet 3/2 {
    \U c,8 [ \U c'8 \U c8 ] }
  | % 185
  \U c,4 -. r4 \U c4 -. \U c'4 r4 | % 186
  \U c,4 -. \U c'4 r4 \U c,4. \U c'4. \U c,8 \U c'8 | % 187
  \U c,4 -. \U c'4 r4 r2 \bar "|."
}

PartPFourVoiceTwo = \relative a {
  \repeat volta 2 {
    \repeat volta 2 {
      \repeat volta 2 {
        \clef "bass" \time 4/4 \key c \major \partial 8 s8*33 \break s1*3 \break
        s1*2 \break s1*2 \pageBreak s1*4 \break s1*3 \break s1*2 \break s1*3
        \break s1*3 \pageBreak s1*2 \break s1*2 \break s1*3 \break s1*4 \break
        s1*2 \pageBreak s1*2 \break s1*3 \break s8*15 }
      \repeat volta 2 {
        \break s8*9 \break s1*3 \pageBreak s1*4 \break s1*4 \break s1*3 \break
        s1*2 \break s1*3 \pageBreak s1*2 \break s1*2 \break s1*2 \break s1*3
        \break s1*4 \pageBreak s1*4 \break s1*3 \break s1*2 \break s1*2 \break
        s1*2 \pageBreak s1*2 \break s1*3 \break s1*3 \break s1*3 \break s1*4
        \pageBreak s1*7 \break s1*3 \break s1*3 \break s1*2 }
      \bar "|."
      \pageBreak \time 2/2 \key g \major s1*5 \break s1*7 \break s2*13 \bar "||"
      \break \time 2/2 s2*5 \pageBreak s1*3 \break s1*3 \break s1*3 \break s1*3
      \break s1*3 \pageBreak s2*5 \bar "||"
      \break \time 4/4 s2*5 | % 42
      \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
      ##t a8 ^\turn s4 \break s1*3 | % 46
      \hideNote r2 \hideNote r8 \tweak Stem.transparent ##t \tweak transparent
      ##t a8 ^\turn s4 \break s1*3 \break s1*3 \pageBreak s1*3 \break s2*7 \bar
      "||"
      \break \time 2/2 s2*9 \break s1*4 \pageBreak s1*4 \break s1*4 \break s2*7
      \bar "||"
      \break \time 2/2 s2*13 \pageBreak s1*5 \break | % 91
      \clef "tenor" s1. \clef "bass" s2*5 \break s1*4 \break s1*5 \bar "|."
      \pageBreak \time 3/4 \key c \major s2*13 \break s1*6 \break s1*2 }
    \repeat volta 2 {
      s2*11 \break s2*15 \break s2*15 \pageBreak s2*13 }
    \break \repeat volta 2 {
      \time 3/4 s1*6 }
    \repeat volta 2 {
      s4*7 \break s2. \break s4*33 \break s4*33 \pageBreak s1*8 }
    s4 \pageBreak \time 2/2 \key es \major s1*7 \break s1*6 \break s1*4 \break
    s1*4 \pageBreak s1*9 \break s1*6 \break s1*6 \break s1*5 \break s1*3
    \pageBreak s1*3 \break s1*3 \break s1*4 \break s1*3 \break s1*3 \pageBreak
    s1*3 \break s1*3 }
  s1*3 \break s1*8 \break s1*4 \break s1*5 \pageBreak s1*4 \break s1*4 \break
  s1*3 \break s1*3 \break s1*3 \pageBreak s1*3 \break s1*4 \break s1*6 \break
  s1*8 \pageBreak s1*7 \break s1*3 \break s1*3 \break s1*3 \pageBreak s1*3
  \break s4*7 \bar "||"
  \key c \major s4*17 \break s1*8 \break s1*7 \pageBreak s1*5 \break s1*4 \break
  s1*4 \break s1*5 \bar "|."
}


% The score definition
\score {
  <<
    \new StaffGroup <<
      \new Staff = "P1" <<
        \set Staff.instrumentName = "Violin 1"
        \context Staff <<
          \mergeDifferentlyDottedOn
          \mergeDifferentlyHeadedOn
          \context Voice = "PartPOneVoiceOne" {
            \voiceOne \PartPOneVoiceOne
          }
          \context Voice = "PartPOneVoiceTwo" {
            \voiceTwo \PartPOneVoiceTwo
          }
        >>
      >>
      \new Staff = "P2" <<
        \set Staff.instrumentName = "Violin 2"
        \context Staff <<
          \mergeDifferentlyDottedOn
          \mergeDifferentlyHeadedOn
          \context Voice = "PartPTwoVoiceOne" {
            \voiceOne \PartPTwoVoiceOne
          }
          \context Voice = "PartPTwoVoiceTwo" {
            \voiceTwo \PartPTwoVoiceTwo
          }
        >>
      >>
      \new Staff = "P3" <<
        \set Staff.instrumentName = "Viola"
        \context Staff <<
          \mergeDifferentlyDottedOn
          \mergeDifferentlyHeadedOn
          \context Voice = "PartPThreeVoiceOne" {
            \voiceOne \PartPThreeVoiceOne
          }
          \context Voice = "PartPThreeVoiceTwo" {
            \voiceTwo \PartPThreeVoiceTwo
          }
        >>
      >>
      \new Staff = "P4" <<
        \set Staff.instrumentName = "Violoncello"
        \context Staff <<
          \override Staff.BarLine.allow-span-bar = ##f
          \mergeDifferentlyDottedOn
          \mergeDifferentlyHeadedOn
          \context Voice = "PartPFourVoiceOne" {
            \voiceOne \PartPFourVoiceOne
          }
          \context Voice = "PartPFourVoiceTwo" {
            \voiceTwo \PartPFourVoiceTwo
          }
        >>
      >>
    >>
  >>
  \layout {}
  % To create MIDI output, uncomment the following line:
  % \midi { \tempo 4 = 112 }
}

