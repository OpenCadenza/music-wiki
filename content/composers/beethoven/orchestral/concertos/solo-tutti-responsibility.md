<!-- music-kb:page {"id": "page.f34a173b1d115fcead12f215f3a92a6c"} -->
<!-- knowledge: composer.beethoven.concertos.solo-tutti-responsibility -->
# 独奏与乐队：让回答拥有新的信息

<!-- aliases: solo, tutti, 独奏, 乐队, concerto, 协奏曲, dual exposition, 双重呈示, responsorial, handover, 责任转移 -->

写协奏曲时，不用每一轮都重复完整主题。更有效的做法是让独奏和乐队在同一事件中承担不同责任：一方提出轮廓，另一方改句法、换音区、缩短动机、延迟终止或继续维持背景。判断“协奏性”时，记录谁先陈述、谁确认调性、谁推动过渡、谁拥有终止。

## 来源与机制

Scalfaro 对 Op.37 第一乐章的分析说明双重呈示中钢琴以不同分工重述乐队材料；BSO 对 Op.73 开篇的描述是弦乐和弦先出现，钢琴以炫技材料回应；Rakochi 对 Op.56 的谱例分析则指出三个独奏者进入后，乐队更常承担段落标记、引子和归纳。三者共同支持“共享材料但改变责任”，并不支持所有贝多芬协奏曲都以对抗为主。[Scalfaro](https://cris.unibo.it/handle/11585/590769)；[BSO](https://www.bso.org/works/beethoven-piano-concerto-no-5-emperor)；[Rakochi](https://dspace.ut.ee/bitstreams/5d57eb2b-c3fb-4b99-bb29-d642b13f37b5/download)。

下面模型把过程压成三段：乐队陈述短主题；钢琴休止后移调改写；乐队加入缩短回应，最后共同落主和弦。所有音符均为新写，不对应任何作品小节。

<!-- opusloom:example {"id": "beethoven.model.concerto-transfer-and-response", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["scalfaro-pc3-first-movement-2016", "bso-pc5-swafford", "rakochi-triple-concerto-orchestra-2021"], "rights": "原创教学模型；无贝多芬原作旋律、现代版谱例或表演录音。", "source_locator": "独奏/乐队轮换的教学设计综合 Scalfaro 对 Op.37/1 双重呈示的分析、BSO 对 Op.73 开篇钢琴回应的导听、Rakochi 对 Op.56 乐队与独奏组三重协奏织体的谱例分析；模型音符为新创，不对应原作小节。", "context": "原创三段：乐队给出短主题，钢琴移调改写，乐队用缩短动机回应并完成终止。供设计独奏—乐队责任转移的练习，不是贝多芬式样复原。"} -->
```lilypond
\version "2.26.0"
\language "english"
orchestra = \relative c' {
  \key g \major \time 4/4
  g4 b d b | R1 |
  e'4^\markup { \italic "response" } d c b | <g, b d>1 |
}
piano = \relative c'' {
  \key g \major \time 4/4
  R1 | r2 g8 a b d | fs4 a d c | <g, b d>1 |
}
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Orchestra" } { \orchestra }
    \new Staff \with { instrumentName = "Piano" } { \piano }
  >>
  \layout { }
}
```

第 1 小节由乐队独奏呈示 G 大调轮廓，钢琴休止。第 2 小节乐队休止；钢琴先休二拍，再以四个八分音符单独进入。第 3 小节钢琴延续，乐队加入 E–D–C–B 作回应，进入共同段。第 4 小节钢琴与乐队同时落在 G 大三和弦，因此模型实际有“乐队—独奏—合奏”三段及共同终止。

## 迁移方法与检查

1. 先建两列，把每一拍的责任分别写在独奏和乐队下面。
2. 让第二次陈述至少改变一项：句法起拍、音区、节奏密度、和声落点或终止方式。
3. 让第三轮由另一方加入，而不是把第一段照搬；乐队最好拥有独奏没有的结构信息。
4. 安排炫技时先写华彩前后的和声目标；安排木管或弦乐独奏时，给它在音区、时值和响度上的可听空间。
5. 最后逐段检查遮蔽：如果去掉独奏后乐队仍完整陈述同一段，或去掉乐队后独奏仍独立成立，责任转移可能尚未真正发生。

## 适用边界

模型使用单行钢琴和单行乐队缩谱，没有总谱移调，也没有历史木管配置，不能直接套入真实总谱。现有来源分别集中于 Op.37 第一乐章、Op.73 导听和 Op.56 分析，不能据此推断贝多芬所有协奏曲都采用同一“冲突—和解”叙事。真实作品比较仍须记录版本、乐章、小节、乐器与华彩来源。
