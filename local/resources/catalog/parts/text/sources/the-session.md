# the-session

> 来源说明：[原始 README](../../../../../origin_resources/sources/the-session/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/the-session/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：2；状态计数：{"cached": 1, "excluded": 1}。

## 来源说明摘要

the-session - 类型：ABC 曲调数据渠道；本项目排除 - 来源：https://github.com/adactio/TheSession-data - 获取策略：仅保存许可作为排除依据。当前许可禁止一般 LLM 使用，因此不获取曲调内容用于本知识库。 - 实际结果：查看 manifest.json 的逐项状态；downloaded/cached 为已保存，reused-existing 为现有本地文件，failed 为未取得。 目录结构 text the-session/ README.md 来源和获取说明 download.py 可重复执行的来源入口 manifest.json 下载或复用清单 raw/ 实际保存资料（不进入 Git） 复用条目的相对路径指向 ../../corpus/；没有在本目录再复制一份。 下载方式与脚本 在 music-library 执行 python sources/the-session/download.py。共用实现为 scripts/acquireadditionalsources.py；使用 Python 标准库，无需额外依赖。已有文件复用；没有覆盖更新远端版本的隐含操作，失败保留在 manifest。缓存不证明已细读，不赋予重新发布许可。

## 清单条目

- **LICENSE.md** — 状态：cached；原件：[raw/LICENSE.md](../../../../../origin_resources/sources/the-session/raw/LICENSE.md)；来源：https://raw.githubusercontent.com/adactio/TheSession-data/main/LICENSE.md；字节：27025
- **未命名条目** — 状态：excluded；说明：Current upstream terms prohibit general LLM processing; no tunes downloaded for this agent knowledge base.

## 本地阅读副本

- [LICENSE.md](../../../../text/source-copies/the-session/LICENSE.md)


## 其他清单元数据

{
  "source": "the-session",
  "acquired_at": "2026-10-21T18:36:32.594173+00:00"
}
