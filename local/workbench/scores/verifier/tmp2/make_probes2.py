"""用 \displayLilyMusic 取两块围栏每个声部的规范形式（绝对音高、显式时值）。"""
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
LILY = r"E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe"

JOBS = [
    ("fence1.ly", "mozart", ["rightHand", "leftHand"]),
    ("fence2.ly", "beethoven", ["violinOne", "violinTwo", "viola", "cello"]),
]

for fname, tag, names in JOBS:
    src = (HERE / fname).read_text(encoding="utf-8")
    head = src.split("\\score {")[0]
    calls = "\n".join(f"\\displayLilyMusic \\{n}" for n in names)
    probe = HERE / f"probe_{tag}.ly"
    probe.write_text(head + "\n" + calls + "\n", encoding="utf-8")
    out = subprocess.run([LILY, "-dno-print-pages", probe.name], cwd=HERE,
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    txt = (out.stdout or "") + "\n-----STDERR-----\n" + (out.stderr or "")
    (HERE / f"display_{tag}.txt").write_text(txt, encoding="utf-8")
    print(f"=== {tag}: exit={out.returncode} 长度={len(txt)}")
    for n in names:
        print(f"  {n}: {'出现' if n in txt else '未出现'}")
