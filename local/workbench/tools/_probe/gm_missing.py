import glob, io, os, re

os.chdir(r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb")
files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]

total_staff = 0
missing = []
for p in files:
    t = io.open(p, encoding="utf-8").read()
    fence_i = 0
    for attrs, body in re.findall(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        fence_i += 1
        # 每个 \new Staff / \new PianoStaff 下的 Staff 段
        staffs = re.findall(r"\\new Staff[^\n{]*\{", body)
        # 粗略：统计 Staff 数量与其中声明的 midiInstrument
        n_staff = len(staffs)
        n_midi = len(re.findall(r"midiInstrument\s*=", body))
        n_set = len(re.findall(r"\\set\s+Staff\.midiInstrument", body))
        total_staff += n_staff
        has_global_instrument = "midiInstrument" in body
        if n_staff > 0 and not has_global_instrument:
            title = re.search(r'title="([^"]*)"', attrs)
            missing.append((os.path.basename(p), title.group(1) if title else "?", n_staff))

print("围栏内 \\new Staff 总数（近似）:", total_staff)
print("没有任何 midiInstrument 声明的围栏:", len(missing))
for m in missing:
    print("   ", m[0], "|", m[1], "| staff数:", m[2])