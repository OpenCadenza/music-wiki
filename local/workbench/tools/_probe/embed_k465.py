import io, os, re

w2 = r"local\workbench\scores\score-s2"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

art = r"content\techniques\harmony\augmented-sixth-mechanics-and-syntactic-drift.md"
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
        if "K. 465" in text:
            for b in block:
                if "谱例占位" in b:
                    out.append("> **谱面定位**")
                elif "交付状态" in b:
                    continue
                else:
                    out.append(b)
            out.append("> - **编号基准**：小节号按 OpenScore 的零基计数（弱起 = 第 0 小节）；若按「弱起算第 1 小节」的通行计法，对应印刷谱 mm. 11–17。")
            out += ["", '```lilypond title="莫扎特 K.465 第四乐章 第 10–16 小节" location="mm. 10–16"', code_of(os.path.join(w2, "S2-K1-mozart-k465-4-m10-16.ly")), "```"]
            i = j
            continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("fences:", s2.count("```lilypond"))