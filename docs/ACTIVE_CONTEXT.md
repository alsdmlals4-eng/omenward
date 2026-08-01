# Active Context

- 갱신일: 2026-07-27
- 공식명: **오멘워드 / OMENWARD**
- 제품 단계: `PROTOTYPE_AND_VERTICAL_SLICE`
- 현재 Work Mode: `PLAN`
- 실행 프로필: `PLANNING_ONLY_PROFILE`
- 직전 단계: `REVIEW_COMPLETE`
- 다음 작업: `V6_PLANNING_INTAKE`
- 현재 제품 Issue: `#69`
- 제품 코드 승인: `NO`
- 구현 상태: `V2_IMPLEMENTATION_NOT_STARTED`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 잠금: `CORE_LOCK_V2_PENDING`
- 최종 Codex 인계: `DEFERRED_BY_USER_FOR_V6_PLANNING`
- 별도 운영 작업: Issue `#62`

## 1. Context Pack

```yaml
project: OMENWARD / 오멘워드
target_platform: PC
current_stage: PROTOTYPE_AND_VERTICAL_SLICE
current_work_mode: PLAN
execution_profile: PLANNING_ONLY_PROFILE
current_branch: main
context_baseline_commit: c4c02dc553dbf6e79fe26fc751bd268bd396c627  # PR #94 v6 전환 병합 기준
player_promise: 예고된 세 전선의 공세를 읽고 건물과 영구 가로 이동으로 미래 릴을 설계한 뒤 당첨 병력을 한 전선에 비가역 커밋한다.
project_core: 정확 공세 예고 + TokenSource + 세 원형 릴 + immutable snapshot + 명시적 확정 + 3라인 자동전투
pointed_fun: 무작위 결과 소비가 아니라 미래 룰렛 구조를 설계하고 그 결과를 전선에 커밋하는 판단
current_slice_or_goal: v6 기준 CORE_POC와 Vertical Slice 사이의 가장 위험한 플레이 가설 재정의
protected_decisions_and_assets: Legacy C1 판정, 3라인, 공용 병종, 진영 Visual 분리, immutable SpinSnapshot, 비가역 배치
canonical_sources: PROJECT_CORE, 통합 결정 원장, R1+R2 검수, F-30 승인 정본, Documentation Map
actual_build_state: V2 제품 구현 미시작, Legacy C1~C3만 실행 증거 보유
open_conflicts: 없음. 다음 PLAN에서 새 충돌이 발견되면 한 문항씩 처리
blocked_unverified: V2 실행 경로, 사람 플레이, 1080p·720p, 성능, 저장·복귀, 마스코트 실제 적용
next_evidence_needed: CORE_POC 가설·관찰 기준·실패 기준과 3스테이지 Slice 후보
```

`context_baseline_commit`은 이 Context Pack이 확정된 전환 병합 기준이다. 현재 `main` HEAD를 자기참조 방식으로 고정하는 필드가 아니다.

## 2. 우선 읽기

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/PROJECT_CORE.md`
5. `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`
6. `docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md`
7. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
8. `docs/reviews/2026-07-27-v6-review-complete-planning-transition.md`
9. `docs/design/APPROVED_V2_CONSTRUCTION_REPAIR_SAME_TIMESTAMP_ORDER_2026-07-27.md`
10. Issue `#69`
11. 현재 작업에 필요한 세부 정본과 실제 파일

## 3. 핵심 문장

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

오멘워드는 좋은 슬롯 결과를 기다리는 게임이 아니다. 플레이어가 공개된 전선 위험을 읽고 건물과 영구 이동으로 미래 릴 배열을 설계하며, 결과를 한 라인에 되돌릴 수 없이 커밋하는 게임이다.

## 4. 보호 대상

- 일반 유닛의 자유로운 라인 횡단 금지.
- 기본·일반 난이도에서 치명적 공세 정보 공개.
- 중앙 가로줄 선행 판정과 기존 C1 결과.
- 가로 이동은 token instance와 출처를 이동시키며 길이·cursor를 유지.
- immutable `SpinSnapshot`.
- 배치 후 회수·라인 변경·판매 금지.
- 공용 `UnitArchetypeProfile`과 진영 Visual 분리.
- UI는 규칙을 계산하지 않고 표시와 사용자 의도 반환만 담당.
- Godot 4.7.1 Standard / GDScript / Compatibility renderer.

## 5. 직전 REVIEW 결과

```text
R1_PLUS_R2_SCOPE: APPROVED_AND_UNCHANGED
LEGACY_C1_PRESERVATION: SOUND
PURE_DOMAIN_ISOLATION: SOUND
F-30: RESOLVED
F-30_ORDER: CONSTRUCTION_PROGRESS_THEN_REPAIR_SETTLEMENT
REVIEW_PHASE: COMPLETE
PRODUCT_CODE_AUTHORIZED: NO
```

PR #93은 F-30 기술 검수 문서만 병합했다. Godot 코드·Scene·Resource·게임 데이터·workflow를 구현하지 않았다.

## 6. 현재 포함·제외

### R1+R2 포함

- 순수 `RouletteBoardResolver`와 Legacy adapter.
- caller-injected token ID.
- transient `RefCounted` 세 원형 릴 도메인.
- 결정론적 정지 index와 deep immutable snapshot.
- 이동·확정 없는 stopped-only `RouletteSpinSession`.

### 계속 제외

- live `RouletteService.spin()`의 V2 전환.
- TokenSource lifecycle과 건물·경제·StageRun·MapRun 연결.
- 세로·가로 이동 실행.
- 럭키·이동 아이템·전설·원자 확정 거래.
- UI·Scene·아트·사운드·사람 플레이·100,000시드.

## 7. 다음 v6 PLAN

우선순위는 다음과 같다.

1. CORE_POC의 가장 위험한 플레이 가설 하나 선택.
2. 플레이어 행동·감정·실패 후 변화·관찰 지표 정의.
3. 대표 3스테이지 Vertical Slice 흐름과 종료점 설계.
4. 설계 청사진·전선 브리핑·전투 인과 사슬 UX 역할 설계.
5. 마스코트·상징 동반자 역할 설계.
6. 에셋·UI·사운드 조달과 검증 계획.
7. Codex Goal은 기획 승인 뒤에만 작성.

```text
NEXT_WORK_MODE: PLAN
NEXT_EXECUTION_PROFILE: PLANNING_ONLY_PROFILE
FINAL_CODEX_HANDOFF: DEFERRED
CODEX_BUILD: NOT_AUTHORIZED
```

## Base v9.4 운영 계약

- adapter에 Base `9.4.0` payload/evidence를 적용했다.
- 제품 코드·데이터·Scene·Resource·자산·Sheet는 변경하지 않는다.
- 런타임·입력·사람·provider 검증은 `NOT_RUN` 또는 `HUMAN_NOT_RUN`이다.
