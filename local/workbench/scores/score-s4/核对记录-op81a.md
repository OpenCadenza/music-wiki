# 核对记录：贝多芬 Op. 81a《告别》第一乐章 mm. 1–25

## 交付物
- `beethoven-op81a-mvt1-mm1-25.ly` → 已用 LilyPond 2.26.0 编译（`.pdf` / `.mid`）。
- 谱源副本：`resources/scores/score-s4/beethoven-op81a/`

## 谱源
| 用途 | 来源 | 位置 |
| --- | --- | --- |
| 主谱源（MusicXML） | DCML 语料 `beethoven_piano_sonatas/MS3/26-1.musicxml` | `https://gitub.u-bordeaux.fr/scrime/score-edition/dcml_corpora_musicxml_exports/-/raw/main/beethoven_piano_sonatas/MS3/26-1.musicxml`；副本 `dcml-26-1.musicxml`（downloads 目录） |
| 交叉核对（Humdrum） | Craig Sapp kern，`kern/sonata26-1.krn` | `local/resources/scores/source-packages/beethoven-score-sources/.../kern/sonata26-1.krn` |
| 版面核对 | Noctave 版（底本 MuseScore/PjDMX hjings，据 Clementi 1811 初版校订，并逐音对照 Sapp kern 与 Breitkopf 1862） | `https://noctavepiano.com/partitions/beethoven-adieux-1/beethoven-adieux-1.mxl`（PDF 已缓存，`adieux-p1.png` 已生成） |
| 版面核对（首系统） | IMSLP：Breitkopf & Härtel Serie 16 No.149 首页预览 | `https://cn.imslp.org/wiki/Piano_Sonata_No.26,_Op.81a_(Beethoven,_Ludwig_van)` |

## 转换路径
DCML `26-1.musicxml` → 抽取 mm. 1–25 → 去 words/dashes/pedal → 修补版 musicxml2ly `--absolute` → 重排 PianoStaff（加 `\tempo "Adagio"`、m.17 `\break` + `\tempo "Allegro"`）→ 英式音名、PianoStaff、GM0、每小节 `| % N`。

## 核对结论
- **小节与拍号**：Adagio 2/4 = mm.1–16（m.16 双纵线；kern `*M2/4`、MM60）；m.17 起 Allegro 2/2（kern `*M2/2`、MM220）。与文章占位“mm.1–16 Adagio / m.17 起 Allegro”一致。
- **音高**：DCML 与 kern 逐小节音高多重集合比对 **24/25 小节一致**；唯一差异在 **m.9**：kern 内声部多一个 E4（kern m.9 第 2 拍），DCML 与 Noctave 均无此音 → 判定为 kern 侧的编辑性差异，本谱例采用 DCML/Noctave 读法（已在谱例注释中未改动，仅此记录）。
- **m.19 差异**：Noctave 对 m.19 的 A♭/B♭ 记谱与延音线呈现不同（3.0 时值合并），DCML 与 kern 在 m.19 完全一致（15 音）→ 以 DCML/kern 为准。
- **MIDI 自检**：MIDI 358 = XML 365 − 7 个延音线续音（tie stop=7），吻合；`\barNumberCheck` 无告警。
- **力度/运音**：Adagio 的 *p espressivo*、cresc.（wedge）、sfz、sf、fp，Allegro 的 f、sf、cresc./dim. 均按源保留（文字 cresc./dim. 因 converter 缺陷未以文字输出，以楔形记号 + 源文本在源 XML 中保留）。

## 备注
- Noctave 版说明（其页面）：“After sixteen bars of Adagio, the Allegro sets off … in two beats to the bar”，与本谱例 m.17 起的 2/2 一致。
