<!-- music-kb:page {"id": "page.07139ccc4eda551b9d795bd65d6fa377"} -->
<!-- knowledge: composer.beethoven.variation-time-scale -->

# 主题骨架与音值变形：怎样改变时间感

检索词：Beethoven Op.120 late variation 变奏 time scale 时间感 音值 duration density 密度 骨架 Kinderman。

**创作问题。** 主题的音高方向已经明确时，怎样只改变音值密度，让同一轮廓听起来更流动，同时避免密度单向递增？

## 来源与定位

Kinderman 对《迪亚贝利变奏曲》的讨论把草稿、动机、连续性和表演解读结合起来。他比较开头转音在第 3 至第 7 变奏间的节奏、音区、对位位置与强度变化，并讨论变奏 6 的颤音（2021，pp. 210–216）。本页只迁移其中“音值变化会改变感知时间”的可操作观察；具体循环分类与 Op.111 关系仍按作者观点归属。

## 原创模型

下例原创，不转写 Op.110、Op.111 或 Op.120。它把主题的音高骨架保留在慢速长音中，以另一行较短音值改写轮廓。适用前提是主题轮廓本身可辨认；若主题依赖复杂和弦或特定音色，单声部缩短音值可能无法保留身份。

<!-- opusloom:example {"id": "beethoven.model.late-variation-time", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["kinderman-diabellicycle-2021", "linke-diabellicycle-2021"], "rights": "原创教学模型；不引用贝多芬原谱、现代谱面编码或文献图例。", "source_locator": "原创变奏模型；参数设计参考 Kinderman 对 Op. 120 动机变形与连续性的讨论（pp. 210–216），不复现其谱例。", "context": "第一行给出慢速骨架，第二行将同一音级方向改为较短音值；用于观察音符密度变化如何改变时间感。"} -->
```lilypond
\version "2.26.0"
\language "nederlands"

theme = \relative c'' {
  \key ees \major \time 3/4
  g4 f ees | bes2 g4 | aes4 g f | ees2. |
}

variation = \relative c'' {
  \key ees \major \time 3/4
  g8 aes g f ees f | bes8 c bes aes g f |
  aes8 bes aes g f ees | ees4 g bes |
}

\score {
  <<
    \new Staff \with { instrumentName = "主题骨架" } { \theme }
    \new Staff \with { instrumentName = "音值变形" } { \variation }
  >>
  \layout { }
}
```

## 机制

第一行每小节的主要落点依次为 G–F–E♭、B♭–G、A♭–G–F、E♭。第二行仍保留向下的音级方向，却把前三小节改为八分音符，第四小节回到四分音符。末尾重新扩大到四分音符，避免密度单向增加到结束。

真实作品中还应检查低音和和弦是否同时改变；若只增加表面音符，时间感未必扩张，可能只是装饰密度提高。模型采用三拍和声时间；迁移到其他拍号时，要另行标出被保留的拍点支点与和声更换频率。

## 迁移与失败检查

1. 先抄出一条不含装饰的骨架，圈出每小节主要落点。
2. 选择缩短哪几小节的音值，以及何时恢复较长音值。
3. 检查轮廓、落点和终止方向是否仍能在单独视唱时辨认。
4. 补写低音后，再判断它支持的是同一和声、替代和声，还是新的段落方向。

失败征兆包括：变奏音符密度增加但和声不变；两行旋律互相遮蔽；或末尾持续加速，使练习只剩下技法展示。这个模型不证明 Kinderman 或 Linke 提出同一分组，也不把密度变化等同于晚期风格。

来源 ID：`kinderman-diabellicycle-2021`、`linke-diabellicycle-2021`。谱例 ID `beethoven.model.late-variation-time` 保持不变。
