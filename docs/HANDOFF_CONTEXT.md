# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: 2026-07-27
- 공식명: **오멘워드 / OMENWARD**
- 제품 단계: `PROTOTYPE_AND_VERTICAL_SLICE`
- 현재 Work Mode: `PLAN`
- 실행 프로필: `PLANNING_ONLY_PROFILE`
- 직전 REVIEW: `COMPLETE`
- 다음 작업: `V6_PLANNING_INTAKE`
- 현재 제품 Issue: `#69`
- 제품 코드 승인: `NO`
- 구현 상태: `V2_IMPLEMENTATION_NOT_STARTED`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 플레이: `HUMAN_QA_NOT_RUN`
- 잠금 상태: `CORE_LOCK_V2_PENDING`
- Codex 최종 인계: `DEFERRED_BY_USER_FOR_V6_PLANNING`

이 문서는 새 작업자가 이전 대화 없이 현재 승인 상태, 보호 경계, 실제 구현 상태와 다음 기획 시작점을 이해하기 위한 압축 인계다.

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 건물과 영구 가로 이동으로 세 원형 릴의 미래 배열을 설계하고 당첨 병력을 세 라인 중 하나에 비가역 배치하는 실시간 전략 오토배틀이다.
2. V2 제품 정본과 GM-01~GM-106 통합 결정은 승인됐지만 V2 Godot 제품 구현은 시작하지 않았다.
3. 현재 C1·C2·C3 실행 증거는 Legacy 설계 기준이며 V2 구현 완료 증거가 아니다.
4. R1+R2 범위와 기술 경계는 검수 완료 상태다.
5. F-30은 `construction progress → repair settlement` 순서로 해결되고 PR #93으로 검수 문서가 병합됐다.
6. 사용자는 다음 작업을 v6 기준 기획으로 계속하도록 지시했다.
7. 따라서 최종 Codex 인계와 Build는 자동 진행하지 않는다.
8. 공용 10병종·진영 Visual 분리, Godot 4.7.1 Standard·GDScript·Compatibility 기준선은 유지한다.

## 2. 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ docs/PROJECT_CORE.md
→ docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md
→ docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ docs/reviews/2026-07-27-v6-review-complete-planning-transition.md
→ docs/design/APPROVED_V2_CONSTRUCTION_REPAIR_SAME_TIMESTAMP_ORDER_2026-07-27.md
→ Issue #69
→ 현재 작업별 세부 정본
→ 실제 code/data/Scene/tests
→ docs/ACTIVE_CONTEXT.md
```

역사적 계획과 Pre-V2 벤치마크는 현재 제품 구현 근거로 사용하지 않는다.

## 3. 제품 약속

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 토큰 구조를 설계·영구 편집한 뒤, 당첨 병력을 어느 전선에 커밋할지 결정해 전황을 뒤집는다.**

핵심 감정:

```text
설계했다 → 릴 토큰·출처·인접 순서를 만들었다
읽어냈다 → 보드·공세·보관·식량을 비교했다
적중했다 → 비가역 배치가 전선을 뒤집었다
학습했다 → 실패 원인을 다음 건설·조작·배치에 반영했다
```

## 4. 현재 실제 구조

현재 `RouletteService`는 Legacy 독립 9칸 생성, 중앙 판정, 등급·금화, 출처 선택, 보상 생성, 경제와 입력 로그를 함께 소유한다. `StageRun`은 Legacy 결과를 pending reward에 보관한다.

```text
LEGACY_C1_C2_C3_PROVEN
!= V2_IMPLEMENTED
!= V2_PROVEN
```

## 5. 검수 완료된 R1+R2 경계

```text
Legacy RouletteService orchestration
├─ paid spin economy
├─ legacy independent 9-cell generation
├─ legendary conversion and reward creation
└─ pure RouletteBoardResolver delegation

Isolated V2 transient RefCounted domain
caller-injected RouletteTokenInstance
→ RouletteReelState × 3
→ RouletteRunState
→ RouletteSpinSnapshot
→ stopped-only RouletteSpinSession
```

### 포함

- 중앙 가로줄 선행 판정·8개 완성선·등급·금화·출처 결정론 보존.
- Legacy service adapter.
- caller-injected token instance ID.
- transient `RefCounted` 원형 릴 도메인.
- `NORMAL_X` 최저 안정 index 교체, 없으면 append.
- `SOURCE_BOUND_X` 일반 교체 제외.
- 전역 token ID 유일성.
- 동일 상태·시드의 동일 정지 index.
- copy-out deep immutable snapshot.
- 이동·확정 없는 stopped session seam.

### 제외

- live `spin()`의 V2 물리 릴 전환.
- TokenSource lifecycle.
- StageRun·MapRun·건물·경제·UI·보관·배치 연결.
- 세로·가로 이동 실행.
- 럭키·이동 아이템·전설·원자 확정 거래.
- Scene·아트·사운드·사람 플레이·분포 시뮬레이션.

## 6. F-30 승인 순서

```text
construction progress
→ lifecycle·allowed max HP 갱신
→ target 유효성
→ repair request 적용
→ 글로벌 affordability
→ debit
→ heal
```

책임 원본:

- `docs/design/APPROVED_V2_CONSTRUCTION_REPAIR_SAME_TIMESTAMP_ORDER_2026-07-27.md`
- `docs/reviews/2026-07-27-v2-construction-repair-same-timestamp-order-review.md`

## 7. 다음 v6 기획 목표

다음 세션은 구현 계획 재개가 아니라 Stage 2 통합 데모 기획을 진행한다.

1. `CORE_POC`에서 가장 위험한 플레이 가설 하나를 선택한다.
2. 플레이어 행동·고민·감정·실패 후 행동 변화·관찰 지표를 정의한다.
3. 대표 3스테이지 Vertical Slice의 첫인상부터 데모 종료까지 설계한다.
4. 설계 청사진·전선 대응 브리핑·전투 인과 사슬의 UX 역할을 정한다.
5. 마스코트 또는 상징 동반자의 세계관·UI·세일즈 역할을 정한다.
6. UI·사운드·에셋은 역할 정의 후 기존 승인·보유·스토어 조사 순서로 접근한다.
7. Codex Goal과 Plan Mode 인계는 기획 승인 뒤 별도 작업으로 작성한다.

## 8. 현재 미검증

- V2 Godot 실행 경로.
- R1+R2 자동 계약과 원격 실행 증거.
- live physical reel.
- CORE_POC 사람 플레이.
- 10~15분 Vertical Slice 흐름.
- 1080p·720p 가독성.
- 저장·복귀·성능.
- 마스코트 실제 적용·기억도.

## 9. 금지된 완료 표현

다음 조건 전에는 `CORE_LOCK_V2`, `V2_IMPLEMENTED`, `CORE_LOOP_PROVEN`, `MVP_COMPLETE`를 사용하지 않는다.

- 해당 V2 실행 경로 구현.
- 자동 계약과 원격 실행 증거.
- 10~15분 사람 플레이.
- 1080p·720p 가독성 검증.

```text
NEXT_WORK_MODE: PLAN
NEXT_EXECUTION_PROFILE: PLANNING_ONLY_PROFILE
FINAL_CODEX_HANDOFF: DEFERRED
PRODUCT_CODE_AUTHORIZED: NO
```
