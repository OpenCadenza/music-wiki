# 复合乐段

- 文章：`content/techniques/structure/compound-period-hierarchical-syntax.md`
- 许可：待确认（详见两表）

## 引用与出处

| 来源 | 版本/位置 | 在本文的用途 |
| --- | --- | --- |
| Open Music Theory (OMT) | v1 legacy source，章节 "Compound period"、"Hybrid themes" 与 "Cadence types" | 复合乐段概念、大前句与大后句层级升阶机制、三类典型复合模式（句型+句型、混合型1+混合型1、混合型3+混合型3）与终止式层级差序逻辑 |
| Humdrum 莫扎特奏鸣曲库 | `0052-52-Piano Sonata No. 12 in F major, K 332 (300k), mvmt. 1.abc`（Derived from sonata12-1.krn） | 第一乐章 mm. 41–56 副部主题（混合型1+混合型1复合乐段、小前句弱收束、延续句HC、三连音变奏与PAC强终止）声部实据核验 |
| Humdrum 莫扎特奏鸣曲库 | `0017-17-Piano Sonata No. 6 in D major, K 284 (205b), mvmt. 2.abc`（Derived from sonata06-2.krn） | 第二乐章 mm. 1–16 开篇主题（句型+句型复合乐段、呈示句大基础乐念、延续句HC、华彩加花变奏与PAC强终止）声部实据核验 |

## 谱例

| 谱例 id | 作品 | 定位 | 底本 | 许可 |
| --- | --- | --- | --- | --- |
| `mozart-k332-i-mm41-56` | 莫扎特《F大调第12钢琴奏鸣曲》K. 332 第一乐章 | Allegro，mm. 41–56（3/4） | CCARH Humdrum Kern（`sonata12-1.krn` → hum2abc 转出的 ABC，`local/resources/scores/source-packages/humdrum/mozart-sonatas/0052-…mvmt. 1.abc`）；排版为本项目自编码 LilyPond 摘录；回比对 DCMLab《莫扎特钢琴奏鸣曲》语料 `notes/K332-1.notes.tsv`（MS3 转录）：11/16 小节音高多重集完全一致，其余 5 小节差异均为底本倚音/装饰音（谱例不展开装饰音）与一处连线写法 | 据 CCARH 转写，学术用途（非 CC0） |
| `mozart-k284-ii-mm1-16` | 莫扎特《D大调第6钢琴奏鸣曲》K. 284 第二乐章 | Rondeau en polonaise: Andante，mm. 1–16（3/4，A 大调） | CCARH Humdrum Kern（`sonata06-2.krn` → hum2abc 转出的 ABC，`local/resources/scores/source-packages/humdrum/mozart-sonatas/0017-…mvmt. 2.abc`）；排版为本项目自编码 LilyPond 摘录；回比对 DCMLab《莫扎特钢琴奏鸣曲》语料 `notes/K284-2.notes.tsv`（MS3 转录）：12/16 小节音高多重集完全一致，其余 4 小节差异在三层叠置（&）与连线写法，音高集合相同 | 据 CCARH 转写，学术用途（非 CC0） |
