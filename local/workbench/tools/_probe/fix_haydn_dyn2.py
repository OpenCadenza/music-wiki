import io, re

p = r"local\workbench\scores\score-s3\haydn-hob-i-104-mvt1-mm33-40-tutti.ly"
lines = io.open(p, encoding="utf-8").read().split("\n")

out = []
pending = None
for ln in lines:
    m = re.match(r"^(.*\|) \\(ff|f)$", ln)
    m2 = re.match(r"^(.*\|) \\transposition d \\f$", ln)
    if m:
        out.append(m.group(1))
        pending = "\\" + m.group(2)
        continue
    if m2:
        out.append(m2.group(1) + " \\transposition d")
        pending = "\\f"
        continue
    if pending and ln.strip():
        out.append(pending + " " + ln)
        pending = None
        continue
    out.append(ln)

s = "\n".join(out)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("ok")