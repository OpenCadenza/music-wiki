import glob, io, re

def fields(block):
    text = "\n".join(block)
    def grab(*keys):
        for k in keys:
            m = re.search(k + r"[：:]\s*(.+)", text)
            if m:
                return m.group(1).strip()
        return ""
    work = grab(r"\*\*作品\*\*", r"作品")
    bars = grab(r"\*\*乐章与小节\*\*", r"\*\*小节范围\*\*", r"小节范围", r"乐章与小节")
    return work, bars

DELETE_KEYS = ("谱面定位", "待填装谱例片段", "待交付谱例定位", "乐谱例证")
KEEP_KEYS = ("相关谱例", "同一段谱例")

count_del = count_conv = 0
for p in [q for q in glob.glob("content/**/*.md", recursive=True) if not q.endswith("index.md")]:
    lines = io.open(p, encoding="utf-8").read().split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if ln.lstrip().startswith(">"):
            block, j = [], i
            while j < len(lines) and lines[j].lstrip().startswith(">"):
                block.append(lines[j])
                j += 1
            text = "\n".join(block)
            nxt = ""
            k = j
            while k < len(lines) and not lines[k].strip():
                k += 1
            if k < len(lines):
                nxt = lines[k]
            has_fence = nxt.lstrip().startswith("```lilypond")
            if any(key in text for key in KEEP_KEYS):
                out.extend(block)
                i = j
                continue
            if any(key in text for key in DELETE_KEYS):
                if has_fence:
                    # 谱例已入正文：整块删除（main 没有这种信息块）
                    count_del += 1
                    i = j
                    # 去掉遗留空行
                    while i < len(lines) and not lines[i].strip():
                        i += 1
                    if out and out[-1].strip():
                        out.append("")
                    continue
                else:
                    # 未补的占位：改成 main 的一行式
                    work, bars = fields(block)
                    work = work.strip()
                    bars = bars.strip()
                    head = "，".join(x for x in (work, bars) if x)
                    out.append(f"**{head}**")
                    out.append("")
                    out.append(f"> 谱例待补：{work} {bars}。".replace("  ", " "))
                    count_conv += 1
                    i = j
                    while i < len(lines) and not lines[i].strip():
                        i += 1
                    if out and out[-1].strip():
                        out.append("")
                    continue
            out.extend(block)
            i = j
            continue
        out.append(ln)
        i += 1
    new = "\n".join(out)
    new = re.sub(r"\n{3,}", "\n\n", new)
    io.open(p, "w", encoding="utf-8", newline="\n").write(new)
print("删除信息块:", count_del, "｜占位改一行式:", count_conv)