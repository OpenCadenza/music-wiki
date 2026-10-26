<!-- music-kb:page {"id": "page.fb4aa67ecc66517ca1ecb14831327433"} -->
<!-- knowledge: composer.beethoven.chamber.quartet.voice-handoff -->
# 四重奏声部接力：何时是交接，何时只是重复

<!-- aliases: Beethoven quartet voice handoff, 弦乐四重奏声部接力, 主题传递, 声部重叠, texture change, Op.18, Op.135 -->

## 创作问题

短动机依次由第一小提琴、第二小提琴和中提琴接手时，怎样让听者听见“材料被交接”，而不是四件乐器重复同一句？

## 来源与定位

## 自编模型：四重奏织体中的接力与重叠

下例为原创教学模型，不引用贝多芬原谱。三件上声部弦乐轮流呈示短节奏材料，低音提供持续支撑，再让第一与第二小提琴重叠，形成独立线条交汇。它训练“主题传递”和“织体改变”两项观察。此手法适用于能由不同音区/音色辨认的短句；若声部都挤在同一音区、同一节奏，接力会听成齐奏。失败征兆是每个声部都仅重复主题而没有后续回应，或低声部的持续音让和声方向含糊。演奏前还需考虑弦乐发音、弓法与实际平衡；谱例本身不能证明可听性。

## 谱例

<!-- opusloom:example {"id": "beethoven.model.quartet-voice-handoff", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["tompkins-op18-2006", "britton-op135-2008", "shapiro-violin-sonatas-2016"], "rights": "原创教学模型；不使用贝多芬作品或现代编码。", "source_locator": "自编声部接力模型；借鉴研究中对 Op. 18 句法/四重奏声部及 Op. 135 动机角色的分析问题，不转录其音乐。", "context": "三件上声部弦乐先后进入，第三小节重叠；大提琴持续作低音；用于观察材料传递后音区和织体关系如何变化。"} -->
```lilypond
\version "2.26.0"
\language "english"
global = { \key c \major \time 4/4 }
vOne = \relative c'' { \global c8 d e g e4 d | c2 e4 d | g2 e2 | }
vTwo = \relative c'' { \global R1 | g8 a b d b4 a | g2 f2 | }
viola = \relative c' { \global \clef alto R1*2 | e8 f g b g4 f | }
cello = \relative c { \global \clef bass c2 g | c,1 | c2 g | }
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Vln. I" } { \vOne }
    \new Staff \with { instrumentName = "Vln. II" } { \vTwo }
    \new Staff \with { instrumentName = "Vla." } { \viola }
    \new Staff \with { instrumentName = "Vc." } { \cello }
  >>
  \layout {}
}
```

## 机制解释

第一小提琴先在 C 大调呈示 C–D–E–G 的上行轮廓，第二小提琴第二小节将材料移至 G–A–B–D；中提琴第三小节接过材料，大提琴则以 C/G 支持调性。第2–3小节的交接改变材料持有者；大提琴先用全音符C，后改为C–G二分音符，低音节奏确有变化，但仍限于C/G音级，未建立新调性。若要推动形式边界，下一步可改变低音，或让接力结束在新的属和弦；不能只靠添加更多音符制造推进。

## 迁移方法

固定短动机的音程或节奏身份；每换一次持有者，至少改变音区、进入拍位、伴奏密度或低音功能中的一项。第三小节让声部重叠时，要保留可辨认的线条，同时检查大提琴是否仍在支撑调性。

## 适用边界

这是原创教学模型，不引用贝多芬原谱。若所有声部同音区、同节奏重复，接力会退化为齐奏；若低音只持续 C/G，推进感也会停在织体层。谱例通过语法不等于已经验证实际弦乐平衡。

## 来源

`tompkins-op18-2006`、`britton-op135-2008`、`shapiro-violin-sonatas-2016`。它们分别提示句法、动机—调性关系与双乐器职责问题，不提供本模型的音符。
