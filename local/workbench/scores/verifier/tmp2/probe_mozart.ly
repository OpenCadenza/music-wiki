\version "2.26.0"
\language "english"

\header {
  title = "Keyboard Sonata No. 10 in C Major, K. 330 (300h)"
  subtitle = "II. Andante cantabile (mm. 1–8)"
  location = "mm. 1–8"
  composer = "Wolfgang Amadeus Mozart"
  tagline = ##f
}

% 编制与 GM 程序号: Piano: 0 (acoustic grand)
% 调性与拍号：F 大调 (\key f \major), 3/4 拍 (\time 3/4)
% 结构：混合乐段类型 1（先行句 mm. 1–4 达成半终止 + 延续句 mm. 5–8 达成正格终止）

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


\displayLilyMusic \rightHand
\displayLilyMusic \leftHand
