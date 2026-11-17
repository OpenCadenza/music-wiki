import io, os, re

w4 = r"local\workbench\scores\score-s4"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

SPEC = [
    ("Op. 13", [("beethoven-op13-mvt1-mm1-19.ly", "贝多芬 Op.13《悲怆》第一乐章 第 1–19 小节", "mm. 1–19")]),
    ("Op. 81a", [("beethoven-op81a-mvt1-mm1-25.ly", "贝多芬 Op.81a《告别》第一乐章 第 1–25 小节", "mm. 1–25")]),
    ("Op. 111", [("beethoven-op111-mvt1-mm1-25.ly", "贝多芬 Op.111 第一乐章 第 1–25 小节", "mm. 1–25")]),
    ("K. 309", [("mozart-k309-mvt3-mm9-19.ly", "莫扎特 K.309 第三乐章 第 9–19 小节（NMA 印刷谱 10–20）", "mm. 9–19")]),
    ("Op. 2 No. 3", [("beethoven-op2no3-mvt1-mm1-13.ly", "贝多芬 Op.2 No.3 第一乐章 第 1–13 小节", "mm. 1–13")]),
]

def embed(art):
    s = io.open(art, encoding="utf-8").read()
    lines = s.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("> - **作品**"):
            # 收集整段 blockquote
            block = []
            j = i
            while j < len(lines) and lines[j].startswith(">"):
                block.append(lines[j])
                j += 1
            text = "\n".join(block)
            hit = next((k for k in SPEC if k[0] in text), None)
            placeholder = any(("交付状态" in b) or ("待填装" in b) or ("待谱例" in b) or ("占位" in b) for b in block)
            if hit and placeholder:
                out += [re.sub(r"待交付谱例定位（[^）]*）", "谱面定位", b) for b in block if "交付状态" not in b and "待填装" not in b]
                for fn, title, loc in hit[1]:
                    out += ["", '```lilypond title="' + title + '" location="' + loc + '"', code_of(os.path.join(w4, fn)), "```"]
                i = j
                continue
        out.append(ln)
        i += 1
    s2 = "\n".join(out)
    io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
    print(art, "fences:", s2.count("```lilypond"))

embed(r"content\composers\beethoven\piano-sonatas\slow-introduction-integration.md")
embed(r"content\techniques\structure\cadential-evasion-and-temporal-expansion.md")