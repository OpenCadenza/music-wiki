#!/usr/bin/env python3
"""Prepare reading copies and provenance cards from an immutable source tree.

The script never downloads or edits source files. It copies text based assets,
extracts the acquired legacy OMT source, and records source manifest entries.
Large score and dataset archives are indexed without bulk extraction.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
import os
import re
import shutil
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

DEFAULT_ORIGIN = Path("local/origin_resources")
DEFAULT_MATERIALS = Path("local/materials")
DEFAULT_OUTPUT = Path("local/resources")
MAX_MEMBER_BYTES = 40 * 1024 * 1024
MAX_IMAGE_BYTES = 8 * 1024 * 1024
TEXT_EXTS = {".md", ".markdown", ".html", ".htm", ".txt", ".rst", ".tsv", ".csv", ".abc", ".krn", ".kern", ".ly", ".lyi", ".xml", ".mei", ".musicxml", ".json", ".yaml", ".yml"}
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
SKIP_PARTS = {".git", "__pycache__", "node_modules"}
SKIP_NAME_RE = re.compile(r"(?:^|[/_.-])(draft|generated|model|prompt|log|scratch|tmp|test)(?:[/_.-]|$)", re.I)


def safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def manifest_entries(data):
    if isinstance(data, list):
        return data
    if not isinstance(data, dict):
        return []
    for key in ("items", "files", "downloads", "sources", "entries", "results", "records"):
        value = data.get(key)
        if isinstance(value, list):
            return value
    if any(key in data for key in ("path", "status", "url", "repository", "archive")):
        return [data]
    if data and all(isinstance(value, dict) for value in data.values()):
        return [dict(value, _manifest_key=key) for key, value in data.items()]
    return []


def first(entry, *keys, default=""):
    for key in keys:
        value = entry.get(key)
        if value not in (None, ""):
            return value
    return default


def source_cards(origin: Path, output: Path, readable, score_packages):
    cards = output / "catalog" / "parts" / "text" / "sources"
    cards.mkdir(parents=True, exist_ok=True)
    summary = []
    sources = origin / "sources"
    if not sources.is_dir():
        raise FileNotFoundError(f"missing source directory: {sources}")
    for src in sorted(path for path in sources.iterdir() if path.is_dir()):
        readme = safe_read(src / "README.md")
        raw_manifest = safe_read(src / "manifest.json")
        try:
            data = json.loads(raw_manifest) if raw_manifest else {}
        except json.JSONDecodeError:
            data = {}
        entries = manifest_entries(data)
        if not entries and isinstance(data, dict) and (data.get("repos") or data.get("score_scan_pages")):
            entries = []
            source_prefix = f"music-library/sources/{src.name}/"
            for repo in data.get("repos", []):
                archive = str(repo.get("archive", ""))
                path = archive[len(source_prefix):] if archive.startswith(source_prefix) else archive
                entries.append({
                    "title": repo.get("repository", archive or "Kern谱包"),
                    "status": "downloaded" if path and (src / path).is_file() else "archive path needs review",
                    "path": path, "url": repo.get("url"), "bytes": repo.get("bytes"),
                    "sha256": repo.get("sha256"), "members": repo.get("humdrum_krn_members"),
                    "note": repo.get("note"),
                })
            for page in data.get("score_scan_pages", []):
                for scan in page.get("files", []):
                    source_path = str(scan.get("path", ""))
                    path = source_path[len(source_prefix):] if source_path.startswith(source_prefix) else source_path
                    entries.append({
                        "title": f"{page.get('work', page.get('id', 'scan'))} — digital page {scan.get('page_number_digital', '?')}",
                        "status": "downloaded" if path and (src / path).is_file() else "image path needs review",
                        "path": path, "url": scan.get("source_image_url", page.get("url")),
                        "page_scope": page.get("page_scope"), "edition": page.get("edition"),
                        "rights": page.get("rights"), "note": page.get("observed"),
                        "bytes": scan.get("bytes"), "sha256": scan.get("sha256"),
                    })
        items, statuses = [], {}
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            status = str(first(entry, "status", "result", "state", default="unspecified"))
            statuses[status] = statuses.get(status, 0) + 1
            file_path = first(entry, "path", "local_path", "file", "target")
            url = first(entry, "url", "source_url", "href")
            title = first(entry, "title", "name", "_manifest_key", default=Path(str(file_path)).name if file_path else "未命名条目")
            origin_link = ""
            if file_path:
                raw_path = PurePosixPath(str(file_path))
                if str(file_path).startswith("../../corpus/"):
                    relative_origin = Path(*raw_path.parts[2:])
                else:
                    relative_origin = Path("sources", src.name, *raw_path.parts)
                if (origin / relative_origin).is_file():
                    origin_link = "../../../../../origin_resources/" + relative_origin.as_posix()
            details = [f"状态：{status}"]
            if file_path and origin_link:
                details.append(f"原件：[{file_path}]({origin_link})")
            elif file_path:
                details.append(f"目标路径未实存：{file_path}")
            if url:
                details.append(f"来源：{url}")
            content_type = first(entry, "content_type", "mime_type")
            if content_type and ("html" in str(content_type).lower() or "text/html" in str(content_type).lower()):
                details.append("HTML页面；视为目录或摘要入口，正文范围未确认")
            for field, label in (("members", "谱文件数"), ("bytes", "字节"), ("page_scope", "页范围"), ("edition", "版本"), ("rights", "权利说明"), ("note", "说明")):
                if entry.get(field) not in (None, ""):
                    detail = str(entry[field]).strip().replace("|", "｜")
                    if field == "note":
                        detail = detail[:500]
                    details.append(f"{label}：{detail}")
            error = first(entry, "error", "message", "failure")
            if error:
                details.append(f"结果备注：{str(error).strip()}")
            items.append("- **" + str(title).replace("|", "｜") + "** — " + "；".join(details))
        readme_summary = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", readme)
        readme_summary = re.sub(r"[`*_>#]", "", readme_summary)
        readme_summary = " ".join(readme_summary.split())
        readme_summary = readme_summary[:1100] + ("…" if len(readme_summary) > 1100 else "")
        body = [
            f"# {src.name}", "",
            f"> 来源说明：[原始 README](../../../../../origin_resources/sources/{src.name}/README.md)；清单：[manifest.json](../../../../../origin_resources/sources/{src.name}/manifest.json)。本卡只说明取得范围和状态，不表示已读完全文。", "",
            f"清单条目：{len(entries)}；状态计数：{json.dumps(statuses, ensure_ascii=False, sort_keys=True)}。", "",
            "## 来源说明摘要", "", readme_summary or "未提供 README 摘要；请以原始 README 和 manifest 为准。", "",
            "## 清单条目", "", *(items or ["manifest 未解析出逐项记录；请直接查看原始 manifest。"]), "",
            "## 本地阅读副本", "",
            *([f"- [{Path(item['copy']).name}](../../../../text/source-copies/{item['source']}/{item['copy'].split('/', 3)[-1]})" for item in readable if item["source"] == src.name] or ["没有从 raw/ 复制单独文本文件；请使用上方的原件入口或压缩包目录清点。"]),
            *(["- [旧版 OMT 可读源码](../../../../text/open-music-theory/legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/contents.md)"] if src.name == "open-music-theory" else []),
            *(["- [整理后的 DCML 标注表](../../../../scores/dcml-abc/README.md)"] if src.name == "dcml" else []), "",
            *([f"- [解包机器可读谱源](../../../../scores/source-packages/{src.name}/README.md)（{sum(p['score_files'] for p in score_packages if p['source'] == src.name)} 个谱文件）"] if any(p["source"] == src.name for p in score_packages) else []), "",
            "## 其他清单元数据", "",
            json.dumps({key: value for key, value in data.items() if key not in {"records", "items", "files", "downloads", "sources", "entries", "results", "repos", "score_scan_pages"}}, ensure_ascii=False, indent=2)[:6000] if isinstance(data, dict) else "无", "",
        ]
        (cards / f"{src.name}.md").write_text("\n".join(body), encoding="utf-8")
        summary.append({"source": src.name, "entries": len(entries), "statuses": statuses, "card": f"catalog/parts/text/sources/{src.name}.md"})
    return summary


def copy_readable_raw(origin: Path, output: Path):
    destroot = output / "text" / "source-copies"
    copied, skipped = [], []
    for src in sorted((origin / "sources").iterdir()):
        if not src.is_dir():
            continue
        raw = src / "raw"
        if not raw.is_dir():
            continue
        for file in raw.rglob("*"):
            if not file.is_file() or any(part in SKIP_PARTS for part in file.parts):
                continue
            if file.suffix.lower() not in TEXT_EXTS | IMAGE_EXTS:
                continue
            if file.suffix.lower() in IMAGE_EXTS and file.stat().st_size > MAX_IMAGE_BYTES:
                continue
            if SKIP_NAME_RE.search(file.as_posix()):
                skipped.append({"path": file.relative_to(origin).as_posix(), "reason": "排除旧生成稿、日志或临时文件名"})
                continue
            target = destroot / src.name / file.relative_to(raw)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, target)
            copied.append({"source": src.name, "origin": file.relative_to(origin).as_posix(), "copy": target.relative_to(output).as_posix(), "bytes": file.stat().st_size})
    return copied, skipped


def extract_omt(origin: Path, output: Path):
    archive = origin / "sources" / "open-music-theory" / "raw" / "openmusictheory.github.io-master.zip"
    if not archive.exists():
        return {"status": "missing", "reason": "旧版 OMT ZIP 未在原始库中找到"}
    base = output / "text" / "open-music-theory" / "legacy-source"
    copied, ignored, errors, ignored_reasons = [], 0, [], {}
    image_exts = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
    with zipfile.ZipFile(archive) as zf:
        for info in zf.infolist():
            if info.is_dir():
                continue
            member = PurePosixPath(info.filename)
            if member.is_absolute() or ".." in member.parts:
                errors.append({"member": info.filename, "reason": "不安全归档路径"})
                continue
            reason = ""
            if member.suffix.lower() not in TEXT_EXTS | image_exts:
                reason = "非阅读文本或图像格式"
            elif SKIP_NAME_RE.search(info.filename):
                reason = "文件名命中旧稿/日志/临时排除规则"
            elif info.file_size > MAX_MEMBER_BYTES:
                reason = "单文件超过40 MiB上限"
            if reason:
                ignored += 1
                ignored_reasons[reason] = ignored_reasons.get(reason, 0) + 1
                continue
            target = base.joinpath(*member.parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                with zf.open(info) as source, target.open("wb") as dest:
                    shutil.copyfileobj(source, dest)
                copied.append({"member": info.filename, "copy": target.relative_to(output).as_posix(), "bytes": info.file_size})
            except (OSError, zipfile.BadZipFile) as exc:
                errors.append({"member": info.filename, "reason": str(exc)})
    guide = output / "text" / "open-music-theory" / "README.md"
    guide.parent.mkdir(parents=True, exist_ok=True)
    guide.write_text("\n".join([
        "# Open Music Theory：旧版教材阅读入口", "",
        "> 此处来自官方 GitHub 旧版 `openmusictheory.github.io` 源码 ZIP，不是当前 OMT2。OMT2 PDF/XML/EPUB 下载均在原始 manifest 记录为 HTTP 403。", "",
        f"- [官方旧版目录页阅读副本](legacy-source/openmusictheory-openmusictheory.github.io-a907aa0/contents.md)。此目录列出的章节是教材正文入口。",
        f"- 完整原件：[openmusictheory.github.io-master.zip](../../../../origin_resources/sources/open-music-theory/raw/openmusictheory.github.io-master.zip)；来源卡：[open-music-theory](../../catalog/parts/text/sources/open-music-theory.md)。",
        f"- 抽取可读文本/图像 {len(copied)} 个；有 {ignored} 个非阅读格式成员未抽取。现有 Markdown 有 130 篇与 ZIP 内同路径原件 SHA-256 一致；只将站内链接改为本地可读路径，正文文字保持原样。", "",
        "仓库中的 `404.md`、`robots.txt`、README、版权/图形制作与链接维护等页面保留来源语境，不作为教材章节。目录中未链接的草稿或辅助页面也不自动当作教材入口。章节文本和图表应结合其原件与版本阅读。", "",
    ]), encoding="utf-8")
    return {"status": "extracted-readable-subset", "count": len(copied), "ignored": ignored, "ignored_reasons": ignored_reasons, "errors": errors, "guide": guide.relative_to(output).as_posix(), "copies": copied}


def copy_dcml_materials(origin: Path, materials: Path, output: Path):
    source = materials / "theory" / "dcml-abc"
    if not source.is_dir():
        return {"status": "missing", "count": 0, "reason": "没有现有 dcml-abc 可读材料"}
    target_root = output / "scores" / "dcml-abc"
    archive = origin / "sources" / "dcml" / "raw" / "ABC-main.zip"
    if not archive.is_file():
        return {"status": "missing-source-archive", "count": 0, "reason": "DCML 原包缺失，不能验证现有副本来源"}
    copied, excluded_reviewed, unmatched = 0, 0, []
    provenance = []
    with zipfile.ZipFile(archive) as zf:
        by_name = {}
        for member in zf.infolist():
            if not member.is_dir():
                by_name.setdefault(PurePosixPath(member.filename).name, []).append(member)
        for file in source.rglob("*"):
            if not file.is_file() or file.suffix.lower() not in {".tsv", ".csv", ".mei", ".xml", ".musicxml", ".md", ".json"}:
                continue
            if file.name.endswith("_reviewed.tsv"):
                excluded_reviewed += 1
                continue
            if SKIP_NAME_RE.search(file.as_posix()):
                continue
            source_member = None
            digest = hashlib.sha256(file.read_bytes()).hexdigest()
            for candidate in by_name.get(file.name, []):
                with zf.open(candidate) as raw:
                    if hashlib.sha256(raw.read()).hexdigest() == digest:
                        source_member = candidate.filename
                        break
            if not source_member:
                unmatched.append(file.relative_to(source).as_posix())
                continue
            target = target_root / file.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, target)
            provenance.append({"copy": target.relative_to(output).as_posix(), "source_member": source_member, "bytes": file.stat().st_size, "sha256": digest})
            copied += 1
    (target_root / "manifest.json").write_text(json.dumps({"source_archive": "sources/dcml/raw/ABC-main.zip", "verified_by": "identical SHA-256 and matching member basename", "matched_files": len(provenance), "unmatched_files": unmatched, "files": provenance}, ensure_ascii=False, indent=2), encoding="utf-8")
    readme = [
        "# DCML Annotated Beethoven Corpus：阅读副本", "",
        "> 来源为 DCMLab 官方 ABC 子库。原始压缩包：[ABC-main.zip](../../../origin_resources/sources/dcml/raw/ABC-main.zip)；来源卡：[dcml](../../catalog/parts/text/sources/dcml.md)。此处副本来自现有加工材料 `local/materials/theory/dcml-abc/`，用于本地查阅。", "",
        f"纳入文件 {copied} 个，并与官方 ABC ZIP 内同名成员逐文件 SHA-256 完全匹配；明细见 [manifest.json](manifest.json)。未匹配文件 {len(unmatched)} 个。排除既有 `_reviewed.tsv` 文件 {excluded_reviewed} 个，因为其加工来源和方法未在原始来源清单中登记。", "",
        "表格按作品记录和弦、harmony、measure、note 等注释，具体列名以 TSV 表头及官方数据字典为准。`metadata.tsv` 记录作品、标注版本、annotators、来源文件路径等。不要将这些结构化标签写成已完成的音乐学解释。", "",
        "ABC 是 DCML 的一个子库，原始许可为 CC BY-NC-SA 4.0；此材料只作为本地研究数据。文件名含 `_reviewed` 的旧加工表未复制，且本整理未逐项核验标注内容。", "",
    ]
    (target_root / "README.md").write_text("\n".join(readme), encoding="utf-8")
    return {"status": "copied-existing-materials", "count": copied, "verified_source_matches": len(provenance), "unmatched": unmatched, "excluded_reviewed": excluded_reviewed, "copy_root": target_root.as_posix(), "origin_reference": "local/materials/theory/dcml-abc", "archive": archive.relative_to(origin).as_posix()}


def compare_existing_omt(materials: Path, omt: dict, output: Path):
    source = materials / "theory" / "open-music-theory"
    copied_root = output / "text" / "open-music-theory" / "legacy-source" / "openmusictheory-openmusictheory.github.io-a907aa0"
    if not source.is_dir() or not copied_root.is_dir():
        return {"matched": 0, "different": [], "missing": []}
    same, different, missing = 0, [], []
    for file in source.rglob("*.md"):
        relative = file.relative_to(source)
        counterpart = copied_root / relative
        if not counterpart.is_file():
            missing.append(relative.as_posix())
        elif hashlib.sha256(file.read_bytes()).digest() == hashlib.sha256(counterpart.read_bytes()).digest():
            same += 1
        else:
            different.append(relative.as_posix())
    return {"matched": same, "different": different, "missing": missing}


def rewrite_omt_links(output: Path):
    """Make a reading copy navigable offline while leaving the ZIP untouched."""
    base = output / "text" / "open-music-theory" / "legacy-source" / "openmusictheory-openmusictheory.github.io-a907aa0"
    if not base.is_dir():
        return {"rewritten": 0, "unresolved": []}
    pattern = re.compile(r"(!?\[[^\]]*\]\()([^\)]+)(\))")
    rewritten = 0
    unresolved = []
    for file in base.rglob("*.md"):
        text = file.read_text(encoding="utf-8", errors="replace")
        text = text.replace("pitch(Class).html", "pitch%28Class%29.md").replace("interval(Class).html", "interval%28Class%29.md")
        text = text.replace("(pitch(Class))", "(pitch%28Class%29.md)").replace("(interval(Class))", "(interval%28Class%29.md)")
        def replace(match):
            nonlocal rewritten
            url = match.group(2)
            if url.startswith(("http://", "https://", "mailto:", "spotify:", "#")):
                return match.group(0)
            suffix = ""
            if "#" in url:
                url, anchor = url.split("#", 1)
                suffix = "#" + anchor
            if url.startswith("{{ site.url }}/"):
                relative = url.split("}}/", 1)[1]
                candidate = base / Path(*PurePosixPath(relative).parts)
                if candidate.is_file():
                    new_url = os.path.relpath(candidate, file.parent).replace(os.sep, "/") + suffix
                    rewritten += 1
                    return match.group(1) + new_url + match.group(3)
            candidate = (file.parent / unquote(url)).resolve()
            alternatives = []
            if candidate.suffix.lower() == ".html":
                alternatives.append(candidate.with_suffix(".md"))
            elif not candidate.suffix:
                alternatives.append(candidate.with_suffix(".md"))
            replacement = next((item for item in alternatives if item.is_file()), None)
            if replacement:
                new_url = os.path.relpath(replacement, file.parent).replace(os.sep, "/") + suffix
                rewritten += 1
                return match.group(1) + new_url + match.group(3)
            if not candidate.is_file() and not url.startswith("{{"):
                unresolved.append({"file": file.relative_to(base).as_posix(), "url": match.group(2)})
            return match.group(0)
        updated = pattern.sub(replace, text)
        if updated != text:
            file.write_text(updated, encoding="utf-8")
    return {"rewritten": rewritten, "unresolved": unresolved[:250], "unresolved_count": len(unresolved)}


def zip_inventory(origin: Path, omt=None, score_packages=None):
    records = []
    extracted_archives = {item["archive"]: item for item in (score_packages or [])}
    for file in (origin / "sources").rglob("*.zip"):
        if file.parent.name != "raw":
            continue
        record = {"origin": file.relative_to(origin).as_posix(), "bytes": file.stat().st_size}
        if file.parent.parent.name == "pdmx":
            record["status"] = "未展开；大型数据集按需使用"
        else:
            try:
                with zipfile.ZipFile(file) as zf:
                    names = [name for name in zf.namelist() if not name.endswith("/")]
                record["member_count"] = len(names)
                record["text_candidates"] = sum(Path(name).suffix.lower() in TEXT_EXTS for name in names)
                record["score_candidates"] = sum(Path(name).suffix.lower() in {".krn", ".kern", ".abc", ".ly", ".lyi", ".mei", ".xml", ".musicxml", ".mscx"} for name in names)
                if file.parent.parent.name == "open-music-theory":
                    record["status"] = "已抽取可读文本和图像子集"
                    record["extracted_readable_items"] = (omt or {}).get("count", 0)
                elif record["origin"] in extracted_archives:
                    record["status"] = "已按类型解包机器可读谱文件"
                    record["extracted_score_files"] = extracted_archives[record["origin"]]["score_files"]
                else:
                    record["status"] = "只检查目录；未解包"
            except (zipfile.BadZipFile, OSError) as exc:
                record.update(status="读取失败", error=str(exc))
        records.append(record)
    return records


def extract_score_packages(origin: Path, output: Path):
    specs = [
        ("beethoven-score-sources", "beethoven-piano-sonatas-main.zip", {".krn"}),
        ("beethoven-score-sources", "beethoven-string-quartets-main.zip", {".krn"}),
        ("humdrum", "bach-370-chorales-main.zip", {".krn"}),
        ("josquin", "jrp-scores-main.zip", {".krn"}),
        ("dcml", "ABC-main.zip", {".mscx"}),
    ]
    root = output / "scores" / "source-packages"
    summaries = []
    for source, archive_name, extensions in specs:
        archive = origin / "sources" / source / "raw" / archive_name
        if not archive.is_file():
            summaries.append({"source": source, "archive": archive.relative_to(origin).as_posix(), "status": "missing", "score_files": 0})
            continue
        package_root = root / source / archive.stem
        files, errors = [], []
        with zipfile.ZipFile(archive) as zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                member = PurePosixPath(info.filename)
                if member.is_absolute() or ".." in member.parts:
                    errors.append({"member": info.filename, "reason": "不安全归档路径"})
                    continue
                if member.suffix.lower() not in extensions:
                    continue
                target = package_root.joinpath(*member.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                try:
                    with zf.open(info) as source_file, target.open("wb") as dest:
                        shutil.copyfileobj(source_file, dest)
                    digest = hashlib.sha256(target.read_bytes()).hexdigest()
                    files.append({"archive_member": info.filename, "copy": target.relative_to(output).as_posix(), "bytes": info.file_size, "sha256": digest})
                except (OSError, zipfile.BadZipFile) as exc:
                    errors.append({"member": info.filename, "reason": str(exc)})
        package_root.mkdir(parents=True, exist_ok=True)
        package_manifest = {"source": source, "archive": archive.relative_to(origin).as_posix(), "archive_bytes": archive.stat().st_size, "selected_extensions": sorted(extensions), "score_files": len(files), "errors": errors, "files": files}
        (package_root / "manifest.json").write_text(json.dumps(package_manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        summaries.append({"source": source, "archive": archive.relative_to(origin).as_posix(), "archive_name": archive_name, "status": "extracted" if not errors else "extracted-with-errors", "score_files": len(files), "bytes": sum(item["bytes"] for item in files), "formats": sorted(extensions), "manifest": (package_root / "manifest.json").relative_to(output).as_posix(), "errors": errors})
    by_source = {}
    for item in summaries:
        by_source.setdefault(item["source"], []).append(item)
    for source, packages in by_source.items():
        source_root = root / source
        source_root.mkdir(parents=True, exist_ok=True)
        lines = [
            f"# {source}：机器可读谱副本", "",
            "> 从原始 ZIP 按扩展名筛选解包；未编译、转码或逐音检查。副本保留 ZIP 内原始成员路径。逐文件清单记录原始成员、复制路径、字节数和 SHA-256。", "",
        ]
        for item in packages:
            lines.extend([
                f"## {item.get('archive_name', Path(item['archive']).name)}", "",
                f"原包：[{Path(item['archive']).name}](../../../../origin_resources/{item['archive']})（{item.get('bytes', 0)} bytes）；格式：{', '.join(item['formats']) if item.get('formats') else '无'}；解包谱文件：{item['score_files']}。状态：{item['status']}。", "",
                f"逐文件清单：[{Path(item['manifest']).name}]({Path(item['archive_name']).stem}/manifest.json)。", "",
            ])
        (source_root / "README.md").write_text("\n".join(lines), encoding="utf-8")
    root.mkdir(parents=True, exist_ok=True)
    total = sum(item["score_files"] for item in summaries)
    lines = [
        "# 机器可读谱包副本", "",
        f"> 从指定来源 ZIP 选取原生谱文件；共 {total} 个。原始 ZIP 保留在 `local/origin_resources/`，此处只提供可直接阅读的解包副本。没有全量转换或编译。", "",
        "| 来源 | 上游 ZIP | 格式 | 文件数 | 解包目录 |", "| --- | --- | --- | ---: | --- |",
    ]
    for item in summaries:
        lines.append(f"| [{item['source']}]({item['source']}/README.md) | [{Path(item['archive']).name}](../../../origin_resources/{item['archive']}) | {', '.join(item.get('formats', []))} | {item['score_files']} | `{item['source']}/{Path(item.get('archive_name', Path(item['archive']).name)).stem}/` |")
    lines.extend(["", "DCML ABC 的机器可读乐谱是 `.mscx`；现有 TSV 标注副本另见 `../dcml-abc/README.md`。原始数据包许可证和边界见各来源说明。", ""])
    (root / "README.md").write_text("\n".join(lines), encoding="utf-8")
    return summaries


def score_material_count(materials: Path):
    root = materials / "scores"
    return sum(1 for file in root.rglob("*") if file.is_file()) if root.is_dir() else 0


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() in {"script", "style", "noscript", "svg"}:
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag.lower() in {"script", "style", "noscript", "svg"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.parts.append(data.strip())


def html_body_summary(path: Path):
    parser = VisibleText()
    parser.feed(path.read_text(encoding="utf-8", errors="replace"))
    body = " ".join(parser.parts)
    return {"visible_text_chars": len(body), "preview": body[:240], "is_error_page": bool(re.search(r"\b(404|page not found|robots denied|access denied)\b", body[:2000], re.I))}


def manifest_reference(origin: Path, source: str, raw_path: str):
    manifest = origin / "sources" / source / "manifest.json"
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    for entry in manifest_entries(data):
        if isinstance(entry, dict) and str(first(entry, "path", "local_path", "file")) == raw_path:
            return {key: entry.get(key) for key in ("url", "status", "bytes", "sha256", "content_type") if entry.get(key) not in (None, "")}
    return {}


def sample_readability_qa(origin: Path, output: Path, omt, score_packages, dcml):
    samples = []
    omt_dir = output / "text" / "open-music-theory" / "legacy-source" / "openmusictheory-openmusictheory.github.io-a907aa0"
    chapter = omt_dir / "bassoContinuo.md"
    contents = safe_read(omt_dir / "contents.md")
    chapter_text = safe_read(chapter)
    image_match = re.search(r"!\[[^\]]*\]\(([^)]+)\)", chapter_text)
    image_relative = image_match.group(1) if image_match else ""
    image_copy = (chapter.parent / image_relative).resolve() if image_relative else None
    image_member = next((item for item in omt.get("copies", []) if item.get("copy") and Path(item["copy"]).as_posix().endswith("/" + image_relative)), None)
    samples.append({
        "kind": "textbook_chapter", "source": "open-music-theory", "copy": chapter.relative_to(output).as_posix(),
        "origin": "sources/open-music-theory/raw/openmusictheory.github.io-master.zip :: " + (image_member or {}).get("member", "bassoContinuo.md"),
        "readable": chapter.is_file() and len(chapter_text) > 500,
        "listed_in_official_table_of_contents": "bassoContinuo.md" in contents,
        "linked_image": {"markdown_target": image_relative, "copy_exists": bool(image_copy and image_copy.is_file()), "origin_member": (image_member or {}).get("member"), "copy": (image_member or {}).get("copy")},
        "note": "旧版 OMT 章节正文；本地化仅改写站内链接，原 ZIP 保留。",
    })
    html_samples = [
        ("analysis_html", "music-theory-online", "raw/cohn-2016-funky-rhythms-1119934417edfd1e.html"),
        ("instrument_html", "philharmonia", "raw/instruments/flute.html"),
        ("work_version_html", "beethoven-analysis-keyboard", "raw/barry-op131-teleology-1990.html"),
    ]
    for kind, source, raw_path in html_samples:
        raw = origin / "sources" / source / raw_path
        copy = output / "text" / "source-copies" / source / Path(raw_path).relative_to("raw")
        summary = html_body_summary(copy) if copy.is_file() else {"visible_text_chars": 0, "preview": "", "is_error_page": True}
        ref = manifest_reference(origin, source, raw_path)
        samples.append({
            "kind": kind, "source": source, "copy": copy.relative_to(output).as_posix(),
            "origin": raw.relative_to(origin).as_posix(), "origin_exists": raw.is_file(),
            "source_manifest_reference": ref, **summary,
            "readable": raw.is_file() and copy.is_file() and summary["visible_text_chars"] > 500 and not summary["is_error_page"],
        })
    kern_package = next(item for item in score_packages if item["source"] == "beethoven-score-sources" and "piano-sonatas" in item["archive_name"])
    kern_manifest_path = output / kern_package["manifest"]
    kern_manifest = json.loads(kern_manifest_path.read_text(encoding="utf-8"))
    kern_file = kern_manifest["files"][0]
    kern_copy = output / kern_file["copy"]
    kern_text = kern_copy.read_text(encoding="utf-8", errors="replace")
    samples.append({
        "kind": "kern_score", "source": "beethoven-score-sources", "copy": kern_file["copy"],
        "origin_archive": kern_package["archive"], "archive_member": kern_file["archive_member"],
        "copy_sha256": kern_file["sha256"], "has_kern_spine": "**kern" in kern_text,
        "has_note_tokens": bool(re.search(r"(?<![A-Za-z])[A-Ga-g]{1,7}[#n-]?(?![A-Za-z])", kern_text)),
        "readable": kern_copy.is_file() and "**kern" in kern_text,
    })
    (output / "scores" / "source-packages" / "README.md").read_text(encoding="utf-8")
    return {
        "scope": "五份本地可读性抽样；检查正文/谱编码、图像路径和来源映射，不做音乐学事实核验。",
        "samples": samples,
        "dcml_provenance": {"matched_files": dcml.get("verified_source_matches", 0), "unmatched_files": len(dcml.get("unmatched", [])), "manifest": "scores/dcml-abc/manifest.json"},
        "result": "pass" if all(item.get("readable") for item in samples) and dcml.get("verified_source_matches", 0) == dcml.get("count", -1) else "needs-review",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--origin", type=Path, default=DEFAULT_ORIGIN, help="只读原始库目录")
    parser.add_argument("--materials", type=Path, default=DEFAULT_MATERIALS, help="既有加工材料")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="加工输出根目录")
    args = parser.parse_args()
    origin, materials, output = args.origin.resolve(), args.materials.resolve(), args.output.resolve()
    if not (origin / "sources").is_dir():
        raise SystemExit(f"origin source directory not found: {origin / 'sources'}")
    output.mkdir(parents=True, exist_ok=True)
    readable, excluded = copy_readable_raw(origin, output)
    omt = extract_omt(origin, output)
    existing_omt = compare_existing_omt(materials, omt, output)
    omt_navigation = rewrite_omt_links(output)
    dcml = copy_dcml_materials(origin, materials, output)
    score_packages = extract_score_packages(origin, output)
    cards = source_cards(origin, output, readable, score_packages)
    archives = zip_inventory(origin, omt, score_packages)
    qa = sample_readability_qa(origin, output, omt, score_packages, dcml)
    score_count = sum(item["score_files"] for item in score_packages)
    report = {
        "scope": "初步整理和可发现性；不是全文阅读、音乐分析或逐条事实核验",
        "source_root": str(origin),
        "counts": {
            "sources": len(cards),
            "readable_text_copies": sum(Path(item["copy"]).suffix.lower() in TEXT_EXTS for item in readable),
            "associated_image_assets": sum(Path(item["copy"]).suffix.lower() in IMAGE_EXTS for item in readable),
            "readable_assets": len(readable),
            "excluded_text_assets": len(excluded),
            "archives": len(archives),
            "machine_readable_score_files": score_count,
            "score_packages": len(score_packages),
        },
        "sources": cards, "omt": omt, "omt_navigation": omt_navigation, "existing_omt_comparison": existing_omt, "dcml": dcml, "score_packages": score_packages, "archives": archives, "qa": qa, "excluded": excluded,
    }
    index_root = output / "catalog" / "parts" / "text"
    index_root.mkdir(parents=True, exist_ok=True)
    (index_root / "index.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (index_root / "qa.json").write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# 文本与编码谱源入口", "",
        "> 初步整理索引。来源卡、目录页、摘要、失败下载均保留状态；这些记录不代表已读完全文或已核验音乐事实。", "",
        f"来源数：{len(cards)}；raw 文本副本 {report['counts']['readable_text_copies']} 个，关联图像 {report['counts']['associated_image_assets']} 个；跟踪 ZIP {len(archives)} 个；另有 {len(score_packages)} 个机器可读谱包已选取解包。", "",
        "## 来源卡", "", *[f"- [{item['source']}](sources/{item['source']}.md)（清单条目 {item['entries']}）" for item in cards], "",
        "## 可读材料", "",
        f"- [OMT 旧版教材阅读入口](../../../text/open-music-theory/README.md)：官方 GitHub 旧版源码，非 OMT2。抽取 {omt.get('count', 0)} 项；现有 Markdown 与官方源码同路径 SHA-256 一致 {existing_omt.get('matched', 0)} 项；已改写 {omt_navigation.get('rewritten', 0)} 个可解析的站内链接，另有 {omt_navigation.get('unresolved_count', 0)} 个源链接目标未取得或未识别。",
        f"- [DCML 标注 TSV 说明](../../../scores/dcml-abc/README.md)：[阅读副本目录](../../../scores/dcml-abc/)，纳入 {dcml.get('count', 0)} 项，排除未登记来源的 `_reviewed.tsv` {dcml.get('excluded_reviewed', 0)} 项；需结合 ABC 原件及数据字典使用。",
        "- [其他 HTML、文本和原生编码副本](../../../text/source-copies/)：保留来源子目录和相对路径。", "",
        f"- [机器可读谱包副本](../../../scores/source-packages/README.md)：从 Beethoven Kern、Bach 370 Chorales、Josquin、DCML ABC 指定原包解出 {score_count} 个原生谱文件；不编译或转换。", "",
        "- [本地可读性抽样记录](qa.json)：覆盖教材、MTO、Philharmonia、作品/版本 HTML 和 Beethoven Kern 谱。", "",
        f"- [既有谱源总目录](../../../../materials/scores/CATALOG.md)（{score_material_count(materials)} 个文件）；[第二批贝多芬奏鸣曲记录](../../../../materials/scores/BATCH2-INDEX.md)。", "",
        "## 大型谱包和未处理项", "",
        "- ZIP 目录数量及类型见 `index.json` 的 `archives`。MIT/OCW 与 OpenScore 大包只记目录；PDMX TAR 不展开。",
        "- 原始 PDF/JPG 的 OCR 由专用 OCR 流程处理；本脚本不读取或转换这些文件。",
        "- 失败、blocked、未取得、仅目录页、在线未缓存等状态见逐来源卡及原始 manifest。",
        "- 旧生成文章、模型输出、提示词、日志和临时文件不得作为可信资料；排除项列在 `index.json`。", "",
    ]
    (index_root / "index.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps(report["counts"] | {"omt_status": omt.get("status"), "omt_count": omt.get("count", 0), "omt_hash_matched": existing_omt.get("matched", 0), "dcml_count": dcml.get("count", 0), "dcml_reviewed_excluded": dcml.get("excluded_reviewed", 0)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
