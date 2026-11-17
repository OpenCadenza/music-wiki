\version "2.26.0"
\language "english"

\header {
  title = "Symphony No. 5 in C minor, Op. 67"
  subtitle = "II. Andante con moto — mm. 205–209（摘录：大管主题变体）"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

% 摘录说明：本段为 Coda（m.205 起）中大管在 p / dolce 下奏出的主题变体；
% 一/二小提琴与中提琴的带休止反复跳音和弦、低音弦乐的弱拍点状短音在源工程中
% 与三连音、双声部交织，本轮只交付大管主题变体（音符按 Mutopia Symphony5_2
% 工程 MIDI 精确定位，3/8 拍、A♭ 大调）。弦乐层待下一轮补齐或不交付。

global = {
  \key af \major
  \time 3/8
  \tempo "Andante con moto" 4. = 92
}

fagotto = {
  \global
  \clef bass
  \set Staff.midiInstrument = "bassoon"
  % m.205
  r4 c'16 ds'16 |
  % m.206
  fs'8 fs'16 f'16 ds'16 fs'16 |
  % m.207
  f'4 cs'16 ds'16 |
  % m.208
  e'8 e'16 ds'16 cs'16 e'16 |
  % m.209
  ds'4 r8 |
}

\score {
  <<
    \new Staff \with { instrumentName = "Fagotto" } \fagotto
  >>
  \layout { }
  \midi { }
}
