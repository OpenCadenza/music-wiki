import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
p = Path(r"local/workbench/scores/verifier/核验报告-修正版.md")
text = p.read_text(encoding="utf-8")
print("当前行数:", len(text.splitlines()))
print("末尾:", repr(text[-160:]))
