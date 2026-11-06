# 本地研究工作目录

**本目录为本地工作目录，请勿合并到main分支**

本开发分支 `音乐学者子代理方案-开发分支` 只有主仓库一个 Git 仓库。`local/` 是普通目录，文档、工具、研究笔记、公共看板和轻量资料索引与 `content/` 一起由仓库根目录管理；不要在这里运行 `git init`，不要另建 local 仓库。原 local 的三次文档提交历史已通过 subtree 保留。

## 接手前先解压资料包

仅克隆分支还没有资料全文。请从[Google Drive下载资料包](https://drive.google.com/file/d/18csDqCQFRM1LOUsRHQzZy98XmUS_deS2/view?usp=sharing)，保存为 **music-wiki-resources-2026-11-07.zip**，按[团队接手步骤](docs/交接/README.md)校验并解压到**仓库根目录**，再接手研究工作。压缩包内已经含 `local/` 层级，不能解压到 `local/` 里，否则会多出一层 local/local。

在仓库根目录运行（Python 3.10+，路径替换为收到的文件）：

```powershell
python local/workbench/tools/handoff_bundle.py restore --archive "D:/收到的资料/music-wiki-resources-2026-11-07.zip"
```

脚本先核对本分支[资料包描述](docs/交接/资料包.json)中的整包 SHA-256，再逐文件检查并恢复 `local/origin_resources/` 和 `local/resources/`。已有同内容文件跳过，遇到不同内容文件停止并保留，避免覆盖团队成员的研究改动。

## 从哪里开始

- [文档入口](docs/README.md)：当前阶段、写作偏好、工作流、看板和预备轮验收。
- [阅读资料库](resources/README.md)：教材、研究、背景、乐器、谱源与OCR结果；解压后才能打开完整资料。
- [来源与下载方法](docs/sources.md)：原件来源、真实取得范围和下载入口，已放入本分支。
- [团队接手说明](docs/交接/README.md)：解压、验证、工具依赖、版本提交与交付边界。

原始库、资料正文、图像、乐谱包、大型历史归档和运行缓存继续由忽略规则排除。资料入口与 catalog 索引纳入 Git；资料包单独发送，不提交到 Git。新增资料由资料助手保存原件并整理可读副本，团队按新版本资料包同步。

本次完成分支迁移和交接准备，正式写作尚未启动。另行启动后，每篇完成归档看板记录，由主控在仓库根目录串行提交 `content/` 与 `local/` 的全部非忽略改动；整批约20篇结束后再进行编辑复读。正文之外的站点工程文件仍不在正式轮改动范围。

本分支不整体合并到 main。后续需要发布时，在单独发布分支仅选取审核通过的 content 改动，来源许可等公共登记按发布任务另行处理；不要把 local 工作文档一起带入 main。
