from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess


def _repo_relative(repo_root: Path, path: Path) -> str:
    root = repo_root.resolve()
    target = path.resolve()
    return target.relative_to(root).as_posix()


def git_blob_bytes(repo_root: Path, path: Path, ref: str = "HEAD") -> bytes:
    relative = _repo_relative(repo_root, path)
    return subprocess.check_output(
        ["git", "-C", str(repo_root), "show", f"{ref}:{relative}"],
    )


def git_blob_sha256(repo_root: Path, path: Path, ref: str = "HEAD") -> str:
    return hashlib.sha256(git_blob_bytes(repo_root, path, ref=ref)).hexdigest()


def git_tracked_paths_utf8(repo_root: Path) -> list[str]:
    raw = subprocess.check_output(
        ["git", "-C", str(repo_root), "-c", "core.quotepath=false", "ls-files", "-z"],
    )
    return [part.decode("utf-8", errors="strict") for part in raw.split(b"\0") if part]
