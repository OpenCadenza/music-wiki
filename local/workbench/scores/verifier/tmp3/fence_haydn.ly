\version "2.26.0"
\language "english"

\header {
  title = "String Quartet in G major, Hob. III:66 (Op. 64 No. 4)"
  subtitle = "II. Menuetto (Allegretto) — mm. 1–8, with upbeat"
  location = "mm. 1–8 (with anacrusis)"
  composer = "Joseph Haydn"
  tagline = ##f
}

% 编制与 GM 程序号:
% Violin I: 40 (violin), Violin II: 40 (violin), Viola: 41 (viola), Violoncello: 42 (cello)
% 调性与拍号：G 大调 (\key g \major), 3/4 拍 (\time 3/4)
% 结构：混合乐段类型 2（先行句 mm. 1–4 弱半终止 + 扩充终止进行 ECP mm. 5–8 强正格终止）

global = {
  \key g \major
  \time 3/4
  \tempo "Allegretto" 4 = 130
}

violinOne = {
  \global
  \clef treble
  \partial 4
  d''8(\f b'8) |
  fs'8( g'8) d'4-. b''8( g''8) |
  fs''8( a''8) c''4-. a'8( c''8) |
  c''16( b'16) r8 d''16( c''16) r8 e''16( c''16) r8 |
  a'2 d'4\p |
  g'2( b'8 gs'8) |
  b'8( a'8) c''4-. c''8( b'8) |
  \grace b'16 a'4( a'8 g'8 a'8 d'8) |
  g'4 r2 |
  \bar "||"
}

violinTwo = {
  \global
  \clef treble
  \partial 4
  r4 |
  r4 d'4-.\f d'4-. |
  r4 fs'4-. fs'4-. |
  g'8-. r8 g'8-. r8 g'8-. r8 |
  fs'2 r4 |
  r4 d'4-.\p d'4-. |
  e'4 r4 e'8( d'8) |
  c'2. |
  b4 r2 |
  \bar "||"
}

viola = {
  \global
  \clef alto
  \partial 4
  r4 |
  r4 b4-.\f b4-. |
  r4 a4-. a4-. |
  g8-. r8 e8-. r8 c8-. r8 |
  d4-. r4 r4 |
  r4 g4-.\p f'4-. |
  e'4 r4 r4 |
  fs'2. |
  g'4 r2 |
  \bar "||"
}

violoncello = {
  \global
  \clef bass
  \partial 4
  r4 |
  r4 g4-.\f g4-. |
  r4 d4-. d4-. |
  g8-. r8 e8-. r8 c8-. r8 |
  d4-. d'4-. r4 |
  r4 b,4-.\p b,4-. |
  c4 r4 r4 |
  d4-. d4-. d4-. |
  g,4-. g4-. r4 |
  \bar "||"
}

\score {
  \new StaffGroup <<
    \new Staff \with {
      instrumentName = "Violin I"
      midiInstrument = "violin"
    } { \violinOne }

    \new Staff \with {
      instrumentName = "Violin II"
      midiInstrument = "violin"
    } { \violinTwo }

    \new Staff \with {
      instrumentName = "Viola"
      midiInstrument = "viola"
    } { \viola }

    \new Staff \with {
      instrumentName = "Violoncello"
      midiInstrument = "cello"
    } { \violoncello }
  >>
  \layout { }
  \midi { }
}
