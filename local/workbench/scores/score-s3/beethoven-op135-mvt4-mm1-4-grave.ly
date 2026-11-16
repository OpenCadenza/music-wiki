\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 16 in F Major, Op. 135"
  subtitle = "IV. Der schwer gefaßte Entschluß — Grave ma non troppo tratto, mm. 1–4"
  location = "Score example 1: mm. 1–4 (Muss es sein?)"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% 谱源（本地权威源）：
%   1. local/resources/scores/source-packages/beethoven-score-sources/
%      beethoven-string-quartets-main/.../kern/quartet16-4.krn（mm. 1–4）
%   2. local/resources/scores/dcml-abc/n16op135_04.notes.tsv（reviewed, mm. 1–4）
%   3. local/resources/scores/dcml-abc/n16op135_04.harmonies.tsv（m. 1: #viio6 → i6）
% 音符数据以 Kern 与 DCML 双向核对后逐音录入；音高采用绝对音名记法。
% 力度：仅录入文章明确给出、且原谱可证的第一小提琴 c''2 上的 fp（文章：“第一小提琴在第 3 拍以 fp 切入高音 c''”）。
% GM 程序：Violin I=40, Violin II=40, Viola=41, Violoncello=42。

global = {
  \key f \minor
  \time 3/2
  \tempo "Grave ma non troppo tratto" 2 = 40
  \set Score.currentBarNumber = #1
}

violinOne = {
  \global
  \clef treble
  r2 r2 c''2^\fp~ |                            % m.1
  c''8( bf'8 af'8 g'8 f'8 af'8 c''8 e''8 f''4) r4 |  % m.2
  r2 r2 f''2~ |                              % m.3
  f''8( ef''8 df''8 c''8 bf'8 df''8 f''8 a''8 bf''4) r4 |  % m.4
  \bar "|."
}

violinTwo = {
  \global
  \clef treble
  r1. |                                     % m.1
  r2 c''2~ c''8( bf'8 af'8 g'8) |            % m.2
  f'4 r4 r2 r2 |                            % m.3
  f'2~ f'8( ef'8 df'8 c'8 bf8 d'8 f'8 bf'8) |   % m.4
  \bar "|."
}

viola = {
  \global
  \clef alto
  g4. e8 af2 r2 |                           % m.1
  c'2~ c'8( bf8 af8 g8 f8 af8 c'8 f'8) |    % m.2
  c'4. a8 df'2 r2 |                         % m.3
  r2 f'2~ f'8 f'8( d'8 bf8) |               % m.4
  \bar "|."
}

cello = {
  \global
  \clef bass
  g,4. e,8 af,2 r2 |                        % m.1
  r1. |                                     % m.2
  c4. a,8 df2 r2 |                          % m.3
  r2 r2 af2 |                               % m.4
  \bar "|."
}

\score {
  \new StaffGroup <<
    \new Staff \with {
      instrumentName = "Violin I"
      midiInstrument = "violin"
    } { \violinOne }

    \new Staff \with {
      instrumentName = "Violin II"
      midiInstrument = "violin"
    } { \violinTwo }

    \new Staff \with {
      instrumentName = "Viola"
      midiInstrument = "viola"
    } { \viola }

    \new Staff \with {
      instrumentName = "Violoncello"
      midiInstrument = "cello"
    } { \cello }
  >>
  \layout { }
  \midi { }
}