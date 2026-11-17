import io, re

p = r"content\techniques\structure\cadential-evasion-and-temporal-expansion.md"
t = io.open(p, encoding="utf-8").read()

# 撤回放错位置的 tempo 行
t = t.replace("\\tempo \"Allegretto grazioso\" 4 = 120  % 播放值按 Allegretto grazioso 推定（源无节拍机）\n", "", 1)

# 放进 upper 声部的 \time 之后
old = """upper = {
  \\clef "treble"
  \\key c \\major
  \\time 2/4
  \\set Score.currentBarNumber = #9"""
new = """upper = {
  \\clef "treble"
  \\key c \\major
  \\time 2/4
  \\tempo "Allegretto grazioso" 4 = 120  % 播放值按 Allegretto grazioso 推定（源无节拍机）
  \\set Score.currentBarNumber = #9"""
if old in t:
    t = t.replace(old, new, 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)
    print("已把 tempo 移入 upper")
else:
    print("未匹配，需手工处理")