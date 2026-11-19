import glob, io, json, os, collections, zstandard as zstd

target = "418993d0-5f8a-4a9f-a9e1-e690ba4f2f7c"
path = None
for r in glob.glob(r"C:\Users\ThinkBook\.dsh\sessions\*"):
    p = os.path.join(r, target, "session.v4.jsonl.zstd")
    if os.path.exists(p):
        path = p
        break
with io.open(path, "rb") as fh:
    text = zstd.ZstdDecompressor().stream_reader(fh, read_across_frames=True).read().decode("utf-8", "ignore")
events = [json.loads(l) for l in text.split("\n") if l.strip()]
counts = collections.Counter(e.get("type") for e in events)
print(counts.most_common())

for typ in ["message", "assistant/message", "user/message", "tool/call", "tool/result", "turn/start", "step/start"]:
    sample = next((e for e in events if e.get("type") == typ), None)
    if sample:
        print("\n---", typ)
        print(json.dumps(sample, ensure_ascii=False)[:500])
