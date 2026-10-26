<!-- music-kb:page {"id": "page.e5a3a9b6abb8414187f1d1ef0f18f884"} -->
<!-- knowledge: style.jazz-harmony-guide-tones-blues -->
# 爵士和声导航：ii–V–I、导向声部与布鲁斯结构

检索别名：jazz harmony、ii–V–I、guide tones、tritone substitution、十二小节布鲁斯、jazz blues、爵士布鲁斯、voice leading。

## 问题和范围

爵士和声不是一个把七和弦连成列表的词汇表。演奏者要同时判断局部目标、低音路径、三音与七音怎样连接、和弦在乐句中的稳定程度，以及这些选择怎样经过多个 chorus。本文以重视七和弦与 chorus 循环的 tonal jazz、blues 和 standard 为主要范围。Modal jazz、free jazz、器乐 timbre 与录音混音需要各自的问题框，不能由本文的和弦语法代替。

ii–V–I 常写作 Dm7–G7–Cmaj7。ii 与 V 不一定是两个同等独立的目的地；McClimon 将它们视作 tonal jazz 中可组合的语法单位，同时说明该模型先描述和弦层面，不自动决定旋律、voicing、即兴或全曲结构。来源：`mcclimon-2017-ii-v-space`，Introduction §§0.1–0.9、§1；`smither-2019-guide-tone-space`，§§0.1–1.6。

## 一个目标和三条检查线

把 Dm7–G7–Cmaj7 配置低音与两条导向声部时，根音给出 `D–G–C`，低音跳进明显；三音与七音则常常提供更小的动作。Dm7 的 F、C 到 G7 的 F、B 时，F 保持，C 下滑半音到 B；G7 的 F、B 到 Cmaj7 的 E、B 时，B 保持，F 下滑到 E。这个局部规律可以支持伴奏、line writing 和即兴中的骨架，却不要求每个实演都只用两个音。

教学模型如下。它不含《All the Things You Are》《Tune Up》或《Nefertiti》的旋律，也不是任一首作品的转写。

<!-- opusloom:example
{
  "id": "jazz.model.guide-tone-ii-v-i",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["mcclimon-2017-ii-v-space", "smither-2019-guide-tone-space", "project-workflow"],
  "rights": "OpusLoom original teaching model, CC BY-SA 4.0; no third-party melody, chord chart, or score excerpt reproduced.",
  "source_locator": "Original four-bar model; conceptual locations: McClimon 2017 §§1.1 and 2.1-2.2; Smither 2019 §§1.1-1.3.",
  "context": "Concert-pitch bass and guide-tone dyads in C major. Bars 1-3 state one ii-V-I; bar 4 returns to V as a study turnaround."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Guide tones" } {
      \clef treble
      \time 4/4
      \key c \major
      <f' c''>1\p
      <f' b'>1
      <e' b'>1
      <f' b'>1\fermata
    }
    \new Staff \with { instrumentName = "Bass" } {
      \clef bass
      \time 4/4
      \key c \major
      d1\p
      g,1
      c1
      g,1
    }
  >>
  \layout { }
  \midi { \tempo 4 = 92 }
}
```

第一小节 Dm7 的 F4 与 C5 分别是三音和七音；第二小节 G7 的 F4 与 B4 仍是七音和三音。C5 到 B4 的半音下降和共同音 F4 让和声改变而声部不必同时跳动。第三小节 Cmaj7 的 E4 与 B4 中，B4 保持，F4 到 E4；第四小节 G7 又让 E4 到 F4，并把 B4 维持为共同音。低音 D3–G2–C3 按五度关系连接，实际低音先下降五度、再上行四度，末小节 C3–G2 下跳同样提供返回下一循环的方向。

这些骨架音并不等于完整伴奏。钢琴可以省略五音、加入 tension 或在弱拍补充节奏；bassist 可能使用经过音和 anticipations；horn player 也可能绕开 guide tone。模型的用途是先确定一个可听见的干声骨架，再判断其他层是在强化它、遮蔽它或重新解释它。

替代和弦须分开检查两件事。G7 换成 D♭7 时，仍是 C 大调的 dominant-function 出发点，但低音的 G–C 下降五度变成 D♭–C 半音。Smither 指出，tritone substitute 往往保留部分三音与七音的平滑连接；McClimon 也把“功能和声”和“根音路径”分开。来源：`smither-2019-guide-tone-space`，§1.3；`mcclimon-2017-ii-v-space`，§§2.1–2.5。

## 多作品比较不是同一张和弦表换名字

《All the Things You Are》的 bridge 只能在具体段落中比较。McClimon 对同一段和弦给出至少三种可并行使用的读法：按 chord tones、按 guide-tone 线、按局部调中心拆成 ii–V 单元。三种读法回答的问题不同，不能因为都能描述这段和声就任选一项当成唯一结构。来源：`mcclimon-2017-ii-v-space`，Introduction §0.1 和 Figure 1。

《Tune Up》十六小节含多个不同调的 ii–V–I。Smither 用连续的三音、七音连接说明，一个目标接一个目标可以在调中心变化中形成平滑路径。这里的“平顺”是局部声部连接，不代表全曲只有一个不动的调。来源：`smither-2019-guide-tone-space`，§§0.1–0.2 和 Examples 1–2。

《Nefertiti》进一步限制结论。Smither 报告其和弦中多数 guide-tone 转换较平滑，但仍有不合该局部规律的一步；此现象帮助连接一段和声，却不能证明作品具有稳定的传统调性中心。来源：`smither-2019-guide-tone-space`，§§2.12–2.14。分析 postbop 时，先记录哪些连接可被 guide-tone 语法解释，再说明哪些结构问题仍在模型之外。

## 布鲁斯是一种可变的 schema

基本十二小节布鲁斯常写成四小节 I、两小节 IV 后回 I、末四小节 V–IV–I–I。Hughes 与 Lavengood 强调 tonic 与 subdominant 都可出现 dominant-seventh quality，plagal motion 与大小三度并置使功能语言需要调整。十六小节、minor blues 和 jazz blues 是同一 big-pattern 的变体，不是“标准十二小节”的失败版本。来源：`hughes-lavengood-blues-harmony`，“12-Bar Blues”“Voice leading”“More Blues Schemas”“Jazz Blues”。

下例是 F 的自编和声模型，使用 tonic 与 subdominant 的 dominant-seventh quality，并保留 turnaround。它不复制任何 blues 旋律或现有 chord chart。

<!-- opusloom:example
{
  "id": "jazz.model.f-blues-shells",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["hughes-lavengood-blues-harmony", "mcclimon-2017-ii-v-space", "project-workflow"],
  "rights": "OpusLoom original teaching model, CC BY-SA 4.0; no melody, lyrics, published chart, or score excerpt reproduced.",
  "source_locator": "Original twelve-bar teaching progression; conceptual locations: Hughes and Lavengood, '12-Bar Blues' and 'Jazz Blues'; McClimon 2017 §3.9.",
  "context": "Concert-pitch two-staff model in F: dominant-quality tonic and subdominant shells over a twelve-bar root pattern with a V-IV-I-V turnaround."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Comping shells" } {
      \clef treble
      \time 4/4
      \key f \major
      <a' ees''>1\mf
      <a' ees''>1
      <a' ees''>1
      <a' ees''>1
      <d'' aes''>1
      <d'' aes''>1
      <a' ees''>1
      <a' ees''>1
      <e' bes'>1
      <d'' aes''>1
      <a' ees''>1
      <e' bes'>1
    }
    \new Staff \with { instrumentName = "Bass roots" } {
      \clef bass
      \time 4/4
      \key f \major
      f,1\mf
      f,1
      f,1
      f,1
      bes,1
      bes,1
      f,1
      f,1
      c,1
      bes,1
      f,1
      c,1
    }
  >>
  \layout { }
  \midi { \tempo 4 = 108 }
}
```

代码第 1–4 小节以 F7 的 A4 与 E♭5 表示三音、七音，同时低音停在 F2；第 5–6 小节是 B♭7 的 D5 与 A♭5，低音移到 B♭2；第 9 与 12 小节的 C7 使用 E4 与 B♭4。这个 voicing 显示固定音区中的 shell，同时避免把旋律、blue notes 或演奏 articulation 当作和弦本身。

实际作品需要跨段证据。McClimon 对《Blues for Alice》的分析指出，第 5 小节出现 subdominant 感，第 9 小节出现 home-key 的 ii–V；中段还把下行五度的目标改写为半音路径，并在第 11 小节落到 tonic 后接 turnaround。不能把它概括成“带附加和弦的十二小节”：具体小节、目标功能、替代路径和循环终止都应同时记录。来源：`mcclimon-2017-ii-v-space`，§§2.7–2.10、§4.1–4.3。

曲式也有不同尺度。Carter 的 113 首录音研究中，4+8 模型把十二小节的前四小节当作 verse、后八小节当作 prolonged refrain；8+8 模型把前四小节扩成八小节，使 verse-chorus 更清楚。Bessie Smith 的《Downhearted Blues》可作为 classic aab 的对照，而《She Moves Me》用密集前四小节与 textually sparse 的后八小节制造更明显的 chorus quality。来源：`carter-2025-beyond-strophic`，§§0.1–0.4、§§2.1–2.4。

因此，判断一曲是否为 blues，至少应并列检查循环长度、和声 quality、cadence/turnaround、歌词重复、录音编制与表演实践。只出现一个 blues scale 或 I7、IV7、V7 不足以完成判断。

## 从和弦骨架到可演奏安排

1. 先用一小节一个符号写出目标与局部 ii–V，确认低音有没有稳定的目标。
2. 在目标前标出三音与七音的连接，写下共同音、半音移动和跳进；三者可以同时存在。
3. 决定 voicing 的音区与密度。钢琴 shell、horn line 和 guitar comping 不必复制同一套四声部。
4. 对每个替代检查功能、根音路径与 upper structure。保留和弦功能不等于保留原来的低音方向。
5. 把一轮变化放回 blues、AABA 或 verse-chorus 等更大循环，检查 turnaround、solo chorus 和最后终止是否仍有不同职责。
6. 用至少一个版本核对旋律、节奏位置和 arpeggiation。Lead sheet 是一项 referent，不是全部实践。

## 反例、边界与证据缺口

- 并非所有爵士以 ii–V–I 为骨架；modal 和 free 风格可以以 pedal、motivic process 或 group interaction 组织。
- 并非所有 blues 都是十二小节；Carter 也记录 AABA、ABAC、verse/bridge blend、solo-bridge 与 two-bridge 等。
- 并非所有 standard 的 chorus 长度相同；《Cherokee》较长，而常见商业歌曲常被写成三十二小节，不能互相代替。
- Tritone substitution 可以保留 dominant function，却改变 bass motion；只看和弦功能会漏听低音路径。
- 谱例编译通过只证明音高、时值和语法可读，不能证明 voicing 好听、solo 有说服力或演奏符合历史风格。
- 当前证据没有为本文提供经过许可的实际作品谱例。涉及具体小节的结论全部属于文献分析，正文没有复制原作旋律或现代和弦谱。

主要来源：`mcclimon-2017-ii-v-space`；`smither-2019-guide-tone-space`；`hughes-lavengood-blues-harmony`；`carter-2025-beyond-strophic`；`smither-2024-referents`。具体版本、许可与段落定位见[来源表](../../knowledge/sources.json)。
