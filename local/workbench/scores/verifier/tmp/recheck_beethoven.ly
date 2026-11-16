\version "2.26.0"
\language "english"

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
  g'4~\fp g'16( f'16 e'16 f'16 e'16 f'16 g'16 f'16 e''16 f''16 g''16 f''16) | |
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

\displayLilyMusic \violinOne
