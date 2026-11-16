\version "2.26.0"
\language "english"

% 核验辅助：把被测文件中的相对音高定义原样复制，然后用 \displayLilyMusic
% 让 LilyPond 自己把 \relative 转成绝对音高，避免人工推算八度。
% 本文件仅用于核验，不修改被测文件。

global = {
  \key g \major
  \time 2/4
  \tempo "Presto" 4 = 132
}

rightHand = \relative c' {
  \global
  \clef treble
  \partial 8 d8 |
  g8( b8 d8 g,8) |
  g4( fs8) d8 |
  a'8( c8 e8 <a, c>8) |
  <a c>4( <g b>8 b8) |
  b'8( g8 ds8 e8) |
  a8( fs8 cs8 d!8) |
  e8( g4) cs,8 |
  d4 r8 \bar "||"
}

\displayLilyMusic \rightHand
