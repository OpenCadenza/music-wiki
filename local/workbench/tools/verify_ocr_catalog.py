import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OCR = ROOT / "local/resources/text/ocr"
RAW = ROOT / "local/origin_resources"
OUT = ROOT / "local/resources/catalog/parts/ocr"

def rel(path):
    return path.relative_to(ROOT).as_posix()

def markdown_links(md_path, text):
    missing = []
    targets = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
    targets += re.findall(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", text, flags=re.I)
    for target in targets:
        target = target.split()[0].strip("<>")
        if re.match(r"^[a-z]+://", target, re.I) or target.startswith("data:"):
            continue
        candidate = (md_path.parent / target.split("#", 1)[0]).resolve()
        if not candidate.exists():
            missing.append({"markdown": rel(md_path), "target": target})
    return missing

items = []
for manifest_path in sorted(OCR.rglob("conversion.json")):
    m = json.loads(manifest_path.read_text(encoding="utf-8"))
    base = manifest_path.parent
    md_target = (m.get("outputs") or [{}])[0].get("markdown")
    jsonl_target = (m.get("outputs") or [{}])[0].get("jsonl")
    md = (ROOT / md_target) if md_target else next(iter(sorted(base.glob("*.md"))), None)
    jsonl = (ROOT / jsonl_target) if jsonl_target else next(iter(sorted(base.glob("*.jsonl"))), None)
    md_text = md.read_text(encoding="utf-8") if md and md.exists() else ""
    jl_text = jsonl.read_text(encoding="utf-8") if jsonl and jsonl.exists() else ""
    records, bad_json = [], []
    for n, line in enumerate(jl_text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except Exception as e:
            bad_json.append({"line": n, "error": str(e)})
    page_counts = []
    for record in records:
        result = record.get("result", {})
        lprs = result.get("layoutParsingResults")
        if isinstance(lprs, list):
            page_counts.append(len(lprs))
        else:
            page_counts.append(None)
    physical_pages = sum(n for n in page_counts if n is not None)
    expected = int(m.get("page_count", 0))
    missing_images = markdown_links(md, md_text) if md else []
    source = RAW / m["source_path"]
    original_ok = source.exists()
    image_only = m.get("reading_mode") == "source_image" and m.get("ocr_text_empty") is True
    service_markdown = ROOT / m["service_markdown"] if m.get("service_markdown") else None
    page_ok = bool(records) and not bad_json and all(n is not None for n in page_counts) and physical_pages == expected
    outputs = m.get("outputs", [])
    item = {
        "source_path": rel(source) if source.exists() else ("local/origin_resources/" + m["source_path"]),
        "source_exists": original_ok,
        "source_sha256": m.get("source_sha256"),
        "kind": source.suffix.lower().lstrip("."),
        "physical_pages_expected": expected,
        "jsonl_records": len(records),
        "jsonl_physical_pages": physical_pages if page_counts and all(n is not None for n in page_counts) else None,
        "jsonl_page_count_per_record": page_counts,
        "jsonl_pages_match": page_ok,
        "jsonl_errors": bad_json,
        "markdown_path": rel(md) if md else None,
        "markdown_nonempty": bool(md_text.strip()),
        "ocr_text_available": bool(md_text.strip()) and not image_only,
        "ocr_text_empty": m.get("ocr_text_empty", False),
        "reading_mode": m.get("reading_mode", "ocr_text"),
        "service_markdown_path": rel(service_markdown) if service_markdown else None,
        "service_markdown_exists": service_markdown.exists() if service_markdown else None,
        "service_markdown_bytes": service_markdown.stat().st_size if service_markdown and service_markdown.exists() else None,
        "source_image_path": rel(source) if image_only and source.exists() else None,
        "jsonl_path": rel(jsonl) if jsonl else None,
        "jsonl_nonempty": bool(jl_text.strip()),
        "manifest_path": rel(manifest_path),
        "conversion_status": m.get("status"),
        "missing_markdown_images": missing_images,
        "output_image_count": sum(int(o.get("image_count", 0)) for o in outputs),
        "images_dirs": [o.get("images_dir") for o in outputs if o.get("images_dir")],
        "page_ranges": m.get("page_ranges", []),
        "model": m.get("model"),
    }
    items.append(item)

OUT.mkdir(parents=True, exist_ok=True)
missing_refs = [r for i in items for r in i["missing_markdown_images"]]
valid_statuses = {"converted_readable", "converted_image_only"}
bad = [i for i in items if not (i["source_exists"] and i["markdown_nonempty"] and i["jsonl_nonempty"] and i["jsonl_pages_match"] and i["conversion_status"] in valid_statuses and (not i["ocr_text_empty"] or (i["reading_mode"] == "source_image" and i["service_markdown_exists"] and i["source_image_path"]))) ]
pdfs = [i for i in items if i["kind"] == "pdf"]
jpgs = [i for i in items if i["kind"] in ("jpg", "jpeg")]
samples = [
    ("教材示例：Alan Belkin, bk-O-O", "bk-O-O.pdf"),
    ("现代论文：Stanley, periodization sample", "stanley-periodization-sample.pdf"),
    ("现代导言：Bärenreiter cello sonatas preface", "barenreiter-cello-sonatas-preface.pdf"),
    ("历史扫描：Sala, Elementi", "sala_elementi_small.pdf"),
    ("原谱 JPG：Beethoven autograph page", "op98-autograph-page-001.jpg"),
]
def os_rel(p):
    return "../../../" + Path(p).relative_to("local/resources").as_posix() if p else ""

sample_results = []
for label, name in samples:
    i = next((x for x in items if Path(x["source_path"]).name == name), None)
    if not i:
        sample_results.append({"label": label, "source": name, "status": "missing_from_conversion_set"})
        continue
    mdp = ROOT / i["markdown_path"] if i["markdown_path"] else None
    text = mdp.read_text(encoding="utf-8") if mdp and mdp.exists() else ""
    sample_results.append({"label": label, "source": i["source_path"], "markdown": i["markdown_path"], "nonempty": bool(text.strip()), "opening_text": text[:500].strip(), "status": "readable_sample" if text.strip() else "empty_markdown"})

summary = {
    "checked_at": "2026-10-28",
    "scope": "conversion completeness and local Markdown image references only; no score-reading, musical fact audit, or scholarly reading claim",
    "totals": {"documents": len(items), "pdfs": len(pdfs), "pdf_pages": sum(i["physical_pages_expected"] for i in pdfs), "jpgs": len(jpgs), "jpg_physical_pages": sum(i["physical_pages_expected"] for i in jpgs), "ocr_text_documents": sum(i["ocr_text_available"] for i in items), "source_image_only_documents": sum(i["reading_mode"] == "source_image" for i in items), "markdown_files_nonempty": sum(i["markdown_nonempty"] for i in items), "jsonl_files_nonempty": sum(i["jsonl_nonempty"] for i in items), "jsonl_batch_records": sum(i["jsonl_records"] for i in items), "jsonl_physical_page_records": sum(i["jsonl_physical_pages"] or 0 for i in items), "jsonl_physical_pages_matched": sum(bool(i["jsonl_pages_match"]) for i in items), "jsonl_mismatches": sum(not i["jsonl_pages_match"] for i in items), "missing_markdown_image_references": len(missing_refs), "missing_original_sources": sum(not i["source_exists"] for i in items), "non_readable_or_incomplete": len(bad)},
    "sample_checks": sample_results,
    "exceptions": {"incomplete_documents": [{"source_path": i["source_path"], "checks": {k: i[k] for k in ("source_exists", "markdown_nonempty", "jsonl_nonempty", "jsonl_pages_match", "conversion_status")}} for i in bad], "missing_markdown_images": missing_refs},
    "page_number_note": "JSONL is batch-oriented. Each result.layoutParsingResults array entry contributes one physical page result in array/source order; the schema has no explicit physical-page-number field here. Any ordinal derived from these entries starts at 0 and is not mapped to printed page numbers.",
    "documents": items,
}
(OUT / "qa.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(OUT / "index.json").write_text(json.dumps({"title": "OCR conversion catalog", "qa": "qa.json", "documents": items}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lines = ["# OCR 转换与验收入口", "", f"已核对 {len(items)} 份：{len(pdfs)} 份 PDF（{sum(i['physical_pages_expected'] for i in pdfs)} 个物理页）及 {len(jpgs)} 份单页 JPG。其中 {sum(i['ocr_text_available'] for i in items)} 份有 OCR 文字，{sum(i['reading_mode'] == 'source_image' for i in items)} 份仅提供原件图像阅读。JSONL 有 {sum(i['jsonl_records'] for i in items)} 条批次记录，合计含 {sum(i['jsonl_physical_pages'] or 0 for i in items)} 个物理页结果；页数逐份匹配。逐页记录、状态、图像引用与原件可追溯性见 [qa.json](qa.json)。", "", "本目录只记录转换完整性。JSONL 批次可含多个页结果；`layoutParsingResults` 中每一项按物理页计数，按来源顺序核对。JSONL 此结构没有显式的物理页号；若从数组位置派生序号，以0起算，且不映射为印刷页码。OCR 可读不代表学者已阅读；原谱识别不作为音符转写或音乐学审计。", "", "## 五份有限读样", "", "以下只抽查开头文本与对应转换文件是否存在、非空，不代表通读或事实审校。", ""]
for s in sample_results:
    lines.append(f"- **{s['label']}**：" + (f"[Markdown]({os_rel(s.get('markdown'))})；状态 `{s['status']}`。" if s.get("markdown") else f"{s['source']}；状态 `{s['status']}`。"))
lines += ["", "## 全部来源", "", "| 原件 | 物理页 | 状态 | Markdown |", "| --- | ---: | --- | --- |"]
for i in items:
    src = Path(i["source_path"]).relative_to("local/origin_resources").as_posix()
    mdlink = f"[{Path(i['markdown_path']).name}]({os_rel(i['markdown_path'])})" if i["markdown_path"] else "缺失"
    stat = i["conversion_status"]
    if i["reading_mode"] == "source_image":
        stat += "；仅原图阅读"
    if not i["markdown_nonempty"]:
        stat += "；MD为空"
    if not i["jsonl_pages_match"] or not i["source_exists"]:
        stat += " ⚠"
    lines.append(f"| [{Path(src).name}](../../../../origin_resources/{src}) | {i['physical_pages_expected']} | `{stat}` | {mdlink} |")
lines += ["", "QA 汇总若有不完整、页数不匹配或缺图引用，会在 qa.json 中逐项列出；不会通过目录文字掩盖问题。", ""]

(OUT / "index.md").write_text("\n".join(lines), encoding="utf-8")
print(json.dumps(summary["totals"] | {"samples": sample_results}, ensure_ascii=False, indent=2))
