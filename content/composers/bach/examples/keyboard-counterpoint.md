<!-- music-kb:page {"id": "page.e77b01632d0140e4ac5c08545b05490e"} -->
<!-- knowledge: composer.bach.keyboard-counterpoint -->
# 巴赫键盘复调：从发明曲到前奏曲—赋格

发明曲与赋格共同把材料交接当作音乐推进的动力，但声部数、主题进入秩序和段落职责并不相同。本章把 BWV 772 的二声部对话与 BWV 846 的前奏曲—赋格并读：先看局部动机如何被另一条线接手，再看四声部进入如何增加约束，最后把听觉焦点从前奏曲的和声流动转向赋格的主题追踪。这里以两部作品作为证据，不把它们概括为全部巴赫键盘写作。

| 问题 | 发明曲 BWV 772 | BWV 846 前奏曲—赋格 |
| --- | --- | --- |
| 材料如何保持辨识度 | 短音型、轮廓和角色交接 | 主题陈述与伴随声部；前奏曲另有持续音型 |
| 织体怎样推进 | 两条线在不同节奏层之间轮换 | 前奏曲稳定分解和弦，赋格逐步引入独立声部 |
| 创作时先检查什么 | 交接后的旋律连续和和声支撑 | 进入间隔、声部冲突、终止与篇章功能 |

以下谱例分别检验这些观察。代码只覆盖注明的小节，整对作品的结构解释与局部音符事实分开阅读。

<!-- knowledge: bach.invention.bwv772.motive-dialogue -->
## BWV 772：用短动机维持二声部对话

### 观察目标

第 1–4 小节不是“右手旋律加左手伴奏”。两个声部使用同一组音级材料：以三和弦音或级进轮廓形成短单元，再由另一声部接续。判断动机关系时，应同时比较音级顺序、节拍位置、方向和后续和声，而不是只比较音高集合。

### 谱例

<!--
id: bach.bwv772.motive-dialogue
source-version: 2.11.46
corpus-path: lilypond/BachJS/BWV772/bach-invention-01/bach-invention-01.ly
corpus-sha256: 3c01302f70efd1dd6f43becaf19b9b2aac49e25b3e89666e3e55bc576c6cd55d
source: mutopia-bach-bwv772
rights: CC-BY-SA-3.0
-->

<!-- opusloom:example
{
  "id": "bach.bwv772.motive-dialogue",
  "status": "published",
  "source_version": "2.11.46",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-bach-bwv772",
    "bach-digital",
    "omt-fugue"
  ],
  "rights": "CC-BY-SA-3.0",
  "source_locator": "lilypond/BachJS/BWV772/bach-invention-01/bach-invention-01.ly",
  "context": "二声部发明曲的短动机呈现、交接与模进"
}
-->
```lilypond
\version "2.11.46"
upper = \relative c' {
  \time 4/4
  r16 c[ d e] f[ d e c] g'8[ c b^\prall c] |
  d16[ g, a b] c[ a b g] d'8[ g f^\prall g] |
  e16[ a g f] e[ g f a] g[ f e d] c[ e d f] |
  e[ d c b] a[ c b d] c[ b a g] fis[ a g b] |
}
lower = \relative c {
  \clef bass \time 4/4
  r2 r16 c[ d e] f[ d e c] |
  g'8[ g,] r4 r16 g'16[ a16 b16] c16[ a16 b16 g16] |
  c8[ b c d] e[ g, a b] |
  c[ e, fis g] a[ b] c4 |
}
\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \lower }
  >>
  \layout { }
  \midi { }
}
```

原编码：jeff covey，Mutopia-2008/06/15-40，CC BY-SA 3.0。此处摘录两声部第1–4小节，保留音高、时值与 prall。仅将变量改名、补上下文，并移除低声部末尾跨越截取边界的延音线；该音原来连到第5小节，不代表此处终止。改编说明与分析按 CC BY-SA 4.0 分发，保留原编码许可归属。

### 代码与音乐对应

| 位置 | 可观察事件 | 写作含义 |
| --- | --- | --- |
| 右手第 1 小节 | 第一拍内 r16 后以 C–D–E–F–D–E–C 进入，继以八分音符 | 短材料以节奏与折返轮廓辨识；r16 是小节内休止，不是弱起小节 |
| 左手第 1–2 小节 | 后半进入相近的级进与装饰性折返 | 第二个声部取得对话资格，并非静态伴奏 |
| 第 2–3 小节 | 第2小节上声部从D进入相近轮廓，第3小节上声部继续十六分活动、低声部转八分活动 | 移位和模进扩大材料，不改变核心语汇 |
| 第 4 小节 | 第4小节两条线仍然继续：低声部终音C在原作连到第5小节 | 截取边界不等于乐句终止，不能从此四小节认定完整终止 |

### 可迁移规则

1. 先选定可辨认的短核，再决定持续音型与轮廓；不把一拍长度当作巴赫主题的通则。
2. 第二声部进入时保留至少两个可辨认关系：音程轮廓、节奏位置或终止方向。
3. 区分实际移调、模进与其他动机变化；重复同一调性也可服务于结构，不能规定每次都必须改变和声功能。
4. 在完整段落末核对终止；本例第4小节只是截取边界。

### 不可直接迁移

这段材料是完整二声部作品的开端。它不能证明四个声部可以同时使用同一音区，也不能单独证明 invertible counterpoint 成立。需要倒置复调时，应把转位后的音程、碰撞和终止重新写成可编译片段并做声部核查。

### 来源和核验

- [Mutopia: BWV 772](https://www.mutopiaproject.org/ftp/BachJS/BWV772/bach-invention-01/)：排版来源 Bach-Gesellschaft，示例代码保留 2.11.46 语法。
- [Bach Digital](https://www.bach-digital.de/)：用于核对 BWV 作品编号和来源记录。
- [Open Music Theory: High Baroque fugal exposition](https://viva.pressbooks.pub/openmusictheory/chapter/high-baroque-fugal-exposition/)：用于区分主题陈述、模仿与伴随材料；本页没有把发明曲误称为赋格。

代码必须在转换到 LilyPond 2.26.0 后生成 PDF 和 MIDI，且源文件、转换报告与谱面抽样通过后才可标为发布状态。

<!-- knowledge: bach.fugue.bwv846.exposition -->
## BWV 846：赋格呈示部不是四遍齐奏

### 先区分术语

`subject` 是首先建立的主要材料；`answer` 是另一声部在属方向作出的回答，常因调性调整而不完全等于移调；`countersubject` 是反复与 subject/answer 结合并能转位使用的伴随材料。一个伴随声部出现过一次，只能叫自由对位。`episode` 则连接主题进入，并不属于呈示部本身。

### 谱例

<!--
id: bach.bwv846.fugue.exposition
source-version: 2.16.1
corpus-path: lilypond/BachJS/BWV846/wtk1-fugue1/wtk1-fugue1.ly
corpus-sha256: 10d51eabac0fdfeddcbb7d76ad3bf361d4c095feec3ce7aa61d034d5b836c708
source: mutopia-bach-bwv846-fugue
rights: Public-Domain
-->

<!-- opusloom:example
{
  "id": "bach.bwv846.fugue.exposition",
  "status": "published",
  "source_version": "2.16.1",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-bach-bwv846-fugue",
    "bach-digital",
    "omt-fugue"
  ],
  "rights": "Public-Domain",
  "source_locator": "lilypond/BachJS/BWV846/wtk1-fugue1/wtk1-fugue1.ly",
  "context": "四声部赋格开头与高巴洛克呈示部"
}
-->
```lilypond
\version "2.16.1"

global = { \time 4/4 \key c \major }

soprano = \relative c' {
  r1 |
  r2 r8 g'[a b] |
  c8. d32 c b8[e] a,[d] ~ d16 e d c |
  b g a b c b c d e d e fis g8 b, |
  c a d16 c b a g8. g16 f e f g |
  a g a b c2 b4 |
}

alto = \relative c {
  r1 |
  r1 |
  r1 |
  r8 g'[a b] c8. d32 c b8 e |
  a, d ~ d16 e d c b8 c ~ c bes |
  a[d] g,[c] r16 a b c d4 |
}

tenor = \relative c' {
  r8 c d e f8. g32 f e8 a |
  d, g ~ g16 a g f e f e d c d c b |
  a8 fis' g4 ~ g8 fis!16 e fis8 d |
  g f! e d c r r g' ~ |
  g f16 e f4 ~ f16 f e8 d4 |
  c8 f r16 g f e f8 d g4 ~ |
}

bass = \relative c {
  r1 |
  r1 |
  r1 |
  r1 |
  r1 |
  r2 r8 c[d e] |
}

\score {
  \new PianoStaff <<
    \new Staff << \global
      \new Voice = "soprano" { \voiceOne \soprano }
      \new Voice = "tenor" { \voiceTwo \tenor }
    >>
    \new Staff << \global \clef bass
      \new Voice = "alto" { \voiceOne \alto }
      \new Voice = "bass" { \voiceTwo \bass }
    >>
  >>
  \layout { }
  \midi { \tempo 4 = 66 }
}
```

### 分析

| 观察点 | 证据 | 生成时的约束 |
| --- | --- | --- |
| 单声部开端 | 主题前两小节先由内声部陈述 | 其他声部进入前不要用伴奏填满所有拍点 |
| 属方向回答 | 第二进入改写音程，保持主题可辨识轮廓 | answer 必须服务调性，不能机械整体移调 |
| 伴随材料 | 每次进入时已有声部继续运动，出现可重复结合的材料 | 至少检查两次结合；能倒置才标为 countersubject |
| 全声部依次进入 | 四声部在短范围内完成 subject/answer 轮换 | 完成呈示部后转入 episode，不应无休止增加入口 |

不要把“主题音高完全相同”当作唯一的材料同一性。生成报告应分别列出：起始音区、音级轮廓、节奏骨架、终止方向、与已有声部的结合。

### 写作流程

1. 先写单声部 subject，并明确调性中心与可辨节奏。
2. 在不同音区写 answer，检查关键音程是否需作 tonal adjustment。
3. 每次新进入前保留一个仍在运动的声部，检查其与 subject/answer 的协和、独立节奏和可转位性。
4. 四声部都进入后安排 episode 或终止，不把主题入口当作结构填充。

### 局限

本片段只覆盖呈示部开头。episode、middle entries、stretto、pedal 与最终终止必须另读实际段落。代码编译成功不代表 answer 类型、countersubject 身份或全曲曲式判断正确。

### 来源

- [Mutopia: BWV 846 Fugue](https://www.mutopiaproject.org/ftp/BachJS/BWV846/wtk1-fugue1/)：公有领域、原始语法 2.16.1。
- [Open Music Theory: High Baroque fugal exposition](https://viva.pressbooks.pub/openmusictheory/chapter/high-baroque-fugal-exposition/)：subject、answer、countersubject、exposition 的工作定义。
- [Bach Digital](https://www.bach-digital.de/)：作品和来源控制。

<!-- knowledge: bach.cycle.bwv846.prelude-to-fugue -->
## BWV 846：前奏曲与赋格的跨段落关系

### 结构判断

前奏曲以重复的分解和弦音型建立稳定节拍和持续流动；赋格改用短主题的分声部进入与复调织体。这里最可靠的跨段关系是功能转换：前奏曲先展开和声与织体空间，赋格随后把听者的注意转向主题识别和声部对话。现有谱面不足以把两者都概括成同一动机的变奏，因此除非另给出轮廓、音程和节奏映射，应保留这一解释边界。

### 前奏曲谱例

<!--
id: bach.bwv846.prelude.opening
source-version: 2.14.2
corpus-path: lilypond/BachJS/BWV846/wtk1-prelude1/wtk1-prelude1.ly
corpus-sha256: afa237b10637ca7839b4c9e98b64ba89c781e2cfc1b980679b2632a31951aacd
source: mutopia-bach-bwv846-prelude
rights: Public-Domain
-->

<!-- opusloom:example
{
  "id": "bach.bwv846.prelude.opening",
  "status": "published",
  "source_version": "2.14.2",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-bach-bwv846-prelude",
    "mutopia-bach-bwv846-fugue",
    "bach-digital"
  ],
  "rights": "Public-Domain",
  "source_locator": "lilypond/BachJS/BWV846/wtk1-prelude1/wtk1-prelude1.ly",
  "context": "成对作品的织体转换；不主张两段共享同一动机"
}
-->
```lilypond
\version "2.14.2"

upper = {
  \time 4/4
  r8 g16[ c'] e'[ g c' e'] r8 g16[ c'] e'[ g c' e'] |
  r8 a16[ d'] f'[ a d' f'] r8 a16[ d'] f'[ a d' f'] |
}

lower = <<
  {
    \clef bass
    c'2 c' | c' c' |
  }
  \\
  {
    r16 e'8. ~ e'4 r16 e'8. ~ e'4 |
    r16 d'8. ~ d'4 r16 d'8. ~ d'4 |
  }
>>

\score {
  \new PianoStaff <<
    \new Staff { \clef treble \transpose c c' { \upper } }
    \new Staff { \lower }
  >>
  \layout { }
  \midi { \tempo 4 = 60 }
}
```

原编码的右手在 `\transpose c c'` 中，摘录保留这层升八度上下文；左手不移调。不能只复制绝对音高片段而丢掉外层移调。仅移除版面指令，前两小节音高、时值与持续低音保留。

### 跨段阅读表

| 段落 | 主要听觉线索 | 作曲任务中的用途 |
| --- | --- | --- |
| 前奏曲开头 | 同一音型的重复、音区铺展、和声逐一变化 | 建立调性空间和持续脉动 |
| 赋格开头 | 单声部主题、分声部进入、伴随对位 | 把发展动力转为材料识别与声部关系 |
| 两段接合 | 调性保持，节奏表面和声部组织明显改变 | 用织体对比形成套曲性，而不是复制主题 |

如果把这一结构用于创作任务，先写出两段的“变化轴”：哪一项保持，哪一项改变。例如保持 C 大调和四拍脉冲，改变发声密度、主要材料和终止策略。只换速度不算跨段设计；只在两段使用同一音型也不会自动形成结构关系。

### 来源

- [Mutopia: BWV 846 Prelude](https://www.mutopiaproject.org/ftp/BachJS/BWV846/wtk1-prelude1/)
- [Mutopia: BWV 846 Fugue](https://www.mutopiaproject.org/ftp/BachJS/BWV846/wtk1-fugue1/)
- [Bach Digital: Wohltemperiertes Klavier I source records](https://www.bach-digital.de/staticpages/Source_Additionals/dlebmsvaria_de.html)

confidence 标为 interpretive，因为“两段如何构成统一整体”属于解释；谱面中的音高、时值、调性和段落类型则是待编译核验的事实。
