import io

cat = r"local\resources\catalog\score-deliveries.md"
add = """
| SCR-038 | 尼尔森 管乐五重奏 Op.43 第一乐章 开头 12 小节 | S8 | **核验未过、返修中**：速度文字应为 Allegro ben moderato；第 7 小节原为 5/4（校勘版谱面证实），交付件误归一为 4/4；另有小节号幽灵号与编号表述问题 |
| SCR-039 | 舒伯特 D.929 第二乐章 mm.1–21 | S9 | 核验通过（补 13 条力度、修 m.16 连音线、隐藏节拍机后），已入正文 |

### 新增谱源：PDMX MusicXML（2026-11-17）

Zenodo 记录 15571083 的 `mxl.tar.gz`（1,894,335,797 B）已取回并解包，5 份 MusicXML 归档在 `scholar-plan-dev/local/resources/scores/pdmx/`（附 README）：Nielsen Op.43 全曲、Nielsen Kvintet 另一转录、Schubert D.929 二乐章三份转录。归档结构为 `mxl/<两位hex>/<两位hex>/<hash>.mxl`，与 `score-s7` 清单里的 `PDMX/mxl/...` 写法不同，按 `members-map.json` 的文件名前缀匹配解出。
"""
with io.open(cat, "a", encoding="utf-8", newline="\n") as f:
    f.write(add)
print("catalog ok")

log = r"local\docs\实施记录\2026-11-16-DSH首批\批次日志.md"
add2 = """

### M24 续：两段核验结果

- **Schubert D.929 第二乐章**：核验发现 3 处缺陷（13 条力度全缺、m.16 连音线起点晚一个十六分、谱面误印 ♩=40）。生产者已全部修正（力度逐条按 XML 定位；用 `\\set Score.tempoWholesPerMinute = 10` 保留播放速度但不印节拍机），重跑比对 0 差异，**已入正文**（围栏 38 块）。核验同时指出正文 4 处表述问题（大提琴实际 F2–E♭4 而不是 C4–G4、"左右手跳音"不精确、"稍快板"自相矛盾、判定流程 G3–C5 高估），已记入 `待作者修订清单.md` 第 11–15 条，等 gemini 恢复后由学者改。
- **Nielsen Op.43**：核验判定不能按当前版回填——速度文字应为 `Allegro ben moderato`（生产者写成 marcato，源自唱片条目笔误）；第 7 小节**原谱确为 5/4**（核验拿到 Spence 校勘版谱面，主控已目视确认"5/4"字样），生产者按 4/4 归一导致四声部该小节及之后所有 onset 提前一拍；另需删 `BarNumber.break-visibility` override 并改正"全曲 2535 小节/谱例 1–12 小节"两处注释。已派回返修，改完再核验一次后回填。

## 待办（主控）"""
s = io.open(log, encoding="utf-8").read()
s = s.replace("## 待办（主控）", add2, 1)
io.open(log, "w", encoding="utf-8", newline="\n").write(s)
print("log ok")