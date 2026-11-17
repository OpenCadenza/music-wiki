import io, re

p = r"local\workbench\scores\score-s3\haydn-hob-i-104-mvt1-mm33-40-tutti.ly"
lines = io.open(p, encoding="utf-8").read().split("\n")
out = []
for ln in lines:
    m = re.match(r"^\\(ff|f)\s+(\S+)(.*)$", ln)
    if m:
        out.append(m.group(2) + "\\" + m.group(1) + m.group(3))
    else:
        out.append(ln)
s = "\n".join(out)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("ok")