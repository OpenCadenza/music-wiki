import io, re

# 1) Op.135 第四乐章 mm.12–16 的实际速度是 Allegro（前一小节末为 Grave）
p1 = r"content\techniques\material\motivic-inversion-and-harmonic-recontextualization.md"
t = io.open(p1, encoding="utf-8").read()
t = t.replace('location="Grave ma non troppo tratto，mm.12–16"', 'location="Allegro，mm.12–16"')
io.open(p1, "w", encoding="utf-8", newline="\n").write(t)

# 2) K.309 缺 tempo：按文章的速度标记补文本，播放值标注为推定
p2 = r"content\techniques\structure\cadential-evasion-and-temporal-expansion.md"
t2 = io.open(p2, encoding="utf-8").read()
t2 = t2.replace('location="mm.9–19"', 'location="Allegretto grazioso，mm.9–19"')
old = "\\tempo \"Allegro con brio\""
# 在 K.309 片段中插入 tempo：定位该 fence 的 \version 后的 \language 行
m = re.search(r'(```lilypond title="莫扎特 K\.309[^\n]*\n\\version "2\.26\.0"\n\\language "english"\n)', t2)
if m:
    insert = "\\tempo \"Allegretto grazioso\" 4 = 120  % 播放值按 Allegretto grazioso 推定（源无节拍机）\n"
    t2 = t2[:m.end()] + insert + t2[m.end():]
    io.open(p2, "w", encoding="utf-8", newline="\n").write(t2)
    print("K.309 tempo 已补")
else:
    print("未找到 K.309 fence 头部，需手工处理")