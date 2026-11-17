\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 16 in F Major, Op. 135"
  subtitle = "IV. Der schwer gefaßte Entschluß — Allegro, mm. 12 (Auftakt) – 16"
  location = "Score example 2: mm. 12 (anacrusis) – 16 (Es muss sein!)"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% 谱源（本地权威源）：
%   1. .../beethoven-string-quartets-main/.../kern/quartet16-4.krn（mm. 12–16）
%   2. local/resources/scores/dcml-abc/n16op135_04.notes.tsv（reviewed, mm. 12–16）
%   3. local/resources/scores/dcml-abc/n16op135_04.harmonies.tsv（mm. 13–14: V → V6; mm. 15–16: I）
% m.12 为 Grave 段末小节（3/2 拍，f 小调 4 降）；m.13 转 F 大调 1 降、4/4 拍、Allegro。
% m.12 末的 a''/a' 四分音符是 Allegro 主部的弱起（第 3 拍后半，按 3/2 记谱），
% 速度标记 Allegro 置于该弱起处（此时起为二分音符 = 80）。
% 音符数据已与 Kern 及 DCML 双向逐音核对；音高采用绝对音名记法。
% 力度：Kern/DCML 源未含力度信息，Allegro 段原谱力度标记未能从实证源确认，故从略（不在谱面臆造）。

global = {
  \key f \minor
  \time 3/2
  \set Score.currentBarNumber = #12
}

violinOne = {
  \global
  \clef treble
  \tempo "Grave ma non troppo tratto" 2 = 40
  r2 c''8 c''8 c''4~ c''4 \tempo "Allegro" 2 = 80 a''4 |   % m.12 (3/2); a''4 = Allegro anacrusis
  \time 4/4 \key f \major
  c'''2 g''2 |                               % m.13 (A -> C -> G)
  r2 r4 g''4 |                               % m.14 (anacrusis G; 3 beats rest)
  bf''2 f''2 |                               % m.15 (G -> Bb -> F)
  r1 |                                       % m.16
  \bar "|."
}

violinTwo = {
  \global
  \clef treble
  r2 c'8 c'8 c'4~ c'4 a'4 |                  % m.12
  \time 4/4 \key f \major
  c''2 g'2 |                                 % m.13
  r2 r4 g'4 |                                % m.14 (3 beats rest)
  bf'2 f'2 |                                 % m.15
  r1 |                                       % m.16
  \bar "|."
}

viola = {
  \global
  \clef alto
  c8 c8 c4 r2 r4 r4 |                        % m.12
  \time 4/4 \key f \major
  r4 c4 e4 g4 |                              % m.13 (C–E–G)
  c'4 d'4 ef'4 e'4 |                         % m.14 (C–D–Eb–E)
  f'4 a'4 c''4 f'4 |                         % m.15 (F–A–C)
  f'4 f'4 f'4 a'4 |                          % m.16
  \bar "|."
}

cello = {
  \global
  \clef bass
  c,8 c,8 c,4 r2 r4 r4 |                     % m.12
  \time 4/4 \key f \major
  r4 c,4 e,4 g,4 |                           % m.13
  c4 d4 ef4 e4 |                             % m.14
  f4 a4 c'4 d'4 |                            % m.15
  ef'4 e'4 f'4 f'4 |                         % m.16
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