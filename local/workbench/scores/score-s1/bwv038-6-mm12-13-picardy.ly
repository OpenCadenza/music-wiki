\version "2.26.0"
\language "english"

% ============================================================
% 作品：J. S. Bach - Chorale "Aus tiefer Not schrei ich zu dir", BWV 38/6
% 片段：mm. 12–13（全曲终曲，旋律长音锚定 + 下方三声部二次对位，皮卡迪终束）
% 来源：Humdrum/Kern chor010.krn（craigsapp/bach-370-chorales）
%       行 84–93（=12 至 ==），BWV 38/6，a 小调，4/4 拍
% 声部：SATB（GM 52）
% 记谱：绝对音高（c' = C4）。
% 核对：逐音对照 Kern；m.13 女高音全音符 E4 带延长记号（1e;）。
% ============================================================

\header {
  title = "Chorale \"Aus tiefer Not schrei ich zu dir\""
  subtitle = "BWV 38/6 (mm. 12–13)"
  composer = "Johann Sebastian Bach"
  tagline = ##f
}

global = {
  \key a \minor
  \time 4/4
  \tempo "Choral" 4 = 100
}

soprano = {
  \global
  a'4 e'4 g'4 f'4 |
  e'1\fermata |
}

alto = {
  \global
  c'4 c'4 d'2~ |
  d'4 c'4 b2\fermata |
}

tenor = {
  \global
  a4 g4 g4 a4 |
  b4 a4 gs2\fermata |
}

bass = {
  \global
  f4 c4 bf,4 a,4 |
  gs,4 a,4 e,2\fermata |
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