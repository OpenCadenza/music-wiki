\version "2.26.0"
\language "english"

% 核验辅助：被测文件左手声部（原样式复制）
global = {
  \key g \major
  \time 2/4
}

leftHand = \relative c' {
  \global
  \clef bass
  \partial 8 r8 |
  <g b>4 r8 <b d>8 |
  <a c>4 r4 |
  r4 r8 fs8 |
  g4 g,8 r8 |
  \clef treble
  g''4 r8 g8 |
  fs4 r8 fs8 |
  g4 a4 |
  \clef bass
  d,4 d,8 \bar "||"
}

\displayLilyMusic \leftHand
