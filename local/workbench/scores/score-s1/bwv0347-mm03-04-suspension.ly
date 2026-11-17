\version "2.26.0"
\language "english"

% ============================================================
% 作品：J. S. Bach - Chorale "Ich dank dir, lieber Herre", BWV 347
% 片段：mm. 3–4（第二乐句半终止，中音声部跨小节 4–3 挂留）
% 来源：Humdrum/Kern chor002.krn（craigsapp/bach-370-chorales）
%       行 37–49（=3 至 =:|!），BWV 347，A 大调，4/4 拍
% 声部：SATB（GM 52）
% 记谱：绝对音高（c' = C4）。
% 时值说明：Kern m.4 末和弦为 4E; 4G#; 4B; 4e;（四分+延长记号，其后无
%       null 行），本谱按“挂留-解决在第 3 拍落地、延长记号吸收第 4 拍”的
%       常规记谱作四分音符+延长记号+隐藏四分休止（经核验员复核，#2 D4）。
% ============================================================

\header {
  title = "Chorale \"Ich dank dir, lieber Herre\""
  subtitle = "BWV 347 (mm. 3–4)"
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
  cs''4 b'4 a'4 gs'8 fs'8 |
  gs'4 fs'4 e'4\fermata \once \omit Rest r4 |
}

alto = {
  \global
  a'4 gs'8 fs'8 e'2~ |
  e'4 ds'4 b4\fermata \once \omit Rest r4 |
}

tenor = {
  \global
  e'4 ds'4 cs'2 |
  b4. a8 gs4\fermata \once \omit Rest r4 |
}

bass = {
  \global
  a4 b4 cs'4 b8 a8 |
  b4 b,4 e4\fermata \once \omit Rest r4 |
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