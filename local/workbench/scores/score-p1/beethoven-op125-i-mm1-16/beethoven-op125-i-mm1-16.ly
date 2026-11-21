\version "2.26.0"
\language "english"

% 贝多芬 第九交响曲 Op.125 第一乐章 Allegro ma non troppo, un poco maestoso，mm.1–16
%% 底本：CCARH MuseData `sym9-mvmt1.md2`（K:-1、T:2/4、四分音符=88，依 Breitkopf & Härtel 转写）；
%%       per-part Q 已分别换算（弦乐 Q:24；圆号/小号/定音鼓 Q:8）。
%% 记谱约定：单簧管 in B♭、圆号 in D、小号 in D 一律写成**实音**（不写 \transposition）；
%%           弦乐 tremolo 按底本时值（每音 1/6 四分音符）折叠为一个十六分三连音组。
global = {
  \key d \minor
  \time 2/4
  \tempo "Allegro ma non troppo" 2 = 88
}

% ---- Flauti 1, 2 ----
flauti = {
  \global
  \clef treble
  \set Staff.midiInstrument = "flute"
  <<
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | a''2 | a''2 | e'''2 | e'''4. a'''8 | a'''2 | a'''4~ a'''8.. d'''32 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | a''2 | a''4. a''8 | a''2 | a''4~ a''8.. d''32 | }
  >>
}

% ---- Oboe 1, 2 ----
oboi = {
  \global
  \clef treble
  \set Staff.midiInstrument = "oboe"
  <<
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | e''2 | e''2 | e''2 | e''2 | e''2 | e''4. a''8 | a''2 | a''4~ a''8.. d'''32 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 r8 a'8 | a'2 | a'4~ a'8.. d''32 | }
  >>
}

% ---- Clarinetti 1, 2 in B♭（实音） ----
clarinetti = {
  \global
  \clef treble
  \set Staff.midiInstrument = "clarinet"
  <<
    { r2 | r2 | r2 | r2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'4. a'8 | a'2 | a'4~ a'8.. d'''32 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 r8 a8 | a2 | a4~ a8.. d''32 | }
  >>
}

% ---- Fagotto 1, 2 ----
fagotti = {
  \global
  \clef bass
  \set Staff.midiInstrument = "bassoon"
  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  a,2 |

  a,8 d,4. |

  d,4~ d,8.. d'32 |

}

% ---- Corni 1, 2 in D（实音） ----
corni = {
  \global
  \clef treble
  \set Staff.midiInstrument = "french horn"
  <<
    { e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'4. a'8 | a'2 | a'4~ a'8.. d''32 | }
    \\
    { a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a4. a,8 | a,2 | a,4~ a,8.. d'32 | }
  >>
}

% ---- Trombe 1, 2 in D（实音） ----
trombe = {
  \global
  \clef treble
  \set Staff.midiInstrument = "trumpet"
  <<
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 r8 r16. d'32 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | d32 r4. r16. | }
  >>
}

% ---- Timpani in D, A ----
timpani = {
  \global
  \clef bass
  \set Staff.midiInstrument = "timpani"
  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r2 |

  r4 r8 r16. d32 |

}

% ---- Violino I ----
violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  r2 |

  r4 r8 r16. e''32 |

  a'4 r8 r16. a'32 |

  e'4 r4 |

  r2 |

  r4 r8 r16. a''32 |

  e''4 r8 r16. e''32 |

  a'4 r4 |

  r2 |

  r2 |

  r8 r16. a''32 e''8 r16. e''32 |

  a'8 r16. a'32 e'8 r8 |

  r16 a''16 a''16 e''16 r16 e''16 e''16 a'16 |

  r16 a'16 a'16 e'16 r4 |

  r16 a''16 a''16 a'16 a'16 a16 a16 a'16 |

  a'16 a''16 a''16 a'16 a'16 a''16 a'16 r32 d'''32 |

}

% ---- Violino II ----
violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  <<
    { \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } | \tuplet 3/2 { e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 e'16 } \tuplet 3/2 { a'16 a'16 a'16 } | \tuplet 3/2 { a'16 a'16 a'16 a'16 a'16 a'16 a'16 a'16 a'16 a'16 a'16 a'16 } | \tuplet 3/2 { a'16 a'16 a'16 a'16 a'16 a'16 a'16 a'16 a'16 } a'16 r32 d'''32 | }
    \\
    { \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 } a16 r16 | }
  >>
}

% ---- Viola ----
viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  r2 |

  r2 |

  r2 |

  r4 r8 r16. e'32 |

  a4 r4 |

  r2 |

  r2 |

  r4 r8 r16. e'32 |

  a4 r4 |

  r2 |

  r2 |

  r4 r8 r16. e'32 |

  a8 r8 r4 |

  r4 r16 e'16 e'16 a16 |

  r4 r16 a'16 a'16 a16 |

  a16 a'16 a'16 a16 a16 a'16 a16 r32 d''32 |

}

% ---- Violoncello ----
violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  <<
    { \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 e16 } | \tuplet 3/2 { e16 e16 e16 e16 e16 e16 e16 e16 e16 } \tuplet 3/2 { a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 a16 } | \tuplet 3/2 { a16 a16 a16 a16 a16 a16 a16 a16 a16 } a16 r32 d'32 | }
    \\
    { \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } | \tuplet 3/2 { a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 a,16 } a,16 r16 | }
  >>
}

% ---- Contrabasso ----
contrabass = {
  \global
  \clef bass
  \set Staff.midiInstrument = "contrabass"
  r2 |

  r2 |

  r2 |

  r4 r8 r16. e32 |

  a,4 r4 |

  r2 |

  r2 |

  r4 r8 r16. e32 |

  a,4 r4 |

  r2 |

  r2 |

  r4 r8 r16. e32 |

  a,8 r8 r4 |

  r4 r16 e16 e16 a,16 |

  r2 |

  r4 r8 r16. d'32 |

}

#(set-global-staff-size 13)
\paper { #(set-paper-size "a4landscape") }

\score {
  <<
    \new StaffGroup <<
      \new Staff \flauti
      \new Staff \oboi
      \new Staff \clarinetti
      \new Staff \fagotti
      \new Staff \corni
      \new Staff \trombe
      \new Staff \timpani
      \new Staff \violinoI
      \new Staff \violinoII
      \new Staff \viola
      \new Staff \violoncello
      \new Staff \contrabass
    >>
  >>
  \layout { ragged-right = ##f }
  \midi { }
}
