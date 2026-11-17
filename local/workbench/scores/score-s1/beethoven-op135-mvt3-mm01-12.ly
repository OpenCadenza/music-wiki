\version "2.26.0"
\language "english"

% ============================================================
% 作品：Ludwig van Beethoven - String Quartet No. 16 in F major, Op. 135
% 片段：III. Lento assai, cantante e tranquillo —— mm. 1–12
% 来源（三源交叉核对）：
%  1) 本地 Humdrum/Kern：quartet16-3.krn（craigsapp/beethoven-string-quartets）
%     文件头：Mvmt. 3；Lento assai, cantante e tranquillo；*D-:；*M6/8；*MM40
%  2) 本地 DCML annotations：n16op135_03.notes.tsv（midi/duration_qb 逐音对照）
%  3) OpenScore String Quartets（CC0）sq12397213.mxl（MuseScore 转写，
%     用于裁定 m.7 次中音时值：A3 为附点四分）
% 声部：Violin I (GM 40), Violin II (GM 40), Viola (GM 41), Violoncello (GM 42)
% 拍/调：6/8，降 D 大调
% 速度：Lento assai, cantante e tranquillo（文章记八分音符 = 50）
% 记谱：绝对音高（c' = C4）；大提琴 mm.3–5 为双声部（低声部为进行低音，上声部为持续 A♭2）
% 说明：Kern 未附力度层，本谱不添加力度记号（文章所述 sotto voce/pp 为叙述性描述）。
% ============================================================

\header {
  title = "String Quartet No. 16 in F major, Op. 135"
  subtitle = "III. Lento assai, cantante e tranquillo (mm. 1–12)"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

global = {
  \key df \major
  \time 6/8
  \tempo "Lento assai, cantante e tranquillo" 8 = 50
}

violinOne = {
  \global
  \clef treble
  r2. |
  df'4.~ <df' f'>4. |
  df'8( c'8 bf8 af8 bf8 c'8) |
  df'8( ef'8 f'8) ef'4. |
  df'8( c'8 bf8 af8 bf8 c'8) |
  df'8( ef'8 f'8) f'8( ef'4) |
  f'4 f'8 f'8( df'8 bf8) |
  bf'4 bf'8 bf'8( gf'8 ef'8) |
  af'4 af'8 af'8( f'8 df'8) |
  af'8( f'8 ef'8) df'4. |
  df'4( c'8) df'8( f'8 gf'8) |
  af'8( f''8 ef''8) df''8( bf'8 gf'8) |
}

violinTwo = {
  \global
  \clef treble
  r4 r8 af4.~ |
  af4.~ af4. |
  af2.~ |
  af2. |
  af2.~ |
  af4. af8( c'8 bf8) |
  a4. bf4. |
  f'4 bf8~ bf4. |
  ef'4 <af ef'>8 af4. |
  df'4 c'8 af4.~ |
  af4. af8 df'4 |
  f'8 af'8 gf'8 f'8 df'8 df'8 |
}

viola = {
  \global
  \clef alto
  f2.~ |
  f4.~ f4. |
  f4.( gf4.) |
  f4. gf4. |
  f4.( gf4.) |
  f4 df8 c4 ef8~ |
  ef4 c8 df4. |
  d4 f8 gf4. |
  gf4 ef8 f4. |
  f4 gf8 f4. |
  f4 gf8 f4 df8 |
  df4 c8 f8 gf8 ef8 |
}

cello = {
  \global
  \clef bass
  r2. |
  r4 r8 <df, df>4. |
  << { af,2. } \\ { df,4. ef,4. } >> |
  << { af,2. } \\ { df,4. c,4. } >> |
  << { af,2. } \\ { df,4. ef,4. } >> |
  <df, af,>4. af,4 gf,8 |
  f,4. bf,4. |
  d,4. ef,4. |
  c,4. df,4 f,8 |
  af,4. df8 f,8 gf,8 |
  af,8 f8 ef8 df4 bf,8 |
  af,4. df8 df8 df8 |
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