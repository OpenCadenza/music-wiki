# abcnotation

> 来源说明：[原始 README](../../../../../origin_resources/sources/abcnotation/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/abcnotation/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：5；状态计数：{"downloaded": 4, "not-bulk-downloaded": 1}。

## 来源说明摘要

abcnotation - 类型：ABC 标准、曲调检索渠道 - 来源：https://abcnotation.com/ - 获取策略：保存主页、下载规则、版权政策与 ABC 2.1 标准。此处不是已下载曲调全集；官方禁止整站复制，不批量抓取。 - 实际结果：查看 manifest.json 的逐项状态；downloaded/cached 为已保存，reused-existing 为现有本地文件，failed 为未取得。 目录结构 text abcnotation/ README.md 来源和获取说明 download.py 可重复执行的来源入口 manifest.json 下载或复用清单 raw/ 实际保存资料（不进入 Git） 复用条目的相对路径指向 ../../corpus/；没有在本目录再复制一份。 下载方式与脚本 在 music-library 执行 python sources/abcnotation/download.py。共用实现为 scripts/acquireadditionalsources.py；使用 Python 标准库，无需额外依赖。已有文件复用；没有覆盖更新远端版本的隐含操作，失败保留在 manifest。缓存不证明已细读，不赋予重新发布许可。

## 清单条目

- **index.html** — 状态：downloaded；原件：[raw/index.html](../../../../../origin_resources/sources/abcnotation/raw/index.html)；来源：https://abcnotation.com/；HTML页面；视为目录或摘要入口，正文范围未确认；字节：20914
- **search-help.html** — 状态：downloaded；原件：[raw/search-help.html](../../../../../origin_resources/sources/abcnotation/raw/search-help.html)；来源：https://abcnotation.com/searchHelp；HTML页面；视为目录或摘要入口，正文范围未确认；字节：57945
- **copyright.html** — 状态：downloaded；原件：[raw/copyright.html](../../../../../origin_resources/sources/abcnotation/raw/copyright.html)；来源：https://abcnotation.com/searchCopyright；HTML页面；视为目录或摘要入口，正文范围未确认；字节：27484
- **abc-2.1-standard.html** — 状态：downloaded；原件：[raw/abc-2.1-standard.html](../../../../../origin_resources/sources/abcnotation/raw/abc-2.1-standard.html)；来源：https://abcnotation.com/wiki/abc:standard:v2.1；HTML页面；视为目录或摘要入口，正文范围未确认；字节：344553
- **未命名条目** — 状态：not-bulk-downloaded；说明：Official search help prohibits whole-site copying. Tune discovery service, not an archived tune corpus.

## 本地阅读副本

- [abc-2.1-standard.html](../../../../text/source-copies/abcnotation/abc-2.1-standard.html)
- [copyright.html](../../../../text/source-copies/abcnotation/copyright.html)
- [index.html](../../../../text/source-copies/abcnotation/index.html)
- [search-help.html](../../../../text/source-copies/abcnotation/search-help.html)

## 整理后的 HTML 正文

- [abc:standard:v2.1    [abc wiki]](../../../../text/organized-html/abcnotation/abc-2.1-standard.md)（176561 字符）
- [abc | tune search copyright](../../../../text/organized-html/abcnotation/copyright.md)（9164 字符）
- [abc | home](../../../../text/organized-html/abcnotation/index.md)（4349 字符）
- [abc | tune search help](../../../../text/organized-html/abcnotation/search-help.md)（35279 字符）


## 其他清单元数据

{
  "source": "abcnotation",
  "acquired_at": "2026-10-21T18:29:11.184946+00:00"
}
