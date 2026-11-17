import os, tarfile, time

src = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\origin_resources\downloads\2026-11-17\pdmx\mxl.tar.gz"
dst = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\origin_resources\downloads\2026-11-17\pdmx\extract"
targets = ("mxl/N/d/", "mxl/V/5/", "mxl/a/5/", "mxl/a/G/", "mxl/a/L/")

os.makedirs(dst, exist_ok=True)
t0 = time.time()
n = 0
seen = 0
with tarfile.open(src, mode="r:gz") as tf:
    for m in tf:
        seen += 1
        if not m.isfile():
            continue
        if any(m.name.startswith(t) for t in targets):
            tf.extract(m, dst)
            n += 1
            print("extracted", m.name, m.size)
print("扫描成员", seen, "解出", n, "耗时 %.1fs" % (time.time() - t0))