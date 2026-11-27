# score-r6 工具与核对记录（第六轮 · 莫扎特方向）

本目录是第六轮谱例助手（`score-mozart`）为补齐莫扎特钢琴/协奏缺口写的转换与核对工具。
所有输出都是**本项目自编码的 LilyPond 摘录**；底本数据只留在 `local/origin_resources`（已被
`.gitignore` 忽略），不随站点发布。

## 〇、复用它之前先读：三条底本读取约定（都是踩过的坑）

1. **CCARH md2 的降号是 `f` 后缀**（`Ef6`=E♭6、`Bf5`=B♭5），不是 `-`；本库 K.467 第一乐章共 1089 处。
   只按 `-` 读会把降号**静默当成休止**（`mozart-k467-i-mm9-28` 首版就因此漏了 mm.18–19 的 E♭6）。
   必须同时认 `#` / `f` / `n` / `-`（`md2parse.PITCH_RE` 与 `md2ly.split_tok` 已改好）。
2. **解析器遇到认不出的音高记号要直接抛错**，不要降级成休止或跳过（`md2ly.part_to_ly` 有硬保护）。
3. **必须做行计数对账**：按 raw 分谱块逐小节数音符行，与解析结果的实音数逐小节比对
   （本轮 Vln1 202/202、Vln2 197/197、Vc 101/101），并给每小节写 `|` 让 LilyPond barcheck 兜底。
   只做「MIDI 音高集合 vs 同源解析结果」的自比对**抓不到丢音**——期望集与产物可能出自同一个错误解析器
   （本轮 abc2ly 的八度错误和 md2 的降号错误都是这么暴露的：前者靠 MIDI 与*独立*底本比，后者靠 barcheck + 外部核对）。

## 一、工具

| 文件 | 作用 |
| --- | --- |
| `abc2ly.py` | hum2abc（Craig Sapp，CCARH kern → ABC）多声部 ABC → LilyPond。支持 `[V:n]` 分轨、`[K:clef=]`、`[I:setbarnb]`、数字/斜杠时值、附点、`-` 连音线、`()` 连奏、`><` 破节奏、`[]` 和弦、`&` 层叠、`z/x` 休止、`!装饰!`/`.`/`{}`、`^_=` 临时记号、`(3` 三连音。LilyPond 自带的 `abc2ly` 会把每小节拆成 cadenza measure 并丢拍号，故自写。 |
| `md2parse.py` / `md2ly.py` | CCARH MuseData stage-2（`.md2`）解析 → LilyPond：分谱、小节、音高（C4=中央 C）、时值（按 `$ Q:` divisions）、连音线、装饰音跳过、非标准时值按 `\tuplet 3/2` 归组。 |
| `dcml2ly.py` | DCML notes.tsv → 钢琴谱 LilyPond（按 `staff`/`voice` 分层、同 onset 合成和弦、缺拍补休止）。 |
| `mxl_dump.py` / `dcml_dump.py` | 把 MusicXML / DCML TSV 读成「每小节音高多重集」。 |
| `compare.py` | ABC 底本 vs DCML 音符表，逐小节音高多重集比对（可合并两谱表，容忍跨谱表记谱）。 |
| `verify_midi.py` / `verify_all.py` | 编译产物 MIDI 的全部 note-on 音高集合，与底本音高集合回比对。 |
| `build_abc_fences.py` / `build_k467.py` | 按目标表生成围栏草稿（写到 `local/workbench/tmp/mozart-r6/`，该目录被忽略）。 |
| `extract_ly.py` | 从围栏草稿抽出 `.ly` 以便本地编译自测。 |
| `insert_fences.py` / `update_provenance.py` | 按占位行原文整行替换围栏/跨文链接、按占位行前缀替换 provenance 谱例行。 |
| `audit_k467_mm1_8.py` | 把既有 `mozart-k467-i-mm1-8` 围栏与 md2 逐小节对音高，复核其声部分配。 |

## 二、本轮交付的 10 块围栏

| id | 作品/乐章 | 定位 | 所在正文 |
| --- | --- | --- | --- |
| `mozart-k331-i-theme-mm1-8` | K.331 I | Thema，mm.1–8 | techniques/structure/variation-types-and-structural-transformations.md |
| `mozart-k331-i-var1-mm19-26` | K.331 I | Variation I，mm.19–26 | 同上 |
| `mozart-k331-i-var3-mm55-72` | K.331 I | Variation III（Minore），mm.55–72 | 同上 |
| `mozart-k545-i-mm5-8` | K.545 I | mm.5–8 | techniques/structure/cadential-prinner-and-structural-closure.md |
| `mozart-k545-i-mm22-26` | K.545 I | mm.22–26 | techniques/harmony/cadential-six-four-and-dominant-syntax.md |
| `mozart-k545-i-mm29-42` | K.545 I | 展开部 mm.29–42 | techniques/structure/sequence-mechanics-and-syntactic-functions.md |
| `mozart-k332-i-mm41-56` | K.332 I | mm.41–56 | techniques/structure/compound-period-hierarchical-syntax.md |
| `mozart-k284-ii-mm1-16` | K.284 II | mm.1–16 | 同上 |
| `mozart-k494-mm1-6` | K.494 回旋曲 | mm.1–6 | techniques/structure/phrase-expansion-and-structural-skeleton.md |
| `mozart-k467-i-mm9-28` | K.467 I | mm.9–28 | techniques/structure/concertante-principle-and-double-exposition.md |
| `mozart-k545-i-mm1-14` | K.545 I | mm.1–14 | techniques/harmony/harmonic-rhythm-and-syntactic-pacing.md（第六轮补派 task-5；与 `mozart-k545-i-mm5-8` 重叠 4 小节，provenance 已注明用途区别） |

## 三、核对记录

### 3.1 底本

- K.331 / K.332 / K.284 / K.545：`local/resources/scores/source-packages/humdrum/mozart-sonatas/*.abc`
  （hum2abc 由 CCARH Humdrum kern 转出；`N:` 行给出对应 `sonataNN-M.krn`）。
- K.494：`local/origin_resources/sources/dcml-mozart-sonatas/raw/K533-3.notes.tsv`（DCMLab 语料，
  即 K.533/494 末乐章回旋曲）；并用 Open Music Theory 仓库 `Graphics/form/XML/k494.mxl` 教材谱例核对定位。
- K.467 I：`local/origin_resources/sources/ccarh-musedata-concertos/mozart-k467-mvt1.md2`。

### 3.2 独立回比对（音高多重集）

| 对象 | 比对方式 | 结果 |
| --- | --- | --- |
| ABC 解析器校准（K.283 I mm.1–10） | 与 Open Music Theory `mozart, k283.xml`（独立排版）逐小节比 | 10/10 小节完全一致（XML 首小节是弱起，整体错一小节对齐） |
| K.545 I mm.1–45 | vs `notes/K545-1.notes.tsv` | 43/45 小节·声部一致；m.23 底本把回音写成显式还原 G（`=g`）而 DCML 记作 G♯，m.25 为长颤音的记法差异 |
| K.331 I mm.1–18（1a） | 同上 | 16/18 一致（m.8 底本用连线代替一处重复音、m.10 装饰音写法差异） |
| K.331 I 变奏一 mm.19–26（1b） | 同上 | 14/16 一致（6/8 小节全部一致，两小节仅装饰音写法差异） |
| K.331 I 变奏三 mm.55–72（1d） | 同上（按 mn 55–72 对齐） | 16/18 一致 —— 同时据此确认 1d 起点就是刊本 m.55 |
| K.332 I mm.41–56 | 同上 | 11/16 一致，其余差异均为底本倚音/装饰音（谱例不展开装饰音）与一处连线写法 |
| K.284 II mm.1–16 | 同上 | 12/16 一致，其余差异在 `&` 三层叠置与连线写法，音高集合相同 |
| K.494 mm.1–6 | vs OMT `k494.mxl` | mm.1–4 完全一致；m.5–6 教材谱例对伴奏写法有简化，本谱例按 DCML 原谱编码 |
| K.467 I mm.9–28 | md2 即底本本身；比对外部无同类源 | 原始行计数 vs 解析计数逐小节一致（Vln1 202/202、Vln2 197/197、Vc 101/101）；生成后 MIDI 音高 498 个 vs 底本 500（2 个为连音线在 MIDI 中合并），集合完全一致 |

### 3.3 编译与音高终检

- 10 块围栏全部 `lilypond` 编译通过，且每小节末尾写了 `|`（小节线自检），**无 barcheck 警告**，说明每小节时值确实填满。
- `verify_all.py`：把每块围栏生成 MIDI 的 note-on 音高集合与底本音高集合比对，**10/10 集合一致**；
  音数差只出现在连音线（LilyPond 在 MIDI 中合并）与被跳过的装饰音。
- 过程中修正过两个真实缺陷：
  1. `abc2ly` 的绝对八度曾整体低一个八度（LilyPond `c'` = 中央 C，实测 MIDI 60），由 MIDI 回比对发现并改正。
  2. `md2parse`/`md2ly` 只认 `-` 作降号，而**这批 md2 用 `f` 后缀写降号**（如 `Ef6`=E♭6，全文件 1089 处），
     导致 K.467 I mm.18–19 的 E♭6 被静默当休止——由 materials 的逐分谱核对（m.18 C6/E♭6、m.19 E♭6/C♯6/D6/C6）
     与 barcheck 报错同时暴露，已改正并重出该围栏；`md2ly` 现对认不出的音高记号直接报错，不再静默丢弃。
     改正后 K.467 mm.9–28 围栏已整块替换，并补登 provenance 谱例行。

### 3.4 复核既有围栏（非本轮交付）

`audit_k467_mm1_8.py` 把既有 `mozart-k467-i-mm1-8` 围栏与 md2 逐小节对音高：定音鼓、双簧管 I/II、
大管 I、圆号 I、小号 I 均 8/8 一致；第一小提琴与大提琴各 6/8，不一致的两小节（m.2、m.4）只是多出一处
重复音（底本用三连音写法）。**该围栏与底本无实质冲突**，本轮未改动。
