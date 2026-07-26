# V2 건설 진행·수리 정산 동일 시각 순서 기술 검수

- 검수일: 2026-07-27
- 검수 ID: `F-30`
- Finding route: `TECHNICAL_REVIEW_PROPOSAL`
- 판정: `RESOLVED_BY_TECHNICAL_REVIEW`
- 사용자 결정 필요: `NO`
- 제품 구현: `V2_IMPLEMENTATION_NOT_STARTED`
- 제품 코드 승인: `NO`
- 최종 Codex 인계: `NOT_AUTHORIZED`

## 1. 검수 대상

다음 미결 순서를 검수한다.

```text
construction progress와 repair settlement가 같은 live timestamp에 도달했을 때
어느 처리를 먼저 적용하는가?
```

책임 원본:

- `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`
- `docs/design/APPROVED_V2_REPAIR_SETTINGS_DEFERRED_LIVE_SETTLEMENT_2026-07-26.md`
- `docs/design/APPROVED_V2_TACTICAL_PLANNING_BUILDING_WORK_CONSOLIDATED_2026-07-26.md`
- `docs/reviews/2026-07-26-v2-tactical-planning-building-work-consolidation-review.md`

## 2. 기술 판정

```text
CONSTRUCTION_PROGRESS_REPAIR_SETTLEMENT_SAME_TIMESTAMP_ORDER:
1. construction progress와 progress 기반 lifecycle·허용 최대 HP 갱신
2. HP 0·삭제·소유권 상실 등 target 유효성 판정
3. 최신 repair worker request 적용
4. 글로벌 affordability와 작업자 자동 해제
5. 실제 임금 차감
6. post-progress lifecycle·허용 최대 HP를 기준으로 실제 치유
7. 최대 HP 도달 시 작업자 해제
```

즉, **건설 진행을 먼저 적용하고 수리 정산을 나중에 적용한다.**

## 3. 판정 근거

1. 통합 계약은 수리 가능량을 `construction_allowed_max_hp_at_settlement`로 계산한다. 정산 시점의 authoritative progress를 먼저 반영해야 이 값이 단일하게 결정된다.
2. 건설이 정산 경계에서 완료되면, 기존 계약의 “settlement 시점의 실제 lifecycle” 원칙에 따라 완공된 active structure 규칙을 적용해야 한다.
3. 통합 결정 원장의 성문 재건 동일 timestamp 계약도 `진행 증가 → 진행 기반 효과 → 후속 사건` 순서를 사용한다. 진행 기반 상태를 먼저 갱신하는 것이 기존 결정론과 일치한다.
4. 수리를 먼저 적용하면 같은 timestamp에 새로 열린 HP cap 또는 완공 lifecycle을 다음 정산까지 사용하지 못해, 플레이어에게 설명하기 어려운 1초 지연이 생긴다.
5. 이 순서는 무료 치유를 만들지 않는다. 수리는 실제 치유량에 대해서만 고정소수점 임금을 차감하며 overheal 비용은 없다.

## 4. 경계 사례

### 4.1 건설 진행으로 HP cap만 증가

```text
기존 허용 최대 HP 40
→ 같은 timestamp 건설 진행 후 허용 최대 HP 50
→ 현재 HP 35
→ 수리 정산은 missing HP 15 범위에서만 유료 치유
```

### 4.2 같은 timestamp에 건설 완료

- progress 적용 뒤 lifecycle을 `ACTIVE`로 전환한다.
- 수리 정산은 active structure의 최대 HP와 `RepairProfile`을 사용한다.
- 완료 자체로 무료 수리하지 않는다.

### 4.3 정산 전 HP 0 또는 target 무효

- repair request를 종료한다.
- 금화 차감과 치유는 0이다.
- 다른 구조물로 자동 이전하지 않는다.

### 4.4 글로벌 금화 부족

- post-progress 상태에서 유효한 요청만 모은다.
- 기존 한계 임금·HP 비율·`StableStructureId` tie-break를 유지한다.
- 실제 유지된 작업자와 실제 치유량만 비용에 반영한다.

## 5. 변경하지 않는 범위

- 같은 timestamp의 전투 공격·피해 처리 순서는 이번 Finding에서 정하지 않는다.
- 건설 progress 자체의 HP 증가 공식이나 허용 최대 HP 곡선 수치를 정하지 않는다.
- 위험 전투의 provisional repair 설정 허용 여부를 정하지 않는다.
- R1+R2 룰렛 기반 패키지 범위를 확장하지 않는다.
- Godot 코드, Scene, Resource, 게임 데이터, workflow를 승인하지 않는다.

## 6. 구현 인계 시 필수 Red 테스트

1. 미완성 건물의 cap 증가와 같은 boundary 수리.
2. 정확히 정산 boundary에서 완공되는 건물.
3. boundary 직전 HP 0이 된 target.
4. post-progress cap보다 큰 요청의 clamp와 실제 치유량 비례 비용.
5. 여러 구조물의 글로벌 affordability와 안정 tie-break.
6. 동일 입력 로그의 동일 결과.
7. 중복 settlement transaction의 무효화 또는 동일 receipt.
8. 순서 반전 mutation이 계약 테스트에서 실패하는지 확인.

## 7. Finding 결과

```text
F-30: RESOLVED_BY_TECHNICAL_REVIEW
ORDER: CONSTRUCTION_PROGRESS_THEN_REPAIR_SETTLEMENT
USER_DECISION_REQUIRED: NO
R1_R2_SCOPE_CHANGE: NONE
V2_IMPLEMENTATION: NOT_STARTED
PRODUCT_CODE_AUTHORIZED: NO
FINAL_CODEX_HANDOFF: BLOCKED_UNTIL_EXACT_REVIEW_COMPLETE_COMMAND
```

이 Finding은 플레이어 약속·핵심 루프·주요 UX·콘텐츠 의미·프로젝트 범위를 변경하지 않는 결정론적 simulation ordering이다. 따라서 v6 계약의 `TECHNICAL_REVIEW_PROPOSAL` 경로로 처리하며 추가 사용자 선택지를 요구하지 않는다.

## 8. Skill Execution Evidence

| 책임 | Skill·Mode | 실제 산출물 | 증거 | 상태 |
|---|---|---|---|---|
| 현재 컨텍스트 라우팅 | `managing-project-intake-and-work-contract: route/contract` 상당 절차 | F-30 단일 검수 범위 | AGENTS·Documentation Map·Active/Handoff Context·Issue #69 대조 | `FALLBACK_USED` |
| 적대적 검토 | `running-adversarial-review-and-refinement: attack/validate-critique/route-findings` 상당 절차 | 순서 후보 공격·반례·기술 판정 | F-29 잔여 항목, GM-64·GM-84, 수리·건설 통합 계약 대조 | `FALLBACK_USED` |
| 정본 최신성 | `auditing-canonical-reference-freshness` 상당 절차 | 최신 main과 후속 통합 정본 확인 | `4368cde451178a25b40dfae79514fe3e38addec1` 기준 | `FALLBACK_USED` |
| 완료 전 검증 | Superpowers `verification-before-completion` | placeholder·범위·상태·필수 마커 검사 | 문서 생성 전 자동 검사 | `EXECUTED_AND_EVIDENCED` |

Base 공용 Skill 본문은 현재 대화 도구로 직접 실행되지 않았으므로 실행했다고 주장하지 않고, 프로젝트 계약에 따른 동등 절차를 `FALLBACK_USED`로 기록한다.
