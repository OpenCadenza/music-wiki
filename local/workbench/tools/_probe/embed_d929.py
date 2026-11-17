import io, os, re

ly = r"local\workbench\scores\score-s9\schubert-d929-mvt2-mm1-21.ly"
art = r"content\ensembles\piano-trio-acoustic-compromise.md"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")
out, i = [], 0
done = False
while i < len(lines):
    ln = lines[i]
    if (not done) and ln.strip().startswith("> 谱例待补：舒伯特 D.929"):
        out += ['```lilypond title="舒伯特 D.929 第二乐章" location="Andante con moto，mm.1–21"',
                code_of(ly), "```"]
        done = True
        i += 1
        # 跳过可能紧跟的多余空行
        while i < len(lines) and not lines[i].strip():
            i += 1
        out.append("")
        continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
s2 = re.sub(r"\n{3,}", "\n\n", s2)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("已替换:", done, "｜围栏数:", s2.count("```lilypond"))