"""从文章 markdown 中抽取两块 lilypond 围栏，原样落盘（不做任何改动）。"""
from pathlib import Path

md = Path("content/techniques/structure/hybrid-themes-and-syntax-decoupling.md")
lines = md.read_text(encoding="utf-8").splitlines()
out_dir = Path("local/workbench/scores/verifier/tmp2")
out_dir.mkdir(parents=True, exist_ok=True)

blocks = []
cur = None
for i, ln in enumerate(lines, 1):
    if cur is None and ln.startswith("```lilypond"):
        cur = {"start": i, "head": ln, "body": []}
    elif cur is not None:
        if ln.strip() == "```":
            cur["end"] = i
            blocks.append(cur)
            cur = None
        else:
            cur["body"].append(ln)

for n, b in enumerate(blocks, 1):
    name = f"fence{n}.ly"
    (out_dir / name).write_text("\n".join(b["body"]) + "\n", encoding="utf-8")
    print(f"{name}: md 行 {b['start']}-{b['end']}  标题 {b['head']}  正文 {len(b['body'])} 行")
