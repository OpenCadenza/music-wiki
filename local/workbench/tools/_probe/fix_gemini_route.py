import io, shutil, datetime, json, os

# 1) profile patch: 增加旧 id 别名（settings.yaml 由它生成）
patch = r"C:\Users\ThinkBook\.dsh\profiles\desktop\cordis.patch.yml"
bak = patch + ".bak-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
shutil.copy2(patch, bak)
print("备份 patch:", bak)

text = io.open(patch, encoding="utf-8").read()
if "id: auto/gemini-3.8-flash" in text:
    print("patch 里已有别名")
else:
    anchor = """          - id: group/gemini-3.8-flash
            name: Gemini 3.8 Flash · routing group
            contextWindow: 1048576
            maxTokens: 65536
            input: [text, image]
            reasoningEfforts:
              low: low
              medium: medium
              high: high
"""
    if anchor not in text:
        # 缩进可能不同，退回按行插在 group/gemini 块之后
        lines = text.split("\n")
        idx = next((i for i, l in enumerate(lines) if "id: group/gemini-3.8-flash" in l), -1)
        if idx < 0:
            raise SystemExit("找不到 group/gemini-3.8-flash")
        indent = lines[idx][: len(lines[idx]) - len(lines[idx].lstrip())]
        alias = [
            indent + "- id: auto/gemini-3.8-flash",
            indent + "  name: Gemini 3.8 Flash · routing group (legacy id)",
            indent + "  contextWindow: 1048576",
            indent + "  maxTokens: 65536",
            indent + "  input: [text, image]",
            indent + "  reasoningEfforts:",
            indent + "    low: low",
            indent + "    medium: medium",
            indent + "    high: high",
        ]
        # 插到 group/gemini 整块之后（直到下一个同级 id 或缩进更浅）
        end = idx + 1
        while end < len(lines):
            l = lines[end]
            if l.strip().startswith("- id:") and len(l) - len(l.lstrip()) == len(indent):
                break
            if l.strip() and (len(l) - len(l.lstrip())) < len(indent):
                break
            end += 1
        lines[end:end] = alias
        text = "\n".join(lines)
        io.open(patch, "w", encoding="utf-8", newline="\n").write(text)
        print("已插入别名（按行）")
    else:
        alias = anchor.replace("group/gemini-3.8-flash", "auto/gemini-3.8-flash").replace(
            "Gemini 3.8 Flash · routing group", "Gemini 3.8 Flash · routing group (legacy id)"
        )
        text = text.replace(anchor, anchor + alias, 1)
        io.open(patch, "w", encoding="utf-8", newline="\n").write(text)
        print("已插入别名（块匹配）")

# 2) 当前会话策略：旧 id → 新 id（双保险）
sess = r"C:\Users\ThinkBook\.dsh\storages\session_projcache\sessions\session-f50514cb-9aca-41c4-a002-6b52d2c7cdfe.json"
if os.path.exists(sess):
    shutil.copy2(sess, sess + ".bak")
    data = json.load(io.open(sess, encoding="utf-8"))
    changed = 0

    def fix(obj):
        global changed
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == "model" and v == "auto/gemini-3.8-flash":
                    obj[k] = "group/gemini-3.8-flash"
                    changed += 1
                else:
                    fix(v)
        elif isinstance(obj, list):
            for v in obj:
                fix(v)

    fix(data)
    if changed:
        json.dump(data, io.open(sess, "w", encoding="utf-8", newline="\n"), ensure_ascii=False)
    print("会话内替换旧 id:", changed)
