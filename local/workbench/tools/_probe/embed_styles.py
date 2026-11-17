import io, re

w3 = r"local\workbench\scores\score-s3"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    return "\n".join(body).rstrip("\n")

art = r"content\styles\orchestral-timbre-aesthetic-shift.md"
s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")

titles = {
1: [("bach-bwv1050-mvt1-mm1-9-tutti.ly", "巴赫 BWV 1050 第一乐章 第 1–9 小节（通奏低音与主奏并置）", "mm. 1–9")],
2: [("haydn-hob-i-104-mvt1-mm17-32-strings.ly", "海顿 Hob.I:104 第一乐章 第 17–31 小节（弦乐弱奏）", "mm. 17–31"),
    ("haydn-hob-i-104-mvt1-mm33-40-tutti.ly", "海顿 Hob.I:104 第一乐章 第 32–39 小节（全奏，圆号八度 D 长音）", "mm. 32–39")],
}

out, i = [], 0
while i < len(lines):
    ln = lines[i]
    m = re.search(r"历史谱例片段 (\d)：", ln)
    if m and int(m.group(1)) in titles:
        n = int(m.group(1))
        out.append(ln)
        i += 1
        # 保留 blockquote，但去掉“交付状态”行并改写定位
        while i < len(lines) and lines[i].startswith(">"):
            t = lines[i]
            if "交付状态" in t:
                i += 1
                continue
            if n == 2:
                t = t.replace("mm. 17–32", "mm. 17–31（弦乐）与 mm. 32–39（全奏）")
            out.append(t)
            i += 1
        for fn, title, loc in titles[n]:
            out += ["", '```lilypond title="' + title + '" location="' + loc + '"', code_of(fn if fn.startswith("local") else w3 + "\\" + fn), "```"]
        continue
    # 片段 3：Op.67 IV 无可靠源 → 诚实占位
    if re.search(r"历史谱例片段 3：", ln):
        out.append(ln)
        i += 1
        while i < len(lines) and lines[i].startswith(">"):
            t = lines[i]
            if "交付状态" in t:
                out.append("> - **交付状态**：未交付。本地无可靠机器可读源（IMSLP 仅扫描且被 bot check 拦截；PDMX 该曲 17 声部转录自相矛盾、拍号与原作冲突，判定为不可用）。正文保留真实定位，待有可靠源时补齐。")
            else:
                out.append(t)
            i += 1
        continue
    out.append(ln)
    i += 1

s2 = "\n".join(out)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("fences:", s2.count("```lilypond"))