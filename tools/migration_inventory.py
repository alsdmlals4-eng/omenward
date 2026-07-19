#!/usr/bin/env python3
"""Create a deterministic, file-level migration inventory for a Git ref."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True).stdout


def headings(data: bytes) -> list[str]:
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return []
    return [line.lstrip("#").strip() for line in text.splitlines() if line.startswith(("# ", "## "))]


def classification(path: str) -> tuple[str, str]:
    """Return the mandatory preservation decision and post-migration home."""
    appendix = "[기획서]/02_게임_디자인/등록_부록"
    if path.startswith("docs/archive/"):
        return "[백업]", "[기획서]/[백업]/omenward/" + path.removeprefix("docs/archive/")
    if path.startswith(("docs/design/proposals/", "docs/design/notes/", "docs/proposals/")):
        return "[보류]", "[기획서]/[보류]/omenward/" + path.removeprefix("docs/")
    if path.startswith(("docs/issues/", "docs/goals/", "docs/work_orders/", "docs/superpowers/")):
        return "[백업]", "[기획서]/[백업]/omenward/" + path.removeprefix("docs/")
    if path.startswith("docs/benchmarks/"):
        return "[등록 부록]", "[기획서]/10_분석_유저리서치/등록_부록/" + path.removeprefix("docs/benchmarks/")
    if path.startswith("docs/images/"):
        return "[증거]", "[기획서]/06_아트/증거/" + path.removeprefix("docs/images/")
    if path.startswith("docs/design/"):
        name = Path(path).name
        if any(token in name for token in ("ART_", "VISUAL", "ANIMATION", "BATTLEFIELD", "BELLU")):
            appendix = "[기획서]/06_아트/등록_부록"
        elif any(token in name for token in ("UI_", "DOPAMINE", "TUTORIAL")):
            appendix = "[기획서]/03_UX_UI_접근성/등록_부록"
        elif "PERFORMANCE" in name:
            appendix = "[기획서]/04_개발_엔지니어링/등록_부록"
        return "[등록 부록]", appendix + "/" + name
    direct = {
        "docs/OMENWARD_GAME_DESIGN.md": "[기획서]/02_게임_디자인/등록_부록/OMENWARD_GAME_DESIGN.md",
        "docs/GODOT_PROJECT_STRUCTURE.md": "[기획서]/04_개발_엔지니어링/등록_부록/GODOT_PROJECT_STRUCTURE.md",
        "docs/PHASE_0_VALIDATION.md": "[기획서]/08_QA/등록_부록/PHASE_0_VALIDATION.md",
        "docs/VERTICAL_SLICE_VALIDATION.md": "[기획서]/08_QA/등록_부록/VERTICAL_SLICE_VALIDATION.md",
        "docs/OMENWARD_ROADMAP.md": "[기획서]/09_프로덕션_PM/등록_부록/OMENWARD_ROADMAP.md",
        "docs/HANDOFF_CONTEXT.md": "[기획서]/09_프로덕션_PM/등록_부록/HANDOFF_CONTEXT.md",
    }
    if path in direct:
        return "[등록 부록]", direct[path]
    if path.startswith("docs/"):
        return "[백업]", "[기획서]/[백업]/omenward/root-docs/" + path.removeprefix("docs/")
    if path in {"README.md", "AGENTS.md"}:
        return "[백업]", "[기획서]/[백업]/omenward/root/" + path
    return "[증거]", path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ref", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--move-documents", action="store_true", help="move baseline docs to their ledger destinations")
    args = parser.parse_args()
    root = Path.cwd()
    rows = []
    for raw in git(root, "ls-tree", "-r", "-z", args.ref).split(b"\0"):
        if not raw:
            continue
        meta, raw_path = raw.split(b"\t", 1)
        mode, kind, blob = meta.decode("ascii").split()
        path = raw_path.decode("utf-8")
        data = git(root, "cat-file", "-p", blob) if kind == "blob" else b""
        disposition, target_path = classification(path)
        rows.append({
            "path": path, "mode": mode, "blob": blob, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(), "suffix": Path(path).suffix.lower(),
            "headings": headings(data), "disposition": disposition, "target_path": target_path,
        })
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"ref": args.ref, "files": rows}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.move_documents:
        moved = 0
        for row in rows:
            source = root / row["path"]
            target = root / row["target_path"]
            if not row["path"].startswith("docs/") or not source.exists() or source == target:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                raise FileExistsError(f"refusing to overwrite: {target}")
            shutil.move(str(source), str(target))
            moved += 1
        print(f"Moved {moved} baseline documentation file(s) to ledger destinations.")
    print(f"Inventoried {len(rows)} file(s) from {args.ref}.")


if __name__ == "__main__":
    raise SystemExit(main())
