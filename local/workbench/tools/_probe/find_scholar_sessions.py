import json, io, glob, os

for p in glob.glob(r"C:\Users\ThinkBook\.dsh\storages\session_projcache\sessions\*.json"):
    try:
        d = json.load(io.open(p, encoding="utf-8"))
    except Exception:
        continue
    ident = d.get("record", {}).get("identity", {})
    title = d.get("record", {}).get("rows", {}).get("title", {}).get("val", "")
    if "scholar" in json.dumps(ident, ensure_ascii=False).lower() or "scholar" in str(title).lower():
        print(os.path.basename(p))
        print("  identity:", json.dumps(ident, ensure_ascii=False)[:400])
        print("  title:", str(title)[:100])
