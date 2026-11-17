import io, os, re

w1 = r"local\workbench\scores\score-s1"
w2 = r"local\workbench\scores\score-s2"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

def embed(art, match_key, ly, title, loc, note=None):
    s = io.open(art, encoding="utf-8").read()
    lines = s.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if "【待填装谱例片段" in ln or "【谱例占位" in ln or "历史谱例片段" in ln or ("跨编制转译对照例证" in ln):
            block, j = [], i
            while j < len(lines) and lines[j].startswith(">"):
                block.append(lines[j])
                j += 1
            text = "\n".join(block)
            if match_key in text:
                for b in block:
                    if "待填装谱例片段" in b or "【谱例占位" in b:
                        out.append("> **谱面定位**")
                    elif "交付状态" in b:
                        continue
                    else:
                        out.append(b)
                if note:
                    out.append("> - **" + note + "**")
                out += ["", '```lilypond title="' + title + '" location="' + loc + '"', code_of(ly), "```"]
                i = j
                continue
        out.append(ln)
        i += 1
    s2 = "\n".join(out)
    io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
    print(art, "fences:", s2.count("```lilypond"))

sq = r"content\ensembles\string-quartet-acoustic-role-differentiation.md"
embed(sq, "Op. 76 No. 3",
      os.path.join(w1, "haydn-op76-3-mvt2-mm01-20-emperor.ly"),
      "海顿 Op.76 No.3《皇帝》第二乐章 第 1–20 小节（主题呈示）", "mm. 1–20（含弱起）",
      "范围说明：文章论述的 40 小节中，本谱例取主题呈示的 mm.1–20；变奏一（mm.21 起）未收录。")

embed(sq, "Op. 135 第三乐章",
      os.path.join(w1, "beethoven-op135-mvt3-mm01-12.ly"),
      "贝多芬 Op.135 第三乐章 第 1–12 小节", "mm. 1–12",
      "速度与力度说明：源工程无节拍机与力度层，速度按 Kern 与 DCML 的播放值取四分音符 = 50（待与印刷谱核对）。")

planes = r"content\techniques\sound\planes-of-tone-layering.md"
embed(planes, "Op. 67, Mov. II",
      os.path.join(w2, "S2-E3-beethoven-op67-2-m205-209-fagotto.ly"),
      "贝多芬 Op.67 第二乐章 第 205–209 小节（大管声部摘录）", "mm. 205–209",
      "摘录说明：只收录大管主题变体；弦乐的带休止反复和弦与低音点状短音未收录（无可逐音置信的四声部源）。")