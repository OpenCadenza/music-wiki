<!-- music-kb:page {"id": "page.a3ee61dff2b44058835f0e2f465111ca"} -->
<!-- knowledge: operation.lilypond -->
# LilyPond 写谱与检查
直接写完整 .ly。按实际编译器版本设置 version。变量、transpose、repeat、book/score 可用；随附脚本采用自包含输入，所有自定义定义和乐章在一个文件内，无本地外部 include，无占位；已有工程处理见 scripts.md。所有发声音符在正常谱面可见，不增加隐藏 MIDI 声部。
规划主题使用原生短谱。局部编辑先读变量定义和使用位置，保护其他声部；全局变量改动可能影响多处。fixed/absolute 更易核对绝对音高，relative 可用但跨段需检查八度锚点与继承时值。
独立声部正确使用 Voice/Staff，钢琴谱表不等于复调声部。逐小节核对时值、连音、弱起、反复、休止和持续音。加 bar check 有助于编译器发现错位。按要求提供 layout 和 midi 块。编译通过不等于对位、曲式或演奏性成立。

## 知识库示例与版本

Wiki 原稿保留来源语法；发布到 GitHub 的 Agent 视图使用已验证的目标稳定版本。代码框和发布 manifest 记录来源及目标版本。新谱按目标版本及对应官方文档书写，历史版本只用于来源追踪。

普通任务通过 GitHub MCP 读取知识快照；工具操作说明随 abc-lily-composer 安装。Wiki 导入前维护 references-origin；导入验收后统一在 Wiki 编辑原稿。后台转换和验证通过后发布，迁移细节保留在维护说明中。转换处理语法兼容；音高、时值、反复与奏法仍须核对。

技术依据：[LilyPond 2.26 Notation Reference](https://lilypond.org/doc/v2.26/Documentation/notation/index.html) 的 Writing pitches、Durations、Simultaneous music；[convert-ly options](https://lilypond.org/doc/v2.26/Documentation/usage/command_002dline-options-for-convert_002dly)；[manual conversions](https://lilypond.org/doc/v2.26/Documentation/usage/manual-conversions)。官方说明有无法自动转换的情况，因此实际编译和迁移审查分别保留。
