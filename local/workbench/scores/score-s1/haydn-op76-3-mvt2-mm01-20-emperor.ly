\version "2.26.0"
\language "english"

% ============================================================
% 作品：Joseph Haydn - String Quartet in C major, Hob.III:77, Op. 76 No. 3
%       ("Emperor" / "Kaiser")
% 片段：II. Poco adagio; cantabile —— 主题呈示 mm. 1–20（含前导弱起小节）
% 来源：OpenScore String Quartets 语料（CC0），文件 sq20428156.mxl
%       （github.com/OpenScore/StringQuartets，scores/Haydn,_Joseph/
%        String_Quartet_in_C_major,_Hob.III77,_Op.76_No.3/sq20428156.mxl；
%        下载件：scholar-plan-dev\local\origin_resources\downloads\2026-11-17\s1\haydn-op76-3.mxl）
%       经 musicxml2ly 转换并逐小节核对；另以 MusicXML 原始 <note>/<direction>
%       数据交叉提取（本地 _haydn 工作副本）。
% 声部：Violin I (GM 40), Violin II (GM 40), Viola (GM 41), Violoncello (GM 42)
% 拍/调：2/2，G 大调
% 速度：Poco adagio; cantabile。数字 4 = 56 为**推定值**（源无 <metronome>，
%       仅有播放用 <sound tempo="80">），非源数据，引用时勿当作原谱标记。
% 记谱：绝对音高（c' = C4）。
% 范围说明：本片段为“主题呈示”段（前导弱起 + mm.1–20），非全乐章；
%       变奏一（mm.21–40）等未含。
% ============================================================

\header {
  title = "String Quartet in C major, Hob.III:77, Op. 76 No. 3 (\"Emperor\")"
  subtitle = "II. Poco adagio; cantabile — theme, mm. 1–20 (with upbeat)"
  composer = "Joseph Haydn"
  tagline = ##f
}

global = {
  \key g \major
  \time 2/2
  % 待核：4 = 56 无谱面依据（OpenScore 源无 <metronome>，仅 <sound tempo="80">），
  % 此处按“推定”保留，供排版示意；正文引用时请说明为推定值。
  \tempo "Poco adagio; cantabile" 4 = 56
}

violinOne = {
  \global
  \clef treble
  \partial 2
  g'4. a'8 |
  b'4 a'4 c''4 b'4 |
  a'8 fs'8 g'4 e''4 d''4 |
  c''4 b'4 a'4 b'8 g'8 |
  d''2 g'4. a'8 |
  b'4 a'4 c''4 b'4 |
  a'8 fs'8 g'4 e''4 d''4 |
  c''4 b'4 a'4 b'8 g'8 |
  d''2 a'4 b'4 |
  a'8 fs'8 d'4 c''4 b'4 |
  a'8 fs'8 d'4 d''4 c''4 |
  b'4. b'8 cs''4 cs''8 d''8 |
  d''2\fermata g''4.\fz fs''8 |
  fs''8 e''8 d''4 e''4. d''8 |
  d''8 c''8 b'4 a'4.\p b'16 c''16 |
  d''8 e''8 c''8 a'8 g'4 \grace b'8 a'8 g'8 |
  g'2 g''4.\fz fs''8 |
  fs''8 e''8 d''4 e''4. d''8 |
  d''8 c''8 b'4 a'4. b'16 c''16 |
  d''8 e''8 c''8 a'8 g'4 \grace b'8 a'8 g'8 |
  g'2 \once \omit Rest r2 |
}

violinTwo = {
  \global
  \clef treble
  \partial 2
  b4. d'8 |
  g'4 fs'4 a'4 g'4 |
  c'4 b4 c''4 b'4 |
  fs'4 g'4 e'2 |
  d'2 b4. d'8 |
  g'4 fs'4 a'4 g'4 |
  c'4 b4 c''4 b'4 |
  fs'4 g'4 e'2 |
  d'2 fs'4 g'4 |
  fs'4 r4 fs'4 g'4 |
  fs'4 r4 b'4 a'4 |
  g'2. g'8 fs'8 |
  fs'2 <g g'>4. g'8 |
  g'8. a'16 b'4 c''4. b'8 |
  fs'4 g'4 fs'4. g'16 a'16 |
  g'4 e'8 a'8 g'4 fs'4 |
  g'2 <g g'>4. g'8 |
  g'8. a'16 b'4 c''4. b'8 |
  fs'4 g'4 fs'4. g'16 a'16 |
  g'4 e'8 a'8 g'4 fs'4 |
  g'2 \once \omit Rest r2 |
}

viola = {
  \global
  \clef alto
  \partial 2
  g4 r4 |
  r2 d'4 d'4 |
  fs8 a8 g4 r2 |
  a4 b4 e'4 g4 |
  fs2 g4 r4 |
  r2 d'4 d'4 |
  fs8 a8 g4 r2 |
  a4 b4 e'4 g4 |
  fs2 d'4 d'4 |
  d'4 r4 a4 g8 b8 |
  d'4 r4 d'4 e'8 fs'8 |
  g'4 g4 e'4 e'8 d'8 |
  d'2 <g d'>2 |
  e'8. fs'16 g'4 g'4. g'8 |
  <d' a'>4 <d' b'>4 d'2 |
  g4 e'8 c'8 b4 \grace d'8 c'4 |
  b2 <g d'>2 |
  e'8. fs'16 g'4 g'4. g'8 |
  <d' a'>4 <d' b'>4 d'2 |
  g4 e'8 c'8 b4 \grace d'8 c'4 |
  b2 \once \omit Rest r2 |
}

cello = {
  \global
  \clef bass
  \partial 2
  g4 r4 |
  r2 f4 g4 |
  d4 g,4 r2 |
  d4 g4 c4 cs4 |
  d2 g4 r4 |
  r2 f4 g4 |
  d4 g,4 r2 |
  d4 g4 c4 cs4 |
  d2 d4 d4 |
  d4 r4 d4 d4 |
  d4 r4 b,4 c8 d8 |
  e2 a,4 a,4 |
  d2 b4. b8 |
  c'4 g4 c4. g8 |
  d4 g4 c2 |
  b,4 c4 d4 d4 |
  g,2 b4. b8 |
  c'4 g4 c4. g8 |
  d4 g4 c2 |
  b,4 c4 d4 d4 |
  g,2 \once \omit Rest r2 |
}

\score {
  \new StaffGroup <<
    \new Staff \with {
      instrumentName = "Violin I (GM 40)"
      midiInstrument = "violin"
    } { \violinOne }
    \new Staff \with {
      instrumentName = "Violin II (GM 40)"
      midiInstrument = "violin"
    } { \violinTwo }
    \new Staff \with {
      instrumentName = "Viola (GM 41)"
      midiInstrument = "viola"
    } { \viola }
    \new Staff \with {
      instrumentName = "Violoncello (GM 42)"
      midiInstrument = "cello"
    } { \cello }
  >>
  \layout { }
  \midi { }
}