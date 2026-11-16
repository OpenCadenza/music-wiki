"""把已核验的谱例回填进 scholar-a 的正文（主控整合步骤）。

- 三处「谱例占位」引用块替换为正式 lilypond 围栏（title/location 属性）
- 去掉正文中已失效的「（待谱例复核：…）」标注
- 谱例代码剥掉生产注释（% 开头行），正文不保留生产元信息
"""

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

root = Path(__file__).resolve().parents[3]
article = root / "content/techniques/structure/galant-schemata-and-formal-functions.md"
scores = root / "local/workbench/scores/assistant-scores-a"

SPECS = [
    {
        "file": scores / "haydn-hob-xvi-27-mvt3-mm1-8.ly",
        "title": "海顿 Hob. XVI:27 第三乐章 Presto",
        "location": "mm.1–8",
        "marker": "约瑟夫·海顿《G大调第42钢琴奏鸣曲》Hob. XVI:27",
    },
    {
        "file": scores / "mozart-k283-mvt1-mm1-10.ly",
        "title": "莫扎特 K. 283 第一乐章 Allegro",
        "location": "mm.1–10",
        "marker": "沃尔夫冈·阿马德乌斯·莫扎特《G大调第5钢琴奏鸣曲》K. 283",
    },
    {
        "file": scores / "beethoven-op74-mvt1-mm1-9-adagio.ly",
        "title": "贝多芬 Op.74《竖琴》第一乐章 Poco adagio",
        "location": "mm.1–9",
        "marker": "路德维希·凡·贝多芬《降E大调第10弦乐四重奏“竖琴”》Op. 74",
    },
]


def code_of(path):
    lines = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("%"):
            continue
        lines.append(line)
    text = "\n".join(lines).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main():
    source = article.read_text(encoding="utf-8")
    for spec in SPECS:
        code = code_of(spec["file"])
        fence = f'```lilypond title="{spec["title"]}" location="{spec["location"]}"\n{code}\n```'
        # 定位该占位块：从含「谱例占位」的引用块起，到含「重编码中」的行为止
        pattern = re.compile(
            r"> \*\*【谱例占位[^\n]*\n(?:>[^\n]*\n)*?> [^\n]*重编码中[^\n]*\n",
            re.MULTILINE,
        )
        blocks = list(pattern.finditer(source))
        target = None
        for block in blocks:
            if spec["marker"] in block.group(0):
                target = block
                break
        if target is None:
            print(f"!! 未找到占位块：{spec['marker']}")
            continue
        source = source[: target.start()] + fence + "\n" + source[target.end():]
        print(f"已回填：{spec['title']}（{spec['location']}）")

    removed = len(re.findall(r"（待谱例复核：[^）]*）", source))
    source = re.sub(r"（待谱例复核：[^）]*）", "", source)
    print(f"去掉失效标注「（待谱例复核：…）」{removed} 处")

    article.write_text(source, encoding="utf-8")
    print(f"写入 {article.relative_to(root)}")


if __name__ == "__main__":
    main()
