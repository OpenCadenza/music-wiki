\version "2.26.0"
\language "english"

% ============================================================
% 作品：J. S. Bach - Chorale "Jesu, meine Freude", BWV 87/7
% 片段：mm. 1–3（A 乐段开篇与 4–3 挂留半终止）
% 来源：Humdrum/Kern chor096.krn（craigsapp/bach-370-chorales）
%       行 22–46（=1- 至 =4 之前），BWV 87/7，d 小调，4/4 拍
% 声部：SATB（GM 52）
% 记谱：绝对音高（c' = C4）。
% 核对：逐音对照 Kern。m.1 b4 低音 A3–G3，m.2 b1 低音 A3，随后 m.2 b2
%       落至 A2；m.2 b3–4 全体 D 大调三和弦带延长记号（皮卡迪）。
% ============================================================

\header {
  title = "Chorale \"Jesu, meine Freude\""
  subtitle = "BWV 87/7 (mm. 1–3)"
  composer = "Johann Sebastian Bach"
  tagline = ##f
}

global = {
  \key d \minor
  \time 4/4
  \tempo "Choral" 4 = 100
}

soprano = {
  \global
  a'4 a'4 g'4 f'4 |
  e'2 d'2\fermata |
  a'4 a'4 b'4 cs''4 |
}

alto = {
  \global
  f'4 f'4 e'4 d'4 |
  d'4 cs'4 a2\fermata |
  f'4 f'4 f'8 d'8 g'4 |
}

tenor = {
  \global
  d'4 d'4 d'8 cs'8 d'4 |
  a8 bf8 a8 g8 f2\fermata |
  d'4 d'4 d'8 b8 e'4 |
}

bass = {
  \global
  d8 e8 f8 d8 bf4 a8 g8 |
  a4 a,4 d2\fermata |
  d8 e8 f8 d8 g4 f8 e8 |
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