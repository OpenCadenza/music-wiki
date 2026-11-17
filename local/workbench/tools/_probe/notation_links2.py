import io, re

art = r"content\notation\machine-readable-sources-and-evidence-hierarchy.md"
new = """> **证据链对齐示例（谱例见同库）**
>
> Op. 135 第四乐章 mm. 12–16 的四声部谱例收录在[《核心细胞的倒影变形与和声再语境化》](../techniques/material/motivic-inversion-and-harmonic-recontextualization.md)。同一片段在人工转写工程里曾被整体抬高一个八度（中提琴记成小字一组、大提琴记成大字组），与原生编码给出的中提琴 C3、大提琴 C2 相差整整八度——这正是本节所说"同一条旋律、两种可信度"的最直接例子。逐音核对的过程与旧件对照记录保存在研究区，不列入正文。"""

s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")
out, i = [], 0
while i < len(lines):
    ln = lines[i]
    if re.search(r"乐谱例证 1：证据链对齐", ln):
        out += new.split("\n")
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            i += 1
        continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("remaining 待交付:", s2.count("待交付"))