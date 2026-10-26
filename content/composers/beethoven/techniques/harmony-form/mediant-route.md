<!-- music-kb:page {"id": "page.0160d9ac9ecd5eb1a19e8612b36dff8e"} -->
<!-- knowledge: composer.beethoven.mediant-route -->

# 三度关系调性路线：准备、到达与确认

检索词：Beethoven mediant 三度关系 远关系调 tonal route functional harmony Op.53 Waldstein 瓦尔德施泰因 到达 确认 preparation arrival confirmation。

**创作问题。** 何时应从主调走到三度关系调？怎样让听者把远关系调听成持续区域，而不是一枚颜色和弦？

## 来源与定位

Igoa 在功能和声体系中分析 Op. 53 第一乐章第 18–38 小节的调性转向，并把到达 E 大调附近的进行解释为延长属功能。具体罗马数字是作者的理论解释；面向新作可保留的保守结论是：从 C 走到 E，需要 E 的导向、到达和在 E 内部的后续活动。[Igoa，2023 修订版，第 30 页、图 11](https://www.enriqueigoa.com/articulos_y_libros/Functional_Harmony.pdf)

## 机制

下例是原创四声部方案，**不是 Op. 53 的和声缩谱**。第 1 小节 C 确立出发点；第 2 小节 A 小调可从 C 的 vi 重新理解为 E 小调的 iv；第 3 小节 B7 使 D♯、A 分别趋向 E、G♯；第 4 小节 E 大调只是初次到达，第 5–8 小节再在该调活动并以根位属—主确认。大小调转换是模型的选择，不能据此倒推贝多芬的心理意图。

<!-- opusloom:example {"id": "beethoven.model.mediant-route", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["beethoven-igoa-functional-harmony"], "rights": "Original four-voice teaching model; not a reduction or transcription of Op.53.", "source_locator": "Self-authored C-major to E-major exercise, eight whole-note sonorities, demonstrating preparation, arrival and confirmation.", "context": "原创三度关系调性路线。罗马数字解释与具体音符对应，非贝多芬作品引文。"} -->
```lilypond
\version "2.26.0"
\language "english"
sop = { e'1 | e' | ds' | e' | cs' | e' | fs' | e' | }
alt = { c'1 | c' | a | gs | a | gs | a | gs | }
ten = { g1 | a | fs | e | fs | e | ds | e | }
bas = { c1 | a, | b, | e, | a, | e, | b, | e, | }
\score {
  \new ChoirStaff <<
    \new Staff <<
      \key c \major \time 4/4
      \new Voice { \voiceOne \sop }
      \new Voice { \voiceTwo \alt }
    >>
    \new Staff <<
      \clef bass \key c \major \time 4/4
      \new Voice { \voiceOne \ten }
      \new Voice { \voiceTwo \bas }
    >>
  >>
  \layout {}
}
```

第 5 小节为 E 大调的 ii6，第 6 小节回到 I；第 7–8 小节再做 V7–I。第一处 B7→E 的低音下降五度，旋律半音上行；第二次到达相同和声时，前面已有新调的 ii6 与 I，因此承担更强确认功能。

从低音轨迹看，前四小节由 C 落到 A、再到 B，最后进入 E；听辨时先唱每条声部，再关掉高音只听低音，检查目标音是否被稳定支撑。若目标调内没有任何局部功能，所谓到达会退回色彩性经过和弦。

## 迁移方法

1. 先写三段状态：当前主调、准备远调的枢轴、目标调中的持续区域。
2. 在准备段明确新调特征音和低音方向，不只更换和弦标签。
3. 到达后至少写一个目标调内部的局部功能，再结束区域。
4. 用全音符检查声部进行，之后才加入句法、主题和织体。

## 适用边界

本例用八个全音符和弦暴露声部进行，用于比较和声规划，不能直接当主题粘贴。目标调是否建立，应综合导向、持续、局部功能与段落位置判断，不能只凭一次和弦或停留时长下结论。Op. 53 的实际心理意图与整章形式结论不由该模型证明。

来源 ID：`beethoven-igoa-functional-harmony`。谱例元数据保留了模型性质、音符范围与作品非转录声明。
