<!-- music-kb:page {"id": "page.6bc70baadb505b3bacedf0ed86ed778b"} -->
<!-- knowledge: composer.beethoven.symphonies.rhythm-cell-to-boundary -->
# 一个节奏核怎样改变段落功能

<!-- aliases: rhythm cell, 节奏核, motive, 动机, phrase boundary, 段落边界, pedal, 持续音, confirmation, 调性确认, Symphony 5, Symphony 6 -->

写短动机时，真正有用的变化不是把同一个音型反复粘贴，而是改变它的句法任务。它可以启动一句话、被延长成停顿、在属持续音上积累压力，最后由主和弦回答。下面先列出可迁移的条件，再用新写模型演示。

来源入口是 Eastman 对第一、五、六交响曲的乐章导航：第一交响曲以带降七级的 C 大调和弦和慢引子延迟主调稳定；第五交响曲把首乐章短单元带过段落并在第三乐章连续进入大调终章；第六交响曲以第三至第五乐章连续展示多乐章整体。这些说法分别属于导听和结构概述，不提供“贝多芬总用错调开始”之类的通则。[项目导言](https://www.esm.rochester.edu/beethoven/)；[第五](https://www.esm.rochester.edu/beethoven/symphony-no-5/)；[第六](https://www.esm.rochester.edu/beethoven/symphony-no-6/)。

## 机制

**先造不稳，再确认主调。** 不稳定可以由和声、节奏停顿、织体空缺或正式引子造成；后面必须回应先前的问题，否则只是一个孤立的怪和弦。

**保持可辨识层，改变结构层。** 记录音高轮廓、时值比例、强拍位置、声部和配器哪些保持不变。若每层同时变化，听者得到新材料；若全部不变，推动只像复制。

**用边界事件连接段落。** 延长音、休止、属持续和音色转换都能让新段开始，但边界仍需由调性、节拍或声部关系确认。连续进入不是抹掉乐章边界。

**让配器参与结构。** 木管从背景进入主题、中低音区承接旋律、极端音区、突变力度和静默都可能改变段落重心。这些效果应按作品取证，不能只凭“扩大管弦乐”概括。

<!-- opusloom:example {"id": "beethoven.model.symphony-rhythm-to-boundary", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["esm-symphony-1", "esm-symphony-5", "esm-symphony-6"], "rights": "原创教学模型；未引用贝多芬原曲音符、谱例图像或现代版本。", "source_locator": "节奏核处理为新写练习。历史观察分别定位于 Eastman 第一交响曲首乐章分析、第五交响曲动机与第三乐章连接段、第六交响曲乐章标题/连续处理；模型不是这些原谱转写。", "context": "两声部新写节奏模型：四短—一长先作动机，后用延长音制造边界，再以属持续接主和弦确认中心。说明动机改变功能的操作，不仿作任何交响曲。"} -->
```lilypond
\version "2.26.0"
\language "english"
upper = \relative c'' {
  \key c \minor \time 2/4
  c16 c c g16 g4 | af16 af af f16 f4 |
  g4~ g8 r8 | c,16 c c g16 g4 |
  a8 g8 f4 | d4~ d8 r8 | <c e g>2 |
}
lower = \relative c {
  \key c \minor \time 2/4
  c4 g4 | af2 | g2 | c,4 g'4 |
  f8 ef8 d4 | g2 | <c e g>2 |
}
\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \clef bass \lower }
  >>
  \layout { }
}
```

第 1–2 小节高声部各以四枚十六分音符启动，再落到四分音符；第 4 小节重现首个节奏型。第 3 小节高声部延音后休止，低声部留在 G，形成局部停顿；第 4 小节低声部由 C–G 支撑重新进入。第 6 小节是 G–D 开放五度，第 7 小节落到 C–E–G 大三和弦，改变局部调式色彩。前一小节没有 B 自然，所以这里只称开放五度到大调主和弦的收束，不认定完整常规 V–I 终止。

## 迁移方法

1. 写出一枚不超过一拍的核心单元，并标出它最可辨识的一项关系。
2. 第一次变化只保留该关系，改句尾、声部或和声目标。
3. 在需要分段的位置删去一部分音符，让延长音或休止制造未完成感。
4. 用属持续、开放五度或音色变化准备确认，再明确写出主和弦与进入声部。
5. 反向检查：如果把停顿改成强拍齐奏、渐强或别种持续音，段落功能是否随之改变。

模型不证明贝多芬写过这些具体音符，也不证明具体历程可以直接映射为叙事标题。用于真实作品时应补总谱版本、乐章、小节和配器。
