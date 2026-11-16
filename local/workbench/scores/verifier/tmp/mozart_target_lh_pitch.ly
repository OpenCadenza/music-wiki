\version "2.26.0"
\language "english"

% 核验辅助：被测文件 Mozart K.283 I 左手声部（原样式复制，仅用于 \displayLilyMusic 取绝对音高）
global = {
  \key g \major
  \time 3/4
}

leftHand = \relative c {
  \global
  \clef bass
  \partial 4 r4 |
  g8(\p b d b d b) |
  a8( c d c d c) |
  fs,8( a d a d a) |
  g8( b d b) g4\f |
  \clef treble
  <c' g'>2\fp r4 |
  <b g'>2\fp r4 |
  \clef bass
  <a c'>4-.\p <g b>4-. <fs a>4-. |
  <g b>4 r4 <e g>4 |
  r4 << { g4 c4 } \\ { d,2 } >> |
  <g b>4 g,4 r4 \bar "||"
}

\displayLilyMusic \leftHand
