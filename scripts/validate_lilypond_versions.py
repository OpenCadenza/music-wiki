#!/usr/bin/env python3
"""Enforce the published knowledge-base LilyPond version policy."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys


TARGET_VERSION = "2.26.0"
OPEN_FENCE = re.compile(r"^[ ]{0,3}```(lilypond|ly)(?:[ \t]+[^\r\n]*)?\r?$")
CLOSE_FENCE = re.compile(r"^[ ]{0,3}```[ \t]*\r?$")
EXAMPLE_METADATA = re.compile(
    r"<!--\s*opusloom:example\s*(\{.*?\})\s*-->", re.DOTALL
)
VERSION_DECLARATION = re.compile(
    r'\\version\s+"([^"]+)"', re.IGNORECASE
)


def iter_markdown(root: Path) -> list[Path]:
    if root.is_file():
        return [root] if root.suffix.lower() == ".md" else []
    return sorted(
        path for path in root.rglob("*.md")
        if ".git" not in path.parts
    )


def code_blocks(text: str):
    """Yield (opening line, closing line, language, code, block index)."""
    lines = text.splitlines(keepends=True)
    index = 0
    block_number = 0
    while index < len(lines):
        opening = OPEN_FENCE.fullmatch(lines[index].rstrip("\r\n"))
        if not opening:
            index += 1
            continue
        block_number += 1
        language = opening.group(1).lower()
        start = index + 1
        index = start
        while (
            index < len(lines)
            and not CLOSE_FENCE.fullmatch(lines[index].rstrip("\r\n"))
        ):
            index += 1
        if index >= len(lines):
            yield start, None, language, "".join(lines[start:]), block_number
            return
        yield start, index + 1, language, "".join(lines[start:index]), block_number
        index += 1


def metadata_for_block(text: str, block_start: int, block_end: int):
    """Return metadata immediately preceding a code block, if present."""
    before = text[:block_start]
    matches = list(EXAMPLE_METADATA.finditer(before))
    if not matches:
        return None
    metadata_match = matches[-1]
    if "```" in before[metadata_match.end():]:
        return None
    return metadata_match


def validate_file(path: Path, root: Path) -> tuple[list[str], int]:
    text = path.read_text(encoding="utf-8")
    display_path = path.relative_to(root).as_posix() if path != root else path.name
    errors: list[str] = []
    blocks = list(code_blocks(text))
    for start, end, _language, code, block_number in blocks:
        if end is None:
            errors.append(
                f"{display_path}:{start}: unclosed LilyPond code fence"
            )
            continue
        versions = VERSION_DECLARATION.findall(code)
        if not versions:
            errors.append(
                f"{display_path}:{start}: LilyPond block {block_number} "
                f'is missing \\version "{TARGET_VERSION}"'
            )
        for version in versions:
            if version != TARGET_VERSION:
                errors.append(
                    f"{display_path}:{start}: LilyPond block {block_number} "
                    f'declares \\version "{version}", expected "{TARGET_VERSION}"'
                )

        metadata_match = metadata_for_block(text, start, end)
        if not metadata_match:
            continue
        try:
            metadata = json.loads(metadata_match.group(1))
        except ValueError as exc:
            errors.append(
                f"{display_path}:{start}: invalid opusloom metadata: {exc}"
            )
            continue
        target = metadata.get("target_version")
        if target != TARGET_VERSION:
            example_id = metadata.get("id", "<missing-id>")
            errors.append(
                f"{display_path}:{start}: example {example_id} has "
                f"target_version={target!r}, expected {TARGET_VERSION!r}"
            )
    return errors, len(blocks)


def validate(root: Path) -> dict:
    files = iter_markdown(root)
    errors: list[str] = []
    blocks = 0
    for path in files:
        file_errors, file_blocks = validate_file(path, root)
        errors.extend(file_errors)
        blocks += file_blocks
    return {
        "ok": not errors,
        "target_version": TARGET_VERSION,
        "markdown_files": len(files),
        "lilypond_blocks": blocks,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[3] / "references-origin",
        help="Markdown file or directory to validate",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    if not root.exists():
        parser.error(f"validation root does not exist: {root}")
    report = validate(root)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
