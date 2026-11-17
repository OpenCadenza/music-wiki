---
schema_version: 1
collection: horizontal-homophony
kind: form
form_id: alberti-bass
category: texture
topic_name: 阿尔贝蒂低音
question: "旋律拉长时怎样保持流动，旋律走密时怎样留出空间？"
title: "阿尔贝蒂低音｜旋律拉长时怎样保持流动，旋律走密时怎样留出空间？"
description: "用「低–高–中–高」的重复次序展开既定和弦。组首给旋律一个落脚点，组内的回返持续供给脉冲。"
aliases: ["Alberti bass"]
accent:
  downbeat: "低音通常落在音型组首，组首与强拍对齐时，重拍最容易听清。"
  emphasis: "把组内两次高音当作细分，留出组首的相对重量。"
  grouping: "按低音再次发声的位置划组。"
pattern:
  音序: "低–高–中–高"
  循环单位: "四次等距发音，时值随段落安排"
cases:
  - id: mozart-k545-i-mm1-12
    question: "旋律拉长时怎样保持流动，旋律走密时怎样留出空间？"
    composer: 莫扎特
    work: "K.545"
    section: "第一乐章"
    measures: { start: 1, end: 12 }
    meter: "4/4"
    tempo:
      marking: "Allegro"
      unit: "1/4"
      bpm: 120
      source: playback
    observed_accent: "第 1 小节第 1、3 拍由低 C 起组。"
    feel: ["流动", "清楚"]
    tension:
      level: low
      evidence: "第 1 小节每拍两次伴奏发音，节奏间隔均匀。第 5–8 小节的中间两拍有伴奏休止。"
    notation:
      format: lilypond
      id: mozart-k545-i-mm1-12
---

<script setup>
import TextureFacts from "../../.vitepress/theme/TextureFacts.vue"
</script>

# 阿尔贝蒂低音｜旋律拉长时怎样保持流动，旋律走密时怎样留出空间？

用「低–高–中–高」的重复次序展开既定和弦。组首给旋律一个落脚点，组内的回返持续供给脉冲。

<TextureFacts />

## 谱例

<TextureFacts case-id="mozart-k545-i-mm1-12" />

第 1 小节旋律 C 持续两拍，伴奏的 C–G–E–G 正好走完一组。第三拍低 C 再发，旋律这时换到 E。第 2 小节把组首换成 D，组内次序与发音间距照旧。

第 5–8 小节的音阶从八分音符接十六分音符。伴奏在每小节第一拍落下，第二、三拍休止，第四拍再发声。把第 1 小节的四音循环临时铺到第 5 小节试听，再删去中间两拍的伴奏，比较音阶的轮廓。

```lilypond title="莫扎特 K.545 第一乐章" location="mm.1–12" id="mozart-k545-i-mm1-12"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \key c \major
      \time 4/4
      \set Score.tempoHideNote = ##t
      \tempo "Allegro" 4 = 120
      \relative c'' {
        c2(\p e4) g | b,4.( c16 d c4) r |
        a'2( g4) c | g4( f8\trill e16 f e4) r |
        a,8( b16 c d e f g a g f e d c b a |
        g8 a16 b c d e f g f e d c b a g |
        f8 g16 a b c d e f e d c b a g f |
        e8 f16 g a b c d e d c b a g f e |
        d8 e16 f g a b cs d a b cs d e f g |
        a b c! b a g f e f g a g f e d c) |
        b8-.\f g'-. e-. c-. d-. g-. e-. c-. |
        d4-. <b d g>-. g-. r |
      }
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \key c \major
      \time 4/4
      \clef bass
      {
        \clef treble
        c'8( g' e' g' c' g' e' g' |
        d' g' f' g' c' g' e' g' |
        c' a' f' a' c' g' e' g' |
        b g' d' g' c' g' e' g') |
        f'4 r r \clef bass <f c'> |
        <e c'> r r <e c'> |
        <d c'> r r <d b> |
        <c c'> r r <c e> |
        <f a>1 |
        f4. g8 a4. fs8 |
        g,16 b, d g g, c e g g, b, d g g, c e g |
        g,4-. g-. g,-. r |
      }
    }
  >>
  \layout { }
  \midi { }
}
```
