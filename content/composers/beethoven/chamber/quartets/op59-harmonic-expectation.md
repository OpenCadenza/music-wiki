<!-- music-kb:page {"id": "page.20c92d5bad9b50cca92a8db4c1d49a78"} -->
<!-- knowledge: composer.beethoven.chamber.quartet.op59-expectation -->
# Op.59 No.3：六四、减七与属七怎样制造局部期待

<!-- aliases: Beethoven Op.59 No.3, Rasumovsky quartet, harmonic expectation, six-four, diminished seventh, G7, 贝多芬拉祖莫夫斯基四重奏, 六四和弦, 减七和弦, 属七, 弱拍强拍 -->

## 创作问题

慢引子中的六四和减七，为什么可能让听者期待一个尚未到达的落点？快板里的弱拍 C 接到强拍 G7 时，又怎样利用前面的语境改变局部重量？

## 来源与定位

Op.59 No.3第一乐章提供中期四重奏中“局部聆听预期可以与单一背景归纳并存”的具体入口。辛辛那提大学硕士论文 Brown 第31–32页转述 Hatten：慢引子 mm.20–22 的减七和弦包围小调六四和弦，C外声部的同音级扩展（语料抽样为C2至C6，四个八度）和缓慢节奏使六四具有 F 小调终止期待；快板 m.31 弱拍 C 接强拍 G7，因拍位及此前语境而显得新奇。此处论点只可引作 Brown 对 Hatten 的转述；Brown 的论文主题是柴可夫斯基第五交响曲，Hatten 1980 原文尚未读到。DCML 的第一乐章抽样和弦标注 viio65–iv64–viio7、音高记录 C2–F3–A♭4–C6，可作局部交叉核对；它是语料标注，不是专论，且版次对应尚未确认。

## 机制解释

教学操作可要求读者先标记每个实际和弦、低音、外声部和拍位，再写出至少两种可能听法；慢速持续的六四是否承载终止期待，应由持续时长和前后和声说明，不能套“六四必不稳定”一条规则。之后才比较还原：若还原把六四和相邻减和弦一并压为装饰，检查它是否因此抹去了快板 m.31 的预期落点。该步骤迁移到其他奏鸣曲式开端时，失败条件是乐谱版次/编号未核、实际节拍不支持“弱—强”对照，或六四持续时间不足以形成相似预期；不得仅凭同类和弦就套用 F 小调读法。

## 谱例

以下谱例是原创课堂模型，非贝多芬作品或仿作，不取自 DCML。它只把“F 小调六四环境—减七和弦—弱拍 C 到较重拍 G7”的机制抽象成四小节；音高和时值都由代码明确给出。

<!-- opusloom:example {"id": "beethoven.model.op59-ambiguity-toy-001", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["brown-cincinnati-thesis-2007", "dcml-annotated-beethoven-corpus-op59-3-mv1"], "rights": "原创教学模型；不是贝多芬原谱，不复制DCML编码或文献图示。", "source_locator": "原创四小节模型；历史论点仅为Brown印刷pp.31–32对Hatten的二手转述，DCML抽样为n09op59-3_01的mm.20–22。", "context": "F小调六四音响、减七和弦、第二拍C到第三拍G7的课堂模型；不证明Op.59的历史听法或具体版本。"} -->
```lilypond
\version "2.26.0"
\score {
  \new PianoStaff <<
    \new Staff \with { instrumentName = "Upper" } {
      \key c \major \time 4/4
      <c' f' aes'>1 |
      <b d' f' aes'>1 |
      r4 c'4 <g b d' f'>2 |
      <c' e' g'>1 \bar "||"
    }
    \new Staff \with { instrumentName = "Bass" } {
      \clef bass \key c \major \time 4/4
      c1 | b,1 | r4 c4 g,2 | c1
    }
  >>
  \layout { }
}
```

## 逐小节核对

逐小节读：第1小节 C 低音托住 F–A♭–C，构成 F 小调第二转位色彩；这只是模型中的悬置声响，没有宣称完整终止。第2小节 B–D–F–A♭ 转为减七和弦。第3小节第一拍休止，C 在第二拍进入，G7 在第三拍落下，因此谱面确实表现 C 弱拍先现、G7 随后落在更重拍；G7 的功能听向需靠听者的调性上下文判断。第4小节 C 大三和弦给出一个可能去向，但模型没有复制历史材料，也不证明贝多芬原曲如何被听见。

## 迁移方法

先标明实际和弦、低音、外声部和拍位，再写出至少两种可能听法；只有持续时长、前后和声和重拍位置都支持时，才把六四或弱拍进入写成“期待”。改变其中一项，可作为反例测试。

## 适用边界

来源 ID：`brown-cincinnati-thesis-2007`、`dcml-annotated-beethoven-corpus-op59-3-mv1`。未读Hatten原文，不把此节列为独立的一手Op.59专论。 Hatten 原文尚未实读；Brown 对 Hatten 的转述与 DCML 抽样是不同证据层级，不能合并成一手专论。
