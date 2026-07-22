from __future__ import annotations

import json
import pathlib
import re
import subprocess
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
REPORT_MD = ROOT / "docs" / "_C1_ROULETTE_AUDIT_INPUT.md"
REPORT_JSON = ROOT / "docs" / "_C1_ROULETTE_AUDIT_INPUT.json"

TEXT_SUFFIXES = {
    ".md", ".gd", ".tscn", ".tres", ".json", ".py", ".yml", ".yaml",
    ".txt", ".cfg", ".godot", ".csv", ".ini", ".toml", ".ps1", ".sh",
}
SKIP_PARTS = {".git", ".godot", "assets", "vendor", "third_party"}
ROULETTE_TERMS = (
    "roulette", "룰렛", "spin", "reroll", "re-roll", "reel", "slot",
    "unitspawndefinition", "lucky", "럭키", "완성선", "중앙 가로줄",
    "중앙 줄", "판정 줄", "result storage", "결과 보관", "이동권",
)
STALE_TERMS = (
    "0001-phase-0-codex-plan-mode", "phase 0 plan mode", "구현 전",
    "existing_core_identified", "core_lock_pending_user_confirmation",
    "pending_user_confirmation", "codex/phase-0-godot-bootstrap",
    "roulettebound", "율비", "경계의 율", "은종성채", "무명야",
    "플레이 가능한 수직 슬라이스 구현 완료",
)
ACTIVE_PREFIXES = (
    "README.md", "AGENTS.md", "docs/ACTIVE_CONTEXT.md", "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md", "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md", "docs/DECISIONS_PENDING.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md", "docs/PROJECT_CORE.md",
    "docs/design/APPROVED_", "docs/PHASE_0_VALIDATION.md",
    "docs/VERTICAL_SLICE_VALIDATION.md", "scripts/", "scenes/", "data/",
    "resources/", "tests/", ".github/", "tools/",
)
HISTORICAL_PARTS = ("/archive/", "/work_orders/", "/proposals/", "/issues/", "/goals/")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def is_text(path: pathlib.Path) -> bool:
    relative = path.relative_to(ROOT)
    if any(part in SKIP_PARTS for part in relative.parts):
        return False
    return path.is_file() and (path.suffix.lower() in TEXT_SUFFIXES or path.name in {"README", "LICENSE"})


def category(relative: str) -> str:
    normalized = "/" + relative.replace("\\", "/")
    if any(part in normalized for part in HISTORICAL_PARTS):
        return "HISTORICAL"
    if relative.startswith(ACTIVE_PREFIXES):
        return "ACTIVE"
    return "REFERENCE_OR_OTHER"


def context(lines: list[str], indexes: set[int], radius: int = 2) -> list[dict[str, object]]:
    selected: list[dict[str, object]] = []
    emitted: set[int] = set()
    for index in sorted(indexes):
        for line_index in range(max(0, index - radius), min(len(lines), index + radius + 1)):
            if line_index in emitted:
                continue
            emitted.add(line_index)
            selected.append({"line": line_index + 1, "text": lines[line_index]})
    return selected


files: list[dict[str, object]] = []
roulette_files: list[dict[str, object]] = []
stale_files: list[dict[str, object]] = []
references: list[dict[str, object]] = []
broken_links: list[dict[str, object]] = []

for path in sorted(ROOT.rglob("*")):
    if not is_text(path):
        continue
    relative = path.relative_to(ROOT).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    lines = text.splitlines()
    lower_lines = [line.casefold() for line in lines]
    item = {"path": relative, "category": category(relative), "lines": len(lines), "bytes": len(text.encode("utf-8"))}
    files.append(item)

    roulette_hits: dict[str, list[int]] = defaultdict(list)
    stale_hits: dict[str, list[int]] = defaultdict(list)
    for index, lowered in enumerate(lower_lines):
        for term in ROULETTE_TERMS:
            if term.casefold() in lowered:
                roulette_hits[term].append(index + 1)
        for term in STALE_TERMS:
            if term.casefold() in lowered:
                stale_hits[term].append(index + 1)

    if roulette_hits:
        all_indexes = {line - 1 for values in roulette_hits.values() for line in values}
        include_full = (
            len(lines) <= 420
            and (
                "roulette" in relative.casefold()
                or relative.startswith(("scripts/", "tests/", "data/", "resources/"))
            )
        )
        roulette_files.append({
            **item,
            "hits": dict(roulette_hits),
            "context": context(lines, all_indexes, 3),
            "full_content": text if include_full else None,
        })

    if stale_hits:
        all_indexes = {line - 1 for values in stale_hits.values() for line in values}
        stale_files.append({
            **item,
            "hits": dict(stale_hits),
            "context": context(lines, all_indexes, 2),
        })

    if path.suffix.lower() == ".md":
        for line_number, line in enumerate(lines, 1):
            for raw_target in LINK_RE.findall(line):
                target = raw_target.split("#", 1)[0].strip()
                if not target or "://" in target or target.startswith(("mailto:", "#")):
                    continue
                resolved = (path.parent / target).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    continue
                exists = resolved.exists()
                record = {
                    "source": relative,
                    "source_category": category(relative),
                    "line": line_number,
                    "target": target,
                    "resolved": resolved.relative_to(ROOT).as_posix(),
                    "exists": exists,
                }
                references.append(record)
                if not exists:
                    broken_links.append(record)

inbound = defaultdict(list)
for reference in references:
    inbound[reference["resolved"]].append({
        "source": reference["source"],
        "source_category": reference["source_category"],
        "line": reference["line"],
    })

payload = {
    "base_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
    "counts": {
        "text_files": len(files),
        "roulette_related_files": len(roulette_files),
        "stale_term_files": len(stale_files),
        "markdown_references": len(references),
        "broken_links": len(broken_links),
    },
    "roulette_files": roulette_files,
    "stale_files": stale_files,
    "broken_links": broken_links,
    "inbound_references": dict(sorted(inbound.items())),
    "file_inventory": files,
}
REPORT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

md: list[str] = [
    "# C1 승인 룰렛 계약 복구 — 기계 수집 감사 입력",
    "",
    f"- 기준 커밋: `{payload['base_commit']}`",
    f"- 텍스트 파일: {len(files)}",
    f"- 룰렛 관련 파일: {len(roulette_files)}",
    f"- 구형 상태·명칭 후보 파일: {len(stale_files)}",
    f"- 마크다운 내부 참조: {len(references)}",
    f"- 깨진 내부 링크: {len(broken_links)}",
    "",
    "이 파일은 기계 수집 입력이다. ACTIVE/HISTORICAL 판정과 삭제 여부는 후속 사람이 검증한다.",
    "",
    "## 룰렛 관련 파일",
]
for entry in roulette_files:
    md.extend([
        "",
        f"### `{entry['path']}` — {entry['category']} / {entry['lines']} lines",
        "",
        "Hits: " + ", ".join(f"`{term}` {lines}" for term, lines in entry["hits"].items()),
        "",
        "```text",
    ])
    for line in entry["context"]:
        md.append(f"{line['line']:>5}: {line['text']}")
    md.append("```")
    if entry["full_content"] is not None:
        md.extend(["", "<details><summary>Full content</summary>", "", "```text", entry["full_content"], "```", "", "</details>"])

md.extend(["", "## 구형 상태·명칭 후보"])
for entry in stale_files:
    md.extend([
        "",
        f"### `{entry['path']}` — {entry['category']}",
        "",
        "Hits: " + ", ".join(f"`{term}` {lines}" for term, lines in entry["hits"].items()),
        "",
        "```text",
    ])
    for line in entry["context"]:
        md.append(f"{line['line']:>5}: {line['text']}")
    md.append("```")

md.extend(["", "## 깨진 내부 링크"])
if broken_links:
    for entry in broken_links:
        md.append(f"- `{entry['source']}:{entry['line']}` → `{entry['target']}` (`{entry['resolved']}`)")
else:
    md.append("- 없음")

md.extend(["", "## 파일 인벤토리"])
for item in files:
    md.append(f"- `{item['path']}` — {item['category']} / {item['lines']} lines / {item['bytes']} bytes")
REPORT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

for relative in ("tools/_collect_c1_roulette_audit.py", ".github/workflows/collect-c1-roulette-audit-once.yml"):
    path = ROOT / relative
    if path.exists():
        path.unlink()

run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "add", "-A")
run("git", "commit", "-m", "collect C1 roulette and stale-reference audit input")
run("git", "push", "origin", "HEAD:agent/c1-approved-roulette-contract-recovery")
