import glob, io, json, os, zstandard as zstd

roots = glob.glob(r"C:\Users\ThinkBook\.dsh\sessions\*")
target = "418993d0-5f8a-4a9f-a9e1-e690ba4f2f7c"
path = None
for r in roots:
    p = os.path.join(r, target, "session.v4.jsonl.zstd")
    if os.path.exists(p):
        path = p
        break
print("file:", path, "size:", os.path.getsize(path) if path else None)

if path:
    dctx = zstd.ZstdDecompressor()
    with io.open(path, "rb") as fh:
        data = dctx.decompress(fh.read(), max_output_size=200 * 1024 * 1024)
    text = data.decode("utf-8", "ignore")
    lines = [l for l in text.split("\n") if l.strip()]
    print("events:", len(lines), "chars:", len(text))
    for line in lines[:3]:
        obj = json.loads(line)
        print("keys:", list(obj.keys()))
        print(json.dumps(obj, ensure_ascii=False)[:600])
