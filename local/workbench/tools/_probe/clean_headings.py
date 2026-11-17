import io, re

p = r"content\composers\bach\chorale\cadential-voice-clock-and-phase-decoupling.md"
s = io.open(p, encoding="utf-8").read()
lines = s.split("\n")
out = []
for ln in lines:
    if ln.strip().startswith("> - **交付状态**"):
        continue
    ln = ln.replace("待交付谱例定位（真实小节规范）", "谱面定位")
    out.append(ln)
s2 = "\n".join(out)
io.open(p, "w", encoding="utf-8", newline="\n").write(s2)
print("placeholders:", s2.count("待交付谱例定位"), "fences:", s2.count("```lilypond"))
