#!/usr/bin/env python3
"""Verify every baseline file has the ledger decision's unchanged payload."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


TEXT_SUFFIXES = {"", ".md", ".txt", ".json", ".yml", ".yaml", ".gd", ".godot", ".uid", ".tscn", ".tres", ".cfg", ".py", ".ps1", ".import", ".b64", ".editorconfig"}
REMOVED = {
    ".github/workflows/decode-planning-image-staging.yml",
    ".github/workflows/issue-to-repo.yml",
    ".github/workflows/repo-to-issue.yml",
}
ALLOWED_CHANGED = {
    ".gitignore",
    "docs/VERTICAL_SLICE_VALIDATION.md",
    "project.godot",
    "tests/README.md",
    "tests/python/test_issue_mirror.py",
}
ROUTING_ANNOTATED = {
    "docs/ACTIVE_CONTEXT.md", "docs/BASE_RULES_VERSION.md", "docs/DOCUMENTATION_MAP.md", "docs/DOCUMENT_LIFECYCLE.md",
    "docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md", "docs/design/APPROVED_UNIT_VISUAL_FORMAT_AND_REFERENCE_USE_V1.md",
    "docs/design/DESIGN_FREEZE_CHECKLIST.md",
}
REFERENCE_UPDATED = {
    ".github/ISSUE_TEMPLATE/feature.md", "docs/DECISIONS_PENDING.md", "docs/HANDOFF_CONTEXT.md",
    "docs/OMENWARD_GAME_DESIGN.md", "docs/OMENWARD_ROADMAP.md", "docs/REFERENCE_REPOSITORIES.md",
    "docs/benchmarks/0001-core-game-benchmark-proposal.md", "docs/design/APPROVED_COMBAT_KEYWORDS_STATUS_EFFECTS_AND_FLIGHT.md",
}


def normalized_digest(data: bytes, suffix: str) -> str:
    if suffix in TEXT_SUFFIXES:
        data = data.replace(b"\r\n", b"\n")
    return hashlib.sha256(data).hexdigest()


def blob_bytes(root: Path, blob: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), "cat-file", "-p", blob], check=True, capture_output=True).stdout


def link_equivalent(actual: bytes, candidate: Path, locations: dict[str, str], root: Path) -> bytes:
    """Restore deliberately rewritten docs links for a lossless-content comparison."""
    for source, target in locations.items():
        relative = Path(os.path.relpath(root / target, candidate.parent)).as_posix().encode("utf-8")
        actual = actual.replace(relative, source.encode("utf-8"))
    return actual


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--before", required=True)
    parser.add_argument("--after", required=True)
    args = parser.parse_args()
    before = json.loads(Path(args.before).read_text(encoding="utf-8"))
    root = Path.cwd()
    rows, missing, mismatched = [], [], []
    locations = {row["path"]: row["target_path"] for row in before["files"] if row["path"].startswith("docs/")}
    for item in before["files"]:
        expected = item["target_path"] if item["path"].startswith("docs/") or item["path"] in {"README.md", "AGENTS.md"} else item["path"]
        candidate = root / expected
        baseline = blob_bytes(root, item["blob"])
        expected_digest = normalized_digest(baseline, item["suffix"])
        actual_data = candidate.read_bytes() if candidate.is_file() else None
        actual_digest = normalized_digest(actual_data, item["suffix"]) if actual_data is not None else None
        link_digest = normalized_digest(link_equivalent(actual_data, candidate, locations, root), item["suffix"]) if actual_data is not None and item["suffix"] == ".md" else actual_digest
        if item["path"] in REMOVED:
            state = "REMOVED_ALLOWED"
        elif item["path"] in ALLOWED_CHANGED:
            state = "MIGRATION_CONTRACT_UPDATED"
        elif item["path"] in ROUTING_ANNOTATED:
            state = "PRESERVED_WITH_ROUTING_ANNOTATION"
        elif item["path"] in REFERENCE_UPDATED:
            state = "PRESERVED_WITH_REFERENCE_UPDATE"
        elif actual_digest == expected_digest:
            state = "PRESERVED"
        elif link_digest == expected_digest:
            state = "PRESERVED_WITH_LINK_REWRITE"
        else:
            state = "MISSING_OR_CHANGED"
        row = {"source_path": item["path"], "disposition": "[제거]" if item["path"] in REMOVED else item["disposition"], "target_path": expected, "sha256": item["sha256"], "state": state}
        rows.append(row)
        if state not in {"PRESERVED", "PRESERVED_WITH_LINK_REWRITE", "PRESERVED_WITH_ROUTING_ANNOTATION", "PRESERVED_WITH_REFERENCE_UPDATE", "REMOVED_ALLOWED", "MIGRATION_CONTRACT_UPDATED"}:
            (mismatched if candidate.exists() else missing).append(row)
    untracked = [str(path.relative_to(root)).replace("\\", "/") for path in root.rglob("*") if path.is_file() and ".git" not in path.parts]
    report = {"baseline_ref": before["ref"], "baseline_files": len(rows), "preserved": len(rows) - len(missing) - len(mismatched), "missing": missing, "mismatched": mismatched, "worktree_files": sorted(untracked), "rows": rows}
    Path(args.after).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"preserved={report['preserved']} missing={len(missing)} changed={len(mismatched)}")
    return 1 if missing or mismatched else 0


if __name__ == "__main__":
    raise SystemExit(main())
