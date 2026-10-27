import argparse, hashlib, json, os, time
from pathlib import Path

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--report-dir", required=True)
    parser.add_argument("--runtime-dir", required=True)
    args = parser.parse_args()
    source = Path(args.source).resolve()
    target = Path(args.target).resolve()
    workspace = Path("E:/github/music-wiki/local").resolve()
    if not target.is_relative_to(workspace) or target == workspace:
        raise SystemExit("Target is outside the intended workspace")
    records = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    report_dir, runtime = Path(args.report_dir), Path(args.runtime_dir)
    report_dir.mkdir(parents=True, exist_ok=True)
    runtime.mkdir(parents=True, exist_ok=True)
    mismatches, verified, total_bytes = [], 0, 0
    started = time.time()
    progress_path = runtime / "verify-progress.json"
    def progress(status):
        progress_path.write_text(json.dumps({"status": status, "checked": verified, "total": len(records), "bytes": total_bytes, "mismatches": len(mismatches), "elapsed_s": round(time.time()-started, 1)}, ensure_ascii=False, indent=2), encoding="utf-8")
    progress("running")
    with (report_dir / "导入摘要清单.jsonl").open("w", encoding="utf-8", newline="\n") as out:
        for row in records:
            rel = row["path"]
            left, right = source / rel, target / rel
            if not left.is_file() or not right.is_file():
                mismatches.append({"path": rel, "reason": "missing_or_not_file"})
                continue
            left_size, right_size = left.stat().st_size, right.stat().st_size
            a, b = digest(left), digest(right)
            valid = left_size == right_size == row["bytes"] and a == b
            out.write(json.dumps({"path": rel, "bytes": right_size, "sha256": a, "target_sha256": b, "match": valid}, ensure_ascii=False) + "\n")
            if not valid:
                mismatches.append({"path": rel, "reason": "size_or_digest_mismatch"})
            verified += 1
            total_bytes += right_size
            if verified % 100 == 0:
                out.flush()
                progress("running")
    present = {p.relative_to(target).as_posix() for p in target.rglob("*") if p.is_file()}
    expected = {r["path"] for r in records}
    extras = sorted(present - expected)
    missing = sorted(expected - present)
    result = {"status": "verified" if not mismatches and not extras and not missing else "failed", "source": str(source), "target": str(target), "files": verified, "bytes": total_bytes, "mismatches": mismatches, "extra_paths": extras, "missing_paths": missing, "elapsed_s": round(time.time()-started, 1)}
    (report_dir / "原始资料导入结果.json").write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    progress(result["status"])
    print(json.dumps({k:v for k,v in result.items() if k not in ("mismatches","extra_paths","missing_paths")},ensure_ascii=False), flush=True)
    return 0 if result["status"] == "verified" else 1

if __name__ == "__main__":
    raise SystemExit(main())
