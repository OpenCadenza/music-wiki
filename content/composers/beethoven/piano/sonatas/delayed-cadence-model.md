<!-- music-kb:page {"id": "page.7fb9e4fb013157db96d0ceb190a5e354"} -->
<!-- knowledge: composer.beethoven.piano.delayed-cadence -->

# 主题提示与延迟收束

检索词：Beethoven piano sonata delayed cadence 延迟终止 主题提示 motive expectation 句法 扩张 原创模型 Op.10 Op.31 Op.53。

**创作问题。** 保留开头的节奏钩子时，怎样把两小节模型延长成四小节，并让延长承担新的句法任务？

## 任务与机制

模型完全自编，不含贝多芬原作旋律。A 的首小节以 G–G–E–G 建立节奏钩子，C–B–A 向 G 回落，第二小节停在属音 G 并留白。B 保留相同起句，第二小节继续上行至 D，再逐步下行；E 长音改变最终旋律落点。变化不在“更长所以更贝多芬”，而在同一动机进入延长的句法后，收束被推迟，听者的期待变得更具体。

<!-- opusloom:example {"id": "beethoven.model.piano-form-expectation", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["beethoven-hepokoski-tempest", "beethoven-boss-op10-1", "beethoven-igoa-functional-harmony"], "rights": "原创教学模型；不引用贝多芬原谱或现代谱面编码。", "source_locator": "原创模型；参照 Hepokoski 对 Op. 31 No. 2 形式进程的讨论、Boss 对 Op. 10 No. 1 的分析及 Igoa 对 Op. 53 I mm.18–38 的和声功能分析。", "context": "A 展示短动机与明确收束；B 保留节奏身份，延长旋律并改变停止时点；未配低音，不证明属和声延长。不是任何贝多芬作品的转写。"} -->
```lilypond
\version "2.26.0"
\language "english"

theme = \relative c'' {
  \key c \major \time 4/4
  g8 g e g c4 b8 a | g2 r2 |
}

delayed = \relative c'' {
  \key c \major \time 4/4
  g8 g e g c4 b8 a | g4 a8 b d4 c8 b | a4 g f2 | e1 |
}

\score {
  <<
    \new Staff \with { instrumentName = "A: 收束" } { \theme }
    \new Staff \with { instrumentName = "B: 延迟" } { \delayed }
  >>
  \layout { }
}
```

## 从谱面到迁移

两行都必须保留 G–G–E–G 的节奏身份。B 的延长需要增加方向：上行到 D、级进下行、E 长音。写入完整织体时，还应核对低音和和弦配置，避免只靠旋律延长造成和声停滞。由于模型没有低音，不能把末尾 E 判成强终止。

可用四步检查：

1. A 是否在第二小节形成清楚、可记忆的停止点？
2. B 是否在第二小节明确继续，而不是重复 A 后随意追加？
3. B 的最终落点是否兑现或重释 A 建立的期待？
4. 补上低音后，是否仍只有一个主要到达点？

若 B 只是把 A 原样重复两次，长度增加没有改变期待；若 B 每两拍出现一次完整主和弦终止，听者会听到若干小结束，最终 E 长音也难以成为更大到达。有效延长通常需要一个可追踪的不解决状态：属功能持续、低音延迟、重复碎片，或旋律尚未兑现的音级。补写和声后，应先用低音与最高声部单独视唱，再决定是否加入内声部与织体。

## 适用边界

模型适用于有明确节奏身份、且和声可延长的短动机。若主题身份主要靠音色或复杂旋律，仅延迟终止可能不足以保持可辨识度。它参照三项作品研究，却不证明贝多芬使用了同一程序。

来源 ID：`beethoven-hepokoski-tempest`、`beethoven-boss-op10-1`、`beethoven-igoa-functional-harmony`。谱例 ID `beethoven.model.piano-form-expectation` 保持不变。
