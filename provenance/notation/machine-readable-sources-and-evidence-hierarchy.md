# 谱源可信度阶梯

- 文章：`content/notation/machine-readable-sources-and-evidence-hierarchy.md`
- 许可：公有领域（详见两表）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| 早期人工转写 `.ly` 资产独立校勘记录 | `local/workbench/scores/assistant-scores-c/旧谱核验报告.md` | 解剖 5 份旧工程 .ly 文件的音高伪造、八度倒错、调号静默错音与运音法篡改等真实事故，作为 Level 4 案例分析基础 |
| 贝多芬弦乐四重奏 Humdrum Kern 语料库 | `local/resources/scores/source-packages/beethoven-score-sources/beethoven-string-quartets-main/beethoven-string-quartets-main/kern/quartet16-4.krn`、`quartet10-1.krn`、`quartet15-1.krn` | 贝多芬 Op. 135（m.13 中提琴 C3 / 大提琴 C2）、Op. 74（mm. 6–9 物理音区与变音记号绑定）、Op. 132（mm. 1–8 半音卡农细胞时间行矩阵对齐）实证依据，作为 Level 1 机器原生语料代表 |
| 洛桑联邦理工学院（DCML）和声标注数据集 | `n15op132_01.harmonies.tsv`、`n16op135_04.harmonies.tsv`、`metadata.tsv`（本工作树无独立副本，引自 DCML 官方规范） | Level 1 分层和声解耦（和弦音/加音/根音/低音）与双重同行复审（annotators / reviewers）机制的学术依据 |
| Mutopia Project 权威校勘工程源码 | `SchubertF/D328/Erlkoenig/Erlkoenig.ly`（基于 C.F. Peters Band I 历史底本；本工作树无独立副本，引自 Mutopia 源码） | 舒伯特《魔王》（D. 328）前奏与展开部短跳音（staccatissimo）及复调织体实证依据，作为 Level 2 严密受控开源排版源码代表 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `beethoven-op135-iv-mm12-16`（关联引用） | 贝多芬 Op. 135 第四乐章 | Allegro，mm. 12–16 | 音乐公有领域；参考 Humdrum Kern `quartet16-4.krn` 与 DCML `n16op135_04.mscx`，谱例收录于《核心细胞》 | 未确认 |
| `beethoven-op74-i-mm1-9`（校勘对照样例） | 贝多芬 Op. 74 第一乐章 | Adagio，mm. 1–9 | 音乐公有领域；参考 Humdrum Kern `quartet10-1.krn` | 未确认 |
| `schubert-d328-mm1-5`（校勘对照样例） | 舒伯特《魔王》D. 328 | mm. 1–5 | 音乐公有领域；参考 Mutopia Project / C.F. Peters Band I 底本 | 未确认 |
