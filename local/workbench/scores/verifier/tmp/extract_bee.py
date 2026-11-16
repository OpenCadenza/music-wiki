import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
root = Path("local/workbench/scores")
src = (root/"assistant-scores-a"/"beethoven-op74-mvt1-mm1-9-adagio.ly").read_text(encoding="utf-8").splitlines()
# 只取 global + 四个声部（第 17–81 行），不含 \score
bee = "\n".join(src[16:81])
out = '\\version "2.26.0"\n\\language "english"\n\n' + bee + "\n\n\\displayLilyMusic \\violinOne\n"
Path(root/"verifier"/"tmp"/"recheck_beethoven.ly").write_text(out, encoding="utf-8")
print("lines:", len(out.splitlines()))
print("tail:", "\n".join(out.splitlines()[-6:]))
