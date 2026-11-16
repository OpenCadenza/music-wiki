\version "2.26.0"
\language "english"

% ============================================================
% 作品：J. S. Bach - Chorale "Aus meines Herzens Grunde", BWV 269
% 片段：mm. 3–4（首乐句半终止，女高音先现音）
% 来源：Humdrum/Kern chor001.krn（craigsapp/bach-370-chorales）
%       行 33–42（=3 至 =4），BWV 269，G 大调，3/4 拍
% 声部：SATB（Soprano/Alto/Tenor/Bass，GM 52 合唱）
% 记谱：绝对音高（c' = C4），所有八度显式给出。
% 核对：逐音对照 Kern；m.4 第 1–2 拍 D 大三和弦全体带延长记号
%       （2D; 2d; 2f#; 2a;）。
% ============================================================

\header {
  title = "Chorale \"Aus meines Herzens Grunde\""
  subtitle = "BWV 269 (mm. 3–4)"
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
  g'4. a'8 b'4 |
  a'2\fermata b'4 |
}

alto = {
  \global
  e'8 d'8 e'8 fs'8 g'4 |
  fs'2\fermata g'4 |
}

tenor = {
  \global
  c'8 b8 c'4 d'4 |
  d'2\fermata d'4 |
}

bass = {
  \global
  c4 b,8 a,8 g,4 |
  d2\fermata g,4 |
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