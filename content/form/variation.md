---
name: 变奏曲式
description: 先呈示主题，再逐轮改变它的旋律、节奏、织体或对位，同时保留可追踪的主题骨架。
---

# 变奏曲式

**结构示意**　主题 → 变奏 I → 变奏 II → … → 最后一轮或主题回归

把谱例的开头对齐，先比较低音和和声落点，再比较主题的关键音在哪个声部、哪个拍位出现。辨认一轮变奏还要听它怎样收束。同一主题的反复可以在后续变奏里被写出并改写，因此各轮的书面小节数可以不同。

## 贝多芬 Op. 109 第三乐章

E 大调主题有两个各八小节的部分，各有反复。以下七段都截取相应段落开头八小节，使用乐章的连续小节号。可对照主题第 1–4 小节的低音 E–G♯–A–B，以及旋律开头的下行三度。

### 主题 · 第 1–8 小节

3/4 拍。第 1 小节旋律从 G♯ 向 E 下落，低音从 E 经 G♯ 向 A 推进。先记住旋律的下行轮廓和低音的上行方向。

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.1–8" id="op109-theme"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \set Score.tempoHideNote = ##t \tempo "Andante molto cantabile ed espressivo" 4 = 84 \time 3/4 \voiceOne gs'4^\markup { \italic "mezza voce" }( e'4. fs'8 |
        \oneVoice <fs ds'>4 <fs a b>2) |
        \voiceOne <gs b gs'>4( e'4. fs'8) |
        \oneVoice <ds' fs'>4( <cs' e' as'>4 <ds' fs' b'>4) |
        \voiceOne \grace { b32( } \grace { e'32 } \grace { gs'32) } b'4( e'4. gs'16 fs'16) |
        \oneVoice ds'4 b4 \grace { a32( } \grace { b32 } \grace { a32 } \grace { gs32) } a4 |
        \oneVoice gs4^\markup { \italic "cresc." }( e'4.-> as8) \clef "bass" |
        \voiceOne as2\p b4 \bar ":|." |
      }
      \new Voice {
        \voiceTwo b4 b4 cs'4 |
        s1*3/4 |
        s4 b4 cs'4 |
        s1*3/4 |
        r4 b4 cs'4 |
        s1*3/4 |
        s1*3/4 |
        g4( e4 ds4) |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \time 3/4 \oneVoice e,4( gs,4 a,4 |
        \oneVoice b,4 cs4 ds4) |
        \oneVoice e4( gs4 as4 |
        \oneVoice b4 fs4 b,8 a,8) |
        \voiceOne gs,4 gs4 a,4 |
        \oneVoice <b, fs>4 <cs e>4 <ds fs>4 |
        \voiceOne s4 e2 |
        \voiceOne e,4( g,4 b,4) |
      }
      \new Voice {
        \voiceTwo s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        gs,2 s4 |
        s1*3/4 |
        e4( <cs, cs>4 <c, c>4) |
        c,2 b,,4 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 变奏 I · 第 17–24 小节

上声部仍可顺着主题的主要落点辨认，音区抬高，低音与中声部让开旋律。附点、倚音和更自由的旋律节奏把和弦式主题写成歌唱性旋律。

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.17–24" id="op109-v1"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \set Score.tempoHideNote = ##t \tempo "Molto espressivo" 4 = 84 \set Score.currentBarNumber = #17 \time 3/4 \oneVoice \grace { b'8(\p } b''2->)( e''8. fs''16 |
        \oneVoice e''4 ds''4)~ ds''8. b'16 |
        \oneVoice \grace { b'8( } b''4.->)( ds''8 \tuplet 5/4 { e''32 fs''32 e''32 ds''32 e''32 } fs''16 gs''16) |
        \oneVoice gs''4^\markup { \italic "cresc." }( fs''4. ds''8) |
        \oneVoice \grace { b'8( } b''4.->)( gs''8) fs''8.-.( e''16-.) |
        \oneVoice e''8( ds''4) cs''8-.( b'8-. a'8-.) |
        \voiceOne a'8( gs'8 fs'8 b'8 as'8 e''8) |
        \voiceOne fs''8( e''8 fs''8 g''8) ds''8. b'16 \bar ":|." |
      }
      \new Voice {
        \voiceTwo s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s2 as'4 |
        as'2 b'4 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \time 3/4 \oneVoice e,4 <b, e gs b>4 <b, e gs b>4 |
        \oneVoice fs,4 <b, fs a b>4 <b, fs a b>4 |
        \oneVoice gs,4 <b, e gs b>4 <b, e gs b>4 |
        \oneVoice a,4 <b, ds fs b>4 <b, ds fs b>4 |
        \oneVoice gs,4 <b, e gs b>4 <b, e gs b>4 |
        \oneVoice fs,4 <b, ds fs a>4 <ds, b,>4 |
        \voiceOne b,4 b,4 cs,8 fs,,8 |
        \voiceOne cs,8( g,8 fs,8 e,8) <b,, fs,>8( cs,16 ds,16) |
      }
      \new Voice {
        \voiceTwo s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        e,4 ds,8 d,8 cs,4 |
        fs,,2 s4 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 变奏 II · 第 33–40 小节

十六分音符在两手间交错。把第 33–36 小节按拍合并，便能辨认主题的低音和和声框架。变奏后续还会把反复写出，并换成另一种织体。

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.33–40" id="op109-v2"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \set Score.tempoHideNote = ##t \tempo "Leggiermente" 4 = 84 \set Score.currentBarNumber = #33 \time 3/4 r16\p b16( gs'16) r16 r16 e'16( b16) r16 r16 cs'16( fs'16) r16 |
        r16 ds'16( fs16) r16 r16 \change Staff = "down" e16 b16 \change Staff = "up" r16 r16 \change Staff = "down" b16 fs16 \change Staff = "up" r16 |
        r16 gs'16 gs''16 r16 r16 e''16 b'16 r16 r16 cs''16 fs''16 r16 |
        r16^\markup { \italic "cresc." } ds''16 fs''16 r16 r16 as''16 e''16 r16 r16 <ds'' fs''>16 b''16 r16 |
        r16 b''16 e''16 r16 r16 gs''16 e'''16 r16 r16 e'''16 fs'''16 r16 |
        r16^\markup { \italic "dim." } e'''16 ds'''16 r16 r16 ds'''16 cs'''16 r16 r16 b''16 a''16 r16 |
        r16^\markup { \italic "cresc." } a''16 gs''16 r16 r16 gs''16 a''16 r16 r16 bf''16 e'''16 r16 |
        r16^\markup { \italic "dim." }\p <bf' e''>16 <a' f''>16 r16 r16 <bf' g''>16 <g' e''>16 r16 r16 b''16 b'16 r16 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \time 3/4 e,16 r16 r16 e16( gs16) r16 r16 gs,16( a,16) r16 r16 a16( |
        b16) r16 r16 b,16 cs16 r16 r16 cs'16 ds'16 r16 r16 ds16 |
        e16 r16 r16 e'16 \clef "treble" gs'16 r16 r16 gs16 as16 r16 r16 as'16 |
        b'16 r16 r16 fs'16 fs'16 r16 r16 cs''16 b'16 r16 r16 a'16 |
        gs'16 r16 r16 gs''16 e''16 r16 r16 b'16 cs''16 r16 r16 as'16 |
        as'16 r16 r16 b'16 cs''16 r16 r16 e''16 ds''16 r16 r16 fs''16 |
        d''16 r16 r16 f''16 cs''16 r16 r16 e''16 c''16 r16 r16 g''16 |
        c''16 r16 r16 c'''16 c''16 r16 r16 c'''16 b''16 r16 r16 b'16 \clef "bass" |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 变奏 III · 第 65–72 小节

换成 2/4 拍和连续十六分音符。第 65–68 小节的两条线保留主题的下行三度和低音音级，第 69 小节起交换高低声部。

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.65–72" id="op109-v3"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \set Score.tempoHideNote = ##t \tempo "Allegro vivace" 4 = 144 \set Score.currentBarNumber = #65 \time 2/4 e'8\f r8 gs'8 r8 |
        b'8 r8 ds''8 r8 |
        e''8 r8 gs''8 r8 |
        as''8-.\sf as''8-. b''8-. r8 |
        gs''16\f b''16 a''16 gs''16 e''16 gs''16 fs''16 e''16 |
        ds''16 fs''16 e''16 ds''16 b'16 ds''16 cs''16 b'16 |
        gs'16 b'16 a'16 gs'16 e'16 gs'16 fs'16 e'16 |
        g'16 e'16 ds'16 e'16 ds'16 fs'16 b'16 ds'16 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \time 2/4 gs16 b16 a16 gs16 e16 gs16 fs16 e16 |
        ds16 fs16 e16 ds16 b,16 ds16 cs16 b,16 |
        gs,16 b,16 a,16 gs,16 e,16 gs,16 fs,16 e,16 |
        cs,16 e,16 ds,16 cs,16 b,,16 cs,16 d,16 ds,16 |
        e,8 r8 gs,8 r8 |
        b,8 r8 ds8 r8 |
        e8 r8 gs8 r8 |
        as8-.\sf as8-. b8-. r8 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 变奏 IV · 第 97–104 小节

9/8 拍。主题的下行三度进入流动的多声部织体。前几小节把相关音型交给不同声部，原本同拍发声的骨架被错开。

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.97–104" id="op109-v4"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \set Score.tempoHideNote = ##t \tempo "Un poco meno andante" 4 = 72 \set Score.currentBarNumber = #97 \time 9/8 \oneVoice b'16( ds''16 e''16 gs'16 a'16 b'16) e'4.~ e'8( gs'8 fs'8) |
        \bar ".|:" \voiceOne r4 r8 a'4.~ a'8( cs''8 b'8) |
        \voiceOne a'4( gs'8) e''4.~ e''8 gs''8 fs''8 |
        \voiceOne e''4. a''4.~ a''8 cs'''8 b''8 |
        \voiceOne a''4(^\markup { \italic "cresc. poco a poco" } gs''8) gs''16( a''16 b''16 e''16 fs''16 gs''16) b'8 r8 r8 |
        \voiceOne a'16(^\markup { \italic "crescendo" } b'16 cs''16 fs'16 gs'16 a'16) fs''16( gs''16 a''16 fs''16 gs''16 a''16 b''16 cs'''16 ds'''16 b''16 cs'''16 ds'''16) |
        \oneVoice e''16(^\markup { \italic "dim." } fs''16 gs''16 e''16 fs''16 gs''16 gs''16 a''16 b''16 gs''16 a''16 b''16) <b' b''>4( <as' as''>8) |
        \oneVoice bf''16( g''16 e''16 bf'16 e''16 g''16 bf''16 g''16 a''16 f''16 g''16 e''16) <e'' as''>8( <ds'' b''>8 bf'8) |
      }
      \new Voice {
        \voiceTwo s1*9/8 |
        e'4.( ds'4.) fs'16( gs'16 a'16 ds'16 e'16 fs'16) |
        e'4. gs'16( a'16 b'16 e'16 fs'16 gs'16) s4. |
        fs'16( gs'16 a'16 fs'16 gs'16 a'16) ds''4. fs''4. |
        fs''4( e''8) r4 r8 gs'16( a'16 b'16 e'16 fs'16 gs'16) |
        b4 r8 s2. |
        s1*9/8 |
        s1*9/8 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \time 9/8 \voiceOne gs'4 r8 \clef "bass" gs16( a16 b16 e16 fs16 gs16)~ gs4. |
        \voiceOne a16( b16 cs'16 fs16 gs16 a16) b,4. b,,4 r8 |
        \voiceOne b16( ds'16 e'16 gs16 a16 b16) s4. b4 r8 |
        \voiceOne b,4 r8 b4 r8 s4. |
        \oneVoice b,16( ds16 e16 gs,16 a,16 b,16) e,4.~ e,8( gs,8 fs,8) |
        \voiceOne e,4( ds,8) a,4.~( a,8 cs8 b,8) |
        \voiceOne <a,, a,>4( <gs,, gs,>8) <fs, fs>4( <e, e>8) e16 fs16 g16 e16 fs16 g16 |
        \voiceOne c16( e16 g16 bf16 g16 e16 g16 e16 f16 a16 bf16 g16) s4. |
      }
      \new Voice {
        \voiceTwo s4. \clef "bass" r4 r8 b,4 r8 |
        r4 r8 fs,16( gs,16 a,16 fs,16 gs,16 a,16) s4. |
        s4. b,4 r8 gs16( a16 b16 e16 fs16 gs16) |
        s4. fs16( gs16 a16 fs16 gs16 a16) b,16( cs16 ds16 b,16 cs16 ds16) |
        s1*9/8 |
        s4. b,,8 cs,8 b,,8 a,,8 cs,8 b,,8 |
        s2. cs4 c8 |
        c4. c4. c8( b,8 a,8) |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 变奏 V · 第 113–120 小节

回到明确的重拍，在 4/4 拍内依次进入模仿声部。下行三度和上行四度组织出新的线条。可以沿各声部的进入追踪它与主题的关系。

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.113–120" id="op109-v5"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \set Score.tempoHideNote = ##t \tempo "Allegro ma non troppo" 4 = 112 \set Score.currentBarNumber = #113 \time 4/4 \oneVoice gs2\f e2 |
        \voiceOne a2 fs2 |
        \voiceOne fs4 gs8 ds8 e4 d4 |
        \voiceOne cs'2 a2~ |
        \voiceOne a4( as4 b4 a4) |
        \voiceOne gs4 b4 b4 e'4 \clef "treble" |
        \oneVoice e'2.( f'4 |
        \oneVoice <e' g'>4 <f' a'>4 <g' bf'>4 <ds' b'>4) \clef "bass" |
      }
      \new Voice {
        \voiceTwo s1 |
        e4 fs8 cs8 ds4 b,4 |
        b2 gs2~ |
        <cs gs>4 a8 e8 fs4 c4 |
        R1 |
        r4 e4 gs2 \clef "treble" |
        s1 |
        s1 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \time 4/4 \oneVoice r4 e,4-. gs,2\sf |
        \oneVoice gs,4 fs,4-. a,2\sf |
        \oneVoice a,4 gs,4-. b,2\sf |
        \oneVoice b,4 a,4-. c4 e,4 |
        \voiceOne b,2 fs,2~ |
        \voiceOne fs,4 gs,4 r2 |
        \voiceOne gs4 a4 bf4 a4 |
        \voiceOne g,4( f,4 e,4 fs,4) |
      }
      \new Voice {
        \voiceTwo s1 |
        s1 |
        s1 |
        s1 |
        e,4 fs,8 cs,8 ds,4 b,,4~ |
        b,,4 gs,8 ds,8 e,4 b,,4 |
        bs,,4( cs,2 <c,~ c>4) |
        c,2. b,,4 |
      }
      \new Voice {
        \voiceThree s1 |
        s1 |
        s1 |
        s1 |
        s1 |
        s1 |
        r2 cs4 s4 |
        s1 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 变奏 VI · 第 153–160 小节

回到主题的速度。从第 153 小节起，B 音由较长时值逐步变为重复细分，到第 164 小节以颤音持续。声部不断加密、音区拉开，B 仍维系长程的属音支点。第 188 小节回归主题，主题两半均不再反复。

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.153–160" id="op109-v6"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \set Score.tempoHideNote = ##t \tempo "Tempo I del tema" 4 = 84 \set Score.currentBarNumber = #153 \time 3/4 \voiceOne b'4-.^\markup { \italic "cantabile" }(\p b'4-. b'4-.) |
        \voiceOne b'4-.( b'4-. b'4-.) |
        \voiceOne b'8 b'8 b'8 b'8 b'8 b'8 |
        \voiceOne b'8 b'8 b'8 b'8 b'8 <ds'' fs'' b''>8 |
        \time 9/8 \voiceOne <e'' b''>4.( e''4. gs''4 fs''8) |
        \voiceOne ds''4.( b''4. a''4.) |
        \voiceOne gs''4.^\markup { \italic "cresc." } e'''4.~ e'''4 e'''8 |
        \set Timing.measureLength = #3/4 \voiceOne e'''4.\p as''4. \bar "" |
      }
      \new Voice {
        \voiceTwo gs'4( e'4 fs'4 |
        ds'4 b2) |
        gs'4( e'4 fs'4) |
        fs'4( as'4 b'8 b'8) |
        b'8 b'8 b'8 b'8 as'8 b'8 b'8 b'8 b'8 |
        b'16 cs''16 b'16 cs''16 b'16 cs''16 b'16 cs''16 b'16 cs''16 b'16 cs''16 b'16 cs''16 b'16 cs''16 b'16 cs''16 |
        b'16 fs''16 e''16 fs''16 e''16 fs''16 e''16 fs''16 e''16 fs''16 e''16 fs''16 e''16 fs''16 e''16 fs''16 e''16 fs''16 |
        e''16 g''16 e''16 g''16 e''16 g''16 e''16 g''16 e''16 g''16 e''16 g''16 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \time 3/4 \voiceOne b,4-.( b,4-. b,4-.) |
        \voiceOne b,4-.( b,4-. b,4-.) |
        \voiceOne b,8 b,8 b,8 b,8 b,8 b,8 |
        \voiceOne b,8 b,8 b,8 b,8 b,8 b,8 |
        \time 9/8 \voiceOne b,8 b,8 b,8 b,8 as,8 b,8 b,8 b,8 b,8 |
        \voiceOne b,16 cs16 b,16 cs16 b,16 cs16 b,16 cs16 b,16 cs16 b,16 cs16 b,16 cs16 b,16 cs16 b,16 cs16 |
        \voiceOne b,16 fs16 e16 fs16 e16 fs16 e16 fs16 e16 fs16 e16 fs16 e16 fs16 e16 fs16 e16 fs16 |
        \set Timing.measureLength = #3/4 \voiceOne g16 e16 g16 e16 g16 e16 g,16 e,16 g,16 e,16 g,16 e,16 |
      }
      \new Voice {
        \voiceTwo e,4 gs,4 fs,4 |
        a,4 fs,4 gs,4 |
        e,4( gs,4 fs,8 e,8) |
        ds,4( cs,4 b,,8 a,8) |
        gs,4. gs,4. a,4. |
        fs,4.( ds,4. fs,4.) |
        e,8 r8 r8 cs4.~ cs4 c8 |
        c4. c,4. |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.161–168" id="op109-v6-trill"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \set Score.tempoHideNote = ##t \tempo 4 = 84 \set Score.currentBarNumber = #161 \time 3/4 \set Timing.measureLength = #1/4 \voiceOne b''4^\markup { \italic "cresc." } |
        \set Timing.measureLength = #3/4 \voiceOne b'32^\markup { \italic "poco" } cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 |
        \voiceOne b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 |
        \voiceOne b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 |
        \voiceOne b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 b'32 cs''32 \tuplet 3/2 { r8 b''8 b''8 } |
        \voiceOne \tuplet 3/2 { b''8 as''8 b''8 } \tuplet 3/2 { b''8 e''8 e''8 } \tuplet 3/2 { e''8 gs''8 fs''8 } |
        \voiceOne \tuplet 3/2 { fs''8 ds''8 ds''8 } \tuplet 3/2 { ds''8 b''8 b''8 } \tuplet 3/2 { b''8 as''8 a''8 } |
        \voiceOne \tuplet 3/2 { a''8 gs''8 gs''8 } \tuplet 3/2 { gs''8 e'''8 e'''8 } \tuplet 3/2 { e'''8( ds'''8 e'''8) } |
      }
      \new Voice {
        \voiceTwo ds''32( cs''32 b'32 cs''32) b'32( cs''32 b'32 cs''32) |
        gs'8( e'8) e'8( gs'8) gs'8( fs'8) |
        fs'8( ds'8) ds'8( e'8) e'8( ds'8) |
        gs'8( e'8) e'8( gs'8) gs'8( fs'8) |
        fs'8 fs'8 as'8 as'8 b'4\trill~ |
        b'2.~ |
        b'2.~ |
        b'4 e''2\trill |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \time 3/4 \set Timing.measureLength = #1/4 \voiceOne b,,32( b,32 b,,32 b,32) b,,32( b,32 b,,32 b,32) |
        \set Timing.measureLength = #3/4 \voiceOne b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 |
        \voiceOne b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 |
        \voiceOne b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 |
        \voiceOne b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,32 cs32 b,4\trill~ |
        \voiceOne b,2.~ |
        \voiceOne b,2.~ |
        \voiceOne b,4 e2\trill |
      }
      \new Voice {
        \voiceTwo s4 |
        e,8( gs,8) gs,8( e,8) e,8( fs,8) |
        ds,8( a,8) a,8( gs,8) gs,8( fs,8) |
        e,8( gs,8) gs,8( e,8) e,8( ds,8) |
        ds,8 ds,8 cs,8 cs,8 \tuplet 3/2 { b,,8 a,8 a,8 } |
        \tuplet 3/2 { gs,8 gs,8 gs,8 } \tuplet 3/2 { gs,8 gs,8 gs,8 } \tuplet 3/2 { gs,8 a,8 a,8 } |
        \tuplet 3/2 { a,8( fs,8 fs,8 } \tuplet 3/2 { fs,8 ds,8 ds,8 } \tuplet 3/2 { ds,8 cs,8 ds,8) } |
        \tuplet 3/2 { ds,8 e,8 e,8 } \tuplet 3/2 { r8 cs8 cs8 } \tuplet 3/2 { cs8 bs,8 cs8 } |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="贝多芬 Op.109 第三乐章" location="mm.188–195" id="op109-return"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \major \set Score.tempoHideNote = ##t \tempo "Tempo I del tema" 4 = 84 \set Score.currentBarNumber = #188 \time 3/4 \voiceOne gs'4^\markup { \italic "cantabile" }^\markup { \italic "sempre legato" }( e'4. fs'8 |
        \oneVoice <fs ds'>4 \change Staff = "down" <fs a b>2) \change Staff = "up" |
        \voiceOne gs'4( e'4. fs'8) |
        \oneVoice <ds' fs'>4( <cs' e' as'>4 <ds' fs' b'>4) |
        \voiceOne <e' gs' b'>4( e'4. gs'16 fs'16) |
        \oneVoice <fs ds'>4 \change Staff = "down" <e b>4 \grace { a32( } \grace { b32 } \grace { a32 } \grace { gs32) } <fs a>4 \change Staff = "up" |
        \oneVoice \change Staff = "down" gs4^\markup { \italic "cresc." }( \change Staff = "up" e'4. as8) \clef "bass" |
        \voiceOne as2(\p b4) \clef "treble" |
      }
      \new Voice {
        \voiceTwo b4 b4 cs'4 |
        s1*3/4 |
        <gs b>4 b4 cs'4 |
        s1*3/4 |
        b4 b4 cs'4 |
        s1*3/4 |
        s1*3/4 |
        g4( e4 ds4) \clef "treble" |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \major \time 3/4 \oneVoice e,4( gs,4 a,4 |
        \oneVoice b,4 cs4 ds4) |
        \oneVoice e4( gs4 as4) |
        \oneVoice b4( fs4 b,8 <a,, a,>8) |
        \voiceOne gs,4 gs,4 a,4 |
        \oneVoice <b,, b,>4 <cs, cs>4 <ds, ds>4 |
        \voiceOne s4 e4 e4 |
        \voiceOne e,4( g,4 b,4) |
      }
      \new Voice {
        \voiceTwo s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        gs,,2 a,,4 |
        s1*3/4 |
        <e, e>4( <cs, cs>4 <c, c>4) |
        c,2 b,,4 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```
