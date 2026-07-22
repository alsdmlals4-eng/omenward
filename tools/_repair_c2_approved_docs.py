from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected one source, found {count}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


replace_once(
    "docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md",
    "- 최신 갱신일: 2026-07-16",
    "- 최신 갱신일: 2026-07-23",
)
replace_once(
    "docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md",
    "C2 검증 구현는 중앙 접전지 3개, 양측 중간거점 6개, 성문 6개, 본진 2개와 같은 라인 목적 순서를 실제 전투 상태로 연결한다. 점령·교착·건설 revision·성문 붕괴·자연 승패 자동 회귀가 존재한다.",
    "C2 전투 목적 루프는 중앙 접전지 3개, 양측 중간거점 6개, 성문 6개, 본진 2개와 같은 라인 목적 순서를 실제 전투 상태로 연결하며 통합 자동 회귀를 통과했다. 점령·교착·건설 revision·성문 붕괴·자연 승패 계약은 `docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`가 증거를 소유한다.",
)
replace_once(
    "docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md",
    "- 작성일: 2026-07-15",
    "- 작성일: 2026-07-15\n- 최신 갱신일: 2026-07-23",
)
replace_once(
    "docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md",
    "C2 검증 구현는 전투 상태에서 실제 아군 접전지 통제 수와 안정 중간거점 소유 수를 계산해 기존 시간 수입 공식에 전달한다.",
    "C2 전투 목적 루프는 전투 상태에서 실제 아군 접전지 통제 수와 안정 중간거점 소유 수를 계산해 기존 시간 수입 공식에 전달하며, 이 연결은 `docs/C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`의 통합 검증 증거를 따른다.",
)

for relative in (
    "docs/_C2_CONTRACT_DIAGNOSTIC.log",
    "tools/_repair_c2_approved_docs.py",
):
    path = ROOT / relative
    if path.exists():
        path.unlink()
