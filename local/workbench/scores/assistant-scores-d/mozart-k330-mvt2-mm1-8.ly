\version "2.26.0"
\language "english"

\header {
  title = "Keyboard Sonata No. 10 in C Major, K. 330 (300h)"
  subtitle = "II. Andante cantabile (mm. 1–8)"
  composer = "Wolfgang Amadeus Mozart"
  tagline = ##f
}

% 依据 Open Music Theory (Graphics/form/XML/mozart, k330,ii.xml 与 k330-ii.png)
% 及 Humdrum Kern (0041-41-Piano Sonata No. 10 in C major, K 330 (300h), mvmt. 2.abc) 严格对齐编码。
% 小节范围：弱起三拍八分音符 (\partial 4.) + mm. 1–8。

global = {
  \key f \major
  \time 3/4
  \tempo "Andante cantabile" 4 = 80
}

rightHand = {
  \global
  \clef treble
  \partial 4.
  c''8-.\(^\markup { \italic dolce } c''-. c''-.\) |
  c''8. \grace { \teeny d''16( c'' b' c'') } f''16 c''8 a'8( c''8 e'8) |
  <<
    {
      g'4( f'8) f'8\f([ <e' g'> <f' a'>)] |
    }
    \\
    {
      s4. c'4 c'8 |
    }
  >> |
  <<
    {
      bf'8.( c''32 d'' c''8) f'8( e' f') |
    }
    \\
    {
      f'4. r8 b4\p |
    }
  >> |
  <<
    {
      <f' a'>4( <e' g'>8) g'8[ g'8 g'8] |
    }
    \\
    {
      c'2 s4 |
    }
  >> |
  <<
    {
      \appoggiatura g'16 g''8.[ d''32( b'32] g'8) g'8-.( g'8-. g'8-.) |
    }
    \\
    {
      <b d' f'>2 <c' e'>4 |
    }
  >> |
  \appoggiatura g'16 g''4 ~ g''16.[ a''64( b''64 c'''16) b''16-.] a''16-.( g''-. f''-. e''-.) |
  <<
    {
      cs''16[( d'' f'' a'')] c''4. e''16[( d'')] |
    }
    \\
    {
      s2 s8 b'8 |
    }
  >> |
  c''4 r2 | \bar "||"
}

leftHand = {
  \global
  \clef bass
  \partial 4.
  r8 r4 |
  <f a c'>2\p <c g bf>4 |
  <<
    {
      bf4 a8( <a, a>8[ <g, g> <f, f>]) |
    }
    \\
    {
      d4. s4. |
    }
  >> |
  <d d'>8[ <bf, bf>8] <a, a>8 r8 d4 |
  c2 \clef treble <c' e'>4\f |
  R2. |
  \clef bass <d f b>4 <e g c'>4 r4 |
  r8\p <f a d'>8 << { <c' e'>4 <d' f'>4 } \\ { g2 } >> |
  <c' e'>4 c8 r4. | \bar "||"
}

\score {
  \new PianoStaff \with {
    instrumentName = "Piano"
    midiInstrument = "acoustic grand"
  } <<
    \new Staff = "upper" { \rightHand }
    \new Staff = "lower" { \leftHand }
  >>
  \layout { }
  \midi { }
}
