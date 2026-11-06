# josquin

> 来源说明：[原始 README](../../../../../origin_resources/sources/josquin/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/josquin/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：1；状态计数：{"downloaded": 1}。

## 来源说明摘要

Josquin Research Project - 类型：原生 Humdrum kern 数字乐谱，适合分析处理。 - 官网/上游：<https://josquin.stanford.edu/；官方代码与数据仓库 <https://github.com/josquin-research-project/jrp-scores。 - 内容范围：约 1420–1520 年作曲家的声乐作品，面向 JRP 搜索与比较研究。 - 下载范围与状态：已下载官方 JRP scores 仓库默认分支 main zip，不逐曲抓取网站；状态和 SHA-256 见 manifest。 - 获取方式：python download.py；可重跑，失败重试一次，500 MiB 单包上限，检查 ZIP 及 Humdrum 文件。官方仓库默认分支为 main。 - 许可：遵循 JRP 仓库及 Stanford 项目页面所列数据使用/署名条款；使用前查看上游当前声明。 目录结构 text josquin/ README.md 类型、内容、来源与使用边界 download.py 下载及缓存复用入口 manifest.json URL、路径、大小、SHA-256 与状态 raw/ 完整官方 ZIP（不进入 Git） 原始包保留仓库自身目录结构；本轮不自动解压或转码。

## 清单条目

- **jrp-scores-main.zip** — 状态：downloaded；原件：[raw/jrp-scores-main.zip](../../../../../origin_resources/sources/josquin/raw/jrp-scores-main.zip)；来源：https://codeload.github.com/josquin-research-project/jrp-scores/zip/refs/heads/main；字节：5541981；结果备注：reused existing valid archive

## 本地阅读副本

没有从 raw/ 复制单独文本文件；请使用上方的原件入口或压缩包目录清点。

- [解包机器可读谱源](../../../../scores/source-packages/josquin/README.md)（1381 个谱文件）

## 其他清单元数据

{
  "url": "https://codeload.github.com/josquin-research-project/jrp-scores/zip/refs/heads/main",
  "path": "raw/jrp-scores-main.zip",
  "bytes": 5541981,
  "sha256": "fc46a557881c3ef3f3924ee25ebddbd4de717ce9d622b1cdfa5ebcd53bd8ca63",
  "status": "downloaded",
  "error": "reused existing valid archive"
}
