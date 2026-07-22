from __future__ import annotations

import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
INPUT = ROOT / "docs" / "_C1_ROULETTE_AUDIT_INPUT.json"
OUTPUT = ROOT / "docs" / "_C1_ROULETTE_SHORTLIST.md"
CANONICAL = {
    "docs/design/APPROVED_ROULETTE_CORE_RULES.md",
    "docs/design/APPROVED_ROULETTE_PROBABILITY_TARGETS_POC_V1.md",
    "docs/design/APPROVED_UNIT_GRADE_AND_ABILITY_GROWTH.md",
    "docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md",
    "docs/design/APPROVED_BUILDINGS_TACTICAL_MERCENARY_POC_V1.md",
}
CODE_PREFIXES = ("scripts/", "tests/", "data/", "resources/", "scenes/", ".github/workflows/")


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


payload = json.loads(INPUT.read_text(encoding="utf-8"))
roulette = {entry["path"]: entry for entry in payload["roulette_files"]}
stale = payload["stale_files"]
inbound = payload["inbound_references"]

selected_paths = sorted(
    path for path in roulette
    if (path in CANONICAL or path.startswith(CODE_PREFIXES)) and (ROOT / path).is_file()
)

lines: list[str] = [
    "# C1 승인 룰렛 계약 복구 — 구현·정본 Shortlist",
    "",
    f"- 기준: `{payload['base_commit']}`",
    f"- 선택 파일: {len(selected_paths)}",
    "",
    "## 선택 경로",
]
for path in selected_paths:
    entry = roulette[path]
    lines.append(f"- `{path}` — {entry['category']} / {entry['lines']} lines")

for path in selected_paths:
    source = ROOT / path
    text = source.read_text(encoding="utf-8")
    lines.extend([
        "",
        f"## `{path}`",
        "",
        f"Category: `{roulette[path]['category']}` / {len(text.splitlines())} lines",
        "",
        "```text",
        text,
        "```",
    ])

lines.extend(["", "## 활성 파일의 구형 상태·명칭 후보"])
active_stale = [entry for entry in stale if entry["category"] == "ACTIVE" and (ROOT / entry["path"]).is_file()]
for entry in active_stale:
    lines.extend([
        "",
        f"### `{entry['path']}`",
        "",
        "Hits: " + ", ".join(f"`{term}` {numbers}" for term, numbers in entry["hits"].items()),
        "",
        "```text",
    ])
    for context in entry["context"]:
        lines.append(f"{context['line']:>5}: {context['text']}")
    lines.append("```")

lines.extend(["", "## 역사·Work Order·Proposal로 향하는 활성 마크다운 참조"])
count = 0
for target, sources in inbound.items():
    normalized = "/" + target
    if not any(part in normalized for part in ("/archive/", "/work_orders/", "/proposals/", "/issues/", "/goals/")):
        continue
    active_sources = [source for source in sources if source["source_category"] == "ACTIVE"]
    if not active_sources:
        continue
    count += 1
    lines.append(f"- target `{target}`")
    for source in active_sources:
        lines.append(f"  - `{source['source']}:{source['line']}`")
if count == 0:
    lines.append("- 없음")

OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

for relative in (
    "tools/_extract_c1_roulette_shortlist.py",
    ".github/workflows/extract-c1-roulette-shortlist-once.yml",
    "docs/_C1_SHORTLIST_FAILURE.log",
):
    path = ROOT / relative
    if path.exists():
        path.unlink()

run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "add", "-A")
run("git", "commit", "-m", "extract C1 roulette canonical and implementation shortlist")
run("git", "push", "origin", "HEAD:agent/c1-approved-roulette-contract-recovery")
