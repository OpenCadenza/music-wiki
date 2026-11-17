import glob, io, os, re, subprocess, tempfile, struct

root = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb"
os.chdir(root)
LILY = r"E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe"

files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
pairs = []          # (file, instrumentName, midiInstrument)
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for attrs, body in re.findall(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        # 单个 Staff 内的 with 块
        for m in re.finditer(r"\\new Staff[^\n{]*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", body, re.S):
            seg = m.group(0)
            nm = re.search(r'instrumentName\s*=\s*"([^"]*)"', seg)
            mi = re.search(r'midiInstrument\s*=\s*"([^"]*)"', seg)
            if nm or mi:
                pairs.append((p, nm.group(1) if nm else None, mi.group(1) if mi else None))

print("带乐器声明的 Staff 数:", len(pairs))

names = sorted({(mi or "") for _, _, mi in pairs if mi})
print("distinct midiInstrument:", names)

def test_name(name):
    d = tempfile.mkdtemp()
    ly = os.path.join(d, "t.ly")
    io.open(ly, "w", encoding="utf-8").write(
        '\\version "2.26.0"\n\\language "english"\n'
        '\\score { \\new Staff \\with { midiInstrument = "%s" } { c\'4 } \\midi {} }\n' % name)
    r = subprocess.run([LILY, "--pdf", "-o", os.path.join(d, "t"), ly],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    warn = len(re.findall(r"warning", r.stdout + r.stderr))
    mid = os.path.join(d, "t.mid")
    prog = None
    if os.path.exists(mid):
        b = open(mid, "rb").read()
        for i in range(len(b) - 1):
            if (b[i] & 0xF0) == 0xC0:
                prog = b[i + 1]
                break
    return warn, prog

print("\n名字合法性实测（program 应为 GM 号；warning>0 或 program=0 需警惕）：")
for n in names:
    w, p = test_name(n)
    print(f"  {n:20s} warnings={w} program={p}")

print("\n名称与标注 GM 的对照：")
for f, nm, mi in pairs:
    label = re.search(r"GM\s*(\d+)", nm or "")
    print(f"  {os.path.basename(f):45s} instrumentName={nm!r:32s} midiInstrument={mi!r} labelGM={label.group(1) if label else '-'}")