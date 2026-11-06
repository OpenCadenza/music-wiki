# pdmx

> 来源说明：[原始 README](../../../../../origin_resources/sources/pdmx/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/pdmx/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。

清单条目：4；状态计数：{"cached": 3, "downloaded": 1}。

## 来源说明摘要

pdmx - 类型：MusicXML 乐谱候选数据集 - 来源：https://github.com/pnlong/PDMX - 获取策略：获取官方说明、Zenodo 数据清单与可取得的小型元数据文件。已取得固定原始数据包，完整大小和校验值见 manifest；未取得的后续扩展包不计入下载。使用时先筛 nolicenseconflict 与有效文件；代码 MIT 不代表全体乐谱无条件可用。 - 实际结果：查看 manifest.json 的逐项状态；downloaded/cached 为已保存，reused-existing 为现有本地文件，failed 为未取得。 目录结构 text pdmx/ README.md 来源和获取说明 download.py 可重复执行的来源入口 manifest.json 下载或复用清单 raw/ 实际保存资料（不进入 Git） 复用条目的相对路径指向 ../../corpus/；没有在本目录再复制一份。 下载方式与脚本 在 music-library 执行 python sources/pdmx/download.py。共用实现为 scripts/acquireadditionalsources.py；使用 Python 标准库，无需额外依赖。已有文件复用；没有覆盖更新远端版本的隐含操作，失败保留在 manifest。缓存不证明已细读，不赋予重新发布许可。 固定的数据版本与大包 本次选择 Zenodo 原始记录 13763756（2024 首版），包为 raw/PDMX.tar.gz，官方大小 1,588,637,145 字节。已读取包头确认含 PDMX.csv 与 metadata JSON；这是原始符号音乐数据包，不是后来扩展的全部 MXL/PDF/MIDI。不得假设已包含最新的 nolicenseconflict 子集。记录的数据许可为 CC BY 4.0；raw/code-LICENSE.txt 仅是仓库代码许可。 可运行 python downloadarchive.py 以四路官方HTTP范围请求续传；通过 MUSICLIBRARYPROXY 配置代理。脚本核对完整字节数和 Zenodo 提供的 MD5 后才写成功清单，另存 SHA-256。当前是否成功以 manifest.json 为准；.part 不属于完整下载。

## 清单条目

- **README.md** — 状态：cached；原件：[raw/README.md](../../../../../origin_resources/sources/pdmx/raw/README.md)；来源：https://raw.githubusercontent.com/pnlong/PDMX/main/README.md；字节：7316
- **code-LICENSE.txt** — 状态：cached；原件：[raw/code-LICENSE.txt](../../../../../origin_resources/sources/pdmx/raw/code-LICENSE.txt)；来源：https://raw.githubusercontent.com/pnlong/PDMX/main/LICENSE；字节：1068
- **zenodo-record.json** — 状态：cached；原件：[raw/zenodo-record.json](../../../../../origin_resources/sources/pdmx/raw/zenodo-record.json)；来源：https://zenodo.org/api/records/13763756；字节：5906
- **PDMX.tar.gz** — 状态：downloaded；原件：[raw/PDMX.tar.gz](../../../../../origin_resources/sources/pdmx/raw/PDMX.tar.gz)；来源：https://zenodo.org/records/13763756/files/PDMX.tar.gz?download=1；字节：1588637145；说明：Pinned original 2024 record, not all later MusicXML expansion archives.

## 本地阅读副本

- [code-LICENSE.txt](../../../../text/source-copies/pdmx/code-LICENSE.txt)
- [README.md](../../../../text/source-copies/pdmx/README.md)
- [zenodo-record.json](../../../../text/source-copies/pdmx/zenodo-record.json)


## 其他清单元数据

{
  "source": "pdmx",
  "acquired_at": "2026-10-21T18:36:32.225836+00:00"
}
