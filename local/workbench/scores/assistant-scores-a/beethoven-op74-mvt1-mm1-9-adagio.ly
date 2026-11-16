\version "2.26.0"
\language "english"

\header {
  title = "String Quartet No. 10 in E-flat Major, Op. 74 (\"Harp\")"
  subtitle = "I. Poco adagio (mm. 1–9)"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% 依据 Humdrum Kern (quartet10-1.krn 第 23–77 行 = mm. 1–9) 与 DCML 权威校订重编码
% 修正记录（经三轮核验，最终判定「一致」）：
% 1. 第一小提琴 m. 9 十六分加花第 5 个改为 e'16 (E♮4)——DCML 与 kern 同小节均有还原号，原写 ef' 属误改；
%    第 9 个取 e''16 (E♮5)，此处 kern 记 16ee-（Eb5）、DCML 记 accidentalNatural（E♮5），两源 1:1 冲突，
%    采信 DCML（未校订的 MS3 原始件即含还原号；且该组为前四音 E-F-G-F 的原位八度移位，取 E♮ 保持模进一致）。
%    正文不得用这一音作半音阶立论。
% 2. 中提琴 m. 6 修正绝对音高八度偏差：cf''4 bf'4 c'4 (Cb5 / Bb4 / C4)，恢复向高音区穿插之原版对位；
% 3. 大提琴 mm. 6–7 修正低于乐器物理发音极限的八度错误：m. 6 末拍改为 a,4 (A2)，m. 7 改为 bf,1 (Bb2)，完全合规于四弦大提琴 C2–C6 物理音域。

global = {
  \key ef \major
  \time 2/2
  \tempo "Poco adagio" 4 = 72
}

violinOne = {
  \global
  \clef treble
  ef''2\p g'4. af'8 |
  df''4\fp r4 r2 |
  ef''2\p g'4. af'8 |
  df''1~\fp |
  df''2. d''4~ |
  d''2 ef''4 c''8( f''8) |
  ef''4( d''4 c''4 bf'4) |
  bf'4( af'8) r8 af'4( g'8) r8 |
  g'4~\fp g'16( f'16 e'16 f'16 e'16 f'16 g'16 f'16 e''16 f''16 g''16 f''16) |
  \bar "||"
}

violinTwo = {
  \global
  \clef treble
  g'2\p ef'4. ef'8 |
  ef'4\fp r4 r2 |
  g'2\p ef'4. ef'8 |
  e'4\fp r4 bf''2~ |
  bf''2 af''2~ |
  af''2 g''4 f''8( f'8) |
  f'2 af'4( g'4) |
  g'4( f'8) r8 bf4( bf8) r8 |
  c'4\fp r4 r2 |
  \bar "||"
}

viola = {
  \global
  \clef alto
  bf2\p bf4. af8 |
  g4\fp r4 r2 |
  bf2\p bf4. af8 |
  bf4\fp r4 r4 e'4~ |
  e'2 f'2~ |
  f'4 cf''4( bf'4 c'4) |
  af2 d4. ef8 |
  e4 f4 d4 ef4 |
  af4\fp r4 r4 af4~ |
  \bar "||"
}

cello = {
  \global
  \clef bass
  ef2\p df4. c8 |
  bf,4\fp r4 r2 |
  ef2\p df4. c8 |
  g,4\fp r4 r2 |
  f,2. bf,4 |
  ef,2. a,4 |
  bf,1 |
  c2 f,4. g,8 |
  af,4\fp r4 r4 f,4~ |
  \bar "||"
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
      instrumentName = "Cello"
      midiInstrument = "cello"
    } { \cello }
  >>
  \layout { }
  \midi { }
}
