import glob, io, json, os, zstandard as zstd

target = "418993d0-5f8a-4a9f-a9e1-e690ba4f2f7c"
path = None
for r in glob.glob(r"C:\Users\ThinkBook\.dsh\sessions\*"):
    p = os.path.join(r, target, "session.v4.jsonl.zstd")
    if os.path.exists(p):
        path = p
        break
print("file:", path)
with io.open(path, "rb") as fh:
    reader = zstd.ZstdDecompressor().stream_reader(fh, read_across_frames=True)
    data = reader.read()
text = data.decode("utf-8", "ignore")
lines = [l for l in text.split("\n") if l.strip()]
print("events:", len(lines), "chars:", len(text))
for line in lines[:4]:
    obj = json.loads(line)
    print("type:", obj.get("type"), "keys:", list(obj.keys())[:12])
    print(json.dumps(obj, ensure_ascii=False)[:400])
