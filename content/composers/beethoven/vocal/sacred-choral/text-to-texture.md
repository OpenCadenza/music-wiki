<!-- music-kb:page {"id": "page.295c4cf6a9c4575c81b87bc1e18ccd03"} -->
<!-- knowledge: composer.beethoven.sacred-choral.text-to-texture -->
# 文本到织体：从同节奏合唱到模仿进入

<!-- aliases: homophony, 主调织体, imitation, 模仿, fugue, 赋格, choral writing, 合唱写作, text intelligibility, 字词清晰度, Credo, Amen -->

合唱写作先确定固定文本的结构、句法和仪式功能，再决定独唱、合唱与乐队何时同声、轮流、模仿或相互制衡。密集复调可以积累动能，也会降低字词清晰度；织体转换应有结构理由。

Drabkin 的 Op.123 章节把弥撒文本作为形式分析起点，并说明 Gloria 与 Credo 的 Amen 采用赋格，联系到礼仪传统；Brundage 对 Credo 的具体研究列出重复主旨、调性段落和双重赋格。Eastman 对第九终曲只提供器乐回顾、独唱合唱进入和席勒文本的导航。三种材料支持的共同操作是“先分段、再选织体”，不证明每段赋格都等于晚期复调风格证明。

## 原创模型

下面四部短例使用新创 C 大调主旨。第 1 小节四部同节奏陈述；随后女低音、男高音和低音相隔一小节依次模仿。模型没有对题、转调或完整终止规划，不复现 Credo 或 Amen 的真实主题。

<!-- opusloom:example {"id": "beethoven.model.choral-homophony-to-imitation", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["drabkin-missa-solemnis-1991", "brundage-missa-credo-2011", "esm-symphony-9"], "rights": "原创教学模型；不含弥撒或交响曲真实主题、礼文谱例图像或校勘版内容。", "source_locator": "模型用新创 C 大调短音型解释同词同节奏与模仿进入的差异。历史依据仅为 Drabkin 对 Amen 赋格传统及声部文本关系的概述、Brundage 对 Credo 双重赋格的具体研究、Eastman 对第九交响曲合唱终曲的导航。", "context": "原创四部短模型；同一主旨先同节奏齐唱、再逐声部模仿。说明纹理变化如何建立层次，不复制任何贝多芬主题、文本或具体赋格。"} -->
```lilypond
\version "2.26.0"
\language "english"
soprano = \relative c'' {
  \key c \major \time 4/4
  c4 d8 e g4 e | a,4 g f e | g4 a b g | c2 d2 | c1 | c1 |
}
alto = \relative c' {
  \key c \major \time 4/4
  c4 d8 e g4 e | R1 | c4 d8 e g4 e | d2 c2 | e2 c2 | e1 |
}
tenor = \relative c {
  \key c \major \time 4/4
  c4 d8 e g4 e | R1 | R1 | c4 d8 e g4 e | g2 f2 | g1 |
}
bass = \relative c {
  \key c \major \time 4/4
  c4 d8 e g4 e | R1 | R1 | R1 | c4 d8 e g4 e | c1 |
}
\score {
  \new ChoirStaff <<
    \new Staff { \soprano }
    \new Staff { \alto }
    \new Staff { \clef "treble_8" \tenor }
    \new Staff { \clef bass \bass }
  >>
  \layout { }
}
```

第 1 小节四部以八度或同音区移位齐奏同一节奏与轮廓 C–D–E–G–E；第 2 小节女高音独自唱新句。第 3 小节女低音在女高音声部下方模仿，第 4 小节男高音、第 5 小节低音依次进入，三次入口均相隔一小节。第 6 小节各部停在 C、E 或 G，组成 C 大三和弦；前面没有属和弦准备，所以不能当作完整古典终止。

增加入口会提高密度、削弱字词可辨度。实际创作需缩短文本、突出关键词或让乐器留白。女高音限定在 E4–G5，次中音为实际 C3–G3；`treble_8` 改变谱表显示，不能将输入音高再降八度。音高规则见 [LilyPond 官方说明](https://lilypond.org/doc/v2.26/Documentation/notation/writing-pitches)。

## 写作步骤与边界

1. 先完成文本分段和重音标注，再排定独唱、合唱与乐队进入顺序。
2. 每次重复指定目的：确认、扩展、回应、对比或闭合。
3. 齐唱提高字词同步；模仿积累动能并突出持续文本；交替区分叙述、祈祷和群体回应。作用由歌词与谱面证据决定。
4. 决定音域和复调密度时，同时检查换气、辅音密集区和乐队覆盖；逐段降低伴奏，比较关键词是否仍可听见。
5. 历史例记录拉丁/德语原文、版本、乐章、声部、小节与调性。新作迁移“文本先于织体”的流程，不迁移固定的贝多芬风格参数。

模型是完整编译单元，不是完整赋格，也不覆盖 Sanctus、Agnus Dei 或第九终曲的具体声部进入。Credo 的小节表仍须与 Henle 总谱独立核对。
