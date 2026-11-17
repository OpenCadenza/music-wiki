import io

cat = r"local\resources\catalog\score-deliveries.md"
c = io.open(cat, encoding="utf-8").read()
c = c.replace("| SCR-038 | 尼尔森 管乐五重奏 Op.43 第一乐章 开头 12 小节（弱起 + 印刷谱 mm.1–11） | S8 | 第 2 版已改：速度文字 Allegro ben moderato、恢复第 7 小节 5/4、修小节号与注释；**待核验员复核四处后回填** |",
              "| SCR-038 | 尼尔森 管乐五重奏 Op.43 第一乐章 开头 12 小节（弱起 + 印刷谱 mm.1–11） | S8 | 第 2 版核验**可放行**（5/4 恢复、速度文字、小节号、注释四处均过），已按新乐器契约回填正文 |")
io.open(cat, "w", encoding="utf-8", newline="\n").write(c)

log = r"local\docs\实施记录\2026-11-16-DSH首批\批次日志.md"
add = """
### M24 收尾：Nielsen 谱例入正文（围栏 39 块）

第 2 版通过复核：5/4 恢复后逐音比对五声部全部 PASS（无补偿）、成品 PDF 抽文本小节号为 1–11（无重复号与幽灵 12）、速度文字 `Allegro ben moderato`（♩=100 注明为试听值）。回填时同时按 2026-11-17 新乐器契约处理：删 `instrumentName`、清 `% GM` 注释，保留 `\\set Staff.midiInstrument` 标准名。

顺带确认：核验员为 "只留行首号" 的替代方案做了对照实验，证明 `break-visibility = #end-of-line-invisible` 是逐小节出号的必要条件（去掉后谱面只剩 4/6/8/10）——生产者的做法被采纳。

## 待办（主控）"""
s = io.open(log, encoding="utf-8").read()
s = s.replace("## 待办（主控）", add, 1)
io.open(log, "w", encoding="utf-8", newline="\n").write(s)
print("docs ok")