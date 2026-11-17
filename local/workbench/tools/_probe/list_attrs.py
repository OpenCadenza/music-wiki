import glob, io, re

def tempo_name(body):
    m = re.search(r'\\tempo\s+"([^"]+)"', body)
    if m:
        return m.group(1).strip()
    return ""

def bars_from(text):
    m = re.search(r"(\d+)\s*[–\-—~]\s*(\d+)", text)
    if m:
        return m.group(1), m.group(2)
    m = re.search(r"(\d+)", text)
    if m:
        return m.group(1), m.group(1)
    return None, None

def norm_title(t):
    t = re.sub(r"[（(][^）)]*[）)]\s*$", "", t).strip()
    t = re.sub(r"第\s*\d+\s*[–\-—~]\s*\d+\s*小节.*$", "", t).strip()
    t = re.sub(r"\s*mm\..*$", "", t).strip()
    return t

def norm_loc(attrs, body):
    m = re.search(r'location="([^"]*)"', attrs)
    loc = m.group(1) if m else ""
    a, b = bars_from(loc)
    if a is None:
        a, b = bars_from(re.search(r'title="([^"]*)"', attrs).group(1))
    rng = f"mm.{a}–{b}" if a and b else loc.strip()
    tn = tempo_name(body)
    return f"{tn}，{rng}" if tn else rng

out_rows = []
for p in [q for q in glob.glob("content/**/*.md", recursive=True) if not q.endswith("index.md")]:
    t = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        attrs, body = m.group(1), m.group(2)
        tm = re.search(r'title="([^"]*)"', attrs)
        title = tm.group(1) if tm else ""
        out_rows.append((p.split("content")[1][1:], title, norm_title(title), norm_loc(attrs, body)))
for r in out_rows:
    print(" | ".join(r))