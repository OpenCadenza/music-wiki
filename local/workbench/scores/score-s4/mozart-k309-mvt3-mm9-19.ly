\version "2.26.0"
\language "english"

\header {
  title = "Mozart: Piano Sonata No. 7 in C major, K. 309 (284b)"
  subtitle = "III. Rondo: Allegretto grazioso · mm. 9–19"
  composer = "Wolfgang Amadeus Mozart (1756–1791)"
  tagline = ##f
}

%% 谱源：Neue Mozart-Ausgabe IX/25/1（DME 在线版，pp. 94–103，“Rondeau / Allegretto grazioso”）；
%% 逐音与 DCML Mozart piano sonatas 的 K309-3 MusicXML（GitLab 导出）核对；
%% Craig Sapp kern/ABC 对照本（sonata07-3）在此段与 MusicXML 仅第 9 小节首音记谱不同（倚音 vs 十六分音符）。

#(set-global-staff-size 17)

upper = {
  \clef "treble"
  \key c \major
  \time 2/4
  \set Score.currentBarNumber = #9
  % 9
  \grace { f''16 } e''8( d''16 c''16 c''8 c''8) |
  % 10
  \grace { b'32[ c''32 d''32] } c''4. c'''8 |
  % 11
  \grace { b''16 } a''8( g''16 f''16 f''8 f''8) |
  % 12
  \grace { e''32[ f''32 g''32] } f''4. a''8 |
  % 13
  \grace { a''16 } g''8( f''16 e''16 e''8) g''8 |
  % 14
  \grace { g''16 } f''8( e''16 d''16 d''8 f''8) |
  % 15
  \grace { f''16 } e''8( f''16 d''16) c''8 b'8\trill |
  % 16
  \grace { a''16 } g''8( f''16 e''16) e'''16\staccato cs'''16\staccato a''16 g''16 |
  % 17
  \grace { g''16 } f''8( e''16 d''16) d'''16\staccato b''16\staccato g''16 f''16 |
  % 18
  \grace { f''16 } e''8 a''16 f''16 e''16\staccato g''16\staccato f''16\staccato d''16\staccato |
  % 19
  c''8 r8 \f c'16 e'16 g'16 c''16 |
}

lower = {
  \clef "bass"
  \key c \major
  \time 2/4
  % 9
  c'16 e'16 g'16 e'16 c'16 e'16 g'16 e'16 |
  % 10
  c'16 e'16 g'16 e'16 c'16 e'16 g'16 e'16 |
  % 11
  c'16 f'16 a'16 f'16 c'16 f'16 a'16 f'16 |
  % 12
  c'16 f'16 a'16 f'16 c'16 f'16 a'16 f'16 |
  % 13
  c'16 e'16 g'16 e'16 cs'16 e'16 a'16 e'16 |
  % 14
  d'16 f'16 a'16 f'16 b16 d'16 g'16 d'16 |
  % 15
  << { <c' g'>8 d'8 e'8 d'8 } \\ { r8 f8 g4 } >> |
  % 16
  c'16 e'16 g'16 e'16 cs'16 e'16 a'16 e'16 |
  % 17
  d'16 f'16 a'16 f'16 b16 d'16 g'16 d'16 |
  % 18
  << { <c' g'>8 d'8 c'8 b8 } \\ { r8 f8 g4 } >> |
  % 19
  c'8 <g, g>8 <e, e>8 <c, c>8 |
}

\score {
  \new PianoStaff \with { instrumentName = "Piano" } <<
    \new Staff = "upper" \with { midiInstrument = "acoustic grand" } { \upper }
    \new Staff = "lower" \with { midiInstrument = "acoustic grand" } { \lower }
  >>
  \layout { }
  \midi { }
}
