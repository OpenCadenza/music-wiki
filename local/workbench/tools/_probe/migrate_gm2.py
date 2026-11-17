import glob, io, re

files = [p for p in glob.glob("content/**/*.md", recursive=True) if not p.endswith("index.md")]

def clean_with_blocks(body):
    # 1) 删除 instrumentName 行
    body = re.sub(r"\n?[ \t]*instrumentName\s*=\s*\"[^\"]*\"[ \t]*", "", body)
    # 2) 删除 % GM 注释
    body = re.sub(r"[ \t]*%\s*GM\s*\d+[^\n]*\n", "", body)
    # 3) 清理空的 \with { }
    body = re.sub(r"\\with\s*\{\s*\}", "", body)
    return body

midi_in_with = re.compile(r"\\with\s*\{([^{}]*)\}", re.S)

def move_pianostaff_midi(body):
    # PianoStaff 上的 midiInstrument 下移到子 staff
    out = []
    pos = 0
    changed = False
    for m in re.finditer(r"\\new PianoStaff\s*\\with\s*\{([^{}]*)\}", body):
        inner = m.group(1)
        mm = re.search(r'midiInstrument\s*=\s*"([^"]+)"', inner)
        if not mm:
            continue
        inst = mm.group(1)
        # 找到该 PianoStaff 的音乐块范围（其后第一个 << ... >> 或 { ... }）
        after = body[m.end():]
        start = None
        depth = 0
        for i, ch in enumerate(after):
            if ch == "<" and after[i:i+2] == "<<":
                start = i
                break
            if ch == "{":
                start = i
                break
        if start is None:
            continue
        # 截取 << >> 配对
        k = start
        if after[k:k+2] == "<<":
            depth = 0
            j = k
            while j < len(after):
                if after[j:j+2] == "<<":
                    depth += 1
                    j += 2
                    continue
                if after[j:j+2] == ">>":
                    depth -= 1
                    j += 2
                    if depth == 0:
                        break
                    continue
                j += 1
            span = after[k:j]
        else:
            depth = 0
            j = k
            while j < len(after):
                if after[j] == "{":
                    depth += 1
                elif after[j] == "}":
                    depth -= 1
                    if depth == 0:
                        j += 1
                        break
                j += 1
            span = after[k:j]
        # 在 span 内给缺乐器的 \new Staff 加 \with
        def add_with(sm):
            head = sm.group(0)
            return head + ' \\with { midiInstrument = "' + inst + '" }'
        newspan = re.sub(r"\\new Staff(?: = \"[^\"]*\")?(?!\s*\\with)", add_with, span)
        body = body[:m.end()] + after[:k] + newspan + after[k+len(span):]
        # 移除 PianoStaff 自身 \with
        body = body[:m.start()] + "\\new PianoStaff" + body[m.end():]
        changed = True
        pos = 0
    return body, changed

total = 0
for p in files:
    t = io.open(p, encoding="utf-8").read()
    out, pos = [], 0
    for m in re.finditer(r"```lilypond([^\n]*)\n(.*?)```", t, re.S):
        out.append(t[pos:m.start()])
        attrs, body = m.group(1), m.group(2)
        body = clean_with_blocks(body)
        body, _ = move_pianostaff_midi(body)
        out.append("```lilypond" + attrs + "\n" + body + "```")
        pos = m.end()
    out.append(t[pos:])
    new = "".join(out)
    if new != t:
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        total += 1
print("处理文件:", total)