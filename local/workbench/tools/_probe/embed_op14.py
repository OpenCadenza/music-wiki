import io, os, re

ly = r"local\workbench\scores\score-s5\beethoven-op14-1-mvt1-mm1-16.ly"
art = r"content\ensembles\bidirectional-selection-of-musical-ideas-and-medium.md"

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
    if "跨编制转译对照例证 1" in ln:
        block, j = [], i
        while j < len(lines) and lines[j].startswith(">"):
            block.append(lines[j])
            j += 1
        for b in block:
            if "交付状态" in b:
                out.append("> - **收录情况**：仅收录钢琴原作 Op. 14 No. 1 的开篇；改编版 Hess 34 暂无可靠机器可读源，未收录（正文对其音区、空弦与织体重构的分析依据版本记述与原文描述）。")
            else:
                out.append(b)
        out += ["", '```lilypond title="贝多芬 Op.14 No.1 第一乐章 第 1–16 小节" location="mm. 1–16"', code_of(ly), "```"]
        i = j
        continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("fences:", s2.count("```lilypond"))