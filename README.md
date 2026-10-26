# 音乐知识库

面向音乐创作 Agent 与人工维护者的作曲知识库。正文通过树状路径和关键词检索，
ABC/LilyPond 谱例会编译为可缩放乐谱、可播放 MP3 和可下载源码。

- 在线站点：<https://opencadenza.github.io/music-wiki/>
- GitHub 仓库：<https://github.com/OpenCadenza/music-wiki>
- 内容镜像：`viking://resources/music-wiki/`

## 仓库结构

- `references-origin/` 是知识内容的唯一权威来源，位于独立仓库。
- `content/` 是发布快照，由 `scripts/publish-content.ps1` 从 `references-origin/` 同步，
  不要在 `content/` 中长期手改正文。
- `.vitepress/` 保存站点、侧边栏和播放器配置。
- `public/` 保存站点静态资源；`public/notation/` 是构建产物，不提交到 Git。
- `.github/workflows/deploy.yml` 在推送到 `main` 后构建并部署 GitHub Pages。

## 更新 `content/` 前的规则

1. 在 `references-origin/` 修改 Markdown，再运行发布脚本。不要直接维护第二份正文。
2. 每个公开目录必须使用 `index.md`，不要使用 `README.md`。目录首页应说明覆盖范围、
   推荐阅读顺序、检索别名、与其他分支的边界及证据缺口，不需要手工列出全部子文件。
3. 叶子正文围绕一个明确的创作问题组织。建议包含创作问题、来源与定位、机制解释、
   完整谱例、迁移方法和适用边界。
4. 保留已有的 page ID、knowledge ID 和谱例 ID。新增 ID 必须唯一、稳定，并使用小写
   字母、数字、点、下划线或连字符。
5. 所有相对链接必须指向实际存在的文件或目录。跨文章关联优先生成链接，不复制正文。
6. 来源必须登记在 `knowledge/sources.json`。每个来源记录标题、出版方、版本、权威级别、
   许可和允许的使用方式；正文中的 `sources` 字段只能引用已登记的来源 ID。
7. 生成文件不要提交。SVG、MIDI、MP3、manifest、缓存和工具链分别位于忽略目录。
8. 新增或改名内容后，至少运行 `pnpm validate`、`pnpm build`，并检查构建后的页面。
   构建器会动态扫描全部谱例，不应修改脚本中的固定谱例数量。
9. 同一页面只允许一首谱例音频播放。开始播放或从头播放任意一首时，页面内其余播放器
   必须暂停；播放控制状态、进度和 MIME 行为需要一起验证。

## LilyPond 2.26.0 要求

每个 `lilypond` 或 `ly` 代码块必须且只能声明一次：

```lilypond
\version "2.26.0"
```

- 可执行语法和示例元数据中的 `target_version` 必须为 `2.26.0`。
- `source_version` 记录历史编码来源，可以保留旧版本，例如 `2.16.1`。
- 旧编码需要迁移时先运行 `convert-ly`、复核转换差异并重新编译，不能只修改版本字符串。
- 编译失败的谱例会阻止发布。

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

## 构建

需要 Node.js 24、pnpm 12.3.4、LilyPond 2.26.0、abc2svg 1.22.1、abcMIDI、
FluidSynth 2.6.1、FFmpeg/ffprobe 和 FluidR3 GM。

```bash
pnpm install --frozen-lockfile
pnpm validate
pnpm notation
pnpm validate:notation
pnpm build:site
pnpm smoke:site
```

`pnpm build` 会依次完成以上内容，并编译当前全部谱例。数量由内容动态决定，不写死。

Linux/WSL 可使用 `scripts/install-toolchain.sh` 下载并校验 LilyPond 与音色库；
FluidSynth 2.6.1 的 Linux 构建步骤见 GitHub Actions 工作流。Windows 可运行：

```powershell
./scripts/install-toolchain.ps1
```

## 发布

```powershell
./scripts/publish-content.ps1 `
  -SourceRepository E:/programfiles/MusicKnowledgeBase/references-origin `
  -DestinationRepository E:/Github/music-wiki
```

脚本会依次：

1. 校验 LilyPond 版本并提交 `references-origin/` 的来源改动。
2. 将受管文件同步到 `content/`，逐个校验 SHA-256。
3. 更新 `.publication.json` 中的来源提交号。
4. 提交并推送 `music-wiki/main`。
5. 由 GitHub Actions 完整编译谱例、构建 VitePress、执行冒烟测试并部署 Pages。

OpenViking 从 GitHub 的 `content/` 子树同步到 `viking://resources/music-wiki/`。
只有 GitHub 推送、Actions 和线上资源检查都成功，才算完成一轮发布。

## 许可

来源许可与引用边界记录在 `content/LICENSE.md` 和 `content/knowledge/sources.json`。
每个谱例还要保留自己的 `rights`、`source_locator` 和来源定位。
