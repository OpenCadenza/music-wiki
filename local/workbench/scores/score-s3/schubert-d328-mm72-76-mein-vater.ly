\version "2.26.0"
\language "english"

\header {
  title = "Erlkönig, D. 328 (Op. 1)"
  subtitle = "„Mein Vater, mein Vater, und hörest du nicht?“ — mm. 72–76"
  location = "Score example 4b: mm. 72–76 (son: E♭5 against pedal D)"
  composer = "Franz Schubert"
  tagline = ##f
}

% 谱源：Mutopia Project 工程源（C. F. Peters 版转录, Mutopia-2007/09/07-1030）
%   local/origin_resources/corpus/lilypond/SchubertF/D328/Erlkoenig/Erlkoenig.ly
% 按 Mutopia 源逐音重编为 2.26.0 语法；音高经工程 MIDI（Erlkoenig.mid, mm.72–76）逐事件验证：
%   - 女高/男高旋律（Voice, GM 54）：m.72 B♭4→D5；m.73–75 固定音 E♭5（= 降六级）反复；
%   - 钢琴右手：D4+D5 八度三连音持续（m.72 首组低音区 D3–F3–B♭3 跨谱表，后接 D4+D5）——属音踏板；
%   - 钢琴左手：低音八度半音导向 B♭1/B♭2 → B2/B3 → C3/C4 → A2/A3 → F♯2/F♯3（重属导向）；
%     m.73 与 m.75: C3/C4 与 A2/A3；m.74 与 m.76: F♯2/F♯3 与 B2/B3。
% 力度（Mutopia 工程力度层）：旋律与右手自 m.72 第 3 拍起 f，右手 m.76 第 3 拍起 p；
%   左手 m.72 起有 decresc（pince），本摘录从简未加斜面（见核对记录）。
% 歌词：依 Mutopia 注释 %72–85（„Mein Vater, mein Vater, und hörest du nicht, / Was Erlenkönig mir leise verspricht?“），
%   本摘录不铺排歌词文本（避免跨小节音节对齐的推测），旋律按音高与节奏如实编码。
% GM 程序：Voice = 54, Piano = 0。

global = {
  \key g \minor
  \time 4/4
  \tempo "Schnell" 4 = 154
}

voice = {
  \global
  \clef treble
  bf'2 r4 d''4 |                        % m.72
  ef''2 ef''4. ef''8 |                  % m.73
  ef''8( d''8) d''4 r4 d''4 |           % m.74
  ef''2 ef''4. ef''8 |                  % m.75
  d''2 r4 a'4 |                         % m.76
  \bar "|."
}

pianoUpper = {
  \global
  \clef treble
  \tuplet 3/2 { <d f bf>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] }
  \f \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } |   % m.72
  \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] }
  \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } |   % m.73
  \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] }
  \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } |   % m.74
  \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] }
  \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } |   % m.75
  \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] }
  \p \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } \tuplet 3/2 { <d' d''>8[ <d' d''> <d' d''>] } |   % m.76
  \bar "|."
}

pianoLower = {
  \global
  \clef bass
  <bf,, bf,>4 r2 <b, b>4 |             % m.72
  <c c'>2 <a, a>2 |                    % m.73
  <fs, fs>2 r4 <b, b>4 |               % m.74
  <c c'>2 <a, a>2 |                    % m.75
  <fs, fs>2 r4 fs'4 |                  % m.76
  \bar "|."
}

\score {
  \new StaffGroup <<
    \new Staff \with {
      instrumentName = "Voice"
      midiInstrument = "voice oohs"
    } { \voice }

    \new PianoStaff <<
      \new Staff \with {
        instrumentName = "Piano"
        midiInstrument = "acoustic grand"
      } { \pianoUpper }
      \new Staff \with {
        midiInstrument = "acoustic grand"
      } { \pianoLower }
    >>
  >>
  \layout { }
  \midi { }
}