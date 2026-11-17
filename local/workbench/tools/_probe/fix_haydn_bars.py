import io, re

# 1) 弦乐摘录：去掉 kern 的空小节（m.17 只有 1 拍休止），使谱面号 = 印刷谱 mm.17–31
p1 = r"local\workbench\scores\score-s3\haydn-hob-i-104-mvt1-mm17-32-strings.ly"
s = io.open(p1, encoding="utf-8").read()
s = s.replace("  \\partial 4\n", "")
s = re.sub(r"  r4 \|\s*% m\.17[^\n]*\n", "", s)
s = s.replace("\\set Score.currentBarNumber = #17", "\\set Score.currentBarNumber = #17")
io.open(p1, "w", encoding="utf-8", newline="\n").write(s)
print("strings ok; partial left:", s.count("\\partial"))

# 2) 全奏摘录：kern m.33 = 印刷谱 m.32
p2 = r"local\workbench\scores\score-s3\haydn-hob-i-104-mvt1-mm33-40-tutti.ly"
s2 = io.open(p2, encoding="utf-8").read()
s2 = s2.replace("\\set Score.currentBarNumber = #33", "\\set Score.currentBarNumber = #32")
s2 = s2.replace("mm. 33–40", "mm. 32–39")
io.open(p2, "w", encoding="utf-8", newline="\n").write(s2)
print("tutti ok")