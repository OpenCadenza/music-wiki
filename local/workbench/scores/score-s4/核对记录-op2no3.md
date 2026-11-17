# 核对记录：贝多芬 Op. 2 No. 3 第一乐章 mm. 1–13

## 交付物
- `beethoven-op2no3-mvt1-mm1-13.ly` → 已用 LilyPond 2.26.0 编译（`.pdf` / `.mid`）。
- 谱源副本：`resources/scores/score-s4/beethoven-op2-no3/`

## 谱源
| 用途 | 来源 | 位置 |
| --- | --- | --- |
| 主谱源（MusicXML） | DCML 语料 `beethoven_piano_sonatas/MS3/03-1.musicxml` | `https://gitub.u-bordeaux.fr/scrime/score-edition/dcml_corpora_musicxml_exports/-/raw/main/beethoven_piano_sonatas/MS3/03-1.musicxml` |
| 交叉核对（Humdrum） | Craig Sapp kern，`kern/sonata03-1.krn` | `local/resources/scores/source-packages/beethoven-score-sources/.../kern/sonata03-1.krn` |
| 版面核对（首系统） | IMSLP：Breitkopf & Härtel Band 20（B126）首页预览；亦对照 everythingsheetmusic 条目（Sapp kern→MusicXML 转码） | `https://cn.imslp.org/wiki/Piano_Sonata_No.3,_Op.2_No.3_(Beethoven,_Ludwig_van)` |

## 转换路径
DCML `03-1.musicxml` → 抽取 mm.1–13（无弱起，m.1 = 完整 4/4）→ 去 words/dashes/pedal → 修补版 musicxml2ly `--absolute` → 重排 PianoStaff，加 `\tempo "Allegro con brio"`。

## 核对结论
- **小节与拍号**：C 大调 4/4（kern `*M4/4`、`*MM132`、`*C:`，DCML `fifths 0`、`time 4/4`）；m.1 为完整小节，无 `\partial`。
- **音高**：DCML 与 kern 逐小节多重集合比对 **13/13 完全一致**。
- **MIDI 自检**：MIDI 174 = XML 180 − 5 个延音线续音 − 1 个跨出片段（至 m.14）的 tie 起始（即 180−5−1=174），吻合。
- **句法与文章对照**：mm.1–4 原型前部（I 级四分音符断奏 + V7 复述），mm.5–8 十六分琶音延续，m.8 弱 IAC（高音停三音），mm.8–13 低音下行连接线 + 高八度五小节扩张，m.13 强 I:PAC —— 与文章占位逐项对应，谱面素材与描述吻合（不涉及改动）。
- 未发现无法解释的差异。
