---
schema_version: 1
collection: horizontal-homophony
kind: form
form_id: tremolo
category: texture
topic_name: 震音
question: "怎样让连续交替听起来轻巧或有重量？"
title: "震音｜怎样让连续交替听起来轻巧或有重量？"
description: "这里收录两音或两组音快速交替的写法。组首、力度和旋律时值共同决定交替是持续的底纹，还是明显的推进力。"
aliases: ["Tremolo", "交替震音"]
accent:
  downbeat: "依乐曲拍号确定重拍，在连续交替中用组首或低音变化提示拍位。"
  emphasis: "交替各音可以均匀，也可以突出每组的起点。"
  grouping: "按拍或半小节把交替音划组，另标旋律的起音与延续。"
pattern:
  交替单位: "两个音高或两组音交替"
  细分安排: "等距交替为骨架，可在组首插入休止或改变音区"
cases:
  - id: beethoven-op13-i-mm11-18
    question: "低音八度持续交替时，怎样给快板增加重量？"
    composer: 贝多芬
    work: "Op.13《悲怆》"
    section: "第一乐章"
    measures: { start: 11, end: 18 }
    meter: "2/2"
    tempo:
      marking: "Allegro di molto e con brio"
      unit: "1/2"
      bpm: 160
      source: playback
    observed_accent: "第 11 小节组首落低 C。第 13 小节第二个四分单位的旋律和弦标 sf。"
    feel: ["有重量", "推进"]
    tension:
      level: high
      evidence: "第 11 小节每个二分拍四次低音发音。第 15–16 小节交替持续，组首升高并渐强。"
    notation:
      format: lilypond
      id: beethoven-op13-i-mm11-18
  - id: ravel-m40-i-mm1-8
    question: "快速交替怎样保持轻巧，让旋律浮在上方？"
    composer: 拉威尔
    work: "M.40《小奏鸣曲》"
    section: "第一乐章"
    measures: { start: 1, end: 8 }
    meter: "2/4"
    tempo:
      marking: "Modéré"
      unit: "1/4"
      bpm: 72
      source: playback
    observed_accent: "第 1 小节上方 F♯、C♯ 构成旋律落点，内层组首的休止把起音空间让给旋律。"
    feel: ["轻巧", "浮动"]
    tension:
      level: low
      evidence: "第 1 小节内层以三十二分音符交替，组内有短休止，上方 C♯ 延续过小节线。"
    notation:
      format: lilypond
      id: ravel-m40-i-mm1-8
---

<script setup>
import TextureFacts from "../../.vitepress/theme/TextureFacts.vue"
</script>

# 震音｜怎样让连续交替听起来轻巧或有重量？

这里收录两音或两组音快速交替的写法。组首、力度和旋律时值共同决定交替是持续的底纹，还是明显的推进力。

<TextureFacts />

## 震音｜低音八度持续交替时，怎样给快板增加重量？

<TextureFacts case-id="beethoven-op13-i-mm11-18" />

第 11 小节下方 C 的两个八度交替，每个二分拍有四个八分音符。上方 C 保持到第四个四分音符单位才换音。第 13 小节的 sf 在同一连续脉冲上格外显眼。第 15–16 小节下方每半小节换一次组首，细分速度维持原样。

写推进段时，先让交替保持均匀，再只改一个组首的位置或一次旋律重音。听落脚是否仍然清楚。

```lilypond title="贝多芬 Op.13《悲怆》 第一乐章" location="mm.11–18" id="beethoven-op13-i-mm11-18"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \set Score.currentBarNumber = #11
      \key c \minor
      \defaultTimeSignature \time 2/2
      \set Score.tempoHideNote = ##t
      \tempo "Allegro di molto e con brio" 2 = 160
      {
        c'2.\p <bf e'>4-. |
        <af f'>4-. <e' g'>-. <f' af'>-. <d' b'>-. |
        <ef' c''>4-. <e' c''>2\sf <bf' e''>4-. |
        <af' f''>4-. <e'' g''>-. <f'' af''>-. <d'' b''>-. |
        <c'' ef'' g'' c'''>2-.\< <g' b' f'' g''>-. |
        <g' c'' ef''>2-. <f' af' d''>-. |
        << { g'2 fs' } \\ { <ef' c''>1~ } >> |
        <ef' a' c''>2 <d' f' b'>\! |
      }
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \set Score.currentBarNumber = #11
      \key c \minor
      \defaultTimeSignature \time 2/2
      \clef bass
      {
        \repeat unfold 4 { c,8 c c, c c, c c, c | }
        c,8 c c, c d, d d, d |
        ef, ef ef, ef f, f f, f |
        g, g g, g af, af af, af |
        fs, fs fs, fs g, g g, g |
      }
    }
  >>
  \layout { }
  \midi { }
}
```

## 震音｜快速交替怎样保持轻巧，让旋律浮在上方？

<TextureFacts case-id="ravel-m40-i-mm1-8" />

第 1 小节先听上方 F♯ 接 C♯，再听 C♯ 下方的 E–G♯ 交替。三十二分音符很密，但组间的三十二分休止给它留出间隙。C♯ 持续过小节线，上方旋律因此保持自己的速度。

先唱旋律，再加内层，最后只删去内层组间的休止试听。与《悲怆》比较时，分别听旋律的时值、交替音的音区和连续程度。

```lilypond title="拉威尔 M.40《小奏鸣曲》 第一乐章" location="mm.1–8" id="ravel-m40-i-mm1-8"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \key fs \minor
      \time 2/4
      \set Score.tempoHideNote = ##t
      \tempo "Modéré" 4 = 72
      <<
        {
          r8 fs''8(\p^\markup \italic "doux et expressif" cs''4~ |
          cs''8 b'16 cs'' d''8 e''16 fs'' |
          gs''8 e'' gs''16) r16 fs''8(->\pp^\markup \italic "subito" |
          cs''4~ cs''8 b'16 cs'' |
          d''8 e''16 fs'' gs''8) fs''(\mf |
          cs'''4~ cs'''16 cs''' d''' e''' |
          cs'''8 b''16 gs'' fs''8 a'') |
          cs'''4~ cs'''16 cs''' d''' e''' |
        }
        \\
        {
          s8 r32 a' cs'' a' r e' gs' e' r e' gs' e' |
          r32 e' gs' e' b' d' cs'' d' r fs' a' fs' e'' gs' fs'' gs' |
          r32 a' cs'' a' r a' cs'' a'
          \tuplet 3/2 { r16 a'16 cs''32 r32 } r32 a' cs'' a' |
          r32 e' gs' e' r e' gs' e' r e' gs' e' b' d' cs'' d' |
          r32 fs' a' fs' e'' gs' fs'' gs' r a' cs'' a' r a' cs'' a' |
          r32 cs'' gs'' cs'' r cs'' gs'' cs'' r cs'' gs'' cs'' g'' e'' g'' e'' |
          r32 cs'' fs'' cs'' e'' b' gs'' b' r fs' cs'' fs' r a' e'' a' |
          r32 cs'' gs'' cs'' r cs'' gs'' cs'' r cs'' gs'' cs'' g'' e'' g'' e'' |
        }
      >>
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \key fs \minor
      \time 2/4
      \clef treble
      <<
        {
          r8 cs''16 r gs' r gs' r |
          gs'16 r fs' r a' r b' r |
          cs''16 r cs'' r cs'' r cs'' r |
          gs'16 r gs' r gs' r fs' r |
          a'16 r b' r cs'' r cs'' r |
          <as' e''>8 as' e'' as' |
          d''8-. d''-. <b ds' a'> <d' fs' c''> |
          <as' e''>8 as' e'' as' |
        }
        \\
        {
          s8 fs'8( cs'4~ |
          cs'8 b16 cs' d'8 e'16 fs' |
          gs'8 e' gs'16) r16 fs'8-> |
          cs'4~ cs'8 b16 cs' |
          d'8 e'16 fs' gs'8 fs' |
          fs'2 |
          <e' gs'>4 s4 |
          fs'2 |
        }
      >>
    }
  >>
  \layout { }
  \midi { }
}
```
