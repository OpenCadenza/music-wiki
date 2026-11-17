\version "2.26.0"
\language "english"

\header {
  title = "Symphony No. 3 in F major, Op. 90"
  subtitle = "III. Poco allegretto — mm. 1–8（摘录：大管律动低音 + 大提琴主题）"
  composer = "Johannes Brahms (1833–1897)"
  tagline = ##f
}

% 摘录说明（依据 espace-midi/J.F. Lucarelli LilyPond 底本核对）：
% 圆号（Corno I/II）在 mm.1–77 为全休止，首次进入在 m.78；
% 本段大管（Fagotti）自 m.1 起以“四分音符 + 八分休止”的律动低音（c4 r8 / f4 r8…）
% 提供和声支点，并非持续长音；大提琴主题在次中音谱号上从 C4 起（底本 \relative c'）。

global = {
  \key c \minor
  \time 3/8
  \tempo "Poco allegretto" 4. = 100
}

fagotto = {
  \global
  \clef bass
  \set Staff.midiInstrument = "bassoon"
  \partial 8 r8 |
  % m.1
  c4\p r8 |
  % m.2
  f4 r8 |
  % m.3
  c4 r8 |
  % m.4
  f4 r8 |
  % m.5
  b,4 r8 |
  % m.6
  c4 r8 |
  % m.7
  af'4 r8 |
  % m.8
  g8 c bf |
}

violoncello = {
  \global
  \clef tenor
  \set Staff.midiInstrument = "cello"
  \partial 8 c'16.( d'32) |
  % m.1
  ef'4.( |
  % m.2
  g'16. f'32 d'8) c'16.( d'32) |
  % m.3
  ef'4.( |
  % m.4
  bf'16. af'32 d8) d16.( ef'32) |
  % m.5
  f'4 af'16.( g'32) |
  % m.6
  ef'4 g'16.( f'32) |
  % m.7
  c'8.( d'32 c') b'16[( c']) |
  % m.8
  d'8( ef'8 e'8) |
}

\score {
  <<
    \new Staff \with { instrumentName = "Fagotto" } \fagotto
    \new Staff \with { instrumentName = "Violoncello" } \violoncello
  >>
  \layout { }
  \midi { }
}
