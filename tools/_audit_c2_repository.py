from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs/_C2_AUDIT_INPUT.md"
TEXT_SUFFIXES = {".gd", ".md", ".tres", ".tscn", ".py", ".yml", ".yaml", ".json", ".cfg", ".godot"}
KEY_TERMS = (
    "OutpostState",
    "GateState",
    "ClashZoneState",
    "clash_zones",
    "stage_victory",
    "stage_defeat",
    "capture_power",
    "begin_capture",
    "control_income",
    "outpost",
    "gate",
    "base_health",
    "headquarters",
    "본진",
    "성문",
    "접전지",
    "중간거점",
)
STALE_TERMS = (
    "C1 승인 룰렛 핵심 계약 구현·원격 검증 진행",
    "PR #49 사용자 검토와 병합 결정",
    "PR #49 병합",
    "[현재] 승인 룰렛 핵심 계약 복구",
    "현재 C1 시작 문서",
    "다음 변경은 게임 코드 전체가 아니라 승인 룰렛 계약 복구",
)
EXCLUDE_DIRS = {".git", ".godot"}


def is_text(path: pathlib.Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"project.godot", "README.md", "AGENTS.md"}


def relative(path: pathlib.Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> None:
    files = [path for path in ROOT.rglob("*") if path.is_file() and not any(part in EXCLUDE_DIRS for part in path.parts) and is_text(path)]
    files.sort(key=relative)
    relevant: list[tuple[str, list[str]]] = []
    stale: list[tuple[str, str, int]] = []
    broken_links: list[tuple[str, str]] = []

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        matched = [term for term in KEY_TERMS if term in text]
        if matched:
            relevant.append((relative(path), matched))
        for term in STALE_TERMS:
            for line_number, line in enumerate(text.splitlines(), start=1):
                if term in line:
                    stale.append((relative(path), term, line_number))
        if path.suffix.lower() == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                clean = target.split("#", 1)[0].strip()
                if not clean or "://" in clean or clean.startswith(("#", "mailto:")):
                    continue
                resolved = (path.parent / clean).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    continue
                if not resolved.exists():
                    broken_links.append((relative(path), clean))

    lines = [
        "# C2 repository audit input",
        "",
        f"- text files scanned: {len(files)}",
        f"- battle/objective relevant files: {len(relevant)}",
        f"- stale current-state occurrences: {len(stale)}",
        f"- broken internal Markdown links: {len(broken_links)}",
        "",
        "## Battle/objective relevant files",
        "",
    ]
    for path, terms in relevant:
        lines.append(f"- `{path}` — {', '.join(sorted(set(terms)))}")
    lines.extend(["", "## Headless tests", ""])
    for path in files:
        rel = relative(path)
        if rel.startswith("tests/headless/") and rel.endswith("_test.gd"):
            lines.append(f"- `{rel}`")
    lines.extend(["", "## Battle scripts", ""])
    for path in files:
        rel = relative(path)
        if rel.startswith("scripts/battle/"):
            lines.append(f"- `{rel}`")
    lines.extend(["", "## Stale current-state occurrences", ""])
    if stale:
        for path, term, line_number in stale:
            lines.append(f"- `{path}:{line_number}` — `{term}`")
    else:
        lines.append("- none")
    lines.extend(["", "## Broken internal Markdown links", ""])
    if broken_links:
        for path, target in broken_links:
            lines.append(f"- `{path}` -> `{target}`")
    else:
        lines.append("- none")
    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
