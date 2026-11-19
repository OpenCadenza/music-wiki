# 工作单：scholar-b3

接替 scholar-b2 / scholar-b。先读 `local/docs/实施记录/2026-11-20-续作/续作说明.md`、
`local/docs/偏好-知识库写作.md`、`local/docs/实施记录/2026-11-16-DSH首批/角色提示词.md`（共同段与学者段）。

## 第一波（先做这个，做完回报）

给下面 7 篇改标题：短标题 + 一行副标题（`<p class="doc-subtitle">…</p>`），并在 frontmatter 写
`title: <短标题>`；同时把要登记进 provenance 的资料列出来（不用一次填完）。

| 文章 | 现在的标题 |
| --- | --- |
| `content/techniques/counterpoint/suspension-mechanics-and-voice-leading.md` | 对位中的挂留延留力学与声部导向机制 |
| `content/composers/bach/chorale/cadential-voice-clock-and-phase-decoupling.md` | 巴赫众赞歌终止式的声部时钟与相位解耦机制 |
| `content/composers/beethoven/quartets/chromatic-suspension-and-structural-topology.md` | 结构功能化的半音挂留：贝多芬弦乐四重奏中的声部阻尼与调性拓扑重塑 |
| `content/notation/machine-readable-sources-and-evidence-hierarchy.md` | 谱源的可信度阶梯：为什么机器可读原生语料能当证据，而人工转写不能？ |
| `content/notation/clef-octave-ambiguity-and-encoding-loss.md` | 机器可读乐谱中的八度歧义与演奏法损失：从符号编码到声学实现 |
| `content/techniques/harmony/neapolitan-chord-structural-mutation.md` | 从局部下属到结构对抗：那不勒斯和弦（bII）的调性异化机制 |
| `content/techniques/material/motivic-inversion-and-harmonic-recontextualization.md` | 核心细胞的倒影变形与和声再语境化机制 |

## 第二波起（逐篇）

按续作说明的五步，一篇一交：改标题、登记 provenance、按需换图、读谱例改文章、更新归档。
你不必等全部改完；每完成一篇就发消息，lead 验收后再放下一篇。

## 你的 provenance 文件

`provenance/techniques/counterpoint/suspension-mechanics-and-voice-leading.md` 等 7 个骨架已建好，
`引用与出处` 表是空的，等你填。

## 注意

`notation/` 两篇讨论的正是"谱源与证据"，正文里的谱源类型名、文件与定位本来就是主题的一部分，
可以保留也可以调整；只是把书目细节（版本、页码、URL、许可）放进 provenance 文件。
