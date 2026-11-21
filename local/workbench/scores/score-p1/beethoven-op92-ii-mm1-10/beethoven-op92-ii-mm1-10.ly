\version "2.26.0"
\language "english"

% 贝多芬 第七交响曲 Op.92 第二乐章 Allegretto，mm.1–10
% 底本：Mutopia Project #595（Symphony No.7 in A major, Op.92 — Allegretto）
%       分谱 Symphony7_2-lys（Stelios Samelis, 2005-08，来源标注 Dover / Litolff）
%       本地副本 local/workbench/scores/score-s2/downloads/op92-2/
% 事实要点（已与两份独立出版说明交叉核对，见同目录 核对记录.md）：
%   m.1–3：双簧管、单簧管(A)、大管、圆号(E) 奏 a 小调主和弦，f → pp，m.3 后半拍释放；
%          长笛、小号、定音鼓此时仍未进入。
%   m.3 起：中提琴、大提琴、低音提琴接固定音型；一、二小提琴在 mm.1–10 仍全休止
%          （第二小提琴 m.27 进入、第一小提琴 m.51 进入）。
% 声部取舍：mm.1–10 内小号与定音鼓全休止（它们 m.75 才进），本摘录从略。
%
% 【记谱方式】除单簧管与圆号外一律按实际发声音高记谱；为让纸面直接读出 a 小调主三和弦，
% 单簧管(in A, 记谱 g'/c'' = 实音 E4/A4) 与圆号(in E, 记谱 c'/c'' = 实音 E3/E4) 也写成
% **音乐会音高**（去掉 \transposition），故 10 行谱表自上而下为：
%   Fl. / Ob.(实音 C5/E5) / Cl. in A → 实音 E4/A4 / Fg.(实音 A3/C4) / Cor. in E → 实音 E3/E4 /
%   Vn I / Vn II / Va.(E3) / Vc.(C3) / Cb.(A2)
% 纸面合成即 A2-C3-E3-E4-A4-C5-E5。拍号/调号仍按底本（a 小调）。
% 播放速度：底本只写 "Allegretto"；Bärenreiter BA 9007 分谱标 Allegretto ♩=76，
% 故取 4=76 作播放速度（非自拟）。
global = {
  \key a \minor
  \time 2/4
  \tempo "Allegretto" 4 = 76
}

flauti = {
  \global
  \clef treble
  \set Staff.midiInstrument = "flute"
  R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
}

oboi = {
  \global
  \clef treble
  \set Staff.midiInstrument = "oboe"
  % m.1–3：a 小调主和弦，f 起、pp 收，m.3 后半拍释放
  <c'' e''>2\f\> ~ | <c'' e''>2\! ~ | <c'' e''>4\pp r4 |
  R2 | R2 | R2 | R2 | R2 | R2 | R2 |
}

clarinetti = {
  \global
  \clef treble
  \set Staff.midiInstrument = "clarinet"
  % 单簧管 in A：底本记谱 g'/c''，此处按实音 E4/A4 记谱（不写 \transposition）
  <e' a'>2\f\> ~ | <e' a'>2\! ~ | <e' a'>4\pp r4 |
  R2 | R2 | R2 | R2 | R2 | R2 | R2 |
}

fagotti = {
  \global
  \clef bass
  \set Staff.midiInstrument = "bassoon"
  <a c'>2\f\> ~ | <a c'>2\! ~ | <a c'>4\pp r4 |
  R2 | R2 | R2 | R2 | R2 | R2 | R2 |
}

corni = {
  \global
  \clef treble
  \set Staff.midiInstrument = "french horn"
  % 圆号 in E：底本记谱 c'/c''（标准 E 调圆号发声下小六度 = E3/E4），此处按实音记谱
  <e e'>2\f\> ~ | <e e'>2\! ~ | <e e'>4\pp r4 |
  R2 | R2 | R2 | R2 | R2 | R2 | R2 |
}

violinoOne = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
}

violinoTwo = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 | R2 |
}

viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  % m.1–2 休止；m.3 起接固定音型
  R2 | R2 |
  e4\p^\markup { \large \italic "ten." } e8\staccato e8\staccato |
  e4\staccato( e4\staccato) |
  e4 e8\staccato e8\staccato |
  e4\staccato( e4\staccato) |
  e4 e8\staccato <d fs>8\staccato |
  <e g>4\staccato( <e g>4\staccato) |
  <d g>4 <c g>8\staccato( <d g>8\staccato) |
  <e g>4 r4 |
}

violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  R2 | R2 |
  c4\p^\markup { \large \italic "ten." } c8\staccato c8\staccato |
  b,4\staccato( b,4\staccato) |
  b,4 b,8\staccato b,8\staccato |
  c4\staccato( c4\staccato) |
  c4 c8\staccato c8\staccato |
  c4\staccato( c4\staccato) |
  b,4 a,8\staccato( b,8\staccato) |
  c4 r4 |
}

contrabass = {
  \global
  \clef bass
  \set Staff.midiInstrument = "contrabass"
  R2 | R2 |
  a,4\p^\markup { \large \italic "ten." } a,8\staccato a,8\staccato |
  gs,4\staccato( gs,4\staccato) |
  e,4 e,8\staccato e,8\staccato |
  a,4\staccato( a,4\staccato) |
  a,4 a,8\staccato a,8\staccato |
  a,4\staccato( a,4\staccato) |
  g,4 g,8\staccato( g,8\staccato) |
  c4 r4 |
}

\score {
  <<
    \new StaffGroup <<
      \new Staff \flauti
      \new Staff \oboi
      \new Staff \clarinetti
      \new Staff \fagotti
      \new Staff \corni
    >>
    \new StaffGroup <<
      \new Staff \violinoOne
      \new Staff \violinoTwo
      \new Staff \viola
      \new Staff \violoncello
      \new Staff \contrabass
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}

