#!/usr/bin/env python3
from __future__ import annotations

import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]
BRANCH = "agent/project-core-canon-recovery"


def run(*args: str) -> None:
    subprocess.run(args, cwd=ROOT, check=True)


def git_show(relative: str) -> str:
    return subprocess.check_output(
        ["git", "show", f"origin/main:{relative}"],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
    )


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match for {old!r}, found {count}")
    return text.replace(old, new, 1)


def replace_section(text: str, start: str, end: str, replacement: str, label: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index)
    return text[:start_index] + replacement.rstrip() + "\n\n" + text[end_index:]


# Restore the exact current-main roadmap, then change only current-state-owned sections.
roadmap = git_show("docs/OMENWARD_ROADMAP.md")
roadmap = replace_once(roadmap, "- 갱신일: 2026-07-16", "- 갱신일: 2026-07-22", "roadmap date")
roadmap = replace_once(
    roadmap,
    "- 기준: `docs/HANDOFF_CONTEXT.md`, `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`",
    "- 기준: `docs/PROJECT_CORE.md`, `docs/CURRENT_IMPLEMENTATION_STATUS.md`, `docs/HANDOFF_CONTEXT.md`",
    "roadmap basis",
)
roadmap = replace_once(
    roadmap,
    "- 현재 상태: **프리프로덕션 구조 승인 완료 / 새 Codex 채팅용 Phase 0 Work Order 준비 완료 / Codex Plan Mode 실행 대기 / 구현 전**",
    "- 현재 상태: **기술 기준선 구현 / 핵심 수직 슬라이스 부분 구현 / C0 정본·프로젝트 코어 복구 진행**",
    "roadmap state",
)
roadmap = replace_once(
    roadmap,
    "- 현재 Work Order: `docs/work_orders/0001-phase-0-codex-plan-mode.md`",
    "- 현재 조사 입력: `docs/work_orders/0002-current-main-audit-and-next-iteration-plan-mode.md`",
    "roadmap work order",
)
roadmap_section_1 = """## 1. 현재 위치

책임 원본:

- 프로젝트 코어: `docs/PROJECT_CORE.md`
- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

```text
프리프로덕션 구조 승인
→ Phase 0 기술·데이터 기준선 구현
→ 수직 슬라이스 구성요소 부분 구현
→ [현재] 정본·프로젝트 코어 복구
→ 승인 룰렛 계약 복구
→ 전투 목적 루프 연결
→ 승인 코어 UX 6종
→ 10~15분 코어 플레이테스트
→ 시스템 안정화
→ 콘텐츠·아트 확장
→ 캠페인·데모 통합
```

현재 `구현됨`은 파일과 실행 경로가 있다는 뜻이며 `검증됨`과 같지 않다.

```text
TECHNICAL_BASELINE_IMPLEMENTED
≠ CORE_VERTICAL_SLICE_COMPLETE
≠ CORE_LOOP_PROVEN
≠ HUMAN_QA_COMPLETE
```"""
roadmap = replace_section(
    roadmap,
    "## 1. 현재 위치",
    "---\n\n## 2. 프로젝트 전체 완료 정의",
    roadmap_section_1,
    "roadmap section 1",
)
roadmap_section_3 = """## 3. 단계 요약

| 단계 | 목표 | 현재 상태 | 다음 게이트 |
|---|---|---|---|
| P0 프리프로덕션 | 제품·전장·공용 데이터·아트·연출 계약 | 완료 | 정본 유지 |
| P1 기술 기준선 | 실행·데이터·결정론·검증 골격 | **구현됨 / 최신 runtime 재검증 필요** | C0 정본 일치 |
| C0 정본·코어 복구 | 프로젝트 코어·상태·로드맵 일치 | **진행 중** | 사용자 코어 문구 확인·문서 PR |
| C1 룰렛 계약 복구 | 중앙 판정 줄·완성선·등급·단일 보상 | 미시작 | 승인 계약 테스트 PASS |
| C2 전투 목적 루프 | 접전지·거점·성문·승패·경제 연결 | 부분 구현 | End-to-End 전투 PASS |
| C3 코어 UX | 승인 UX 6종을 실제 데이터와 연결 | 미시작 | 이해도·가독성 기준 |
| C4 코어 플레이테스트 | 10~15분 핵심 재미와 학습 검증 | 미실행 | 사람 플레이 기준 충족 |
| P3 시스템 안정화 | 확률·경제·전투·성능 조정 | 미시작 | 반복 가능한 기준선 |
| P4 콘텐츠·아트 확장 | 10병종·건물·보스·UI·자산 확대 | 미시작 | 제작 QA 통과 |
| P5 캠페인·데모 | 튜토리얼+정규 스테이지 통합 | 미시작 | 외부 플레이테스트 |
| P6 출시 준비 | 저장·옵션·패키징·최적화 | 장기 | 릴리스 후보 |

이 표와 1절이 현재 상태의 권위 원본이다. 아래 G1~P6 상세 절은 완료 기준·불변 조건·검증 계약의 보존 기록이며, 과거 상태 문구가 현재 위치를 덮지 않는다."""
roadmap = replace_section(
    roadmap,
    "## 3. 단계 요약",
    "---\n\n## 4. G1 — Phase 0 Work Order",
    roadmap_section_3,
    "roadmap section 3",
)
roadmap_section_15 = """## 15. 지금 실행할 단 하나의 작업

```text
정본·프로젝트 코어 복구 Draft PR 검토
→ 프로젝트 코어 문구의 사용자 확인
→ 문서 PR 병합
→ 승인 룰렛 계약 복구를 별도 Plan·Build·Review 작업으로 시작
```

현재 작업에서는 게임 코드·Scene·Resource·게임 데이터와 승인 수치를 변경하지 않는다. 다음 기능 PR도 룰렛 계약 복구만 포함하며 전투 목적 루프·UX·콘텐츠 확대를 섞지 않는다."""
section_15_start = roadmap.index("## 15. 지금 실행할 단 하나의 작업")
roadmap = roadmap[:section_15_start] + roadmap_section_15 + "\n"
write("docs/OMENWARD_ROADMAP.md", roadmap)

# Restore current-main decisions and preserve unique Phase 0 alternatives while updating current gates.
decisions = git_show("docs/DECISIONS_PENDING.md")
decisions = replace_once(decisions, "- 갱신일: 2026-07-16", "- 갱신일: 2026-07-22", "decisions date")
decisions = replace_once(
    decisions,
    "- 기준: `docs/HANDOFF_CONTEXT.md`, `docs/design/APPROVED_PREPRODUCTION_POC_BASELINE_V1.md`",
    "- 기준: `docs/PROJECT_CORE.md`, `docs/CURRENT_IMPLEMENTATION_STATUS.md`, `docs/HANDOFF_CONTEXT.md`",
    "decisions basis",
)
decisions = replace_once(
    decisions,
    "- 현재 제안서: `docs/design/proposals/0001-phase-0-godot-bootstrap.md`",
    "- 현재 작업: 정본·프로젝트 코어 복구 / 다음 기능 게이트: 승인 룰렛 계약 복구",
    "decisions current work",
)
decisions_section_1 = """## 1. 현재 가장 먼저 결정할 항목

### A. 프로젝트 코어 문구 잠금

`docs/PROJECT_CORE.md`는 기존 승인 기획과 실제 구현에서 코어를 식별해 `EXISTING_CORE_IDENTIFIED`로 기록한다.

- [ ] 정체성 한 문장과 세 기둥을 사용자 확인 후 `CORE_CONFIRMED`로 전환.
- [ ] 제거 테스트와 불변 조건을 사용자 확인 후 `CORE_LOCKED`로 전환.
- 잠금 전에도 수직 슬라이스 우선순위와 검증 게이트는 해당 문서를 따른다.

### B. 다음 기능 작업 — 승인 룰렛 계약 복구

현재 구현은 9개의 카드를 직접 반환하지만 승인 계약은 중앙 가로줄 판정, 동일 심벌 완성선, 등급과 단일 보상 생성이다.

- [ ] placeholder 테스트를 승인 계약 테스트로 교체하는 Plan 승인.
- [ ] 중앙 판정·완성선·등급·단일 보상을 먼저 복구하고 X·금화·럭키 찬스·이동권은 같은 계약 안에서 단계적으로 연결.
- [ ] 결과 보관함 기본 용량과 UI는 기존 미확정 상태 유지.
- [ ] 전투 목적 루프와 코어 UX를 같은 PR에 섞지 않음.

### C. 검증 증거

- [ ] 문서 PR 뒤 Godot editor import와 기존 headless suite 재실행.
- [ ] 룰렛 복구 PR에서 같은 시드·보드·결과 결정론 검증.
- [ ] 코어 UX 뒤 1920×1080·1280×720 사람 플레이.
- [ ] W1~W20 전체 플레이는 코어 루프 완결 뒤 실행.

### D. 이미 구현된 기술 기준선

| 항목 | 현재 상태 |
|---|---|
| Godot 4.7.1 standard·GDScript·Compatibility renderer | 실제 `project.godot`에 존재 |
| 960×540 viewport·1920×1080 출력·viewport stretch·keep aspect·integer scale | 실제 `project.godot`에 존재 |
| Main·GameSession·CombatClock·DeterminismService·DataRegistry | 실제 코드에 존재 |
| typed `.tres`와 StageManifest·input log | 실제 코드·데이터에 존재 |
| 공용 10병종과 진영 Visual 분리 골격 | 실제 Resource·validator에 존재 |
| headless 테스트 파일 | 존재하지만 이번 문서 PR에서 Godot로 재실행하지 않음 |

### E. 과거 Phase 0 추천에서 남은 확인·대안

다음 항목은 삭제된 결정이 아니라 구현 기준선의 재검증 또는 조건부 대안이다.

- [ ] Godot 4.7.1에서 치명적 회귀가 확인될 경우에만 4.6.3 대안 검토.
- [ ] 고급 렌더링 기능의 실제 필요가 확인될 경우에만 Mobile·Forward+ 재검토.
- [ ] 1280×720 정수 확대 레터박스 허용 여부를 사람 QA로 확인.
- [ ] 레터박스가 허용되지 않을 경우에만 640×360 논리 화면 대안 검토.
- [x] Phase 0 AutoLoad 미사용 구조가 실제 코드에 존재.
- [ ] 다중 Scene 공유 필요가 확인된 뒤에만 AutoLoad 승격 재검토.
- [x] typed `.tres`: UnitArchetype·Tier·Rank·FactionVisual·AnimationContract·Battlefield 계열.
- [x] JSON 성격 데이터: StageManifest·input/replay log.
- [x] CSV를 Phase 0 런타임 원본으로 사용하지 않음.
- [ ] JSON Schema 파일과 GDScript validator의 최종 책임 분리.
- [x] UnitArchetype 10개, Tier 3개, player Rank 4개 골격.
- [x] AnimationContract 10개, allied/veil Visual Profile 20개 골격.
- [ ] 실제 최종 이미지는 placeholder 공유가 아니라 아트·가독성 검증 뒤 교체."""
decisions = replace_section(
    decisions,
    "## 1. 현재 가장 먼저 결정할 항목",
    "---\n\n## 2. 공식 명칭·세계관",
    decisions_section_1,
    "decisions section 1",
)
tech_start = decisions.index("## 10. 기술·성능·테스트")
performance_start = decisions.index("### 성능 첫 가설", tech_start)
tech_intro = """## 10. 기술·성능·테스트

### 현재 구현됨 / 최신 재검증 필요

- [x] Godot 4.7.1 standard 기준 프로젝트 파일.
- [x] Compatibility renderer.
- [x] 960×540 viewport·integer scale·1920×1080 출력.
- [x] 현재 Phase 0 AutoLoad 없음.
- [x] typed Resource와 StageManifest·input log 경계.
- [x] 이름 기반 RNG stream과 input log 구조.
- [x] GDScript headless test 파일.

현재 전투 고정 스텝은 `BattleSimulator.FIXED_STEP_SECONDS = 0.1`이다. 과거 60Hz 제안과 같다고 간주하지 않으며, 성능·판정 요구를 근거로 별도 결정한다.

"""
decisions = decisions[:tech_start] + tech_intro + decisions[performance_start:]
decisions_section_12 = """## 12. 현재 실행 순서

```text
1. 정본·프로젝트 코어 복구 PR 검토
2. 프로젝트 코어 문구 잠금 여부 사용자 확인
3. 승인 룰렛 계약 복구 Plan
4. 룰렛 계약 구현·자동 검증
5. 전투 목적 루프 연결
6. 승인 코어 UX 6종
7. 10~15분 사람 플레이와 1080p·720p QA
8. 밸런스 안정화
9. 콘텐츠·아트 확장
```

현재는 새로운 병종·Tier·보스·캠페인 콘텐츠를 추가하는 단계가 아니다. 다음 기능 변경은 승인 룰렛 계약 복구로 제한한다."""
section_12_start = decisions.index("## 12. 현재 실행 순서")
decisions = decisions[:section_12_start] + decisions_section_12 + "\n"
write("docs/DECISIONS_PENDING.md", decisions)

# Remove duplicate README router entry while restoring the technical structure link.
readme = read("README.md")
readme = replace_once(
    readme,
    "11. [`docs/DOCUMENTATION_MAP.md`](docs/DOCUMENTATION_MAP.md)에서 작업별 추가 책임 원본을 확인",
    "11. [`docs/GODOT_PROJECT_STRUCTURE.md`](docs/GODOT_PROJECT_STRUCTURE.md) — 현재 Godot Scene·상태 소유·데이터 구조",
    "README duplicate router entry",
)
write("README.md", readme)

# Record the P0 caught by adversarial diff review.
audit = read("docs/CORE_RECOVERY_AUDIT_2026-07-22.md")
audit += """

## 10. PR diff 적대적 재검토에서 발견한 P0

초기 자동 변환의 Roadmap 단계 표 정규식이 `re.S`와 결합돼 과거 G1~P6 상세 절 약 300줄을 함께 제거했다. 자동 Validator는 필수 현재 상태 문구만 검사해 이 손실을 잡지 못했다.

조치:

- 최신 `main`의 Roadmap과 Decisions를 Git에서 직접 복원.
- 현재 상태가 소유하는 1절·3절·15절만 경계 기반으로 교체.
- G1~P6의 목적·불변·종료 기준을 그대로 보존.
- Phase 0의 renderer·해상도·AutoLoad·데이터 경계·fallback 대안을 현재 Decisions에 재분류해 보존.
- Roadmap 상세 절·고유 문구·최소 길이와 Decisions 고유 대안·중복 제목을 검사하는 회귀 계약 추가.

판정: `P0_FOUND_AND_REPAIRED_BEFORE_MERGE`.
"""
write("docs/CORE_RECOVERY_AUDIT_2026-07-22.md", audit)

# Strengthen the validator with no-loss checks.
validator = read("tools/validate_project_core_docs.py")
constants_marker = "REQUIRED_STATUS_TERMS = (\n    \"TECHNICAL_BASELINE_IMPLEMENTED\",\n    \"CORE_VERTICAL_SLICE_PARTIAL\",\n    \"CORE_LOOP_NOT_PROVEN\",\n    \"HUMAN_QA_NOT_RUN\",\n    \"CORE_CONTRACT_DIVERGENT\",\n)\n"
constants_replacement = constants_marker + '''\nROADMAP_REQUIRED_SECTIONS = (\n    "## 4. G1 — Phase 0 Work Order",\n    "## 5. G2 — Phase 0 Codex Plan Mode",\n    "## 6. Gate — 사용자 승인",\n    "## 7. P1 — Phase 0 Godot 기술 기준선 구현",\n    "## 8. G3 — 핵심 수직 슬라이스 Plan Mode",\n    "## 9. P2 — 10~15분 핵심 수직 슬라이스",\n    "## 10. P3 — 시스템 안정화",\n    "## 11. P4 — 콘텐츠·아트 확장",\n    "## 12. P5 — 캠페인·데모",\n    "## 13. P6 — 출시 준비",\n    "## 14. 단계 변경 시 문서 동기화",\n    "## 15. 지금 실행할 단 하나의 작업",\n)\n\nROADMAP_PRESERVED_PHRASES = (\n    "별도 `EnemyUnitProfile` 없음",\n    "룰렛 최소 100,000시드 시뮬레이션",\n    "지상 120·비행 24·투사체 160·VFX 80 정상 목표",\n    "모든 Gate와 Phase 종료 시 다음을 갱신한다",\n)\n\nDECISIONS_PRESERVED_PHRASES = (\n    "4.6.3 대안 검토",\n    "Mobile·Forward+ 재검토",\n    "640×360 논리 화면 대안 검토",\n    "AutoLoad 승격 재검토",\n    "JSON Schema 파일과 GDScript validator의 최종 책임 분리",\n    "AnimationContract 10개, allied/veil Visual Profile 20개",\n)\n'''
validator = replace_once(validator, constants_marker, constants_replacement, "validator constants")
check_marker = '''    for missing in _contains_all(roadmap, required_sequence):
        errors.append(f"roadmap missing recovery sequence item: {missing}")

    decisions = _read(root, "docs/DECISIONS_PENDING.md")
'''
check_replacement = '''    for missing in _contains_all(roadmap, required_sequence):
        errors.append(f"roadmap missing recovery sequence item: {missing}")
    if len(roadmap.splitlines()) < 330:
        errors.append("roadmap appears truncated; expected preserved Phase detail sections")
    for missing in _contains_all(roadmap, ROADMAP_REQUIRED_SECTIONS):
        errors.append(f"roadmap missing preserved section: {missing}")
    for missing in _contains_all(roadmap, ROADMAP_PRESERVED_PHRASES):
        errors.append(f"roadmap missing preserved contract phrase: {missing}")

    decisions = _read(root, "docs/DECISIONS_PENDING.md")
    if len(decisions.splitlines()) < 400:
        errors.append("DECISIONS_PENDING appears truncated; expected preserved decision detail")
    if "### 성능 첫 가설###" in decisions:
        errors.append("DECISIONS_PENDING contains a duplicated performance heading")
    for missing in _contains_all(decisions, DECISIONS_PRESERVED_PHRASES):
        errors.append(f"DECISIONS_PENDING missing preserved alternative: {missing}")
'''
validator = replace_once(validator, check_marker, check_replacement, "validator no-loss checks")
write("tools/validate_project_core_docs.py", validator)

# Add mutation tests for large-section loss and unique decision loss.
tests = read("tests/python/test_project_core_docs.py")
test_marker = "    def _copy_contract_files(self, destination: pathlib.Path) -> None:\n"
test_addition = '''    def test_roadmap_phase_history_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_contract_files(temp_root)
            roadmap = temp_root / "docs" / "OMENWARD_ROADMAP.md"
            roadmap.write_text(
                roadmap.read_text(encoding="utf-8").replace(
                    "## 7. P1 — Phase 0 Godot 기술 기준선 구현",
                    "## 7. P1 REMOVED",
                ),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("missing preserved section" in error for error in errors))

    def test_unique_decision_alternative_loss_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            temp_root = pathlib.Path(directory)
            self._copy_contract_files(temp_root)
            decisions = temp_root / "docs" / "DECISIONS_PENDING.md"
            decisions.write_text(
                decisions.read_text(encoding="utf-8").replace("4.6.3 대안 검토", "fallback removed"),
                encoding="utf-8",
            )
            errors = validate(temp_root)
            self.assertTrue(any("missing preserved alternative" in error for error in errors))

'''
tests = replace_once(tests, test_marker, test_addition + test_marker, "test insertion")
write("tests/python/test_project_core_docs.py", tests)

run("python", "tools/validate_project_core_docs.py")
run("python", "-m", "unittest", "discover", "-s", "tests/python", "-v")
run("python", "-m", "py_compile", "tools/validate_project_core_docs.py", "tests/python/test_project_core_docs.py")
run("python", "tools/validate_skill_system.py")

for relative in ("tools/_repair_project_core_recovery.py", "docs/_CORE_REPAIR_FAILURE.log", "project-core-repair.log"):
    path = ROOT / relative
    if path.exists():
        path.unlink()
for cache in ROOT.rglob("__pycache__"):
    for child in cache.iterdir():
        child.unlink()
    cache.rmdir()

run("git", "add", "-A")
run("git", "diff", "--cached", "--check")
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "commit", "-m", "restore roadmap history and add no-loss documentation guards")
run("git", "push", "origin", f"HEAD:{BRANCH}")
