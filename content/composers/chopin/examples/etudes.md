<!-- music-kb:page {"id": "page.2442b8fb84834bfa9c8b09b740432062"} -->
<!-- knowledge: composer.chopin.etudes -->
# 肖邦练习曲：动作怎样长成结构

肖邦练习曲研究的起点不只是“右手要快”或“左手跨度很大”，而是一个更可核对的组合：哪一种动作持续、由哪只手承担、什么时候改变负担，以及改变以后音乐通过什么方式继续、返回并结束。Op. 10 与 Op. 25 经常让一个技术形状贯穿短小作品；B. 130 的三首《新练习曲》也可作为比较技术组织的案例。三者共享“技术限制产生音乐方向”的问题，却没有一套统一的织体或曲式。

本章比较 Op. 10 No. 2、Op. 10 No. 12、Op. 25 No. 1 与 B. 130 No. 1。乐谱事实来自本地 Mutopia 编码，涉及全曲的判断只覆盖已读段落。B. 130 的真实摘录仅取第 9–10 小节；另一例把 Op. 10 No. 2 开头两小节压缩成右手音高线索，省略伴奏并保留德语音名；第三例是本库自编模型，不含肖邦原句。

## 先把动作写成可观察量

可以用五个问题描述一首练习曲的技术组织：

| 观察量 | 要问什么 | 常见误判 |
| --- | --- | --- |
| 持续单位 | 何种时值、分组或音程反复出现？ | 把音型外观当成完整结构 |
| 手部负担 | 动作是否长期在一手，何时交给另一手？ | 把总谱中的旋律误认为一直由同一只手演奏 |
| 声部职责 | 主旋律、内声部和低音是否共享音型？ | 只记最高音，忽略内声部的方向 |
| 张力路径 | 音区、 chromaticism、密度和踏板怎样累积？ | 只凭力度记号判断高潮 |
| 返回方式 | 原样再现、缩略、换手、换调还是只保留轮廓？ | 把熟悉音型出现一次就称为全曲再现 |

这套观察把“技术”和“表达”连起来，也给出反例：持续音型可以只是伴奏；换手可以毫不改变和声方向；最快的段落也不一定是结构高潮。

## B. 130 No. 1：先分开，再叠合

B. 130 No. 1 的原编码有一个容易误读的开头。第 1–4 小节左手休止，右手演奏三连音；第 5 小节右手以前一阶段的收束音 F 结束，同时左手开始八分音符分解和弦；第 6–8 小节只有左手继续。把前四小节直接描述成“双手持续 3:4”会把先后展开的技术材料压成一个不存在的织体。第 9–10 小节出现本段所选的两手叠合：每一半小节是右手的三个三等分时值对左手的四个八分音符。

下面保留 Mutopia 的 2.16.2 语法和两个声部定义。原稿右手为相对音高；摘取第9小节时把锚点重设为 `\relative c'`，使首个C仍是C4，左手仍使用绝对音高；它们不是同一种音高输入方式，不能把左手的记号直接搬进右手相对块。

<!-- opusloom:example
{
  "id": "chopin.b130.etude1.combined-mm9-10",
  "status": "published",
  "source_version": "2.16.2",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-chopin-b130-etude1",
    "chopin-laphil-etudes"
  ],
  "rights": "Short excerpt from a Mutopia encoding declared Public Domain by typesetter Romain Behar. Attribution to Chopin, Behar, Mutopia, and the Bote & Bock 1880 source is retained.",
  "source_locator": "Trois Nouvelles Etudes No. 1, B. 130, mm. 9-10; source SHA-256 aa80beded6f3407afae7366a5f523c987e6cd58694054af7a524f820877835be",
  "context": "Pitch-duration excerpt mm9-10. Right-hand anchor reset to relative c' to retain the actual C4 entrance after omitted preceding bars; left hand absolute. Slurs, fingering, dynamics and pedal omitted. Original syntax version retained."
}
-->
```lilypond
\version "2.16.2"
\score {
  \new PianoStaff <<
    \new Staff = "right" \relative c' {
      \key f \minor
      \time 2/2
      \tupletUp
      \times 2/3 { r4 c aes' } \times 2/3 { g f b }
      \times 2/3 { c des b } \times 2/3 { c c, bes' }
    }
    \new Staff = "left" {
      \clef bass
      \key f \minor
      \time 2/2
      f,8 c f aes c' aes f c
      e,8 c g bes c' bes g c
    }
  >>
  \layout { }
  \midi { \tempo 4 = 100 }
}
```

读谱时先对齐两组半小节，而不是整小节笼统地听成“三对四”：右手的 `r4–c–aes` 与左手四个八分音符在同一半小节竞争；后半小节又出现 `g–f–b`。第 10 小节继续用相同的时间框架，但音高组织改变，左手的 `E–C–G–B♭` 也不再把同一和弦机械重复。两手的实际叠合因此同时带来节奏摩擦、和声变化和音区交换。

这一事实还限制了后续论述：谱例不能证明前八小节始终有两种律动重叠，也不能证明全曲每一段都靠 3:4 产生张力。该曲后续在单线织体、交替音型、持续音域运动和长段一连串三连音之间变化；第 57 小节回到较简单的收束线，随后进入和弦性尾段。结构来自“技术负担如何转移”，不是固定比例本身。

## Op. 10 No. 2：一只手的内部层级

Op. 10 No. 2 的常见概述强调右手 chromatic scalar passage，但原编码显示右手并非只有一个平面：外层持续十六分音符，另一层用双音标记和声落点，左手负责更稀疏的支撑。第 1–2 小节已经把这种关系写清楚：

<!-- opusloom:example
{
  "id": "chopin.op10-2.pitch-path-mm1-2",
  "status": "published",
  "source_version": "2.16.1",
  "compile": "fragment",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-chopin-etude-op10-2",
    "chopin-laphil-etudes"
  ],
  "rights": "Public Domain encoding declared by typesetter Roland Goretzki; only a two-measure right-hand pitch path is reproduced with attribution.",
  "source_locator": "Etude Op. 10 No. 2, mm. 1-2; right-hand outer voice; source SHA-256 2471fb07690a2b8f7550d8d96b686c4bb3907556a8002b57fcef71111e503c1c",
  "context": "Pitch-duration reduction of original right-hand outer voice, mm1-2; original relative c' anchor and German spelling retained (h=B natural, b=B flat). Right-hand dyads, accompaniment, fingerings, dynamics and other expressive marks omitted."
}
-->
```lilypond
\version "2.16.1"
\include "deutsch.ly"
\key a \minor
\time 4/4
\tempo "Allegro" 4 = 144
\relative c' {
  a'16 ais h c cis d dis e f fis g gis a ais h c |
  cis d dis e f e dis d cis c h b a gis h a |
}
```

这里保留原编码的德语音名：h为B自然、b为B降。相对音高外层也保留，第一音a'是A4，随后沿半音上行。两条十六分音符线都填满四拍。第一条主要上行，第二条先继续向高音，再通过前半音的密集邻接回落。原谱在这些音符下方另列双音和左手支持；所以不能把这一例子当作“旋律加伴奏”的完整模型。它只证明外层音高路径本身具有方向性： chromatic ascent在第二小节被反向重述，而不是均匀绕圈。

这种“少数几个音级不断被不同八度、邻音和和声点重新解释”的写法，和 Op. 25 No. 1 的持续三连音有可比性，但动作并不一样。Op. 25 No. 1 让两个手共同维持宽阔的分解和弦场，旋律性来自重音、内层音高和音区；Op. 10 No. 2 则把旋律线索留在右手持续线中，用更明显的 chromatic邻接制造技术难点。

## Op. 10 No. 12：某只手的休止不是全谱的停顿

这首练习曲适合检验“技术冲动怎样持续”的另一个层面。原编码第1小节，右手以重音和弦开始，随后休止；左手却在一个八分休止之后立即接入快速十六分音符下行。因而，“开头先是和弦与空拍、之后才有快速运动”只描述了右手的一部分，不能代表总谱。

| 原编码位置 | 可核对的左手事件 | 分析时要同时问什么 |
| --- | --- | --- |
| mm.1–4 | 短休止后的连续快速下降与低处反复 | 右手空白是否由左手维持运动？ |
| mm.9–13 | C小调分解轮廓反复，含C–G–C–D–E♭等音级 | 相似动作怎样由和声及音区重新定向？ |
| mm.29–36 | 不同和声背景与半音邻接下仍有密集十六分活动 | 力度或右手密度改变是否真的带来速度、总密度的改变？ |

这里不把中段称作“较慢的歌唱段”，也不把几处安静或右手休止当作左手停止。作曲时可先让某一声部保持动力，再改变另一声部的发声职责；复核时逐声部查看，最后合读总谱。这些小节支持局部对照，完整再现与尾声边界仍需另做全曲分析。

## Op. 25 No. 1：同一分解动作中的声部与重音

Op.25 No.1的原编码有四分音符弱起；随后快速分解用三连音十六分组织，每个四分拍包含六个快速音。这里的“三连音”与B.130的三连音四分、左手普通八分不是同一种时值层级，不能把两首都简化为相同的3:4模型。

与Op.10 No.2的外层半音线相比，这首的辨识线索需要在连续分解中寻找：哪些音被强调、哪些音保留更长时值、内声部怎样延续、低音与上层音区何时改变。连续快速音提供稳定背景，重音与持续音则可使另一条较慢的线被读出。把每个快速音都视为同等旋律单位，会抹平这种层级；每两小节另造新音型，又可能取消持续动作的记忆作用。

Roy Howat在2026年研究中区分不同长度和功能的连线，包括短的强弱呼吸、乐句连线和跨较长段落的spianato（p.60）；不能把所有弧线统一理解成换气或普通legato。本文用这一限定提醒读者回到具体声部与版本，没有把未编码的Op.25 No.4手稿图例当作本页谱例，也不为Op.25 No.1的全曲边界给出未经逐段核验的固定表。

## 自编模型：把技术负担从右手移到左手

下面的模型不是肖邦原作，也不借用上述作品的旋律。它只演示一种可迁移结构：右手用固定十六分音型建立“动作”，随后停在一个短动机上；左手接过这个动机，右手变为稀疏支点；最后一小节让两手在同一终止位置汇合。

<!-- opusloom:example
{
  "id": "chopin.etudes.model.role-migration",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["chopin-laphil-etudes", "mutopia-chopin-etude-op25-1"],
  "rights": "OpusLoom original pedagogical model. It contains no Chopin melody or copied score excerpt.",
  "source_locator": "Transfer model derived from the chapter's observations on Op. 25 No. 1 and B. 130 No. 1; not a transcription",
  "context": "Four-bar piano model in C minor. An upper surface yields to left-hand motivic ownership, then both hands converge on one structural arrival."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new PianoStaff <<
    \new Staff = "upper" {
      \clef treble \key c \minor \time 4/4
      \tempo "Agitato" 4 = 132
      g'16 c'' ees'' c'' g' c'' ees'' c'' g' c'' ees'' c'' g' c'' ees'' c'' |
      g'16 b' d'' b' g' b' d'' b' g' b' d'' b' g' b' d'' b' |
      r2 g'4 c'' |
      <c'' ees''>2 <g' c''>2 |
    }
    \new Staff = "lower" {
      \clef bass \key c \minor \time 4/4
      c,1 | g,,1 |
      g,8 c ees c g,4 c4 |
      <g,, g,>2 <c, c>2 |
    }
  >>
  \layout { }
  \midi { }
}
```

前两小节的和声骨架其实很慢：C 到 G。快的是右手表面，不是低音。第一小节右手将G4–C5–E♭5–C5重复四次；第三小节左手把同一轮廓移低两个八度，并将十六分扩大为八分，右手先休止半小节再用G–C支点回应。第四小节让G到C的低音和上方C小调音组共同收束。这个模型说明“换手”只有改变听觉职责时才有结构意义。若左手只是重复右手音型，而重音、音区和和声都没有改变，换手仍然只是位移。

迁移到新作品时，可以固定四项并只改一项：

| 步骤 | 保持 | 改变 | 检查 |
| --- | --- | --- | --- |
| 1 建立动作 | 音型、拍位、音区 | 不改变 | 是否能听出持续单位？ |
| 2 加入负担 | 低音骨架 | 增加远距离或 inner-voice 运动 | 张力来自哪里？ |
| 3 转移职责 | 节奏身份 | 换手、重音、声部密度 | 新声部是否成为主角？ |
| 4 返回 | 材料轮廓 | 和声、手位、长度或结尾 | 返回增加了什么新意义？ |

## 证据边界

本章使用了四份本地乐谱编码。它们是 Mutopia 排版，不是肖邦手稿校勘；作品内部的段落判断来自本次读谱，部分概述有洛杉矶爱乐节目说明支持。Roy Howat 关于开放连线和 tenuto 标记的研究提醒我们：谱上的一条线可能同时涉及触键、声部延续与释放时间，不能一概译成普通连奏。该研究的具体Op. 25 No. 4 例子没有在本章编码。

本章未证明的内容包括：三套练习曲共享同一曲式模板；B. 130 全曲持续 3:4；所有高速段落都对应情感高潮；或者“在任何钢琴织体中，换手都会形成曲式”。这些都需要逐曲、逐段证据。

### 来源

- `mutopia-chopin-etude-op10-2`、`mutopia-chopin-etude-op10-12`、`mutopia-chopin-etude-op25-1`、`mutopia-chopin-b130-etude1`：本地编码版本、来源谱、维护者、许可和 SHA-256。
- `chopin-laphil-etudes`：Steve Lacoste，洛杉矶爱乐节目说明；支持作品级技术问题概述，不替代读谱。
- `howat-2026-chopin-tenuto`：Roy Howat，*Music Performance Research* 13（2026）；支持对开放连线与 tenuto 边界的具体研究提醒。
