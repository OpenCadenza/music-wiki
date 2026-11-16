\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \key f \major
      \time 3/4
      \clef treble
      \partial 4.
      c''8-.\(^\markup { \italic dolce } c''8-. c''8-.\) |
      c''8. \grace { \teeny d''16( c'' b' c'') } f''16 c''8 a'8( c''8 e'8) |
      <<
        {
          g'4( f'8) f'8\f([ <e' g'> <f' a'>)] |
          bf'8.( c''32 d'' c''8) f'8( e' f') |
          <f' a'>4( <e' g'>8) g'8[ g'8 g'8] |
          \appoggiatura g'16 g''8.[ d''32( b'32] g'8) g'8-.( g'8-. g'8-.) |
          \appoggiatura g'16 g''4 ~ g''16.[ a''64( b''64 c'''16) b''16-.] a''16-.( g''-. f''-. e''-.) |
          cs''16[( d'' f'' a'')] c''4. e''16[( d'')] |
          \partial 4. c''4 r8 | \bar "||"
        }
        \\
        {
          s4. c'4 c'8 |
          f'4. r8 b4\p |
          c'2 s4 |
          <b d' f'>2 <c' e'>4 |
          s2. |
          s2 s8 b'8 |
          \partial 4. s4. |
        }
      >>
    }
    \new Staff = "lower" {
      \key f \major
      \time 3/4
      \clef bass
      \partial 4.
      r8 r4 |
      <f, a, c>2\p <c, g, bf>4 |
      <<
        {
          bf4 a8( <a, a>8[ <g, g> <f, f>]) |
          <d d'>8[ <bf, bf>8] <a, a>8 r8 d4 |
          c2 \clef treble <c' e'>4\f |
          R2. |
          \clef bass <d f b>4 <e g c'>4 r4 |
          r8\p <f a d'>8 << { <c' e'>4 <d' f'>4 } \\ { g,2 } >> |
          \partial 4. <c' e'>4 c8 | \bar "||"
        }
        \\
        {
          d4. s4. |
        }
      >>
    }
  >>
  \layout { }
  \midi { }
}
