\version "2.26.0"
\language "english"

\header {
  title = "Brandenburg Concerto No. 5 in D major, BWV 1050"
  subtitle = "I. Allegro — mm. 1–9 (tutti, baroque polarity and continuo scaffolding)"
  location = "Score example 1: mm. 1–9"
  composer = "Johann Sebastian Bach"
  tagline = ##f
}

% 谱源：
%   local/origin_resources/downloads/2026-11-17/s3/bwv1050-1.krn
%   （MuseData / CCARH, Humdrum **kern, BWV 1050 Movement 1, Eulenburg 版转录；经 GitHub musedata/humdrum-bach-brandenburg 下载）
% 音高/时值经自写 krn2ly 转换（绝对音名、显式升降号）并逐小节比对 kern 原文；编译后经 MIDI 反查。
% 声部：Flauto traverso, Violino principale, Violino di ripieno, Viola di ripieno,
%       Violoncello, Violone, Cembalo concertato（本谱例的大键琴以右手/左手两行呈现，
%       kern 的第三行 cemba2 与大键琴高声部和弦重叠，故从略——记录中说明）。
% 拍号 2/2（alla breve）；调号 D 大调（F#, C#）；速度 二分音符 = 66。
% GM：Flute=73, Violin=40(x2), Viola=41, Cello=42, Acoustic Bass=32, Harpsichord=6。

global = {
  \key d \major
  \time 2/2
  \tempo "Allegro" 2 = 66
}

flauto = {
  \global
  \clef treble
  |
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  r8 d''8 cs''8 b'8 a'2
  \bar "|."
}

violinoPrincipale = {
  \global
  \clef treble
  |
  d'16 d'16 fs'16 fs'16 a'16 a'16 d''16 d''16 cs''16 d''16 cs''16 b'16 a'16 g'16 fs'16 e'16 |
  d'16 d'16 fs'16 fs'16 a'16 a'16 d''16 d''16 e''8 a'8 r8 e''8 |
  fs''16 fs''16 e''16 e''16 g''16 g''16 fs''16 fs''16 b''16 b''16 a''16 a''16 cs''16 cs''16 d''16 d''16 |
  g'16 g'16 fs'16 fs'16 b'16 b'16 a'16 a'16 cs'16 cs'16 d'16 d'16 a16 a16 g'16 g'16 |
  fs'16 e'16 fs'16 d'16 e'16 e'16 a16 a16 d'16 e'16 fs'16 g'16 a'16 b'16 cs''16 a'16 |
  d''16 d''16 cs''16 cs''16 e''16 e''16 d''16 d''16 g''16 g''16 fs''16 fs''16 b''16 b''16 a''16 a''16 |
  g''16 fs''16 e''16 d''16 e''8 a'16 b'16 c''16 a'16 b'16 d''16 cs''16 e''16 a'16 g'16 |
  fs'16 d'16 e'16 g'16 fs'16 a'16 d'16 cs'16 b16 g'16 fs'16 e'16 e'8. d'16 |
  d'8 r8 r4 r8 fs''8 e''8 d''8
  \bar "|."
}

violinoRipieno = {
  \global
  \clef treble
  |
  d'16 d'16 fs'16 fs'16 a'16 a'16 d''16 d''16 cs''16 d''16 cs''16 b'16 a'16 g'16 fs'16 e'16 |
  d'16 d'16 fs'16 fs'16 a'16 a'16 d''16 d''16 e''8 a'8 r8 e''8 |
  fs''16 fs''16 e''16 e''16 g''16 g''16 fs''16 fs''16 b''16 b''16 a''16 a''16 cs''16 cs''16 d''16 d''16 |
  g'16 g'16 fs'16 fs'16 b'16 b'16 a'16 a'16 cs'16 cs'16 d'16 d'16 a16 a16 g'16 g'16 |
  fs'16 e'16 fs'16 d'16 e'16 e'16 a16 a16 d'16 e'16 fs'16 g'16 a'16 b'16 cs''16 a'16 |
  d''16 d''16 cs''16 cs''16 e''16 e''16 d''16 d''16 g''16 g''16 fs''16 fs''16 b''16 b''16 a''16 a''16 |
  g''16 fs''16 e''16 d''16 e''8 a'16 b'16 c''16 a'16 b'16 d''16 cs''16 e''16 a'16 g'16 |
  fs'16 d'16 e'16 g'16 fs'16 a'16 d'16 cs'16 b16 g'16 fs'16 e'16 e'8. d'16 |
  d'8 r8 r4 r2
  \bar "|."
}

viola = {
  \global
  \clef alto
  |
  fs'4 r8 fs'8 e'8 d'8 e'8 cs'8 |
  d'8 a8 d'8 fs'8 cs'8 d'8 e'8 cs'8 |
  d'8 a'8 d''8 cs''8 d''8 d'8 g'8 fs'8 |
  e'8 d'8 d'8 d'8 g'8 fs'8 e'8 a8 |
  a8 d'8 b8 cs'8 d'16 e'16 fs'16 g'16 a'16 b'16 cs''16 a'16 |
  d''8 fs'8 b'8 a'8 cs'8 d'8 e'8 cs'8 |
  d'8 a'8 b'8 cs''8 a'8 g'16 fs'16 e'8 e'8 |
  a8 a8 a8 a8 d8 d'8 cs'8 g'8 |
  fs'8 r8 r4 r2
  \bar "|."
}

violoncello = {
  \global
  \clef bass
  |
  d4 r8 d8 a8 b8 cs'8 a8 |
  fs8 e8 fs8 d8 a8 b8 cs'8 a8 |
  d'8 cs'8 b8 a8 g8 fs8 e8 d8 |
  cs8 d8 g,8 fs,8 e,8 d,8 cs,8 cs8 |
  d8 b,8 g,8 a,8 b,16 cs16 d16 e16 fs16 g16 a16 fs16 |
  b8 a8 g8 fs8 e8 d8 cs8 a,8 |
  d8 fs8 g8 a16 g16 fs8 g8 r8 cs16 cs16 |
  d16 d16 cs16 cs16 d16 d16 fs,16 fs,16 g,8 g8 a8 a,8 |
  d4 r4 r2
  \bar "|."
}

violone = {
  \global
  \clef bass
  |
  d,4 r8 d,8 a,8 b,8 cs8 a,8 |
  fs,8 e,8 fs,8 d,8 a,8 b,8 cs8 a,8 |
  d8 cs8 b,8 a,8 g,8 fs,8 e,8 d,8 |
  cs,8 d,8 g,8 fs,8 e,8 d,8 cs,8 a,,8 |
  d,8 b,,8 g,,8 a,,8 b,,16 cs,16 d,16 e,16 fs,16 g,16 a,16 fs,16 |
  b,8 a,8 g,8 fs,8 e,8 d,8 cs,8 a,,8 |
  d,8 fs,8 g,8 a,16 g,16 fs,8 g,8 r8 cs,16 cs,16 |
  d,16 d,16 cs,16 cs,16 d,16 d,16 fs,,16 fs,,16 g,,8 g,8 a,8 a,,8 |
  d,,4 r4 r2
  \bar "|."
}

cembaloUpper = {
  \global
  \clef treble
  |
  <d'' a' fs' d'>4 r4 r2 |
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  r16 a''32 g''32 fs''16 a''16 e''16 a''16 d''16 a''16 cs''16 a''16 d''16 a''16 cs''16 a''16 b'16 a''16
  \bar "|."
}

cembaloLower = {
  \global
  \clef bass
  |
  d4 r8 d8 a8 b8 cs'8 a8 |
  fs8 e8 fs8 d8 a8 b8 cs'8 a8 |
  d'8 cs'8 b8 a8 g8 fs8 e8 d8 |
  cs8 d8 g,8 fs,8 e,8 d,8 cs,8 cs8 |
  d8 b,8 g,8 a,8 b,16 cs16 d16 e16 fs16 g16 a16 fs16 |
  b8 a8 g8 fs8 e8 d8 cs8 a,8 |
  d8 fs8 g8 a16 g16 fs8 g8 r8 cs16 cs16 |
  d16 d16 cs16 cs16 d16 d16 fs,16 fs,16 g,8 g8 a8 a,8 |
  d4 r4 r2
  \bar "|."
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Flauto" midiInstrument = "flute" } { \flauto }
    \new Staff \with { instrumentName = "Vl. principale" midiInstrument = "violin" } { \violinoPrincipale }
    \new Staff \with { instrumentName = "Vl. di ripieno" midiInstrument = "violin" } { \violinoRipieno }
    \new Staff \with { instrumentName = "Viola" midiInstrument = "viola" } { \viola }
    \new Staff \with { instrumentName = "Violoncello" midiInstrument = "cello" } { \violoncello }
    \new Staff \with { instrumentName = "Violone" midiInstrument = "contrabass" } { \violone }
    \new PianoStaff <<
      \new Staff \with { instrumentName = "Cembalo" midiInstrument = "harpsichord" } { \cembaloUpper }
      \new Staff \with { midiInstrument = "harpsichord" } { \cembaloLower }
    >>
  >>
  \layout { }
  \midi { }
}