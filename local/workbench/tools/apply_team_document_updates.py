import hashlib, json
from pathlib import Path
ROOT=Path("E:/github/music-wiki/local")
STAGE=ROOT/"workbench/team-doc-updates"
TARGET=Path("E:/github/opencadenza-dev-doc/music-wiki-知识生产")
NAMES={"README.md","writing-rules.md","sources.md","score-pipeline.md","handover.md","progress.md"}
def sha(data): return hashlib.sha256(data).hexdigest()
rows=json.loads((STAGE/"apply-manifest.json").read_text(encoding="utf-8"))
if {r["name"] for r in rows} != NAMES: raise SystemExit("Unexpected target names")
pending=[]
for row in rows:
    name=row["name"]
    old=(TARGET/name).read_bytes()
    new=(STAGE/name).read_bytes()
    if sha(old) not in {row["expected_sha256"],sha(new)}: raise SystemExit(f"Concurrent change detected: {name}")
    pending.append((name,new,sha(old),sha(new)))
result=[]
for name,new,before,after in pending:
    if before!=after:
        tmp=TARGET/(name+".codex-revision-tmp")
        tmp.write_bytes(new)
        tmp.replace(TARGET/name)
    result.append({"file":str(TARGET/name),"before_sha256":before,"after_sha256":after,"verified":sha((TARGET/name).read_bytes())==after})
report=ROOT/"docs/实施记录/2026-10-28-预备轮/团队文档修订结果.json"
report.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"updated":len(result),"verified":all(r["verified"] for r in result)},ensure_ascii=False))
