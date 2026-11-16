import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
p = Path(r"local/workbench/scores/verifier/核验报告-修正版.md")
t = p.read_text(encoding="utf-8")
fixes = [
 ("| 依据 | 该音（m.9 第 12 个十六分中的第 9 个，onset = 3 个四分拍） | 性质 |",
  "| 依据 | 该音（m.9 十二个十六分中的第 9 个，onset = 3 个四分拍） | 性质 |"),
 ("├── bl_one.ly / bl_two.svg / bl_one.svg                            # | 与 | | 排版等价性验证",
  "├── bl_one.ly / bl_two.ly / bl_one.svg / bl_two.svg               # `\\|` 与 `\\| \\|` 排版等价性验证"),
]
for old, new in fixes:
    assert old in t, old[:40]
    t = t.replace(old, new)
p.write_text(t, encoding="utf-8")
print("ok, 行数:", len(t.splitlines()))
