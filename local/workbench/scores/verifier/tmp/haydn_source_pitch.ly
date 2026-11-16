\version "2.26.0"
\language "nederlands"

% 核验辅助：Haydn Mutopia 源文件 mm.1-8 原样摘录
% 来源 hob-xvi-27-iii-presto.ly 第 32-45 行（MD 第一结尾）与第 254-266 行（MS 前 8 小节）
% 说明：原文件 `-|` 记号在 2.26 中不合法（该源文件为 2.16 语法），故仅删除不影响音高时值的 `-|`，
%       所有音名、八度记号、时值、和弦、谱号切换保持与源完全一致。
% 源文件第 3 行为 \include "nederlands.ly"，故此处同样使用荷兰语（fis/dis/cis/bes）。

Treble = \clef treble
Bass = \clef bass

MD = \relative c' {
  \key g \major \time 2/4 \partial 8
  d8
  g ( b d  g,)
  g4 ( fis8) d
  a' ( c e <a, c>)
  <a  c>4( < g b>8\noBeam b)
  b' ( g dis  e)
  a ( fis cis  d!)
  e8 ( g4) cis,8
  d4\mordent r8
}

MS = \relative c' {
  r8
  <g b>4 r8 <b d>
  <a c>4 r
  r r8 fis
  g4 g,8 r
  \Treble g''4 r8 g
  fis4 r8 fis
  g4 a
  \Bass d, d,8
}

\displayLilyMusic \MD
\displayLilyMusic \MS
