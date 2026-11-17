---
schema_version: 1
collection: horizontal-homophony
kind: form
form_id: ascending-arpeggio
category: texture
topic_name: 向上分解和弦
question: "同样往上走，怎样写出轻巧和内敛？"
title: "向上分解和弦｜同样往上走，怎样写出轻巧和内敛？"
description: "把既定和弦的若干音从低向高错时排开。组首与上行顶点分别落在哪里，决定这组音与旋律怎样交接。"
aliases: ["Ascending arpeggio"]
accent:
  downbeat: "用每组的最低起音标出组首，再看它与小节重拍的关系。"
  emphasis: "旋律的长音或组首可承重，上行顶点也可以只是经过。"
  grouping: "从低起音到该组最高音作为一个单位。"
pattern:
  音高方向: "每组由低到高"
  时值安排: "组内可均分，也可给顶点较长时值"
cases:
  - id: schumann-op18-mm1-8
    question: "怎样把上行音群写得轻巧？"
    composer: 舒曼
    work: "Op.18《阿拉贝斯克》"
    section: "开头"
    measures: { start: 1, end: 8 }
    meter: "2/4"
    tempo:
      marking: "Leicht und zart"
      unit: "1/4"
      bpm: 152
      source: score
    observed_accent: "第 1 小节两拍都从伴奏 G 起组，最高音都出现在拍内。"
    feel: ["轻巧", "连贯"]
    tension:
      level: low
      evidence: "第 1 小节每组前两音是十六分音符，组尾是八分音符，均匀重复的节奏给旋律留下清晰落点。"
    notation:
      format: lilypond
      id: schumann-op18-mm1-8
  - id: brahms-op76no7-mm9-16
    question: "伴奏往上走时，怎样保留旋律的内敛感？"
    composer: 勃拉姆斯
    work: "Op.76 No.7"
    section: "中段开头"
    measures: { start: 9, end: 16 }
    meter: "2/2"
    tempo:
      marking: "Moderato semplice"
      unit: "1/2"
      bpm: 48
      source: playback
    observed_accent: "第 9 小节的两个低起音各开启一组，旋律 C 落在第二组开始处。"
    feel: ["内敛", "忧郁"]
    tension:
      level: medium
      evidence: "第 9 小节连续八分上行，第 10 小节下方音群在小节后半留出空拍。"
    notation:
      format: lilypond
      id: brahms-op76no7-mm9-16
---

<script setup>
import TextureFacts from "../../.vitepress/theme/TextureFacts.vue"
</script>

# 向上分解和弦｜同样往上走，怎样写出轻巧和内敛？

把既定和弦的若干音从低向高错时排开。组首与上行顶点分别落在哪里，决定这组音与旋律怎样交接。

<TextureFacts />

## 向上分解和弦｜怎样把上行音群写得轻巧？

<TextureFacts case-id="schumann-op18-mm1-8" />

第 1 小节第一拍的伴奏 G–C–E 和第二拍的 G–B–F 都用两个十六分音符接一个八分音符。每组由低 G 起，最高音到半拍处才发声。旋律的附点八分音符从拍头就开始，接在后面的十六分音符让两层的节奏可以分别听清。

把自己的上行音群都改成均分试听，再恢复较长的组尾。保持旋律的起音，听两种安排怎样把同一拍交给旋律。

```lilypond title="舒曼 Op.18《阿拉贝斯克》 开头" location="弱起，mm.1–8" id="schumann-op18-mm1-8"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \partial 16*5
      \key c \major
      \time 2/4
      \tempo "Leicht und zart" 4 = 152
      {
        g'16(\pp \acciaccatura b'8 a'8. g'16 |
        c''8. g'16) \acciaccatura b'8 a'8.( g'16 |
        c''8. c''16) cs''8.( cs''16 |
        d''8. d''16) e''8.( e''16 |
        f''8) r16 a'16( \acciaccatura c''8 bf'8. a'16 |
        d''8. a'16) \acciaccatura c''8 bf'8.( a'16 |
        d''8. d''16) e''8.( e''16 |
        f''8. f''16) fs''8.( fs''16 |
        g''8) r16 g'16( \acciaccatura b'8 a'8. g'16) |
      }
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \partial 16*5
      \key c \major
      \time 2/4
      \clef bass
      <<
        {
          r16 g16[ b f'8] |
          g16[ c' e'8] g16[ b f'8] |
          g16[ c' e'8] a16[ cs' e'8] |
          a16[ d' f'8] a16[ cs' g'8] |
          a16[ d' f'8] a16[ cs' e'8] |
          a16[ d' f'8] a16[ cs' e'8] |
          a16[ d' f'8] a16[ cs' g'8] |
          a16[ d' f'8] a16[ d' fs'8] |
          g16[ d' f'8] g16[ b f'8] |
        }
        \\
        {
          s16 d4 |
          c4 d |
          c g |
          f e |
          d g |
          f g |
          f e |
          d c |
          b, d |
        }
      >>
    }
  >>
  \layout { }
  \midi { }
}
```

## 向上分解和弦｜伴奏往上走时，怎样保留旋律的内敛感？

<TextureFacts case-id="brahms-op76no7-mm9-16" />

第 9 小节的两组八分音符各从低音向上爬。第一组以 C–E–A–C 到顶，旋律的 C 则在第二组开始时落下。第 10 小节下方的八分音群只到第三个四分音符的前半，留下的休止让旋律片段继续说下去。

对照舒曼每拍一个短上行组的写法。这里把一个组放进半小节，下一小节又留空。写内敛段落时，可以先延长一组占用的拍数，再试听少填半拍，让旋律的回落显出来。

```lilypond title="勃拉姆斯 Op.76 No.7 中段开头" location="mm.9–16" id="brahms-op76no7-mm9-16"
\version "2.26.0"
\language "english"

\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \set Score.currentBarNumber = #9
      \key a \minor
      \defaultTimeSignature \time 2/2
      \set Score.tempoHideNote = ##t
      \tempo "Moderato semplice" 2 = 48
      <<
        {
          gs'4\p r8 a'8( c''4) r4 |
          r4 r8 e''8~ e'' ds'' e'' c'' |
          gs'4 r8 a'( c''4) r8 fs'' |
          r4 r8 e''8~ e'' ds'' e'' c'' |
          gs'4 r8 <a' e''>8~ <a' e''> ds'' e'' c'' |
          gs'4 r8 <a' e''>8~ <a' e''> ds'' e'' c''~ |
          <af' c'' e''>4\p r8 <g' d'' f''>8~ <g' d'' f''>4 r8 <f' b' ds''>8~ |
          <f' b' ds''>4. <e' c'' e''>8~ <e' c'' e''> ds'' e'' c'' |
        }
        \\
        {
          s2. s8 ds'8~ |
          ds'4. e'8 r2 |
          s1 |
          gs'4. b'8 r2 |
          s1 |
          s1 |
          s1 |
          s1 |
        }
      >>
    }
    \new Staff = "lower" {
      \set Staff.midiInstrument = "acoustic grand"
      % GM 0
      \set Score.currentBarNumber = #9
      \key a \minor
      \defaultTimeSignature \time 2/2
      \clef bass
      {
        c8( e a c') a,( ds fs c') |
        gs,8( b, b gs e) r8 r4 |
        c8( e a c') ds,( a, fs a) |
        e,8( b, b gs e) r8 r4 |
        f,8( c c'~ <a c'~> <f c'>) r8 r4 |
        fs,8( c c'~ <a c'~> <fs c'>) r8 r4 |
        g,8( c c' g) g,( b, b g) |
        c,8( g, g e c4) r |
      }
    }
  >>
  \layout { }
  \midi { }
}
```
