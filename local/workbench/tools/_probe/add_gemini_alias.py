import io, shutil, os, datetime

path = r"C:\Users\ThinkBook\.dsh\settings.yaml"
bak = path + ".bak-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
shutil.copy2(path, bak)
print("备份:", bak)

text = io.open(path, encoding="utf-8").read()
alias = """        - id: auto/gemini-3.8-flash
          name: Gemini 3.8 Flash · routing group (legacy id)
          contextWindow: 1048576
          maxTokens: 65536
          input: [text, image]
          reasoningEfforts:
            low: low
            medium: medium
            high: high
"""
if "id: auto/gemini-3.8-flash" in text:
    print("别名已存在，跳过")
else:
    anchor = """        - id: group/gemini-3.8-flash
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
        raise SystemExit("找不到 group/gemini 块，未修改")
    text = text.replace(anchor, anchor + alias, 1)
    io.open(path, "w", encoding="utf-8", newline="\n").write(text)
    print("已插入别名条目")
