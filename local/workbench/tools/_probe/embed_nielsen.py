import io, re

ly = r"local\workbench\scores\score-s8\nielsen-op43-mvt1-mm1-12.ly"
art = r"content\ensembles\wind-quintet-acoustic-balance.md"

def code_of(path):
    s = io.open(path, encoding="utf-8").read().split("\n")
    start = next(i for i, l in enumerate(s) if l.startswith("\\version"))
    body = [l for l in s[start:] if not l.lstrip().startswith("%")]
    body = "\n".join(body)
    # 新乐器契约：去掉 instrumentName 与空 \with，保留 \set Staff.midiInstrument
    body = re.sub(r"\n?[ \t]*instrumentName\s*=\s*\"[^\"]*\"[ \t]*", "", body)
    body = re.sub(r"\\with\s*\{\s*\}", "", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.rstrip("\n")

s = io.open(art, encoding="utf-8").read()
lines = s.split("\n")
out, i = [], 0
done = False
while i < len(lines):
    ln = lines[i]
    if (not done) and ("谱例待补：卡尔·尼尔森" in ln):
        # 若上一行是空行，删掉它；若上上行为加粗标题，一并删除
        if out and not out[-1].strip():
            out.pop()
        if out and out[-1].startswith("**卡尔·尼尔森"):
            out.pop()
            if out and not out[-1].strip():
                out.pop()
        out += ['```lilypond title="卡尔·尼尔森 管乐五重奏 Op.43 第一乐章" location="Allegro ben moderato，mm.1–11（含 1 拍弱起）"',
                code_of(ly), "```"]
        done = True
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        out.append("")
        continue
    out.append(ln)
    i += 1
s2 = "\n".join(out)
s2 = re.sub(r"\n{3,}", "\n\n", s2)
io.open(art, "w", encoding="utf-8", newline="\n").write(s2)
print("已替换:", done, "｜围栏数:", s2.count("```lilypond"))