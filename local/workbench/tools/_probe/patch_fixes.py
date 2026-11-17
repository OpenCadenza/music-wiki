import io

def patch(path, pairs):
    s = io.open(path, encoding="utf-8").read()
    miss = []
    for a, b in pairs:
        if a not in s:
            miss.append(a)
            continue
        s = s.replace(a, b, 1)
    io.open(path, "w", encoding="utf-8", newline="\n").write(s)
    print(path, "| misses:", len(miss), miss[:3])

# 1) Op.135 III：4 处音高/临时记号 + 速度 + 注释
patch(r"local\workbench\scores\score-s1\beethoven-op135-mvt3-mm01-12.ly", [
    ("af'8", "af8"),
    ("a4.", "an4."),
    ("d4", "dn4"),
    ("d,4.", "dn,4."),
    ("8 = 50", "4 = 50"),
])

# 2) Haydn Op.76/3 II：6 处八度
patch(r"local\workbench\scores\score-s1\haydn-op76-3-mvt2-mm01-20-emperor.ly", [
    ("e8 fs8", "e'8 fs'8"),
    ("e8 d8", "e'8 d'8"),
    ("c,4.", "c4."),
    ("c,2", "c2"),
])

# 3) Brahms Op.90 III：m.4 后半起降八度
patch(r"local\workbench\scores\score-s2\S2-E2-brahms-op90-3-m1-8.ly", [
    ("ef'32", "ef32"),
    ("f'4 af16.(g32)", "f4 af16.(g32)"),
])