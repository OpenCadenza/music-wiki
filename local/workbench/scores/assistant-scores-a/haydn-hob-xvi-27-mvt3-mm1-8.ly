\version "2.26.0"
\language "english"

\header {
  title = "Keyboard Sonata No. 42 in G Major, Hob. XVI:27"
  subtitle = "III. Presto (mm. 1–8)"
  composer = "Franz Joseph Haydn"
  tagline = ##f
}

% 依据 Mutopia 原版工程 (Mutopia-2007/11/04-1097, ed. Maurizio Tomasi) 重编码
% 对应原文件：hob-xvi-27-iii-presto.ly 右手第 34–44 行、左手第 256–267 行
% 修正记录：
% 1. 右手基准设为 \relative c'，弱起为 D4 (MIDI 62)，旋律处于 G4–B5 正常音区（修正原交付件高八度偏差）；
% 2. 左手第 5 小节转入高音谱表后设为 g''4 (MIDI 67 / G4)，修正原交付件单撇 g' 导致低八度的问题。

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
  d4\mordent r8 \bar "||"
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

\score {
  \new PianoStaff \with {
    instrumentName = "Piano"
    midiInstrument = "acoustic grand"
  } <<
    \new Staff = "upper" { \rightHand }
    \new Staff = "lower" { \leftHand }
  >>
  \layout { }
  \midi { }
}
