import glob, os, zipfile, re

dst = r"E:\github\music-wiki\.agents\worktrees\scholar-plan-dev\local\origin_resources\downloads\2026-11-17\pdmx\extract"
files = sorted(glob.glob(os.path.join(dst, "**", "*.mxl"), recursive=True))
print("文件数:", len(files))
for f in files:
    try:
        z = zipfile.ZipFile(f)
        names = z.namelist()
        root = next((n for n in names if n.endswith(".xml") and "META-INF" not in n), names[0])
        data = z.read(root).decode("utf-8", "ignore")
        title = re.search(r"<work-title>(.*?)</work-title>", data) or re.search(r"<movement-title>(.*?)</movement-title>", data)
        parts = re.findall(r"<score-part id=\"[^\"]+\">\s*<part-name>([^<]+)</part-name>", data)
        measures = len(re.findall(r"<measure ", data))
        times = re.findall(r"<time>.*?<beats>(\d+)</beats>.*?<beat-type>(\d+)</beat-type>", data, re.S)
        print("\n---", os.path.basename(f), os.path.getsize(f), "字节")
        print("  title:", (title.group(1).strip() if title else "?"))
        print("  parts:", parts[:8])
        print("  measures:", measures, "| time sigs:", sorted(set(times))[:4])
    except Exception as e:
        print(os.path.basename(f), "读取失败:", e)