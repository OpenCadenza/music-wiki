---
schema_version: 1
collection: horizontal-homophony
kind: form
form_id: repeated-notes
category: texture
topic_name: 重复音
question: "怎样用连续复击建立脉冲，并让句子继续向前？"
title: "重复音｜怎样用连续复击建立脉冲，并让句子继续向前？"
description: "让同一个音或同一组音连续重新发声，建立可预期的脉冲。旋律可以在脉冲之上渐渐取得独立的节奏。"
aliases: ["Repeated notes", "重复和弦"]
accent:
  downbeat: "按节拍把复击划组，低音首击或组首的变化可以标出重拍。"
  emphasis: "利用长音、休止或音组改变提示重心。"
  grouping: "比较一组内复击的间距，以及换组时发生的变化。"
pattern:
  复击单位: "同一音或同一组音"
  脉冲安排: "固定组内间距，换组时调整发音或留空"
cases:
  - id: beethoven-op53-i-mm1-8
    question: "怎样用连续复击建立脉冲，并让句子继续向前？"
    composer: 贝多芬
    work: "Op.53《华尔斯坦》"
    section: "第一乐章"
    measures: { start: 1, end: 8 }
    meter: "4/4"
    tempo:
      marking: "Allegro con brio"
      unit: "1/4"
      bpm: 144
      source: playback
    observed_accent: "第 1 小节低 C 先落，右侧音组在第一拍后半加入。"
    feel: ["轻奏", "持续推进"]
    tension:
      level: medium
      evidence: "第 1–3 小节下方保持八分复击，上方在第 3 小节换成附点长音与短音。"
    notation:
      format: lilypond
      id: beethoven-op53-i-mm1-8
---

<script setup>
import TextureFacts from "../../.vitepress/theme/TextureFacts.vue"
</script>

# 重复音｜怎样用连续复击建立脉冲，并让句子继续向前？

让同一个音或同一组音连续重新发声，建立可预期的脉冲。旋律可以在脉冲之上渐渐取得独立的节奏。

<TextureFacts />

## 谱例

<TextureFacts case-id="beethoven-op53-i-mm1-8" />

第 1 小节低 C 单独起拍，后面的八分音符复击给出脉冲。第 2 小节末尾音组变化，八分间距继续。第 3 小节下方仍然每拍两次发音，上方改用附点四分音符、十六分音符和休止形成清楚的句子。

在自己的段落先保留八分复击，分别试听移动一次上方起音和加一个休止。比较哪次变化更容易听出句子的方向。

```lilypond title="贝多芬 Op.53《华尔斯坦》 第一乐章" location="mm.1–8" id="beethoven-op53-i-mm1-8"
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
      \tempo "Allegro con brio" 4 = 144
      {
        \clef bass
        r8\pp \repeat unfold 7 { <c e>8 } |
        \repeat unfold 6 { <c e>8 } <d fs>8 <d fs> |
        <d g>4.( b16 a g8-.) r8 r4 |
        \clef treble \acciaccatura cs'''8 d'''4~( d'''16 c''' b'' a'' g''4) r |
        \clef bass \repeat unfold 8 { <bf, d>8 } |
        \repeat unfold 6 { <bf, d>8 } <c e>8 <c e> |
        <c f>4.( a16 g f8-.) r8 r4 |
        \clef treble \acciaccatura b''8 c'''4~( c'''16 bf'' af'' g'' f''4) r |
      }
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \key c \major
      \time 4/4
      \clef bass
      {
        c,8 \repeat unfold 7 { <c, g,>8 } |
        \repeat unfold 6 { <c, g,>8 } <c, a,>8 <c, a,> |
        \repeat unfold 8 { <b,, g,>8 } |
        \repeat unfold 8 { <b,, g,>8 } |
        \repeat unfold 8 { <bf,, f,>8 } |
        \repeat unfold 6 { <bf,, f,>8 } <bf,, g,>8 <bf,, g,> |
        \repeat unfold 8 { <a,, f,>8 } |
        \repeat unfold 8 { <af,, f,>8 } |
      }
    }
  >>
  \layout { }
  \midi { }
}
```
