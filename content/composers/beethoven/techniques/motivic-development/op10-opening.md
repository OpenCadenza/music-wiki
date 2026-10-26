<!-- music-kb:page {"id": "page.20c07f70542d5c7ab6acf42543b3a09f"} -->
<!-- knowledge: composer.beethoven.op10-opening -->

# Op.10 No.1 开头：同调性中的不同动机行为

检索词：Op.10 No.1 c minor opening 动机 motive register dynamics 音区 力度 fragmentation 碎片化 Mutopia 778。

**创作问题。** 开头没有转调时，怎样让重复材料表现出“爆发、应答、再碎片化”三种不同功能？

## 来源与定位

下面保留 Mutopia 原码的绝对音高、3/4、力度和基本发音；只截第 1–4 小节并补显小节线，去掉标题等版面设置。原码为 LilyPond 2.8.0，不因使用新版编译器就把它记作原生 2.26。底本为 Breitkopf & Härtel 1862–65；[Mutopia 条目 778](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=778)。

<!-- opusloom:example {"id": "beethoven.score.op10-1.opening", "status": "published", "source_version": "2.8.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["mutopia-beethoven-op10-1"], "rights": "Beethoven work and Mutopia typesetting declared Public Domain; maintainer Stelios Samelis. Short excerpt with explicit bar lines, no pitch/rhythm modernization.", "source_locator": "Op.10 No.1, I, mm.1–4, both piano staves; Mutopia-2006/06/12-778, source Breitkopf & Hartel 1862–1865; corpus/lilypond/BeethovenLv/O10/LVB_Sonate_10no1_1/LVB_Sonate_10no1_1.ly, declared version 2.8.0.", "context": "原谱四小节：上行爆发、休止与较低音区的弱奏应答。下谱表第3小节换高音谱号是原编码的一部分。"} -->
```lilypond
\version "2.8.0"
\score {
  \new PianoStaff <<
    \new Staff {
      \clef treble \key c \minor \time 3/4
      <ees' g' c''>4.\f r16 g'16([ ees''8. c''16] |
      g''8.[ ees''16 c'''8. g''16] ees'''4\staccato) |
      ees'''4\staccato r4 <g' c''>4\p |
      <g' c''>2( <g' b'>4) |
    }
    \new Staff {
      \clef bass \key c \minor \time 3/4
      <c ees g c'>4.\f r8 r4 | R2. |
      r4 r \clef treble <c' ees'>4\p |
      <c' ees'>2( <d' f'>4) |
    }
  >>
  \layout {}
}
```

## 机制

第 1 小节的强和弦后，十六分音符进入上行琶音；第 2 小节到高音 E♭，第 3 小节先重复高音再空出一拍，随后落到中音区弱奏和声音型。第 4 小节保留 G，上方 C 转向 B，所以应答不是“同一琶音移调”。对创作有用的是两种材料占据不同音区、力度和时间密度。

Boss 进一步讨论两种声部进行材料如何交换显著程度。其动机分段受特定申克／勋伯格综合方法约束，是有归属的解释，不是表面音型的唯一分法。[Boss 1999，段 5–6](https://mtosmt.org/issues/mto.99.5.1/mto.99.5.1.boss.html)

逐小节看，第 1 小节同时给出厚和弦、空拍和快速上行，三种信号都在很短时间出现。第 2 小节延续上行，但落到高音 E♭ 后以断奏收住；第 3 小节先重复最高音，再让休止把强拍前后的连续动作切开。第 4 小节改用较弱力度和中音区，C→B 的半音变化则让“回应”仍带方向，而不是完全静止的重复。

若只抄取音高，容易漏掉音区、力度与休止造成的功能差异；若只抄节奏，又无法解释高音区的上升怎样制造紧张。因此迁移时应同时标记“演奏动作”和“结构作用”。例如可在新作中保留四分音符起音与十六分音符细分，让第一次出现在低音区，第二次移向高音区，第三次只留下起音与休止。低音和终止仍须重新设计。

## 迁移方法

选一条可听见的不变量，例如“四分音符起音后接一组十六分音符”，让它在高音区保持运动，在中音区变慢，并在段落边界只剩片断。每次变化至少选择一个可观察条件：音区、重音、低音支撑、休止位置或声部交换。

## 适用边界

四小节只能支持局部观察。它不能独立证明全乐章的曲式、叙事或心理内容。要继续写发展段，先把这里的机制与原创六小节练习连读：[保留节奏，改变动机任务](motive-functions.md)。

来源 ID：`mutopia-beethoven-op10-1`、`beethoven-boss-op10-1`。谱例 ID `beethoven.score.op10-1.opening` 保持不变。
