<!-- music-kb:page {"id": "page.fbb06409537d53a79a42dcc881ee894c"} -->
<!-- knowledge: composer.beethoven.piano.op2no1-opening -->

# Op.2 No.1 开头：弱起、重复与移位

检索词：Beethoven Op.2 No.1 F minor opening 右手 弱起 upbeat repetition transposition 三连音 Mutopia 1211。

**创作问题。** 短句没有完成转调时，怎样通过弱起、音区扩展和节奏重复制造连续推进？

## 来源与定位

以下四小节取自 Mutopia 的公有领域版本，采用 Breitkopf & Härtel 1862–65 版，原编码为 LilyPond 2.10.3。仅取右手开头，保留弱起、节奏、音高与原调，省略左手、力度、反复、延音和版面。它能支持局部观察，不足以独自证明全乐章曲式。[Mutopia 条目 1211](https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1211)

<!-- opusloom:example {"id": "beethoven.op2no1.opening-right-hand", "status": "published", "source_version": "2.10.3", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["mutopia-beethoven-op2no1-m1"], "rights": "贝多芬原作与此 Mutopia 类型稿由制作者声明置于公有领域。保留 Mutopia/制作者署名；短片段从原 LilyPond 2.10.3 类型稿摘录，删去左手、反复、力度、延音与版面，不是新编原谱。", "source_locator": "Mutopia-2008/01/07-1211; Beethoven, Piano Sonata in F minor, Op. 2 No. 1, I, opening, first four complete bars after the quarter-note upbeat; Breitkopf & Härtel 1862–65; Stelios Samelis.", "context": "右手旋律/和弦声部摘录。原稿 version 2.10.3; \\partial 4 的四分音符弱起后接四个 4/4 小节。简化标记以便只讨论节奏与音高方向。"} -->
```lilypond
\version "2.10.3"
\score {
  \new Staff {
    \clef treble \key f \minor \time 4/4
    \partial 4 c'4 |
    f'4 aes' c'' f'' |
    aes''4. \times 2/3 { g''16[ f'' e''] } f''4 r4 |
    g'4 c'' e'' g'' |
    bes''4. \times 2/3 { aes''16[ g'' f''] } g''4 r4 |
  }
  \layout {}
}
```

## 机制

弱起 C4 后，首个完整小节以 F 小调主和弦分解式向上铺开；下一小节将附点四分音符接三连音邻接下行，再以休止切断。第三小节重复同一节奏骨架，但把起点移到属和弦音区；第四小节以相同的附点—三连音型回答。

这四小节足以观察“重复与移位”的并置，却不说明后续段落的调性功能。右手摘录省略左手，因此不能据此判断每次上行的和声支撑、终止强度或踏板。创作时若使用类似节奏，应另写低音目标，并检查重复是在继续同一区域，还是已经进入新的形式位置。

## 迁移方法

1. 选一个两小节节奏骨架，不先填满和声。
2. 用弱起进入第一陈述，再用音区或和弦位置移动第二陈述。
3. 两次陈述只改变一项主要参数，保留可辨识的附点与细分节奏。
4. 补写低音后才判断新句是继续、转调还是终止。

听辨时可以把四个完整小节分成两组：第一组由 F 小调主和弦音向上扩张，第二组把同一节奏骨架移到属和弦音区。两组都在高点后以休止截断，但第二组最高音更高、落点也不同。此差异支持“重复中的移位”，不足以说明全章如何离开 F 小调；要回答后者，必须补回左手、转调过程与终止位置。

## 适用边界

该摘录只支持开头四小节的局部观察，不能证明整章的结构或情绪。原稿声明版本为 2.10.3；编译兼容不等于把历史编码改成原生 2.26。谱例 ID `beethoven.op2no1.opening-right-hand` 保持不变。

来源 ID：`mutopia-beethoven-op2no1-m1`。
