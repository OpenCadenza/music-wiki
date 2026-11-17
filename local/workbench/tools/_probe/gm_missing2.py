import glob, io, os, re

os.chdir(r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb")
files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]

no_midi = []
total = 0
for p in files:
    t = io.open(p, encoding="utf-8").read()
    for attrs, body in re.findall(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        title = re.search(r'title="([^"]*)"', attrs)
        for m in re.finditer(r"\\new Staff[^\n{]*\{", body):
            seg_start = m.start()
            seg = body[seg_start:seg_start+400]
            total += 1
            if "midiInstrument" not in seg:
                no_midi.append((os.path.basename(p), title.group(1) if title else "?", seg.splitlines()[0][:60]))

print("Staff 声明总数:", total)
print("所在 Staff 段内没有 midiInstrument（会默认钢琴）:", len(no_midi))
for x in no_midi:
    print("   ", x[0], "|", x[1], "|", x[2])