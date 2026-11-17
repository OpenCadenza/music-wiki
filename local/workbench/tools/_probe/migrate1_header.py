import glob, io, re

def strip_header(body):
    """删除 \\header { ... } 块（含花括号配对，忽略字符串内的括号）。"""
    i = body.find("\\header")
    if i < 0:
        return body, False
    j = body.find("{", i)
    if j < 0:
        return body, False
    depth = 0
    k = j
    in_str = False
    while k < len(body):
        ch = body[k]
        if in_str:
            if ch == "\\":
                k += 1
            elif ch == '"':
                in_str = False
        else:
            if ch == '"':
                in_str = True
            elif ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    break
        k += 1
    if k >= len(body):
        return body, False
    # 扩展到整行
    start = body.rfind("\n", 0, i) + 1
    end = body.find("\n", k)
    if end < 0:
        end = len(body)
    new = body[:start] + body[end + 1:]
    # 去掉块后多余空行
    new = re.sub(r"\n{3,}", "\n\n", new)
    return new, True

ACC = {"ees": "ef", "ges": "gf", "des": "df", "fes": "ff", "aes": "af", "bes": "bf", "ces": "cf"}
acc_re = re.compile(r"(?<![A-Za-z])(" + "|".join(ACC) + r")(?![A-Za-z])")

def fix_accidentals(body):
    out = []
    changed = 0
    for line in body.split("\n"):
        if line.lstrip().startswith("%"):
            out.append(line)
            continue
        def rep(m):
            nonlocal changed
            changed += 1
            return ACC[m.group(1)]
        out.append(acc_re.sub(rep, line))
    return "\n".join(out), changed

def ragged(body):
    if "\\layout { }" in body:
        return body.replace("\\layout { }", "\\layout { ragged-right = ##f }"), True
    return body, False

files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]
n_hdr = n_acc = n_rag = 0
touched = []
for p in files:
    t = io.open(p, encoding="utf-8").read()
    out = []
    pos = 0
    changed_any = False
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        out.append(t[pos:m.start()])
        attrs, body = m.group(1), m.group(2)
        body2, h = strip_header(body)
        body2, a = fix_accidentals(body2)
        body2, r = ragged(body2)
        n_hdr += h; n_acc += a; n_rag += r
        changed_any = changed_any or h or a or r
        out.append("```lilypond" + attrs + "\n" + body2 + "```")
        pos = m.end()
    out.append(t[pos:])
    new = "".join(out)
    if changed_any:
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        touched.append(p)
print("去掉 \\header 的围栏:", n_hdr, "｜音名替换:", n_acc, "｜加 ragged-right:", n_rag, "｜改动文件:", len(touched))