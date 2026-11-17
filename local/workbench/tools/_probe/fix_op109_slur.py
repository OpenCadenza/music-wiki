import io

p = r"local\workbench\scores\score-s6\beethoven-op109-mvt3-mm1-8.ly"
s = io.open(p, encoding="utf-8").read()
pairs = [
    ("      e4 e2 | % 7", "      s4 e2 | % 7"),
    ("      s4 <cs, cs>4 <c, c>4 | % 7", "      e4( <cs, cs>4 <c, c>4) | % 7"),
]
for a, b in pairs:
    print("found" if a in s else "MISS: " + a)
    s = s.replace(a, b, 1)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)