\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 10 in E-flat Major, Op. 74 („Harp“)"
  subtitle = "I. Poco Adagio — mm. 6–9 (clef/octave trap: cello B♭2 and violin passage)"
  location = "Score example 2: mm. 6–9"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% 谱源：
%   1. local/resources/scores/source-packages/beethoven-score-sources/.../kern/quartet10-1.krn（mm.6–9）
%   2. local/materials/theory/dcml-abc/n10op74_01.notes.tsv（reviewed, DCML；逐音交叉验证）
% 音符经 krn2ly 转换（绝对音名、显式升降号）并与 DCML notes 的 midi 值逐音比对：
%   m.6 Vln2 = A♭5（80）二分 — DCML 证实（非八度噪声）；m.7 Vc = B♭2（46）全音符（文章指出的旧谱
%   bf,,1 = B♭1 错误，本版为 bf,1 = B♭2）；m.9 Vln1 花彩 16ee- 16ff 16gg 16ff（E♭5–F5–G5–F5）。
% 拍号：原谱 2/2（Poco Adagio）；kern 记 4/4（等价）。速度：四分音符 = 72（kern *MM72）→ 二分音符 = 36。
% 力度：kern 的 **dynam 列在 mm.6–9 为空，从略。
% GM：Violin I/II=40, Viola=41, Violoncello=42。

global = {
  \key ef \major
  \time 2/2
  \tempo "Poco Adagio" 2 = 36
  \set Score.currentBarNumber = #6
}

violinOne = {
  \global
  \clef treble
  |
  d''2 ef''4 c''8 f''8 |
  ef''4 d''4 c''4 bf'4 |
  bf'4 af'8 r8 af'4 g'8 r8 |
  g'4 g'16 f'16 e'16 f'16 e'16 f'16 g'16 f'16 ef''16 f''16 g''16 f''16
  \bar "|."
}

violinTwo = {
  \global
  \clef treble
  |
  af''2 g''4 f''8 f'8 |
  f'2 af'4 g'4 |
  g'4 f'8 r8 bf4 bf8 r8 |
  c'4 r4 r2
  \bar "|."
}

viola = {
  \global
  \clef alto
  |
  f'4 cf''4 bf'4 c'4 |
  af2 d4. ef8 |
  e4 f4 d4 ef4 |
  af4 r4 r4 af4
  \bar "|."
}

cello = {
  \global
  \clef bass
  |
  ef,2. a,4 |
  bf,1 |
  c2 f,4. g,8 |
  af,4 r4 r4 f,4
  \bar "|."
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Violin I" midiInstrument = "violin" } { \violinOne }
    \new Staff \with { instrumentName = "Violin II" midiInstrument = "violin" } { \violinTwo }
    \new Staff \with { instrumentName = "Viola" midiInstrument = "viola" } { \viola }
    \new Staff \with { instrumentName = "Violoncello" midiInstrument = "cello" } { \cello }
  >>
  \layout { }
  \midi { }
}