# -*- coding: utf-8 -*-
"""Verify downloaded score sources: format validity + basic coverage facts."""
import io, json, os, re, sys, zipfile
from pathlib import Path

ROOT = Path(r"E:\github\music-wiki\.agents\worktrees\dsh-ee5c71d0-e1b5\local\workbench\scores\score-r3\downloads")
out = []

def xml_summary(raw: bytes):
    txt = raw.decode("utf-8", "replace")
    measures = len(re.findall(r"<measure\b", txt))
    parts = len(re.findall(r"<score-part\b", txt))
    title = re.search(r"<movement-title>([^<]*)</movement-title>", txt)
    wtitle = re.search(r"<work-title>([^<]*)</work-title>", txt)
    ident = re.findall(r"<part-name[^>]*>([^<]*)</part-name>", txt)
    return dict(measures=measures, parts=parts,
                title=(title.group(1) if title else (wtitle.group(1) if wtitle else "")),
                instruments=[i.strip() for i in ident][:14])

for p in sorted(ROOT.rglob("*")):
    if not p.is_file():
        continue
    rel = p.relative_to(ROOT)
    size = p.stat().st_size
    ext = p.suffix.lower()
    rec = dict(slug=rel.parts[0], name=p.name, bytes=size)
    try:
        if ext == ".mxl":
            with zipfile.ZipFile(p) as z:
                names = z.namelist()
                rec["zip_ok"] = True
                rec["members"] = names[:6]
                container = next((n for n in names if n.endswith("container.xml")), None)
                score = next((n for n in names if n.endswith((".xml", ".musicxml")) and "container" not in n and "META-INF" not in n), None)
                rec["has_container"] = bool(container)
                if score:
                    raw = z.read(score)
                    rec.update(xml_summary(raw))
                rec["valid"] = bool(container and score)
        elif ext == ".md2":
            txt = p.read_text("utf-8", "replace")
            rec["valid"] = ("WK#" in txt or "@filename" in txt) and "M:" in txt
            wk = re.search(r"WK#:(\S+)", txt)
            mv = re.search(r"MV#:(\S+)", txt)
            rec["wk"] = wk.group(1) if wk else None
            rec["mv"] = mv.group(1) if mv else None
            # count measure records: lines starting with '=' (barline markers) in MuseData streams
            rec["barlines"] = len([l for l in txt.splitlines() if l.startswith("=")])
            rec["source_line"] = (re.search(r"(Breitkopf[^\r\n]*)", txt).group(1).strip() if re.search(r"(Breitkopf[^\r\n]*)", txt) else "")
        elif ext == ".krn":
            txt = p.read_text("utf-8", "replace")
            rec["valid"] = "**kern" in txt
            rec["spines"] = txt.count("**kern")
            rec["barlines"] = len([l for l in txt.splitlines() if l.startswith("=")])
            m = re.search(r"!!!OTL:\s*(.+)", txt)
            rec["otl"] = m.group(1).strip() if m else ""
        elif ext == ".abc":
            txt = p.read_text("utf-8", "replace")
            rec["valid"] = "X:" in txt and "K:" in txt
        else:
            rec["valid"] = False
    except Exception as e:
        rec["valid"] = False
        rec["error"] = repr(e)
    out.append(rec)

Path(r"E:\github\music-wiki\.agents\worktrees\dsh-ee5c71d0-e1b5\local\workbench\scores\score-r3\verify.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
bad = [r for r in out if not r.get("valid")]
print("\n=== INVALID:", len(bad), "===")
for r in bad:
    print(" ", r["slug"], r["name"], r.get("error", ""))
print("\n=== totals ===", len(out), "files", sum(r["bytes"] for r in out), "bytes")

