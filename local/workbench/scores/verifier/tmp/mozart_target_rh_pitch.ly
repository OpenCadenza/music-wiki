\version "2.26.0"
\language "english"

% 核验辅助：被测文件 Mozart K.283 I 右手声部（原样式复制，仅用于 \displayLilyMusic 取绝对音高）
global = {
  \key g \major
  \time 3/4
}

rightHand = \relative c'' {
  \global
  \clef treble
  \partial 4 d8.(\p b16) |
  d4 r4 g,4 |
  fs4 r4 a'8.( fs16) |
  a4 r4 c,4 |
  b4 r4 g'8.(\f fs16) |
  fs8( e8) e4 g8.( e16) |
  e8( d8) d4 g8.( d16) |
  d4-.\p d4-. d4-. |
  d16( e fs g a b c d c b a g) |
  fs16( e d c b d b g a c a fs) |
  g4 r4 \bar "||"
}

\displayLilyMusic \rightHand
