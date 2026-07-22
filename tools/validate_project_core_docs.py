#!/usr/bin/env python3
"""Validate Omenward project-core and current-state documentation contracts."""

from __future__ import annotations

import pathlib
import re
import sys
from typing import Iterable

ROOT = pathlib.Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "docs/PROJECT_CORE.md",
    "docs/CURRENT_IMPLEMENTATION_STATUS.md",
    "docs/CORE_RECOVERY_AUDIT_2026-07-22.md",
    "README.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
)

REFERENCE_FILES = (
    "README.md",
    "docs/ACTIVE_CONTEXT.md",
    "docs/HANDOFF_CONTEXT.md",
    "docs/DOCUMENTATION_MAP.md",
    "docs/OMENWARD_GAME_DESIGN.md",
    "docs/OMENWARD_ROADMAP.md",
    "docs/DECISIONS_PENDING.md",
)

STALE_CURRENT_CLAIMS = {
    "README.md": (
        "플레이 가능한 수직 슬라이스 구현 완료",
        "Issue #1 Phase 0 Plan Mode",
        "정확한 경로와 파일은 Phase 0 Plan Mode 승인 후 확정합니다.",
    ),
    "docs/OMENWARD_GAME_DESIGN.md": (
        "Phase 0 Plan Mode 대기 / 구현 전",
    ),
    "docs/OMENWARD_ROADMAP.md": (
        "Codex Plan Mode 실행 대기 / 구현 전",
        "현재는 Phase 0 구현이나 수직 슬라이스 구현을 시작하지 않는다.",
    ),
    "docs/DECISIONS_PENDING.md": (
        "1. Phase 0 기술 제안서 사용자 검토",
    ),
}

REQUIRED_CORE_TERMS = (
    "EXISTING_CORE_IDENTIFIED",
    "CORE_LOCK_PENDING_USER_CONFIRMATION",
    "## 3. 핵심 루프",
    "## 5. 분류",
    "## 6. 불변 조건",
    "## 7. 제거·대체 스트레스 테스트",
    "## 8. 코어 검증 게이트",
)

REQUIRED_STATUS_TERMS = (
    "TECHNICAL_BASELINE_IMPLEMENTED",
    "CORE_VERTICAL_SLICE_PARTIAL",
    "CORE_LOOP_NOT_PROVEN",
    "HUMAN_QA_NOT_RUN",
    "CORE_CONTRACT_DIVERGENT",
)


def _read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def _contains_all(text: str, values: Iterable[str]) -> list[str]:
    return [value for value in values if value not in text]


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            errors.append(f"missing required file: {relative}")

    if errors:
        return errors

    core = _read(root, "docs/PROJECT_CORE.md")
    status = _read(root, "docs/CURRENT_IMPLEMENTATION_STATUS.md")

    for missing in _contains_all(core, REQUIRED_CORE_TERMS):
        errors.append(f"PROJECT_CORE missing contract term: {missing}")
    for missing in _contains_all(status, REQUIRED_STATUS_TERMS):
        errors.append(f"CURRENT_IMPLEMENTATION_STATUS missing state term: {missing}")

    if re.search(r"(?m)^- (?:상태|잠금 상태): `(?:CORE_CONFIRMED|CORE_LOCKED)`$", core):
        errors.append("project core may not claim confirmed/locked without explicit user approval")

    for relative in REFERENCE_FILES:
        text = _read(root, relative)
        if "PROJECT_CORE.md" not in text:
            errors.append(f"{relative} does not reference PROJECT_CORE.md")
        if "CURRENT_IMPLEMENTATION_STATUS.md" not in text:
            errors.append(f"{relative} does not reference CURRENT_IMPLEMENTATION_STATUS.md")

    for relative, phrases in STALE_CURRENT_CLAIMS.items():
        text = _read(root, relative)
        for phrase in phrases:
            if phrase in text:
                errors.append(f"{relative} retains stale current-state claim: {phrase}")

    readme = _read(root, "README.md")
    if "기술·데이터 그레이박스" not in readme or "코어 루프 미완결" not in readme:
        errors.append("README does not expose the partial vertical-slice boundary")

    roadmap = _read(root, "docs/OMENWARD_ROADMAP.md")
    required_sequence = (
        "정본·프로젝트 코어 복구",
        "승인 룰렛 계약 복구",
        "전투 목적 루프 연결",
        "승인 코어 UX 6종",
        "코어 플레이테스트",
    )
    for missing in _contains_all(roadmap, required_sequence):
        errors.append(f"roadmap missing recovery sequence item: {missing}")

    decisions = _read(root, "docs/DECISIONS_PENDING.md")
    if "Godot 4.7.1·Compatibility·960×540" not in decisions:
        errors.append("DECISIONS_PENDING does not distinguish implemented technical baseline")
    if "승인 룰렛 계약 복구" not in decisions:
        errors.append("DECISIONS_PENDING does not point to the next decision gate")

    map_text = _read(root, "docs/DOCUMENTATION_MAP.md")
    if re.search(r"\|\s*프로젝트 코어\s*\|\s*`PROJECT_CORE\.md`", map_text) is None:
        errors.append("DOCUMENTATION_MAP has no project-core responsibility row")
    if re.search(r"\|\s*현재 구현 증거\s*\|\s*`CURRENT_IMPLEMENTATION_STATUS\.md`", map_text) is None:
        errors.append("DOCUMENTATION_MAP has no implementation-status responsibility row")

    for relative in ("docs/PROJECT_CORE.md", "docs/CURRENT_IMPLEMENTATION_STATUS.md"):
        text = _read(root, relative)
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (root / relative).parent / target.split("#", 1)[0]
            if not resolved.exists():
                errors.append(f"broken local link in {relative}: {target}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Project core documentation validation FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Project core documentation validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
