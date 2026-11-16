\version "2.26.0"
\language "english"

% ============================================================
% 作品：J. S. Bach - Chorale "Aus meines Herzens Grunde", BWV 269
% 片段：mm. 5–7（完全正格终止，4–3 挂留锁扣）
% 来源：Humdrum/Kern chor001.krn（craigsapp/bach-370-chorales）
%       行 43–53（=5 至 =:|!），BWV 269，G 大调，3/4 拍
% 声部：SATB（GM 52）
% 记谱：绝对音高（c' = C4）。
% 时值说明：Kern m.7 为 2GG; 2B; 2d; 2g;（二分+延长记号，3/4 小节第 3 拍
%       由延长记号吸收），本谱以二分+延长记号并补一隐藏四分休止以补全小节。
% ============================================================

\header {
  title = "Chorale \"Aus meines Herzens Grunde\""
  subtitle = "BWV 269 (mm. 5–7)"
  composer = "Johann Sebastian Bach"
  tagline = ##f
}

global = {
  \key g \major
  \time 3/4
  \tempo "Choral" 4 = 100
}

soprano = {
  \global
  d''2 cs''4 |
  b'4 a'2 |
  g'2\fermata \once \omit Rest r4 |
}

alto = {
  \global
  d'4 e'4 fs'4 |
  g'2 fs'4 |
  d'2\fermata \once \omit Rest r4 |
}

tenor = {
  \global
  a4 b4 c'4 |
  d'4 e'4 d'8 c'8 |
  b2\fermata \once \omit Rest r4 |
}

bass = {
  \global
  fs,4 g,4 a,4 |
  b,4 c4 d4 |
  g,2\fermata \once \omit Rest r4 |
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