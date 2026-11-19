import json, io

p = r"C:\Users\ThinkBook\.dsh\storages\session_projcache\sessions\418993d0-5f8a-4a9f-a9e1-e690ba4f2f7c.json"
d = json.load(io.open(p, encoding="utf-8"))
print("top:", list(d.keys()))
rec = d.get("record", {})
print("record:", list(rec.keys()))
rows = rec.get("rows", {})
print("rows:", list(rows.keys()))

def find_text(obj, path="", out=None, depth=0):
    if out is None:
        out = []
    if depth > 6:
        return out
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, str) and ("接手与交付总结报告" in v or "scholar-a2" in v):
                out.append((path + "/" + k, len(v), v[:80]))
            find_text(v, path + "/" + k, out, depth + 1)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            find_text(v, f"{path}[{i}]", out, depth + 1)
    return out

for item in find_text(d)[:10]:
    print(item)
