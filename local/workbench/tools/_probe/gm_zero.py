import glob, io, os, re

os.chdir(r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb")
files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
zero = []
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for attrs, body in re.findall(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        if "midiInstrument" not in body:
            title = re.search(r'title="([^"]*)"', attrs)
            zero.append((os.path.basename(p), title.group(1) if title else "?"))
print("完全没有任何 midiInstrument 的围栏:", len(zero))
for z in zero:
    print("   ", z[0], "|", z[1])