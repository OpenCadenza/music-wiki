<!-- music-kb:page {"id": "page.3e98c0e8bf1d5ef5be827bd140865965"} -->
<!-- knowledge: composer.beethoven.chamber.sonata.cello-piano-roles -->
# 大提琴与钢琴：先分配职责，再追踪材料

<!-- aliases: Beethoven cello sonata Op.5 Op.69 Op.102, piano cello roles, melody bass response fugue, 贝多芬大提琴奏鸣曲, 大提琴钢琴, 角色分配, 旋律低音, 回应, 赋格 -->

## 创作问题

大提琴和钢琴合奏时，怎样在同一短句里保持旋律、低音、回应和终止职责各自清楚，而不是让两件乐器从开头到结尾齐奏？

## 来源与定位

大提琴在贝多芬奏鸣曲中不只承担旋律。Bärenreiter版导言对Op.5 No.1第一乐章给出可核对的角色索引：大提琴在第1小节齐奏、第7小节领奏、第11小节作低音、第35小节作伴奏，第85小节进入对位中声部，第94小节与钢琴对话，第98小节维持持续音，且第40小节短暂休止（Cooper，导言印刷页III）。这些位置说明作曲时可在同一乐章内更换重心；它们不构成五首奏鸣曲的统一配方。

Op.69以大提琴无伴奏旋律开场。Cooper指出，Op.69第一乐章的发展部在手稿中留下密集修订：草稿已经显示整体布局，具体织体则在自笔谱阶段形成（导言印刷页III–IV）。到Op.102 No.1，头27小节可听作独立短乐章，也可听作慢引子；随后快板进入主调关系小调，慢乐章又像连接段，短暂召回开头Andante，终乐章不间断跟进。钢琴在第2–4小节回应大提琴，并把其开头若干音型重新组合到低声部（同书，印刷页IV）。Op.102 No.2则在慢乐章后直接进入赋格终乐章；钢琴可展开多声部，而大提琴仍是一条线，赋格几乎始终保持四声部数量（印刷页V）。写作时因此应分别标注旋律、低音、内声部、模仿和休止的承担者，再检验材料是否被另一件乐器重新组织。

## 机制解释

以下模型为新写的 C 大调四小节练习，不是贝多芬原谱、改编或风格认证。钢琴右手从分解和弦转为间隔式和弦回应，再转为属七和弦分解；左手给出低音方向。大提琴保持连贯旋律，但不与钢琴同节奏齐奏。它把“各自独立”和“共同终止”放在同一短句中。音名采用 LilyPond English 绝对音高：`c'` 为 C4，`c''` 为 C5，`c` 为 C3，`g,` 为 G2。

## 谱例

<!-- opusloom:example {"id": "beethoven.model.cello-piano-independent-roles", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["beethoven-barenreiter-cello-sonatas-2004"], "rights": "原创教学模型；不转录、改写或模仿贝多芬作品或现代版谱例。", "source_locator": "新写四小节C大调练习。历史对照仅为Bärenreiter导言对Op.69开头大提琴独奏及Op.102 No.1钢琴回应的说明（印刷页IV），不是本例音符来源。", "context": "大提琴演奏连贯旋律；钢琴右手负责分解和弦、和弦回应、属七和弦分解与主和弦收束，左手勾画低音。用于练习乐器任务独立与终止协调，不是贝多芬风格仿作。"} -->
```lilypond
\version "2.26.0"
\language "english"

global = { \key c \major \time 4/4 }
cello = {
  \clef bass \global
  c'4 d' e' g' |
  a'2 g'4 e'4 |
  d'4 e' f' g' |
  c'1 |
}
pianoRight = {
  \global
  e'8 g' c'' g' e' g' b' g' |
  r4 <f' a' c''>4 r4 <g' b' d''>4 |
  g'8 b' d'' f'' b' d'' f'' d'' |
  <e' g' c''>1 |
}
pianoLeft = {
  \clef bass \global
  c2 g,2 |
  f,2 c2 |
  g,2 d2 |
  c1 |
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Vc." } { \cello }
    \new PianoStaff \with { instrumentName = "Pno." } <<
      \new Staff { \pianoRight }
      \new Staff { \pianoLeft }
    >>
  >>
  \layout { }
}
```

## 逐小节核对与迁移

本例的编译结果登记在批次核验中；语法通过不认证历史解释、演奏可行性或声部平衡。

### 逐小节核对与迁移边界

- **第1小节：** 大提琴以C4–D4–E4–G4四个四分音符提出连贯旋律；钢琴右手用八分音符分解C大调音型，左手C3与G2各占二分音符。两手与大提琴的节奏不同，钢琴既保持和声活动又给旋律留出空间。
- **第2小节：** 大提琴A4二分音符后接G4、E4；钢琴右手在第2、4拍各奏一个四分和弦，中间留空，左手F2–C3支撑。其功能是间歇回应，不是逐音模仿Op.102 No.1。
- **第3小节：** 大提琴D4–E4–F4–G4继续四分音符线；钢琴右手连续分解G7音集合G4–B4–D5–F5，左手G2–D3建立属功能。钢琴此处承担更主动的和声推动，大提琴仍保有自己的旋律方向。
- **第4小节：** 大提琴C4全音符与钢琴C大三和弦、C3低音共同收束；前小节G7到本小节C大调构成模型内可听的V7–I。此模型的明确属七和弦不用于推论历史作品终止。

练习时可交换第2小节的发起者，让钢琴先呈示材料而由大提琴接续；也可把第1小节钢琴分解音型移交给大提琴，观察独立低音是否仍清楚。若两件乐器在同一音区、同节奏重复，角色分工会消失；若钢琴和弦过密或过响，大提琴线条可能被遮蔽。实际演奏仍需按速度、弓法、踏板和声学条件调整，四小节模型没有模拟这些条件。

## 适用边界

来源 ID：`beethoven-barenreiter-cello-sonatas-2004`（导言实读）、`bonds-op95-jams-2017`（在线正文选节）、`november-theatrical-quartets-excerpt-2014`（仅索引片段，用于背景）。

模型是新写的四小节 C 大调练习，不是贝多芬原谱、改编或风格认证。文献部分只支持 Op.5/69/102 的角色与稿本索引，不能由此概括所有大提琴奏鸣曲。
