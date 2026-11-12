---
schema_version: 1
collection: horizontal-homophony
kind: form
form_id: polka
category: dance
topic_name: 波尔卡
question: "怎样用两拍的分工写出落脚和回弹？"
title: "波尔卡｜怎样用两拍的分工写出落脚和回弹？"
description: "波尔卡以二拍组织舞步。短音、休止与下一拍的发音位置共同决定步子如何弹起。"
aliases: ["Polka"]
accent:
  downbeat_beat: 1
  typical_meters: ["2/4"]
  downbeat: "第一拍建立每小节的落脚。"
  emphasis: "第二拍或拍内的短音可把动作带到下一小节。"
  grouping: "按二拍计数，听前后两拍的时值与动作如何互补。"
pattern:
  舞步节拍: "二拍"
  伴奏拍型: "低音可作落脚，较短的回音可由同层或另一层承担"
cases:
  - id: smetana-jb107-2-mm1-8
    question: "怎样用两拍的分工写出落脚和回弹？"
    composer: 斯美塔那
    work: "《捷克舞曲》第一集"
    section: "第 2 首"
    measures: { start: 1, end: 8 }
    meter: "2/4"
    tempo:
      marking: "Moderato"
      unit: "1/4"
      bpm: 80
      source: score
    observed_accent: "第 1、3、5 小节首拍落低 A，旋律在半拍后进入。"
    feel: ["轻快", "弹跳"]
    tension:
      level: medium
      evidence: "第 1–2 小节在短低音、十六分音符和长和弦之间交换发音任务。"
    notation:
      format: lilypond
      id: smetana-jb107-2-mm1-8
---

<script setup>
import TextureFacts from "../../.vitepress/theme/TextureFacts.vue"
</script>

# 波尔卡｜怎样用两拍的分工写出落脚和回弹？

波尔卡以二拍组织舞步。短音、休止与下一拍的发音位置共同决定步子如何弹起。

<TextureFacts />

## 谱例

<TextureFacts case-id="smetana-jb107-2-mm1-8" />

第 1 小节第一拍先落短低音 A，旋律在半拍后用 E–F 两个十六分音符进入，第二拍继续到 E–A。第 2 小节上方换成长和弦，下方从第一拍后半接过短音群。把这两小节连着数「一、二」，两种写法都有落脚，也都有向前的回弹。

试听时先只拍第一拍，再加上短音群。若每个短音都像重新落脚，先把两颗十六分音符唱成一组。

```lilypond title="斯美塔那 《捷克舞曲》第一集 第 2 首" location="mm.1–8" id="smetana-jb107-2-mm1-8"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \key a \minor
      \time 2/4
      \tempo "Moderato" 4 = 80
      <<
        {
          r8 e'16(\p f' e'8-.) a'-. |
          <d' e' gs' b'>2-- |
          r8 e'16( f' e'8-.) a'-. |
          <d' e' gs' b'>8.( c''16 b'4) |
          r8 e'16( f' e'8-.) a'-. |
          <bf e' g'>2-- |
          r8 c'16( d' c'8-.) f'-. |
          <g c' e'>4.-- <gs d'>8-. |
        }
        \\
        {
          s8 <a c'>4( <c' e'>8-.) |
          s2 |
          s8 <a c'>4( <c' e'>8-.) |
          s2 |
          s8 <a c'>4( <c' e'>8-.) |
          s2 |
          s8 <f a c'>4( <g b>8-.) |
          s2 |
        }
      >>
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \key a \minor
      \time 2/4
      \clef bass
      {
        a,8-. r r4 |
        r8 e16( f e8-.) e,-. |
        a,-. r r4 |
        r8 ds16( e \acciaccatura g8 f8 e16 e,) |
        a,8-. r r4 |
        r8 b,16( c \acciaccatura ef8 df8 c-.) |
        f,4.( d,8-.) |
        r8 c,16( d, c,8) b,,-. |
      }
    }
  >>
  \layout { }
  \midi { }
}
```
