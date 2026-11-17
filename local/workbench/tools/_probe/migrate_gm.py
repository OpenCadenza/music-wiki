import glob, io, re

pats = [
    # 多行：instrumentName + midiInstrument
    re.compile(r"\\new Staff \\with \{\s*instrumentName = \"[^\"]*\"\s*midiInstrument = \"([^\"]+)\"\s*\}\s*\{"),
    # 单行/紧凑
    re.compile(r"\\new Staff \\with \{ instrumentName = \"[^\"]*\" midiInstrument = \"([^\"]+)\" \}\s*\{"),
    # 只有 midiInstrument
    re.compile(r"\\new Staff \\with \{\s*midiInstrument = \"([^\"]+)\"\s*\}\s*\{"),
    re.compile(r"\\new Staff \\with \{ midiInstrument = \"([^\"]+)\" \}\s*\{"),
]

changed = 0
files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
for p in files:
    t = io.open(p, encoding="utf-8").read()
    out, pos = [], 0
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        out.append(t[pos:m.start()])
        attrs, body = m.group(1), m.group(2)
        for pat in pats:
            def rep(mm):
                global changed
                changed += 1
                return '\\new Staff { \\set Staff.midiInstrument = "' + mm.group(1) + '"'
            body = pat.sub(rep, body)
        out.append("```lilypond" + attrs + "\n" + body + "```")
        pos = m.end()
    out.append(t[pos:])
    new = "".join(out)
    if new != t:
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)

print("转换 staff 声明:", changed)

# 剩余检查
left = 0
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for attrs, body in re.findall(r"```lilypond[^\n]*\n(.*?)```", t, re.S):
        left += len(re.findall(r"instrumentName", body))
        left += len(re.findall(r"%\s*GM\s*\d+", body))
print("残留 instrumentName/ GM 注释:", left)

# 统计没有 midiInstrument 的 staff
missing = []
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for attrs, body in re.findall(r"```lilypond[^\n]*\n(.*?)```", t, re.S):
        n_staff = len(re.findall(r"\\new Staff", body))
        n_midi = len(re.findall(r"\\set Staff\.midiInstrument", body)) + len(re.findall(r"midiInstrument =", body))
        if n_staff != n_midi:
            missing.append((p, n_staff, n_midi))
for x in missing:
    print("staff 数与乐器声明不匹配:", x)