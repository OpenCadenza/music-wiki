<!-- music-kb:page {"id": "page.58e64ede933a41519460ef2e002085df"} -->
<!-- knowledge: composer.haydn.thematic-treatment -->
# 海顿室内与交响的主题处理：重述何时成为结构事件

海顿的主题究竟靠什么维持同一性？只比较旋律轮廓往往得到两个相反的错误答案：要么把一个短音型重复出现当成“动机统一全曲”，要么把第71小节没有在D大调出现写成曲式失败。Op. 33 No. 6第一乐章和“Military”交响曲No. 100提供了更有用的比较。前者让开场材料在属调重新出现，随后才处理主调闭合；后者先在呈示部用类似主部的材料拖延副部，再在再现和后续乐章里反复使用♭VI。两例的共同点不是固定曲式，而是**材料、功能、调性位置三件事被拆开重组**。

本章使用Open Music Theory的P、TR、S、C功能作为描述工具，并以Timothy Mastic对两部作品的具体分析检验。术语是分析接口，不是海顿时代已经统一使用的作品说明书。

## 同一材料，不同职责

Op. 33 No. 6第一乐章开场不是一条连续咏唱。短小的跳跃、收束和停顿把四音型拆成几块，听者先得到“话题”，还没有得到稳定句法。Mastic记录的关键结构决定在第71–81小节：再现并未立刻让主部主题与主和弦同时返回，开场材料先进入属调，再在后续过程中回到主调。Schematic sonata labels会把这一处判成异常；历史与过程分析则要问，这种错位建立了什么可辨认关系。

Mastic对此给出两项证据。第一，属调开场保留了主部主题的音高—节奏外形；第二，紧随其后的主调转向继续完成再现职责。因而，“没有双返回”不能直接等于“没有再现”。主题辨识回答“这是什么材料”，调性与终止回答“它现在做什么”，两层可以暂时不同步。海顿让听者先认出旧话，再听到它被放到新位置。

“Military”交响曲No. 100把同一原则扩展到更长的跨度。Mastic分析其第一乐章时指出：第72–85小节附近的属调主部材料看似可作副部，却在结束、分裂和第二次过渡中暴露出“不够像副部”的问题；另一组材料才取得更完整的副部职能。也就是说，同一轮廓进入新调并不必然取得新主题功能。到了再现，海顿又重排呈示部的材料块，并在第239–252小节突出♭VI。这个和弦并非凭空出现：引子、过渡、发展和第二乐章都有它先前或后续的支点。

| 结构问题 | Op. 33 No. 6第一乐章 | Symphony No. 100第一乐章 |
| --- | --- | --- |
| 旧材料在哪重返 | 第71小节起先进入属调 | 属调、再现和尾声多次重组主部/过渡材料 |
| 什么保持辨识 | 开场的音高—节奏单元 | 主部材料可被缩短、移位并置于不同织体 |
| 什么改变功能 | 属调开场先充当多重可能，再被主调过程解释 | 看似副部的重复材料继续过渡；另一材料完成更稳定的副部职责 |
| 什么形成全曲联系 | 旧主题错位与后文解决 | ♭VI在乐章内反复，并在第二乐章继续得到回声 |
| 不能由短例证明的事项 | 完整四声部的每小节连接 | 第239–252小节以外每一处♭VI的同等地位 |

### 谱例一：开场材料与属调返程

下面只录入第一小提琴的旋律，不重做完整四声部，也不复制现代编辑版的排版。第一行呈现八分音符弱起加第1–4完整小节（弱起不计小节号）；第二行按Mastic明确报告的Op. 33 No. 6第71–74小节属调陈述作等音程移写。它是待复核的分析简化草稿；尚未锁定历史扫描版次、编者与出版信息，也未完成两处逐音对照，Mastic的分析定位不能替代一手谱面核验：节奏和单声部轮廓用于比较，其他弦部、配器变化和后续终止必须回到全谱。

<!-- opusloom:example
{
  "id": "haydn.op33no6.displaced-return",
  "status": "draft",
  "source_version": "2.26.0",
  "target_version": "2.26.0",
  "compile": "score",
  "midi": false,
  "requires": [],
  "sources": [
    "imslp-haydn-op33",
    "haydn-mastic-normative-wit",
    "omt-sonata-exposition"
  ],
  "rights": "Original work public domain; independently entered short melody for analysis, with MTO source text paraphrased rather than copied.",
  "source_locator": "Haydn, String Quartet in D major, Hob.III:42 / Op.33 No.6, I, violin I anacrusis + mm.1-4 (pickup unnumbered) and dominant-return analytical transposition mm.71-74; historical edition not yet locked",
  "context": "单声部分析简化：比较开场D大调轮廓与Mastic所述属调再现开头。第二行省略其余三声部。"
}
-->
```lilypond
\version "2.26.0"

theme = \relative a'' {
  \time 6/8
  \partial 8 a8
  a8( d) b-. a-. r-. a-. |
  a8( g fis) e-. r-. g |
  g8( fis e) d-. r d |
  e4( fis8) d-. r4 |
}

exposition = {
  \key d \major
  \theme
}

recapitulation = {
  \key a \major
  \transpose d a { \theme }
}

\score {
  <<
    \new Staff \with { instrumentName = "Vln. I, mm. 1-4" }
    { \exposition }
    \new Staff \with { instrumentName = "Vln. I, mm. 71-74" }
    { \recapitulation }
  >>
  \layout { }
}
```

第1–2小节的A–D跳进建立D大调的中心音区，B–A的回落和E–D的级进使短句像一次结束又立即重启。第3小节转到E–D—同一旋律骨架落在较低支点；第4小节以E–F♯–D收束。移入A大调后，同一关系变为E–A、F♯–E等，听者追踪的是音程轮廓与节奏位，而不是绝对音高的复制。代码中的第二行不能证明所有声部都原样移调；它只使Mastic报告的单声部关系可读。

## 跨段组织不等于“主题越多越好”

“Military”交响曲的结构价值也不在最著名的鼓点，而在一个短促材料经过不同功能位置后仍能被识别。Mastic的阅读把几次♭VI出现连成“失配后得到解释”的链条：引子先种下它，发展部让它在新的调性背景中占有空间，再现又把预期终止推开，第二乐章再提供跨乐章回想。这里需要两种记录。

1. **局部记录**：这一秒发生了什么和声、音区、声部交接或终止？
2. **长篇记录**：该事件与哪些先前位置对应，后文有没有让它获得新意义？

只做第一层，会把每个意外写成“戏剧性”；只做第二层，则容易把任何重复音程追成全曲网络。两者必须由可复核位置连接。

### 谱例二：把♭VI写成可检查的回返轴

第二组是自编教学模型，不含Op. 33或Symphony No. 100的原创旋律。模型故意只用一个四音单元、一个伴奏轮廓和一个♭VI区段，展示“材料重复而功能改变”的写法：A区的短促单元先在主调建立；B区保留节奏和音程核心，却让和声离开主调；C区重新出现同一单元，并由终止确认回来。这个模型教的是检查顺序，不能作为海顿原句或实际曲式证据。

<!-- opusloom:example
{
  "id": "haydn.model.flat-six-return-axis",
  "status": "published",
  "source_version": "2.26.0",
  "target_version": "2.26.0",
  "compile": "score",
  "midi": false,
  "requires": [],
  "sources": [
    "haydn-mastic-normative-wit",
    "omt-sonata-exposition"
  ],
  "rights": "Self-authored teaching model; no Haydn melody is reproduced.",
  "source_locator": "New six-measure model inspired by Mastic's analysis of recurring flat submediant contexts, not a transcription of Symphony No. 100",
  "context": "自编教学模型：先建立短单元，再经♭VI区段返回主调；用于设计跨段检查表。"
}
-->
```lilypond
\version "2.26.0"
upper = {
  \key c \minor \time 4/4
  \mark \markup { \italic "A: cell" }
  c''8 d'' ees'' g'' f''4 r4 |
  ees''4 d'' c'' g' |
  \mark \markup { \italic "B: flat VI" }
  \key aes \major
  aes'4 c'' ees'' c'' | bes'2 aes'2 |
  \mark \markup { \italic "C: return" }
  \key c \minor
  c''8 d'' ees'' g'' f''4 d''4 | b'2 c''2 |
}
lower = {
  \clef bass \key c \minor \time 4/4
  c2 f,2 | aes,2 g,2 | aes,2 ees2 | ees2 aes,2 |
  c2 f,2 | g,2 c2 |
}
\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \lower }
  >>
  \layout { }
}
```

模型第1–2小节在C小调提出C–D–E♭–G单元；第3–4小节以A♭大调区域改变语境；第5–6小节回到C小调，由低音G2–C3和上方B4–C5完成本模型的终止。以C为基准，♭VI是A♭；原《军队》交响曲以G为主调，相应的♭VI为E♭。迁移保留的是级数关系，并非原样搬用音名。此例不冒充海顿原作和声。

## 可迁移的写作流程

1. 先把候选材料写成三行参数：音高轮廓、节奏姿态、和声/低音支点。只共享其中一行时，暂称“关联”，不要先叫“主题再现”。
2. 列出材料的四次位置：初次建立、偏离、误认、最终解释。每次记录所在段、调性、长度和终止。返回若没有改变职责，只是 literalism。
3. 若要让材料在新调开始，先保留一个高辨识参数，再写出两个后续选择：转入主调完成，或拒绝主调而制造进一步发展。两条都要有终止计划。
4. 检查反向影响。偏离段是否在返回时被重新解释？若后文完全不需要先前材料，所谓统一就只剩表面相似。
5. 用完整段落而非开头几小节验收。短例可以证明局部音高关系，不能代替对展开部、再现部和尾声的实际分析。

## 反例与证据边界

- 单调性不是“只有一个主题”。Mastic与Open Music Theory都强调材料复用和新调、终止功能的结合；副部仍可有自己的主题类型和终止任务。
- 属调再现不是自动的“假再现”或结构错误。它与更早的二部歌曲/二部结构传统有关；判断取决于后续怎样回主调、怎样闭合。
- ♭VI的每次出现未必同义。一个和弦可承担色彩、转调支点或延误终止；“都表示命运”之类的统一叙事没有谱面依据。
- Mastic对第239–252小节提出的是一种有文本和谱面支持的解释，不是海顿本人留下的创作说明。本章保留该解释归属，不把它写成不可争议的事实。

## 来源

- Mastic, “Normative Wit: Haydn's Recomposed Recapitulations,” *Music Theory Online* 21.2 (2015)，§3.1–3.10与§4.1–4.10：[文章](https://mtosmt.org/issues/mto.15.21.2/mto.15.21.2.mastic.php)。
- Open Music Theory, “Sonata form – thematic modules”：[教材](https://openmusictheory.github.io/sonataThematicModules.html)。
- IMSLP, [String Quartets, Op. 33](https://imslp.org/wiki/String_Quartets,_Op.33_(Haydn,_Joseph))：作品编号与多版本目录；所选scan的逐音比对仍待独立审稿。

两个新来源ID与许可记录见[中央来源表](../../knowledge/sources.json)。本页示例为`draft`，需由主代理合并来源表并完成独立谱面复核后方可进入生成知识库。
