import io, os, re

ly = r"local\workbench\scores\assistant-scores-c\beethoven-op135-mvt4-mm165-172-grave.ly"
art = r"content\techniques\material\motivic-inversion-and-harmonic-recontextualization.md"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")
out, i = [], 0
while i < len(lines):
    ln = lines[i]
    if re.search(r"乐谱例证 3：待交付谱例定位", ln):
        out.append(re.sub(r"待交付谱例定位（[^）]*）", "谱面定位", ln))
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            if "交付状态" not in lines[i]:
                out.append(lines[i])
            i += 1
        out += ["", '```lilypond title="贝多芬 Op.135 第四乐章 第 165–172 小节（Grave）" location="mm. 165–172"', code_of(ly), "```"]
        continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("fences:", s2.count("```lilypond"), "placeholders:", s2.count("待交付谱例定位"))