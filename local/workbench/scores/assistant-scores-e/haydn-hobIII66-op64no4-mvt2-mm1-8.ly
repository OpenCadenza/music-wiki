\version "2.26.0"
\language "english"

\header {
  title = "String Quartet in G major, Hob. III:66 (Op. 64 No. 4)"
  subtitle = "II. Menuetto (Allegretto) — mm. 1–8, with upbeat"
  location = "mm. 1–8 (with anacrusis)"
  composer = "Joseph Haydn"
  tagline = ##f
}

% ─────────────────────────────────────────────────────────────────────────────
% 作品：Joseph Haydn, String Quartet in G major, Hob. III:66 = Op. 64 No. 4
% 乐章：II. Menuetto, Allegretto（G 大调，3/4 拍，弱起 1 拍：D5–B4 两个八分音符）
% 谱源：
%   1) OpenScore StringQuartets 转写（据 IMSLP #06556 / Eulenburg 版 Altmann 编订）
%      sq7249986.mxl → 逐小节核对 mm.0–8（four-part 全声部）
%   2) Open Music Theory 教材旧版库 Graphics/form/haydn-III-66-ii.png
%      （同一图示即本文所引用者，二谱表缩编本，作独立版本交叉核对）
% 编制与 GM 程序号 (0–127)：
%   Violin I: 40 (violin) | Violin II: 40 (violin) | Viola: 41 (viola) | Violoncello: 42 (cello)
% 调号：G 大调 (\key g \major)，拍号：3/4
% 速度：原谱仅印 "Allegretto"，无数字节拍机记号；此处 4 = 130 取自所用转写谱的
%       播放速度属性，仅供 MIDI 回放参考，非原谱标记。
% 结构：mm.1–4 先行句（m.4 达成半终止 HC，V 和弦 D–F#–A）
%       mm.5–8 扩充终止进行 ECP：m.5 I6(G/B) → m.6 ii6/5(C 低音) → m.7 V(D 属七) → m.8 I(G)
% 说明：旋律用绝对音高书写（不使用 \relative），以杜绝八度漂移。
% ─────────────────────────────────────────────────────────────────────────────

global = {
  \key g \major
  \time 3/4
  \tempo "Allegretto" 4 = 130
}

violinOne = {
  \global
  \clef treble
  \partial 4
  d''8(\f b'8) |
  fs'8( g'8) d'4-. b''8( g''8) |          % m.1  BI（半音级进动机）
  fs''8( a''8) c''4-. a'8( c''8) |        % m.2  CI
  c''16( b'16) r8 d''16( c''16) r8 e''16( c''16) r8 |  % m.3
  a'2 d'4\p |                             % m.4  半终止（HC）
  g'2( b'8 gs'8) |                        % m.5  I6
  b'8( a'8) c''4-. c''8( b'8) |           % m.6  ii6/5
  \grace b'16 a'4( a'8 g'8 a'8 d'8) |     % m.7  V
  g'4 r2 |                                % m.8  I
  \bar "||"
}

violinTwo = {
  \global
  \clef treble
  \partial 4
  r4 |
  r4 d'4-.\f d'4-. |                      % m.1
  r4 fs'4-. fs'4-. |                      % m.2
  g'8-. r8 g'8-. r8 g'8-. r8 |            % m.3
  fs'2 r4 |                               % m.4
  r4 d'4-.\p d'4-. |                      % m.5
  e'4 r4 e'8( d'8) |                      % m.6
  c'2. |                                  % m.7
  b4 r2 |                                 % m.8
  \bar "||"
}

viola = {
  \global
  \clef alto
  \partial 4
  r4 |
  r4 b4-.\f b4-. |                        % m.1
  r4 a4-. a4-. |                          % m.2
  g8-. r8 e8-. r8 c8-. r8 |               % m.3
  d4-. r4 r4 |                            % m.4
  r4 g4-.\p f'4-. |                       % m.5
  e'4 r4 r4 |                             % m.6
  fs'2. |                                 % m.7
  g'4 r2 |                                % m.8
  \bar "||"
}

violoncello = {
  \global
  \clef bass
  \partial 4
  r4 |
  r4 g4-.\f g4-. |                        % m.1
  r4 d4-. d4-. |                          % m.2
  g8-. r8 e8-. r8 c8-. r8 |               % m.3
  d4-. d'4-. r4 |                         % m.4
  r4 b,4-.\p b,4-. |                      % m.5
  c4 r4 r4 |                              % m.6
  d4-. d4-. d4-. |                        % m.7
  g,4-. g4-. r4 |                         % m.8
  \bar "||"
}

\score {
  \new StaffGroup <<
    \new Staff \with {
      instrumentName = "Violin I"
      midiInstrument = "violin"          % GM 40
    } { \violinOne }

    \new Staff \with {
      instrumentName = "Violin II"
      midiInstrument = "violin"          % GM 40
    } { \violinTwo }

    \new Staff \with {
      instrumentName = "Viola"
      midiInstrument = "viola"           % GM 41
    } { \viola }

    \new Staff \with {
      instrumentName = "Violoncello"
      midiInstrument = "cello"           % GM 42
    } { \violoncello }
  >>
  \layout { }
  \midi { }
}
