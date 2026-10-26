<!-- music-kb:page {"id": "page.ff596fa9916450dcb1e096325024c75b"} -->
<!-- knowledge: composer.beethoven.chamber.quartet.op18-opening -->
# Op.18 No.4 开头：旋律持续与脉动低音怎样并存

<!-- aliases: Beethoven Op.18 No.4, C minor quartet opening, string quartet texture, pulsed bass, 贝多芬弦乐四重奏, Op.18之4, C小调, 开头, 声部, 脉动低音 -->

## 创作问题

四重奏开头同时出现长音旋律、邻音装饰和重复低音时，声部怎样避免挤成同一种动作？这一段提供可直接核对的声部职责：上声部组织旋律与句尾，大提琴维持脉搏，中声部补充和声运动。

## 来源与定位

Tompkins 用 Heinrich Koch 的句法理论分析 Op. 18 若干首第一乐章（2006，PDF pp. 56–89、100–109）。他对 Op. 18 No. 3 追踪短句单元的顺序移位、交叠和逐渐加快的调性运动；分析指出，这些局部语句参与更大的奏鸣曲形式功能，而非彼此孤立的旋律片段。对 No. 1，他讨论两小节节拍推进如何遭遇 hemiola、休止与乐句扩张。此处 Koch 是分析视角，不是贝多芬直接受到 Koch 理论影响的证据。转用于新四重奏时，应问每个声部怎样参与句尾、重拍和调性抵达，而不只标注主题出现次数。

以下是 Mutopia 公有领域类型稿开头弱起后两个完整小节的重新转写，来源为 Breitkopf & Härtel 1862–65 版，原稿 LilyPond 2.7.40（Mutopia-2006/07/30-790）。新代码以 LilyPond 2.26.0 重录首四件乐器的音高和时值；保留弱起和装饰音，删去力度、弓法、反复、版面及后续音乐。它是短例转写，不是现代校勘版，也不替代完整声部核对。

## 谱例

<!-- opusloom:example {"id": "beethoven.op18no4.quartet-opening", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["mutopia-beethoven-op18no4-m1"], "rights": "贝多芬作品及 Mutopia 类型稿由类型者声明置于公有领域。本例为 OpusLoom 从 Mutopia-2006/07/30-790 的 LilyPond 2.7.40 文件重新转写的短摘录，保留来源署名；未复制原文件版面/语法，删去力度、弓法与反复。", "source_locator": "Beethoven, String Quartet in C minor, Op. 18 No. 4, I, upbeat and mm.1–2; Mutopia-2006/07/30-790; source Breitkopf and Härtel 1862–1865; maintainer/typesetter Stelios Samelis.", "context": "四声部音高及时值转写，保留四分音符弱起与首两小节，略去表情标记及反复。以原稿核对音高/时值；不是整份现代校勘谱。"} -->
```lilypond
\version "2.26.0"
\language "nederlands"
global = { \key c \minor \time 4/4 }

vOne = {
  \global
  \partial 4 g4 |
  c'2 ~ c'8 \grace { d'16[ c' b] } c'8( ees' d') |
  d'2( c'4) c'4 |
}
vTwo = {
  \global
  \partial 4 r4 |
  g2. b4 |
  b2( g4) r4 |
}
viola = {
  \global
  \clef alto
  \partial 4 r4 |
  ees2.( f4) |
  aes4.( f8) ees4 r4 |
}
cello = {
  \global
  \clef bass
  \partial 4 r4 |
  c,8 c c c c c c c |
  c8 c c c c c c c |
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Vln. I" } { \vOne }
    \new Staff \with { instrumentName = "Vln. II" } { \vTwo }
    \new Staff \with { instrumentName = "Vla." } { \viola }
    \new Staff \with { instrumentName = "Vc." } { \cello }
  >>
  \layout { }
}
```

## 机制解释

首个完整小节中，第一小提琴把 C 小调主和弦音拉成长线，并以倚音/邻音装饰其回返；第二小提琴在G上延长后升至B自然（原码b，不是bes），中提琴从 E♭ 延展至 F，大提琴则连续重复 C。第二小节上声部相继收束，而大提琴仍维持同音八分音符脉动。这个局部结构显示旋律持续音与脉动低音可同时存在；具体全乐章句法要结合 Tompkins 对其他 Op. 18 首乐章的理论分析和更长原谱范围，不把两小节直接推广为 Op. 18 的通则。

## 迁移方法

先分别标出“长音持有者、装饰活动、脉动低音、句尾落点”，再写四声部。若要把材料交给另一件乐器，同时改变音区或节奏分组，让听者能辨认职责已经改变。真实短例只覆盖弱起后两个完整小节，不能据此写成 Op.18 全部作品的固定织体规则。

## 来源与边界

来源 ID：`tompkins-op18-2006`、`mutopia-beethoven-op18no4-m1`。Mutopia 类型稿来自 Breitkopf & Härtel 1862–65；短例删去力度、弓法、反复与版面，不是现代校勘版。
