\version "2.26.0"
\language "english"

\header {
  title = "Keyboard Sonata No. 5 in G Major, K. 283 (189h)"
  subtitle = "I. Allegro (mm. 1–10)"
  composer = "Wolfgang Amadeus Mozart"
  tagline = ##f
}

% 依据 Humdrum Kern (0013-13-Piano Sonata No. 5 in G major, K 283 (189h), mvmt. 1.abc 第 25–46 行)
% 与 NMA 原版乐谱 (Graphics/form/k283.png) 重编码
% 修正记录：
% 1. mm. 5–6 左手转入高音谱表后恢复为原谱二分音符双音 <c' g'>2 与 <b g'>2，并保留第 3 拍四分休止符 r4（去除原交付件中错误添加的 E4/D4 及附点延长）；
% 2. m. 9 左手补回低音 D 音（D3）持续支撑与四六/属七和声级进解决（r4 << { g4 c4 } \\ { d,2 } >>）；
% 3. m. 10 修正相对音高下坠错误，落音为标准低音 G2 (MIDI 43)，消除了超出 88 键钢琴物理下限的 G-1 (MIDI 19) 严重错误。

global = {
  \key g \major
  \time 3/4
  \tempo "Allegro" 4 = 120
}

rightHand = \relative c'' {
  \global
  \clef treble
  \partial 4 d8.(\p b16) |
  d4 r4 g,4 |
  fs4 r4 a'8.( fs16) |
  a4 r4 c,4 |
  b4 r4 g'8.(\f fs16) |
  fs8( e8) e4 g8.( e16) |
  e8( d8) d4 g8.( d16) |
  d4-.\p d4-. d4-. |
  d16( e fs g a b c d c b a g) |
  fs16( e d c b d b g a c a fs) |
  g4 r4 \bar "||"
}

leftHand = \relative c {
  \global
  \clef bass
  \partial 4 r4 |
  g8(\p b d b d b) |
  a8( c d c d c) |
  fs,8( a d a d a) |
  g8( b d b) g4\f |
  \clef treble
  <c' g'>2\fp r4 |
  <b g'>2\fp r4 |
  \clef bass
  <a c'>4-.\p <g b>4-. <fs a>4-. |
  <g b>4 r4 <e g>4 |
  r4 << { g4 c4 } \\ { d,2 } >> |
  <g b>4 g,4 r4 \bar "||"
}

\score {
  \new PianoStaff \with {
    instrumentName = "Piano"
    midiInstrument = "acoustic grand"
  } <<
    \new Staff = "upper" { \rightHand }
    \new Staff = "lower" { \leftHand }
  >>
  \layout { }
  \midi { }
}
