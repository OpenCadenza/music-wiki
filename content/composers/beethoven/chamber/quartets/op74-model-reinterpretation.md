<!-- music-kb:page {"id": "page.dee4629e4b6a5c4ea14d9d4a5d17195b"} -->
<!-- knowledge: composer.beethoven.chamber.quartet.op74-model -->
# Op.74/I：七和弦重释与外声部 10–8–6

<!-- aliases: Beethoven Op.74 harp quartet introduction, 4/3, 6/5, 10-8-6, outer voices, 贝多芬竖琴四重奏, Op.74和声, 减七和弦, 外声部, 反向运动 -->

## 创作问题

同一组外声部反向运动，怎样在换低音或换和弦解释后继续保留身份？Op.74/I 的慢引子提供了一个局部案例：开放七和弦被重释为减七音响，外声部关系随后进入呈示开端。

## 来源与定位

Johannes Raiser 对第一乐章慢引子及呈示部开端的全文分析认为：开头大提琴的降E–降D–C–降B下行四度可在降A大调语境读作5–2；引子第2小节属七和弦第二转位（4/3，原文Terzquartakkord）与休止让这次“错位”起步保持开放。第4小节把这一开放声响改成G低音上的减七和弦第一转位（6/5），导入Fonte序列；第7小节抵达降E大调属和弦，第8小节加快和弦更替。第9小节降A低音又同时支持降E大调下属方向、并召回降A大调的早先期待。到第8小节，外声部模式移入中提琴与第一小提琴，原开头动机转入低声部；后续10–8–6反向运动在第11–13、15–18小节继续变化。Raiser还将第25–35小节呈示部开端联系回引子轮廓：声部交换，且调性路线最终在降E大调终止（Raiser，ZGMTH 15/1，2018，例2–14、第一乐章mm.1–35）。这些都是作者的分析，不作为唯一听法或贝多芬直接意图证据。

## 机制解释

可迁移操作：先写上下声部相反方向的三点序列，再记录每个起音间形成的复合音程；转调或转入另一段时，可整体移动该关系、交换声部，并改变同一低音的和弦解释。历史作品的具体音符不从下面模型推导；下例只把10–8–6外声部运动变成可核对练习。

Op.59 No.3 的 Hatten 一手分析仍未获得全文。本轮不新增 Op.59 史实，既有 Brown 对 Hatten 的二手概述不作一手材料替代。正文若保留 Op.59，应继续注明该证据等级，直至实际读到原文并核对版本与小节号。

## 谱例

以下是原创G大调双声部练习，不是四重奏改编或贝多芬原谱。上声部下行、低声部上行，在第1和第3小节形成两次10–8–6序列；中间小节改变低音背景，最后停在D–A开放五度，不构成完整终止。

<!-- opusloom:example {"id": "beethoven.model.op74-10-8-6-transfer", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["raiser-op74-introduction-2018"], "rights": "原创双声部教学练习；没有转录 Raiser 文中贝多芬谱例或其他原谱。", "source_locator": "原创模型；只迁移 Raiser 对 Op.74/I 外声部10–8–6反向运动的分析问题（“Das Eröffnungsmodell”及“Das Modell im Gesamtkontext”，例2–14，mm.1–35（印刷pp.159–172））。", "context": "在G大调中做两次上、下声部反向的10–8–6运动，中间改换低音支撑；最终D–A开放五度，不显示V7–I终止。模型不证明贝多芬使用相同音符或和声。"} -->
```lilypond
\version "2.26.0"
\language "english"

global = { \key g \major \time 4/4 }

upper = {
  \global
  b'4 a'4 g'2 |
  g'1 |
  c''4 b'4 a'2 |
  a'1 |
}
lower = {
  \global
  \clef bass
  g4 a4 b2 |
  c1 |
  a4 b4 c'2 |
  d1 |
}

\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Upper line" } { \upper }
    \new Staff \with { instrumentName = "Bass line" } { \lower }
  >>
  \layout { }
}
```

## 逐音核对

逐小节核对：第1小节的同拍音程依次为G3–B4大十度、A3–A4纯八度、B3–G4小六度；低声部每拍上行，上声部下行，正是10–8–6。第2小节C3与G4形成纯十二度（音级关系为开放五度），为该形态提供新的低音背景，不补写成完整和弦序列。第3小节把线条上移一级：A3–C5小十度、B3–B4纯八度、C4–A4大六度，轮廓与音程级数相同，但十度和六度的性质改变。第4小节D3与A4形成开放十二度/五度；没有第三音，故不称完整属和弦或终止。此模型只练习线性关系转置，失效情形是听者无法听出反向运动，或作者把它误当作作品全段的固定和声模板。

LilyPond 使用 English 绝对音高：`c'`=C4、`b'`=B4、`c''`=C5；代码没有 `relative`/`fixed` 八度参照。

来源与权利：Raiser2018官方HTML全文实读，CC BY4.0；后续已缓存并核验实际正文，本节只作转述，不重印其谱例。Hatten 1980 仅登记为未读的 Op.59 一手候选，不支撑此模型。

## 迁移方法

先写一条上行低音和一条下行高声部，再记录每一拍形成的复合音程；保持 10–8–6 的轮廓，换低音背景与调性位置。若需要转成四重奏，再把两条外声部放入不同乐器，并补足内声部功能。

## 适用边界

来源ID：`raiser-op74-introduction-2018`（Raiser自己的局部谱面分析）。Hatten原文仍仅为未读候选，不为本节增加音乐论据。
