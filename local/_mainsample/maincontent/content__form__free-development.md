---
name: 自由发展
description: 主题变形、调性目标、速度和织体共同组织长程发展，可以把宣叙调、变奏和赋格等写法组合成不同的整体。
---

# 自由发展

这一页从具体作品出发。先找出段落转换时发生了什么，再追踪哪些材料跨过了边界、在哪个调性或音区再次出现。每个案例都有自己的结构，下面的箭头表示该作品的听读顺序。

## 莫扎特《d 小调幻想曲》K. 397

**段落图**　Andante 琶音 → Adagio 歌唱主题 → Presto 华彩与 Adagio 回返 → D 大调 Allegretto

开头的三连音分解和弦不断改变和声和音区。第 11 小节的延长休止让这个过程停下，第 12 小节换成可歌唱的上声部，并把密集的音型放到伴奏里。后续两次 Presto 华彩把节拍暂时悬置，Tempo I 又恢复 Adagio 的速度和熟悉的旋律轮廓。D 大调 Allegretto 用新主题打开另一个调性区域。这里分析早期印本已收录的段落，通行谱的末尾另有补笔。

```lilypond title="莫扎特 K.397《d 小调幻想曲》" location="Andante → Adagio，mm.1–15" id="k397"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key d \minor \time 2/2
      \set Score.tempoHideNote = ##t
      \tempo "Andante" 2 = 40
      \clef bass
      \relative c {
        r4 \tuplet 3/2 { r8 f( a d a f' d a f) } |
        r4 \tuplet 3/2 { r8 f( a d a f' d a f) } |
        \clef treble
        r4 \tuplet 3/2 { r8 g( bf e bf g' e bf g) } |
        r4 \tuplet 3/2 { r8 g( bf e bf g' e bf g) } |
        r4 \tuplet 3/2 { r8 a( d fs d a' fs d a) } |
        r4 \tuplet 3/2 { r8 a( d fs d a' fs d a) } |
        r4 \tuplet 3/2 { d8 a' g~ } g4 \tuplet 3/2 { c,8 g' f!~ } |
        f4 \tuplet 3/2 { bf,8 f' ef~ } ef4 \tuplet 3/2 { b8 e d } |
        r4 \tuplet 3/2 { r8 cs e a cs e! a cs e } |
        \tuplet 3/2 { ds8 e bs cs gs a ds, e bs cs gs a } |
        r1^\fermata \bar "||" |
        \tempo "Adagio" 2 = 30
        f'4..\p e32 f g!8 f e d! |
        cs4 r8. d16-. ds8( e) r4 |
        g4.. fs32 g a8 g f e |
        d!4 r8. e16-. g8( f) r4 |
      }
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key d \minor \time 2/2
      \relative c, {
        <<
          {
            \voiceOne
            \tuplet 3/2 { d8 f a } d2. |
            \tuplet 3/2 { d,8 f a } d2. |
            \tuplet 3/2 { d,8 g bf } d2. |
            \tuplet 3/2 { d,8 g bf } d2. |
            \tuplet 3/2 { c,8 fs a } c2. |
            \tuplet 3/2 { c,8 fs a } c2. |
            \tuplet 3/2 { bf8 d g~ } g4 \tuplet 3/2 { a,8 c f!~ } f4 |
            \tuplet 3/2 { g,8 bf ef~ } ef4 \tuplet 3/2 { gs,8 b f'~ } f4 |
          } \\
          {
            d,1 | d1 | d1 | d1 | c1 | c1 | bf'2 a | g gs |
          }
        >>
        \oneVoice
        \tuplet 3/2 { a8 cs e! } a4 r2 |
        R1 |
        a,,2_\fermata r2 |
        \clef treble
        <<
          { r8 <f''' a> <f a> <f a> r <f a> <f a> <f a> |
            r <g a> <g a> <g a> r <g a> <g a> <g a> |
            r <e a> <e a> <e a> r <e a> <e a> <e a> |
            r <f a> <f a> <f a> r <f a> <f a> <f a> | } \\
          { d2 d | e e | cs cs | d d | }
        >>
      }
    }
  >>
  \layout { }
  \midi { }
}
```

## 莫扎特《c 小调幻想曲》K. 475

**段落图**　Adagio → Allegro → Andantino → Più allegro → Tempo primo

开头让两手同向陈述短动机，和声很快沿半音改变。其后 Allegro、Andantino 与 Più allegro 以速度、织体和调性形成几次大幅转折。Tempo primo 带回开头的速度、轮廓和 c 小调指向，在最后确认全曲的调性落点。把两段的第一句并排读，留意回返段保留了哪些音程，又怎样把开头的悬念转为收束。

```lilypond title="莫扎特 K.475《c 小调幻想曲》" location="Adagio，mm.1–3" id="k475-opening"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key c \major \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo "Adagio" 4 = 52
      c'4.\f( ef'8\p fs' g' af' c') |
      b8 r8 <c'' ef''>8( <b' d''>16) r16 <c'' fs''>8( <b' g''>16) r16 r4 |
      bf4.\f( df'8\p e'8.\turn f'16 g'8 bf) |
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key c \major \time 4/4
      <c, c>4.( <ef, ef>8 <fs, fs> <g, g> <af, af> <c, c>) |
      <b,, b,>8 r8 \clef treble fs'8( g'16) r16 af'8( g'16) r16 r4 \clef bass |
      <bf,, bf,>4.( <df, df>8 <e, e>8. <f, f>16 <g, g>8 <bf,, bf,>) |
    }
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="莫扎特 K.475《c 小调幻想曲》" location="Tempo primo，mm.161–163" id="k475-return"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef treble \key c \major \time 4/4 \set Score.currentBarNumber = #161
      \set Score.tempoHideNote = ##t
      \tempo "Tempo primo" 4 = 52
      c'4.\f( ef'8\p fs' g' af' c') |
      b8 r8 <c'' ef''>8( <b' d''>16) r16 <c'' fs''>8( <b' g''>16) r16 r4 |
      af4.\f( b!8\p c'8.\turn df'16 ef'8 af) |
    }
    \new Staff = "down" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \clef bass \key c \major \time 4/4
      <c, c>4.( <ef, ef>8 <fs, fs> <g, g> <af, af> <c, c>) |
      <b,, b,>8 r8 \clef treble fs'8( g'16) r16 af'8( g'16) r16 r4 \clef bass |
      <af,, af,>4.( <b,, b,>8 <c, c>8. <df, df>16 <ef, ef>8 <af,, af,>) |
    }
  >>
  \layout { }
  \midi { }
}
```

## 贝多芬 Op. 106 第四乐章

**段落图**　Largo 引子及速度变化 → Allegro risoluto 赋格 → 对位变形与主调收束

引子用分开的音区、休止、华彩和接连变化的速度来试探方向，随后以属功能聚焦到 B♭ 大调的赋格。听接缝时，先跟低音，随后跟入题声部的大跳和颤音。赋格中，主题还能经倒影、逆行和增值等方式变形，音乐的连续性来自对位线索。

```lilypond title="贝多芬 Op.106 第四乐章" location="Largo 至 Allegro risoluto 开头" id="op106-intro-fugue"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key bf \major \set Score.tempoHideNote = ##t \tempo "Largo" 4 = 40 \omit Staff.TimeSignature \time 6/4 \oneVoice r16\p \tuplet 3/2 { r32 r32 f32( } \tuplet 3/2 { f'32) r32 r32 } \tuplet 3/2 { f''32 f'''32~ f'''32~ } <f'' f'''>16.\fermata <f''~ f'''~>32 <f'' f'''>16 r16 r16. <f''~ af''~ df'''~ f'''~>32 <f'' af'' df''' f'''>16 r16 r16. <f''~ bf''~ df'''~ f'''~>32 <f'' bf'' df''' f'''>16 r16 r16. <gf''~ bf''~ df'''~ gf'''~>32 <gf''~ bf''~ df'''~ gf'''~>8 <gf'' bf'' df''' gf'''>32\fermata( df''32 gf''32 df''32 gf''32 df''32 gf''32 bf'32) \bar "" |
        \voiceOne ef''4^\markup { \italic "cresc." }^\markup { \italic "decresc." }\p ef''16 df''8 cf''16 bf'16 <bff' ef''>16 af'16~ af'32. bf'64 r4 r4 r4 |
        \time 5/4 \tempo "Un poco più vivace" 4 = 88 \oneVoice r32 r32 r16 r8 r32 fs'32 gs'32 as'32 b'32 cs''32 ds''32 e''32 ds''32 b'32 fs''32 e''32 ds''32 cs''32 b'32 as'32 b'32 fs''32 gs''32 as''32 b''32 cs'''32 ds'''32 e'''32 ds'''32 cs'''32 b''32 as''32 gs''32 fs''32 e''32 ds''32 \bar "" |
        \set Timing.measureLength = #23/32 \oneVoice cs''32^\markup { \italic "cresc." }^\markup { \italic "decresc." } b'32 as'32 gs'32 fs'32 e''32 ds''32 gs''32 fs''32 b''32 as''32 e'''32 <e'' as'' e'''>16.\fermata <ds''~ fs''~ b''~ ds'''~>32 <ds'' fs'' b'' ds'''>16 r16 r16 <ds''~ gs''~ b''~ ds'''~>32 |
        \time 4/4 \set Timing.measureLength = #1/1 \tempo "Allegro" 4 = 126 \oneVoice <ds'' gs'' b'' ds'''>16 ds''16 gs'16 ds''16 e''16 ds''16 gs'16 ds''16 e''2~ |
        \oneVoice e''16 as'16 ds''16 css''16 ds''16 as'16 ds''16 cs''16 bs'16 ds''16 bs'16 gs''16 cs''16 gs''16 ds''16 gs''16 |
        \oneVoice e''4 e'4~ e'16 cs'16 fs'16 es'16 fs'16 cs'16 fs'16 e'16 |
        \voiceOne r2. b''4~ |
        \voiceOne b''16\f gs''16 a''16 cs'''16 e''16 a''16 ds''16 gs''16 ds''16 gs''16 ds''16 fss''16 ds''16 gs''16 ds''16 as''16 |
        \tempo "Tempo I" 4 = 40 \oneVoice r8..\p\fermata <b'~ ds''~ gs''~ b''~>32 <b' ds'' gs'' b''>16 r16 r16. <b'~ e''~ gs''~ b''~>32 <b' e'' gs'' b''>8 r16 r16 <cs''~ e''~ gs''~ cs'''~>32 <cs'' e'' gs'' cs'''>16 r16 r16 <cs''~ e''~ a''~ cs'''~>32 |
        \time 3/4 \oneVoice <cs'' e'' a'' cs'''>16 \clef "bass" \tuplet 3/2 { a,32( a32 a32) } \clef "treble" \tuplet 3/2 { a'32( a'32 a''32)~ } \tuplet 3/2 { a''32~ <a''~ as'''~>32 <a''~ as'''~>32 } \key a \major \tuplet 3/2 { <a'' as'''>8( <gs'' gs'''>8 <e'' e'''>8 } \tuplet 3/2 { <ds'' ds'''>8 <d'' d'''>8 <b' b''>8) } |
        \key a \major \time 10/4 \oneVoice \tuplet 6/4 { gs''16 e''16 ds''16 d''16 b'16 gs'16 } \tuplet 3/2 { e'16( ds'16 d'16 } \clef "bass" b32 gs32 e32 ds32) d4. ds8~ ds8 e4.\fermata \grace { ds4( } \grace { e4 } <cs~ e~>16) <cs e>16 <cs e>32 r32 <cs e>16 <cs~ e~>16 <cs e>16 <cs a>32 r32 <cs fs a>16 <fs~ a~>16 <fs a>16 <fs a>32 r32 <fs a>16 <fs~ a~>16 <fs a>16 <fs d'>32 r32 <fs b d'>16 \clef "treble" |
        \time 6/4 \oneVoice <b~ d'~>16 <b d'>16 <b d'>32 r32 <b d'>16 <b~ d'~>16 <b d'>16 <b g'>32 r32 <b g'>16 <e'~ g'~>16 <e' g'>16 <e' g'>32 r32 <e' g'>16 <e'~ c''~>16 <e' c''>16 <e' c''>32 r32 <e' c''>16 <a'~ c''~>16 <a' c''>16 <a' c''>32 r32 <a' c''>16 <a'~ f''~>16 <a' f''>16 <a' d'' f''>32 r32 <a' d'' f''>16 |
        \oneVoice <a' cs''~ e''~ a''~>16(\ff^\markup { \italic "decresc." } <a' cs'' e'' a''>16) <a' cs'' e'' a''>32 r32 <a' cs'' e'' a''>16 <a' cs''~ e''~ a''~>16( <a' cs'' e'' a''>16) <a' cs'' e'' a''>32 r32 <a' cs'' e'' a''>16 <a'~ cs''~ e''~ a''~>16 <a' cs'' e'' a''>16 <a' a''>32 r32 <a' a''>16 <a'~ a''~>16 <a' a''>16 <a' a''>32 r32 <a' a''>16 <a'~ a''~>16 <a' a''>16 <a' a''>32 r32 <a' a''>16 <a'~ a''~>16 <a' a''>16 <a' a''>32 r32 <a' a''>16 |
        \undo \omit Staff.TimeSignature \time 3/4 \tempo "Allegro risoluto" 4 = 144 \oneVoice a''2.\pp~\trill |
        \oneVoice a''4 c'''2~\trill |
        \oneVoice c'''4^\markup { \italic "cresc." } f'''2~\trill |
        \oneVoice f'''16\f ef'''16 d'''16 c'''16 bf''16 a''16 g''16 f''16 ef''16-. d''16 c''16 f''16 |
        \oneVoice <bf d' f' bf'>8\p r8 r8 g'16 f'16 ef'16 d'16 c'16 bf16 \clef "bass" |
        \oneVoice a16 bf16 a16 g16 f16 g16 f16 ef16 d16 ef16 d16 c16 |
      }
      \new Voice {
        \voiceTwo s1*3/2 |
        r32 gf'32( cf''32 gf'32 cf''32 gf'32 cf''32 ef'32 f'32) af'32 f'32 af'32 f'32 af'32 f'32 af'32 gf'16 gf'16 f'16~ f'32. gf'64 <bf' df'' gf'' bf''>16 r16 r16. <bf'~ ef''~ gf''~ bf''~>32 <bf' ef'' gf'' bf''>16 r16 r16. <ef'' gf'' ef'''>32( <ds'' fs'' ds'''>32)\fermata r32 r16 r8 |
        s1*5/4 |
        s1*23/32 |
        s1 |
        s1 |
        s1 |
        ds'8 ds''4 cs''8 b'16 ds''16 b'16 ds''16 e''16 ds''16 b'16 ds''16 |
        e''4 a'8 b'8 b'8 cs''8 b'8 as'8 |
        s1 |
        s1*3/4 |
        s1*5/2 |
        s1*3/2 |
        s1*3/2 |
        s1*3/4 |
        s1*3/4 |
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
        \clef "bass" \key bf \major \omit Staff.TimeSignature \time 6/4 \oneVoice r16 \tuplet 3/2 { f,32 f32 r32 } \tuplet 3/2 { r32 \clef "treble" f'32 f''32 } \clef "bass" \tuplet 3/2 { r32 r32 <f,,~ f,~>32 } <f,, f,>16.\fermata r32 r16 <f, f>16 r16 r16 r16 <df, df>16 r16 r16 r16 <bf,, bf,>16 r16 r16 r16 <gf,,~ gf,~>16 <gf,, gf,>32\fermata r32 r16 r8 |
        \oneVoice r4 r32 f32( af32 f32 af32 f32 af32 df32) gf16( c16 df16 gf,16) r16 <gf, gf>16 r16 r16 r16 <ef, ef>16 r16 r16 <b,, b,>32\fermata r32 r16 r8 |
        \time 5/4 \oneVoice r32 fs32 gs32 as32 b32 cs'32 ds'32 e'32 ds'32 b32 fs'32 e'32 ds'32 cs'32 b32 as32 b32 fs32 gs32 as32 b32 cs'32 ds'32 e'32 ds'32 \clef "treble" ds''32 fs''32 e''32 ds''32 cs''32 b'32 as'32 b'32 as'32 ds''32 cs''32 b'32 as'32 gs'32 fs'32 |
        \set Timing.measureLength = #23/32 \oneVoice e'32 ds'32 cs'32 b32 as32 cs'32 b32 e'32 ds'32 d'32 cs'32 fs32 \clef "bass" <fs cs' fs'>16.\fermata r16 <b,, b,>16 r16 r16 |
        \time 4/4 \set Timing.measureLength = #1/1 \oneVoice <gs,, gs,>8 r8 r4 r16 \clef "treble" gs'16 cs'16 gs'16 as'16 gs'16 cs'16 gs'16 |
        \oneVoice fss'4. fs'8~ fs'8 fs'8 e'8 ds'8 \clef "bass" |
        \oneVoice cs'16 gs16 cs16 gs16 a16 gs16 cs16 gs16 a4. gs8 |
        \voiceOne as16 cs'16 as16 ds'16 e'16 ds'16 as16 ds'16 gs16 b16 gs16 b16 cs'16 b16 gs16 b16 |
        \voiceOne e8 cs'4 b8 b8 as8 gs8 fss8 |
        \oneVoice r8\fermata r8 r16 <gs, gs>16 r16 r16 r16 <e, e>16 r16 r16 r16 <cs, cs>16-. r16 r16 |
        \time 3/4 \oneVoice \tuplet 3/2 { r32 a,,32 a,32 } r16 r16 \tuplet 3/2 { r32 r32 <a,, a,>32 } \key a \major <a,, d, e, b,>2 |
        \key a \major \time 10/4 \oneVoice <a,,~ d,~ e,~ b,~>1 <a,, d, e, b,>2 r16 <a,, a,>16 r32. <a,, a,>64 r16 r16 <a,, a,>16 r32. <fs,, fs,>64 r16 r16 <d, d>16 r32. <d, d>64 r16 r16 <d, d>16 r32. <b,, b,>64 r16 |
        \time 6/4 \oneVoice r16 <g, g>16 r32. <g, g>64 r16 r16 <g, g>16 r32. <e, e>64 r16 r16 <c c'>16 r32 <c c'>32 r16 r16 <a, a>16 r32 <a, a>32 r16 r16 <f, f>16 r32 <f, f>32 r16 r16 <d, d>16 r32 <d, d>32 r16 |
        \oneVoice r16 <a,, cs, e, a,>16 r32 <a,, cs, e, a,>32 r16 r16 <a,, cs, e, a,>16 r32 <a,, cs, e, a,>32 r16 r16 <a,, cs, e, a,>16 r32 <a,, a,>32 r16 r16 <a,, a,>16 r32 <a,, a,>32 r16 r16 <a,, a,>16 r32 <a,, a,>32 r16 r16 <f,, f,>16 r32 <f,, f,>32 r16 |
        \undo \omit Staff.TimeSignature \time 3/4 \oneVoice <f,, f,>8 r8 <f a>8 r8 r4 |
        \oneVoice <f,, f,>8 r8 <a c'>8 r8 r4 |
        \oneVoice <f,, f,>8 r8 <f a c' f'>8-. r8 <f,, f,>8 r8 |
        \oneVoice <f a c' f'>8 r8 <f,, f,>4. g,16 a,16 |
        \oneVoice <bf,, d, f, bf,>8 r8 r4 r4 |
        \oneVoice f8 r8 \clef "treble" a'2 |
      }
      \new Voice {
        \voiceTwo s1*3/2 |
        s1*3/2 |
        s1*5/4 |
        s1*23/32 |
        s1 |
        s1 |
        s1 |
        fs2 r4 r8 b,8 |
        cs4. ds8 ds4. ds8 |
        s1 |
        s1*3/4 |
        s1*5/2 |
        s1*3/2 |
        s1*3/2 |
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

## 贝多芬 Op. 110 第三乐章

**段落图**　慢引子与宣叙调 → Arioso dolente → 赋格 → Arioso 回归 → 倒影赋格 → 原形与主调回归

第一次咏叹调在 a♭ 小调以重复和弦托住歌唱线，随后 A♭ 大调赋格用一连串上行四度建立新方向。咏叹调在 g 小调回归，旋律被休止切得更碎。第二次赋格从 G 大调出发，把原来向上的四度倒转成向下，逐步加速、加密，再带回主题原形并在 A♭ 大调结束。

```lilypond title="贝多芬 Op.110 第三乐章" location="mm.9–16" id="op110-arioso-one"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key gf \major \set Score.tempoHideNote = ##t \tempo "Arioso dolente" 4 = 60 \set Score.currentBarNumber = #9 \time 12/16 ef''8.\p~ ef''8( df''16~ df''8 cf''16 bf'16 cf''16 af'16) |
        af'8.( g'8.)~ g'8( ff''16~ ff''8 ef''16) |
        ef''8^\markup { \italic "cresc." }( af''16~ af''8 gf''16)~ gf''8( ff''16 ef''8 df''16) |
        cf''8.\p~^\markup { \italic "cresc." }^\markup { \italic "decresc." } cf''16( df''16 ef''32 df''64 cf''64) bf'8.~ bf'16( cf''16 df''16) |
        cf''4.\p( df''4. |
        ef''4. ff''8. af''8. |
        gf''8^\markup { \italic "decresc." } cf'''16 af''8 af'''16)~ af'''8 gf'''16~( gf'''16 ef'''16 ff'''32 bf''32) |
        df'''4.( cf'''8.) ef''8. |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key gf \major \time 12/16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 |
        <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef>16 <bf, df ef g>16 |
        <cf ef af>16 <cf ef af>16 <cf ef af>16 <c ef af>16 <c ef af>16 <c ef af>16 <df ff af>16 <df ff af>16 <df ff af>16 <ff af df'>16 <ff af df'>16 <ff af df'>16 |
        <ef af cf'>16 <ef af cf'>16 <ef af cf'>16 <ef af cf'>16 <ef af cf'>16 <ef af cf'>16 <ef g bf>16 <ef g bf>16 <ef g bf>16 <df ef g bf>16 <cf ef af>16 <bf, ef g>16 |
        <af, ef af>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <af, cf ef>16 <gf, cf ff>16 <gf, cf ff>16 <gf, cf ff>16 <gf, bf, ff>16 <gf, bf, ff>16 <gf, bf, ff>16 |
        <gf, cf ef>16 <gf, cf ef>16 <gf, cf ef>16 <cf gf cf'>16 <cf gf cf'>16 <cf gf cf'>16 <df ff cf'>16 <df ff cf'>16 <df ff cf'>16 <df ff bf>16 <df ff bf>16 <df ff bf>16 |
        <ef gf cf'>16 <ef gf cf'>16 <ef gf cf'>16 <ff cf' ff'>16 <ff cf' ff'>16 <ff cf' ff'>16 <gf cf' ef'>16 <gf cf' ef'>16 <gf cf' ef'>16 <gf bf df' ff'>16 <gf bf df' ff'>16 <gf bf df' ff'>16 |
        <g bf df' ff'>16 <g bf df' ff'>16 <g bf df' ff'>16 <gf bf df' ff'>16 <gf bf df' ff'>16 <gf bf df' gf'>16 \clef "treble" <cf' ef' gf'>16 <cf' ef' gf'>16 <cf' ef' gf'>16 <cf' ef' gf'>16 <cf' ef' gf'>16 <cf' ef' gf'>16 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="贝多芬 Op.110 第三乐章" location="mm.116–123" id="op110-arioso-two"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key g \minor \set Score.tempoHideNote = ##t \tempo "L’istesso tempo di Arioso" 4 = 60 \set Score.currentBarNumber = #116 \time 12/16 \grace { d'16(\p } d''8.)~ d''8 c''16 c''16( bf'16) r32 a'32 a'16( bf'16) r32 g'32 |
        g'8^\markup { \italic "cresc." }(^\markup { \italic "decresc." } fs'16~ fs'8 ef''16) r16 ef''16( f''32 ef''32) r16 d''16( ef''32 d''32) |
        d''8^\markup { \italic "cresc." }( g''16)~ g''16 g''16( f''16) r16 f''16( ef''16) r16 d''16 c''16~ |
        c''16(^\markup { \italic "decresc." }\p bf'16 c''32 d''32) r16 d''16( c''32 bf'32 bf'8.)( a'8.) |
        bf'8.^\markup { \italic "cresc." }~ bf'16( a'16 bf'32-.) r32 c''8.~ c''16( b'16 c''32-.) r32 |
        d''8.~ d''16( cs''16 d''16-.) r16 d''16( ef''16) r16 fs''16( g''16) |
        r16 g''32( f''32 bf''16)~ bf''16( a''32 g''32 g'''16)~ g'''16 f'''16( d''16) r16. f''32( ef''32 a'32) |
        \grace { a'16( } c''4.)( bf'8. d''8.) |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key g \minor \time 12/16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 <g, bf, d>16 |
        <a, c d>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 <a, c d fs>16 |
        <bf, d g>16 <bf, d g>16 <bf, d g>16 <b, d g>16 <b, d g>16 <b, d g>16 <c ef g>16 <c ef g>16 <c ef g>16 <ef g c'>16 <ef g c'>16 <ef g c'>16 |
        <d g bf>16 <d g bf>16 <d g bf>16 <d g bf>16 <d g bf>16 <d g bf>16 <d g bf>16 <d g bf>16 <d g bf>16 <d fs a>16 <d fs a>16 <d fs a>16 |
        <g, bf, d g>16 <g, bf, d g>16 <g, bf, d g>16 <g, bf, ef>16 <g, bf, ef>16 <g, bf, ef>16 <f, bf, ef>16 <f, bf, ef>16 <f, bf, ef>16 <f, a, ef>16 <f, a, ef>16 <f, a, ef>16 |
        <f, bf, d>16 <f, bf, d>16 <f, bf, d>16 <f, af, bf, d>16 <f, af, bf, d>16 <f, af, bf, d>16 <g, bf, ef>16 <g, bf, ef>16 <g, bf, ef>16 <ef, bf, ef>16 <ef, bf, ef>16 <ef, bf, ef>16 |
        <d, bf, d>16 <d, bf, d>16 <d, bf, d>16 <ef, bf, ef>16 <ef, bf, ef>16 <ef, bf, ef>16 <f, bf, d>16 <f, bf, d>16 <f, bf, d>16 <gf, c ef>16 <gf, c ef>16 <gf, c ef gf>16 |
        <gf, c ef gf>16 <gf, c ef gf>16 <f, c ef f>16 <f, c ef f>16 <f, a, c ef>16 <f, a, c ef>16 <f, bf, d>16 <bf, d f>16 <bf, d f>16 <bf, d f>16 <bf, d f>16 <bf, d f>16 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="贝多芬 Op.110 第三乐章" location="主题弱起及 mm.28–35" id="op110-fugue-one"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key gf \major \set Score.tempoHideNote = ##t \tempo "Fuga. Allegro ma non troppo" 4 = 110 \set Score.currentBarNumber = #28 \time 6/8 \partial 1*3/8 r4 r8 |
        \set Timing.measureLength = #3/4 \set Score.currentBarNumber = #28 R1*3/4 |
        R1*3/4 |
        R1*3/4 |
        r4\p r8 ef'4.( |
        af'4.\p f'4. |
        bf'4. g'4. |
        c''4. bf'4 af'8 |
        g'4.) bf'4. |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key gf \major \time 6/8 \partial 1*3/8 af4.( |
        \set Timing.measureLength = #3/4 df'4. bf4. |
        ef'4. c'4. |
        f'4. ef'4 df'8) |
        c'4.~ c'8 af8 g8 |
        f8 g8 ef8 d8 ef8 f8 |
        g8 af8 f8 e8 f8 g8 |
        af8 g8 af8 bf8 c'8 d'8 |
        ef'8 f'8 d'8 ef'8 f'8 df'8 |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="贝多芬 Op.110 第三乐章" location="主题弱起及 mm.137–144" id="op110-fugue-two"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "up" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "treble" \key gf \major \set Score.tempoHideNote = ##t \tempo "L’istesso tempo della Fuga" 4 = 110 \set Score.currentBarNumber = #137 \time 6/8 \partial 1*3/8 \oneVoice d''4. |
        \set Timing.measureLength = #3/4 \set Score.currentBarNumber = #137 \oneVoice a'4.( c''4. |
        \oneVoice g'4. b'4. |
        \oneVoice fs'4. g'4 a'8) |
        \voiceOne r4. g''4.( |
        \voiceOne d''4. fs''4. |
        \voiceOne cs''4. e''4. |
        \voiceOne a'4. b'4 cs''8 |
        \voiceOne d''8 c''8 b'8 a'4 b'8) |
      }
      \new Voice {
        \voiceTwo s1*3/8 |
        s1*3/4 |
        s1*3/4 |
        s1*3/4 |
        b'4.~ b'8 c''8 b'8~( |
        b'8 a'8 gs'8 a'8 b'8 a'8)~( |
        a'8 g'8 fs'8 g'8 a'8 g'8)~ |
        g'8 e'8 fs'8 g'8 fs'8 e'8 |
        fs'8 a'8 g'8~ g'8 f'4 |
      }
    >>
    \new Staff = "down" <<
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \new Voice {
        \clef "bass" \key gf \major \time 6/8 \partial 1*3/8 r4 r8 |
        \set Timing.measureLength = #3/4 R1*3/4 |
        R1*3/4 |
        R1*3/4 |
        R1*3/4 |
        R1*3/4 |
        R1*3/4 |
        R1*3/4 |
        r4 r8 d'4. |
      }
    >>
  >>
  \layout { }
  \midi { }
}
```

## 贝多芬《第九交响曲〈合唱〉》第四乐章

**段落图**　器乐宣叙与前三乐章回顾 → 低弦欢乐主题及变奏 → 人声宣叙与合唱 → 进行曲与器乐发展 → 两主题结合 → 尾声

开头大提琴与低音提琴用宣叙式的断句回应乐队。欢乐主题在第 92 小节由低弦轻声提出，随后交给更丰富的配器。第 216 小节男中音独唱把器乐宣叙的角色接过来。第 595 小节附近引入「亿万人民，相互拥抱」的主题，第 655 小节起进入双主题的对位结合。把低弦主题的朴素句法与后面的合唱声部对照，可以听出同一材料从单线到全乐章高潮的过程。

```lilypond title="贝多芬 Op.125《第九交响曲》第四乐章" location="低弦的欢乐主题，mm.92–99" id="op125-joy"
\version "2.26.0"
\language "english"

joy = {
  \key d \major \time 4/4
  fs2\p( fs4 g) |
  a4( g fs e) |
  d2( e4 fs) |
  fs4.( e8) e2 |
  fs2( fs4 g) |
  a4( g fs e) |
  d2( e4 fs) |
  e4.( d8) d2 |
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Violoncello" } {
      \set Staff.midiInstrument = "cello"
      % GM 42
      \clef bass
      \set Score.currentBarNumber = #92
      \tempo "Allegro assai" 2 = 80
      \joy
    }
    \new Staff \with { instrumentName = "Contrabbasso" } {
      \set Staff.midiInstrument = "contrabass"
      % GM 43
      \clef "bass_8"
      \transpose c c, \joy
    }
  >>
  \layout { }
  \midi { }
}
```

```lilypond title="贝多芬 Op.125《第九交响曲》第四乐章" location="双主题开头，mm.655–663（女高音、女低音）" id="op125-double"
\version "2.26.0"
\language "english"

\score {
  \new ChoirStaff <<
    \new Staff \with { instrumentName = "Soprano" } {
      \set Staff.midiInstrument = "choir aahs"
      % GM 52
      \clef treble \key d \major \time 6/4
      \set Score.currentBarNumber = #655
      \tempo "Allegro energico, sempre ben marcato" 2. = 84
      \partial 2.
      r2. |
      \set Score.currentBarNumber = #656
      fs''2\f^\markup { \italic "Freude" } fs''4 g''2 a''4 |
      a''2 g''4 fs''2 e''4 |
      d''2 d''4 e''2 fs''4 |
      fs''2 e''4 d''2( cs''4) |
      b'2 b'4 cs''2 d''4 |
      d''2 cs''4 b'2 a'4 |
      g'2 fs'4 e'2 d'4 |
      a'2 a'4 a'2 r4 |
    }
    \new Staff \with { instrumentName = "Alto" } {
      \set Staff.midiInstrument = "choir aahs"
      % GM 52
      \clef treble \key d \major \time 6/4
      \partial 2.
      d''2.\f^\markup { \italic "Seid umschlungen" }~ |
      d''2. d''2. |
      cs''2. a'2. |
      b'2. b'2. |
      a'2. fs'2. |
      g'2. g'2. |
      fs'2. d'2. |
      b'2. b'2. |
      a'2. cs'2. |
    }
  >>
  \layout { }
  \midi { }
}
```

## 跨作品对照

| 案例 | 边界如何听见 | 材料怎样延续 | 高潮与收束 |
| --- | --- | --- | --- |
| K. 397 | 延长休止、速度切换和华彩 | Adagio 主题在华彩后回返 | D 大调 Allegretto 改变全曲的色彩 |
| K. 475 | 速度、调性与音型成组改变 | Tempo primo 带回开头轮廓 | 多次离调后以 c 小调终止 |
| Op. 106 IV | 自由引子的断句转成稳定的赋格脉冲 | 大跳与颤音使赋格主题易于追踪 | 对位和音区逐步扩展，最后确认主调 |
| Op. 110 III | 宣叙、咏叹与赋格交替 | 咏叹旋律移调，赋格主题倒影后回到原形 | 渐快、渐强，最后回到 A♭ 大调 |
| Op. 125 IV | 器乐宣叙、人声进入、进行曲和合唱换层 | 欢乐主题经过变奏和配器转换，再与另一主题叠合 | 声部与配器逐级增多，最后在 D 大调收束 |

读这类作品时，可以先在谱上标出段落接缝、主题再次出现的位置和全曲最强的终止，再看三者何时重合。写作时，听众即使不熟悉全曲的结构，也能通过反复听见的音程、节奏或低音方向认出长程联系。
