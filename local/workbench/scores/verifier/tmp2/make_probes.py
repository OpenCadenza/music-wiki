"""把两块围栏里的音乐变量分别抽出，生成 \displayLilyMusic 探针，取绝对音高/时值。"""
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
LILY = r"E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe"

TARGETS = [
    ("fence1.ly", "mozart", ["rightHand", "leftHand"]),
    ("fence2.ly", "beethoven", ["violinOne", "violinTwo", "viola", "cello"]),
]


def extract_var(src: str, name: str) -> str:
    m = re.search(rf"^{name} = \{{(.*?)^\}}\s*$", src, re.S | re.M)
    if not m:
        raise SystemExit(f"变量 {name} 未找到")
    return m.group(1)


def extract_global(src: str) -> str:
    return extract_var(src, "global")


for fname, tag, names in TARGETS:
    src = (HERE / fname).read_text(encoding="utf-8")
    glob = extract_global(src)
    (HERE / f"{tag}_global.ily").write_text(
        "\\version \"2.26.0\"\n\\language \"english\"\nglobal = {" + glob + "}\n",
        encoding="utf-8",
    )
    for n in names:
        body = extract_var(src, n)
        # 替换 \global 为内联展开，避免探针里引用 variable
        body = body.replace("\\global", "{ \\key g \\major }" if tag == "beethoven" else "{ \\key f \\major }")
        ily = HERE / f"{tag}_{n}.ily"
        ily.write_text(body, encoding="utf-8")
        probe = HERE / f"probe_{tag}_{n}.ly"
        probe.write_text(
            "\n".join([
                "\\version \"2.26.0\"",
                "\\language \"english\"",
                f"\\include \"{tag}_{n}.ily\"",
                "",
                f"\\displayLilyMusic \\{n}",
                "",
            ]),
            encoding="utf-8",
        )
        out = subprocess.run([LILY, "-dno-print-pages", probe.name], cwd=HERE,
                             capture_output=True, text=True, encoding="utf-8", errors="replace")
        txt = (out.stdout or "") + "\n" + (out.stderr or "")
        (HERE / f"display_{tag}_{n}.txt").write_text(txt, encoding="utf-8")
        print(f"=== {tag}/{n} ===")
        print(txt[:3000])
