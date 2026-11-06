# dcml

> 来源说明：[原始 README](../../../../../origin_resources/sources/dcml/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/dcml/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：1；状态计数：{"downloaded": 1}。

## 来源说明摘要

DCML - 类型：DCML 多数子库提供原生 TSV/CSV 分析标注，并包含 MEI、MuseScore 或其他源乐谱格式，具体依子库而异。 - 官网/上游：<https://github.com/DCMLab/distantlisteningcorpus；本目录选择官方子库 Annotated Beethoven Corpus：<https://github.com/DCMLab/ABC。 - 内容范围：ABC 涵盖贝多芬弦乐四重奏及其标准化和声分析；主库是多个子库的元仓库。 - 下载范围与状态：已下载 ABC 官方默认分支 main zip 到 raw/ABC-main.zip；字节数和 SHA-256 见 manifest.json。此 ABC 子库自身即采用 CC BY-NC-SA 4.0；仅保存在本地研究资料区，不纳入公开运行库。 - 获取方式：python download.py，可重复运行，失败重试一次，500 MiB 单包上限；脚本检查 ZIP 与预期语料文件。 - 许可：已从下载包 ABC-main/LICENSE 核实为 CC BY-NC-SA 4.0。DCML 子库许可并不统一；NC-SA 仅本地研究，不纳入运行发布。 目录结构 README.md 为来源说明，download.py 为下载器，manifest.json 为实际记录，raw/ABC-main.zip 为完整子库原包；不在此自动解压、转码或发布。

## 清单条目

- **ABC-main.zip** — 状态：downloaded；原件：[raw/ABC-main.zip](../../../../../origin_resources/sources/dcml/raw/ABC-main.zip)；来源：https://codeload.github.com/DCMLab/ABC/zip/refs/heads/main；字节：97449169；结果备注：reused existing valid archive

## 本地阅读副本

没有从 raw/ 复制单独文本文件；请使用上方的原件入口或压缩包目录清点。
- [整理后的 DCML 标注表](../../../../scores/dcml-abc/README.md)

- [解包机器可读谱源](../../../../scores/source-packages/dcml/README.md)（140 个谱文件）

## 其他清单元数据

{
  "url": "https://codeload.github.com/DCMLab/ABC/zip/refs/heads/main",
  "path": "raw/ABC-main.zip",
  "bytes": 97449169,
  "sha256": "573b24e36a48c469af3398607875128fdd0645ddf7776fc9b64e0d6ed3acc42e",
  "status": "downloaded",
  "error": "reused existing valid archive"
}
