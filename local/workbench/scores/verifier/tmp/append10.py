import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
p = Path(r"local/workbench/scores/verifier/tmp/section10.md")
t = p.read_text(encoding="utf-8")
old = "✅（改 `<c' g'>`→`<c g'>` 必要且正确：新基准下 `c'` 会变成 C5）"
new = "✅（改 `<c' g'>`→`<c g'>` **必要且正确**：实测新基准下 `<c' g'>` 会解析为 **C5+G5**，比原谱高两个八度；`<c g'>` 才是 C4+G4）"
assert old in t
t = t.replace(old, new)
old2 = "✅（此处在旧基准下本就对，改用 `<b g'>` 后仍对，属幸运巧合，已复核）"
new2 = "✅（此写法在新基准下正确；注意若沿用旧式的 `<b' g'>` 会解析为 B4+G5，本轮未动它是对的）"
assert old2 in t
t = t.replace(old2, new2)
p.write_text(t, encoding="utf-8")
print("section10 修订完成")

rep = Path(r"local/workbench/scores/verifier/核验报告-修正版.md")
body = rep.read_text(encoding="utf-8")
if "## §10 改动复审" in body:
    print("报告已含 §10，跳过")
else:
    body = body.rstrip("\n") + "\n" + t
    rep.write_text(body, encoding="utf-8")
    print("已追加 §10，总行数:", len(body.splitlines()))
