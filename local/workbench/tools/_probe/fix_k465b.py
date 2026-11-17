import io

p = r"local\workbench\scores\score-s2\S2-K1-mozart-k465-4-m10-16.ly"
lines = io.open(p, encoding="utf-8").read().split("\n")

for i, ln in enumerate(lines):
    if 'Allegro molto' in ln and 'tempo' in ln:
        lines[i] = '  \\tempo "Allegro" 4 = 144'
    if ln == "  f''8 f''8 f''8 f''8 |":
        # m.14 Vn1 第 3 个八分：F♯5（源 acc=sharp）
        lines[i] = "  f''8 f''8 fs''8 f''8 |"
    if ln == "  a8 a8 gs8 gs8 |":
        # 大提琴 A♭3 拼写
        lines[i] = "  a8 a8 af8 af8 |"

s = "\n".join(lines)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("ok")