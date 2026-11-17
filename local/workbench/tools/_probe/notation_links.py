import io, re

art = r"content\notation\clef-octave-ambiguity-and-encoding-loss.md"

repl = {
1: ("> **乐谱例证 1：八度倒错对比（待交付标准谱例）**",
    """> **相关谱例（同库唯一收录）**
>
> 本段 Op. 135 第四乐章 mm. 12–16 的完整四声部谱例已收录在[《核心细胞的倒影变形与和声再语境化》](../techniques/material/motivic-inversion-and-harmonic-recontextualization.md)（同一作品的同一片段，全库只保留一份）。读者对照该谱时，重点看中提琴声部开场的小字组 C3 位置与大提琴的最低音 C2——正是本节讨论的八度基准所在。"""),
2: ("> **乐谱例证 2：调号与音名方言对比（待交付标准谱例）**",
    """> **相关谱例（同库唯一收录）**
>
> 本段 Op. 74 第一乐章慢引子（含 m. 6–9）的四声部谱例已收录在[《加兰特图式在古典句法中的曲式功能整合》](../techniques/structure/galant-schemata-and-formal-functions.md)。读者对照该谱时，可核对第 9 小节第一小提琴花彩的音名是否显式带降号，以及第 6–8 小节大提琴的实际音区（B♭2，而不是低八度的 B♭1）。"""),
3: ("> **乐谱例证 3：演奏法与声乐织体校正对比（待交付标准谱例）**",
    """> **相关谱例（同库唯一收录）**
>
> D. 328《魔王》的两段谱例（钢琴前奏 mm. 1–5、独唱段 mm. 72–76）已收录在[《核心细胞的倒影变形与和声再语境化》](../techniques/material/motivic-inversion-and-harmonic-recontextualization.md)。读者对照该谱时，注意左手第 2、4 小节的垂直短跳音记号，以及第 76 小节独唱声部第 4 拍的弱起音。"""),
}

s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")
out, i = [], 0
while i < len(lines):
    ln = lines[i]
    m = re.search(r"乐谱例证 (\d)：", ln)
    if m and int(m.group(1)) in repl and ("待交付" in ln or "待填装" in ln):
        n = int(m.group(1))
        head, pointer = repl[n]
        if ln.strip() != head:
            # 行首可能有其它修饰，按整行替换
            pass
        out += pointer.split("\n")
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            i += 1
        continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("remaining placeholders:", s2.count("待交付标准谱例"), s2.count("待填装"))