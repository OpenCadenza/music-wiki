\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 19 in C major, K. 465 “Dissonance”"
  subtitle = "IV. Allegro molto — mm. 10–16"
  composer = "Wolfgang Amadeus Mozart (1756–1791)"
  tagline = ##f
}

% 谱源：OpenScore StringQuartets（sq7471661.mxl，CC0）；用 musicxml2ly 与
% MusicXML 直接解析（measure number 显式，弱起为 number 0）取得音高/时值。
% 与先前 musicxml2ly 的 .ly 文本交叉核对；m.15 的 16 分音为倚音（grace note）。

global = {
  \key c \major
  \time 2/4
  \tempo "Allegro" 4 = 144
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.10
  b''4. f''8 |
  % m.11
  e''8 c''8 a'8 d''8 |
  % m.12
  c''8 b'8 c''8 c''8 |
  % m.13
  d''8 d''8 e''8 e''8 |
  % m.14
  f''8 f''8 fs''8 f''8 |
  % m.15
  g''8 e''8 \grace { g''16 } f''8 e''16 d''16 |
  % m.16
  c''8 r8 c'8 c'8 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.10
  f'16 d'16 f'16 d'16 f'8 r8 |
  % m.11
  r8 g'8 c'8 a'8 |
  % m.12
  e'8 d'8 c'8 c'8 |
  % m.13
  c'8 c'8 c'8 c'8 |
  % m.14
  c''8 c''8 c''8 c''8 |
  % m.15
  c''4 \grace { e''16 } d''8 c''16 b'16 |
  % m.16
  c''8 r8 c'8 c'8 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.10
  d'16 b16 d'16 b16 d'8 r8 |
  % m.11
  R2 |
  % m.12
  r4 g8 g8 |
  % m.13
  a8 a8 bf8 bf8 |
  % m.14
  c'8 c'8 d'8 d'8 |
  % m.15
  e'8 c'8 g'8 g'8 |
  % m.16
  e'8 r8 c'8 c'8 |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  % m.10
  g8 g8 g8 r8 |
  % m.11
  c'8 e8 f8 fs8 |
  % m.12
  g8 f8 e8 e8 |
  % m.13
  f8 f8 g8 g8 |
  % m.14
  a8 a8 af8 af8 |
  % m.15
  g8 g8 g8 g8 |
  % m.16
  c8 r8 c8 c8 |
}

\score {
  <<
    \new Staff \with { instrumentName = "Violino I" } \violinoI
    \new Staff \with { instrumentName = "Violino II" } \violinoII
    \new Staff \with { instrumentName = "Viola" } \viola
    \new Staff \with { instrumentName = "Violoncello" } \violoncello
  >>
  \layout { }
  \midi { }
}
