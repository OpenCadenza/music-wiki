import io, os, re

work2 = r"local\workbench\scores\score-s2"
work1 = r"local\workbench\scores\score-s1"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

def embed(art, specs, skip_status_line=True):
    s = io.open(art, encoding="utf-8").read()
    lines = s.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        m = re.search(r"乐谱例证 (\d)：待交付谱例定位", ln)
        if m and int(m.group(1)) in specs:
            n = int(m.group(1))
            ly, title, loc = specs[n]
            out.append(re.sub(r"待交付谱例定位（[^）]*）", "谱面定位", ln))
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                if "交付状态" not in lines[i]:
                    out.append(lines[i])
                i += 1
            out += ["", '```lilypond title="' + title + '" location="' + loc + '"', code_of(ly), "```"]
            continue
        out.append(ln)
        i += 1
    s2 = "\n".join(out)
    io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
    print(art, "fences:", s2.count("```lilypond"), "placeholders:", s2.count("待交付谱例定位"))

embed(r"content\composers\beethoven\quartets\chromatic-suspension-and-structural-topology.md", {
    1: (os.path.join(work2, "S2-D1-beethoven-op74-m18-24.ly"), "贝多芬 Op.74 第一乐章 第 18–24 小节", "mm. 18–24"),
    2: (os.path.join(work2, "S2-D2-beethoven-op131-m6-11.ly"), "贝多芬 Op.131 第一乐章 第 6–11 小节", "mm. 6–11"),
    3: (os.path.join(work2, "S2-D3-beethoven-op132-m1-8.ly"), "贝多芬 Op.132 第一乐章 第 1–8 小节", "mm. 1–8"),
})

embed(r"content\techniques\harmony\neapolitan-chord-structural-mutation.md", {
    2: (os.path.join(work2, "S2-C1-beethoven-op95-m1-8.ly"), "贝多芬 Op.95 第一乐章 第 1–8 小节", "mm. 1–8"),
    3: (os.path.join(work2, "S2-C2-beethoven-op95-m19-24.ly"), "贝多芬 Op.95 第一乐章 第 19–24 小节", "mm. 19–24"),
})

# 那不勒斯例证1：教科书模型，非真实作品，保留占位但改成诚实表述
art = r"content\techniques\harmony\neapolitan-chord-structural-mutation.md"
s = io.open(art, encoding="utf-8").read()
s = s.replace("> **乐谱例证 1：待交付谱例定位（规范前属对照模型）**",
              "> **乐谱例证 1：教科书规范前属模型（非真实作品原谱）**")
s = s.replace("> - **交付状态**：待资料助手核验理论代码后替换嵌入",
              "> - **说明**：这是教材式规范句法模型（i → N⁶ → V⁷ → i），不是任何一部作品的原谱，因此不按真实作品编码，留待作者决定是否改为示意性谱例或删除。")
io.open(art, "w", encoding="utf-8", newline="\n").write(s)

# 挂留篇例证4：与半音挂留篇同一段 Op.74 mm.18–24，按“同一段谱例全库只保留一份”改成链接
art = r"content\techniques\counterpoint\suspension-mechanics-and-voice-leading.md"
s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")
out, i = [], 0
while i < len(lines):
    ln = lines[i]
    if re.search(r"乐谱例证 4：待交付谱例定位", ln):
        out.append("> **乐谱例证 4：见同库另一篇的同一段谱例**")
        out.append(">")
        out.append("> 本段 Op. 74 第一乐章 mm. 18–24 的谱例已嵌入[《结构功能化的半音挂留》](../../composers/beethoven/quartets/chromatic-suspension-and-structural-topology.md)（该篇从和声链与调性拓扑角度分析同一片段）。全库同一段谱例只保留一份，此处不重复收录，读者可在该篇查看完整四声部乐谱。")
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            i += 1
        continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("suspension placeholders:", s2.count("待交付谱例定位"))
