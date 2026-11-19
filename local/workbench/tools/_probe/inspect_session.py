import json, io, os, glob

p = r"C:\Users\ThinkBook\.dsh\storages\session_projcache\sessions\session-f50514cb-9aca-41c4-a002-6b52d2c7cdfe.json"
d = json.load(io.open(p, encoding="utf-8"))
print("top keys:", list(d.keys()))
r = d.get("record", {})
print("record keys:", list(r.keys())[:20])
rows = r.get("rows", {})
print("rows count:", len(rows))
for k in list(rows.keys())[:40]:
    v = rows[k]
    if isinstance(v, dict):
        val = v.get("val")
        t = type(val).__name__
        preview = json.dumps(val, ensure_ascii=False)[:80] if t not in ("str",) else val[:80]
        print(f"{k:40s} {t:8s} {preview}")
