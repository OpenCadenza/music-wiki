<!-- music-kb:page {"id": "page.59739bdaa009513bb6ab8d2428a176c7"} -->
<!-- knowledge: composer.beethoven.metric-displacement -->

# 节拍错位与留白：三拍框架上的两拍重音

检索词：metric displacement 切分 hemiola 3/4 2拍 重音 fermata rest LilyPond ABC Beethoven 节奏。

**创作问题。** 怎样保留三拍框架，同时让两拍重音持续出现，并在需要时恢复小节强拍？

## 来源与机制

Eastman 对第七交响曲的导读把持续节奏与结构性静默联系起来：第一乐章 Vivace 的重复节奏在段落关口被停顿打断。这个个案支持“持续行为的中断能划界”，不能推出每个休止都象征命运，也不能推广到所有交响曲。[Eastman，Symphony No.7，Significance and Structure](https://www.esm.rochester.edu/beethoven/symphony-no-7/)

下例没有引用贝多芬旋律。第 1–2 小节共同形成每两拍一次的重音：落在第 1 小节第 1、3 拍以及第 2 小节第 2 拍。实际时间总长为六个四分拍，仍按两个 3/4 小节记谱；低声部每小节的根音让三拍框架可感知。第 3 小节回到小节强拍，第 4 小节停顿。

<!-- opusloom:example {"id": "beethoven.model.metric-displacement", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["esm-symphony-7"], "rights": "Original teaching model; no Beethoven melody reproduced.", "source_locator": "Self-authored four-bar 3/4 model, first two bars accent beats 1,3,5 in a six-beat span.", "context": "原创：3/4小节框架上叠加两拍重音分组，之后恢复与留白。不是原作节奏的转录。"} -->
```lilypond
\version "2.26.0"
\language "english"
\score {
  \new PianoStaff <<
    \new Staff \relative a' {
      \key a \minor \time 3/4
      a4-> b c-> | d e-> f |
      e2-> d4 | c2 r4\fermata |
    }
    \new Staff \relative a, {
      \clef bass \key a \minor \time 3/4
      a4 <c e> <c e> | d <f a> <f a> |
      e <gs b> <gs b> | a <c e> r |
    }
  >>
  \layout {}
}
```

重音不需要每次换和弦。前两小节低声部按小节换根音，上声部按两拍形成重音，两种分组因此可以同时被听见。第 3 小节的二分音符放宽动作；最后少一拍发声，停顿因前面一直有拍子而明确。增加配器时，应先决定谁维持拍子、谁偏移重音，避免全体乐器复制同一条切分。

## 同义的 ABC 编码

下面给出同一模型的 ABC 表达。`!accent!` 标明前述三处重音和恢复点，不改变 `M:`；`!fermata!z` 仍有一个四分音符的基本时值。两声部每小节各为三个四分拍，末小节上方 C 持续两拍，下面 A 与和弦各一拍后共同休止。此例与前面的 LilyPond 共享教学意图，仍是原创。

<!-- opusloom:example {"id": "beethoven.model.metric-displacement-abc", "status": "draft", "source_version": "2.1", "compile": "score", "midi": false, "requires": [], "sources": ["esm-symphony-7"], "rights": "Original teaching model, ABC encoding of the paired original LilyPond exercise.", "source_locator": "Self-authored four bars in ABC 2.1; not a Beethoven transcription.", "context": "原创双声部ABC，与同页LilyPond模型配对说明节拍、重音和休止的编码。"} -->
<!-- music-kb:block {"id": "abc.beethoven.metric-displacement", "language": "abc"} -->
```abc
%abc-2.1
X:1
T:Accent groups within 3/4 — original model
M:3/4
L:1/4
%%score (1 2)
V:1 clef=treble name="Gesture"
V:2 clef=bass name="Pulse"
K:Am
[V:1] !accent!A B !accent!c | d !accent!e f | !accent!e2 d | c2 !fermata!z |]
[V:2] A,, [C,E,] [C,E,] | D, [F,A,] [F,A,] | E, [^G,B,] [^G,B,] | A, [CE] z |]
```

## 迁移与边界

ABC 编写时，把拍号写在 `M:`，把实际重音写为装饰或力度；不要为了每两拍的重音就把这段改成 2/4。LilyPond 的 `->` 是重音，并不自动改变和声或节拍。停顿要区别 `r` 的有度量休止与 `\fermata` 的演奏延长，后者不能替代缺失时值。模型不说明真实作品的速度、踏板或配器。

来源 ID：`esm-symphony-7`。谱例 ID `beethoven.model.metric-displacement` 与 `beethoven.model.metric-displacement-abc` 保持不变。
