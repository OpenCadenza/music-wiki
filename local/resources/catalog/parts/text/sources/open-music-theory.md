# open-music-theory

> 来源说明：[原始 README](../../../../../origin_resources/sources/open-music-theory/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/open-music-theory/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：4；状态计数：{"downloaded": 1, "failed": 3}。

## 来源说明摘要

Open Music Theory - 类型：乐理教材。官网：https://viva.pressbooks.pub/openmusictheory/；旧版项目：https://github.com/openmusictheory/openmusictheory.github.io - 范围：GitHub API 验证仓库存在，默认分支为 master，已下载该官方源码 ZIP（38,917,643 字节）。这是早期 openmusictheory.github.io 旧版，不是当前 OMT2 Pressbooks 教材。当前 OMT2 XML/PDF/EPUB 导出此前均返回 HTTP 403，失败记录保留且脚本不会重试这些端点。 - 状态：旧版源码 ZIP 成功，manifest 有 SHA-256；当前 OMT2 正文未取得。 - 许可：仓库历史版本依其 LICENSE 文件和官网声明；当前 OMT2 为 CC BY-SA 4.0。 - 重跑：python download.py；可选环境变量 MKBDOWNLOADPROXY 指定代理。 - 目录树：download.py、sources.json、manifest.json、.gitignore、raw/openmusictheory.github.io-master.zip。

## 清单条目

- **openmusictheory.github.io-master.zip** — 状态：downloaded；原件：[raw/openmusictheory.github.io-master.zip](../../../../../origin_resources/sources/open-music-theory/raw/openmusictheory.github.io-master.zip)；来源：https://api.github.com/repos/openmusictheory/openmusictheory.github.io/zipball/master；字节：38917643
- **open-music-theory.xml** — 状态：failed；目标路径未实存：raw/open-music-theory.xml；来源：https://viva.pressbooks.pub/openmusictheory/open/download?type=wxr；字节：0；结果备注：HTTP 403: Forbidden (previous attempt; not retried)
- **open-music-theory.pdf** — 状态：failed；目标路径未实存：raw/open-music-theory.pdf；来源：https://viva.pressbooks.pub/openmusictheory/open/download?type=pdf；字节：0；结果备注：HTTP 403: Forbidden (previous attempt; not retried)
- **open-music-theory.epub** — 状态：failed；目标路径未实存：raw/open-music-theory.epub；来源：https://viva.pressbooks.pub/openmusictheory/open/download?type=epub；字节：0；结果备注：HTTP 403: Forbidden (previous attempt; not retried)

## 本地阅读副本

没有从 raw/ 复制单独文本文件；请使用上方的原件入口或压缩包目录清点。
- [旧版 OMT 可读源码](../../../../text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/contents.md)


## 其他清单元数据

无
