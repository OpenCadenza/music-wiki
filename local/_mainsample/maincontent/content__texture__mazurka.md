---
schema_version: 1
collection: horizontal-homophony
kind: form
form_id: mazurka
category: dance
topic_name: 玛祖卡
question: "第三拍加重时，怎样让第一拍仍然站得住？"
title: "玛祖卡｜第三拍加重时，怎样让第一拍仍然站得住？"
description: "三拍子给舞步提供落脚点，旋律可在第二或第三拍借重音、时值或跨小节延音改变重心。"
aliases: ["Mazurka"]
accent:
  downbeat_beat: 1
  emphasis_beats: [2, 3]
  typical_meters: ["3/4"]
  downbeat: "小节第一拍提供节拍落脚。"
  emphasis: "第二或第三拍可被突出，具体听旋律、时值和重音记号。"
  grouping: "以一小节为三拍一组，分辨落脚拍和旋律的强调位置。"
pattern:
  舞步节拍: "三拍"
  典型做法: "在第一拍保留节拍支点，在后续拍位加入强调"
cases:
  - id: chopin-op6no1-mm1-8
    question: "第三拍加重时，怎样让第一拍仍然站得住？"
    composer: 肖邦
    work: "Op.6 No.1"
    measures: { start: 1, end: 8 }
    meter: "3/4"
    tempo:
      marking: "Mazurka"
      unit: "1/4"
      bpm: 132
      source: score
    observed_accent: "第 6 小节第三拍的旋律 A 有重音并延续过小节线。"
    feel: ["有弹性", "含蓄"]
    tension:
      level: medium
      evidence: "第 6 小节第一拍的三连音与末拍的长重音形成发音密度反差。"
    notation:
      format: lilypond
      id: chopin-op6no1-mm1-8
---

<script setup>
import TextureFacts from "../../.vitepress/theme/TextureFacts.vue"
</script>

# 玛祖卡｜第三拍加重时，怎样让第一拍仍然站得住？

三拍子给舞步提供落脚点，旋律可在第二或第三拍借重音、时值或跨小节延音改变重心。

<TextureFacts />

## 谱例

<TextureFacts case-id="chopin-op6no1-mm1-8" />

第 1 小节的第一拍有低 C♯ 和旋律三连音。把小节的第一拍先拍稳，再唱第 6 小节第三拍带重音的 A。A 接到下一小节开头，三拍的落脚仍可从伴奏位置听见。

写类似段落时，先只延长第三拍的旋律音，再另试写上力度重音。两次试听都维持第一拍的脉冲。

```lilypond title="肖邦 Op.6 No.1" location="弱起，mm.1–8" id="chopin-op6no1-mm1-8"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \partial 4
      \key fs \minor
      \time 3/4
      \tempo "Mazurka" 4 = 132
      <<
        \relative c' {
          fs4->\p~ |
          \tuplet 3/2 { fs8( gs fs) } es8[ fs gs8. d16] |
          cs8[ r16 fs] a4 a->~ |
          \tuplet 3/2 { a8( b a) } gs8[ a b8. fs16] |
          e8[ r16 a] cs8 r cs4->~ |
          \tuplet 3/2 { cs8( ds cs) } bs8[ r16 gs] b4->~ |
          \tuplet 3/2 { b8( cs b) } as8[ r16 fs] a4->~ |
          \tuplet 3/2 { a8( b a) } gs8[ r16 e] g4 |
          \tuplet 3/2 { gs8( a g) } fs8[ d] fs4 |
        }
        \\
        { s4 | s2. | s2 fs'4~ | fs' e' d'->~ | d' cs' s | s2.*4 | }
      >>
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \partial 4
      \key fs \minor
      \time 3/4
      \clef bass
      <<
        \relative c {
          r4 |
          cs,4 <cs' gs' b>8 r <cs es b'>4 |
          fs, <fs' cs'>8 r <fs cs'>4 |
          e, <e' b'>8 r e4~ |
          <a, e'>4 a'8 r <a e'>4 |
          <ds fs>2 <cs es>4 |
          <cs e>2 <c ds>4 |
          <b d>2 <bf cs>4-> |
          <a c>2 <gs b>4 |
        }
        \\
        \relative c' { s4 | s2.*4 | a4 gs2 | g4 fs2 | f4 e2 | es4 d2 | }
      >>
    }
  >>
  \layout { }
  \midi { }
}
```
