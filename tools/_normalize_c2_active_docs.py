from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]


def replace_once(relative: str, old: str, new: str) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{relative}: expected exactly one source, found {count}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


# README: remove duplicated status and clarify the proven/human-QA boundary.
replace_once(
    "README.md",
    "현재 저장소에는 원격 검증된 C1 룰렛 핵심 계약과 C2 전투 목적 루프가 존재한다. C2는 접전지·거점·성문·본진·자연 승패·경제를 연결했지만 공통 원격 검증은 완료됐고 사람 플레이는 남아 있다. 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이다.",
    "현재 저장소에는 원격 검증된 C1 룰렛 핵심 계약과 C2 전투 목적 루프가 존재한다. C2는 접전지·거점·성문·본진·자연 승패·경제를 연결했고 통합 자동 검증을 마쳤다. 현재 판정은 `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`, `CORE_VERTICAL_SLICE_PARTIAL`, `CORE_LOOP_NOT_PROVEN`, `HUMAN_QA_NOT_RUN`이며 사람 플레이는 아직 실행하지 않았다.",
)

# Active context: latest proof and next implementation order.
replace_once("docs/ACTIVE_CONTEXT.md", "- 갱신일: 2026-07-22", "- 갱신일: 2026-07-23")
replace_once("docs/ACTIVE_CONTEXT.md", "현재 상태는 다음 네 문구를 함께 사용한다.", "현재 상태는 다음 여섯 문구를 함께 사용한다.")
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- C2 검증 구현는 같은 라인 교전→접전지→중간거점→성문→본진·W15 보스→승패와 실제 소유 수 경제를 연결한다.",
    "- C2 전투 목적 루프는 같은 라인 교전→접전지→중간거점→성문→본진·W15 보스→승패와 실제 소유 수 경제를 연결한다.",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- 최종 공통 원격 검증·코어 UX 6종·사람 플레이는 아직 완료되지 않았다.",
    "- C1·C2 통합 원격 검증은 완료됐고 코어 UX 6종·사람 플레이는 아직 완료되지 않았다.",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "→ C2 전투 목적 루프 원격 검증 완료\n→ [결정 게이트] C1U 이동권·럭키·100,000시드\n→ 승인 코어 UX 6종\n→ 사람 플레이 검증",
    "→ C2 전투 목적 루프 원격 검증 완료\n→ [다음 구현] C3 승인 코어 UX 6종\n→ [결정 게이트] C1U 이동권·럭키·100,000시드\n→ 사람 플레이 검증",
)
replace_once(
    "docs/ACTIVE_CONTEXT.md",
    "- PR #49는 main에 병합됐다. PR #50은 C2 전투 목적 루프 검증 구현와 문서·검증 동기화를 다룬다.",
    "- PR #49는 main에 병합됐다. PR #50은 C2 전투 목적 루프의 원격 검증과 문서·검증 동기화를 완료했으며 병합 대상이다.",
)

# Handoff: remove candidate-era statements.
replace_once("docs/HANDOFF_CONTEXT.md", "- 갱신일: 2026-07-22", "- 갱신일: 2026-07-23")
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "2. 저장소에는 원격 검증된 C1 룰렛 핵심과 C2 전투 목적 구현 후보가 있다. C2 최종 공통 원격 검증, C1U 유틸리티 결정, 코어 UX와 사람 플레이는 남아 있다.",
    "2. 저장소에는 원격 검증된 C1 룰렛 핵심과 C2 전투 목적 루프가 있다. C1U 유틸리티 결정, C3 코어 UX와 사람 플레이는 남아 있다.",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "현재 Godot 프로젝트는 run `29926598807`에서 검증된 C1 룰렛 핵심과 C2 전투 목적 구현 후보를 포함한다. C2는 접전지·중간거점·성문·본진·W15 보스·자연 승패·경제를 연결했지만 최종 공통 원격 검증과 승인 UX 6종·사람 플레이는 남아 있으므로 ‘핵심 수직 슬라이스 완료’로 부르지 않는다.",
    "현재 Godot 프로젝트는 C1 run `29926598807`과 통합 Core Contracts run `29936497790`에서 검증된 C1 룰렛 핵심·C2 전투 목적 루프를 포함한다. C3 승인 UX 6종과 사람 플레이는 남아 있으므로 ‘핵심 수직 슬라이스 완료’로 부르지 않는다.",
)
replace_once(
    "docs/HANDOFF_CONTEXT.md",
    "다음 순서는 PR #50 C2 공통 원격 검증, C1U 사용자 결정, 코어 UX, 사람 플레이 검증이다.",
    "다음 순서는 PR #50 병합, C3 승인 코어 UX 6종, C1U 사용자 결정 게이트, 사람 플레이 검증이다.",
)

# GDD: grammar and final proof.
replace_once("docs/OMENWARD_GAME_DESIGN.md", "- 갱신일: 2026-07-22", "- 갱신일: 2026-07-23")
replace_once(
    "docs/OMENWARD_GAME_DESIGN.md",
    "C2 검증 구현는 `같은 라인 교전 → 접전지 → 중간거점 → 성문 → 본진·W15 보스 → 자연 승패`와 점령 기반 건물·경제를 연결한다. 본진 독립 방어 수치와 접전지 별도 점령 시간은 미승인이므로 기존 승인 계약을 가역 fallback으로 재사용한다. 전체 설계와 사람 경험이 완결됐다는 뜻은 아니며 실제 구현 여부는 상태 문서와 코드·데이터·테스트를 대조한다.",
    "C2 전투 목적 루프는 `같은 라인 교전 → 접전지 → 중간거점 → 성문 → 본진·W15 보스 → 자연 승패`와 점령 기반 건물·경제를 연결하며 통합 Core Contracts run `29936497790`에서 검증됐다. 본진 독립 방어 수치와 접전지 별도 점령 시간은 미승인이므로 기존 승인 계약을 가역 fallback으로 재사용한다. 전체 설계와 사람 경험이 완결됐다는 뜻은 아니며 실제 구현 여부는 상태 문서와 코드·데이터·테스트를 대조한다.",
)

# Roadmap: C3 implementation precedes unresolved C1U and points to latest proof.
replace_once("docs/OMENWARD_ROADMAP.md", "- 갱신일: 2026-07-22", "- 갱신일: 2026-07-23")
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "→ C2 전투 목적 루프 원격 검증 완료\n→ [결정 게이트] C1U 이동권·럭키 규칙 통합·100,000시드 검증\n→ 승인 코어 UX 6종\n→ 10~15분 코어 플레이테스트",
    "→ C2 전투 목적 루프 원격 검증 완료\n→ [다음 구현] C3 승인 코어 UX 6종\n→ [결정 게이트] C1U 이동권·럭키 규칙 통합·100,000시드 검증\n→ 10~15분 코어 플레이테스트",
)
replace_once(
    "docs/OMENWARD_ROADMAP.md",
    "C2는 head `85e2930a839fd210548c7aa2a53125d18c4de875`, run `29934172758`에서 원격 검증됐다.",
    "C2는 통합 head `496157d0b87ab71ea2c9f25780f21df9f68b67f3`, `Validate Core Contracts` run `29936497790`에서 원격 검증됐다.",
)

# Pending decisions: C2 is complete, C3 is current implementation, C1U remains a user gate.
replace_once("docs/DECISIONS_PENDING.md", "- 갱신일: 2026-07-22", "- 갱신일: 2026-07-23")
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- 현재 작업: PR #50 C2 공통 원격 검증 / 다음 사용자 결정: C1U 이동권·럭키·분포",
    "- 현재 작업: PR #50 C2 병합 및 C3 코어 UX 착수 / 다음 사용자 결정: C1U 이동권·럭키·분포",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- [ ] 최종 공통 `Core Contracts` 원격 검증과 PR #50 병합.",
    "- [x] 통합 `Validate Core Contracts` 원격 검증 — head `496157d0b87ab71ea2c9f25780f21df9f68b67f3`, run `29936497790`.\n- [ ] PR #50 병합.",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "- [x] Godot 4.7.1 editor import·전체 headless·runtime smoke — run `29926598807`.",
    "- [x] C1 Godot 4.7.1 editor import·전체 headless·runtime smoke — run `29926598807`.\n- [x] C1·C2 통합 Godot·4환경 계약·문서·Skill 검증 — run `29936497790`.",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (`29926598807`) |",
    "| headless 테스트 | Godot 4.7.1 전체 suite 원격 통과 (C1 `29926598807`, 통합 C1·C2 `29936497790`) |",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "1. PR #50 C2 공통 원격 검증·병합 결정\n2. C1U 이동권·럭키 정본 통합과 100,000시드 사용자 결정\n3. 승인 코어 UX 6종\n5. 10~15분 사람 플레이와 1080p·720p QA\n6. 밸런스 안정화\n7. 콘텐츠·아트 확장",
    "1. PR #50 C2 병합\n2. C3 승인 코어 UX 6종 최소 구현\n3. C1U 이동권·럭키 정본 통합과 100,000시드 사용자 결정\n4. 10~15분 사람 플레이와 1080p·720p QA\n5. 밸런스 안정화\n6. 콘텐츠·아트 확장",
)
replace_once(
    "docs/DECISIONS_PENDING.md",
    "현재는 새로운 병종·Tier·보스·캠페인 콘텐츠를 추가하는 단계가 아니다. C2는 승인 인과만 복구하며, C1U는 사용자 결정 전 구현하지 않는다.",
    "현재는 새로운 병종·Tier·보스·캠페인 콘텐츠를 추가하는 단계가 아니다. C2는 원격 검증을 완료했고 다음 구현은 C3 코어 UX이며, C1U는 사용자 결정 전 구현하지 않는다.",
)

# Documentation router and technical doc.
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "현재 C2 시작 문서는 `C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md`와 전장·공용 병종·경제 APPROVED 정본이다. C1 증거는 보존 책임 문서이며, 과거 Work Order·Goal·Proposal은 Git 이력에서만 추적한다.",
    "현재 C3 시작점은 `CURRENT_IMPLEMENTATION_STATUS.md`, `OMENWARD_ROADMAP.md`, 승인 UI·징조·룰렛·전투 표시 책임 문서와 실제 `scripts/ui/`, `scenes/ui/`, 테스트다. C1·C2 보고서는 검증 증거로 보존하며, 과거 Work Order·Goal·Proposal은 Git 이력에서만 추적한다.",
)
replace_once(
    "docs/DOCUMENTATION_MAP.md",
    "| 현재 C2 구현·감사 | `C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md` |",
    "| C2 구현·검증 증거 | `C2_BATTLE_OBJECTIVE_AUDIT_2026-07-22.md` |",
)
replace_once("docs/GODOT_PROJECT_STRUCTURE.md", "- 갱신일: 2026-07-22", "- 갱신일: 2026-07-23")

# Strengthen the durable validator against the exact transition errors found manually.
validator_path = ROOT / "tools/validate_c2_battle_objective.py"
validator = validator_path.read_text(encoding="utf-8")
needle = '''    stale_active = (
        "PR #49 사용자 검토 대기",'''
replacement = '''    stale_active = (
        "C2 검증 구현는",
        "C2 전투 목적 구현 후보",
        "최종 공통 원격 검증·코어 UX 6종·사람 플레이는 아직 완료되지 않았다",
        "PR #49 사용자 검토 대기",'''
if needle not in validator:
    raise RuntimeError("validator stale-state insertion point missing")
validator = validator.replace(needle, replacement, 1)
needle = '''    status = (root / "docs/CURRENT_IMPLEMENTATION_STATUS.md").read_text(encoding="utf-8")'''
replacement = '''    readme = (root / "README.md").read_text(encoding="utf-8")
    if readme.count("C2_BATTLE_OBJECTIVE_REMOTE_PROVEN") != 1:
        errors.append("README must list the C2 proven state exactly once")
    active_context = (root / "docs/ACTIVE_CONTEXT.md").read_text(encoding="utf-8")
    if "C1·C2 통합 원격 검증은 완료" not in active_context or "[다음 구현] C3 승인 코어 UX 6종" not in active_context:
        errors.append("ACTIVE_CONTEXT does not expose the final C2 proof and C3 next step")
    handoff = (root / "docs/HANDOFF_CONTEXT.md").read_text(encoding="utf-8")
    if "C2 전투 목적 구현 후보" in handoff or "PR #50 C2 공통 원격 검증" in handoff:
        errors.append("HANDOFF_CONTEXT retains the C2 candidate-era next step")

    status = (root / "docs/CURRENT_IMPLEMENTATION_STATUS.md").read_text(encoding="utf-8")'''
if needle not in validator:
    raise RuntimeError("validator proof insertion point missing")
validator = validator.replace(needle, replacement, 1)
validator_path.write_text(validator, encoding="utf-8", newline="\n")

pathlib.Path(__file__).unlink()
