\version "2.26.0"
\language "english"

% ============================================================
% 作品：J. S. Bach - Chorale "Herzlich tut mich verlangen", BWV 153/5
% 片段：mm. 3–4（完全正格终止落音，落地和弦省略五音）
% 来源：Humdrum/Kern chor021.krn（craigsapp/bach-370-chorales）
%       行 36–44（=3 至 =:|!），BWV 153/5，a 小调，4/4 拍
% 声部：SATB（GM 52）
% 记谱：绝对音高（c' = C4）。
% 时值说明：Kern m.4 为 2.AA; 2.A; 2.c; 2.a;（附点二分+延长记号，4/4 小节第
%       4 拍由延长记号吸收），本谱保持附点二分+延长记号并补一隐藏四分休止。
% 核对：逐音对照 Kern；m.4 落地 A 三和弦 = A2–A3–C4–A4（三倍根音+单三音，
%       无五音 E）。
% ============================================================

\header {
  title = "Chorale \"Herzlich tut mich verlangen\""
  subtitle = "BWV 153/5 (mm. 3–4)"
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
  c''4 c''4 b'4 b'4 |
  a'2.\fermata \once \omit Rest r4 |
}

alto = {
  \global
  ds'4 e'4 fs'4 e'8 d'8 |
  c'2.\fermata \once \omit Rest r4 |
}

tenor = {
  \global
  a4 a4 a4 gs4 |
  a2.\fermata \once \omit Rest r4 |
}

bass = {
  \global
  fs4 e4 ds4 e4 |
  a,2.\fermata \once \omit Rest r4 |
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