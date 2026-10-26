<!-- music-kb:page {"id": "page.79093d97a9114c2cafea47ba8a4f48c2"} -->
<!-- knowledge: composer.ravel.chamber-cyclic-writing -->
# 拉威尔室内乐：独立声部与循环材料

室内乐中的音色变化受到演奏人数和声部可执行性的约束。本章目前用 F 大调弦乐四重奏作为循环材料、声部职责和音区控制的具体证据：先读旋律，再对照开头两小节的四声部音高—时值缩编。阅读时结合[四重奏专题](../string-quartet.md)区分全文献分析与实际编码范围。后续应围绕同一问题纳入更多室内作品，而不是按曲名追加孤立案例。

## Ravel String Quartet: modal opening and cyclic return

<!-- knowledge: example.ravel.string-quartet.cyclic -->

### What to observe

The opening works by making several parameters agree without becoming a
four-square chord progression:

- the first violin projects a short identifiable cell;
- the second violin and cello move in slow, registrally separated steps;
- the viola often supplies a middle harmonic plane rather than a conventional
  Alberti or sustained chord;
- Jenkins (pp. 71–72) identifies an opening four-measure unit within a
  multi-part first theme; the local pitch vocabulary remains modal and open.

The short code below is an exact melody-only transcription from the CC0
OpenScore encoding. It omits the lower three parts. The three-bar excerpt is
only the beginning of that four-measure unit, not the complete multi-part
first theme. Jenkins places a six-measure transition and a repeat of part one
before the separate part two.

<!-- opusloom:example
{
  "id": "ravel.sq.opening-violin1",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "fragment",
  "midi": false,
  "requires": [],
  "sources": ["openscore-string-quartets"],
  "rights": "OpenScore String Quartets is released as CC0. This is a short melody-only transcription from score 8482283 with attribution retained.",
  "source_locator": "Ravel, String Quartet in F major, movement I, mm. 1-3, first violin",
  "context": "Opening melody only; the accompaniment and subsequent phrase are intentionally omitted."
}
-->
```lilypond
\version "2.26.0"
\time 4/4
\key f \major
a'4 g'8 a'8 e'4 d'4 |
a'8 f'8 c''8 e''8 d''2 |
f''4 e''8 a''8 g''4 f''8 e''8 |
```

### 从旋律回到真实四声部

只看上述旋律，无法知道低声部怎样支撑它。下例根据同一 OpenScore 记录的 MusicXML 编码，转写第一乐章第1–2小节全部四件乐器的音高与时值；为便于核对，省略力度、连奏、弓法及版面，移除没有发声音符的辅助休止声部。它是**音高—时值分析缩编**，不是原版排印的完整复制。原文件 SHA-256：`3bffd57550f92adb8049971ab1a6b92a14f24c984a92f3f2ddbc32c7aa79f72e`。

<!-- opusloom:example
{
  "id": "ravel.sq.opening-four-part",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["openscore-ravel-quartet-mxl"],
  "rights": "Source encoding CC0 1.0, OpenScore String Quartets contributors. New pitch-duration LilyPond transcription and analysis by OpusLoom; original expressive and layout markings omitted.",
  "source_locator": "Ravel String Quartet in F major I, mm1-2, all four parts; OpenScore sq8482283.mxl, Git blob c6f9c7041983ec54a09d2736bfccb86044436a18.",
  "context": "Concert pitch, original key and meter; all sounding pitch/duration events retained. Dynamics, slurs, bowings, engraving and silent auxiliary voices omitted. First authored in LilyPond 2.26.0 from MusicXML, not converted from an older LilyPond source. MIDI tempo is a study setting."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Violin I" midiInstrument = "violin" } {
      \key f \major \time 4/4
      a'4 g'8 a'8 e'4 d'4 |
      a'8 f'8 c''8 e''8 d''2 |
    }
    \new Staff \with { instrumentName = "Violin II" midiInstrument = "violin" } {
      \key f \major \time 4/4
      a4 bes c' d' | e' f' g' a' |
    }
    \new Staff \with { instrumentName = "Viola" midiInstrument = "viola" } {
      \clef alto \key f \major \time 4/4
      c2 g4 f | bes1 |
    }
    \new Staff \with { instrumentName = "Cello" midiInstrument = "cello" } {
      \clef bass \key f \major \time 4/4
      f,4 g, a, bes, | c d e f |
    }
  >>
  \layout { }
  \midi { \tempo 4 = 116 }
}
```

第二小提琴从 A3–B♭3–C4–D4 继续上行至 E4–F4–G4–A4，大提琴同时从 F2 逐级走到 F3，两条线形成平行的复三度（十度）；十度的大小随调内音级而变：F2–A3为大十度，G2–B♭3为小十度，并非固定半音数的机械平移。中提琴第一小节用 C3 半音符接 G3、F3 四分音符，第二小节停在 B♭3，使中间层的变化速度不同。

第一小节末两把小提琴同为 D4。声部在这里暂时汇合，之后再次分开；“每件乐器有独立声部”不等于“每个时点必须四个不同音高”。写作时可先安排这样可核对的相遇与分离，再判断音区、重音和和声是否支持材料的连续性。两小节只能支持此局部观察，跨乐章的循环关系仍需下文文献与对应段落证据。

新 MusicXML 的全文件解析存在其他小节的时值及动态楔形警告，已留在维护审计中；这里逐项核对开头两小节，不把一次解析成功宣称为整部编码无损。

### Cyclic design

Jenkins’s full-text analysis (pp. 80–85) identifies the following
large-scale network:

- the slow movement quotes or develops the first-movement opening cell several
  times;
- the finale builds a secondary/third theme from second-theme material of the
  first movement;
- the coda recombines first-movement and finale material before the final
  harmonic close.

Use this as a **relation** to build in a new quartet:

```text
movement I: identity cell A + contrasting lyric cell B
movement III: expose A at a slower speed, altered register, and new harmony
movement IV: derive C from B and combine C with fragments of A in the coda
```

The late return should add a new musical function. Literal quotation is one
option, but contraction, reharmonization, inversion, fragmentation, and
counterpoint all provide more room for the new work to have its own identity.

### Transfer checklist

- Can the returned material be recognized without reading its label?
- Does the new harmony or register change its emotional or formal role?
- Are the claims supported by actual notes in every affected part?
- Does the movement remain playable when the return is distributed among
  instruments?
- Does the coda close the tonal and thematic processes instead of only
  performing a thematic montage?

### Evidence

- `openscore-string-quartets`: score, movement, measure, and pitch evidence.
- `ravel-jenkins-quartet-thesis`: page-level cyclic-return inventory.
- `ravel-heinzelmann-dissertation`: metadata and abstract-level verification
  only; a research lead, not independent full-text evidence for the cyclic
  relationships above.
