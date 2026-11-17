import io

p = r"local\workbench\scores\score-s2\S2-K1-mozart-k465-4-m10-16.ly"
s = io.open(p, encoding="utf-8").read()
pairs = [
    ('\\tempo "Allegro molto" 4 = 160', '\\tempo "Allegro" 4 = 144'),
    ("f''8", "fs''8"),
    ("gs8", "af8"),
]
for a, b in pairs:
    if a not in s:
        print("MISS:", a)
    s = s.replace(a, b)
# 编号基准注明
s = s.replace('subtitle = "IV. Allegro', 'subtitle = "IV. Allegro')
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("done; tempo now:", s.count('4 = 144'), "fs:", s.count("fs''8"))