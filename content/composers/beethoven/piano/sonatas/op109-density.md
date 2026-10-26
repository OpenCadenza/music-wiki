<!-- music-kb:page {"id": "page.a88ef58c35b650febe84196999168890"} -->
<!-- knowledge: composer.beethoven.piano.op109-density -->

# Op.109 变奏密度：保留拍点骨架，增加拍间音

检索词：Beethoven Op.109 finale 变奏 variation six variations density diminution 音值 密度 骨架 Warburton。

**创作问题。** 主题与变奏的音符变多时，怎样让听者仍能追踪原来的拍点和结构音？

## 来源与定位

Warburton 将 Op. 109 终乐章分析为主题与六个变奏：主题左手步行低音与右手构成互补旋律；第五变奏具有赋格式的进行感，却不是严格赋格；第六变奏逐级缩短音值，并带回主题轮廓（Warburton, pp. 72–75）。其论述以演奏准备为核心，不能替代末五首奏鸣曲的总体形式研究。来源 ID 为 `warburton-op109-2018`。

## 机制

下例是新写的 C 大调四小节练习，不转录 Op. 109 音符，也不声称仿作贝多芬。前两小节用四分、二分音符陈述简短骨架；后两小节把骨架支点保留在每拍第一枚八分音符上，并在拍间加入经过音。它只示范一个可操作参数：增加音符密度，同时维持低音支点和拍点上的结构音。

<!-- opusloom:example {"id": "beethoven.model.late-sonata-density-expansion", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["warburton-op109-2018"], "rights": "原创 C 大调教学练习；未引用或转录贝多芬原谱、现代版谱例或文献编码。", "source_locator": "只迁移 Warburton 对 Op. 109/III 变奏中音值密度与主题回返的观察（PDF pp. 72–75）；模型音符、调性、节拍与结构均为新写。", "context": "两小节四分音符/二分音符骨架，随后两小节以八分音符填充拍间，结构音保持在强拍。练习音值扩张/缩短的可控参数，不是完整变奏或赋格。"} -->
```lilypond
\version "2.26.0"
\language "english"

upper = {
  \key c \major \time 4/4
  e'4 g' a' g' | c''2 b'4 a'4 |
  e'8 f' g' a' a' b' g' f' | c''8 d'' c'' b' b' c'' a' g' |
}
lower = {
  \key c \major \time 4/4
  c4 e4 g4 g4 | f4 a4 c'4 c'4 |
  c8 d e f g a g f | f8 g a b c' d' c' b |
}

\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \clef bass \lower }
  >>
  \layout { }
}
```

第 1 小节上声部以 E–G–A–G 和低音 C–E–G–G 形成四个清楚拍点；第 2 小节上声部以持续的 C 后接 B–A，低音移动到 F–A–C–C。第 3 小节把原先拍点上的 E–G–A–G 保留为每拍第一枚八分音符，中间增加 F、A、B、F；低音同样保留 C–E–G–G 支点并填入经过音。第 4 小节上声部保留 C–C–B–A，低音保留 F–A–C–C，再把拍间填音写成八分音符。

## 迁移与失败检查

先圈出主题每拍的骨架音，再写低音支点，最后填拍间音。每加一层都问：强拍上的原结构音是否仍能单独唱出？新音是否改变原定和弦功能？如果拍点支点听不清，或填音把声部进行改成另一条旋律，这个压缩模型就没有保住骨架。

模型停在开放进行中，避免把四小节练习伪装成贝多芬终止。它不模拟 Op. 109 的实际旋律、和声、九拍子变化或六个变奏，也不证明“音符更多”必然等于音乐时间扩张。

来源 ID：`warburton-op109-2018`。谱例 ID `beethoven.model.late-sonata-density-expansion` 保持不变。
