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

rightHand = \relative c'' {
  \global
  \clef treble
  \partial 4.
  c8-.\(^\markup { \italic dolce } c-. c-.\) |
  c8. \grace { \teeny d16( c b c) } f16 c8 a( c e) |
  <<
    {
      g4( f8) f\f([ <e g> <f a>)] |
    }
    \\
    {
      s4. c4 c8 |
    }
  >> |
  <<
    {
      bf8.( c32 d c8) f( e f) |
    }
    \\
    {
      f4. r8 b,4\p |
    }
  >> |
  <<
    {
      <f a>4( <e g>8) g[ g g] |
    }
    \\
    {
      c,2 s4 |
    }
  >> |
  <<
    {
      \appoggiatura g'16 g'8.[ d32( b32] g8) g-.( g-. g-.) |
    }
    \\
    {
      <b, d f>2 <c e>4 |
    }
  >> |
  \appoggiatura g'16 g'4 ~ g'16.[ a'64( b'64 c''16) b'16-.] a'16-.( g'-. f'-. e'-.) |
  <<
    {
      cs'16[( d' f' a')] c'4. e'16[( d')] |
    }
    \\
    {
      s2 s8 b8 |
    }
  >> |
  c'4 r2 | \bar "||"
}

leftHand = \relative c {
  \global
  \clef bass
  \partial 4.
  r8 r4 |
  <f, a, c>2\p <c, g, bf,>4 |
  <<
    {
      bf'4 a8( <a, a>[ <g, g> <f, f>]) |
    }
    \\
    {
      d4. s4. |
    }
  >> |
  <d d'>8[ <bf, bf>] <a, a> r d4 |
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
