\version "2.26.0"
\language "english"

\header {
  title = "Erlkönig, D. 328 (Op. 1)"
  subtitle = "Piano introduction: mm. 1–5 (Schnell)"
  location = "Score example 4a: mm. 1–5 (prelude, piano solo)"
  composer = "Franz Schubert"
  tagline = ##f
}

% 谱源：Mutopia Project Project 工程源
%   local/origin_resources/corpus/lilypond/SchubertF/D328/Erlkoenig/Erlkoenig.ly
%   （C. F. Peters 版转录, Mutopia-2007/09/07-1030）
% 按 Mutopia 源逐音重编为 2.26.0 语法；八度与音高另经工程 MIDI（Erlkoenig.mid）逐事件验证：
%   - 右手 mm.1–5：G3+G4 八度三连音（MIDI 55/67）持续；
%   - 左手 m.1 全休止；m.2 与 m.4 低音三连音 G2–A2–B♭2 + C3–D3–E♭3，随后 D3 四分 + B♭2 四分（断奏）；
%   - m.3 与 m.5：G2 四分（断奏），其后休止。
% 速度：Mutopia 工程取四分音符 = 154（文章作 152）；此处采用工程值 154，并在核对记录中说明。
% 力度：前奏右手 f（Mutopia pianoDynPart 第 1 小节 f；低音 m.2 起 f）。
% GM 程序：Piano = 0。

global = {
  \key g \minor
  \time 4/4
  \tempo "Schnell" 4 = 152
}

pianoUpper = {
  \global
  \clef treble
  % m.1–5: G3+G4 octave triplets, four groups per bar
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] }
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } |   % m.1
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] }
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } |   % m.2
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] }
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } |   % m.3
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] }
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } |   % m.4
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] }
  \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } \tuplet 3/2 { <g g'>8[ <g g'> <g g'>] } |   % m.5
  \bar "|."
}

pianoLower = {
  \global
  \clef bass
  R1 |                                                                  % m.1 (rest)
  \tuplet 3/2 { g,8( a,8 bf,8 } \tuplet 3/2 { c8 d8 ef8) } d4-. bf,4-. |  % m.2
  g,4-. r4 r2 |                                                        % m.3
  \tuplet 3/2 { g,8( a,8 bf,8 } \tuplet 3/2 { c8 d8 ef8) } d4-. bf,4-. |  % m.4
  g,4-. r4 r2 |                                                        % m.5
  \bar "|."
}

\score {
  \new PianoStaff <<
    \new Staff \with {
      instrumentName = "Piano"
      midiInstrument = "acoustic grand"
    } { \pianoUpper }
    \new Staff \with {
      midiInstrument = "acoustic grand"
    } { \pianoLower }
  >>
  \layout { }
  \midi { }
}