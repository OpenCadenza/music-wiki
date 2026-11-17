import io, os

ly = r"local\workbench\scores\score-s6\beethoven-op109-mvt3-mm1-8.ly"
art = r"content\techniques\harmony\augmented-sixth-mechanics-and-syntactic-drift.md"

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
    if "【谱例占位" in ln:
        block, j = [], i
        while j < len(lines) and lines[j].startswith(">"):
            block.append(lines[j])
            j += 1
        text = "\n".join(block)
        if "Op. 109" in text:
            for b in block:
                if "谱例占位" in b:
                    out.append("> **谱面定位**")
                elif "交付状态" in b:
                    continue
                else:
                    out.append(b)
            out.append("> - **速度与力度来源**：`4 = 84` 与 m.8 的 *p* 均据 Kern，DCML 该段没有节拍机与力度标记。")
            out += ["", '```lilypond title="贝多芬 Op.109 第三乐章 第 1–8 小节" location="mm. 1–8"', code_of(ly), "```"]
            i = j
            continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("fences:", s2.count("```lilypond"))