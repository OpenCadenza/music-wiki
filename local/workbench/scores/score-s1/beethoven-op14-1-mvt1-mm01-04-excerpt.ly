\version "2.26.0"
\language "english"

% ============================================================
% 作品：Ludwig van Beethoven - Piano Sonata No. 9 in E major, Op. 14 No. 1
% 片段（摘录）：I. Allegro —— mm. 1–4（左手八分音符和弦音型 + 右手主题起句）
% 来源：Humdrum/Kern sonata09-1.krn（craigsapp/beethoven-piano-sonatas）
%       文件头：Piano Sonata no. 9 in E major；OPS 14；ONM 1；OMV 1；Allegro；
%       *k[f#c#g#d#] *E: *M4/4 *MM132
%       行 20–53（`=1-` 至 `=4`），mm.1–4
% 声部：Piano（GM 0 Acoustic Grand Piano，双手分别记谱）
% 拍/调：4/4，E 大调
% 速度：Allegro（Kern *MM132；本谱记 4 = 132）
% 记谱：绝对音高（c' = C4）。
% 范围说明：仅 mm.1–4。mm.5–16 含双手十六分音符跑动与谱号切换（越手）
%       的多声部织体，本批未逐音编码（见核对记录“缺口”一节）。
% ============================================================

\header {
  title = "Piano Sonata No. 9 in E major, Op. 14 No. 1"
  subtitle = "I. Allegro — mm. 1–4 (excerpt)"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

global = {
  \key e \major
  \time 4/4
  \tempo "Allegro" 4 = 132
}

upper = {
  \global
  \clef treble
  b'2\p <e' e''>2 |
  cs''2 <fs' fs''>2 |
  ds''2 <b' b''>2 |
  b'4. cs'''16 ds'''16 e'''4 r4 |
}

lower = {
  \global
  \clef bass
  r8 <e gs b>8 <e gs b>8 <e gs b>8 r8 <e gs b>8 <e gs b>8 <e gs b>8 |
  r8 <e a cs'>8 <e a cs'>8 <e a cs'>8 r8 <e a cs'>8 <e a cs'>8 <e a cs'>8 |
  r8 <e fs a ds'>8 <e fs a ds'>8 <e fs a ds'>8 r8 <e fs a ds'>8 <e fs a ds'>8 <e fs a ds'>8 |
  <e gs b e'>2. r4 |
}

\score {
  \new PianoStaff <<
    \new Staff \with {
      instrumentName = "Piano (GM 0) RH"
      midiInstrument = "acoustic grand"
    } { \upper }
    \new Staff \with {
      instrumentName = "Piano (GM 0) LH"
      midiInstrument = "acoustic grand"
    } { \lower }
  >>
  \layout { }
  \midi { }
}