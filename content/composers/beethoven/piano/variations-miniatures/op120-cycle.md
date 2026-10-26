<!-- music-kb:page {"id": "page.18ea0fc906605ccc85926d6801abc683"} -->
<!-- knowledge: composer.beethoven.op120-variation-cycle -->

# Op.120《迪亚贝利变奏曲》：变化参数与循环结构

检索词：Beethoven Diabelli Variations Op.120 迪亚贝利变奏曲 trill 转音 variation 3–7 音区 节奏 对位 草稿 循环。

**创作问题。** 主题短小、变奏很多时，怎样让变化被听见，并让相邻与远距离变奏共同形成循环？

## 来源与定位

Kinderman 指出，变奏 3–7 持续重释主题的转音：节奏、音区、对位位置与强度不同，变奏 6 的颤音成为突出实例（2021，pp. 210–213）。相邻变奏间的连接与对比，与非相邻变奏间的呼应并存；因此逐曲问“主题还剩多少”并不足够，也要问变化后的材料承担什么形式任务。Kinderman 还对照 1819 年草稿和 1822–23 年完成稿，说明编排、弃用材料和后期修改共同塑造循环（pp. 215–216）。这是有草稿依据的研究结论，不能简化成单一时间线。

Linke 的话语史研究追踪 1823 至 2016 年的分析文本，指出分析者会用主题关联、变奏分组、对比和宏观形式等不同方法。“幽默”“神秘”“崇高”属于解释及接受范畴，不是无须论证的中性乐谱事实（2021，pp. 169–180、186–188）。与 Kinderman 并读可得到写作纪律：先陈述可查变化，再说明某位作者如何解释宏观作用。

## 机制

变奏不只改旋律。转音可在不同变奏中改变节奏密度、所在音区、对位角色和强调强度；同一个音程或动机因此可能从前景手势变成低声部支撑，再成为段落的连接。判断循环时，要记录每个变化在整套中的位置，以及相邻变奏怎样建立期待或对比。

## 原创参数练习

下面不是贝多芬作品的转写。第一声部保留主题节奏和轮廓；第二声部保留轮廓但改变节奏密度；第三声部只保留终止前的级进方向。模型训练“保留—变换—弱化”的判断。若只剩共同音阶或调性，便不应声称听者一定能识别原主题。

<!-- opusloom:example {"id": "beethoven.model.variation-parameter-map", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["kinderman-diabellicycle-2021", "linke-diabellicycle-2021", "leather-op126-2005"], "rights": "原创教学模型；未引用贝多芬原谱或现代编码。", "source_locator": "自编三种参数保留模型；参照 Kinderman 对 Op. 120 的变形讨论及 Leather 对 Op. 126 局部形式/周期联系的研究。", "context": "第一行呈示材料，第二行改变音符密度，第三行只留下下行方向；比较每种保留策略的辨识力。"} -->
```lilypond
\version "2.26.0"
\language "english"

theme = \relative c'' { \key g \major \time 2/4 g8 g a b | d4 b | }
rhythmicChange = \relative c'' { \key g \major \time 2/4 g16 a g fs a8 b | d8 c b4 | }
directionOnly = \relative c'' { \key g \major \time 2/4 r4 d8 c | b8 a g4 | }

\score {
  <<
    \new Staff \with { instrumentName = "材料" } { \theme }
    \new Staff \with { instrumentName = "节奏改写" } { \rhythmicChange }
    \new Staff \with { instrumentName = "方向保留" } { \directionOnly }
  >>
  \layout { }
}
```

第一行 G–G–A–B 后跳到 D，再回到 B；第二行沿用 G 作为起点与向 A、B 上行的目标，加入 A–G–F♯ 回摆，但插入短音并改变后半段节奏。第三行只保留 D–C–B–A–G 的下行方向。依次试听或视唱，可以比较主题身份随参数减少而减弱的过程。

## 迁移与边界

模型适用于主题有清晰节奏或轮廓的情况；若识别主要靠和弦、织体或音色，应把这些维度另行纳入。写循环时，还要记录每个变奏在整套中的位置、相邻对比和远距离呼应，不能只列相同音符。此例不证明 Op.120 或 Op.126 实际采用同一程序，也不替 Linke 裁定唯一宏观分组。

来源 ID：`kinderman-diabellicycle-2021`、`linke-diabellicycle-2021`。谱例 ID `beethoven.model.variation-parameter-map` 保持不变。
