import json, os, tarfile, time

root = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\origin_resources"
map_path = r"E:\github\music-wiki\.agents\worktrees\dsh-c6ded6ed-82bb\local\workbench\scores\score-s7\_probe\members-map.json"
arch = os.path.join(root, r"downloads\2026-11-17\pdmx\mxl.tar.gz")
dst = os.path.join(root, r"downloads\2026-11-17\pdmx\extract")

entries = json.load(open(map_path, encoding="utf-8"))
targets = []
for e in entries:
    t = (e.get("title") or "").lower()
    if ("nielsen" in t and "quintet" in t) or ("schubert" in t and ("trio" in t or "op. 100" in t or "op.100" in t)):
        base = os.path.basename(e.get("member", "")).replace(".json", "")
        targets.append((e.get("key"), e.get("title"), base))
print("目标：")
for k, t, b in targets:
    print(" ", k, "|", t, "| hash 前缀", b[:10], "...")

hashes = [b for _, _, b in targets]
os.makedirs(dst, exist_ok=True)
t0 = time.time()
n = 0
with tarfile.open(arch, mode="r:gz") as tf:
    for m in tf:
        if not m.isfile():
            continue
        base = os.path.basename(m.name)
        if base.endswith(".mxl") and any(base.startswith(h) for h in hashes):
            tf.extract(m, dst)
            n += 1
            print("extracted", m.name, m.size)
print("解出", n, "个，耗时 %.0fs" % (time.time() - t0))