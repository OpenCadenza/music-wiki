<!-- music-kb:page {"id": "page.d620b1f4e35753d9966441a237e0c42f"} -->
<!-- knowledge: composer.beethoven.motive-functions -->

# 保留节奏，改变动机任务

检索词：动机 development A B C 原型 模进 fragmentation liquidation 碎片化 低音 终止 创作 exercise。

**创作问题。** 怎样让同一节奏先陈述、再继续、最后变成终止前的碎片，而不只是逐调复制？

## 任务与机制

先限定一个可听见的不变量，再让其他参数服务段落目标。下例不是 Op. 10 No. 1 的续写，也不使用贝多芬旋律。A 是两小节单元；B 把第一小节轮廓移到另一音级，并把第二小节改成继续；C 抽取前两次起音，让单元成为向终止推进的碎片。

<!-- opusloom:example {"id": "beethoven.model.motive-functions", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["beethoven-boss-op10-1"], "rights": "Original teaching model; no Beethoven excerpt reproduced.", "source_locator": "Self-authored six bars, grouped as A/B/C. An exercise in distinguishing retained rhythm from changed phrase role, not Boss's analytical graph.", "context": "原创：重复、继续、碎片化，必须连同和声目标理解。"} -->
```lilypond
\version "2.26.0"
\language "english"
\score {
  \new PianoStaff <<
    \new Staff \relative c'' {
      \key c \minor \time 4/4
      \mark "A" c8[ ef g ef] d4 c | bf2 r2 |
      \mark "B" ef8[ g bf g] f4 ef | d8[ ef f g] af4 f |
      \mark "C" d8[ f] r4 d8[ f] r4 | b,4 d c2 |
    }
    \new Staff \relative c {
      \clef bass \key c \minor \time 4/4
      c1 | g | ef | f | g | g2 c, |
    }
  >>
  \layout {}
}
```

B 第 3 小节仍是四个八分音符加两个四分音符，但第 4 小节填上运动而不休止。C 第 5 小节将两音碎片插入空白，低音 G 持续，使听觉等待归向 C；第 6 小节 B→C 完成局部收束。原型、模进和碎片不是三张可任意拼贴的标签，低音与终止目标决定它们在这里的作用。

## 迁移方法

写较长发展段时，先选两条操作，例如“保留前三次起音，每两小节改变低音”，或“保留半音邻接，交换前景声部”。若旋律、节奏、低音、音区同时全改，联系很难被感知；若只把原型逐调复制，材料虽一致却没有段落方向。

完成操作后逐项检查：

1. A 的不变量是否在三段都能听见？
2. B 是否出现新的和声目标或低音方向？
3. C 的减少是否推动终止，而不是单纯删除音符？
4. 任一相似音程是否还有出现位置与声部作用的支持？

若 B 段只改变调高而低音仍机械重复 A，听者容易把它当作同一句的平移；若 C 段删得只剩一个音，联系虽然极简，却已缺少可比较的节奏身份。较稳妥的顺序是先保留两至三个参数完成一次可辨模进，再逐步减少到单一碎片。每次减少都应同时交代新的和声压力或终止方向，让“少”成为推进的结果。

## 适用边界

模型只证明局部节奏与和声任务可以并行改变，不证明贝多芬采用同一程序。对四重奏的声部交接转查 `chamber/quartets/`；对跨乐章与大规模交响结构转查 `orchestral/symphonies/`。不能把“检索到相同三音”当作跨乐章统一性的充分证据。

来源 ID：`beethoven-boss-op10-1`。谱例 ID `beethoven.model.motive-functions` 保持不变。
