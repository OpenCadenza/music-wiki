# 八度歧义与演奏法

- 文章：`content/notation/clef-octave-ambiguity-and-encoding-loss.md`
- 许可：待补

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| 早期人工转写 `.ly` 资产独立校勘记录 | `local/workbench/scores/assistant-scores-c/旧谱核验报告.md` | 解剖 5 份旧工程 .ly 文件在中提琴/大提琴八度倒错、调号静默错音与演奏法篡改等真实事故，作为案例分析基础 |
| 贝多芬弦乐四重奏 Humdrum Kern 官方语料 | `local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet16-4.krn`、`quartet10-1.krn` | 贝多芬 Op. 135（m. 13 中提琴 C3 / 大提琴 C2 物理音区与低音支撑）与 Op. 74（m. 7 大提琴 B♭2 与 m. 9 第一小提琴花彩显式变音字符 `16ee-`）的实证基准 |
| Mutopia Project 权威校勘工程源码 | `SchubertF/D328/Erlkoenig/Erlkoenig.ly`（基于 C.F. Peters Band I 底本；本工作树无独立副本，引自 Mutopia 权威校勘源码） | 舒伯特《魔王》（D. 328）开篇 mm. 1–5 左手八度短跳音（staccatissimo: `re4-| sib-|`）与 mm. 72–76 独唱弱起音（A4: `re2 r4 la`）的实证基准 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `beethoven-op135-iv-mm12-16`（关联引用） | 贝多芬 Op. 135 第四乐章 | Allegro，mm. 12–16 | 音乐公有领域；谱源基于 Humdrum Kern `quartet16-4.krn`，谱例收录于《核心细胞》 | 未确认 |
| `beethoven-op74-i-mm6-9`（关联引用） | 贝多芬 Op. 74 第一乐章 | Poco Adagio，mm. 6–9 | 音乐公有领域；谱源基于 Humdrum Kern `quartet10-1.krn`，谱例收录于《加兰特图式》 | 未确认 |
| `schubert-d328-prelude-and-vocal`（关联引用） | 舒伯特《魔王》D. 328 | mm. 1–5、mm. 72–76 | 音乐公有领域；谱源基于 Mutopia Project / C.F. Peters Band I，谱例收录于《核心细胞》 | 未确认 |
