import io, re

p = r"local\workbench\scores\score-s3\haydn-hob-i-104-mvt1-mm33-40-tutti.ly"
lines = io.open(p, encoding="utf-8").read().split("\n")

ff_names = {"flautoOne", "flautoTwo", "oboeOne", "oboeTwo",
            "violinOne", "violinTwo", "viola", "cello", "bass"}
f_names = {"cornoOne", "cornoTwo", "timpani"}

out = []
i = 0
while i < len(lines):
    ln = lines[i]
    m = re.match(r"^(\w+) = \{ \\global \\clef (\w+) \|$", ln)
    if m:
        name = m.group(1)
        if name in ff_names:
            out.append(ln + " \\ff")
            i += 1
            continue
        if name in ("cornoOne", "cornoTwo"):
            out.append(ln + " \\transposition d \\f")
            i += 1
            # 圆号：实音 D→written C（D 调圆号记谱比实音高小七度）
            if name == "cornoOne":
                while i < len(lines) and not lines[i].startswith("cornoTwo") and lines[i].strip() != "}":
                    out.append(lines[i].replace("d'", "c''").replace("d1", "c''1").replace("d2", "c''2").replace("d4", "c''4"))
                    i += 1
                continue
            else:
                while i < len(lines) and lines[i].strip() != "}":
                    out.append(lines[i].replace("d1", "c'1").replace("d2", "c'2").replace("d4", "c'4"))
                    i += 1
                continue
        if name == "timpani":
            out.append(ln + " \\f")
            i += 1
            continue
    out.append(ln)
    i += 1

s = "\n".join(out)
# 圆号 m.39–40 连音线
s = s.replace("  c''1 |\n  c''1 \\bar \"|.\" }", "  c''1~ |\n  c''1 \\bar \"|.\" }")
s = s.replace("  c'1 |\n  c'1 \\bar \"|.\" }", "  c'1~ |\n  c'1 \\bar \"|.\" }")
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("done")