<!-- music-kb:page {"id": "page.91c83d89c07e4e8fad3f76b6ea5f9d39"} -->
<!-- knowledge: composers.beethoven.navigation -->
# 贝多芬：按创作问题逐层检索

贝多芬的材料发展需要同时考察轮廓、节奏、和声目标与声部职责。相似音型出现并不自动构成结构统一；只有当材料在开端、推进、回归或结尾承担可说明的任务时，分析才转化为可迁移的创作依据。早中晚期是比较框架，同一技法在不同作品中可能承担不同功能。

钢琴奏鸣曲、室内乐、交响协奏和声乐不能共用一套风格公式。新作先确定体裁、编制和乐章任务，再读相关的1–3篇具体问题；讲解、完整谱例、迁移条件和证据边界一起读。

进一步讨论分为[跨体裁技法](techniques/index.md)、[钢琴](piano/index.md)、[室内乐](chamber/index.md)、[交响与协奏](orchestral/index.md)、[声乐](vocal/index.md)、[从检索、草稿到成谱](workflow/index.md)。这些分支限定各自的编制与段落语境，相关机制通过正文交叉引用。

## 技法、体裁与实际成谱

[跨体裁技法](techniques/index.md)讨论动机、和声曲式与节奏句法；[创作流程](workflow/index.md)讨论草稿、声部实现和检索到成谱。具体作品用于限定音乐观察的来源与位置；原创模型用于把问题变成可编写的音符，两者不能互相代替。

## 证据与覆盖缺口

现有内容覆盖主要体裁，深度不等。正文区分原作事实、具名研究解释与本库原创教学建议；真实摘录保留版本、声部、小节及删改范围。原创模型不能代替历史作品证据。

Op.59部分分析仍依赖二手转述与局部语料；Op.97演奏平衡、完整作品与草稿比较、大型声乐和管弦乐原谱实证、历史乐器与配器仍需深化。当前28个新增谱例中27个LilyPond例已有编译记录，1个ABC例只有配对人工核对；另保留2个旧LilyPond例。本轮不新增音乐事实或谱例。

当前完成的是两轮内容建设与树状整理，并未穷尽贝多芬作品，也未完成音乐学专家认证、ABC独立渲染或受控创作效果评估。谱例的published仅指本地生成器收录；编译通过不等于音乐质量或远端Wiki已发布。

[全库来源表](../../knowledge/sources.json)登记许可与证据范围；[稳定ID索引](../../knowledge/INDEX.md)可直达正文。在线实读、已缓存全文、索引片段、二手转述分别判断，不能用下载数量代替实读。

```powershell
rg -n 'Op\.?\s*110|Arioso|倒影|赋格' references-origin/composers/beethoven/piano/sonatas
rg -n 'Op\.?\s*74|4/3|10–8–6' references-origin/composers/beethoven/chamber/quartets
rg -n 'knowledge:|opusloom:example' references-origin/composers/beethoven/techniques
```
