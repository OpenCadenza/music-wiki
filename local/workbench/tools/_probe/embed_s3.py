import io, os, re

art = r"content\techniques\material\motivic-inversion-and-harmonic-recontextualization.md"
w = r"local\workbench\scores\score-s3"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

specs = {
    1: [(os.path.join(w, "beethoven-op135-mvt4-mm1-4-grave.ly"), "贝多芬 Op.135 第四乐章 第 1–4 小节（Grave）", "mm. 1–4")],
    2: [(os.path.join(w, "beethoven-op135-mvt4-mm12-16-allegro.ly"), "贝多芬 Op.135 第四乐章 第 12–16 小节（Allegro）", "mm. 12–16")],
    4: [(os.path.join(w, "schubert-d328-mm1-5-prelude.ly"), "舒伯特 D.328《魔王》钢琴前奏 第 1–5 小节", "mm. 1–5"),
        (os.path.join(w, "schubert-d328-mm72-76-mein-vater.ly"), "舒伯特 D.328《魔王》第 72–76 小节", "mm. 72–76")],
}

s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")
out, i = [], 0
while i < len(lines):
    ln = lines[i]
    m = re.search(r"乐谱例证 (\d)[：:]", ln)
    if m and int(m.group(1)) in specs and "待交付" in ln:
        n = int(m.group(1))
        out.append(re.sub(r"待交付谱例定位（[^）]*）", "谱面定位", ln))
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            if "交付状态" not in lines[i]:
                out.append(lines[i])
            i += 1
        for ly, title, loc in specs[n]:
            out += ["", '```lilypond title="' + title + '" location="' + loc + '"', code_of(ly), "```"]
        continue
    out.append(ln)
    i += 1

s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("fences:", s2.count("```lilypond"), "placeholders:", s2.count("待交付谱例定位"))