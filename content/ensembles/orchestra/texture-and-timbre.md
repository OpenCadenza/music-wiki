<!-- music-kb:page {"id": "page.d8f9ef46a54045deb9e27f3e2e30b023"} -->
<!-- knowledge: ensemble.orchestra.texture-timbre -->
# 管弦织体：从线条到音色结构

检索别名：orchestral texture、doubling、auditory stream、timbral progression、配器、音色交接。

一段旋律可以由一支长笛承担，也可以由几组乐器共同发声。增加乐器时，首先要问听者将听见几条线：加倍可以加固一条线，也可能遮蔽内声部；改变音区、奏法或起音，则可能让同一音高材料被分成不同层次。作曲时应先决定音乐职责，再决定谁来演奏。

## 线条与乐器不是一一对应

VSL 的乐器资料提醒我们同时考虑音区、力度与奏法，而非只检查最低最高音。小提琴多音和弦涉及相邻弦和指法；圆号旧谱还可能采用不同的低音谱号移调规则。把旧谱或缩编谱分配给新乐队时，须先统一实音，再讨论音色。来源：`vsl-violin-technique`，Playing Techniques / Double stops–Quadruple stops；`vsl-horn-notation`，Modern notation / Older notation。

下例是自编的三层缩编，**不是任何历史作品的摘录**。旋律按四分音符运动，支撑层每小节换一次，低音以半音符定位。它的用途是让三个变化速度在代码中可见。选择三件乐器不等于已经完成交响配器。

<!-- opusloom:example
{
  "id": "orchestra.model.three-functional-layers",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["vsl-horn-notation", "vsl-violin-technique"],
  "rights": "OpusLoom original teaching model, CC BY-SA 4.0; no third-party score transcription.",
  "source_locator": "Original four-bar model; institutional technique references support instrumentation checks, not authorship or formal analysis of these notes.",
  "context": "All staves are in concert pitch, including Horn in F; this is a sounding-score study, not extracted transposing parts."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Flute" midiInstrument = "flute" } {
      \time 4/4 c''4\p d'' e'' g'' | f'' e'' d'' c'' |
      e'' g'' f'' d'' | c''2 r2 |
    }
    \new Staff \with { instrumentName = "Horn (concert)" midiInstrument = "french horn" } {
      \time 4/4 e'1\p | f'1 | d'1 | e'2 r2 |
    }
    \new Staff \with { instrumentName = "Cello" midiInstrument = "cello" } {
      \clef bass \time 4/4 c2\p g, | f c | g, b, | c2 r2 |
    }
  >>
  \layout { }
  \midi { \tempo 4 = 84 }
}
```

第一小节的长笛 C5–D5–E5–G5 负责前景，圆号 E4 留作支撑，大提琴 C3–G2 形成低层。第三小节三层同时改变，第四小节又共同缩短到半小节：这个对齐是自编的结束线索，不是由某个音色标签保证的终止。新作若希望内声部成为对话者，就应改变其节奏和动机职责，并检查它是否仍被旋律层覆盖。

这里全部按实音编码。正式生成 F 圆号分谱时应进行明确的记谱移调，而不是只把谱表名改为“F 圆号”。MIDI 的乐器名称只是试听近似，不能验证真实圆号与长笛的音量关系。

## 比较作品时，比较变化的过程

[拉威尔管弦章](../../composers/ravel/examples/orchestral-processes.md)将《波莱罗》的重复层、《达夫尼与克洛埃》的节拍层次、《鹅妈妈》的音程返回并置。这些材料提示不同问题：什么保持辨识度、什么发生变化、变化在哪个段落承担职责。不能从“有持续音型”直接推断三部作品具有同一种曲式。

与之相邻的研究问题是音色本身如何参与分段。Zeller 对勋伯格《色彩》的分析指出，音高目标与音色终止可以不在同一时点；他也区分普通音色对比与具有结构方向的音色进程。这里引用的是作者的解释框架，不把任何换乐器都称为“音色调制”。来源：`zeller-2023-farben`，[3.8–3.9]、[5.5–5.6]、[6.7–6.10]。

下面仅演示**带重叠的角色交接**，不是《色彩》的缩编，也不声称两个小节足以构成该文讨论的音色终止。

<!-- opusloom:example
{
  "id": "orchestra.model.overlapping-timbre-transfer",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["zeller-2023-farben"],
  "rights": "OpusLoom original teaching model, CC BY-SA 4.0; no Schoenberg notes, score images or article examples copied.",
  "source_locator": "Original two-bar study illustrating a general overlap/withdrawal operation; conceptual context: Zeller 2023 [3.8–3.9], [5.5–5.6].",
  "context": "Concert-pitch flute, solo violin and cello; the model shows transfer, not a complete historical timbral cadence."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Flute" midiInstrument = "flute" } {
      \time 4/4 c''1\p~ | c''2 r2 |
    }
    \new Staff \with { instrumentName = "Violin" midiInstrument = "violin" } {
      \time 4/4 r1 | c''1\p |
    }
    \new Staff \with { instrumentName = "Cello" midiInstrument = "cello" } {
      \clef bass \time 4/4 c1\pp~ | c1 |
    }
  >>
  \layout { }
  \midi { \tempo 4 = 60 }
}
```

第二小节前半，长笛与小提琴同奏 C5；后半长笛退出，小提琴继续。大提琴 C3 跨小节延留，因此变化集中在上层发声者和起音，音高集合没有改变。它给出“先重叠、后退出”的操作；听觉上是融合、接力还是断裂，仍取决于力度、奏法、音区、空间及真实演奏。

## 从缩编到完整乐队

| 需要解决的问题 | 写谱时的动作 | 复核证据 |
| --- | --- | --- |
| 前景被遮蔽 | 调整竞争声部的音区、密度、奏法或进入时点 | 逐层读谱，必要时真实音频与演奏反馈 |
| 加倍后失去线条身份 | 标出谁与谁同起音，谁保留独立节奏 | 实音声部图和完整时值，不只数谱表 |
| 打击乐拖过边界 | 为定音鼓写明止音、滚奏和调音计划 | 乐器条件、演奏时间及谱面指令 |
| 换音色却没有方向 | 建立参照音色，规划对比与返回发生的位置 | 跨段比较；不能只看局部乐器表 |

定音鼓的滚奏、止音与踏板条件见 `vsl-timpani-function`，Playing Techniques / Cut-off stroke / Glissando roll。此处提出的逐层写作流程是本库教学建议，不能代替具体作品分析或演奏员核对。

大型乐队的每一件乐器还涉及换气、耐力、弓段、换乐器、乐器数和分谱可读性。编译与 music21 可确认部分时值和音高关系；它们不能裁决融合、穿透力、残响或作品的艺术完成度。

## 查证入口

- [VSL 小提琴](https://www.vsl.co.at/academy/strings/violin)：Playing Techniques，双音与多音和弦。
- [VSL 圆号](https://www.vsl.co.at/academy/brass/horn-f)：Notation，新旧移调约定。
- [VSL 定音鼓](https://www.vsl.co.at/academy/percussion/timpani)：Playing Techniques，滚奏、止音与踏板条件。
- [Zeller，2023，MTO 29.3](https://mtosmt.org/issues/mto.23.29.3/mto.23.29.3.zeller.html)：上文注明的分析段落。许可和完整书目见[来源表](../../knowledge/sources.json)。
