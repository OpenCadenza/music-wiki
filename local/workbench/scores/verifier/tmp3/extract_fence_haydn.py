"""从 md 抽取 title 含「海顿 Op. 64 No. 4」的 lilypond 围栏，原样落盘。"""
from pathlib import Path

md = Path("content/techniques/structure/hybrid-themes-and-syntax-decoupling.md")
lines = md.read_text(encoding="utf-8").splitlines()
out = Path("local/workbench/scores/verifier/tmp3")
out.mkdir(parents=True, exist_ok=True)

captured = None
start = end = None
for i, ln in enumerate(lines, 1):
    if ln.startswith("```lilypond"):
        if "海顿 Op. 64 No. 4" in ln:
            captured = []
            start = i
            continue
    elif captured is not None:
        if ln.strip() == "```":
            end = i
            break
        captured.append(ln)

if captured is None:
    raise SystemExit("未找到目标围栏")
(out / "fence_haydn.ly").write_text("\n".join(captured) + "\n", encoding="utf-8")
print(f"md 行 {start}-{end}，正文 {len(captured)} 行 -> tmp3/fence_haydn.ly")