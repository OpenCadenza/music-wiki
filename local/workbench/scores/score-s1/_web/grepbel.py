import io
import re

path = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s1\_web\hfm_bel.txt"
with io.open(path, "r", encoding="utf-8", errors="replace") as f:
    text = f.read()

# split the table into cell rows by newline; print lines mentioning Trio or Op.97
for line in text.split("\n"):
    if ("Trio" in line) or re.search(r"Op\.?\s*97", line):
        print(line[:400])
        print("---")
