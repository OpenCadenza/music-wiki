# 从这里开始：知识生产交接

> ⚠️ **先读这一条：现有 37 篇正文必须全部重写。**
> 谱例是真的，但围绕谱例的理论与分析没有文献依据——是写手凭自己的知识生成的。
> 详见 [`贝多芬-知识库-交接.md`](贝多芬-知识库-交接.md)。

---

## 三份文档

| 文件 | 读它来搞清什么 |
| --- | --- |
| **本页** | 东西在哪、先做什么 |
| [`贝多芬-知识库-交接.md`](贝多芬-知识库-交接.md) | **现有文章为什么全部作废**、哪些内容可信、权威资料在哪、重写的判据 |
| [`偏好-知识库写作.md`](偏好-知识库写作.md) | 用户的写作偏好：要内容不要形式、不许编、不要过度防御性编程 |

**团队级文档在另一个仓库**（`E:\github\opencadenza-dev-doc\music-wiki-知识生产\`），进 Git、给全团队看：
`README.md`（全局设计）、`writing-rules.md`（写作方法）、`score-pipeline.md`（配货管线）、
`sources.md`（来源与许可）、`handover.md`（进度与缺口）。

---

## 资料在哪

```
E:\github\music-wiki\local\
├── docs\                       ← 你在这里
│   ├── README.md
│   ├── 贝多芬-知识库-交接.md
│   └── 偏好-知识库写作.md
└── materials\
    ├── theory\                 # ← 重写要用的权威资料（42.9 MB）
    │   ├── open-music-theory\  #   乐理教材全文，130 个 Markdown 章节
    │   └── dcml-abc\           #   16 部四重奏的逐拍和声标注，421 个 TSV
    ├── scores\                 # 乐谱源码（817 个 .ly/.lyi，8.6 MB）
    │   ├── CATALOG.md          #   全库目录：每个体裁下有哪些作品
    │   ├── INDEX.md            #   钢琴第一批配货记录
    │   └── BATCH2-INDEX.md     #   钢琴第二批配货记录
    └── tools\                  # 19 个切片/转换/验证脚本
```

**原始资料中心在 `E:\programfiles\MusicKnowledgeBase\music-library\`**（2.8 GB）——
那里还有 32 篇分析论文 PDF（贝多芬键盘/管弦/室内乐、MIT 和声与对位、Belkin 配器、partimenti），
需要抽文本才能用（pypdf 6.16.2 已验证可用）。清单见交接文档第四节。

---

## 先做什么

1. **读交接文档**，搞清哪些内容可信、哪些作废。
2. **把 32 篇 PDF 抽成文本**，和已解出的 OMT、DCML 一起建成可检索语料。
3. **逐篇重写**：每个分析性论断都要能指到资料里的某一页；指不到的降级为描述或删除。
4. 谱例块可以全部复用——它们是真的，已通过编译与 `\barNumberCheck`。

---

## 环境

工具链在 `E:\github\music-wiki\.tools\`（gitignore，本机已装好）：LilyPond 2.26.0、abcmidi、
fluidsynth、FluidR3_GM.sf2。换机器跑 `pwsh scripts/install-toolchain.ps1`。Node 依赖 `pnpm install`。

验证环境（约 1 分钟）：

```powershell
node scripts/validate-content.mjs
node scripts/build-notation.mjs
node scripts/prepare-site-public.mjs      # 必须在 notation 之后
node node_modules/vitepress/bin/vitepress.js build
node scripts/smoke-site.mjs
```

> 不要用 `pnpm exec vitepress build`，本机会报 `ERR_PNPM_PACKAGE_MANAGER_REMOVE_MODULES_DIR`。

**注意**：构建全绿只说明谱例能编译，**不说明内容成立**。

---

## 仓库状态

| 仓库 | 位置 | 状态 |
| --- | --- | --- |
| `music-wiki` | `E:\github\music-wiki\` | 本地 `bfc5f57`，领先 `origin/main` 14 个提交，未推送 |
| `opencadenza-dev-doc` | `E:\github\opencadenza-dev-doc\` | 团队文档，已提交 |
