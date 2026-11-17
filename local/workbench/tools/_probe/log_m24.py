import io

log = r"local\docs\实施记录\2026-11-16-DSH首批\批次日志.md"
add = """

## 2026-11-18 M24 PDMX MusicXML 归档取回（编制篇最后一搏）

### 下载与解包

- 从 Zenodo 记录 15571083 取回 `mxl.tar.gz`（1,894,335,797 B，约 1.8 GB），单连接约 500 KB/s，历时约 1 小时。
- **归档结构与清单不符**：`score-s7` 的清单写 `PDMX/mxl/N/d/<hash>.mxl`，实际归档是 `mxl/<两位hex>/<两位hex>/<hash>.mxl`。按清单路径 `tar --include` 全部 Not found；最终用 `members-map.json` 里的文件名前缀在归档里按 basename 匹配，一次解出 5 份。
- 已解出并归档到 `scholar-plan-dev/local/resources/scores/pdmx/`（附 README 记录来源与许可）：

| 归档目录 | 内容 | 大小 |
| --- | --- | --- |
| `nielsen-op43-full/` | Nielsen 管乐五重奏 Op.43 全曲（5 声部，各 507 小节） | 198 KB |
| `nielsen-kvnintet/` | 另一份 Nielsen 转录（丹麦语声部名，各 147 小节） | 76 KB |
| `schubert-d929-ii-a/` `-b/` `-c/` | Schubert D.929 第二乐章三份转录（4 声部，各 212 小节） | 99／100／126 KB |

- 反例记录：`score-s7` 曾判定 PDMX **JSON** 数据集里 Nielsen 与 D.929 声部小节错位、不可用——这判断对 JSON 有效，但 `mxl.tar.gz` 是独立的 MusicXML 导出，与 JSON 不同源，故仍可用（内容正确性另行逐音核验）。

### 编码

- `score-s8`：Nielsen Op.43 第一乐章开头 12 小节（含 1 拍弱起）。第一乐章边界由「每声部小节号三次重启 0–146/1–82/1–278」定位；拍号 4/4（common）、E 大调；A 调单簧管与 F 调圆号按记谱音写并加 `\\transposition`。发现 XML 第 8 小节标 5/4 且各声部多一个四分休止，判为 OMR 多读一拍，按 4/4 归一（记录里给了改回原样的做法）。
- `score-s9`：Schubert D.929 第二乐章 mm.1–21。三份源逐音完全一致（仅一份多德文和弦名 direction），主源取 98 KB 那份。2/4、c 小调；XML 只给 `tempo=40`，对 Andante con moto 偏慢，按要求照取并标注。文章两处说法经核对成立（大提琴 mm.3 起接管旋律、小提琴 mm.1–20 全休止；钢琴断奏音型），但「主题头部」实际在 m.4（m.3 两个 g 是引导）。

两段均已逐音对 XML 自查（0 差异；S9 首轮自查抓到并修了两处手误），现由独立核验员复核。

## 待办（主控）"""
s = io.open(log, encoding="utf-8").read()
s = s.replace("## 待办（主控）", add, 1)
io.open(log, "w", encoding="utf-8", newline="\n").write(s)
print("log ok")