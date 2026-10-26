<!-- music-kb:page {"id": "page.1c707dbdf3ff4c079312386bf5d170f1"} -->
<!-- knowledge: style.popular-song-form-groove -->
# 流行歌曲曲式与 groove：从段落功能到节奏骨架

检索别名：popular song form、Tin Pan Alley、AABA、ABAC、verse-chorus、refrain、SRDC、groove、backbeat、swing、syncopation、歌曲创作。

## 问题和范围

流行歌曲里的“verse”“chorus”“bridge”“refrain”可能处于不同层级。一个短句可以在 section 内重复，也可以是一整个 section；把标签贴在段落上之前，必须先写出边界、重复单位、终止位置和谁承担标题或主要意念。本文覆盖二十世纪美国 Tin Pan Alley、Great American Songbook、早期Beatles、以backbeat为核心的groove，以及部分千禧年后流行/EDM研究。它不是全球流行音乐的分类总表。

Open Music Theory 把三十二小节 AABA 描述为 earlier Golden Age repertoire 中的常见历史形态：四个八小节单位，A 承载主要材料并常延长 tonic，B以对比材料建立回到A的期待。来源：`hughes-lavengood-aaba-strophic`，“32-Bar Song Form (AABA)”与“Sections of AABA and Strophic Forms”。“常见”不等于“规范”，更不等于每首歌曲必须属于它。

## A 的四个内部功能

Nobile 把早期 Beatles 的常见模型称为 SRDC-B：A 内先 statement，再 restatement，然后 departure，最后由 conclusion 完成 cadence；B 是 bridge，通常 off-tonic 开始并以 dominant retransition 导向 A。SRDC 描述 A 的内部功能，AABA 描述更大层级，二者不能混写。来源：`nobile-2011-beatles-form`，§§1.1–1.3、§2。

下例是八小节 A 的自编和声与旋律模型，用 C 大调显示两次 tonic 陈述、离开和返回。它不复制 Beatles 或其他歌曲。

<!-- opusloom:example
{
  "id": "popular.model.srdc-eight-bar-a",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["nobile-2011-beatles-form", "hughes-lavengood-aaba-strophic", "callahan-2013-songbook", "project-workflow"],
  "rights": "OpusLoom original teaching model, CC BY-SA 4.0; no existing melody, lyric, chord chart, or score excerpt reproduced.",
  "source_locator": "Original eight-bar SRDC model; conceptual locations: Nobile 2011 §§1.1-2.2; Hughes and Lavengood, '32-Bar Song Form (AABA)'; Callahan 2013 §§1.1-2.5.",
  "context": "Concert-pitch original melody, harmonic reduction, and bass. Bars 1-4 are S+R; bars 5-6 depart; bars 7-8 conclude."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Original lead" } {
      \clef treble
      \time 4/4
      \key c \major
      e''4 d'' c'' b'
      a'2 g'2
      e''4 d'' c'' b'
      a'2 g'2
      f''4 e'' d'' c''
      b'1
      c''2 e''2
      c''1
    }
    \new Staff \with { instrumentName = "Harmonic guide" } {
      \clef treble
      \time 4/4
      \key c \major
      <d' f' a' c''>2 <g' b' d'' f''>2
      <c' e' g' b'>1
      <d' f' a' c''>2 <g' b' d'' f''>2
      <c' e' g' b'>1
      <f' a' c'' e''>1
      <g' b' d'' f''>1
      <c' e' g' b'>1
      <c' e' g' b'>1
    }
    \new Staff \with { instrumentName = "Bass" } {
      \clef bass
      \time 4/4
      \key c \major
      d,2 g,2
      c,1
      d,2 g,2
      c,1
      f,1
      g,1
      c,1
      c,1
    }
  >>
  \layout { }
  \midi { \tempo 4 = 96 }
}
```

第 1–2 与第 3–4 小节反复 Dm7–G7–Cmaj7，构成两个 basic statements 的展示。第 5 小节由 Fmaj7 离开 tonic，第 6 小节到 G7 时形成 departure 的未完成感。第 7 小节回到 C，第 8 小节留在 C 完成 conclusion。旋律的 A4–G4、第5小节F5–E5–D5–C5的级进、低音的 D2–G2–C2，以及从第 5 小节开始上移到 F2，给同一和声骨架增加可辨认的局部形状。

这个八小节只是一个 A。三十二小节 AABA 的判断还必须看到第二个 A 的重复、B 的 off-tonic 开始与 retransition、末 A 的回返；四个小节的 G7 或一份主歌谱面不足以证明全曲结构。

## 比较作品时先对齐分析层级

Nobile 的《From Me to You》例子在 A 内呈现 SRDC，整曲又形成 AABAABA。bridge 从 IV 出发，并通过对 V 的 tonicization 准备回返。不能把“bridge 的 IV–V”与“整曲三十二小节”混成一个结论。来源：`nobile-2011-beatles-form`，§§1.2–1.3。

《Misery》的 verse 在 S、R 中延长 tonic，D 引入 IV–V，C 完成回 I，形成上行或邻音式的不同 upper-voice path。《A Hard Day's Night》同样有 tonic prolongation 与 IV–V，但 upper voice 形成上升到 tonic 的路径。《I'll Cry Instead》则把 C 提前，让 `V–I` 发生在 C 内；先出现的 tonic 被 Nobile 解释为 prolong dominant 的 cadential I。三首作品共有 AABA/SRDC 的期待，却用不同的终止时点与上层线条实现它。来源：`nobile-2011-beatles-form`，§§2.1–3.3。

《Eight Days a Week》进一步显示，同一种 IV 可以因为所处位置不同而承担 pre-dominant 或 cadential function。Nobile 把 C 内的 IV–I 解释为整个 verse 的终止；若只按“IV 就是 pre-dominant”套用 roman-numeral 规则，就会忽略段内位置。来源：`nobile-2011-beatles-form`，§§4.2–4.3。

Songbook 的词也参与句法。Callahan 以 207 首歌曲为语料，把 sentence 的音乐 presentation–continuation–cadence 与歌词的重复、加速、收束并置；《You Took Advantage of Me》中的 list 在第 5–6 小节碎片化，并在 7–8 小节以标题式 reveal 与 perfect authentic cadence 同步完成，而《They Can't Take That Away from Me》的词与乐曲的强弱关系、错位与补偿更复杂。来源：`callahan-2013-songbook`，§§1.1–1.2、§§2.1–3.5。这说明分析时至少要看音乐终止、歌词句法和标题落点是否一致。

## Refrain 与 chorus 是功能判断

Open Music Theory 把 refrain 界定为 section 内反复、歌词基本不变的短句；它不一定达到独立 chorus 的尺度。Carter 则把 blues 末尾持续多小节的反复材料解释为 prolonged refrain。两者使用同一词的不同尺度，不能用单一定义强迫作品服从。来源：`hughes-lavengood-aaba-strophic`，“Refrains”；`carter-2025-beyond-strophic`，§§2.1–2.2。

Carter 的《She Moves Me》把 4+8 模型构成十二小节：前四小节的 wordy quatrain 与 stop time 让 verse 感更明显，后八小节的 prolonged refrain 歌词较稀、内部重复更强，使 chorus quality 上升。《Live So Easy》与《Downhearted Blues》可帮助比较不同词汇密度、phrase rhythm 与文本重复怎样改变段落感。这里的腔词语气、发音与演奏细节来自作者对录音的分析，不能被一个只能保存音符的 MIDI 文件证明。来源：`carter-2025-beyond-strophic`，§§2.2–2.4。

## 千禧年后的流行：和弦循环之外的方向

Nobile在《Let’s Get It Started》（2004）的分析中，讨论同一i–♭III–♭VI–V循环怎样容纳rap、歌唱和伴奏织体的变化；“启动—积累—抵达”可由这些参数承担，而非每段必须换一套和弦。他同时把这个框架限定在所研究的曲式语境，没有把所有副歌都规定为同一种抵达。来源：`nobile-2022-teleology`，[1.1–1.2]、[3.9]。

《Roar》（2013）提供另一层区别。Stroud将其中副歌达到高潮之后的材料讨论为codetta型后副歌；她另区分在后副歌本身才获得高潮的anthem型。后副歌的判断因此涉及位置、闭合与高潮分配，不是见到副歌后还有几小节就贴标签。来源：`stroud-2022-postchorus`，[0.1]、[1.1–1.3]。

| 结构参数 | 研究提供的观察框架 | 写谱与编配时可记录什么 |
| --- | --- | --- |
| 鼓型 | Geary用层数、节奏、乐器配置比较2012–2021年特定流行语料 | kick、snare、hat各层何时出现/退出，边界前后有什么变化 |
| 连续过程 | Smith区分离散节奏加密与连续音高、力度、滤波变化，讨论特定2010年代EDM | 哪项连续变化指向drop，哪项只是局部装饰；对应的制作记录放在哪里 |
| 高潮位置 | Nobile、Stroud区分段落的积累、抵达和闭合职责 | 抵达在副歌开始、段内还是后副歌；是否故意削弱预期 |

上表是有范围的分析工具。作为本库教学建议，可以给每段同时列和声循环、鼓层、音区与力度，再写出哪一项保持、哪一项改变。下文模型只演示记谱的节奏骨架；滤波、声音包络和真实制作音色需要另有制作说明或自动化数据，不能声称几个音符已重建原录音。来源：`geary-2024-drum-form`，[1.2–1.3]；`smith-2021-continuous-edm`，[1.2–1.4]、[3.8–3.11]。

## Groove 同时由模式与时间构成

基础 swing 骨架可以写作：ride cymbal 的 `ding-ding-a-ding`、hi-hat 在第 2 与第 4 拍的短促 backbeat、walking bass 四分音符。背拍固定“重心”在 2、4，实际演奏却可以在拍点附近提前或延后。Butterfield 把这种几十毫秒的差异称为 participatory discrepancies，并指出 on-top 更容易产生 forward drive，behind-the-beat 更容易产生 laid-back 感。来源：`butterfield-2006-anacrusis`，§§2、§§17–22、§§32–37。

下例只把节奏骨架写到谱面。它是自编模型，重点是让 downbeat、backbeat、offbeat comping 与低音关系可核对；它不声称正确重现 swing ratio 或某一乐队的 feel。

<!-- opusloom:example
{
  "id": "popular.model.groove-skeleton",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["lavengood-swing-rhythms", "butterfield-2006-anacrusis", "cohn-2016-funky-rhythms", "project-workflow"],
  "rights": "OpusLoom original teaching model, CC BY-SA 4.0; no third-party rhythm transcription, audio, or score excerpt reproduced.",
  "source_locator": "Original four-bar groove skeleton; conceptual locations: Lavengood, 'The Basic Swing Groove' and 'Syncopation'; Butterfield 2006 §§17-22 and 32-37; Cohn 2016 §1.1.",
  "context": "Notation-level role study. Straight MIDI playback is not evidence of swing, microtiming, timbre, articulation, or ensemble balance."
}
-->
```lilypond
\version "2.26.0"
\score {
  <<
    \new Staff \with { instrumentName = "Comp" } {
      \clef treble
      \time 4/4
      \key c \major
      r8 <e' g' b'>8 r4 <e' g' b'>4 r4
      r8 <e' g' b'>8 r4 <e' g' b'>4 r4
      r8 <e' g' b'>8 r4 <e' g' b'>4 r4
      r8 <e' g' b'>8 r4 <e' g' b'>2
    }
    \new Staff \with { instrumentName = "Bass" } {
      \clef bass
      \time 4/4
      \key c \major
      c,4 g, c'2
      a,,4 g, c'2
      f,4 g, c'2
      c,4 g, c'2
    }
    \new DrumStaff \with { instrumentName = "Drums" } {
      \time 4/4
      \drummode {
        <<
          { cymr8 cymr cymr cymr cymr cymr cymr cymr }
          \\
          { r4 hhp4 r4 hhp4 }
        >>
        <<
          { cymr8 cymr cymr cymr cymr cymr cymr cymr }
          \\
          { r4 hhp4 r4 hhp4 }
        >>
        <<
          { cymr8 cymr cymr cymr cymr cymr cymr cymr }
          \\
          { r4 hhp4 r4 hhp4 }
        >>
        <<
          { cymr8 cymr cymr cymr cymr cymr cymr cymr }
          \\
          { r4 hhp4 r4 hhp4 }
        >>
      }
    }
  >>
  \layout { }
  \midi { \tempo 4 = 112 }
}
```

鼓谱把 ride 八分音符与脚踏hi-hat的第2、4拍分开；低音每小节以 C2、G2、C3、A1、F2 等落点形成循环；guitar在第1拍后半与第3拍发声，形成弱拍推进。代码中的 eighth notes 等值排布只是骨架，编译器不会自动演奏 swing，也不会产生“in the pocket”的时间偏移。试听 \midi 输出若接近机械等分，恰恰说明不能把编译成功当作 groove 证明。

《It Don't Mean a Thing》显示鼓/低音之外的层次。Cohn 对 1932 录音的分析中，bass 与 hocketing chords 支持快速 duple frame，Anderson 唱过标题后，brass 用八组 short-long `doo-wah` 回应。短长关系、plunger timbre 与结尾的 relock 共同塑造推进，所以 tenor 或 bass 的单独音高不能解释整个 groove。来源：`cohn-2016-funky-rhythms`，§§1.1–1.10。

《Chameleon》则把 rock/funk 低音与背拍放到统计证据中。Butterfield 测量录音：开场 bass 的 syncopated backbeat 多数约晚 12–13 ms；主 groove 与后段 reprise 中 bass、snare 的 backbeat 也倾向 behind the beat。这个时间差和记谱位置是两类证据。来源：`butterfield-2006-anacrusis`，§§40–52。

## 创作迁移的操作顺序

1. 先写 section map：intro、sectional verse、A、B、chorus、refrain、solo、outro 各自的开始和结束，而非先选 AABA。
2. 在 A 内标出 statement、restatement、departure、conclusion；检查旋律、和声和歌词是否在同一位置完成变化。
3. 写 B 的离开材料与 retransition。如果 B 以 dominant 结束，却同时完成完整终止，回返功能会改变。
4. 为 refrain/chorus 写出重复单位。标题落点、文本密度、音区和 texture 变化要进入结构判断。
5. 先做没有 swing 标记的 rhythm grid，再决定哪些声部强化 downbeat、backbeat 与 offbeat。记谱只能固定骨架。
6. 在录音中比较 attack、accent、tie、rest、乐手之间的 timing 和音色。制作层面的 EQ 与 reverb、压缩，以及人声近距离感，分别登记为编曲或录音证据。
7. 将每个段落放回全曲。一次 verse 的短语不能自动证明整曲 chorus function。

## 反例与局限

- AABA 不必恰好三十二小节；A 也可被重叠、扩写或只出现一部分。
- 同一 IV 可因段内位置成为 pre-dominant 或 cadence 的一部分。
- Refrain 不等同于主副歌总体结构中的独立 section；chorus 或 bridge 的语义常随分析框架改变。
- 一个 swing ratio 无法描述摇摆。快速度可更平均，但 accent、articulation、ride pattern 与 ensemble timing 仍参与组成。
- 此处由记谱生成的MIDI不证明真实拨弦/刷奏起音、乐手时序、厅堂音色或现场平衡；带精细时间戳的演奏MIDI另需具体分析。谱面与音频证据必须分开。
- Carter 的 blues corpus 与本文的早期 Beatles/Songbook 例子分属不同 repertoires；比较机制，不把统计频率外推成普遍歌曲规则。
- 当前没有获准使用的原作歌词或整段旋律谱。所有作品级分析只概述来源，不重制原文。

主要来源：`hughes-lavengood-aaba-strophic`；`nobile-2011-beatles-form`；`callahan-2013-songbook`；`carter-2025-beyond-strophic`；`lavengood-swing-rhythms`；`butterfield-2006-anacrusis`；`cohn-2016-funky-rhythms`。

查证与许可：[来源表](../../knowledge/sources.json)；[Nobile 2022](https://mtosmt.org/issues/mto.22.28.3/mto.22.28.3.nobile.html)、[Stroud 2022](https://www.mtosmt.org/issues/mto.22.28.2/mto.22.28.2.stroud.html)、[Geary 2024](https://mtosmt.org/issues/mto.24.30.2/mto.24.30.2.geary.html)、[Smith 2021](https://mtosmt.org/issues/mto.21.27.2/mto.21.27.2.smith.html)。
