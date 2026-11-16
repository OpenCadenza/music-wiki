import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8")
root = Path("local/workbench/scores")
# --- Mozart: 程序化抽取（避免手抄误差） ---
src = (root/"assistant-scores-a"/"mozart-k283-mvt1-mm1-10.ly").read_text(encoding="utf-8").splitlines()
moz = "\n".join(src[17:56])   # global + rightHand + leftHand
out = '\\version "2.26.0"\n\\language "english"\n\n' + moz + "\n\n\\displayLilyMusic \\rightHand\n\\displayLilyMusic \\leftHand\n"
Path(root/"verifier"/"tmp"/"recheck_mozart.ly").write_text(out, encoding="utf-8")
# --- Beethoven ---
src = (root/"assistant-scores-a"/"beethoven-op74-mvt1-mm1-9-adagio.ly").read_text(encoding="utf-8").splitlines()
bee = "\n".join(src[16:103])  # global + violinOne..cello
out = '\\version "2.26.0"\n\\language "english"\n\n' + bee + "\n\n\\displayLilyMusic \\violinOne\n"
Path(root/"verifier"/"tmp"/"recheck_beethoven.ly").write_text(out, encoding="utf-8")
# --- Haydn ---
src = (root/"assistant-scores-a"/"haydn-hob-xvi-27-mvt3-mm1-8.ly").read_text(encoding="utf-8").splitlines()
hay = "\n".join(src[16:51])
out = '\\version "2.26.0"\n\\language "english"\n\n' + hay + "\n\n\\displayLilyMusic \\rightHand\n\\displayLilyMusic \\leftHand\n"
Path(root/"verifier"/"tmp"/"recheck_haydn.ly").write_text(out, encoding="utf-8")
print("written")
for n in ("recheck_mozart.ly","recheck_beethoven.ly","recheck_haydn.ly"):
    p = root/"verifier"/"tmp"/n
    print(f"--- {n} ({len(p.read_text(encoding='utf-8').splitlines())} lines) head ---")
    print("\n".join(p.read_text(encoding="utf-8").splitlines()[:6]))
