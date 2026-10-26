<!-- music-kb:page {"id": "page.7d49f43636a755008d2fdc79318512b0"} -->
<!-- knowledge: composer.beethoven.woo78-theme-march -->

# WoO 78 主题与第六变奏：从 3/4 到 4/4 进行曲

检索词：Beethoven WoO78 God Save the King variations 七变奏 3/4 4/4 march 进行曲 发音分组 Mutopia 1024。

**创作问题。** 保留和弦骨架和调性目标时，拍号、弱起与发音分组怎样把主题改写成进行曲？

## 来源与定位

《God Save the King》七变奏 WoO 78 主题右手第 1–2 小节，与第六变奏（Allegro. Alla Marcia.）的弱起及第 1–2 小节，可观察到 3/4 与 4/4 的转换。底本为 Mutopia-2007/08/14-1024，Breitkopf & Härtel 1862–1865，制作者 Stelios Samelis 声明 Public Domain。下面以 2.26.0 独立转录原调、绝对音高、时值和第六变奏弱起；省去左手、反复、力度及版面。[Mutopia 条目 1024](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1024)

<!-- opusloom:example {"id": "beethoven.score.woo78.theme-variation6", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["mutopia-beethoven-woo78"], "rights": "Beethoven work and Mutopia typesetting declared Public Domain; credit Stelios Samelis and Mutopia. Independent short transcription; right hand only.", "source_locator": "WoO78: Theme, RH mm1–2; Variation VI, RH quarter-note pickup and mm1–2. Mutopia-2007/08/14-1024; Breitkopf & Hartel 1862–1865; original LilyPond 2.10.3, new transcription 2.26.0. Left hand, repeats, dynamics and layout omitted.", "context": "真实短例对照3/4主题与4/4进行曲变奏。独立重新转录，非逐音对齐的和声缩谱。"} -->
```lilypond
\version "2.26.0"
\language "nederlands"

\score {
  \new Staff \with { instrumentName = "Theme RH" } {
    \key c \major
    \time 3/4
    <e' c''>4 <g' c''>4 <a' d''>4 |
    <d' b'>4. <g' c''>8 <g' d''>4 |
  }
  \layout { }
}

\score {
  \new Staff \with { instrumentName = "VI RH" } {
    \key c \major
    \time 4/4
    \partial 4
    <e' g' c''>8. <e' g' c''>16 |
    <e' g' c''>4. <f' g' b'>8
    <g' c''>8.-.[ <f' g' b'>16-.]
    <e' g' c''>8.-.[ <f' a' d''>16-.] |
    <d' g' b'>4. <g' c''>8
    <g' d''>8.-.[ <g' b'>16-.]
    <g' c''>8.-.[ <g' d''>16-.] |
  }
  \layout { }
}
```

## 机制

主题首小节最高声部 C–C–D，三个四分音符和弦建立步态；次小节 B 附点四分音符、C 八分音符、D 四分音符合计三拍。第六变奏弱起是 C 大三和弦的附点八分音符加十六分音符，随后完整小节在较长和弦与成对短音之间交替。

谱例只证明拍号、时值与发音分组的局部改变，不给出整套变奏的统一公式；两段也不是逐音对齐的同一乐句。迁移时可先保留和弦骨架和调性目标，改写拍子及起音分组，再补低音检查。此例省略左手，不能由右手独自推断和声全部保持不变。

主题第一小节的最高声部停在 D，下一小节先以 B 为长音，再经 C 到 D。第六变奏把重音与发音关系改写成弱起和短音回应：完整小节先保留较长的 C 和弦，再用附点与十六分音符把音头成对分组。这里的“进行曲感”来自拍号、弱起、长音和短音的组合，不能只归因于速度标题。

实际操作可分四步。第一步，写下原主题的和弦骨架与各和弦持续时值；第二步，选择新的拍号和小节分组；第三步，只改变发音起点，检查每个长音是否仍被低音支撑；第四步，补齐左手后再判断终止与调性。若拍号改变后每小节仍照原样塞入三个等长动作，4/4 只成为表面标签；若短音分组破坏了目标和弦，进行曲步态也会失去和声基础。

比较两段时，还要避免把它们说成逐音变奏。主题与第六变奏的右手材料并非全部一一对应，省略的左手又承担和声与步态。正确结论只能落在当前截取的拍号、时值、音高和发音分组上；其他变奏是否使用同一策略，需要分别核谱。

## 适用边界

真实摘录支持两个局部段落之间的可观察差异，不能证明第六变奏是主题的逐音改写，也不能概括七首变奏的整体过程。谱例 ID `beethoven.score.woo78.theme-variation6` 保持不变。

来源 ID：`mutopia-beethoven-woo78`。
