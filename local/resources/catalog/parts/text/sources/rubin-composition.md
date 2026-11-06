# rubin-composition

> 来源说明：[原始 README](../../../../../origin_resources/sources/rubin-composition/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/rubin-composition/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：2；状态计数：{"failed": 2}。

## 来源说明摘要

Rubin: Music Composition & Theory - 类型：作曲教材。官网：https://open.lib.umn.edu/musiccomposition/ - 范围：通过官网 Pressbooks 导出端点尝试 PDF 和 EPUB 全书导出；本机代理请求均返回 HTTP 403，因此未取得正文文件。 - 状态：导出失败，manifest 记录 403。下载脚本可通过 MKBDOWNLOADPROXY 环境变量配置代理，例如 PowerShell：$env:MKBDOWNLOADPROXY='http://127.0.0.1:7890'; python download.py；403 不绕过。 - 许可：CC BY 4.0（署名；个别材料可能另有声明）。 - 重跑：python download.py - 目录树：download.py、sources.json、manifest.json、.gitignore、raw/。

## 清单条目

- **music-composition.pdf** — 状态：failed；目标路径未实存：raw/music-composition.pdf；来源：https://open.lib.umn.edu/musiccomposition/open/download?type=pdf；字节：0；结果备注：HTTP 403: Forbidden
- **music-composition.epub** — 状态：failed；目标路径未实存：raw/music-composition.epub；来源：https://open.lib.umn.edu/musiccomposition/open/download?type=epub；字节：0；结果备注：HTTP 403: Forbidden

## 本地阅读副本

没有从 raw/ 复制单独文本文件；请使用上方的原件入口或压缩包目录清点。


## 其他清单元数据

无
