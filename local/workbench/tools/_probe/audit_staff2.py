import glob, io, re

files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
bad = []
total = 0
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        body = m.group(2)
        # 只匹配真正的 \new Staff（后面是空白或 =，不是字母）
        for sm in re.finditer(r"\\new Staff(?=[\s=])", body):
            total += 1
            head = body[sm.start(): sm.start() + 260]
            if "midiInstrument" not in head and "\\set Staff.midiInstrument" not in head:
                bad.append((p, body[max(0, sm.start()-80): sm.start()+120].replace("\n", " / ")))
print("真正的 \\new Staff 数:", total, "｜缺乐器声明的:", len(bad))
for p, ctx in bad:
    print(" ", p, "|", ctx)

# 也查 StaffGroup 上是否还挂着 \with
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r"```lilypond[^\n]*\n(.*?)```", t, re.S):
        if re.search(r"\\new (StaffGroup|ChoirStaff)\s*\\with", m.group(1)):
            print("StaffGroup 上有 \\with:", p)