\version "2.26.0"
\language "english"

% ============================================================
% 作品：Ludwig van Beethoven - String Quartet No. 10 in E-flat Major, Op. 74
%       ("Harp")
% 片段：I. Poco Adagio，mm. 18–24（慢引子尾声：半音攀升与多重挂留和声链，
%       衔接 m.25 Allegro 主部）
% 来源：Humdrum/Kern quartet10-1.krn（craigsapp/beethoven-string-quartets）
%       行 138–173（=18 至 =24），第一乐章，E-flat 大调
% 拍号：原谱为 2/2（DCML n10op74_01 的 timesig=2/2）；kern 按 4/4 记小节，
%       每小节同为 4 个四分音符，故本谱按原谱 2/2 记，速度沿用 kern *MM72
%       记作 4 = 72（2/2 下等价于二分音符=36）。
% 声部：Violin I (GM 40), Violin II (GM 40), Viola (GM 41),
%       Violoncello (GM 42)
% 记谱：本片段用绝对音高（c' = C4）。小提琴 I 在 m.18 有 C♭5→D4 的下行大跳，
%       \relative 模式的"最近音"规则会把 D4 错选成 D5，因此与已交付的
%       beethoven-op74-mvt1-mm1-9-adagio.ly 一致采用绝对音高。
% 核对：逐音与 kern 及 DCML annotations（n10op74_01.notes.tsv 的 midi 列）
%       比对一致；连音线/延音线/力度（p）取自 kern。
% ============================================================

\header {
  title = "String Quartet No. 10 in E-flat Major, Op. 74 (\"Harp\")"
  subtitle = "I. Poco Adagio (mm. 18–24)"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

global = {
  \key ef \major
  \time 2/2
  \tempo "Poco Adagio" 4 = 72
}

violinOne = {
  \global
  \clef treble
  cf''2\p( d'4. ef'8) |
  ef'4.( ff'8) ff'4.( f'8) |
  f'4.( gf'8) gf'4.( g'8) |
  g'4.( af'8) af'4.( a'8) |
  a'4.( bf'8) bf'4.( cf''8) |
  cf''4.( c''8) df''2~ |
  df''4.( d''8) d''4. ef''8 |
  \bar "||"
}

violinTwo = {
  \global
  \clef treble
  cf'1\p~ |
  cf'1 |
  df'1 |
  df'4.( ef'8) f'4.( gf'8) |
  gf'4.( g'8) df'4.( cf'8) |
  ef'2 e'2~ |
  e'4.( f'8) <bf f'>4.~ <bf ef'>8 |
  \bar "||"
}

viola = {
  \global
  \clef alto
  af1\p |
  af1 |
  bf1 |
  bf4.( cf'8) cf'4.( c'8) |
  c'4.( df'8) ff'4.( ef'8) |
  r4 gf4( g2~) |
  g4. af8 af4. g8 |
  \bar "||"
}

cello = {
  \global
  \clef bass
  r1 |
  r1 |
  r1 |
  af,2\p( d,4. ef,8) |
  ef2( g,4. af,8) |
  gf2( a,4. bf,8) |
  bf,2 bf,4.( ef8) |
  \bar "||"
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