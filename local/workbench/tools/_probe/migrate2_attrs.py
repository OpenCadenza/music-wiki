import glob, io, re

MOVE = {"一": "i", "二": "ii", "三": "iii", "四": "iv", "五": "v"}

TEMPO_WORDS = r"(Presto|Allegro|Adagio|Andante|Grave|Largo|Lento|Menuetto|Poco adagio|Poco allegretto|Maestoso|Choral|Schnell|Allegretto)"
TITLE_TAIL = re.compile(r"\s*(?:" + TEMPO_WORDS + r")\s*$")

# 每个文件的特殊 tempo 覆盖：(文件片段, 标题片段) -> tempo
OVERRIDE = {
    ("chromatic-suspension", "第 12–16 小节"): "Allegro",
    ("motivic-inversion", "第 12–16 小节（Allegro）"): "Allegro",
}

def tempo_names(body):
    return [m.group(1).strip() for m in re.finditer(r'\\tempo\s+"([^"]+)"', body)]

def bars_from(*texts):
    for txt in texts:
        if not txt:
            continue
        m = re.search(r"(\d+)\s*[–\-—~]\s*(\d+)", txt)
        if m:
            return m.group(1), m.group(2)
    for txt in texts:
        if not txt:
            continue
        m = re.search(r"(\d+)", txt)
        if m:
            return m.group(1), m.group(1)
    return None, None

def clean_title(title):
    t = title.strip()
    t = re.sub(r"[（(][^）)]*[）)]\s*$", "", t).strip()
    t = re.sub(r"第\s*\d+\s*[–\-—~]\s*\d+\s*小节.*$", "", t).strip()
    t = re.sub(r"\s*mm\..*$", "", t).strip()
    # 去掉标题尾部的速度词（与 location 重复）
    prev = None
    while prev != t:
        prev = t
        t = TITLE_TAIL.sub("", t).strip()
    if t.startswith("BWV"):
        t = "巴赫 众赞歌 " + t
    return t

def pick_tempo(path, title, body):
    for (frag, tkey), val in OVERRIDE.items():
        if frag in path and tkey in title:
            return val
    names = tempo_names(body)
    return names[0] if names else ""

files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
count = 0
for p in files:
    t = io.open(p, encoding="utf-8").read()
    out, pos = [], 0
    changed = False
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        out.append(t[pos:m.start()])
        attrs, body = m.group(1), m.group(2)
        tm = re.search(r'title="([^"]*)"', attrs)
        lm = re.search(r'location="([^"]*)"', attrs)
        title = tm.group(1) if tm else ""
        loc = lm.group(1) if lm else ""
        new_title = clean_title(title)
        a, b = bars_from(loc, title)
        rng = f"mm.{a}–{b}" if a and b else loc
        tn = pick_tempo(p, title + " " + loc, body)
        new_loc = f"{tn}，{rng}" if tn else rng
        new_attrs = attrs
        new_attrs = re.sub(r'title="[^"]*"', f'title="{new_title}"', new_attrs)
        new_attrs = re.sub(r'location="[^"]*"', f'location="{new_loc}"', new_attrs)
        if new_attrs != attrs:
            changed = True
            count += 1
        out.append("```lilypond" + new_attrs + "\n" + body + "```")
        pos = m.end()
    out.append(t[pos:])
    if changed:
        io.open(p, "w", encoding="utf-8", newline="\n").write("".join(out))
print("规范化围栏属性:", count)