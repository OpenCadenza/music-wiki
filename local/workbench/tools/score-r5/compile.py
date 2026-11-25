import os
import re
import subprocess
import sys
import tempfile

LILYPOND = r"E:\GreenSoftware\lilypond-2.26.0\bin\lilypond.exe"


def main():
    for path in sys.argv[1:]:
        text = open(path, encoding="utf-8").read()
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        body = "\n".join(lines)
        if '\\version' not in body:
            body = '\\version "2.26.0"\n' + body
        d = tempfile.mkdtemp(prefix="lycheck-")
        target = os.path.join(d, "f.ly")
        open(target, "w", encoding="utf-8").write(body)
        p = subprocess.run([LILYPOND, "--pdf", "-dno-point-and-click", "-o",
                            os.path.join(d, "out"), target],
                           capture_output=True, text=True)
        ok = p.returncode == 0
        print(("OK   " if ok else "FAIL ") + path)
        if not ok:
            err = [l for l in (p.stderr or p.stdout).splitlines() if l.strip()][:12]
            for l in err:
                print("   ", l)


if __name__ == "__main__":
    main()
