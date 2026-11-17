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
% 与三连音、双声部交织，本轮只交付大管主题变体（3/8 拍、A♭ 大调、5 小节 m.205–209）。
% 弦乐层待下一轮补齐或不交付。
%
% 音高与拼写依据：Mutopia `Symphony5_2` 工程分谱
%   downloads\op67-2\Symphony5_2-lys\fagotti.ly 第 72–73 行（tenor 谱号）
% 逐音为  c'16 ees'16 | ges'8 ges'16 f'16 ees'16 ges'16 | f'4 des'16 ees'16 |
%         fes'8 fes'16 ees'16 des'16 fes'16 | ees'4
% 注意：A♭ 大调（4 降）下必须按调性拼写为降号（E♭ / G♭ / D♭ / F♭），
% 不能沿用“按 MIDI 音高反查”得到的升号等音异名（D♯ / F♯ / C♯ / E）——MIDI 里没有
% 拼写信息，反查必然丢升降号。谱号亦按底本用 tenor（原谱此处即次中音谱号）。

global = {
  \key af \major
  \time 3/8
  \tempo "Andante con moto" 4. = 92
}

fagotto = {
  \global
  \clef tenor
  \set Staff.midiInstrument = "bassoon"
  % m.205  r4 c'16 ees'16
  r4 c'16 ef'16 |
  % m.206  ges'8 ges'16 f'16 ees'16 ges'16
  gf'8 gf'16 f'16 ef'16 gf'16 |
  % m.207  f'4 des'16 ees'16
  f'4 df'16 ef'16 |
  % m.208  fes'8 fes'16 ees'16 des'16 fes'16
  ff'8 ff'16 ef'16 df'16 ff'16 |
  % m.209  ees'4
  ef'4 r8 |
}

\score {
  <<
    \new Staff \with { instrumentName = "Fagotto" } \fagotto
  >>
  \layout { }
  \midi { }
}
