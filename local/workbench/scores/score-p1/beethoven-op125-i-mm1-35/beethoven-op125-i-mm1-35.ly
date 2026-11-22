\version "2.26.0"
\language "english"

% 贝多芬 第九交响曲 Op.125 第一乐章 Allegro ma non troppo, un poco maestoso，mm.1–35
%% 底本：CCARH MuseData `sym9-mvmt1.md2`（依 Breitkopf & Härtel 全集 / Bennion 2005；非 CC0）
%%       per-part Q 已分别换算（弦乐/木管/定音鼓 Q:24；圆号/小号 Q:8）；行首缩进音 = 和弦音。
%% 移调乐器写实音（不写 \transposition）：Cl in B♭ −2；Hn in D −10；Hn3,4 in B♭ basso −14；Tr in D +2；Cb −12。
%% 弦乐 tremolo 按底本实际时值（每音 1/6 四分音符）折叠为十六分三连音组。
global = {
  \key d \minor
  \time 2/4
  \tempo "Allegro ma non troppo, un poco maestoso" 4 = 88
}

% ---- Flauti 1, 2 ----
flauti = {
  \global
  \clef treble
  \set Staff.midiInstrument = "flute"
  <<
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | e'''2 | e'''4. a'''8 | a'''2 | a'''4~ a'''8.. d'''32 | a'''4~ a'''8.. f'''32 | d'''8.. a''32 f''8. a''32 f''32 | d''4~ d''16 f'''16 e'''16 d'''16 | a'''8 g'''8 e'''8 a'''8 | d'''8. r16 e'''8. r16 | f'''8. r16 r4 | g'''8. r16 a'''8. r16 | bf''4 g'''4 | g'''2 | g'''8 f'''8 ef'''8 d'''8 | cs'''8 r8 r4 | g'''4 e'''8.. f'''32 | f'''8 r8 r4 | a'''4 f'''8.. g'''32 | g'''8 r8 e'''4 | e'''4 f'''4 | f'''4 f'''8 r8 | a'''2 | a'''4 d'8 r8 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | a''2 | a''2 | a''2 | a''4. a''8 | a''2 | a''4~ a''8.. d''32 | a''4~ a''8.. f''32 | d''8.. a''32 f''8. a''32 f''32 | r2 | r2 | d'''8. r16 cs'''8. r16 | d'''8. r16 r4 | bf''8. r16 fs'''8. r16 | g''4 bf''4 | bf''2 | bf''8 bf''8 bf''8 bf''8 | bf''8 r8 r4 | e'''4 cs'''8.. d'''32 | d'''8 r8 r4 | f'''4 d'''8.. e'''32 | e'''8 r8 cs'''4 | cs'''4 d'''4 | d'''4 d'''8 r8 | a''2 | a''4 d'8 r8 | }
  >>
}

% ---- Oboe 1, 2 ----
oboi = {
  \global
  \clef treble
  \set Staff.midiInstrument = "oboe"
  <<
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | e''2 | e''2 | e''2 | e''2 | e''2 | e''4. a''8 | a''2 | a''4~ a''8.. d'''32 | a''4~ a''8.. f''32 | d''8.. a'32 f'8. a'32 f'32 | d'4~ d'16 f''16 e''16 d''16 | a''8 g''8 e''8 a''8 | d''8. r16 e''8. r16 | f''8. r16 r4 | g''8. r16 a''8. r16 | bf''2 | bf''2 | bf''8 bf''8 bf''8 bf''8 | bf''8 r8 r4 | g''4 e''8.. f''32 | f''8 r8 r4 | a''4 f''8.. g''32 | g''8 r8 cs'''4 | cs'''4 d'''4 | d'''4 d'''8 r8 | d'''2 | d'''8 r8 r4 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 r8 a'8 | a'2 | a'4~ a'8.. d''32 | a'4~ a'8.. f'32 | d'8.. a'32 f'8. a'32 f'32 | d'4~ d'16 f'16 e'16 d'16 | a'8 g'8 e'8 a'8 | d'8. r16 cs''8. r16 | d''8. r16 r4 | bf'8. r16 fs''8. r16 | g''2 | g''2 | g''8 f''8 ef''8 d''8 | cs''8 r8 r4 | e''4 cs''8.. d''32 | d''8 r8 r4 | f''4 d''8.. e''32 | e''8 r8 e''4 | e''4 f''4 | f''4 f''8 r8 | f''2 | f''8 r8 r4 | }
  >>
}

% ---- Clarinetti 1, 2 in B♭（实音） ----
clarinetti = {
  \global
  \clef treble
  \set Staff.midiInstrument = "clarinet"
  <<
    { r2 | r2 | r2 | r2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'2 | a'4. a'8 | a'2 | a'4~ a'8.. d'''32 | a''4~ a''8.. f''32 | d''8.. a'32 f'8. a'32 f'32 | d'4~ d'16 f''16 e''16 d''16 | a''8 g''8 e''8 a''8 | d''8. r16 e'8. r16 | f'8. r16 r4 | g'8. r16 a'8. r16 | bf'2 | bf'2 | bf'8 bf'8 bf'8 bf'8 | bf'8 r8 r4 | g'4 e'8.. f'32 | f'8 r8 r4 | a'4 f'8.. g'32 | g'8 r8 bf''4 | bf''4 f''4 | f''4 f''8 r8 | a''2 | a'2 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 r8 a8 | a2 | a4~ a8.. d''32 | a'4~ a'8.. f'32 | d'8.. a32 f8. a'32 f'32 | d'4~ d'16 f'16 e'16 d'16 | a'8 g'8 e'8 a'8 | d'8. r16 cs'8. r16 | d'8. r16 r4 | bf8. r16 fs'8. r16 | g'2 | g'2 | g'8 g'8 g'8 g'8 | g'8 r8 r4 | e'4 cs'8.. d'32 | d'8 r8 r4 | f'4 d'8.. e'32 | e'8 r8 bf'4 | bf'4 d''4 | d''4 d''8 r8 | a'2 | d'2 | }
  >>
}

% ---- Fagotto 1, 2 ----
fagotti = {
  \global
  \clef bass
  \set Staff.midiInstrument = "bassoon"
  <<
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | a,2 | a,8 d,4. | d,4~ d,8.. d'32 | a4~ a8.. f32 | d8.. a,32 f,8. a,32 f,32 | d,4~ d,16 f16 e16 d16 | a8 g8 e8 a8 | d'8. r16 a8. r16 | d8. r16 r4 | g8. r16 a8. r16 | bf2 | bf4. a8 | g8 f'8 ef'8 d'8 | cs'8 r8 r4 | g4 e8.. f32 | f8 r8 r4 | a4 f8.. g32 | g8 r8 g4 | g4 af4 | af4 a4 | a4 a,8 r8 | d4. r8 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | a,8 g,8 e,8 a,8 | d8. r16 a,8. r16 | d,8. r16 r4 | g8. r16 fs8. r16 | g2 | g4. a8 | g8 f8 ef8 d'8 | cs'8 r8 r4 | e4 cs8.. d32 | d8 r8 r4 | f4 d8.. e32 | e8 r8 g,4 | g,4 af,4 | af,4 a,4 | a,4 a,8 r8 | d4. r8 | }
  >>
}

% ---- Corni 1, 2 in D（实音） ----
corni = {
  \global
  \clef treble
  \set Staff.midiInstrument = "french horn"
  <<
    { e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'2 | e'4. a'8 | a'2 | a'4~ a'8.. d''32 | a'4~ a'8.. f'32 | d'8.. a32 f'8. a'32 f'32 | d'4~ d'16 f'16 e'16 d'16 | a'8 g'8 e'8 a'8 | d'8. r16 e'8. r16 | d'8. r16 r4 | d'8. r16 d'8. r16 | g'2 | g'2 | g'8 g'8 g'8 g'8 | g'8 r8 r4 | a2 | a8 r8 r4 | a2 | g'8 r8 e'4 | e'4 d'4 | d'4 f'8 r8 | a'2 | a2 | }
    \\
    { a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a2 | a4. a,8 | a,2 | a,4~ a,8.. d'32 | a4~ a8.. f32 | d8.. a,32 f8. a32 f32 | d4~ d16 f'16 e'16 d'16 | a'8 g'8 e'8 a'8 | d8. r16 a8. r16 | d8. r16 r4 | d8. r16 d8. r16 | r2 | r2 | r2 | r2 | a,2 | a,8 r8 r4 | a,2 | e'8 r8 e'4 | e'4 d4 | d4 d'8 r8 | a2 | d2 | }
  >>
}

% ---- Corno 3, 4 in B♭ basso（实音） ----
corniBassi = {
  \global
  \clef treble
  \set Staff.midiInstrument = "french horn"
  <<
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r8 d'4. | d'4~ d'8.. d'32 | d'4~ d'8.. d'32 | d'8.. d'32 d'8. d'32 d'32 | d'4~ d'16 r16 r8 | r2 | d'8. r16 r4 | d'8. r16 r4 | d'8. r16 d'8. r16 | r4 bf4 | bf2 | bf8 bf8 bf8 bf8 | bf8 r8 r4 | r2 | r2 | r2 | r4 bf4 | bf4 f'4 | f'4 f'8 r8 | r2 | r2 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r8 d4. | d4~ d8.. d32 | d4~ d8.. d32 | d8.. d32 d8. d32 d32 | d4~ d16 r16 r8 | r2 | d8. r16 r4 | d8. r16 r4 | d8. r16 d8. r16 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 bf,4 | bf,4 f4 | f4 f8 r8 | r2 | r2 | }
  >>
}

% ---- Trombe 1, 2 in D（实音） ----
trombe = {
  \global
  \clef treble
  \set Staff.midiInstrument = "trumpet"
  <<
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 r8 r16. d''32 | a'4~ a'8.. d''32 | d''8.. a'32 d''8. d''32 d''32 | d''4~ d''16 d''16 d''16 d''16 | a'8 a'8 a'8 a'8 | d''8 r8 a'8 r8 | d''8 r8 r4 | d''8 r8 d''8 r8 | g''8 r8 r4 | r2 | r2 | r8 a'16. a'32 a'8 a'8 | a'8 r8 r4 | a'8 a'16. a'32 a'8 a'8 | a'8 r8 r4 | a'8 r8 a'8 r8 | r4 d''8 r8 | r4 d''8 r8 | a'2 | r4 d'8 r8 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 r8 r16. d'32 | a4~ a8.. d'32 | d'8.. a32 d'8. d'32 d'32 | d'4~ d'16 d'16 d'16 d'16 | a8 a8 a8 a8 | d'8 r8 a8 r8 | d'8 r8 r4 | d'8 r8 d'8 r8 | g''8 r8 r4 | r2 | r2 | r8 a16. a32 a8 a8 | a8 r8 r4 | a8 a16. a32 a8 a8 | a8 r8 r4 | a8 r8 a8 r8 | r4 d'8 r8 | r4 d'8 r8 | a2 | r4 d'8 r8 | }
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
  a,4~ a,8.. d32 |
  d8 r16. a,32 d8 r16 d32 d32 |
  d8 r8 r16 d16 d16 d16 |
  a,8 a,8 a,8 a,8 |
  d8 r8 a,8 r8 |
  d8 r8 r4 |
  d8 r8 d8 r8 |
  r2 |
  r2 |
  r2 |
  r8 a,16. a,32 a,8 a,8 |
  a,8 r8 r4 |
  a,8 a,16. a,32 a,8 a,8 |
  a,8 r8 r4 |
  a,8 r8 a,8 r8 |
  r4 d8 r8 |
  r4 a,8 r8 |
  r4 a,8 r8 |
  d4 r4 |
}

% ---- Violino I ----
violinoI = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  <<
    { r2 | r4 r8 r16. e''32 | a'4 r8 r16. a'32 | e'4 r4 | r2 | r4 r8 r16. a''32 | e''4 r8 r16. e''32 | a'4 r4 | r2 | r2 | r8 r16. a''32 e''8 r16. e''32 | a'8 r16. a'32 e'8 r8 | r16 a''16 a''16 e''16 r16 e''16 e''16 a'16 | r16 a'16 a'16 e'16 r4 | r16 a''16 a''16 a'16 a'16 a16 a16 a'16 | a'16 a''16 a''16 a'16 a'16 a''16 a'16 r32 d'''32 | a''4~ a''8.. f''32 | d''8.. a'32 f'8. a'32 f'32 | d'4~ d'16 f''16 e''16 d''16 | a''8 g''8 e''8 a''8 | d''8. r16 <e'' a' e' cs'>8. r16 | <f'' a' d'>8. r16 r4 | <g'' bf' d'>8. r16 <a'' a' fs'>8. r16 | \grace { bf'16 } bf''2 | bf''4. a''8 | g''8 f''8 ef''8 d''8 | cs''8 r8 r4 | cs'8 r8 r4 | <f'' a' d'>8 r8 r4 | f'8 r8 r4 | <g'' cs'' e'>8 r8 bf''4 | bf''4 d'''4 | d'''4 <f'' a' d'>8 r8 | a''4~ a''16 bf''32 a''32 g''32 f''32 e''32 d''32 | cs''32 d''32 c''32 bf'32 a'32 g'32 f'32 e'32 d'8 r8 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | d'4~ d'16 r16 r8 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | }
  >>
}

% ---- Violino II ----
violinoII = {
  \global
  \clef treble
  \set Staff.midiInstrument = "violin"
  <<
    { \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } | \tuplet 3/2 { <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 <e' a>16 } \tuplet 3/2 { <a' a>16 <a' a>16 <a' a>16 } | \tuplet 3/2 { <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 } | \tuplet 3/2 { <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 <a' a>16 } <a' a>16 r32 d'''32 | a''4~ a''8.. f''32 | d''8.. a'32 f'8. a'32 f'32 | d'4~ d'16 f''16 e''16 d''16 | a''8 g''8 e''8 a''8 | d''8. r16 <e'' a' e' cs'>8. r16 | <f'' a' d'>8. r16 r4 | <g'' bf' d'>8. r16 <a'' a' fs'>8. r16 | \grace { <g g'>16 } <g'' bf'>2 | <g'' bf'>2 | <g'' bf'>8 g8 g8 bf'8 | <bf' g'>8 r8 r4 | cs''8 r8 r4 | <f'' a' d'>8 r8 r4 | <a' f'>8 r8 r4 | <g'' cs'' e'>8 r8 <e'' cs''>4 | <e'' cs''>4 <f'' d''>4 | <f'' d''>4 <f'' d''>4 | <f'' d''>4~ \tuplet 3/2 { <f'' d''>16 } \tuplet 3/2 { <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 } | \tuplet 3/2 { <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 <a' d'>16 } | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | d'4~ d'16 r16 r8 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | }
  >>
}

% ---- Viola ----
viola = {
  \global
  \clef alto
  \set Staff.midiInstrument = "viola"
  <<
    { r2 | r2 | r2 | r4 r8 r16. e'32 | a4 r4 | r2 | r2 | r4 r8 r16. e'32 | a4 r4 | r2 | r2 | r4 r8 r16. e'32 | a8 r8 r4 | r4 r16 e'16 e'16 a16 | r4 r16 a'16 a'16 a16 | a16 a'16 a'16 a16 a16 a'16 a16 r32 d''32 | a'4~ a'8.. f'32 | d'8.. a32 f8. a32 f32 | d4~ d16 f'16 e'16 d'16 | a'8 g'8 e'8 a'8 | d'8. r16 <a' a>8. r16 | <d' d>8. r16 r4 | <g' g>8. r16 d'8. r16 | g8 <g' g>4. | <g' g>2 | <g' g>8 bf'8 bf'8 g8 | g8 r8 r4 | <g e>8 r8 r4 | <d'' f' a>8 r8 r4 | <d' a>8 r8 r4 | <e' cs'>8 r8 bf4 | bf4 b4 | b4 <a' a>4 | <a' a>4~ <a' a>16 bf'32 a'32 g'32 f'32 e'32 d'32 | cs'32 d'32 c'32 bf32 a32 g32 f32 e32 d8 r8 | }
    \\
    { r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r4 d'8. r16 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | r2 | }
  >>
}

% ---- Violoncello ----
violoncello = {
  \global
  \clef bass
  \set Staff.midiInstrument = "cello"
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } |
  \tuplet 3/2 { <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 <e a,>16 } \tuplet 3/2 { <a a,>16 <a a,>16 <a a,>16 } |
  \tuplet 3/2 { <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 } |
  \tuplet 3/2 { <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 <a a,>16 } <a a,>16 r32 d'32 |
  a4~ a8.. f32 |
  d8.. a,32 f,8. a,32 f,32 |
  d,4~ d,16 f16 e16 d16 |
  a8 g8 e8 a8 |
  d'8. r16 a8. r16 |
  d8. r16 r4 |
  g8. r16 d8. r16 |
  g,8 ef4. |
  ef2 |
  ef8 ef8 ef8 ef8 |
  e8 r8 r4 |
  a,8 r8 r4 |
  a,8 r8 r4 |
  a,8 r8 r4 |
  a,8 r8 g4 |
  g4 af4 |
  af4 a4 |
  a4~ \tuplet 3/2 { a16 } \tuplet 3/2 { <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 } |
  \tuplet 3/2 { <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 <a d>16 } |
}

% ---- Contrabasso（实音） ----
contrabass = {
  \global
  \clef bass
  \set Staff.midiInstrument = "contrabass"
  r2 |
  r2 |
  r2 |
  r4 r8 r16. e,32 |
  a,,4 r4 |
  r2 |
  r2 |
  r4 r8 r16. e,32 |
  a,,4 r4 |
  r2 |
  r2 |
  r4 r8 r16. e,32 |
  a,,8 r8 r4 |
  r4 r16 e,16 e,16 a,,16 |
  r2 |
  r4 r8 r16. d32 |
  a,4~ a,8.. f,32 |
  d,8.. a,,32 f,,8. a,,32 f,,32 |
  d,4~ d,16 f,16 e,16 d,16 |
  a,8 g,8 e,8 a,8 |
  d8. r16 a,8. r16 |
  d,8. r16 r4 |
  g,8. r16 d,8. r16 |
  g,,8 ef,4. |
  ef,2 |
  ef,8 ef,8 ef,8 ef,8 |
  e,8 r8 r4 |
  a,,8 r8 r4 |
  a,,8 r8 r4 |
  a,,8 r8 r4 |
  a,,8 r8 g,4 |
  g,4 af,4 |
  af,4 a,4 |
  a,4 a,,8 r8 |
  d,4 r4 |
}

#(set-global-staff-size 11)
\paper { #(set-paper-size "a4landscape") }

\score {
  <<
    \new StaffGroup <<
      \new Staff \flauti
      \new Staff \oboi
      \new Staff \clarinetti
      \new Staff \fagotti
      \new Staff \corni
      \new Staff \corniBassi
      \new Staff \trombe
      \new Staff \timpani
      \new Staff \violinoI
      \new Staff \violinoII
      \new Staff \viola
      \new Staff \violoncello
      \new Staff \contrabass
    >>
  >>
  \layout { ragged-right = ##f system-count = #5 }
  \midi { }
}
