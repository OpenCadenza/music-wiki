\version "2.26.0"
\language "english"

% ============================================================
% 作品：J. S. Bach - Chorale "Es ist genug! so nimm Herr", BWV 60/5
% 片段：mm. 1–4（开篇三全音呼告与半音阶下行的多重挂留网）
% 来源：Humdrum/Kern chor216.krn（craigsapp/bach-370-chorales）
%       行 19–40（=1- 至 =5 之前），BWV 60/5，A 大调，4/4 拍
% 声部：SATB（GM 52）
% 记谱：绝对音高（c' = C4）。
% 核对：逐音对照 Kern。m.2 全体 B# 大三和弦带延长记号（2B#; 2f#; 2g#;
%       2dd#;）后接一拍休止；m.3 低音 9 音下行（C#4 B3 A3 G#3 F#3 E3 D3
%       C#3 B2）；m.4 落在 A 大调主和弦。
% ============================================================

\header {
  title = "Chorale \"Es ist genug! so nimm Herr\""
  subtitle = "BWV 60/5 (mm. 1–4)"
  composer = "Johann Sebastian Bach"
  tagline = ##f
}

global = {
  \key a \major
  \time 4/4
  \tempo "Choral" 4 = 100
}

soprano = {
  \global
  a'2 b'4 cs''4 |
  ds''2\fermata r4 ds''4 |
  e''4 b'4 b'4 d''4 |
  cs''2.\fermata b'4 |
}

alto = {
  \global
  e'2 e'4 d'8 cs'8 |
  gs'2\fermata r4 gs'4 |
  gs'4. a'8 gs'8 fs'8 gs'8 e'8 |
  a'2.\fermata gs'4 |
}

tenor = {
  \global
  cs'2 b4 fs'4 |
  fs'2\fermata r4 bs4 |
  cs'8 ds'8 e'4 e'4 e'4 |
  e'2.\fermata e'4 |
}

bass = {
  \global
  a2 gs4 as4 |
  bs2\fermata r4 gs4 |
  cs'8 b16 a16 gs8 fs8 e8 d8 cs8 b,8 |
  a,2.\fermata e4 |
}

\score {
  \new StaffGroup <<
    \new Staff \with {
      instrumentName = "Soprano (GM 52)"
      midiInstrument = "choir aahs"
    } { \soprano }
    \new Staff \with {
      instrumentName = "Alto (GM 52)"
      midiInstrument = "choir aahs"
    } { \alto }
    \new Staff \with {
      instrumentName = "Tenor (GM 52)"
      midiInstrument = "choir aahs"
    } { \clef "treble_8" \tenor }
    \new Staff \with {
      instrumentName = "Bass (GM 52)"
      midiInstrument = "choir aahs"
    } { \clef bass \bass }
  >>
  \layout { }
  \midi { }
}