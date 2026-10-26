<!-- music-kb:page {"id": "page.e845082f45994b84b2a7f7a670f425ff"} -->
<!-- knowledge: composer.mozart.piano-sonatas -->
# 莫扎特钢琴奏鸣曲：乐句、戏剧对比与再现

“清晰的古典句法”不等于所有乐句长度、织体和调性回归都相同。K.545 与 K.457 适合并读：前者展示开头材料如何继续，后者让主和弦轮廓与突然的织体对比进入前景。再把 K.545 开头与再现入口并置，可以看见局部主题辨识和全曲调性过程并非同一个层次。

| 分析尺度 | 对照材料 | 可转成创作检查的问题 |
| --- | --- | --- |
| 动机与乐句 | K.545 开头八小节 | 基本乐思之后如何加速、分裂和指向终止？截取结束是否真为终止？ |
| 织体与修辞 | K.457 开头 | 对比来自音符、力度、停顿还是音区？低音是否支持所称的和声？ |
| 较大结构 | K.545 开头与再现 | 可辨认的材料如何在不同调性位置回归？何处才完成主调闭合？ |

谱例分别承担局部证据；不能仅凭开头四或八小节推导整首曲式。尤其 K.545 再现入口位于 F 大调，不应套用“再现第一音必在主调”的规则。

<!-- knowledge: mozart.sentence.k545.opening -->
## K. 545：从短单元观察主题继续

### 先看功能

开头句法可根据重复/变化关系分成 presentation 与 continuation。presentation 提出 basic idea，并通过重复或应答稳定它；continuation 通常增加碎片化、和声活动或节奏推进，并把乐句带向终止。标记这些功能需要同时分析旋律和低音，不能只数小节。

### 谱例

<!--
id: mozart.k545.opening-sentence
source-version: 2.16.0
corpus-path: lilypond/MozartWA/KV545/K545-1/K545-1.ly
corpus-sha256: 84d0e951e6d8807d3286f31ed7878a35dfddb9850bbae9156be0f5ac0a3e2e10
source: mutopia-mozart-k545-m1
rights: CC-BY-SA-3.0
-->

<!-- opusloom:example
{
  "id": "mozart.k545.opening-sentence",
  "status": "published",
  "source_version": "2.16.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-mozart-k545-m1",
    "bl-mozart-catalogue",
    "omt-sentence",
    "omt-cadences"
  ],
  "rights": "CC-BY-SA-3.0",
  "source_locator": "lilypond/MozartWA/KV545/K545-1/K545-1.ly",
  "context": "古典主题开头的句法分段与右手/左手功能"
}
-->
```lilypond
\version "2.16.0"

right = \relative c'' {
  \time 4/4 \key c \major
  c2-1(\mp e4-3 g-5 |
  b,4.-1_> c16 d c4) r4 |
  a'2-3(_\accent g4\< c\! |
  g-3_\accent f8\trill\> e16 f e4)\! r4 |
  a,8\p\<\( b16 c d-1 e f g\! a\> g f e d c-4 b a\! |
  g8\< a16 b c-1 d e f\! g\> f e d c b-4 a g\! |
  f8\< g16 a b-1 c d e\! f\> e d c b a-4 g f\! |
  e8\< f16 g a-1 b c d\! e\> d c b a-4 g f e\!\)
}

left = \relative c'' {
  \clef treble \time 4/4 \key c \major
  c,8-5(\p g'-1 e-3 g c, g' e g) |
  d-4 g-1 f-2 g c,-5 g'-1 e-3 g |
  c, a'-1 f-2 a c, g'-1 e-3 g |
  b,-5 g'-1 d-3 g c,-4 g'-1 e-2 g |
  f4 r4 r4 \clef bass <f, c'>_4-. |
  <e c'>-. r4 r4 <e c'>_4-. |
  <d c'>-. r4 r4 <d b'>_4-. |
}
lastLeft = \relative c { <c c'>4-. r4 r4 <c-5 e-3>-. }

\score {
  \new PianoStaff <<
    \new Staff { \right }
    \new Staff { \left \lastLeft }
  >>
  \layout { }
  \midi { \tempo 4 = 132 }
}
```

源编码 Alejandro Sierra，Mutopia-2013/09/01-998，CC BY-SA 3.0。摘取原谱第1–8小节，保留左手原始 `\relative c''` 锚点（开头C4），从 `ptlh` 补齐第8小节；添加小节线和独立变量，仅去除重复遍的指法分支。改编说明与分析按 CC BY-SA 4.0 分发。

### 分析表

| 段落功能 | 右手证据 | 左手证据 | 生成检查 |
| --- | --- | --- | --- |
| basic idea | 主和弦音组成的短轮廓 | 阿尔贝蒂低音建立节拍和声 | 主题应能缩短成一个可复述单元 |
| 应答/重复 | 第 3–4 小节换音区并改变终止落点 | 低音和声改变，织体保持 | 重复要改变功能或音区，不能无目标复制 |
| continuation | 第 5 小节起节奏加快，旋律碎片化 | 低音级进和声活动增加 | 推进必须服务于终止目标 |
| 截取边界 | 第8小节仍延续十六分音符活动 | 原谱第8小节是C八度及C–E支点，不是误拼的后续属低音 | 本例没有展示完整终止，须继续读取第9–12小节 |

### 可迁移流程

1. 用一个 2 小节 basic idea 建立可辨轮廓。
2. 用音的交换、音区或终止落点写出应答，而不是把伴奏一同复制。
3. 在 continuation 中缩小动机单位、增加节奏事件并推进和声。
4. 最后以真实低音和终止型结束。只拉长旋律而不改变低音，不会形成完整句法。

### 局限

前 8 小节可以支持 sentence 阅读，但完整主题或更大曲式的判断要结合后续段落。`music21` 可核对拍、时值和音高；sentence、basic idea 与 continuation 仍需要谱面分析。

### 来源

- [Mutopia: K. 545 first movement](https://www.mutopiaproject.org/ftp/MozartWA/KV545/K545-1/)：CC BY-SA 3.0，原始 LilyPond 2.16.0。
- [Open Music Theory: The sentence](https://openmusictheory.github.io/sentence.html)
- [Open Music Theory: Cadence types](https://openmusictheory.github.io/cadenceTypes)
- [British Library: Mozart Thematic Catalogue](https://searcharchives.bl.uk/catalog/040-001945812)：一手目录材料边界。

<!-- knowledge: mozart.sonata.k545.cross-section -->
## K. 545：把奏鸣曲式写成可检查的跨段任务

### 结构地图

任务中写“奏鸣曲式”时，交付物应先有段落表：P、TR、S、C、展开与 P/S 材料旋转、再现最终实现主调闭合；主部回返不必立即在主调。代码中的变量名不能替代分析；必须给出实际小节、调性、终止和材料来源。

| 段落 | 当前作品的来源标签 | 检查问题 |
| --- | --- | --- |
| exposition | `ptrha`、`strha` 等 | 主部是否稳定，副部是否在属调或关系调成立 |
| development | `dvrh` 与左手 `dvlh` | 使用了哪些既有材料，张力如何积累 |
| recapitulation | `\transpose c f \relative c'' { \ptrha }` 与后续副部 | 第42小节主部在F大调回返；副部后续转回C大调，最终闭合须读完整段 |

### 再现入口谱例

<!--
id: mozart.k545.recapitulation-entry
source-version: 2.16.0
corpus-path: lilypond/MozartWA/KV545/K545-1/K545-1.ly
corpus-sha256: 84d0e951e6d8807d3286f31ed7878a35dfddb9850bbae9156be0f5ac0a3e2e10
source: mutopia-mozart-k545-m1
rights: CC-BY-SA-3.0
-->

<!-- opusloom:example
{
  "id": "mozart.k545.recapitulation-entry",
  "status": "published",
  "source_version": "2.16.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-mozart-k545-m1",
    "omt-sonata-intro",
    "omt-sonata-development",
    "omt-sonata-recap"
  ],
  "rights": "CC-BY-SA-3.0",
  "source_locator": "lilypond/MozartWA/KV545/K545-1/K545-1.ly",
  "context": "用主题旋转和调性闭合检查奏鸣曲式跨段落修改"
}
-->
```lilypond
\version "2.16.0"
right = {
  \time 4/4 \key c \major
  \transpose c f \relative c'' {
    c2-1(\mp e4-3 g-5 |
    b,4.-1_> c16 d c4) r4 |
    a'2-3(_\accent g4\< c\! |
    g-3_\accent f8\trill\> e16 f e4)\! r4 |
  }
}
left = {
  \clef bass \time 4/4 \key c \major
  \transpose c f \relative c'' {
    c,8-5(\p g'-1 e-3 g c, g' e g) |
    d-4 g-1 f-2 g c,-5 g'-1 e-3 g |
    c, a'-1 f-2 a c, g'-1 e-3 g |
    b,-5 g'-1 d-3 g c,-4 g'-1 e-2 g |
  }
}
\score {
  \new PianoStaff <<
    \new Staff { \right }
    \new Staff { \left }
  >>
  \layout { }
  \midi { }
}
```

### 为什么选这一段

这是再现开始第42–45小节，不是原来误拼的六小节右手加四小节左手。对照[呈示开头](piano-sonatas.md)第1–4小节：这里从源谱 `ptrha` / `ptlha` 的对应内容各取前四小节，并执行源谱中的 `\transpose c f`。源文件 `\relative c''` 锚点保留，左右手各四小节；变量改名、补上下文与小节线，未改实际音高和时值。

K.545 的特殊处是主部材料在下属调F大调回返，不能把“再现主部必须在主调”当作硬规则。之后经过重写转接，副部才在主调C大调组织闭合。再现辨认要结合材料对应及后续调性过程，不能单凭第一和弦或两个主题变量名。

原编码者 Alejandro Sierra（Mutopia-2013/09/01-998），完整编码的署名、版本和 CC BY-SA 3.0 见原文件 header；本库摘录与分析的改编按 CC BY-SA 4.0 提供。此谱例只证明再现入口与呈示对应，不单独证明末尾的终止类型。

### 生成任务模板

```text
段落表：
P:  小节 ___，调 ___，材料 ___，终止 ___
TR: 小节 ___，起点 ___，到达 ___，准备 ___
S:  小节 ___，调 ___，材料 ___，终止 ___
C:  小节 ___，补充材料 ___，终止 ___
Dev: 小节 ___，引用 ___，张力峰 ___，回主调准备 ___
Recap: P ___，TR ___，S ___，C ___，主调终止 ___
```

生成的代码、`music21` 事实表和段落表必须互相一致。编译通过但副部没有调性闭合时，任务状态仍是音乐目标未达成。

### 来源

- [Mutopia: K. 545 first movement](https://www.mutopiaproject.org/ftp/MozartWA/KV545/K545-1/)：示例的谱面与原始语法。
- [Open Music Theory: Introduction to sonata theory](https://openmusictheory.github.io/SonataTheory-intro.html)
- [Open Music Theory: The development](https://openmusictheory.github.io/sonataDevelopment.html)
- [Open Music Theory: The recapitulation](https://openmusictheory.github.io/sonataRecap.html)

本页代码只覆盖一个接合片段；段落表来自源文件中的功能分区，不构成未经核验的小节级完整分析。

<!-- knowledge: mozart.rhetoric.k457.c-minor -->
## K. 457：用小调主题结构限制“戏剧性”

### 谱例

<!--
id: mozart.k457.first-movement.opening
source-version: 2.18.0
corpus-path: lilypond/MozartWA/KV457/sonata1/sonata1.ly
corpus-sha256: 991ca730de5cb9e4550bb7f67ce1226c72f56b5bf3fd6bba03551667707541ee
source: mutopia-mozart-k457-m1
rights: Public-Domain
-->

<!-- opusloom:example
{
  "id": "mozart.k457.first-movement.opening",
  "status": "published",
  "source_version": "2.18.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "mutopia-mozart-k457-m1",
    "omt-sonata-intro",
    "omt-harmonic-functions"
  ],
  "rights": "Public-Domain",
  "source_locator": "lilypond/MozartWA/KV457/sonata1/sonata1.ly",
  "context": "小调主题中的主和弦轮廓、突然对比和钢琴织体"
}
-->
```lilypond
\version "2.18.0"
\include "english.ly"

upper = \relative c' {
  \time 2/2 \key c \minor
  c2^^-\f eflat4-\staccatissimo g-\staccatissimo |
  c-\staccatissimo eflat-\staccatissimo r8. eflat16-.-\p eflat8(-[-\trill d16 eflat-] |
  g4 c,-.-) c-. c-. |
  aflat'-( b,-)-. b-. r |
}

lower = \relative c, {
  \time 2/2 \key c \minor
  <c c'>2^^-\sustainOn <eflat eflat'>4-\staccatissimo-\sustainOff <g g'>-\staccatissimo |
  <c c'>-\staccatissimo <eflat eflat'>-\staccatissimo r2 |
  \clef "treble"
  r4 <eflat' g>-. <eflat g>-. <eflat g>-. |
  r <d f aflat>-. <d f aflat>-. r |
}

\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \lower }
  >>
  \layout { }
  \midi { \tempo "Molto allegro" 2 = 84 }
}
```

代码保留源文件前四小节的右手主题和真实低音，不把钢琴织体简化成虚构的静态和弦。

### 分析

| 事件 | 谱面证据 | 生成约束 |
| --- | --- | --- |
| 小调主和弦轮廓 | C–E-flat–G 的跳跃与重复 | 调性和弦音要清楚建立，不能只靠音阶快速跑动 |
| 强弱与奏法对比 | 强奏柱式材料后立即进入弱奏流动音型 | 对比要有共同结构锚点，否则只是段落拼接 |
| 突然的半音关系 | A-flat 与还原 B 方向的变化制造色彩和张力 | 半音音级要服务和声目标，不能无解决地堆积 |
| 乐句短促进入 | 前两小节连续改变密度 | 长篇写作应先保存动机与终止计划，再增加戏剧性 |

### 可迁移策略

1. 用主和弦音和清楚节奏建立小调中心。
2. 第二单元改变密度与力度，但保留乐句长度、低音目标或音高轮廓之一。
3. 将突变安排在结构点附近，并检查后续和声是否真正解释它。
4. 每次变化后回到可辨认材料；持续高张力会让对比失去意义。

### 局限

“戏剧性”“紧张”不能由机器自动证明。`music21` 可以计算调号、拍号、音高、音程与时值，终止类型、表现解释和风格相似度仍需要人工或独立 Agent 复核。上方简化低音必须作为待核验草稿处理。

### 来源

- [Mutopia: K. 457 first movement](https://www.mutopiaproject.org/ftp/MozartWA/KV457/sonata1/)：公有领域；排版依据 Schirmer 1918 与 Breitkopf & Härtel 1878。
- [Open Music Theory: Introduction to sonata theory](https://openmusictheory.github.io/SonataTheory-intro.html)
- [Open Music Theory: Harmonic functions](https://openmusictheory.github.io/harmonicFunctions.html)
