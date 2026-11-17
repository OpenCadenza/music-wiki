import io

p = r"local\workbench\scores\score-s4\beethoven-op2no3-mvt1-mm1-13.ly"
s = io.open(p, encoding="utf-8").read()
old = "\\D fs,4 ~ | % 11"
new = "\\D fs,4 | % 11"
print("found" if old in s else "MISS")
s = s.replace(old, new, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)

# 文章：Op.111 Allegro 拍号 2/2 → 4/4
a = r"content\composers\beethoven\piano-sonatas\slow-introduction-integration.md"
t = io.open(a, encoding="utf-8").read()
before = t.count("Allegro 2/2 拍")
t = t.replace("- **调性与拍号**：c 小调，Maestoso 4/4 拍 $\\rightarrow$ Allegro 2/2 拍",
              "- **调性与拍号**：c 小调，Maestoso 4/4 拍 $\\rightarrow$ Allegro 也是 4/4 拍（全乐章只有一个拍号，速度加快而拍号不变）")
io.open(a, "w", encoding="utf-8", newline="\n").write(t)
print("article replaced; before:", before, "after:", t.count("Allegro 2/2 拍"))