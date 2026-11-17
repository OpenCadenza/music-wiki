import io
p = r"content\techniques\sound\planes-of-tone-layering.md"
s = io.open(p, encoding="utf-8").read()
old = "值得注意的是，圆号在这十二小节里完全休止（本乐章圆号首次进入要到 m. 78）"
new = "值得注意的是，圆号在这十二小节里完全休止（本乐章圆号首次进入在 m. 40 末的弱起、m. 41 起陈述主题）"
print("found" if old in s else "MISS")
s = s.replace(old, new, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("ok")