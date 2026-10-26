<!-- music-kb:page {"id": "page.89eed1bee33249bdb4adac247c31defc"} -->
<!-- knowledge: composer.debussy.keyboard-orchestral-texture -->
# 德彪西：平行层、持续音与音色转移

讨论德彪西时，“和声很新”或“色彩很丰富”都不足以指导写作。一个和弦可以只是表面装饰，也可以与持续低音、内声部下行和音色转移共同制造段落方向。本章因此把四个作品放在同一组问题上：《水之倒影》（*Reflets dans l'eau*，1905）怎样让平行声部仍有隐含声部线；《帆》（*Voiles*，约 1909–10）怎样用不同节奏和音区分开全音素材；《大海》（*La Mer*，1903–05）怎样让织体密度、固定音级和音色承担跨段结构；《牧神午后前奏曲》怎样通过一次乐器转移改变熟悉主题的意义。

本章的代码都是原创教学模型。它们演示“平面”“持续层”“乐器转移”如何写在谱上，不包含上述作品的主题，也不证明某件作品的完整曲式。

## 平行不是把普通和声整体搬高

Peter DeLone 对《水之倒影》开头第 1–2 小节的读谱给出了一个有用的区分：上方是三个音一组、连续移动的 sonorities，下方另有一条下行旋律 A♭–F–E♭；同时，三音和弦本身的最高或最低位置又形成一条隐含的 D♭–C–B♭ 下行。也就是说，“平行声部”不是每音都同向移动的视觉现象，它还可以在固定音程或和弦外形中保留一条可追踪的线。

DeLone 指出，这条下行关系在第 66–69 小节的 au Mouvement 段落再次得到强调，并在第 70 小节回到 D♭ 时清晰出现。这里的跨段关系不是“某和弦回来”，而是外层音型、音区定位和隐含线条共同让返回可辨。正确的问题不是“每小节应该换几个七和弦”，而是：

1. 平行平面里哪一条线决定方向？
2. 哪一条线故意保持或反向，避免整块滑动失去句法？
3. 低音是跟随平面、保持 pedal，还是提供另一个目标？
4. 返回时保留音程外形，还是保留声响密度，哪一项更重要？

下面的模型把五组四音纵向 sonorities 写成上移的平面，同时让低音走另一条 C–B–B♭–A–A♭–E♭ 路线。最后停在 E♭，不是回到开头 C；返回的可能性由低音与音区留下，而非首尾和弦相同。

<!-- opusloom:example
{
  "id": "debussy.model.parallel-planes",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["debussy-delone-contrapuntal", "omt-impressionism"],
  "rights": "OpusLoom original teaching model. It does not reproduce Debussy's Reflets dans l'eau or any protected score encoding.",
  "source_locator": "Mechanism derived from the chapter's reading of Reflets dans l'eau mm. 1-2 and 66-70; pitches and rhythm are original",
  "context": "Three-bar piano model: an ascending parallel surface, a separate chromatic descent, and a bass goal that does not restore the opening sonority."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new PianoStaff <<
    \new Staff = "upper" \relative c' {
      \clef treble
      \time 4/4
      \tempo "Modere" 4 = 66
      <c ees g bes>2 <des f aes c> |
      <d fis a cis>2 <ees g bes d> |
      <f aes c ees>1 |
    }
    \new Staff = "lower" \relative c, {
      \clef bass
      \time 4/4
      c2 b |
      bes2 a |
      aes2. ees4 |
    }
  >>
  \layout { }
  \midi { }
}
```

右手三小节实际上只走 C、D♭、D、E♭、F 五级起点，它们都是七和弦外形，但包含小七和弦与大七和弦，并非严格保持全部半音间距的平行移位；左手则以半音下降后再落到 E♭。听者可以同时感到“上方整块移动”和“下方仍有目的”。如果把左手也写成一一对应的平行七和弦，两层的共同运动可能融合成一个更厚的平面，返回方向就需要由其他参数承担。

这也提供反例：平行和弦不会自动产生空间。若每小节在低音、节奏和声部数量上同步变化，和声可能只剩换色；若整页只有一个和弦外形，隐含线也不移动，则上方高低变化会塌成静态 pedal。

## 《帆》：用节奏和音区分开同一集合

《帆》常被整体概括为全音阶作品，但 DeLone 对第 10–18 小节的观察更具体：在 0、2、4、6、8、10 的 pitch set 内，上方动机以平行大三度移动，下方则用八度或平行的 augmented triads；两个动机进入时节奏错开，听觉主要靠独立节奏和 registral-timbral contrast 分开，而不是依靠传统 consonance–dissonance 对立。

这给写作一个有边界的操作：

| 参数 | 上方角色 | 下方角色 | 若两者相同会怎样 |
| --- | --- | --- | --- |
| 音程外形 | 平行三度 | 八度／增三和弦 | 音色与轮廓融成一层 |
| 节奏 | 一组独立分组 | 另一组错位进入 | 入口失去辨识 |
| 音区 | 固定高处 | 较低或 pedal | 共同音集听成厚块 |
| 和声目标 | 局部色彩 | 持续重心与张力 | 全音材料缺少方向 |

全音集合并不规定哪一条线是旋律。它可以提供共同词汇，节奏和音区决定角色。这里也不能推出“所有使用全音阶的作品都漂浮或无功能”：集合只是一组可用音级，局部中心音、bass pedal、重复音的落点和段落返回仍然需要单独判断。

《大海》显示出另一种尺度。柏林爱乐节目说明把第一乐章描述为从幽暗、稀疏的开头逐层增加密度，末尾在 D♭ 的明确基础上达到“正午”；第二乐章则以颤音、重复音、glissandi 和快速跑动连成 wave-like motifs，避免单一古典主题连续发展；第三乐章同时使用 chromatic sequences、五声音阶和类似 gamelan 的乐器色彩。三者的共同点不是同一和弦类型，而是“持续层—运动层—色块层”之间不断交换职责。

## 音色怎样参与结构

Claude Abromont在《牧神午后前奏曲》分析的“Les thèmes”和“Leitmotive”部分，区分长笛主题、第37小节的不同双簧管主题，以及第82小节由双簧管接过的L1片段。后者的音程跨度也缩窄，不能把不同主题与同一片段的变体混为一谈。这些是作者的具体分析，不构成所有乐器必须轮流演奏动机的规则。更有用的判断是：转移是否造成了段落入口、回忆、拟人、距离或高潮。如果没有功能变化，配器只是一种替换。

下面的原创三声部模型让同一个四音单元从长笛移到双簧管，再移到小提琴。小提琴把G4跨前两小节保持，双簧管将同一音程轮廓移低一个八度；末尾三件乐器各持一个单音，合成C–E–G音组。这样，音色转移与共同音保持同时发生，句子仍有记忆锚点。

<!-- opusloom:example
{
  "id": "debussy.model.timbre-transfer-strata",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "conservatoire-paris-debussy-prelude",
    "berliner-philharmoniker-debussy-la-mer"
  ],
  "rights": "OpusLoom original orchestration study. No Debussy theme, score excerpt, recording, or source image is included.",
  "source_locator": "Principle derived from the documented oboe transfer of the Prelude's flute theme and La Mer's stratified orchestral texture; pitches and rhythm are original",
  "context": "Four-bar concert-pitch study. C-D-E-G moves flute to oboe one octave lower then violin; violin G4 is tied across bars1-2. Final flute E5/oboe C5/violin G4 form one ensemble sonority; no wind chords."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Flute" midiInstrument = "flute" } {
      \time 4/4 \tempo "Modere" 4 = 72
      c''8 d'' e'' g'' r2 | R1 | R1 | e''1\fermata |
    }
    \new Staff \with { instrumentName = "Oboe" midiInstrument = "oboe" } {
      \time 4/4 R1 | c'8 d' e' g' r2 | R1 | c''1\fermata |
    }
    \new Staff \with { instrumentName = "Violin" midiInstrument = "violin" } {
      \time 4/4 g'1~ | g'1 | c''8 d'' e'' g'' r2 | g'1\fermata |
    }
  >>
  \layout { }
  \midi { }
}
```

第1小节长笛演奏C5–D5–E5–G5，小提琴保持G4；第2小节双簧管在低八度接手，小提琴的G4仍持续。第3小节小提琴回到C5–D5–E5–G5，最后三声部分别保持E5、C5、G4，合成C–E–G音组。这个模型只证明“怎样让音色转移可追踪”。MIDI 能播放音高时值，不能证明真实乐器的 blend、呼吸、弓压、厅堂混响或听觉层级。

## 跨段结构：先看什么被保留

四件作品可以按结构问题而不是风格词比较：

| 作品 | 表面特征 | 跨段保留项 | 返回时的变化 | 不能从短段推出什么 |
| --- | --- | --- | --- | --- |
| 《水之倒影》 | 平行三音和弦、独立下行层 | 隐含下行线与音区关系 | 材料回到 D♭ 附近时由新的运动段强调 | 不能把全部曲式归结为 D♭ 循环 |
| 《帆》 | 全音集合、错位动机、低音 pedal | 音程外形与节奏身份 | 两组动机的错位与密度改变 | 全音材料不等于无中心或无法分句 |
| 《大海》 | 分层音色、Waves、chromatic sequences | 运动型潮汐形状、pedal 与音区目标 | 第一乐章由稀疏到 D♭ 的明亮密度；末乐章在多种素材中重组能量 | 不能用标题直接证明未读段落的形式功能 |
| 《牧神午后前奏曲》 | 长笛主题、亲密配器、音色回声 | 主题轮廓与 timbral identity | L1片段在第82小节缩窄音程并转交双簧管 | 不能把一次转移概括为全曲轮奏 |

如果新作需要“漂移而不散”，可以先写一张四列表：背景 pedal、运动层、色块层、返回时会变化的目标。每一列只要求一个可听证据。这样的计划比写“Debussy-like harmonies”更可审阅。

## 迁移步骤与反例

1. **选一层背景**：持续音、重复和弦或极慢的声部线。写清它在哪些小节真正持续，何时被重新解释。
2. **选一层运动**：快速分解、颤音、错位动机或 glissando-like sweep。它需要自己的轮廓，否则只是噪点。
3. **选一个隐含线**：即使和弦整体平行，也让最高、最低或内声部保持可追踪的方向。
4. **安排一次音色职责变化**：在动机转移时保留一个共同音、节奏型或音程外形，让听者知道“同一性”在哪里。
5. **让返回加入新功能**：返回可以是背景重新变厚、低音出现新支点、色块改由另一组乐器承担，或片段被缩短。

常见反例包括：所有和弦都按同一音程移动，导致每个落点功能相同；把全音阶、五声音阶和 octatonic 材料随意叠放，却没有中心与转换规则；让每种乐器轮流演奏短句，但没有段落目标；以及在 MIDI 中把弦乐 tremolo、管乐 flutter-tongue 或钢琴踏板写成普通时值，再把技术标签当作已经实现的音色。

## 证据边界

《水之倒影》和《帆》的位置与解释主要来自 DeLone 的论文，属于该作者的分析；本章没有使用其图片或谱图。《大海》的段落叙述来自 Susanne Stähr 的机构节目说明；机构 note 支持作品层面的观察，但不等同于完整乐谱校勘。《牧神午后前奏曲》的乐器转移来自Claude Abromont在巴黎音乐学院网站发表的分析文章；本章只采用其有限的轮廓证据。

本章没有整体核对德彪西所有钢琴或管弦作品中是否存在同一组织体规则。模型也不是作品摘录；它们只展示如何把观察转成可写的操作。跨到真实配器时，还要检查每件乐器的音区、可延续性、移调和可听度。

### 来源

- `debussy-delone-contrapuntal`：Peter DeLone，*Claude Debussy, Contrapuntiste Malgre Lui*，*College Music Symposium* 17（1977），对《水之倒影》开头、第 66–70 小节和《帆》第 10–18 小节的讨论。
- `berliner-philharmoniker-debussy-la-mer`：Susanne Stähr，柏林爱乐《大海》节目说明。
- `conservatoire-paris-debussy-prelude`：Claude Abromont，巴黎音乐学院网站的《牧神午后前奏曲》分析，Les thèmes与Leitmotive小节。
- `omt-impressionism`：开放教材对 modes、extended sonorities、parallelism 与 planing 的术语说明。
