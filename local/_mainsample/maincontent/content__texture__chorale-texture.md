---
schema_version: 1
collection: horizontal-homophony
kind: form
form_id: chorale-texture
category: texture
topic_name: 圣咏式和弦织体
question: "怎样用同起和延续写出平实的步态？"
title: "圣咏式和弦织体｜怎样用同起和延续写出平实的步态？"
description: "旋律与和弦在关键拍位一起发声，形成清楚的垂直落点。支撑音可以继续保持，也可以在下一个拍点更新。"
aliases: ["Chorale texture", "圣咏式"]
accent:
  downbeat: "小节重拍由节拍确定，乐句的支点常通过若干音同起而显现。"
  emphasis: "用共同起音与延长音组织重心，个别拍可用书面重音凸显。"
  grouping: "先划出一拍或一句的共同落点，再标出各音的延续。"
pattern:
  发音方式: "骨架音在关键拍同起"
  延续方式: "支撑音可跨越旋律的细分"
cases:
  - id: schumann-op18-minore-i-mm41-48
    question: "怎样用同起和延续写出平实的步态？"
    composer: 舒曼
    work: "Op.18《阿拉贝斯克》"
    section: "Minore I"
    measures: { start: 41, end: 48 }
    meter: "2/4"
    tempo:
      marking: "Etwas langsamer"
      unit: "1/4"
      bpm: 112
      source: playback
    observed_accent: "Minore I 开头两小节成组，后一小节第一拍标重音。"
    feel: ["平实", "连贯"]
    tension:
      level: medium
      evidence: "第 41 小节的四个旋律八分音符走过两个四分支撑音，第 42 小节的支撑在第二拍留空。"
    notation:
      format: lilypond
      id: schumann-op18-minore-i-mm41-48
---

<script setup>
import TextureFacts from "../../.vitepress/theme/TextureFacts.vue"
</script>

# 圣咏式和弦织体｜怎样用同起和延续写出平实的步态？

旋律与和弦在关键拍位一起发声，形成清楚的垂直落点。支撑音可以继续保持，也可以在下一个拍点更新。

<TextureFacts />

## 谱例

<TextureFacts case-id="schumann-op18-minore-i-mm41-48" />

第 41 小节上方 B 与支撑音 G、低 E 同起。随后上方继续四个八分音符，支撑音按四分音符推进。第 42 小节第一拍用带重音的 G 标出下一处共同落点，第二拍的支撑声部休止，让八分音符继续走完。这里的圣咏式听感来自有秩序的共同起音与延续。

练习时先用同长音符写出共同落点，再给旋律恢复原来的细分。比较两次的重心是否一样清楚。

```lilypond title="舒曼 Op.18《阿拉贝斯克》 Minore I" location="mm.41–48" id="schumann-op18-minore-i-mm41-48"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \set Score.currentBarNumber = #41
      \key e \minor
      \time 2/4
      \set Score.tempoHideNote = ##t
      \tempo "Etwas langsamer" 4 = 112
      <<
        \relative c'' {
          b8(\mf c b fs' | g-> e d! c) |
          b( c b fs' | g-> e d! c) |
          b( c b f'! | e-> c b a) |
          a( b g! a | b-> fs e ds) |
        }
        \\
        \relative c' {
          g'4 a | b r | g a | b r |
          g gs | a r | e e | ds r |
        }
      >>
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \set Score.currentBarNumber = #41
      \key e \minor
      \time 2/4
      \clef bass
      <<
        \relative c' {
          b8( c b fs' | <b, g'>8->\arpeggio e d! c) |
          b( c b fs' | <b, g'>8->\arpeggio e d! c) |
          b( c b f'! | e-> c b a) |
          a( b g! a | b-> fs e ds) |
        }
        \\
        \relative c {
          e4\< ds | e\! r | e\< ds | e\! r |
          e\< d | c\! r | c c | b r |
        }
      >>
    }
  >>
  \layout { }
  \midi { }
}
```
