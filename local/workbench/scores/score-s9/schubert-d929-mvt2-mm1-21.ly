\version "2.26.0"
\language "english"

% 舒伯特 D.929《降 E 大调第二钢琴三重奏》第二乐章，mm.1–21
% 源：pdmx 包中 "Trio pour piano violon et violoncelle op 100, 2e mvt"
%     （MuseScore 3.6.2 导出，4 声部 / 212 小节 / divisions=48）
% 调号 3 降（c 小调），拍号 2/4，唯一速度标记 "Andante con moto"（源为 <sound tempo="40"/>，
% 源无 <metronome>；MusicXML 的 sound tempo 以四分音符/分钟计，故记作 4 = 40）。
% 速度文字用 \mark 单独排（本机 LilyPond 在文字+节拍机组合标记的横向字形推进上会重叠）。

#(set-global-staff-size 18)

global = {
  \key c \minor
  \time 2/4
  \tempo 4 = 40
}

violin = {
  \global
  \clef treble
  \mark \markup { \bold "Andante con moto" }
  % mm.1–20 全休止（源 XML 每小节均为整小节休止）
  r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 |
  r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 |
  <g ef'>8-. <g ef'>8-. <g ef'>8-. <g ef'>16.\tenuto\accent( <af f'>32-.) |
}

cello = {
  \global
  \clef bass
  r2 | r2 |
  g4(-. g4-.) |
  \grace { af16 bf16 } c'4.( bf16 af16) |
  g8( ef'8) b8.( a32 b32) |
  c'2 |
  c'4. c'8 |
  c'16( bf8. g4) |
  g8( ef'8) b8.( a32 b32) |
  c'2 |
  ef'4( d'4) |
  d'16( g16~ g4 g8-.) |
  g4( a8. g16) |
  g4. g8->-. |
  g,4. g8->-. |
  g,4~ g,16( g,16-. a,16-. b,16-.) |
  c8-. ef'8->( c'8.) ef16( |
  d8) d8~( d16 ef32 f32) ef16-. d16-. |
  c8-. ef'8->( c'8.) ef16( |
  d8) d8~( d16 ef32 f32) ef16-. d16-. |
  c8-. c8-. c8-. c16.\tenuto\accent( f,32-.) |
}

pianoRH = {
  \global
  \clef treble
  <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>16.-> <c' f' af'>32-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>16.-> <c' f' af'>32-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. |
  <c' f' af'>8-. <c' f' af'>8-. <c' f' af'>8-. <c' f' af'>8-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <d' f' g'>8-. <d' f' g'>8-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>16.-> <c' f' af'>32-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. |
  <bf ef' g'>8-. <bf ef' g'>8-. <bf ef' g'>8-. <c' ef' g'>8-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <d' f' g'>8-. <d' f' g'>8-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. <c' ef' g'>8-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <d' g'>8-. <d' g'>8-. |
  <bf ef' g'>8-. <bf ef' g'>8-. <bf ef' g'>8-. <bf ef' g'>8-. |
  <c' ef' g'>8-. <c' ef' g'>8-. <a ef' a'>8-. <a ef' a'>8-. |
  <b d' g'>8-. <b d' g'>8-. <b d' g'>8-. r8 |
  r8 g'8->-. g4 |
  r8 g'8->-. g4~ |
  g8 <c' g' c''>8-. <c' g' c''>8-. <ef' g' c''>8-. |
  <d' af' c''>8-. <d' af' c''>8-. <f' b'>8-. <f' b'>8 |
  <ef' c''>8-. <ef' c''>8-. <ef' g' c''>8-. <ef' g' c''>8-. |
  <d' af' c''>8-. <d' af' c''>8-. <f' g' b'>8-. <f' g' b'>8 |
  <ef' g' c''>8-. r8 r4 |
}

pianoLH = {
  \global
  \clef bass
  c8 c8 c8 c16. f,32-. |
  c8 c8 c8 c16. f,32-. |
  c8 c8 c8 c8 |
  c8 c8 c8 c8 |
  c8 c8 g,8 g,8 |
  c8 c8 c8 c16. f,32-. |
  c8 c8 c8 c8 |
  ef8 ef8 ef8 c8 |
  g,8 g,8 g,8 g,8 |
  c8 c8 c8 c8 |
  c8 c8 bf,8 bf,8 |
  ef8 ef8 ef8 ef8 |
  c8 c8 c8 c8 |
  g,8 g,8 g,8 r8 |
  r8 g8 g,4 |
  r8 g8 g,8( f,8 |
  ef,8) ef,8 ef,8 ef,8 |
  f,8 f,8 g,8 g,8 |
  af,8 af,8 ef,8 ef,8 |
  f,8 f,8 g,8 g,8 |
  c,8 r8 r4 |
}

\score {
  \new StaffGroup <<
    \new Staff = "violin" \with {
      instrumentName = "Violin"
    } {
      \set Staff.midiInstrument = "violin"
      % GM 40
      \violin
    }
    \new Staff = "cello" \with {
      instrumentName = "Violoncello"
    } {
      \set Staff.midiInstrument = "cello"
      % GM 42
      \cello
    }
    \new PianoStaff = "piano" \with {
      instrumentName = "Piano"
    } <<
      \new Staff = "pianoRH" {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \pianoRH
      }
      \new Staff = "pianoLH" {
        \set Staff.midiInstrument = "acoustic grand"
        % GM 0
        \pianoLH
      }
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}

