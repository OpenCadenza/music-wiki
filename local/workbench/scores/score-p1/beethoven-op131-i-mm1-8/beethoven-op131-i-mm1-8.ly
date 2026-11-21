\version "2.26.0"
\language "english"

% 贝多芬 第14弦乐四重奏 Op.131 第一乐章 Adagio ma non troppo e molto espressivo
% 弱起（1 拍，不计号）+ 印刷谱 mm.1–8
% 底本：local/resources/scores/source-packages/beethoven-score-sources/
%        beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet14-1.krn
%       （kern 文件头 OMV 标成 "Mvmt. 4" 是元数据错误，内容即第一乐章 C♯ 小调赋格）
% 取音：第一小提琴赋格主题（弱起–m.4）、第二小提琴答题（m.4 进入）、中提琴第三声部进入（m.8）
% 八度核对：该语料 kern 约定为标准（c = 中央 C），已用已入正文且经核验的
%           beethoven-op131-i-mm6-11（S2-D2-beethoven-op131-m6-11.ly）逐音校准。

global = {
  \key cs \minor
  \time 2/2
  \tempo "Adagio ma non troppo e molto espressivo" 4 = 69
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  \partial 4
  gs'4\p( |
  % m.1
  bs'2 cs''2) |
  % m.2
  a'2.( gs'4 |
  % m.3
  fs'4 a'4 gs'4 fs'4) |
  % m.4
  e'4 fs'4 gs'2~ |
  % m.5
  gs'4 b'2 a'4~ |
  % m.6
  a'4 es'4 fs'4 a'4 |
  % m.7
  g'4 es'2 es''4 |
  % m.8
  fs''2( e''4 ds''4) |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  \partial 4
  r4 |
  % m.1
  r1 |
  % m.2
  r1 |
  % m.3
  r1 |
  % m.4
  cs'4\p( r2. |
  % m.5
  es'2 fs'2) |
  % m.6
  d'2.( cs'4 |
  % m.7
  b4 d'4 cs'4 b4 |
  % m.8
  a4 b4 cs'4) bs4 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  \partial 4
  r4 |
  % m.1
  r1 |
  % m.2
  r1 |
  % m.3
  r1 |
  % m.4
  r1 |
  % m.5
  r1 |
  % m.6
  r1 |
  % m.7
  r1 |
  % m.8
  r2 r4 gs4\p |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  \partial 4
  r4 |
  % m.1
  r1 |
  % m.2
  r1 |
  % m.3
  r1 |
  % m.4
  r1 |
  % m.5
  r1 |
  % m.6
  r1 |
  % m.7
  r1 |
  % m.8
  r1 |
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

