import json, io, glob, os

needle = '"name": "scholar-a2"'
found = []
for p in glob.glob(r"C:\Users\ThinkBook\.dsh\storages\session_projcache\sessions\*.json"):
    raw = io.open(p, encoding="utf-8", errors="ignore").read()
    if needle in raw or '"name":"scholar-a2"' in raw:
        found.append(p)
print("files:", len(found))
for p in found[:5]:
    d = json.load(io.open(p, encoding="utf-8"))
    rec = d.get("record", {})
    rows = rec.get("rows", {})
    print("\n==", os.path.basename(p))
    print(" identity:", json.dumps(rec.get("identity", {}), ensure_ascii=False)[:300])
    print(" title:", json.dumps(rows.get("title", {}), ensure_ascii=False)[:200])
    print(" rows keys:", list(rows.keys())[:15])
    # 找 subagent 相关行
    for k in rows:
        s = json.dumps(rows[k], ensure_ascii=False)
        if "scholar-a2" in s:
            print("  row with scholar-a2:", k, s[:300])
            break
