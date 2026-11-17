import io, os, re, subprocess, glob

root = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb"
os.chdir(root)

def stats(paths):
    n_files = len(paths)
    fences = 0
    with_header = 0
    with_setmidi = 0
    with_gm = 0
    with_tempo = 0
    with_id = 0
    ees = 0
    frontmatter = 0
    refs = 0
    bold_caption = 0
    for p in paths:
        t = io.open(p, encoding="utf-8").read()
        if t.startswith("---"):
            frontmatter += 1
        if re.search(r"参考文献|资料索引", t):
            refs += 1
        blocks = re.findall(r"```lilypond([^\n]*)\n(.*?)```", t, re.S)
        for attrs, body in blocks:
            fences += 1
            if "\\header" in body:
                with_header += 1
            if "\\set Staff.midiInstrument" in body:
                with_setmidi += 1
            if re.search(r"%\s*GM\s*\d+", body):
                with_gm += 1
            if "\\tempo" in body:
                with_tempo += 1
            if 'id="' in attrs:
                with_id += 1
            if re.search(r"\b(ees|bes|ges|des|aes|ces)\b", body):
                ees += 1
        # 加粗标题行紧跟围栏的旧写法
        if re.search(r"\*\*[^\n]{4,40}\*\*\s*\n+\s*```lilypond", t):
            bold_caption += 1
    return dict(files=n_files, fences=fences, header=with_header, setmidi=with_setmidi,
                gm=with_gm, tempo=with_tempo, id=with_id, ees=ees,
                frontmatter=frontmatter, refs=refs, bold_caption=bold_caption)

ours = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
print("本分支:", stats(ours))

# main 分支：导出到临时目录后统计
tmp = os.path.join(root, "local", "_mainsample", "maincontent")
os.makedirs(tmp, exist_ok=True)
files = subprocess.run(["git", "ls-tree", "-r", "--name-only", "main", "content"],
                       capture_output=True, text=True, encoding="utf-8").stdout.split()
paths = []
for f in files:
    if not f.endswith(".md") or f.endswith("index.md"):
        continue
    out = os.path.join(tmp, f.replace("/", "__"))
    with open(out, "wb") as fh:
        data = subprocess.run(["git", "show", "main:" + f], capture_output=True).stdout
        fh.write(data)
    paths.append(out)
print("main:", stats(paths))