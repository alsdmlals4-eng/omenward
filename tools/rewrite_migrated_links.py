#!/usr/bin/env python3
"""Rewrite absolute-in-repository legacy docs links after the Omenward migration."""

from __future__ import annotations

import json
import os
import re
from pathlib import Path


ROOT = Path.cwd()
LEDGER = ROOT / "[기획서]" / "00_프로젝트_허브" / "MIGRATION_INVENTORY_BEFORE.json"
SKIP = {"[백업]", "[보류]"}
PATTERN = re.compile(r"(?<![\w/])(docs/[A-Za-z0-9_./-]+(?:\.md|\.png|\.jpg|\.json))")


def main() -> int:
    entries = json.loads(LEDGER.read_text(encoding="utf-8"))["files"]
    locations = {row["path"]: row["target_path"] for row in entries if row["path"].startswith("docs/")}
    changed = 0
    for file in ROOT.rglob("*.md"):
        if any(part in SKIP for part in file.parts):
            continue
        text = file.read_text(encoding="utf-8")

        def replace(match: re.Match[str]) -> str:
            destination = locations.get(match.group(1))
            if not destination:
                return match.group(1)
            return Path(os.path.relpath(ROOT / destination, file.parent)).as_posix()

        rewritten = PATTERN.sub(replace, text)
        if rewritten != text:
            file.write_text(rewritten, encoding="utf-8")
            changed += 1
    print(f"Rewrote legacy links in {changed} active Markdown file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
