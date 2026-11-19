import io, re

mapping = {
    "content/composers/index.md": "作曲家",
    "content/composers/bach/index.md": "巴赫",
    "content/composers/bach/chorale/index.md": "众赞歌",
    "content/composers/beethoven/index.md": "贝多芬",
    "content/composers/beethoven/piano-sonatas/index.md": "钢琴奏鸣曲",
    "content/composers/beethoven/quartets/index.md": "弦乐四重奏",
    "content/ensembles/index.md": "室内乐",
    "content/notation/index.md": "记谱",
    "content/styles/index.md": "风格",
    "content/techniques/index.md": "技法",
    "content/techniques/counterpoint/index.md": "对位",
    "content/techniques/harmony/index.md": "和声",
    "content/techniques/material/index.md": "素材",
    "content/techniques/rhythm/index.md": "节奏",
    "content/techniques/sound/index.md": "配器",
    "content/techniques/structure/index.md": "结构",
}

for path, short in mapping.items():
    t = io.open(path, encoding="utf-8").read()
    new, n = re.subn(r"^#\s+.+$", "# " + short, t, count=1, flags=re.M)
    if n:
        io.open(path, "w", encoding="utf-8", newline="\n").write(new)
        print("改了", path, "->", short)
    else:
        print("未找到 H1:", path)
