# 승인된 V2 건설 진행·수리 정산 동일 시각 순서

- 승인일: 2026-07-27
- 상태: `V2_SPEC_APPROVED / REVIEW_COMPLETE / PRODUCT_CODE_NOT_AUTHORIZED`
- Finding: `F-30`
- 검수 근거: `docs/reviews/2026-07-27-v2-construction-repair-same-timestamp-order-review.md`
- 병합 근거: PR `#93` / `8b0d8aac5784813b1c4e765634b44dc64f782959`
- 적용 범위: 건설 중 플레이어 소유 구조물의 live construction progress와 repair settlement가 같은 deterministic simulation timestamp에 도달한 경우

이 문서는 `APPROVED_V2_TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATED_2026-07-26.md`의 다음 미결 필드를 대체한다.

```text
CONSTRUCTION_PROGRESS_REPAIR_SETTLEMENT_SAME_TIMESTAMP_ORDER: REVIEW_PENDING
```

## 1. 승인 순서

```text
CONSTRUCTION_PROGRESS_REPAIR_SETTLEMENT_SAME_TIMESTAMP_ORDER:
1. construction progress 적용
2. progress 기반 lifecycle·construction allowed max HP 갱신
3. HP 0·삭제·소유권 상실 등 target 유효성 판정
4. 최신 repair worker request 적용
5. 글로벌 affordability와 작업자 자동 해제
6. 실제 임금 차감
7. post-progress lifecycle·허용 최대 HP 기준 실제 치유
8. 최대 HP 도달 시 작업자 해제
```

압축하면 다음과 같다.

```text
CONSTRUCTION_PROGRESS
→ POST_PROGRESS_STATE
→ TARGET_VALIDATION
→ REPAIR_AFFORDABILITY
→ DEBIT
→ HEAL
```

## 2. 이유

- 수리 가능량은 settlement 시점의 `construction_allowed_max_hp`를 사용한다.
- 같은 timestamp에 건설이 완료되면 수리는 완료 후 실제 lifecycle과 `RepairProfile`을 사용한다.
- 진행 기반 상태를 먼저 갱신해야 동일 입력 로그에서 단일하고 설명 가능한 결과가 나온다.
- 수리를 먼저 처리해 새 HP cap과 완료 lifecycle 반영을 다음 초까지 지연하지 않는다.
- 무료 치유를 만들지 않는다. 실제 치유량만 비용 basis가 되며 overheal 비용은 0이다.

## 3. 경계

### Cap만 증가

건설 진행 후 증가한 cap 범위 안에서만 유료 치유한다.

### 같은 timestamp에 완공

완공 lifecycle 전환 뒤 active structure 규칙으로 수리한다. 완공 자체는 HP를 무료로 채우지 않는다.

### Target 무효

HP 0, 삭제, 소유권 상실 등으로 무효가 되면 요청을 종료하며 금화 차감·치유·자동 재지정은 0이다.

### 글로벌 금화 부족

post-progress 상태에서 유효한 요청만 모으고 기존 한계 임금 → HP 비율 → `StableStructureId` tie-break를 유지한다.

## 4. 비적용 범위

- 같은 timestamp의 공격·피해와 수리 사이의 전체 전투 event order
- construction progress 자체의 HP 공식과 cap 곡선 수치
- 위험 전투에서 provisional repair setting 허용 여부
- R1+R2 룰렛 기반 패키지 범위
- Godot 제품 구현, Scene, Resource, 데이터, workflow

## 5. 구현 검증 계약

후속 구현 패키지는 최소 다음 Red 테스트를 포함한다.

1. 미완성 건물의 cap 증가와 같은 boundary 수리.
2. 정확히 settlement boundary에서 완공되는 건물.
3. boundary 직전 HP 0 target.
4. post-progress cap clamp와 실제 치유량 비례 비용.
5. 여러 구조물의 글로벌 affordability와 안정 tie-break.
6. 동일 입력 로그의 동일 결과.
7. 중복 settlement transaction의 중복 효과 방지.
8. 순서 반전 mutation 거부.

```text
F-30: RESOLVED
ORDER: CONSTRUCTION_PROGRESS_THEN_REPAIR_SETTLEMENT
USER_DECISION_REQUIRED: NO
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
```
