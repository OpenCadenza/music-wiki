\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 2 in G Major, Op. 18, No. 2"
  subtitle = "IV. Allegro molto quasi presto (mm. 1–8)"
  location = "mm. 1–8"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% 编制与 GM 程序号:
% Violin I: 40 (violin), Violin II: 40 (violin), Viola: 41 (viola), Violoncello: 42 (cello)
% 调性与拍号：G 大调 (\key g \major), 2/4 拍 (\time 2/4)
% 结构：混合乐段类型 4（CBI mm. 1–4 大提琴独奏无终止 + 后继句 mm. 5–8 全奏正格终止收束）

global = {
  \key g \major
  \time 2/4
  \tempo "Allegro molto quasi presto" 4 = 192
}

violinOne = {
  \global
  \clef treble
  R2 |
  R2 |
  R2 |
  R2 |
  d'4-.\p g'4-. |
  b'4.( a'16 g') |
  fs'8-. a'8-. g'8-. e'8-. |
  d'8 r8 r4 | \bar "||"
}

violinTwo = {
  \global
  \clef treble
  R2 |
  R2 |
  R2 |
  R2 |
  b4-.\p d'4-. |
  g'4.( fs'16 e') |
  d'8-. d'8-. cs'8-. cs'8-. |
  d'8 r8 r4 | \bar "||"
}

viola = {
  \global
  \clef alto
  R2 |
  R2 |
  R2 |
  R2 |
  b4-.\p b4-. |
  g4.( a16 b) |
  a8-. fs8-. e8-. g8-. |
  fs8 r8 r4 | \bar "||"
}

cello = {
  \global
  \clef bass
  d4-.\p g4-. |
  b4.( a16 g) |
  fs8-. g8-. a8-. b8-. |
  c'8 r8 r4 |
  g4-.\p g4-. |
  e4.( fs16 g) |
  a8-. a,8-. a,8-. a,8-. |
  d8 r8 r4 | \bar "||"
}


\displayLilyMusic \violinOne
\displayLilyMusic \violinTwo
\displayLilyMusic \viola
\displayLilyMusic \cello
