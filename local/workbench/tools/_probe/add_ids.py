import glob, io, re

COMPOSER = {
    "巴赫": "bach", "贝多芬": "beethoven", "莫扎特": "mozart", "海顿": "haydn",
    "舒伯特": "schubert", "尼尔森": "nielsen", "卡尔·尼尔森": "nielsen",
}
MOV = {"第一乐章": "i", "第二乐章": "ii", "第三乐章": "iii", "第四乐章": "iv"}


def slug_work(title):
    t = title
    m = re.search(r"Op\.?\s*(\d+)(?:\s*No\.?\s*(\d+))?", t)
    if m:
        return f"op{m.group(1)}" + (f"no{m.group(2)}" if m.group(2) else "")
    m = re.search(r"\bBWV\s*(\d+)", t)
    if m:
        return f"bwv{m.group(1)}"
    m = re.search(r"\bK\.?\s*(\d+)", t)
    if m:
        return f"k{m.group(1)}"
    m = re.search(r"Hob\.?\s*I:(\d+)", t)
    if m:
        return f"hob1-{m.group(1)}"
    m = re.search(r"Hob\.?\s*XVI:(\d+)", t)
    if m:
        return f"hob16-{m.group(1)}"
    m = re.search(r"\bD\.?\s*(\d+)", t)
    if m:
        return f"d{m.group(1)}"
    return re.sub(r"[^a-z0-9]+", "", t.lower())[:20]


def slug_bars(loc):
    m = re.search(r"mm\.\s*(\d+)\s*[–\-~]\s*(\d+)", loc)
    if m:
        return f"mm{m.group(1)}-{m.group(2)}"
    m = re.search(r"mm\.\s*(\d+)", loc)
    if m:
        return f"mm{m.group(1)}"
    return "mm1"


files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
made = 0
for p in files:
    t = io.open(p, encoding="utf-8").read()
    out, pos = [], 0
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        out.append(t[pos:m.start()])
        attrs, body = m.group(1), m.group(2)
        tm = re.search(r'title="([^"]*)"', attrs)
        lm = re.search(r'location="([^"]*)"', attrs)
        title = tm.group(1) if tm else ""
        loc = lm.group(1) if lm else ""
        composer = next((v for k, v in COMPOSER.items() if k in title), "unknown")
        work = slug_work(title)
        mov = next((v for k, v in MOV.items() if k in title), "")
        bars = slug_bars(loc)
        base = "-".join(x for x in (composer, work, mov, bars) if x)
        sid = base
        n = 1
        while re.search(r'id="' + re.escape(sid) + r'"', attrs):
            n += 1
            sid = f"{base}-{n}"
        if 'id="' not in attrs:
            attrs = attrs + f' id="{sid}"'
            made += 1
        out.append("```lilypond" + attrs + "\n" + body + "```")
        pos = m.end()
    out.append(t[pos:])
    new = "".join(out)
    if new != t:
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
print("补 id 的围栏:", made)

# 输出 id 清单
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r"```lilypond([^\n]*)\n", t):
        i = re.search(r'id="([^"]*)"', m.group(1))
        ti = re.search(r'title="([^"]*)"', m.group(1))
        lo = re.search(r'location="([^"]*)"', m.group(1))
        print(f"{i.group(1) if i else '?':40s} {ti.group(1) if ti else '':40s} {lo.group(1) if lo else ''}")
