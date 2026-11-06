# humdrum

> 来源说明：[原始 README](../../../../../origin_resources/sources/humdrum/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/humdrum/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：1；状态计数：{"downloaded": 1}。

## 来源说明摘要

Humdrum - 类型：上游 kern 原生纯文本乐谱，tab 分隔的多声部 Humdrum 格式。 - 官网/上游：<https://github.com/humdrum-tools/humdrum-data 是下载接口/元仓库；本目录取得的实际子库为 <https://github.com/craigsapp/bach-370-chorales。 - 内容范围：Bach chorales 子库；大合集不从接口整体重复下载。本地现有 corpus/abc 有大量由 Humdrum 转制的 ABC 文件，保留在既有 corpus，不复制到本来源目录。 - 下载范围与状态：脚本下载 Bach 370 Chorales zip 到 raw/bach-370-chorales-main.zip；详见 manifest.json。接口仓库本身不计作乐谱下载。 - 获取方式：python download.py，支持重跑，失败重试一次，包体上限 500 MiB；验证 ZIP 有 .krn/.kern 文件。 - 许可：按 Bach 子库仓库中的 LICENSE/NOTICE；Humdrum 元仓库所聚合数据的许可依来源而异。 目录结构 text humdrum/ README.md 类型、内容、来源与使用边界 download.py 下载及缓存复用入口 manifest.json URL、路径、大小、SHA-256 与状态 raw/ 完整官方 ZIP（不进入 Git） 原始包保留仓库自身目录结构；本轮不自动解压或转码。

## 清单条目

- **bach-370-chorales-main.zip** — 状态：downloaded；原件：[raw/bach-370-chorales-main.zip](../../../../../origin_resources/sources/humdrum/raw/bach-370-chorales-main.zip)；来源：https://codeload.github.com/craigsapp/bach-370-chorales/zip/refs/heads/main；字节：584230；结果备注：reused existing valid archive

## 本地阅读副本

没有从 raw/ 复制单独文本文件；请使用上方的原件入口或压缩包目录清点。

- [解包机器可读谱源](../../../../scores/source-packages/humdrum/README.md)（370 个谱文件）

## 其他清单元数据

{
  "url": "https://codeload.github.com/craigsapp/bach-370-chorales/zip/refs/heads/main",
  "path": "raw/bach-370-chorales-main.zip",
  "bytes": 584230,
  "sha256": "d613033a50cbce849184b2094b7f50a96ef91c17a729faab0771c0a1cb175e63",
  "status": "downloaded",
  "error": "reused existing valid archive"
}
