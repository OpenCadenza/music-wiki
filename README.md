# 音乐知识库

面向音乐创作 Agent 与人工协作者的作曲知识库。正文通过树状路径和关键词检索，
ABC/LilyPond 谱例会编译为可缩放乐谱、可播放 MP3 和可下载源码。

- 在线站点：<https://opencadenza.github.io/music-wiki/>
- 协作仓库：<https://github.com/OpenCadenza/music-wiki>
- 内容镜像：`viking://resources/music-wiki/`

## 协作方式

线上知识库以 `content/` 为维护对象，团队通过 fork 和 Pull Request 协作。

1. Fork `OpenCadenza/music-wiki`，在自己的仓库中建立分支。
2. 在分支中直接修改 `content/`，不要修改生成目录或构建产物。
3. 向 `OpenCadenza/music-wiki:main` 提交 Pull Request。
4. PR 会自动运行完整的构建检查，但不会部署到线上站点。
5. 维护者评审并合入 PR。
6. 合入 `main` 后，GitHub Actions 会自动重新构建并部署 GitHub Pages。

正常流程不需要手动触发 Actions。`workflow_dispatch` 仅用于维护者在服务异常或需要
重新发布时手动重跑。首次贡献者的工作流运行可能需要维护者批准；如果仓库为
`github-pages` 环境配置了审批规则，部署任务会等待指定维护者批准。

建议维护者在仓库设置中要求所有 `content/` 修改通过 Pull Request，并启用分支保护。

## 仓库结构

- `content/`：公开知识正文、来源登记和许可信息，通过 Pull Request 维护。
- `.vitepress/`：站点配置、主题和播放器组件。
- `.github/workflows/deploy.yml`：PR 检查与 `main` 自动部署。
- `public/`：站点公共静态资源；生成的 SVG、MIDI、MP3 和 manifest 不提交。

本地开发、工具链安装和单机发布步骤由项目内部文档维护，不属于公共协作说明。

## 内容组织规则

1. 每个公开目录必须使用 `index.md`，不要使用 `README.md`。目录首页应说明覆盖范围、
   推荐阅读顺序、检索别名、与其他分支的边界及证据缺口，不需要手工列出全部子文件。
2. 叶子正文围绕一个明确的创作问题组织。建议包含创作问题、来源与定位、机制解释、
   完整谱例、迁移方法和适用边界。
3. 保留已有的 page ID、knowledge ID 和谱例 ID。新增 ID 必须唯一、稳定，并使用小写
   字母、数字、点、下划线或连字符。
4. 所有相对链接必须指向实际存在的文件或目录。跨文章关联优先生成链接，不复制正文。
5. 来源必须登记在 `knowledge/sources.json`。每个来源记录标题、出版方、版本、权威级别、
   许可和允许的使用方式；正文中的 `sources` 字段只能引用已登记的来源 ID。
6. 生成的 SVG、MIDI、MP3、manifest、缓存和工具链文件不要提交。
7. 同一页面只允许一首谱例音频播放。开始播放或从头播放任意一首时，页面内其余播放器
   必须暂停。
8. PR 的自动检查会扫描当前全部谱例，谱例数量由内容动态决定。

## LilyPond 2.26.0 要求

每个 `lilypond` 或 `ly` 代码块必须且只能声明一次：

```lilypond
\version "2.26.0"
```

- 可执行语法和示例元数据中的 `target_version` 必须为 `2.26.0`。
- `source_version` 记录历史编码来源，可以保留旧版本，例如 `2.16.1`。
- 旧编码需要迁移时先运行 `convert-ly`、复核转换差异并重新编译，不能只修改版本字符串。
- 编译失败的谱例会阻止 PR 检查通过，也不会进入正式站点。

## 谱例元数据

谱例元数据必须紧挨着代码围栏之前。常用格式如下：

````markdown
<!-- opusloom:example
{
  "id": "composer.model.topic",
  "status": "published",
  "source_version": "2.16.1",
  "target_version": "2.26.0",
  "compile": "score",
  "midi": true,
  "requires": [],
  "sources": ["source-id"],
  "rights": "许可与再分发范围",
  "source_locator": "作品、乐章、页码或小节定位",
  "context": "谱例展示的创作问题和边界"
}
-->
```lilypond
\version "2.26.0"
% ...
```
````

字段要求：

- `id`：唯一、稳定的谱例 ID。
- `status`：`published` 或 `draft`；草稿仍会编译并在网页标注“草稿”。
- `source_version`：原始编码版本，只表示来源，不决定目标语法。
- `target_version`：必须为 `2.26.0`。
- `compile`：完整谱使用 `score`，音乐表达式使用 `fragment`。
- `midi`：是否要求原代码直接生成 MIDI；网页播放会另行生成派生音频。
- `requires`：当前示例依赖的其他谱例 ID。
- `sources`：`knowledge/sources.json` 中登记的来源 ID。
- `rights`、`source_locator`、`context`：说明许可、精确定位、用途和证据边界。
- `instrument` 或 `midi_instrument`：可选。填写 General MIDI 乐器名称或 0–127
  编号；未填写时保留代码内乐器，代码也未指定时默认钢琴。

ABC 代码块可使用 `music-kb:block` 或 `opusloom:example` 元数据，同样需要唯一 ID。
每段谱例内容必须唯一；如果多处确实引用同一段代码，应把谱例保留在单一位置并通过链接引用。

## 合并前检查

PR 会自动执行：

- 内容目录、链接、ID 和谱例元数据校验。
- 全部 LilyPond 与 ABC 谱例编译。
- SVG、MIDI、MP3 与 manifest 完整性检查。
- VitePress 构建和代表性页面冒烟测试。

任何步骤失败，PR 不应合入。合入 `main` 后会再次执行相同检查并部署站点。

## 许可

来源许可与引用边界记录在 `content/LICENSE.md` 和 `content/knowledge/sources.json`。
每个谱例还要保留自己的 `rights`、`source_locator` 和来源定位。
