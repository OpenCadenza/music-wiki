\version "2.26.0"
\language "english"

\header {
  title = "Piano Sonata No. 30 in E major, Op. 109"
  subtitle = "III. Andante molto cantabile ed espressivo — Tema, mm. 1–8"
  composer = "Ludwig van Beethoven (1770–1827)"
  tagline = ##f
}

global = {
  \key e \major
  \time 3/4
  \tempo "Andante molto cantabile ed espressivo" 4 = 84
}

upper = {
  \clef treble
  <<
    \new Voice = "rh1" {
      \voiceOne
      % m. 1
      gs'4( e'4 fs'8) | % 1
      % m. 2
      \oneVoice <fs ds'>4 <fs a b>2 | % 2
      \voiceOne
      % m. 3
      <gs b gs'>4( e'4. fs'8) | % 3
      % m. 4
      \oneVoice <ds' fs'>4( <cs' e' as'>4 <ds' fs' b'>4) | % 4
      % m. 5
      \voiceOne \grace { b32[( e'32 gs'32]) } b'4( e'4. gs'16 fs'16) | % 5
      % m. 6
      \oneVoice ds'4( b4 \grace { a32[ b32 a32 gs32] } a4) | % 6
      % m. 7
      \voiceOne gs4 e'4.->( as8) | % 7
      % m. 8
      \oneVoice \clef bass as2\p( b4) | % 8
    }
    \new Voice = "rh2" {
      \voiceTwo
      b4 b4 cs'4 | % 1
      s2. | % 2
      r4 b4 cs'4 | % 3
      s2. | % 4
      r4 b4 cs'4 | % 5
      s2. | % 6
      s2. | % 7
      g4( e4 ds4) | % 8
    }
  >>
}

lower = {
  \clef bass
  <<
    \new Voice = "lh1" {
      \voiceOne
      e,4( gs,4 a,4 | % 1
      b,4 cs4 ds4) | % 2
      e4( gs4 as4 | % 3
      b4 fs4 b,8 a,8) | % 4
      gs,4 gs4 a,4 | % 5
      <b, fs>4 <cs e>4 <ds fs>4 | % 6
      e4 e2 | % 7
      e,4( g,4 b,4) | % 8
    }
    \new Voice = "lh2" {
      \voiceTwo
      s2. | % 1
      s2. | % 2
      s2. | % 3
      s2. | % 4
      gs,2 s4 | % 5
      s2. | % 6
      s4 <cs, cs>4 <c, c>4 | % 7
      c,2 b,,4 | % 8
    }
  >>
}

\score {
  \new PianoStaff <<
    \new Staff = "RH" \with { midiInstrument = "acoustic grand" } {
      \global
      \upper
    }
    \new Staff = "LH" \with { midiInstrument = "acoustic grand" } {
      \global
      \clef bass
      \lower
    }
  >>
  \layout {
    \context {
      \Score
      \override SpacingSpanner.common-shortest-duration =
        #(ly:make-moment 1/16)
    }
  }
  \midi {
    \context {
      \Score
      midiMergeUnisons = ##f
    }
  }
}

