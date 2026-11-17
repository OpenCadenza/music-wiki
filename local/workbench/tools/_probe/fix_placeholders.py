import io, re, subprocess

files = [
    "content/techniques/sound/timbral-contrast-and-formal-articulation.md",
    "content/techniques/harmony/neapolitan-chord-structural-mutation.md",
    "content/ensembles/piano-trio-acoustic-compromise.md",
    "content/ensembles/wind-quintet-acoustic-balance.md",
]

def old_text(p):
    out = subprocess.run(["git", "show", "HEAD:" + p], capture_output=True)
    return out.stdout.decode("utf-8")

def extract_titles(t):
    titles = []
    lines = t.split("\n")
    i = 0
    while i < len(lines):
        if lines[i].lstrip().startswith(">") and ("待填装谱例片段" in lines[i] or "待交付谱例定位" in lines[i]):
            block, j = [], i
            while j < len(lines) and lines[j].lstrip().startswith(">"):
                block.append(lines[j])
                j += 1
            text = "\n".join(block)
            m = re.search(r"【待填装谱例片段：(.+?)】", text)
            if m:
                titles.append(m.group(1).strip())
            else:
                w = re.search(r"\*\*作品\*\*[：:]\s*(.+)", text)
                b = re.search(r"\*\*小节范围\*\*[：:]\s*(.+)", text) or re.search(r"\*\*乐章与小节\*\*[：:]\s*(.+)", text)
                parts = []
                if w: parts.append(w.group(1).strip())
                if b: parts.append(b.group(1).strip())
                titles.append(" ".join(parts).strip())
            i = j
            continue
        i += 1
    return titles

for p in files:
    old = old_text(p)
    titles = extract_titles(old)
    cur = io.open(p, encoding="utf-8").read()
    n = cur.count("****\n\n> 谱例待补： 。")
    if n != len(titles):
        print(p, "数量不匹配: 占位", n, "标题", len(titles), titles)
        continue
    for t in titles:
        block = f"**{t}**\n\n> 谱例待补：{t}。"
        cur = cur.replace("****\n\n> 谱例待补： 。", block, 1)
    io.open(p, "w", encoding="utf-8", newline="\n").write(cur)
    print(p, "修复", len(titles), "处")