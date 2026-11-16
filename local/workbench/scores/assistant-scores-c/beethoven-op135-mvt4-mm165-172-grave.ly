\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 16 in F Major, Op. 135"
  subtitle = "IV. Der schwer gefaßte Entschluß (Grave, mm. 165–172)"
  location = "mm. 165–172"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% 严格按原谱与可靠谱源核对：
% 作品：Ludwig van Beethoven - String Quartet No. 16 in F Major, Op. 135
% 乐章：IV. Der schwer gefaßte Entschluß
% 片段：Grave ma non troppo tratto (mm. 165–172，再现部前夕第二次 Grave 增三和弦语境)
% 原谱依据：
% 1. local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet16-4.krn (mm. 165-172)
% 2. local/resources/scores/source-packages/dcml/ABC-main/ABC-main/MS3/n16op135_04.mscx (reviewed)
% 3. local/resources/scores/dcml-abc/n16op135_04.harmonies.tsv (m. 165: III+ / III+6, m. 167: VI+7)
% 编制：弦乐四重奏 (Violin I, Violin II, Viola, Violoncello)
% GM 程序号 (0-127 基准):
% Violin I: 40 (violin)
% Violin II: 40 (violin)
% Viola: 41 (viola)
% Violoncello: 42 (cello)
% 速度与拍号：Grave ma non troppo tratto (3/2 拍, 二分音符 = 40)

global = {
  \key f \minor
  \time 3/2
  \tempo "Grave ma non troppo tratto" 2 = 40
  \set Score.currentBarNumber = #165
}

violinOne = {
  \global
  \clef treble
  c'''2:16\ff c'''2:16 c'''2:16 |
  c'''2:16\> c'''2:16 c'''2:16 |
  c'''2:16\ff c'''2:16 c'''2:16\! |
  c'''2:16\> c'''2:16 bf''2:16 |
  bf''2:16\f bf''2:16 bf''2:16\> |
  <df'' bf''>2:16\f <df'' bf''>2:16 <df'' bf''>4 r4 |
  r2 <df'' bf''>2:16\f <df'' bf''>4 r4 |
  r2 <df'' bf''>2:16\f\> <df'' bf''>4\dim r4\! |
  \bar "||"
}

violinTwo = {
  \global
  \clef treble
  <c'' e''>2:16\ff <c'' e''>2:16 <c'' e''>2:16 |
  <c'' e''>2:16\> <c'' e''>2:16 <c'' f''>2:16 |
  <a' f''>2:16\ff <a' f''>2:16 <a' f''>2:16\! |
  <a' f''>2:16\> <a' f''>2:16 <bf' f''>2:16 |
  <df'' f''>2:16\f <df'' g''>2:16 <df'' g''>2:16\> |
  <e'' g''>2:16\f <e'' g''>2:16 <e'' g''>4 r4 |
  r2 <e'' g''>2:16\f <e'' g''>4 r4 |
  r2 <e'' g''>2:16\f\> <e'' g''>4\dim r4\! |
  \bar "||"
}

viola = {
  \global
  \clef alto
  g4.\ff e8-. af2~ <af c'>2 |
  <af c'>8( bf af g af c' f' g' af' f' c' af) |
  c'4.\ff a8-. df'2 r2 |
  r2 r2 ( df'8 f' bf' df'' ) |
  df'4.\f bf8-. e'2 r2 |
  df2:16\f df4 r4 r2 |
  df2:16\f c4 r4 r2 |
  c2:16\f\> c4\dim r4 r2\! |
  \bar "||"
}

cello = {
  \global
  \clef bass
  g,4.\ff e,8-. af,2 r2 |
  R1. |
  c4.\ff a,8-. df2 f2~\sf |
  f8( ef df c df f bf c' df'4) r4 |
  df4.\f bf,8-. e2 r2 |
  df,2:16\f df,4 r4 r2 |
  df,2:16\f c,4 r4 r2 |
  c,2:16\f\> c,4\dim r4 r2\! |
  \bar "||"
}

\score {
  \new StaffGroup <<
    \new Staff \with {
      instrumentName = "Violin I"
      midiInstrument = "violin"
      midiMinimumVolume = #0.2
      midiMaximumVolume = #0.9
    } { \violinOne }

    \new Staff \with {
      instrumentName = "Violin II"
      midiInstrument = "violin"
      midiMinimumVolume = #0.2
      midiMaximumVolume = #0.9
    } { \violinTwo }

    \new Staff \with {
      instrumentName = "Viola"
      midiInstrument = "viola"
      midiMinimumVolume = #0.2
      midiMaximumVolume = #0.9
    } { \viola }

    \new Staff \with {
      instrumentName = "Violoncello"
      midiInstrument = "cello"
      midiMinimumVolume = #0.2
      midiMaximumVolume = #0.9
    } { \cello }
  >>
  \layout { }
  \midi { }
}
