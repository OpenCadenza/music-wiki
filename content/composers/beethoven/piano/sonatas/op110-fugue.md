<!-- music-kb:page {"id": "page.7b928c06a2e45191a909c46cc6f6dcaa"} -->
<!-- knowledge: composer.beethoven.piano.op110-fugue -->

# Op.110：稿本证据与赋格主题变形

检索词：Beethoven Op.110 fugue 赋格 Arioso inversion 倒影 augmentation 增值 diminution 缩减 G minor G major A-flat return m.174。

**创作问题。** 怎样让赋格主题的倒影和原形回返成为段落事件，而不是只列出一串进入？

## 创作史：草稿次序不能等同于完成过程

Matheson 对 Op. 110 的研究以巴黎袖珍草稿、相关柏林与波恩材料、亲笔总谱层次和终乐章修订为核心。她指出，现存亲笔谱有大量修订，终乐章有独立的改写净稿；在判定草稿次序以前，还需重建巴黎袖珍稿的物理结构（1993，绪论 pp. 1–8；终乐章创作史 pp. 65–104）。这项研究的价值首先是限制断言：纸页排列或出版次序不能单独证明创作顺序。

面对多版乐谱时，按四层记录：实物层（纸页、谱表、插入、划除与重写）、材料层（主题、节奏、低音、调性、织体变化）、决定层（哪些变化进入改写净稿）、解释层（为何选择此版本及其段落功能）。完成记录后，才可把改动概括为“压缩”“扩展”或“回返”。Matheson 的研究不是三乐章完整曲式分析，不能单独推出终乐章形式或演奏意义。

## 来源与定位

Ofcarcik 将 Arioso 与赋格看成彼此交替、各自回返的线索。她辨认第一赋格第 26–30 小节降 A 大调的上行四度主题；第一赋格结尾的预期终止在第 114 小节转向 G 小调，第二赋格第 136–140 小节在 G 大调以倒影形态开始。第 160 小节的低音增值与右手缩减紧接，第 174 小节降 A 大调原形回返提供可定位的变形比较。“追寻／悲剧”的叙事是作者解释，音程、进入位置和调性才是优先核查的层次。[Ofcarcik 2020，段 2.15–2.20](https://mtosmt.org/issues/mto.20.26.2/mto.20.26.2.ofcarcik.html)

Beethoven-Haus 展览册为 Op.59 No.3、Op.102 No.2、Op.106、Op.110 与 Op.130/133 提供赋格及稿本入口。它支持跨作品背景，不能替代上述逐小节分析。[展览册，页 4–7](https://internet.beethoven.de/pdf-web/fuge_begleitheft_en_screen)

## 原创检查模型

下例是四小节新写练习，不是 Op. 110 原谱，也不是完整赋格或贝多芬风格仿作。它只演示一个检查流程：先写短主题，再以反向音程轮廓安排应答，随后恢复原形并改变低音支撑。主题 C–D–E–G 的相邻音程为上行全音、全音、小三度；倒影 G–F–E♭–C 依次下行全音、全音、小三度。模型不声称解决调性应答、对题、主题与对题组合、插部、紧接或赋格式终止。

<!-- opusloom:example {"id": "beethoven.model.op110-subject-transformation", "status": "published", "source_version": "2.26.0", "target_version": "2.26.0", "compile": "score", "midi": false, "requires": [], "sources": ["beethoven-ofcarcik-2020", "beethoven-haus-fugue-2022"], "rights": "原创教学模型；未转录或改写贝多芬原谱、现代版谱图或本文献示例。", "source_locator": "原创四小节模型；Op. 110 原作讨论位置为第一赋格 mm. 26–30、第一赋格结尾的调性改向 mm. 98–114、第二赋格倒影主题 mm. 136–140、原形回返 m. 174（Ofcarcik 2020, §§2.15–2.20）。这些小节定位描述历史作品，不是模型来源音符。", "context": "新创 C 大调双手键盘练习，展示上行主题的倒影轮廓、另一声部应答及主题原形回归。片段不完整，不是完整赋格，也不声称复原贝多芬风格。"} -->
```lilypond
\version "2.26.0"
\language "english"

upper = {
  \key c \major \time 4/4
  c''4 d'' e'' g'' | b'4 c'' g' e' |
  c''4 d'' e'' g'' | <c' e' g'>1 |
}
lower = {
  \key c \major \time 4/4
  R1 | g4 f ef c |
  c4 g c' e' | c1 |
}

\score {
  \new PianoStaff <<
    \new Staff { \upper }
    \new Staff { \clef bass \lower }
  >>
  \layout { }
}
```

第 1 小节高声部单独提出 C–D–E–G 主题，四个四分音符把上行轮廓清楚呈示。第 2 小节低声部以 G–F–E♭–C 作倒影应答；高声部 B–C–G–E 作为缓慢对旋律，与低声部保持间隔，避免被误听成同音齐奏。第 3 小节高声部恢复原主题；低声部 C–G–C–E 改作和声支撑，使主题回归与低音框架改变可以同时听见。第 4 小节落在 C 大三和弦，因前面没有属和弦准备，不是完整的属—主终止。

## 迁移与边界

操作时分别记录主题形态、进入声部、调性、时间压缩和与前段的衔接。先检验倒影或缩减后仍能否辨识主题，再解释它为什么在这里出现。模型只完成主题、倒影、回归三个局部动作；写成赋格还需独立检查应答调性、对题共存、声部间距、和声节奏和终止证据。

来源 ID：`matheson-op110-genesis-1993`、`beethoven-ofcarcik-2020`、`beethoven-haus-fugue-2022`。Matheson 的研究未在本批逐页精读终乐章全章；任何扩大为全曲创作史或形式定论的表述都超出证据。谱例 ID `beethoven.model.op110-subject-transformation` 保持不变。
