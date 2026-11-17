import glob, os, shutil

extract = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\origin_resources\downloads\2026-11-17\pdmx\extract"
dest_root = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\resources\scores\pdmx"

names = {
    198819: ("nielsen-op43-full", "nielsen-op43-wind-quintet-full.mxl"),
    75611: ("nielsen-kvnintet", "nielsen-kvnintet-alt.mxl"),
    98865: ("schubert-d929-ii-a", "schubert-d929-mvt2-a.mxl"),
    99688: ("schubert-d929-ii-b", "schubert-d929-mvt2-b.mxl"),
    125808: ("schubert-d929-ii-c", "schubert-d929-mvt2-c-with-directions.mxl"),
}

files = glob.glob(os.path.join(extract, "**", "*.mxl"), recursive=True)
for f in sorted(files):
    size = os.path.getsize(f)
    if size not in names:
        print("未登记大小:", size, f)
        continue
    d, fn = names[size]
    target_dir = os.path.join(dest_root, d)
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy2(f, os.path.join(target_dir, fn))
    print("已归档:", d, fn, size)

readme = os.path.join(dest_root, "README.md")
if not os.path.exists(readme):
    with open(readme, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("""# PDMX MusicXML 谱源（2026-11-17 入库）

来源：PDMX（Public Domain MusicXML）数据集，Zenodo 记录 15571083，文件 `mxl.tar.gz`（1,894,335,797 B），CC0/公有领域条目。

| 目录 | 文件 | 内容 |
| --- | --- | --- |
| `nielsen-op43-full/` | `nielsen-op43-wind-quintet-full.mxl` | Carl Nielsen 管乐五重奏 Op.43 全曲（5 声部：Flute/Oboe/A Clarinet/Horn in F/Bassoon，各 507 小节） |
| `nielsen-kvnintet/` | `nielsen-kvnintet-alt.mxl` | 另一份 Nielsen 管乐五重奏转录（丹麦语声部名，各 147 小节），备用 |
| `schubert-d929-ii-a/` | `schubert-d929-mvt2-a.mxl` | Schubert D.929 第二乐章（4 声部，212 小节）— 编码主源 |
| `schubert-d929-ii-b/` | `schubert-d929-mvt2-b.mxl` | 同曲另一份转录（排版坐标不同） |
| `schubert-d929-ii-c/` | `schubert-d929-mvt2-c-with-directions.mxl` | 同曲第三份，含德文和弦名 direction（导出噪声） |

原始 tar 归档位置：`local/origin_resources/downloads/2026-11-17/pdmx/mxl.tar.gz`。
归档结构为 `mxl/<两位hex>/<两位hex>/<hash>.mxl`；按 `score-s7/_probe/members-map.json` 里的文件名前缀匹配解出（tar 内的路径与清单里 `PDMX/mxl/...` 的写法不同）。
""")
    print("写入 README")