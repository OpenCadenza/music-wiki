\version "2.26.0"
\language "english"

\header {
  title = "Symphony No. 104 in D major („London“), Hob. I:104"
  subtitle = "I. Allegro — mm. 17–32 (strings excerpt; horns rest in this passage)"
  location = "Score example 2: mm. 17–32, excerpt (strings only)"
  composer = "Franz Joseph Haydn"
  tagline = ##f
}

% 谱源：
%   local/origin_resources/downloads/2026-11-17/s3/haydn104-1.krn
%   （MuseData / CCARH, Humdrum **kern, Symphony No.104, Movement 1, Eulenburg 版转录；
%    经 GitHub musedata/humdrum-haydn-symphonies 下载）
% 摘录说明：本段实际参奏为弦乐五部（Vln I/II、Va、Vc、Cb）；kern 显示 mm.18–32 圆号/小号/
%   定音鼓/木管均为休止，全奏爆发（圆号 D 长音、双簧管加倍）实际始于 m.33。故本摘录只取弦乐，
%   并在记录中说明与文章描述的差异（文章称 mm.25–32 圆号长音）。
% 拍号：m.17 为 4/4 引子的 1 拍弱起（\partial 4）；m.18 起 Allegro 转 2/2。
% 调号 D 大调（F#, C#）；速度 二分音符 = 120（kern *MM240）。
% 力度：article 称 mm.17–24 弦乐弱奏；谱面标 p 于 m.18。其余从略（kern 无力度层）。
% GM：Violin I/II=40, Viola=41, Violoncello=42, Contrabass=32。

global = {
  \key d \major
  \partial 4
  r4 |                              % m.17 (1-beat anacrusis, end of Adagio)
  \time 2/2
  \tempo "Allegro" 2 = 120
}

violinOne = {
  \global
  \clef treble
  |
  fs'2 g'4 e'4 |
  d'2 d'8 e'8 fs'8 g'8 |
  a''4 a''4 a''4 a''4 |
  b'2 a'2 |
  d''2 cs''2 |
  b'2 a'2 |
  a'8 g'8 b'8 a'8 g'4 fs'4 |
  a'4. fs'8 e''4 r4 |
  fs'2 g'4 e'4 |
  d'2 d'8 e'8 fs'8 g'8 |
  a''4 a''4 a''4 a''4 |
  b'2 a'2 |
  d''2 e''2 |
  fs''2 g''2 |
  g''8 fs''8 g'''8 e'''8 d'''4 cs'''4
  \bar "|."
}

violinTwo = {
  \global
  \clef treble
  |
  a2 b4 cs'4 |
  d'2. r4 |
  g'1 |
  fs'2. a'4 |
  a'4 g'2 fs'4 |
  fs'4 e'2 d'4 |
  cs'2. d'4 |
  fs'4. d'8 cs''4 r4 |
  a2 b4 cs'4 |
  d'2. r4 |
  g'1 |
  fs'1 |
  a4 b2 cs'4 |
  cs'4 d'2 e'4 |
  e'8 d'8 b''8 g''8 fs''4 e''4
  \bar "|."
}

viola = {
  \global
  \clef alto
  |
  a2 b4 g4 |
  fs2. r4 |
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  d4 fs4 a'4 r4 |
  a2 b4 g4 |
  fs2. r4 |
  r1 |
  r1 |
  r1 |
  r1 |
  r1
  \bar "|."
}

cello = {
  \global
  \clef bass
  |
  d1 |
  d2. r4 |
  cs'1 |
  d'2. cs'4 |
  b2 a2 |
  g2 fs2 |
  e2. d4 |
  a,2 r2 |
  d1 |
  d2. r4 |
  cs'1 |
  d'1 |
  fs4 g2 a4 |
  a4 b2 cs'4 |
  d'4 g4 a4 a,4
  \bar "|."
}

bass = {
  \global
  \clef bass
  |
  d,1 |
  d,2. r4 |
  cs1 |
  d2. cs4 |
  b,2 a,2 |
  g,2 fs,2 |
  e,2. d,4 |
  a,,2 r2 |
  d,1 |
  d,2. r4 |
  cs1 |
  d1 |
  fs,4 g,2 a,4 |
  a,4 b,2 cs4 |
  d4 g,4 a,4 a,,4
  \bar "|."
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Violino I" midiInstrument = "violin" } { \violinOne }
    \new Staff \with { instrumentName = "Violino II" midiInstrument = "violin" } { \violinTwo }
    \new Staff \with { instrumentName = "Viola" midiInstrument = "viola" } { \viola }
    \new Staff \with { instrumentName = "Violoncello" midiInstrument = "cello" } { \cello }
    \new Staff \with { instrumentName = "Contrabasso" midiInstrument = "contrabass" } { \bass }
  >>
  \layout { }
  \midi { }
}