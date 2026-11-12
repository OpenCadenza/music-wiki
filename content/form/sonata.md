---
name: 奏鸣曲式
description: 呈示部建立调性对比，展开部发展材料，再现部通常将副部带回主调，随后可接尾声。
---

# 奏鸣曲式

**结构示意**　呈示部（P 主部 → TR 连接部 → S 副部 → C 结束部）→ 展开部 → 再现部（P → 改写的 TR → S → C）→ 尾声（可选）

分析时先追踪副部的调性和终止，再比较主部动机在展开和再现中的用法。大调乐章常把副部放在属调，小调乐章可用关系大调、小属调等。展开部可以只取其中一个主题，也可以使用连接部、结束部或新材料。主题回来的小节与和声解决的时刻有时并不重合。

## 贝多芬 Op. 90 第一乐章

| 大段 | 小节 | 材料与调性 |
| --- | --- | --- |
| 呈示部 | 1–84 | P 1–24，e 小调。TR 25–54。S 55–67，b 小调。C 67–84。 |
| 展开部 | 85–143 | 主部片段重新组织，从局部调性转向 e 小调的属功能，末尾以主部动机的模仿接入再现。 |
| 再现部 | 144–222 | P 144–167。TR 168–197。S 198–214，回到 e 小调。C 214–222。 |
| 尾声 | 223–245 | 结束部过后的扩展，最后压缩主部材料并回到 e 小调主和弦。 |

弱起随其所引入的主题说明，小节号以完整小节计。第 67、214 小节兼有副部终止和结束部起点两种功能。

### 呈示部 · 主部与副部

主部一开口是强奏的 e 小调和弦弱起，随后上声部 G–F♯ 的附点节奏与弱奏回应交替。第 8 小节起，连续下行的材料逐渐减薄。第 15 小节停在属功能上，主部继续到第 24 小节才在 e 小调收拢。[主部开头的原谱与音频](../composers/beethoven/piano/sonatas/op90-two-movements.md#一、前十五小节-张力自己花掉)

第 45 小节已落到 b 小调，因此可以把这里听成副部区的入口。这里仍有连续推进与重复和弦，第 53–54 小节又在 b 小调的属和声上停留。第 55 小节力度、织体和主题轮廓同时改变，适合作为副部主题的起点。

| 乐句 | 小节 | 读谱线索 |
| --- | --- | --- |
| 第一乐句 | 55–60 | 左手十六分分解和弦衬托右手八度。右手从 G 向 F♯ 下行，再将长音移入较低音区。第 60 小节的终止被回避。 |
| 第二乐句 | 61–67 | 右手在休止之间重新起句，压缩下行动作，第 67 小节在 b 小调达成正格终止，随即接入结束部。 |

```lilypond title="贝多芬 Op.90 第一乐章" location="mm.53–67" id="op90-s"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \set Score.tempoHideNote = ##t \tempo 4 = 156 \set Score.currentBarNumber = #53 \time 3/4 <fs' as' cs'' e'' fs''>8\ff( <g' as' cs'' e'' g''>8) <g' as' cs'' e'' g''>8-. <g' as' cs'' e'' g''>8-. <g' as' cs'' e'' g''>8 <g' as' cs'' e'' g''>8 |
        <g' as' cs'' e'' g''>8^\markup { \italic "dim." }^\markup { \italic "Rit." } <g' as' cs'' e'' g''>8 <g' as' cs'' e'' g''>8 <g' as' cs'' e'' g''>8 <g' as' cs'' e'' g''>8 <g' as' cs'' e'' g''>8 |
        <g' g''>4^\markup { \italic "a Tempo" } <fs'~ fs''~>2 |
        <fs' fs''>4 <b'~ b''~>2 |
        <b' b''>4 <fs'~ fs''~>2 |
        <fs' fs''>4 <b b'~>2 |
        b'4( g'4 fs'4) |
        fs'2( as'4) |
        r8 g''8( g'''4.-> fs'''8) |
        r8 fs'''8( cs'''4.-> b''8) |
        r8 b''8( g''4.-> fs''8) |
        r8 fs''8( cs''4.-> b'8) |
        b'4( g'4 fs'4) |
        fs'8( d'8 b8 g8 fs8 as8) |
        b4 r4 r4 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \minor \time 3/4 <fs as cs' e'>8 <fs as cs' e'>8 <fs as cs' e'>8 <fs as cs' e'>8 <fs as cs' e'>8 <fs as cs' e'>8 |
        <fs as cs' e'>8 <fs as cs' e'>8 <fs as cs' e'>8 <fs as cs' e'>8 <fs as cs' e'>8 <fs as cs' e'>8 |
        b,16\p d'16 fs16 d'16 cs16 e'16 fs16 e'16 d16 fs'16 fs16 fs'16 |
        b,16 d'16 fs16 d'16 cs16 e'16 fs16 e'16 d16 fs'16 fs16 fs'16 |
        b,16 d'16 fs16 d'16 cs16 e'16 fs16 e'16 d16 fs'16 fs16 fs'16 |
        b,16 d'16 fs16 d'16 cs16 e'16 fs16 e'16 d16 fs'16 fs16 fs'16 |
        e16 d'16 b16 d'16 es16 d'16 b16 d'16 fs16 d'16 b16 d'16 |
        fs16 d'16 b16 d'16 fs16 d'16 b16 d'16 fs16 e'16 cs'16 e'16 |
        b,16 d'16 fs16 d'16 cs16 e'16 fs16 e'16 d16 fs'16 fs16 fs'16 |
        b,16 d'16 fs16 d'16 cs16 e'16 fs16 e'16 d16 fs'16 fs16 fs'16 |
        b,16 d'16 fs16 d'16 cs16 e'16 fs16 e'16 d16 fs'16 fs16 fs'16 |
        b,16 d'16 fs16 d'16 cs16 e'16 fs16 e'16 d16 fs'16 fs16 fs'16 |
        e16 d'16 b16 d'16 es16 d'16 b16 d'16 fs16 d'16 b16 d'16 |
        fs2 <fs,, fs,>4 |
        <b,, b,>8-.\f <cs, cs>8-. <d, d>8-. <e, e>8-. <fs, fs>4\sf |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 展开部 · 主部动机、织体呼应与再现准备

- **主部材料**　第 85–92 小节在 e 小调改写开头的陈述与回应。第 110–117 小节把附点短句移到不同音高和声部，先突出 C 大调区域，再移到降二级附近。
- **副部材料**　第 110 小节后的重复音织体可与呈示部第 45–54 小节的重复和弦对照。第 55–67 小节那两个带八度下行和分解和弦的副部乐句，要到第 198 小节起才重新出现。
- **准备再现**　第 118–129 小节的低音上行推向 B。第 130 小节的 B 低音上方出现 E 与 G，形成 e 小调的终止四六，听觉上期待 E–G 分别向 D♯–F♯ 解决。谱面延长了这份预期，继而在第 133 小节起用 G–F♯–E 的二声部模仿减薄织体，再从第 144 小节进入主部。这里省去了终止四六到根位 V 的常规解决。

```lilypond title="贝多芬 Op.90 第一乐章" location="mm.85–92" id="op90-dev"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \set Score.tempoHideNote = ##t \tempo 4 = 156 \set Score.currentBarNumber = #85 \time 3/4 \voiceOne a''4.( g''8) fs''8 r8 |
        \voiceOne <g'' b''>4 r4 <g'' b''>4 |
        \voiceOne <gs'' b''>4.( a''8) <gs'' b''>8 r8 |
        \voiceOne <a'' c'''>4^\markup { \italic "cresc." } r4 s4 |
        \oneVoice <c'' c'''>4.( <b' b''>8) <a' a''>8 r8 |
        \oneVoice <d'' d'''>4 r4 <d'' d'''>4 |
        \oneVoice <d'' d'''>4.( <c'' c'''>8) <d'' d'''>8 r8 |
        \oneVoice <ef'' ef'''>4.\f( <d'' d'''>8) <ef'' ef'''>8 r8 |
      }
      \new Voice {
        \voiceTwo b'8 b'8 b'8 b'8 b'8 b'8 |
        b'8 b'8 b'8 b'8 b'8 b'8 |
        b'8 b'8 b'8 b'8 b'8 b'8 |
        c''4 r4 <c'' c'''>4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \time 3/4 \oneVoice <fs' a'>4 r4 <fs' a'>8 r8 |
        \oneVoice <e' g'>4 r4 <e' g'>4 |
        \oneVoice <d' f'>4 r4 <d' f'>8 r8 |
        \oneVoice <c' e'>8 e'8 e'8 e'8 e'8 e'8 |
        \voiceOne e'8 e'8 e'8 e'8 e'8 e'8 |
        \voiceOne f'8 f'8 f'8 f'8 f'8 f'8 |
        \voiceOne f'8 f'8 f'8 f'8 f'8 f'8 |
        \oneVoice <g bf ef'>8 <g bf ef'>8 <g bf ef'>8 <g bf ef'>8 <g bf ef'>8 <g bf ef'>8 |
      }
      \new Voice {
        \voiceTwo s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        <a c'>4 r4 <a c'>8 r8 |
        <af b>4 r4 <af b>4 |
        <af bf>4 r4 <af bf>4 |
        s1*3/4 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="贝多芬 Op.90 第一乐章" location="mm.110–117" id="op90-sequence"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \set Score.tempoHideNote = ##t \tempo 4 = 156 \set Score.currentBarNumber = #110 \time 3/4 g'4 c''4( a'4 |
        g'4 f'4) f'4~ |
        f'4 d''4( f'4~ |
        f'4 e'4) e'16 g'16 c''16 e''16 |
        f''16 c''16 a'16 f'16 a'16 c''16 f''16 a''16 a''16 d''16 a''16 d'''16 |
        a''16 d''16 a''16 bf''16 g''16 d''16 g''16 bf''16 g''16 df''16 g''16 bf''16 |
        g''16 c''16 g''16 bf''16 e''16 c''16 e''16 g''16 g''16 e''16 g''16 c'''16 |
        g''16^\markup { \italic "cresc." } e''16 g''16 c'''16 a''16 f''16 a''16 c'''16 a''16 f''16 a''16 c'''16 \bar "||" |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key e \minor \time 3/4 <c' e'>4 c'4 cs'4 |
        d'4 a4 bf4 |
        b4 g4 d'4 |
        df'4 c'4 <bf c'~>4( |
        <a c'>4 <f f'>4 <fs d'>4 |
        <g c'>4 <d bf>4) <f bf~>4( |
        <e bf>4 g'4 <c bf~>4 |
        <f bf>4 <f a>4) a,4 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="贝多芬 Op.90 第一乐章" location="mm.129–148" id="op90-recap"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \set Score.tempoHideNote = ##t \tempo 4 = 156 \set Score.currentBarNumber = #129 \time 3/4 \oneVoice cs''16 g'16 cs''16 e''16 cs''16 g'16 cs''16 e''16 cs''16 g'16 cs''16 e''16 |
        \oneVoice b'16 g'16 b'16 e''16 g''16 fs''16 e''16 ds''16 e''16 ds''16 e''16 fs''16 \bar "||" |
        \oneVoice g''16 fs''16 e''16 ds''16 g''16 fs''16 e''16 ds''16 g''16 fs''16 e''16 ds''16 |
        \oneVoice g''16\ff fs''16 e''16 ds''16 e''8 r8 r4 |
        \oneVoice g''8\p( fs''8 e''8 ds''8 e''4) |
        \oneVoice g''4^\markup { \italic "sempre diminuendo" }( fs''4 e''4 |
        \oneVoice ds''4 e''4) r4 |
        \oneVoice g''2( fs''4~ |
        \oneVoice fs''4 e''4) r4 |
        \oneVoice g'2( fs'8 e'8 |
        \oneVoice e'4) r4 r4 |
        \oneVoice r4\pp g'4( fs'8 e'8) |
        \oneVoice e'8^\markup { \italic "cresc." }^\markup { \italic "Poco rit." } r8 r8 g'8( fs'8 e'8) |
        \oneVoice r8 g''8( fs''8 e''8) r8 g'8( |
        \oneVoice fs'8\f e'8) r4 g'8 r8 |
        \voiceOne g'4.^\markup { \italic "a Tempo" }( fs'8 <g e'>8) r8 |
        \oneVoice <a fs' a'>8\p r8 r4 <fs' a'>4 |
        \oneVoice <fs' a'>4.( g'8) <fs' a'>4-.( |
        \oneVoice <g' b'>4-.)\f r4 <b d' g' b'>8 r8 |
        \voiceOne b'4.( a'8 <b g'>8) r8 |
      }
      \new Voice {
        \voiceTwo s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        <g b e'>2 s4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        <b d' g'>2 s4 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \time 3/4 \voiceOne s4 g'2 |
        \voiceOne b4 e'4 g'4 |
        \oneVoice b'4 e''4 g''4 |
        \oneVoice r4 g''16 fs''16 e''16 ds''16 e''8 r8 |
        \oneVoice r4 g''8( fs''8 e''8 ds''8 |
        \oneVoice e''4) r4 g''4( |
        \oneVoice fs''4 e''4 ds''4 |
        \oneVoice e''4) r4 r4 |
        \oneVoice g''2( fs''4~ |
        \oneVoice fs''4 e''4) r4 |
        \oneVoice g'2( fs'8 e'8 |
        \oneVoice e'4) r4 g'4( |
        \oneVoice fs'8 e'8 e'8) r8 r8 g''8( |
        \oneVoice fs''8 e''8) r8 g''8( fs''8 e''8) |
        \oneVoice r8 \clef "bass" g8( fs8 e8) e8 r8 |
        \oneVoice <e, e>2 <e, e>8 r8 |
        \oneVoice <d, d>8 r8 r4 d'4 |
        \oneVoice <c' d'>4.( <b d'>8) <a c'>4-.( |
        \oneVoice <g b>4-.) r4 <g, g>8 r8 |
        \oneVoice <g, g>2 <g,, g,>8 r8 |
      }
      \new Voice {
        \voiceTwo as4 g'4\sf as4 |
        b2 s4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 再现部 · 同一副部在 e 小调

| 功能 | 呈示部 | 再现部 |
| --- | --- | --- |
| P 主部 | 弱起及第 1–24 小节，e 小调，开头为饱满的和弦 | 第 144–167 小节，e 小调。弱起缩成稀疏的八度，随即接回开头的附点节奏。 |
| S 副部 | 第 55–67 小节，b 小调，由 F♯ 属和声导入 | 第 198–214 小节，e 小调。第 196–197 小节的 B–D♯–F♯–A 属七导入副部，同类八度旋律与分解和弦移到主调。 |

这一次能在谱面上听见明确的根位属七引向 e 小调。把第 196–198 小节与展开末尾的第 129–144 小节对照，就能听出两处属功能处理的差别。

```lilypond title="贝多芬 Op.90 第一乐章" location="mm.196–205" id="op90-recap-s"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \set Score.tempoHideNote = ##t \tempo 4 = 156 \set Score.currentBarNumber = #196 \time 3/4 \oneVoice <b' b''>8( <c'' c'''>8) <c'' c'''>8-. <c'' c'''>8-. <c'' c'''>8-. <c'' c'''>8-. |
        \oneVoice <c'' c'''>8^\markup { \italic "dim." } <c'' c'''>8 <c'' c'''>8 <c'' c'''>8 <c'' c'''>8 <c'' c'''>8 |
        \oneVoice <c''' c''''>4\p <b''~ b'''~>2 |
        \oneVoice <b'' b'''>4 <e''~ e'''~>2 |
        \oneVoice <e'' e'''>4 <b'~ b''~>2 |
        \oneVoice <b' b''>4 e''2~ |
        \voiceOne e''4( c''4 b'4) |
        \voiceOne b'2 ds''4 |
        \oneVoice e''8 c''8( c'''4.-> b''8) |
        \oneVoice r8 b''8( fs''4.-> e''8) |
      }
      \new Voice {
        \voiceTwo s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        \change Staff = "down" a16 \change Staff = "up" g'16 e'16 g'16 \change Staff = "down" as16 \change Staff = "up" g'16 e'16 g'16 b16 g'16 e'16 g'16 |
        b16 g'16 e'16 g'16 b16 g'16 e'16 g'16 b16 a'16 fs'16 a'16 |
        s1*3/4 |
        s1*3/4 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \time 3/4 <b ds' fs' a'>8 <b ds' fs' a'>8 <b ds' fs' a'>8 <b ds' fs' a'>8 <b ds' fs' a'>8 <b ds' fs' a'>8 |
        <b ds' fs' a'>8 <b ds' fs' a'>8 <b ds' fs' a'>8 <b ds' fs' a'>8 <b ds' fs' a'>8 <b ds' fs' a'>8 \clef "bass" |
        e16 \change Staff = "up" g'16 \change Staff = "down" b16 \change Staff = "up" g'16 \change Staff = "down" fs16 \change Staff = "up" a'16 \change Staff = "down" b16 \change Staff = "up" a'16 \change Staff = "down" g16 \change Staff = "up" b'16 \change Staff = "down" b16 \change Staff = "up" b'16 \change Staff = "down" |
        e16 \change Staff = "up" g'16 \change Staff = "down" b16 \change Staff = "up" g'16 \change Staff = "down" fs16 \change Staff = "up" a'16 \change Staff = "down" b16 \change Staff = "up" a'16 \change Staff = "down" g16 \change Staff = "up" b'16 \change Staff = "down" b16 \change Staff = "up" b'16 \change Staff = "down" |
        e16 \change Staff = "up" g'16 \change Staff = "down" b16 \change Staff = "up" g'16 \change Staff = "down" fs16 \change Staff = "up" a'16 \change Staff = "down" b16 \change Staff = "up" a'16 \change Staff = "down" g16 \change Staff = "up" b'16 \change Staff = "down" b16 \change Staff = "up" b'16 \change Staff = "down" |
        e16 \change Staff = "up" g'16 \change Staff = "down" b16 \change Staff = "up" g'16 \change Staff = "down" fs16 \change Staff = "up" a'16 \change Staff = "down" b16 \change Staff = "up" a'16 \change Staff = "down" g16 \change Staff = "up" b'16 \change Staff = "down" b16 \change Staff = "up" b'16 \change Staff = "down" |
        R1*3/4 |
        R1*3/4 |
        e,16 g16 b,16 g16 fs,16 a16 b,16 a16 g,16 b16 b,16 b16 |
        e,16 g16 b,16 g16 fs,16 a16 b,16 a16 g,16 b16 b,16 b16 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

### 结束部与尾声

第 214–222 小节延续副部的收束。第 223 小节起，尾声再拉开时间。第 232–245 小节把主部的回应和后续乐句压缩在一起，力度渐弱，最后的低音 E 和上方 G、E 保持小调色彩。

```lilypond title="贝多芬 Op.90 第一乐章" location="mm.232–245" id="op90-coda"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \set Score.tempoHideNote = ##t \tempo 4 = 156 \set Score.currentBarNumber = #232 \time 3/4 \oneVoice <e'' g''>4.( <ds'' fs''>8 e''4) |
        \oneVoice <fs'' a''>4^\markup { \italic "Ritardando" } r4 <fs'' a''>4 |
        \oneVoice <fs'' a''>4.( g''8 <fs'' a''>4) |
        \oneVoice <g'' b''>4 r4 b''4 |
        \oneVoice b''4.( a''8 <g'' b''>4) |
        \oneVoice <a'' c'''>4 r4\fermata <e''~ e'''~>4 |
        \oneVoice <e'' e'''>4.^\markup { \italic "a Tempo" }( <ds'' ds'''>8 <e'' e'''>4) |
        \oneVoice <c' e' fs'>2 <cs' e' fs'>4 |
        \voiceOne fs'4.( g'8 a'8 g'8 |
        \oneVoice fs'4 e'4) <e''~ e'''~>4 |
        \oneVoice <e'' e'''>4.( <ds'' ds'''>8 <e'' e'''>4) |
        \oneVoice <c' e' fs'>2^\markup { \italic "dim." } <cs' e' fs'>4 |
        \voiceOne fs'4.\pp( a'8 g'8 fs'8 |
        \set Timing.measureLength = #1/2 \oneVoice <g e'>4) r4\fermata \bar "|." |
      }
      \new Voice {
        \voiceTwo s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        <a ds'>2. |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        <a ds'>2. |
        s1*1/2 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key e \minor \time 3/4 <e' g'>4.( <fs' a'>8 g'4) |
        <d' fs' a'>4 r4 d''4 |
        <c'' d''>4.( <b' d''>8 <a' c''>4) |
        <g' b'>4 r4 g''4 |
        g''4.( fs''8 e''4) |
        ds''4 r4\fermata r4 \clef "bass" |
        <g, e b>2. |
        a,2 as,4 |
        b,2. |
        <c g>2 <b,, b,>8( <a,, a,>8 |
        <g,, g,>2 <gs,, gs,>4 |
        <a,, a,>2 <as,, as,>4 |
        <b,, b,>2. |
        \set Timing.measureLength = #1/2 e,4) r4\fermata |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```
