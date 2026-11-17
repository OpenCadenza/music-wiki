import io, os, re

root = os.getcwd()
art = r"content\techniques\counterpoint\suspension-mechanics-and-voice-leading.md"
work = r"local\workbench\scores\score-s1"

specs = {
    1: (os.path.join(work, "bwv087-7-mm01-03-suspension.ly"), "BWV 87/7 第 1–3 小节", "mm. 1–3"),
    2: (os.path.join(work, "bwv0269-mm05-07-pac.ly"), "BWV 269 第 5–7 小节", "mm. 5–7"),
    3: (os.path.join(work, "bwv060-5-mm01-04-tritone.ly"), "BWV 60/5 第 1–4 小节", "mm. 1–4"),
}

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    # 从第一行 \version 开始，去掉 % 注释行
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")

out = []
i = 0
while i < len(lines):
    ln = lines[i]
    m = re.search(r"乐谱例证 (\d)：待交付谱例定位", ln)
    if m and int(m.group(1)) in specs:
        n = int(m.group(1))
        ly, title, loc = specs[n]
        out.append(ln.replace("待交付谱例定位（真实小节规范）", "谱面定位"))
        i += 1
        # 复制 blockquote 行，丢弃“交付状态”
        while i < len(lines) and lines[i].startswith(">"):
            if "交付状态" not in lines[i]:
                out.append(lines[i])
            i += 1
        out.append("")
        out.append('```lilypond title="' + title + '" location="' + loc + '"')
        out.append(code_of(ly))
        out.append("```")
        continue
    out.append(ln)
    i += 1

s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("fences:", s2.count("```lilypond"), "remaining placeholders:", s2.count("待交付谱例定位"))
