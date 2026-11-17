import io, re

# 1) 待作者修订清单：补 Nielsen 编号表述条
p = r"local\docs\实施记录\2026-11-16-DSH首批\待作者修订清单.md"
s = io.open(p, encoding="utf-8").read()
add = """
### `ensembles/wind-quintet-acoustic-balance.md`（Nielsen Op.43 谱例）
17. **小节编号表述**：谱例实际覆盖 **印刷谱 mm.1–11 + 1 拍弱起**（共 12 个谱面小节，不含印本 m.12）。文章现在写"mm.1–12"，若按"12 小节"口语计法（含弱起）尚可，但严格说应写成"mm.1–11（含弱起）"。建议学者统一为"弱起 + mm.1–11"或把谱例延到 m.12。
18. **第 7 小节是 5/4**：该乐章开头第 7 小节为 5/4（校勘版谱面与 XML 一致），随后回 4/4。正文若描述"规整四拍"或"持续 4/4"，需补一句说明这处 5/4。
"""
if "Nielsen Op.43 谱例）" not in s:
    s = s.rstrip() + add
    io.open(p, "w", encoding="utf-8", newline="\n").write(s)
    print("checklist 追加")
else:
    print("checklist 已有，跳过")

# 2) catalog: SCR-038 状态更新
cat = r"local\resources\catalog\score-deliveries.md"
c = io.open(cat, encoding="utf-8").read()
c = c.replace("| SCR-038 | 尼尔森 管乐五重奏 Op.43 第一乐章 开头 12 小节 | S8 | **核验未过、返修中**：速度文字应为 Allegro ben moderato；第 7 小节原为 5/4（校勘版谱面证实），交付件误归一为 4/4；另有小节号幽灵号与编号表述问题 |",
              "| SCR-038 | 尼尔森 管乐五重奏 Op.43 第一乐章 开头 12 小节（弱起 + 印刷谱 mm.1–11） | S8 | 第 2 版已改：速度文字 Allegro ben moderato、恢复第 7 小节 5/4、修小节号与注释；**待核验员复核四处后回填** |")
io.open(cat, "w", encoding="utf-8", newline="\n").write(c)
print("catalog 更新")