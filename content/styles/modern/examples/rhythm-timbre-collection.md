<!-- music-kb:page {"id": "page.c935836a4ba045429f332d0f78305a8a"} -->
<!-- knowledge: style.modern.rhythm-timbre-collection -->
# 二十世纪不是一种风格：节奏、音色、音集与篇章

二十世纪的西方艺术音乐没有一个能覆盖全部作品的技术核心。斯特拉文斯基可以把节拍组织成不断加减的块面；巴托克能让一个 chromatic fugue 主题贯穿多个乐章；舍恩伯格在《色彩》里可以让 timbral progression 与音高终止错开；梅西安则用有限移调模式、附加时值和不可逆行节奏，把“时间”本身写成曲式问题。用同一个“现代和声”预设解释四者，会把最可检验的差异删掉。

本章比较《春之祭》（1911–13）、《为弦乐、打击乐和钢片琴而作》（1936）、《五首管弦乐曲》第三首《色彩》（1909）与《时间终结四重奏》（1940–41）。这些作品跨越芭蕾、管弦乐和室内乐，不能构成时代样本。它们只说明：节奏、音色、音集与跨段结构可以分别成为主要组织力量，而且经常彼此冲突。

## 节奏：单位可以相加，重音可以重写

《春之祭》的经典段落常以 irregular accents 和频繁更换拍号被记住。柏林爱乐节目说明把“节奏”称为作品突然夺回控制的真正力量：固定脉冲不断被尖锐重音打断，拍号连续变化，和声 footing 也随之被削弱。更精确的写法不是“没有拍子”，而是作曲家一再建立可数的单位，又改变哪些单位组成大组。

为把“可数的脉冲怎样改变分组”写成代码，下面另建一个原创模型：同一小动机依次进入 7/16、5/16、8/16，保留十六分音符脉冲，却让句首和落点改变。这是本库的技法练习，不是《春之祭》某一段的转录；所引节目说明不足以把这些具体分组或 aksak 分类归给原作。

<!-- opusloom:example
{
  "id": "modern.model.additive-accents",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "fragment",
  "midi": true,
  "requires": [],
  "sources": ["berliner-philharmoniker-stravinsky-rite"],
  "rights": "OpusLoom original rhythmic model. It contains no Stravinsky melody or score excerpt.",
  "source_locator": "General mechanism derived from the programme note's discussion of fixed pulses, disruptive accents, and changing metre in The Rite of Spring",
  "context": "Three bars of 7/16, 5/16, and 8/16. Durational totals and accent placement are changed independently while the repeated pitch cells remain."
}
-->
```lilypond
\version "2.26.0"
\time 7/16
\tempo "Presto" 8 = 240
c16-! r16 c8 e16 g8 |
\time 5/16
c16-! e8 g8 |
\time 8/16
c16 e8 g8 c8 e16 |
```

第一小节是 1+1+2+1+2 个十六分；第二小节 1+2+2；第三小节 1+2+2+2+1。音高没有展开成主题，节奏单位先成为主要结构。若把音高完全移除，三小节仍可比较；若把时值全部均分，重复音型会立刻失去那些“推一下、停一下”的边界。

反例是把每个拍号变化都当作高潮。一个作品可以在慢速中维持固定小节、也可以在每种拍号里保持同一分组。只有实际重音与句法改变，才支持“节奏是结构参数”的判断。MIDI 能读出时值，不能证明现场重音、弦乐 attack 或铜管 articulation 是否足够清楚。

## 跨乐章材料：一个主题可以换形态继续

巴托克《为弦乐、打击乐和钢片琴而作》把两套弦乐团置于 percussion 两侧，空间本身成为配器条件。节目说明指出，第一乐章从两组 violas 的 fugue subject 开始；材料经过低声部、antiphonal strings、timpani 和 cymbals 推向紧张高点，之后 subject 以 inversion 出现，celesta cascades 改变它的音乐空间。第三乐章的 night music 也取材于第一乐章主题，终曲在 Bulgarian rhythm 与快速换拍中再次召回它。

这提供的是跨段关系，而不是单一主题的逐句复述：

| 出现阶段 | 主题动作 | 新的音乐职责 |
| --- | --- | --- |
| 第一乐章开头 | 半音起伏的 fugue subject | 建立不确定调性与模仿空间 |
| 第一乐章后段 | inversion、celesta、muted strings | 把展开后的张力变成高层音区的回声 |
| 第三乐章 | 局部材料转入 night-music 织体 | 主题不再是 fugue，而成为背景性的记忆 |
| 终曲 | 变体召回、dance rhythm、换拍 | 主题参与终曲的方向与结束 |

前后材料相似并不能自动证明“整部作品都在严格循环”。必须指出哪些音程或节奏被保留，哪些调式、配器与句法被改写。把“主题回来”写成抽象标签，不如列出至少一项可听保留项与一项功能变化。

## 音色：当变化率与终止共同组织段落

舍恩伯格《色彩》常被直接等同于 Klangfarbenmelodie。Matthew Zeller 的研究避免把“换乐器”当作充分条件。他把 timbral progression 看成有方向的变化，把 timbral cadence 看成由音色进程提供到达或稳定的终点。其分析把作品的形式节段放在第 11–12 与第 30–31 小节附近：第 11 小节由低频持续声、clarinet line、弦乐 punctuation 与 fermata 共同完成第一次 timbral arrival；第 30 小节又用 harp、celesta 和 string harmonics 形成更大的终止，然后回到开头 organism 的 timbral profile。

关键不是“所有乐器轮流拿和弦”，而是音色变化的速率、音符共同性、配器的融合与分离以及终止时间互相配合。Zeller 特别指出，音高到达可以早于 timbral arrival；形式边界因此可由音色完成，即使 pitch process 已暂时停住。

下面的四小节自编模型使用音级集合[0,1,4,6,9]，由稀疏线条、重叠进入转向共同长音。它没有复制《色彩》的音高；末尾同时延长和停顿只是本模型安排的分段线索，不足以重建原作的音色终止。

<!-- opusloom:example
{
  "id": "modern.model.timbre-transfer",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": [
    "zeller-2023-farben",
    "berliner-philharmoniker-stravinsky-rite"
  ],
  "rights": "OpusLoom original orchestration model. No Schoenberg, Stravinsky, or third-party score, recording, or article image is reproduced.",
  "source_locator": "Timbral-function mechanism derived from Zeller's discussion of Farben, especially mm. 11, 20-25, and 30",
  "context": "Four-bar original concert-pitch study using pitch classes [0,1,4,6,9]. Sparse lines overlap, change leading roles and converge in a held sonority; monophonic wind parts. Not a Schoenberg transcription or proof of a historical timbral cadence."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new StaffGroup <<
    \new Staff \with { instrumentName = "Flute" midiInstrument = "flute" } {
      \time 4/4 \tempo "Lent" 4 = 52
      c''2 cis''2 | e''1 | R1 | e''1\fermata |
    }
    \new Staff \with { instrumentName = "Oboe" midiInstrument = "oboe" } {
      \time 4/4 R1 | r2 fis'2 | a'1 | c''1\fermata |
    }
    \new Staff \with { instrumentName = "Violin" midiInstrument = "violin" } {
      \time 4/4 a'1~ | a'1 | fis''2 e''2 | cis''1\fermata |
    }
  >>
  \layout { }
  \midi { }
}
```

第一小节长笛C5–C♯5与小提琴A4组成两层；第二小节双簧管F♯4在后半进入，小提琴A4继续保持；第三小节由小提琴F♯5–E5取得较快运动，长笛休止。末小节三个声部分别保持E5、C5、C♯5，单声部管乐共同构成纵向音组。这里可检查的是进入、退出、共同持续与停止的时点；感知上是否构成音色到达，仍需听觉与更大段落支持。

反例有三类：同一旋律只是换音色，却没有段落功能变化；持续音与音色变化不同步却没有任何对应关系；以及把 timbre cadence 和 tonal cadence 混成同一个概念。Zeller 的框架是特定分析承诺，不能扩大为所有 twentieth-century 配器的统一规则。

## 音集：集合关系只说明部分组织

音级集合分析把音高类别从八度、节奏和配器中抽象出来。Open Music Theory 区分 pitch-class set、normal order、transposition 与 inversion；这些工具能说明两段材料是否保持相同音程结构，却不自动说明哪个音是中心、哪件乐器承担旋律、何时形成段落。分析集合后仍要回到实际谱面。

下面的模型使用五音集合 `{0,1,4,6,9}`，先以 C 为 bass axis，再整体 T3 移位到 E♭。旋律外形、时值和节奏身份不变，bass 与其他声部一起移动。集合与动机保持，中心与音区环境改变。

<!-- opusloom:example
{
  "id": "modern.model.collection-transposition",
  "status": "published",
  "source_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["omt-pitch-class-set", "zeller-2023-farben"],
  "rights": "OpusLoom original pitch-class exercise. It does not quote a twentieth-century work.",
  "source_locator": "Conceptual model using pitch classes [0,1,4,6,9] and transposition T3; pitches and rhythm are original",
  "context": "Two-bar model. The five-note collection and melodic contour repeat under transposition while a bass axis moves from C to E-flat."
}
-->
```lilypond
\version "2.26.0"
\score {
  \new PianoStaff <<
    \new Staff = "upper" \relative c'' {
      \clef treble
      \time 4/4
      c8 cis e fis a fis e cis |
      ees8 e g a c a g e |
    }
    \new Staff = "lower" \relative c, {
      \clef bass
      \time 4/4
      c1 |
      ees1 |
    }
  >>
  \layout { }
  \midi { }
}
```

第一小节音级为 C、C♯、E、F♯、A；第二小节依次为 E♭、E、G、A、C，正是原集合的 T3。音程关系与旋律轮廓仍然可辨，低音重心却改变。若把第二小节改写成普通 V–I 终止，集合外形可能仍在，听感与句法已经换成完全不同的组织；若 bass 原地不动，所谓“移位”也可能只像局部色彩。

集合分析的反例包括：看见五个音就强行命名，不问它们在作品里是否形成结构单位；忽略重复音造成的中心感；把集合等价当作全曲形式证明；以及用一套集合描述替代乐器法与节奏。集合是一种观察层，不能吞掉其他参数。

## 篇章：终止、返回和“时间”分别怎样成立

四部作品给出不同的大尺度关系：

| 作品 | 主要组织参数 | 跨段证据 | 终止或返回 | 不能外推的规则 |
| --- | --- | --- | --- | --- |
| 《春之祭》 | 脉冲、重音、拍号块面、音色爆发 | 小型 cells 在场景与段落中重新组合 | 通过积累、突然停顿与重新启动收束 | 频繁换拍不是作品成立的充分条件 |
| 巴托克《为弦乐、打击乐和钢片琴而作》 | fugue、空间配器、inversion、night music、舞蹈节奏 | 第一乐章 subject 在后乐章转义 | inversion 与终曲变体共同回应开头 | 主题相关不能证明四个乐章同一曲式 |
| 舍恩伯格《色彩》 | timbral progression、timbre cadence、同时存在的音高层 | Zeller 读作 ABA′，边界约在 mm. 11–12 与 30–31 | 开头 timbrality 在结尾变体回归，以 fade-out 而非强终止 | 每次换乐器不构成色彩旋律 |
| 梅西安《时间终结四重奏》 | 不可逆行节奏、有限移调模式、附加时值、鸟歌、极慢速度 | 八乐章从不同角度处理时间与永恒 | 运动常被长音、停顿或不同时间尺度切断 | 节奏技术不决定作品的情感与宗教意义 |

梅西安的八乐章不是同一形式的八次重复。Diane Luchese 对 Anthony Pople 研究的评述列出 non-retrogradable rhythm、modes of limited transposition、rhythmic pedal、added values 与 inexact augmentation/diminution；同时提醒，“不可逆行”表示节奏序列正反向阅读相同，不等于全曲不会前进或返回。洛杉矶爱乐节目说明中，Messiaen 又把 birdsong、极慢 cello melody 与 unison trumpet movement 分配给不同时间经验。技术模式必须与体裁、速度、配器和篇章位置一起解释。

同样，斯特拉文斯基把不规则重音集中成短暂块面；巴托克让 irregular dance rhythm 进入一个由 fugue subject 统一的多乐章网络；舍恩伯格让音色进程自己形成 cadence；梅西安让不同的时间尺度在八段中并置。把它们都说成“无调性”会漏掉三件调性或模式因素，也不能解释节奏和配器为何如此不同。

## 迁移检查表

新作若只写“20世纪风格”，无法验证。应先选一至两个主要参数，并给每个参数建立检查条件：

| 参数 | 起草问题 | 通过条件 | 典型失败 |
| --- | --- | --- | --- |
| 节奏 | 脉冲、最短单位和 group lengths 是什么？ | 重音与句法可由时值关系解释 | 只是每小节任意换拍 |
| 音色 | 哪个音色变化率或 arrival 构成段落边界？ | 至少一项共同身份与一项职责变化并存 | 无方向地轮流配器 |
| 音集 | 集合在哪里成立，哪一段转换，bass 与音区如何？ | 集合关系可回到可听材料 | 只有和弦清单，没有段落作用 |
| 跨段 | 什么被认出，返回时承担什么新功能？ | 保留项与变化项均可指出 | 把曲名或标签当连续证据 |

把这些检查写进草稿后，再编译和看谱。MIDI 可以核对音高与时值，不能证明真实乐器的 blend、空间距离、percussion attack、富有表现力的时序，也不能证明某一历史解释成立。

## 证据边界

本章对《春之祭》的段落级描述来自 Kerstin Schüssler-Bach 的机构节目说明；rehearsal numbers 由本章补充，未把节目说明当作完整乐谱分析。巴托克作品的跨乐章关系来自 Orrin Howard 的作品说明。舍恩伯格的形式判断明确归属于 Zeller，并保留其 ABA′、mm. 11–12 与 30–31 的分析范围。梅西安的技术清单来自 Luchese 对 Pople 的评述；节目说明中的八乐章标题与作曲家自述来自洛杉矶爱乐。

本章没有校对四部作品的历史原稿或比较多个 edition，也没有以录音实验测试 perceive。所有 LilyPond 例子都是原创教学模型；它们不能证明任何作品使用了相同音高，也不构成对作品实际声响的重建。

### 来源

- `berliner-philharmoniker-stravinsky-rite`：Kerstin Schüssler-Bach，柏林爱乐《春之祭》节目说明。
- `laphil-bartok-mspc`：Orrin Howard，洛杉矶爱乐《为弦乐、打击乐和钢片琴而作》节目说明。
- `zeller-2023-farben`：Matthew Zeller，“Klangfarbenmelodie, Chromophony, and Timbral Function in Arnold Schoenberg's ‘Farben’”，*Music Theory Online* 29.3（2023）。
- `laphil-messiaen-quartet`：洛杉矶爱乐《时间终结四重奏》节目说明，含 Messiaen 的乐章描述。
- `luchese-1999-messiaen-review`：Diane Luchese 对 Anthony Pople 专著的评述，*Music Theory Online* 5.2（1999）。
- `omt-pitch-class-set`：Open Music Theory 关于 pitch-class sets、normal order、transposition 与 inversion 的术语说明。
