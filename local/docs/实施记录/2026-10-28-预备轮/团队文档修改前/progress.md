# 当前进度与路线图

> 核验日期：2026-10-28
> 本地开发 `main`：`f91f22f7ea333fba405ab380a6861de4aedb44dd`（领先远端 12 个提交）
> 已发布 `origin/main`：`9412a67003a082124b666b1a88ce9157668d0de3`
> 数值来自实际文件统计，不是估算。

## 三轮的定位

| 轮次 | 目的 | 规模 |
| --- | --- | --- |
| 第一轮 | 定形态：验证"选题制 + 真实谱例"能不能写出来 | 5 篇，全部真实谱例 |
| 第二轮 | 验证流水线可复制：换体裁位置、换作品、加大占位比例 | 6 篇，7 个真实谱例 + 4 处占位 |
| 第三轮 | 全量：覆盖贝多芬的主要体裁 | 进行中，已完成四重奏分支 6 篇 |

## 已交付

### 贝多芬钢琴奏鸣曲（17 篇）

| 文章 | 谱例块 | 占位 | 主要作品 |
| --- | ---: | ---: | --- |
| `opening-gestures` | 1 | 0 | Op.13 |
| `motive-tasks` | 1 | 0 | Op.2 No.1 |
| `transition` | 1 | 0 | Op.2 No.1 |
| `secondary-theme` | 2 | 0 | Op.2 No.1、Op.31 No.2 |
| `exposition-closure` | 2 | 0 | Op.10 No.1、Op.2 No.1 |
| `development-techniques` | 2 | 0 | Op.10 No.1、Op.31 No.2 |
| `op90-two-movements` | 2 | 0 | Op.90 |
| `slow-movement-variation` | 1 | 1 | Op.57 II；Op.109 III 待补 |
| `finale-choice` | 2 | 1 | Op.57 III、Op.49 No.2；Op.111 II 待补 |
| `fugue-or-fugato` | 1 | 2 | Op.2 No.1；Op.110 III、Op.106 IV 待补 |
| `late-texture` | 0 | 3 | Op.111、Op.101、Op.106 全部待补 |
| `sonatina-position` | 2 | 0 | Op.49 No.1 I、Op.49 No.2 II |
| `early-experiments` | 1 | 1 | Op.10 No.2 I；Allegretto 待补 |
| `slow-movement-types` | 2 | 0 | Op.31 No.2 II、Op.90 II |
| `scherzo-replaces-minuet` | 2 | 0 | Op.2 No.1 III（Menuetto + Trio） |
| `accompaniment-as-form` | 1 | 0 | Op.27 No.2 I |
| `two-movement-sonata` | 1 | 0 | Op.78 I |

### 贝多芬弦乐四重奏（6 篇）

| 文章 | 谱例块 | 占位 | 状态 |
| --- | ---: | ---: | --- |
| `voice-roles` | 1 | 0 | Op.18 No.4 I mm.1–16 |
| `quartet-texture` | 1 | 0 | Op.59 No.3 II mm.1–16；复调样本链接指向 `quartet-fugue` |
| `inner-voices` | 1 | 0 | Op.18 No.4 I mm.53–68（展开部） |
| `quartet-fugue` | 1 | 0 | 已有一个真实谱例 |
| `cello-melody` | 0 | 1 | 内容完整，谱例待补 |
| `late-quartet-cycles` | 0 | 1 | 内容完整，谱例待补 |

### 其他分支

| 分支 | 篇数 | 文章 |
| --- | ---: | --- |
| 交响曲 | 2 | `orchestration-layers`、`motivic-cell` |
| 室内乐 | 6 | `cello-piano-dialogue`、`violin-sonata-equality`、`five-voice-fugue`、`horn-sonata-writing`、`piano-trio-balance`、`slow-intro-to-allegro` |
| 协奏曲 | 2 | `solo-versus-tutti`、`double-exposition` |
| 序曲 | 1 | `overture-in-one-breath` |
| 技法（跨体裁） | 3 | `postponing-the-cadence`、`motivic-transformation`、`variation-technique` |

### 汇总

| 指标 | 数值 |
| --- | ---: |
| 正文 | 37 |
| 目录页 | 11 |
| 谱例块（已编译） | 51 |
| 待补占位 | 10 |
| `content/` 下 Markdown 文件 | 48 |
| 真实谱例覆盖作品 | Op.2/1、Op.10/1、Op.13、Op.31/2、Op.49/2、Op.57 II/III、Op.90 I/II、Op.111 I、Op.131 |

> 注：以上只统计本地 `main@f91f22f` 已提交内容，不包含工作树中的未提交草稿。线上 `origin/main@9412a67` 落后于该开发快照，发布前按实际 `git ls-tree` 再核对。

## 缺口：10 处占位

按补起来的难度排序：

| 工作量 | 占位 | 说明 |
| --- | --- | --- |
| 中 | `finale-choice` 的 Op.111 II、`slow-movement-variation` 的 Op.109 III | 需从 IMSLP 扫描件转录，或换 Op.49/1 II 等有源作品替代 |
| 中 | `fugue-or-fugato` 的 Op.110 III、Op.106 IV | 同上，晚期奏鸣曲无机器可读源 |
| 中 | `quartets/cello-melody` 的 Op.18 No.2 II | Mutopia 的 `O18/` 只有 No.4，缺 No.2；可换 Op.18 No.4 II（已配货）或另找源 |
| 高 | `late-texture` 三处（Op.111、Op.101、Op.106） | Op.111 的 `\cadenzaOn` 段落小节号与通行版不符，需要重新对齐小节号才能切片 |
| 高 | `quartets/late-quartet-cycles` 的 Op.131 VI→VII | Op.131 源码是 2.6.2 版，`convert-ly` 迁移后 `1global.ly` 仍报错（见已知阻塞） |

已完成（2026-10-27 补）：三个四重奏谱例已切进文章——
`voice-roles` Op.18 No.4 I mm.1–16、`quartet-texture` Op.59 No.3 II mm.1–16、
`inner-voices` Op.18 No.4 I mm.53–68。切割工具 `qcut.mjs` 在
`.work/score-tools/`，支持变量体、任意拍号、弱起与 `\repeat volta` 同行的情况。

## 第三轮：分阶段计划

完整方案见 <https://github.com/OpenCadenza/music-wiki> 之外的项目记录；这里只列可执行阶段。

| 阶段 | 内容 | 状态 |
| --- | --- | --- |
| P0 配货 | 把可切片乐谱库扩充到覆盖四重奏 + 部分交响曲 | **四重奏完成**（Op.18 No.4 四乐章、Op.59 No.3 II 已备；Op.131 迁移失败） |
| P1 四重奏 | 6 篇正文 + 谱例填充 | **完成 4 篇有真实谱例**，余 2 处占位缺源 |
| P2 钢琴奏鸣曲补全 | 谐谑曲、慢乐章类型、早期实验、小奏鸣曲定位 | **完成 4 篇**（21 篇正文） |
| P3 交响曲与协奏曲 | 动机细胞与段落边界、配器分层、独奏与乐队职责 | **已开分支**：交响曲 2 篇、协奏曲 2 篇、序曲 1 篇 |
| P4 声乐与合唱 | 歌词重音与旋律、合唱织体、宣叙与咏叹边界 | 未开始 |
| P5 技法层 | 从作曲家分支抽共性，建 `techniques/` | **已开分支，2 篇已提交**；另有 1 篇本地未提交草稿 |
| P6 收尾 | 索引、`NOTICE.md` 补全、重复清理、站点验收 | 未开始 |

### P3 已确认的交响曲与协奏曲源（2026-10-27 实测）

Mutopia 的 `BeethovenLv/` 下确实存在这些目录，按 `-lys/` 整目录下载即可：

| 作品 | 目录 | 说明 |
| --- | --- | --- |
| Op.55《英雄》 | `O55/BeethovenSymphony3` | 交响曲总谱 |
| Op.67 第五交响曲 | `O67/Symphony5_1`、`O67/Symphony5_2` | 两个乐章 |
| Op.92 第七交响曲 | `O92/Symphony7_1`、`O92/Symphony7_2` | 两个乐章 |
| Op.37 第三钢琴协奏曲 | `O37/Concerto_No3` | 独奏 + 乐队缩编 |
| Op.61 小提琴协奏曲 | `O61/violin_concerto_1/2/3` | 三份 |

未找到：Op.21、Op.36、Op.68、Op.93、Op.125（合唱）、Op.15/19/56/58/73 协奏曲。
Op.67 有两个版本（`Symphony5_1` 与 `beethoven_fifth_op67`），下载前先比较编译结果再选。

### 下一批建议选题

按"有源优先"排序，都能从已备源码里取到谱例：

| 分支 | 选题 | 可用作品 |
| --- | --- | --- |
| 四重奏 | 四件乐器的职责分配 | Op.18 No.4（已完成） |
| 四重奏 | 主调 / 复调 / 两个平面 | Op.59 No.3 II（已完成） |
| 四重奏 | 内声部怎么不塌 | Op.18 No.4（已完成） |
| 四重奏 | 大提琴唱旋律时其余三声部做什么 | Op.18 No.4 II（已配货，待切片） |
| 四重奏 | 四重奏里的赋格 | Op.131 I（已完成） |
| 四重奏 | 晚期四重奏的乐章连接 | 缺源，保留占位 |
| 交响曲 | 动机细胞与段落边界 | Op.67、Op.92 |
| 交响曲 | 配器分层：谁在加倍谁 | Op.55、Op.67 |
| 协奏曲 | 独奏与乐队的职责交换 | Op.37、Op.61 |
| 钢琴 | 谐谑曲取代小步舞曲 | Op.2 No.1 III、Op.79 |
| 钢琴 | 小奏鸣曲的定位 | Op.49 No.1 / No.2 |
| 钢琴 | 早期奏鸣曲的实验 | Op.10 No.2 |

## 已核实的标记与结构事实

写作时容易被常识误导的几点，已按原始乐谱核对，后续批次直接引用：

| 事实 | 说明 |
| --- | --- |
| Op.2 No.1 第三乐章标的是 `Menuetto. Allegretto`，不是 Scherzo | Mutopia/Breitkopf 源、IMSLP、MusicBrainz 一致。Op.2 三首里最先标 Scherzo 的是 **No.2**（A 大调，Trio 在 a 小调），No.3 也标 Scherzo（Allegro）。"谐谑曲取代小步舞曲"这个说法在 Op.2 No.1 上只能算**标题滞后于音乐** |
| Op.10 No.2 是 **F 大调**，三乐章 Allegro / Allegretto（f 小调）/ Presto | 不是 f 小调；三个乐章不是孤例（Op.10 No.1 也是三个），缺席的慢乐章才是 |
| Op.49 No.1 第一乐章**有**展开部 | mm.33–63 共 31 小节，第 64 小节主部主题原样回来当再现部。"小奏鸣曲省略展开部"是不准确的，准确说法是展开部不发展主部主题、只搬运 |
| Op.31 No.2 第二乐章开头是宣叙式写法 | 前几小节有休止符切断的短句，`d''8..` 起于 m.6；靠 `\barNumberCheck` 逐段核对过 |
## 已知阻塞

1. **晚期钢琴奏鸣曲无机器可读源。** Op.101/106/109/110 在 Mutopia 不存在；
   MuseScore → musicxml2ly 通道实测失败（见[资料来源](sources.md)）。
   要么走 IMSLP 人工转录，要么用占位并在其他作品上找同类例证。
2. **Op.111 的小节号不可靠。** Maestoso 用 `\cadenzaOn` + `\partial 32` 排版，
   LilyPond 把每个手势块算作一个小节，与通行版 16 小节不符。切片前必须重新对齐。
3. **Op.53、Op.57 I、Op.74、Op.95、Op.127、Op.130、Op.132、Op.133、Op.135 无源。**
   涉及这些作品的选题只能用占位或换例证。
4. **Op.131（Mutopia 594）是 LilyPond 2.6.2 源码，迁移失败。** 42 个文件能下全（大于 500 字节），
   但 `convert-ly` 到 2.26.0 后 `1global.ly` 报 `syntax error, unexpected NUMBER_IDENTIFIER`，
   累计 359 个 error。原因是它 `\include "english.ly"` 并在 header 里用了旧式写法。
   要修需要手工重写 global 文件，成本高于收益；涉及 Op.131 的选题（`late-quartet-cycles`）
   暂时保留占位。`quartet-fugue` 里那块 Op.131 谱例是早前单独处理过的，不受影响。
5. **Mutopia 的 `O18/` 只有 Op.18 No.4。** 想用 Op.18 No.1 / No.2 的选题拿不到源，
   需要换例证（Op.18 No.4 已配好四个乐章）或另找渠道。
6. **并行子代理不稳定。** 第三轮出现过 6 次代理中途被系统中断、空手而归的情况。
   建议每批不超过 2 个代理，并在任务书里明确"拿不到就写占位、立刻交稿"。

