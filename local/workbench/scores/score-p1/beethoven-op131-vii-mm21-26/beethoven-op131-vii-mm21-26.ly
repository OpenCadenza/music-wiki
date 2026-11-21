\version "2.26.0"
\language "english"

% 贝多芬 第14弦乐四重奏 Op.131 第七乐章 Allegro，mm.21–26
% 底本：local/resources/scores/source-packages/beethoven-score-sources/
%        beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet14-7.krn
%       （kern 文件头 OMV: Mvmt. 7 / OMD: Allegro / *M2/2 / *MM240 / *c#:）
% 内容：第一小提琴 C♯6–B♯5–A5–G♯5 的下行线（m.21 末拍起）与大提琴 C♯3–D♯3–F♯3–E3 的上行线
%       构成倒影对位；中提琴以 C♯5?/G♯4 的同音反复作伴奏（每拍 8 分休止 + 8 分音），
%       第二小提琴以 E–F♯–A、B♯–C♯ 的音型穿插。
% 八度基准：该语料 kern 约定为标准（c = 中央 C），已用已核验的 beethoven-op131-i-mm6-11 逐音校准。

global = {
  \key cs \minor
  \time 2/2
  \tempo "Allegro" 2 = 120
}

violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.21
  cs''2. cs'''4 |
  % m.22
  bs''2 a''2 |
  % m.23
  gs''2. cs'''4 |
  % m.24
  bs''4\p cs'''4 ds'''4 e'''4 |
  % m.25
  ds'''4 r2 cs'''4 |
  % m.26
  bs''2 a''2 |
}

violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  % m.21
  e'2. e'4 |
  % m.22
  fs'2 a'4 fs'4 |
  % m.23
  bs'2 cs''4 e'4 |
  % m.24
  fs'4\p e'4 ds'4 cs'4 |
  % m.25
  bs'4 r2 e'4 |
  % m.26
  fs'2 a'4 fs'4 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.21
  cs'4 r8 gs8 gs4 r8 gs8 |
  % m.22
  gs4 r8 gs8 gs4 r8 gs8 |
  % m.23
  gs4 r8 gs8 gs4 r8 gs8 |
  % m.24
  gs4\p r8 gs8 gs4 r8 gs8 |
  % m.25
  gs4 r8 gs8 gs4 r8 gs8 |
  % m.26
  gs4 r8 gs8 gs4 r8 gs8 |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  % m.21
  gs4 r2 cs4 |
  % m.22
  ds2 fs2 |
  % m.23
  e2. cs4 |
  % m.24
  ds4\p cs4 bs,4 cs4 |
  % m.25
  gs,4 r2 cs4 |
  % m.26
  ds2 fs2 |
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


