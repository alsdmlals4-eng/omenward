#!/usr/bin/env python3
"""Route a protected product PR to Base's exact approved-change validator.

The project owns only the PR-local manifest selection rule: if protected files
changed, exactly one new or modified approval manifest must accompany them.
The Base validator remains the sole owner of approval schema, protected-path
comparison, and contract reconciliation.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


PROTECTED_PREFIXES = ("scripts/", "scenes/", "data/", "assets/", "addons/")
APPROVAL_DIRECTORY = Path("docs/approvals")
APPROVAL_PREFIX = "PROJECT_PROTECTED_CHANGE_APPROVAL_"


def _normalized(path: str) -> str:
    return path.replace("\\", "/")


def _git(project_root: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(project_root), *arguments],
        text=True,
        capture_output=True,
        check=False,
    )


def _is_protected(path: str) -> bool:
    normalized = _normalized(path)
    return normalized == "project.godot" or normalized.startswith(PROTECTED_PREFIXES)


def _is_approval_manifest(path: str) -> bool:
    candidate = Path(_normalized(path))
    return (
        candidate.parent == APPROVAL_DIRECTORY
        and candidate.name.startswith(APPROVAL_PREFIX)
        and candidate.suffix == ".json"
    )


def _changed_paths(project_root: Path, pr_base: str) -> list[str]:
    completed = _git(project_root, "diff", "--name-only", f"{pr_base}...HEAD")
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or "cannot read pull-request change set")
    return sorted(path for path in completed.stdout.splitlines() if path)


def _validate_pr_base(project_root: Path, pr_base: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", pr_base):
        raise ValueError("--pr-base must be an exact 40-character SHA")
    commit = _git(project_root, "cat-file", "-e", f"{pr_base}^{{commit}}")
    if commit.returncode != 0:
        raise ValueError("--pr-base must identify a project commit")
    ancestor = _git(project_root, "merge-base", "--is-ancestor", pr_base, "HEAD")
    if ancestor.returncode != 0:
        raise ValueError("--pr-base must be an ancestor of the checked-out PR head")


def _select_approval_manifest(project_root: Path, changed_paths: list[str]) -> str:
    manifests = [path for path in changed_paths if _is_approval_manifest(path)]
    if len(manifests) != 1:
        raise ValueError(
            "approved protected change requires exactly one changed approval manifest; "
            f"found={manifests}"
        )
    manifest = manifests[0]
    target = project_root / manifest
    if not target.is_file():
        raise ValueError(f"changed approval manifest is unavailable at PR head: {manifest}")
    return manifest


def validate(options: argparse.Namespace) -> int:
    project_root = options.project_root.resolve()
    base_repository = options.base_repository.resolve()
    _validate_pr_base(project_root, options.pr_base)
    if not re.fullmatch(r"[0-9a-f]{40}", options.protected_base):
        raise ValueError("--protected-base must be an exact 40-character SHA")

    changed_paths = _changed_paths(project_root, options.pr_base)
    protected_paths = [path for path in changed_paths if _is_protected(path)]
    if not protected_paths:
        print("NO_PROTECTED_PATHS: historical document-only CI remains authoritative")
        return 0

    approval = _select_approval_manifest(project_root, changed_paths)
    gate = base_repository / "tools" / "check_approved_project_operating_contract.py"
    if not gate.is_file():
        raise ValueError(f"Base approved protected-change gate is missing: {gate}")

    command = [
        sys.executable,
        str(gate),
        "--project-root",
        str(project_root),
        "--base-repository",
        str(base_repository),
        "--protected-base",
        options.protected_base,
        "--approval",
        approval,
        "--external-approval",
        options.external_approval,
        "--check",
    ]
    completed = subprocess.run(command, cwd=project_root, check=False)
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--base-repository", type=Path, required=True)
    parser.add_argument("--pr-base", required=True)
    parser.add_argument("--protected-base", required=True)
    parser.add_argument("--external-approval", choices=("true", "false"), required=True)
    options = parser.parse_args()
    try:
        return validate(options)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"Approved protected change CI validation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
