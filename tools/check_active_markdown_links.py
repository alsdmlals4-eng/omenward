#!/usr/bin/env python3
"""Fail if an active Markdown link resolves outside the migrated project tree."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path.cwd()
EXCLUDED = {"[백업]", "[보류]"}
LINK = re.compile(r"(?<!!)\[[^]]*\]\(([^)#]+)(?:#[^)]+)?\)")


def main() -> int:
    failures: list[str] = []
    for source in ROOT.rglob("*.md"):
        if ".git" in source.parts or any(part in EXCLUDED for part in source.parts):
            continue
        text = source.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (source.parent / target).resolve()
            if not resolved.exists() or ROOT.resolve() not in resolved.parents and resolved != ROOT.resolve():
                failures.append(f"{source.relative_to(ROOT)} -> {target}")
    if failures:
        print("Broken active Markdown links:\n" + "\n".join(failures))
        return 1
    print("Active Markdown links: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
