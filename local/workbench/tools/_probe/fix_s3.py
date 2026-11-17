import io

def patch(path, pairs):
    s = io.open(path, encoding="utf-8").read()
    for a, b in pairs:
        if a not in s:
            print("MISS:", path, "|", a[:60])
            continue
        s = s.replace(a, b, 1)
    io.open(path, "w", encoding="utf-8", newline="\n").write(s)
    print("patched", path)

patch(r"local\workbench\scores\score-s3\schubert-d328-mm72-76-mein-vater.ly", [
    ("<fs, fs>2 r4 fs'4 |", "<fs, fs>2 r4 fs4 |"),
    ("\\tempo \"Schnell\" 4 = 154", "\\tempo \"Schnell\" 4 = 152"),
])
patch(r"local\workbench\scores\score-s3\schubert-d328-mm1-5-prelude.ly", [
    ("\\tempo \"Schnell\" 4 = 154", "\\tempo \"Schnell\" 4 = 152"),
])