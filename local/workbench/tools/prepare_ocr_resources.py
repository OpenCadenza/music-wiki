#!/usr/bin/env python3
"""Preprocess trusted incoming PDFs and JPGs with the pinned EverythingMarkdown cloud OCR."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
SOURCE_ROOT = ROOT / "local" / "origin_resources"
OUTPUT_ROOT = ROOT / "local" / "resources" / "text" / "ocr"
TOOL_ROOT = Path(r"C:\Users\ThinkBook\workspace\文档转换与OCR\EverythingMarkdown")
sys.path.insert(0, str(TOOL_ROOT / "src"))

MODEL = "PaddleOCR-VL-1.6"
MAX_PAGES = 1000
JOB_LOG = ROOT / "local" / "workbench" / "ocr-runtime" / "submitted-jobs.jsonl"
APPDATA_PACKAGES = Path(r"C:\Users\ThinkBook\AppData\Roaming\Python\Python314\site-packages")
if APPDATA_PACKAGES.is_dir():
    sys.path.insert(0, str(APPDATA_PACKAGES))


def page_count(path: Path) -> int:
    if path.suffix.lower() != ".pdf":
        return 1
    # Poppler ships with this Codex runtime and counts PDF pages without OCR.
    exe = Path(r"C:\Users\ThinkBook\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe")
    if not exe.is_file():
        raise RuntimeError("pdfinfo is unavailable; refusing to guess PDF page count")
    result = subprocess.run([str(exe), str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    if result.returncode:
        raise RuntimeError(f"pdfinfo failed (exit {result.returncode})")
    for line in result.stdout.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise RuntimeError("pdfinfo did not report a page count")


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def source_files():
    extensions = {".pdf", ".jpg", ".jpeg"}
    return sorted((p for p in SOURCE_ROOT.rglob('*') if p.is_file() and p.suffix.lower() in extensions and 'raw' in p.relative_to(SOURCE_ROOT).parts), key=lambda p: (p.stat().st_size, p.relative_to(SOURCE_ROOT).as_posix()))


def read_job_events():
    events = []
    if JOB_LOG.is_file():
        for line in JOB_LOG.read_text(encoding="utf-8").splitlines():
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return events


def append_job_event(event):
    JOB_LOG.parent.mkdir(parents=True, exist_ok=True)
    with JOB_LOG.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(event, ensure_ascii=False) + "\n")


def cached_outputs_match(metadata_path: Path, source_sha: str, range_labels: list[str]):
    try:
        old = json.loads(metadata_path.read_text(encoding="utf-8"))
        if (old.get("status") not in {"converted_readable", "converted_image_only"}
                or old.get("source_sha256") != source_sha
                or old.get("model") != MODEL
                or old.get("page_ranges") != range_labels):
            return None
        outputs = old.get("outputs") or []
        if len(outputs) != len(range_labels):
            return None
        for output in outputs:
            md = ROOT / output["markdown"]
            jsonl = ROOT / output["jsonl"] if output.get("jsonl") else None
            images = ROOT / output["images_dir"]
            if not md.is_file() or not md.read_text(encoding="utf-8-sig").strip():
                return None
            if jsonl and (not jsonl.is_file() or jsonl.stat().st_size == 0):
                return None
            if not images.is_dir():
                return None
        return old
    except (OSError, ValueError, KeyError, TypeError):
        return None


def blocking_reason(exc: Exception):
    message = f"{type(exc).__name__}: {exc}".lower()
    markers = (
        "proxyerror", "connectionerror", "connectionreseterror", "remotedisconnected",
        "unable to connect", "winerror 10013",
        "network is unreachable", "name or service not known", "timed out",
        "daily quota", "quota exceeded", "quota", "rate limit", "rate-limit",
        "too many requests", "http 401", "http 403", "http 429",
        "code=401", "code=403", "code=429", "unauthorized", "forbidden",
        "配额", "限流", "日额度",
    )
    if any(marker in message for marker in markers):
        return str(exc)[:1200]
    return None


def install_get_retries(cloud_api):
    """Retry transient GET connection failures only, at most three times."""
    requests = cloud_api.requests
    original_requests_get = requests.get
    original_session_get = requests.Session.get
    counter = {"count": 0}

    def wrap_get(original):
        def retrying_get(*args, **kwargs):
            for attempt in range(4):  # initial request plus at most three reconnects
                try:
                    return original(*args, **kwargs)
                except (requests.ConnectionError, requests.Timeout) as exc:
                    message = str(exc).lower()
                    permanent = any(token in message for token in (
                        "proxyerror", "winerror 10013", "unauthorized", "forbidden",
                        "quota", "rate limit", "too many requests", "http 401",
                        "http 403", "http 429", "code=429",
                    ))
                    if permanent or attempt == 3:
                        raise
                    counter["count"] += 1
                    time.sleep(1 + attempt)
        return retrying_get

    requests.get = wrap_get(original_requests_get)
    requests.Session.get = wrap_get(original_session_get)

    def restore():
        requests.get = original_requests_get
        requests.Session.get = original_session_get

    return restore, counter


def process(path: Path, dry_run: bool, network_error: str | None = None,
            retry_uncertain: bool = False):
    rel = path.relative_to(SOURCE_ROOT).as_posix()
    parts = Path(rel).parts
    source_name = parts[1] if len(parts) >= 4 else path.parent.parent.name
    doc_name = path.stem
    out_dir = OUTPUT_ROOT / source_name / doc_name
    metadata_path = out_dir / "conversion.json"
    source_sha = digest(path)
    record = {
        "source_path": rel,
        "source_sha256": source_sha,
        "model": MODEL,
        "page_count": None,
        "page_ranges": [],
        "status": "planned" if dry_run else "pending",
        "outputs": [],
        "score_ocr_note": "For scores and manuscript images, OCR text/layout is not reliable note encoding.",
    }
    last_job = {"value": None, "page_range": None}
    try:
        count = page_count(path)
        record["page_count"] = count
        ranges = [(start, min(start + MAX_PAGES - 1, count)) for start in range(1, count + 1, MAX_PAGES)] if path.suffix.lower() == ".pdf" else [(None, None)]
        range_labels = [f"{a}-{b}" if a is not None else "image" for a, b in ranges]
        record["page_ranges"] = range_labels
        if dry_run:
            return record
        cached = cached_outputs_match(metadata_path, source_sha, range_labels)
        if cached:
            return cached
        if network_error:
            record["status"] = "not_attempted_network_unavailable"
            record["network_error"] = network_error
            out_dir.mkdir(parents=True, exist_ok=True)
            metadata_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            return record
        matching_events = [e for e in read_job_events()
                           if e.get("source_path") == rel
                           and e.get("source_sha256") == source_sha
                           and e.get("model") == MODEL
                           and e.get("page_range") in range_labels]
        latest_by_range = {}
        for event in matching_events:
            latest_by_range[event["page_range"]] = event
        uncertain = [e for e in latest_by_range.values()
                     if e.get("status") in {"uncertain_submission", "uncertain_submission_retry_started"}]
        if uncertain and not retry_uncertain:
            record["status"] = "submission_uncertain"
            record["error"] = uncertain[-1].get("error", "Previous POST ended without a jobId")
            out_dir.mkdir(parents=True, exist_ok=True)
            metadata_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            return record
        if uncertain and retry_uncertain:
            record["uncertainty_retries"] = []
            for event in uncertain:
                retry_event = {"source_path": rel, "source_sha256": source_sha,
                               "model": MODEL, "page_range": event["page_range"],
                               "job_id": None, "status": "uncertain_submission_retry_started",
                               "reason": "An explicit one-document retry was authorized after a prior connection reset without a returned jobId.",
                               "previous_error": event.get("error"),
                               "recorded_at_epoch": time.time()}
                append_job_event(retry_event)
                record["uncertainty_retries"].append(retry_event)
        out_dir.mkdir(parents=True, exist_ok=True)
        from everythingmarkdown import cloud_api
        job_events = read_job_events()
        for start, end in ranges:
            original_submit = cloud_api.submit_file
            page_range = f"{start}-{end}" if start is not None else "image"
            latest_by_job = {}
            for event in job_events:
                if (event.get("source_path") == rel
                        and event.get("source_sha256") == source_sha
                        and event.get("model") == MODEL
                        and event.get("page_range") == page_range
                        and event.get("job_id")):
                    latest_by_job[event["job_id"]] = event
            matching_jobs = [e for e in latest_by_job.values()
                             if e.get("status") in {"submitted", "completed"}]
            resume_job = matching_jobs[-1] if matching_jobs else None
            current_job = {"value": None}
            def tracked_submit(*args, **kwargs):
                if resume_job:
                    job_id = resume_job["job_id"]
                    event = dict(resume_job, resumed_at_epoch=time.time())
                    event["status"] = "submitted"
                else:
                    try:
                        job_id = original_submit(*args, **kwargs)
                    except (cloud_api.requests.ConnectionError, cloud_api.requests.Timeout) as exc:
                        message = str(exc)[:1200]
                        append_job_event({"source_path": rel, "source_sha256": source_sha,
                                          "model": MODEL, "page_range": page_range,
                                          "job_id": None, "status": "uncertain_submission",
                                          "error": message, "recorded_at_epoch": time.time()})
                        record["status"] = "submission_uncertain"
                        record["error"] = message
                        metadata_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                        raise
                    event = {"source_path": rel, "source_sha256": source_sha,
                             "model": MODEL, "page_range": page_range,
                             "job_id": job_id, "status": "submitted",
                             "submitted_at_epoch": time.time()}
                append_job_event(event)
                current_job["value"] = job_id
                last_job["value"] = job_id
                last_job["page_range"] = page_range
                record.setdefault("job_ids", []).append(job_id)
                record["status"] = "submitted"
                metadata_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
                return job_id
            cloud_api.submit_file = tracked_submit
            segment_dir = out_dir if start is None or (start == 1 and end == count) else out_dir / f"pages_{start:04d}-{end:04d}"
            segment_dir.mkdir(parents=True, exist_ok=True)
            restore_get, retry_counter = install_get_retries(cloud_api)
            record["get_retry_count"] = record.get("get_retry_count", 0)
            try:
                result = cloud_api.convert_file(
                    str(path), model=MODEL, out_dir=str(segment_dir),
                    page_ranges=f"{start}-{end}" if start is not None and count > MAX_PAGES else None,
                    keep_json=True,
                )
                if current_job["value"]:
                    append_job_event({"source_path": rel, "source_sha256": source_sha,
                                      "model": MODEL, "page_range": page_range,
                                      "job_id": current_job["value"], "status": "completed",
                                      "completed_at_epoch": time.time()})
            finally:
                cloud_api.submit_file = original_submit
                restore_get()
                record["get_retry_count"] += retry_counter["count"]
            record["outputs"].append({
                "page_range": f"{start}-{end}" if start is not None else "image",
                "markdown": Path(result["md_path"]).relative_to(ROOT).as_posix(),
                "jsonl": Path(result["jsonl_path"]).relative_to(ROOT).as_posix() if result.get("jsonl_path") else None,
                "images_dir": Path(result["images_dir"]).relative_to(ROOT).as_posix(),
                "image_count": result["image_count"],
                "elapsed_s": result["elapsed_s"],
                "status": "converted_readable",
            })
        record["status"] = "converted_readable"
    except Exception as exc:
        # Keep failures visible and finite; this script never retries automatically.
        if record.get("status") != "submission_uncertain":
            record["status"] = "failed"
        record["error_type"] = type(exc).__name__
        record["error"] = str(exc)[:1200]
        if last_job["value"] and "job failed:" in str(exc).lower():
            append_job_event({"source_path": rel, "source_sha256": source_sha,
                              "model": MODEL, "page_range": last_job["page_range"],
                              "job_id": last_job["value"], "status": "failed",
                              "error": str(exc)[:1200], "failed_at_epoch": time.time()})
        stop_reason = blocking_reason(exc)
        if stop_reason and record["status"] != "submission_uncertain":
            record["stop_batch_reason"] = stop_reason
    if not dry_run:
        out_dir.mkdir(parents=True, exist_ok=True)
        metadata_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return record


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run", action="store_true", help="submit OCR jobs; default is a read-only page-count plan")
    parser.add_argument("--only", action="append", help="process only these source-relative paths (repeatable)")
    parser.add_argument("--record-network-block", help="record documents as unattempted due to a known network block")
    parser.add_argument("--skip", action="append", default=[], help="exclude a source-relative path")
    parser.add_argument("--retry-uncertain", action="store_true", help="retry a prior no-jobId submission only for one explicitly selected document")
    args = parser.parse_args()
    if args.retry_uncertain and (not args.only or len(args.only) != 1):
        parser.error("--retry-uncertain requires exactly one --only source-relative path")
    files = source_files()
    if args.only:
        files = [p for p in files if p.relative_to(SOURCE_ROOT).as_posix() in args.only]
    if args.skip:
        files = [p for p in files if p.relative_to(SOURCE_ROOT).as_posix() not in args.skip]
    rows = []
    blocked = args.record_network_block
    for path in files:
        row = process(path, dry_run=not args.run and not blocked, network_error=blocked,
                      retry_uncertain=args.retry_uncertain)
        rows.append(row)
        if row.get("stop_batch_reason") and blocked is None:
            blocked = row["stop_batch_reason"]
    print(json.dumps({"total_files": len(rows), "pdfs": sum(Path(r["source_path"]).suffix.lower()==".pdf" for r in rows), "images": sum(Path(r["source_path"]).suffix.lower() in {".jpg",".jpeg"} for r in rows), "total_pdf_pages": sum(r.get("page_count") or 0 for r in rows if Path(r["source_path"]).suffix.lower()==".pdf"), "rows": rows}, ensure_ascii=False, indent=2))
    if args.run and any(r["status"] == "failed" for r in rows):
        raise SystemExit(2)


if __name__ == "__main__":
    main()
