<!-- music-kb:page {"id": "page.ab04dd06258545b6aac740bcc31c4792"} -->
<!-- knowledge: navigation.root -->
<!-- 迁移说明：setup.md、scripts.md、review.md 为历史操作资料；当前操作入口在独立 abc-lily-composer Skill，不作为初次 Wiki 知识页面导入。 -->
# 按创作任务查资料

先确定问题，再读取最小相关资料。术语、分析标签和风格判断都需要与当前音符对应。

| 任务 / 检索词 | 入口 |
| --- | --- |
| ABC、LilyPond、版本、声部、时值 | [ABC](abc.md)、[LilyPond](lilypond.md)、[记谱](notation/index.md) |
| sentence / period、奏鸣曲、变奏、终止 | [曲式](forms/index.md)、[整体衔接](form.md) |
| 倒影、增减值、模进、角色交换 | [发展](development.md)、[技法](techniques/index.md) |
| counterpoint / fugue / canon / invention | [对位](techniques/counterpoint/index.md) |
| Bach / 巴赫、Mozart / 莫扎特、Ravel / 拉威尔 | [作曲家](composers/index.md) |
| 贝多芬 / Beethoven、晚期奏鸣曲、四重奏、交响曲 | [贝多芬任务导航](composers/beethoven/index.md)、[检索到成谱](composers/beethoven/workflow/retrieval-to-score.md) |
| 风格证据、平行和声、音色与结构 | [风格](styles/index.md) |
| string quartet / 弦乐四重奏、音域、织体 | [编制](ensembles/index.md) |
| 编译、music21、独立审稿、工具安装 | [脚本](scripts.md)、[审稿](review.md)、[环境](setup.md) |
| 来源、许可、稳定 ID、引用边界 | [稳定 ID 直达](knowledge/stable-ids.md)、[来源索引](knowledge/index.md)、[许可](LICENSE.md) |

组合任务示例：拉威尔风格弦乐四重奏先读作曲家与编制入口，再读指定曲式和对位资料；各自约束先组合试写，不能把风格标签当成和弦预设。最后一乐章写赋格是用户的创作选择，不代表拉威尔原四重奏末乐章就是赋格。

本地Agent先读专题导航，再用rg按中英文术语、别名和知识ID搜索路径；读取有关章节及谱例的完整上下文，记录实际采用的知识ID。远端读取时固定commit或修订号。新LilyPond谱使用维护目标版本，ABC按其独立标准处理。

所有可执行的LilyPond代码必须声明`\version "2.26.0"`，例子元数据的`target_version`也必须是`2.26.0`。`source_version`只记录历史编码来源，可以保留旧版本；发布脚本会拒绝旧版本、缺失版本或目标版本不一致的代码。语法需要迁移时先转换并重新编译，不能只替换版本字符串。

## 百科章节

按音乐问题与体裁组织章节，以多部作品比较机制与适用条件；单曲作为章内证据。

- [作曲家](composers/index.md)：巴赫、海顿、莫扎特、贝多芬、肖邦、德彪西与拉威尔。
- [风格](styles/index.md)：现代音乐、爵士与流行音乐专题。
- [曲式](forms/index.md)：主题功能与协奏曲。
- [编制](ensembles/index.md)：弦乐四重奏、管弦乐与爵士组合。
