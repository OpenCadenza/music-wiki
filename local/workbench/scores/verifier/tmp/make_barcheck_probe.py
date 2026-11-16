import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
root = Path("local/workbench/scores")
src = (root/"assistant-scores-a"/"mozart-k283-mvt1-mm1-10.ly").read_text(encoding="utf-8")
# 副本：只在左手末小节加一个 barcheck，用来检验 m.10 是否真的是 3 拍（不动原文件）
assert "<g b>4 g,4 r4 \\bar \"||\"" in src
patched = src.replace("<g b>4 g,4 r4 \\bar \"||\"", "<g b>4 g,4 r4 | \\bar \"||\"")
Path(root/"verifier"/"tmp"/"mozart_barcheck_probe.ly").write_text(patched, encoding="utf-8")
print("patched ok")
