import glob, io, json, os, datetime
import zstandard as zstd

OUT = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\docs\研究归档\_运行记录"
os.makedirs(OUT, exist_ok=True)

SESSIONS = {
    "scholar-1": ("7c908aa4-f1cf-4c35-9309-e2a0e96a8921", "音乐学者1"),
    "scholar-2": ("1b898ee7-6dd7-448a-9a93-97db86e16637", "音乐学者2"),
    "scholar-3": ("8e44d836-1f42-45fc-a847-c9b72e6453df", "音乐学者3"),
    "scholar-a": ("0cd7dfd4-133e-48c0-ad9d-c5c2a2f5ebc4", "学者A：教材与理论起步"),
    "scholar-b": ("aacbe5d0-929b-47b0-ab02-f63ab36b05b4", "学者B：谱源与标注起步"),
    "scholar-c": ("1e50ba2f-ead4-4d88-a1b0-bb24b397d49f", "学者C：论文与背景起步"),
    "scholar-a2": ("418993d0-5f8a-4a9f-a9e1-e690ba4f2f7c", "学者A2：续写结构篇"),
    "scholar-b2": ("5f7e404c-ec30-4689-bb24-7d27946da050", "学者B2：续写和声篇"),
    "scholar-c2": ("d24d169b-881e-48eb-aded-e6ca72cccb03", "学者C2：续写配器篇"),
}

TOOL_ARG = 240
TOOL_RESULT = 360
REASONING = 240
TEXT = 12000


def find_log(child_id):
    for r in glob.glob(r"C:\Users\ThinkBook\.dsh\sessions\*"):
        p = os.path.join(r, child_id, "session.v4.jsonl.zstd")
        if os.path.exists(p):
            return p
    return None


def read_events(path):
    with io.open(path, "rb") as fh:
        data = zstd.ZstdDecompressor().stream_reader(fh, read_across_frames=True).read()
    return [json.loads(l) for l in data.decode("utf-8", "ignore").split("\n") if l.strip()]


def text_of(message):
    out = []
    for block in message.get("content", []):
        if block.get("type") == "text":
            out.append(block.get("text", ""))
        elif block.get("type") == "reasoning":
            r = block.get("text", "").replace("\n", " ")
            out.append(f"[思考摘要] {r[:REASONING]}…")
    return "\n\n".join(x for x in out if x)


made = []
for name, (cid, label) in SESSIONS.items():
    path = find_log(cid)
    if not path:
        print("缺日志:", name, cid)
        continue
    events = read_events(path)
    events.sort(key=lambda e: e.get("seq", 0))
    head = next((e for e in events if e.get("type") == "session"), {})
    desc = next((e for e in events if e.get("type") == "subagent/descriptor"), {})
    model = desc.get("data", {}).get("agentModel", "")
    lines = [
        f"# 运行记录：{name}",
        "",
        f"- 标签：{label}",
        f"- 会话：`{cid}`",
        f"- 模型：`{model}`",
        f"- 创建：{datetime.datetime.fromtimestamp(head.get('createdAt', 0)/1000).strftime('%Y-%m-%d %H:%M')}",
        f"- 父会话：`{head.get('parentSession', '')}`",
        "",
        "> 本文件由 DSH 会话日志导出；工具结果与思考过程做了截断，助手/用户正文保留。",
        "",
    ]
    turn = None
    seen_user = set()
    for e in events:
        t = e.get("type")
        d = e.get("data", {})
        if t == "turn/start":
            turn = d.get("turn")
            lines += ["", f"## Turn {turn}", ""]
        elif t == "user/message":
            src = d.get("source", {}).get("kind", "")
            if src in ("working-directory", "system"):
                continue
            txt = (text_of(d) or "").strip()
            if txt and txt not in seen_user:
                seen_user.add(txt)
                lines += ["### 用户/主控", "", txt[:TEXT], ""]
        elif t == "agent/inbox/spliced":
            continue
        elif t == "assistant/message":
            txt = text_of(d.get("message", {}))
            if txt.strip():
                lines += ["### 助手", "", txt[:TEXT], ""]
        elif t == "tool/call":
            args = d.get("arguments", "")
            lines += [f"- 工具 `{d.get('name')}`：`{args[:TOOL_ARG]}`"]
        elif t == "tool/result":
            msg = d.get("message", {})
            txt = text_of(msg)
            if txt.strip():
                one = txt.replace("\n", " ")[:TOOL_RESULT]
                lines += [f"  - 结果：{one}…"]
    out = os.path.join(OUT, f"{name}.md")
    io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(lines) + "\n")
    made.append((name, os.path.getsize(out), len(events)))
    print(name, os.path.getsize(out), "bytes,", len(events), "events")

print("完成", len(made))
