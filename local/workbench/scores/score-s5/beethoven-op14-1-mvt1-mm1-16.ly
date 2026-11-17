\version "2.26.0"
\language "english"

\header {
  title = "Piano Sonata No. 9 in E major, Op. 14 No. 1"
  subtitle = "I. Allegro — mm. 1–16（真实摘录，双手完整声部）"
  composer = "Ludwig van Beethoven"
  tagline = ##f
}

% Source: Humdrum **kern `sonata09-1.krn`
%   craigsapp/beethoven-piano-sonatas — digital edition of Durand 1915, ed. Paul Dukas.
% Key E major, 4/4, MM quarter = 132. Dynamics from the file's **dynam spine
% (p m.1, p m.5, f m.8, p m.11, p m.13, f m.16).
% Absolute pitches throughout (no \relative). mm.5–12 exchange the hands'
% regsters; clefs follow the source at measure boundaries only.

global = {
  \key e \major
  \time 4/4
  \tempo "Allegro" 4 = 132
}

% ---------------------------- right hand ----------------------------------
rhUpper = {
  \global \voiceOne
  \clef treble
  b'2 <e' e''>2 |
  cs''2 <fs' fs''>2 |
  ds''2 <b' b''>2 |
  b''4. cs'''16 ds'''16 e'''4 r4 |
  gs''16 e''16 a''16 fs''16 b''16 gs''16 cs'''16 a''16 b''4 r4 |
  \clef bass
  gs16 e16 a16 fs16 b16 gs16 cs'16 a16 b4 r4 |
  \clef treble
  r8 b8 gs'8 e'8 a'8 fs'8 ds'8 b'8 |
  r8 b'8 gs''8 e''8 a''8 fs''8 ds''8 b''8 |
  b''4. a''16 gs''16 fs''8 e''8 ds''8 cs''8 |
  b'1 |
  b'4. a'16 gs'16 fs'8 e'8 ds'8 cs'8 |
  \clef bass
  b1 |
  b2 <e e'>2 |
  cs'2 <fs fs'>2 |
  <gs gs'>2 <a a'>2 |
  <as as'>2 <b b'>2 |
}

rhLower = {
  \global \voiceTwo
  R1*6 |
  r8 b4.~ b2 |
  r8 b'4.~ b'2 |
  b'2 cs''2 |
  gs'4 g'4 fs'2 |
  <b e'>2 cs'2 |
  gs4 g4 fs2 |
  R1*4 |
}

rhThird = {
  \global \voiceThree
  R1*9 |
  e'2. ds'4 |
  R1 |
  e2. ds4 |
  R1*4 |
}

% ----------------------------- left hand ----------------------------------
lhUpper = {
  \global \voiceOne
  \clef bass
  r8 <e gs b>8[ <e gs b>8 <e gs b>8] r8 <e gs b>8[ <e gs b>8 <e gs b>8]\p |
  r8 <e a cs'>8[ <e a cs'>8 <e a cs'>8] r8 <e a cs'>8[ <e a cs'>8 <e a cs'>8] |
  r8 <e fs a ds'>8[ <e fs a ds'>8 <e fs a ds'>8] r8 <e fs a ds'>8[ <e fs a ds'>8 <e fs a ds'>8] |
  <e gs b e'>2. r4 |
  \clef treble
  r2\p gs'16 e'16 a'16 fs'16 b'16 gs'16 cs''16 a'16 |
  \clef bass
  b'4 r4 gs,16 e,16 a,16 fs,16 b,16 gs,16 cs16 as,16 |
  r4 r8 gs8 ds8 fs8 a4 |
  b1\f |
  \clef treble
  <e' gs'>4 gs4 a4 as4 |
  b2 as4 a4 |
  \clef bass
  <e gs>4\p gs,4 a,4 as,4 |
  b,2 as,4 a,4 |
  r8 <e, gs,>8[ <e, gs,>8 <e, gs,>8]\p r8 <e, gs,>8[ <e, gs,>8 <e, gs,>8] |
  r8 <e, a,>8[ <e, a,>8 <e, a,>8] r8 <e, as,>8[ <e, as,>8 <e, as,>8] |
  r8 <e, b,>8[ <e, b,>8 <e, b,>8] r8 <e, c>8[ <e, c>8 <e, c>8] |
  r2\f d2 |
}

lhLower = {
  \global \voiceTwo
  R1*6 |
  b,1 |
  r4 r8 gs'8 ds'8 fs'8 a'4 |
  R1 |
  r2 b,2 |
  R1 |
  r2 b,,2 |
  R1*3 |
  r8 <e, cs>8[ <e, cs>8 <e, cs>8] f,8[ f,8 f,8 f,8] |
}

\score {
  \new PianoStaff <<
    \new Staff = "RH" \with { midiInstrument = "acoustic grand" } <<
      \new Voice = "r1" { \rhUpper }
      \new Voice = "r2" { \rhLower }
      \new Voice = "r3" { \rhThird }
    >>
    \new Staff = "LH" \with { midiInstrument = "acoustic grand" } <<
      \new Voice = "l1" { \lhUpper }
      \new Voice = "l2" { \lhLower }
    >>
  >>
  \layout { }
  \midi { }
}



