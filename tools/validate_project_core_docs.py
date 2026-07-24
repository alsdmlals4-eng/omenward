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
    "docs/OMENWARD_GAME_DESIGN.md": ("Phase 0 Plan Mode 대기 / 구현 전",),
    "docs/OMENWARD_ROADMAP.md": (
        "Codex Plan Mode 실행 대기 / 구현 전",
        "현재는 Phase 0 구현이나 수직 슬라이스 구현을 시작하지 않는다.",
    ),
    "docs/DECISIONS_PENDING.md": ("1. Phase 0 기술 제안서 사용자 검토",),
}
REQUIRED_CORE_TERMS = (
    "CORE_CONFIRMED",
    "CORE_LOCKED",
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
    "C1_ROULETTE_CORE_REMOTE_PROVEN",
    "C2_BATTLE_OBJECTIVE_REMOTE_PROVEN",
    "C3_AUTOMATED_CONTRACTS_PROVEN",
)
ROADMAP_REQUIRED_SECTIONS = (
    "## 4. G1 — Phase 0 Work Order",
    "## 5. G2 — Phase 0 Codex Plan Mode",
    "## 6. Gate — 사용자 승인",
    "## 7. P1 — Phase 0 Godot 기술 기준선 구현",
    "## 8. G3 — 핵심 수직 슬라이스 Plan Mode",
    "## 9. P2 — 10~15분 핵심 수직 슬라이스",
    "## 10. P3 — 시스템 안정화",
    "## 11. P4 — 콘텐츠·아트 확장",
    "## 12. P5 — 캠페인·데모",
    "## 13. P6 — 출시 준비",
    "## 14. 단계 변경 시 문서 동기화",
    "## 15. 지금 실행할 단 하나의 작업",
)
ROADMAP_PRESERVED_PHRASES = (
    "별도 `EnemyUnitProfile` 없음",
    "룰렛 최소 100,000시드 시뮬레이션",
    "지상 120·비행 24·투사체 160·VFX 80 정상 목표",
    "모든 Gate와 Phase 종료 시 다음을 갱신한다",
)
DECISIONS_PRESERVED_PHRASES = (
    "4.6.3 대안 검토",
    "Mobile·Forward+ 재검토",
    "640×360 논리 화면 대안 검토",
    "AutoLoad 승격 재검토",
    "JSON Schema 파일과 GDScript validator의 최종 책임 분리",
    "AnimationContract 10개, allied/veil Visual Profile 20개",
)


def _read(root: pathlib.Path, relative: str) -> str:
    return (root / relative).read_text(encoding="utf-8")


def _missing(text: str, values: Iterable[str]) -> list[str]:
    return [value for value in values if value not in text]


def validate(root: pathlib.Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    if errors:
        return errors

    core = _read(root, "docs/PROJECT_CORE.md")
    status = _read(root, "docs/CURRENT_IMPLEMENTATION_STATUS.md")
    for term in _missing(core, REQUIRED_CORE_TERMS):
        errors.append(f"PROJECT_CORE missing contract term: {term}")
    for term in _missing(status, REQUIRED_STATUS_TERMS):
        errors.append(f"CURRENT_IMPLEMENTATION_STATUS missing state term: {term}")

    for term in (
        "- 상태: `CORE_CONFIRMED`",
        "- 잠금 상태: `CORE_LOCKED`",
        "2026-07-22 대화에서 `코어확정`",
    ):
        if term not in core:
            errors.append(f"PROJECT_CORE missing confirmed lock evidence: {term}")

    for relative in (
        "docs/PROJECT_CORE.md",
        "docs/CORE_RECOVERY_AUDIT_2026-07-22.md",
        "docs/DECISIONS_PENDING.md",
        "docs/OMENWARD_ROADMAP.md",
    ):
        text = _read(root, relative)
        for term in ("EXISTING_CORE_IDENTIFIED", "CORE_LOCK_PENDING_USER_CONFIRMATION", "PENDING_USER_CONFIRMATION"):
            if term in text:
                errors.append(f"{relative} retains stale project-core lock state: {term}")

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
    if not all(term in readme for term in ("C1 룰렛 REMOTE_PROVEN", "C2 전투 목적 루프 REMOTE_PROVEN", "사람 플레이 미완결")):
        errors.append("README does not expose proven C1/C2 and the human-QA boundary")

    roadmap = _read(root, "docs/OMENWARD_ROADMAP.md")
    for term in (
        "정본·프로젝트 코어 확정·잠금 완료",
        "C1 승인 룰렛 핵심 계약 원격 검증·병합 완료",
        "C2 전투 목적 루프 원격 검증·병합 완료",
        "C3 승인 코어 UX 6종 자동 계약 검증 완료",
        "코어 플레이테스트",
    ):
        if term not in roadmap:
            errors.append(f"roadmap missing recovery sequence item: {term}")
    for term in ROADMAP_REQUIRED_SECTIONS:
        if term not in roadmap:
            errors.append(f"roadmap missing preserved section: {term}")
    for term in ROADMAP_PRESERVED_PHRASES:
        if term not in roadmap:
            errors.append(f"roadmap missing preserved contract phrase: {term}")

    decisions = _read(root, "docs/DECISIONS_PENDING.md")
    if "### 성능 첫 가설###" in decisions:
        errors.append("DECISIONS_PENDING contains a duplicated performance heading")
    for term in DECISIONS_PRESERVED_PHRASES:
        if term not in decisions:
            errors.append(f"DECISIONS_PENDING missing preserved alternative: {term}")
    for term in (
        "Godot 4.7.1·Compatibility·960×540",
        "C1U 이동권·럭키",
        "프로젝트 코어 확정·잠금 — 완료",
    ):
        if term not in decisions:
            errors.append(f"DECISIONS_PENDING missing current decision contract: {term}")

    doc_map = _read(root, "docs/DOCUMENTATION_MAP.md")
    if re.search(r"\|\s*프로젝트 코어\s*\|\s*`PROJECT_CORE\.md`", doc_map) is None:
        errors.append("DOCUMENTATION_MAP has no project-core responsibility row")
    if re.search(r"\|\s*현재 구현 증거\s*\|\s*`CURRENT_IMPLEMENTATION_STATUS\.md`", doc_map) is None:
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
