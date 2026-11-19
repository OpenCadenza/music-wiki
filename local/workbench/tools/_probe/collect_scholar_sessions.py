import json, io, glob, os

root = r"C:\Users\ThinkBook\.dsh\storages\session_projcache\sessions"
rows = {}
for p in glob.glob(os.path.join(root, "*.json")):
    try:
        d = json.load(io.open(p, encoding="utf-8"))
    except Exception:
        continue
    cat = d.get("record", {}).get("rows", {}).get("subagentCatalog", {})
    val = cat.get("val") if isinstance(cat, dict) else None
    if not isinstance(val, dict):
        continue
    for item in (val.get("head") or {}).get("values", []) or []:
        name = item.get("name") or ""
        if "scholar" in name:
            rows[item.get("childId")] = {
                "name": name,
                "label": item.get("label", ""),
                "createdAt": item.get("childCreatedAt"),
                "parent": os.path.basename(p),
            }
print("scholar child sessions:", len(rows))
for cid, info in sorted(rows.items(), key=lambda x: x[1]["createdAt"] or 0):
    print(cid, "|", info["name"], "|", info["label"][:40])

# 保存清单
io.open(os.path.join(os.getcwd(), "local", "workbench", "tools", "_probe", "scholar_sessions.json"), "w", encoding="utf-8").write(
    json.dumps(rows, ensure_ascii=False, indent=2))
