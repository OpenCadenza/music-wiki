\version "2.26.0"
\language "english"

% 贝多芬 第14弦乐四重奏 Op.131 第七乐章 Allegro，mm.216–224
% 底本：local/resources/scores/source-packages/beethoven-score-sources/
%        beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet14-7.krn
% 内容：D 大调踏板织体（大提琴 D2+A2 全音符、中提琴 F♯/A、第二小提琴 A），
%       第一小提琴在其上作 F♯5–A6 的运动（下行四音列 + 八度上跳）。
% 调号：底本 kern 在 m.211 已改为 *k[f#c#]（2 升号 = D 大调），下一次回 4 升号是 m.248，
%       故本段用 \key d \major（不是 C♯ 小调）。
% 力度：底本 **dynam 在 m.216 强拍四声部齐标 p（紧接 m.214 的 f），m.220 / m.224 重申。
% 八度基准：该语料 kern 约定为标准（c = 中央 C），已用已核验的 beethoven-op131-i-mm6-11 校准。

global = {
  \key d \major
  \time 2/2
  \tempo "Allegro" 2 = 120
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.216
  fs''2\p~ fs''8 e''8 d''8 cs''8 |
  % m.217
  d''8 cs''8 b'8 a'8 g'8 fs'8 e'8 d'8 |
  % m.218
  d'4. cs'8 a''2 |
  % m.219
  a''2 a''2 |
  % m.220
  a''2\p d'''2 |
  % m.221
  fs'''2 a'''2 |
  % m.222
  a''2 cs'''2 |
  % m.223
  e'''2 a'''2 |
  % m.224
  a''2\p d'''2 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.216
  <a a'>1\p~ |
  % m.217
  <a a'>1 |
  % m.218
  <a a'>1~ |
  % m.219
  <a a'>1 |
  % m.220
  <a a'>2\p fs'2~ |
  % m.221
  <a fs'>1 |
  % m.222
  <a g'>1~ |
  % m.223
  <a g'>1 |
  % m.224
  fs''2\p~ fs''8 e''8 d''8 cs''8 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.216
  fs1\p~ |
  % m.217
  fs1 |
  % m.218
  g1~ |
  % m.219
  g1 |
  % m.220
  fs'2\p~ fs'8 e'8 d'8 cs'8 |
  % m.221
  d'8 cs'8 b8 a8 g8 fs8 e8 d8 |
  % m.222
  d4.\p cs8 a'2 |
  % m.223
  a'2 a'2 |
  % m.224
  <a fs'>1\p |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  % m.216
  <d, a,>1\p~ |
  % m.217
  <d, a,>1 |
  % m.218
  <e, a,>1~ |
  % m.219
  <e, a,>1 |
  % m.220
  <d, a,>1\p~ |
  % m.221
  <d, a,>1 |
  % m.222
  <e, a,>1~ |
  % m.223
  <e, a,>1 |
  % m.224
  <d, a,>1\p |
}

\score {
  <<
    \new StaffGroup <<
      \new Staff \violinoI
      \new Staff \violinoII
      \new Staff \viola
      \new Staff \violoncello
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
