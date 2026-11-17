import json, os, tarfile, re, time

root = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\origin_resources"
cands = []
for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        if fn.lower() == "pdmx.tar.gz":
            cands.append(os.path.join(dirpath, fn))
print("找到 PDMX JSON 包:", cands)

path = cands[0]
t0 = time.time()
want = []
with tarfile.open(path, mode="r:gz") as tf:
    for m in tf:
        if not m.isfile() or not m.name.endswith(".json"):
            continue
        try:
            f = tf.extractfile(m)
            if f is None:
                continue
            data = json.loads(f.read().decode("utf-8", "ignore"))
        except Exception:
            continue
        title = str(data.get("title") or "")
        low = title.lower()
        if ("nielsen" in low and "quintet" in low) or ("schubert" in low and ("d. 926" in low or "d.926" in low or "d 929" in low or "op. 100" in low or "op.100" in low)):
            want.append({
                "member": m.name,
                "title": title,
                "composer": data.get("composer"),
                "license": data.get("license"),
                "tracks": data.get("tracks"),
                "n_tracks": data.get("n_tracks"),
                "bars": data.get("bars"),
                "id": data.get("id") or os.path.basename(m.name).replace(".json", ""),
            })
            print(want[-1])
print("匹配", len(want), "条；耗时 %.0fs" % (time.time() - t0))