\version "2.26.0"
\language "english"

% 莫扎特 第六钢琴奏鸣曲 K.284 (205b) 第一乐章 Allegro，mm.17–24
% 底本：local/resources/scores/source-packages/humdrum/mozart-sonatas/
%       0016-16-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 1.abc
%       （hum2abc 由 Humdrum kern "sonata06-1.krn" 转换，2021-01-14；L:1/16、M:C、K:D）
% 该段为过渡段收束 → 内聚裂隙（MC）→ A 大调副题起句：
%   m.17–20 A 大调分解琶音与十六分音符动力蓄积（左手 A 踏板音，右手和弦+下行音阶）
%   m.21     左手连续三次击槌 A 大调原位和弦（A–C♯–E），第 4 拍拍点双手同时休止
%   m.22     左手整小节休止，右手八分音符旋律（含 G♯）——织体骤然变薄
%   m.23–24  A 大调副题材质展开，左手 G♯–B / E–G 双音伴奏（E 大调属和声）
% 说明：底本在 m.16 末给左手加 [K:clef=treble]，故本片段左手为高音谱号。

global = {
  \key d \major
  \time 4/4
  \tempo "Allegro" 4 = 138
}

upper = {
  \global
  \clef treble
  \set Staff.midiInstrument = "acoustic grand"
  % m.17
  <e'' a'' cs'''>4 r8 a''8-. g''8-. fs''8-. e''8-. d''8-. |
  % m.18
  cs''8-. d''8-. e''8-. fs''8-. a''16 g''16 fs''16 e''16 g''16 fs''16 e''16 d''16 |
  % m.19
  <cs'' e'' a''>4 r8 a''8-. g''8-. fs''8-. e''8-. d''8-. |
  % m.20
  cs''8-. d''8-. e''8-. fs''8-. a''16 g''16 fs''16 e''16 g''16 fs''16 e''16 d''16 |
  % m.21
  <cs'' e'' a''>4 e''16 cs''16 e''16 cs''16 a'4 r4 |
  % m.22
  e''4 a''8 gs''8 b''8 a''8 gs''8 fs''8 |
  % m.23
  fs''8\mordent e''8 e''4. e''16\mordent ds''16 e''8-. fs''8-. |
  % m.24
  e''8 d''!4 fs''8 d''8 cs''4 e''8 |
}

lower = {
  \global
  \clef treble
  \set Staff.midiInstrument = "acoustic grand"
  % m.17
  a16 a'16 gs'16 a'16 b'16 a'16 fs'16 a'16 e'16 a'16 d'16 a'16 cs'16 a'16 b16 a'16 |
  % m.18
  a16 a'16 b16  a'16 cs'16 a'16 d'16 a'16 e'16 a'16 cs'16 a'16 d'16 a'16 b16 a'16 |
  % m.19
  a16 a'16 gs'16 a'16 b'16 a'16 fs'16 a'16 e'16 a'16 d'16 a'16 cs'16 a'16 b16 a'16 |
  % m.20
  a16 a'16 b16  a'16 cs'16 a'16 d'16 a'16 e'16 a'16 cs'16 a'16 d'16 a'16 b16 a'16 |
  % m.21
  a4 <a cs' e'>4 <a cs' e'>4 r4 |
  % m.22
  r1 |
  % m.23
  <gs' b'>8 <gs' b'>8 <gs' b'>8 <gs' b'>8 <gs' b'>8 <gs' b'>8 <gs' b'>8 <gs' b'>8 |
  % m.24
  <fs' a'>8 <fs' a'>8 <fs' a'>8 <fs' a'>8 <e' gs'>8 <e' gs'>8 <e' gs'>8 <e' gs'>8 |
}

\score {
  <<
    \new PianoStaff <<
      \new Staff \upper
      \new Staff \lower
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}

