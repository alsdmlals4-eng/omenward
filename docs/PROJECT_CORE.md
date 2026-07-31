# 오멘워드 프로젝트 코어

- 공식명: **오멘워드 / OMENWARD**
- 갱신일: `2026-08-01`
- 작업 모드: `PLAN / PLANNING_ONLY_PROFILE`
- 전달 목표: `FULL_SYSTEM_VERTICAL_SLICE / MINIMUM_CONTENT_BREADTH`
- 활성 Base: `v9.1`
- Base v9.3: `MIGRATION_PLANNING_ONLY / NOT_ADOPTED`
- 현재 제품: `LEGACY_PROTOTYPE`
- 최신 Vertical Slice: `NOT_IMPLEMENTED`
- 제품 코드·Codex·병합: `NOT_AUTHORIZED / BLOCKED`
- 자동 최신 계약·Runtime·사람 검증: `NOT_RUN`
- Core Lock: `NOT_ALLOWED`

이 문서는 제품 정체성, 핵심 인과, 불변 조건, 권위 경계와 작업 게이트를 소유한다. 세부 수치·콘텐츠·스키마는 분야별 승인 계약과 `DECISIONS_PENDING.md`가 소유한다.

## 1. 권위 순서

```text
최신 사용자 지시
→ PROJECT_CORE.md
→ 최신 분야별 APPROVED 계약
→ PROJECT_CANON_DECISION_LEDGER.md
→ DECISIONS_PENDING.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ 실제 Scene·Script·Resource·data·tests
→ 연결 Google Sheet
→ 시각 작업이면 docs/images/VISUAL_REFERENCE_INDEX.md와 실제 이미지
```

필수 게이트:

- `docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md`
- `docs/reviews/OMENWARD_COMPREHENSIVE_PROJECT_INTEGRITY_REVIEW_2026-08-01.md`
- `docs/operations/BENCHMARK_FIRST_PLANNING_RULE_2026-07-31.md`
- `docs/operations/CANON_SYNC_PROTOCOL_2026-07-31.md`

핵심 분야 계약:

- 전장·노드: `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_CONSTRUCTION_NODE_INVARIANTS_2026-08-01.md`
- 룰렛: `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
- 20 Stage·4막: `docs/design/APPROVED_VERTICAL_SLICE_20_STAGE_FOUR_ACT_AND_FIRST_10_MINUTES_CONTRACT_2026-07-31.md`
- 콘텐츠·미션: `docs/design/APPROVED_VERTICAL_SLICE_CONTENT_MANIFEST_AND_MISSION_CARD_POOL_2026-07-31.md`
- 위험 Stage·보스: `docs/design/APPROVED_VERTICAL_SLICE_DANGER_STAGE_AND_BOSS_PACKAGE_2026-07-31.md`
- 패배·재시도: `docs/design/APPROVED_VERTICAL_SLICE_DEFEAT_AND_PAID_RETRY_PRINCIPLE_2026-07-31.md`
- 안내자 벨루: `docs/design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md`

## 2. 현재 주요 Decision

- `OMW-DEC-20260731-CONTENT-MANIFEST-V1`
- `OMW-DEC-20260731-CANON-SYNC-V1`
- `OMW-DEC-20260731-DEFEAT-RETRY-V1`
- `OMW-DEC-20260731-DANGER-BOSS-V1`
- `OMW-DEC-20260731-MID-IMAGE-REVIEW-V1`
- `OMW-DEC-20260731-VISUAL-SCREEN-BOARD-V1` — `REJECTED_EVIDENCE`
- `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`
- `OMW-DEC-20260801-BELU-IDENTITY-V1`

## 3. 제품 정체성

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 토큰 구조를 설계·영구 편집한 뒤, 획득 병력을 어느 전선에 비가역적으로 커밋할지 결정해 전황을 뒤집는 실시간 전략 오토배틀 게임.**

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

핵심 루프:

```text
공세 확인
→ 건설·업그레이드·수리
→ 세 물리 릴 회전·영구 이동·확정
→ 보관·판매·라인 배치
→ 세 전선 자동전투
→ 접전지·중간 거점·본진 공방
→ 인과 복기·정산·checkpoint
```

## 4. 전장·건설 노드 불변 조건

전장은 하나이며 상·중·하 세 라인을 가진다.

```text
아군 본진
→ 아군 중간 거점
→ 중앙 접전지
→ 적 중간 거점
→ 적 본진
```

```text
node_kind = CONSTRUCTION_NODE_ONLY
nodes_per_base = 6 per faction
midpoint_outposts = 3 lanes × 2 factions = 6
nodes_per_midpoint_outpost = 3
nodes_per_clash_zone = 0
total_nodes = 2×6 + 6×3 = 30
```

- 본진·중간 거점은 노드 종류가 아니라 위치다.
- 방어·전진·특수·접전지 노드를 임의로 만들지 않는다.
- 중앙 접전지는 교전·점령 목적지이며 건설 장소가 아니다.
- 일반 병력은 라인 사이를 자유롭게 횡단하지 않는다.

## 5. 룰렛 불변 조건

```text
내부: 왼쪽·중앙·오른쪽 세 원형 TokenInstance 배열
화면: 각 릴의 연속 3칸으로 만든 3×3 정지 보드
TokenSource 1동: 같은 출처 토큰을 세 릴에 하나씩 공급
세로 이동: 선택 릴 cursor 회전
가로 이동: 노출 행 TokenInstance의 세 릴 순환 교환
가로 이동 결과: live 릴 배열에 영구 유지
기본 판정: 중앙 가로줄 동일 비-X 심벌 3개
```

- 멈춘 결과는 immutable `SpinSnapshot`에서 계산한다.
- source 변경은 기존 snapshot과 PendingReward를 소급 변경하지 않는다.
- 보상은 명시적 확정 한 번에만 생성·지급한다.
- 독립 원형 판 3개 또는 독립 9칸 추첨으로 표현하지 않는다.

## 6. 결과·전선 커밋

```text
룰렛 결과
→ PendingReward
→ 보관 / 판매 / 한 라인 배치
→ 자동 이동·교전·점령
→ 생존·HP·영토·건물 상태를 다음 Stage로 유지
```

- 보관 중 병력은 식량을 사용하지 않는다.
- 배치 후 라인 변경·회수·판매는 불가능하다.
- 식량 한도 감소는 신규 배치만 차단한다.
- 후방 거점 상실은 전진 병력을 강제 후퇴·약화·소멸시키지 않는다.
- 접전지·중간 거점 점령속도는 병력 수·Tier·등급으로 가속하지 않는다.

## 7. 건물·콘텐츠·MapRun

건물 가족:

| 건물 | 역할 | TokenSource |
|---|---|---|
| 금고 | 골드/초 | 금화 |
| 농장 | 식량 생산·한도 | 없음 |
| 타워 | 방어 공격 | 없음 |
| 병영 | 병종 생산 | 병종 |
| 지휘소 | 범위형 전장 버프 | 없음 |

콘텐츠 범위:

```yaml
stages: 20
acts: [1_to_5, 6_to_10, 11_to_15, 16_to_20]
battlefields: 1
battlefield_act_states: 4
standard_assault_templates: 8
danger_packages: 4
boss_behavior_packages: 3
tier_1_units: 1
tier_2_units: 10
tier_3_specializations: 20
mission_cards: 12
mission_offer_stages: [6, 11, 16]
```

- 위험 Stage는 5·10·15, 최종 위험 Stage는 20이다.
- 미션은 2장 중 1장 선택 또는 모두 거절한다.
- 목표·판정·실패·정확한 보상을 선택 전에 공개한다.
- 미션 보상 종류는 골드·사용 가능한 식량·추가 무료 회전이다.

패배·재시도:

```yaml
available_from_stage: 5
maximum_per_maprun: 1
restore_point: failed_stage_preparation_checkpoint
same_rng_lineage: true
exact_costs: pending_simulation
```

- 본진 HP 0은 기본 MapRun 종료다.
- 영구재화 차감과 checkpoint 복원은 원자 거래다.
- 개발 무료 재시도는 제품 보상·업적·기록과 분리한다.

## 8. 안내자 벨루

```text
CANONICAL_NAME_KO = 벨루
CANONICAL_NAME_EN = Belu
HISTORICAL_ALIAS = 율비
IDENTITY_RELATION = SAME_CHARACTER
```

- 과거 `요정 율비 시안.png`의 캐릭터와 기존 벨루는 동일 인물이다.
- 신규 UI·대사·에셋·데이터·파일명은 `벨루 / Belu / belu`로 통일한다.
- `율비`는 과거 시안 파일명과 변경 이력에서만 역사 별칭으로 보존한다.
- 벨루는 상황 설명·선택 근거·위험 경고·결과 반응을 제공한다.
- 벨루는 플레이어 대신 건설·릴 조작·병력 배치·전술 결정을 수행하지 않는다.
- 최종 애니메이션·음성·표정 조건·UI 배치는 미확정이다.

## 9. 현재 구현과 Legacy 경계

| 영역 | 현재 구현 | 최신 정본 |
|---|---|---|
| 룰렛 | 독립 9칸 가중 추첨 | 세 물리 릴·3×3 노출·영구 이동 |
| 노드 | 중간 거점 `front_a/front_b/rear` | 본진 6/진영·거점당 3·접전지 0·전체 30 |
| 건물 | 병영·타워·농장 | 다섯 건물 가족 |
| 점령 | `capture_power` 합산 | 고정시간 점령 계약 |
| 재시도 | 무료 동일 Stage 재시작 | Stage 5 이후 MapRun당 1회 유료 재시도 |
| UI·전장 | Label·code-drawn graybox | 제품 UI·제품 에셋 미구현 |

Legacy가 실행된다는 사실을 최신 Vertical Slice 구현 완료로 표시하지 않는다.

## 10. 시각·작업 상태

- 화면 명세 보드 V1: `REJECTED_EVIDENCE / DO_NOT_REUSE`
- 생성 이미지: `REJECTED_PROJECT_MISMATCH / RESET_REQUIRED`
- 최신 사용자 시각자료: 인덱스 등록, 바이너리 이전 `MIGRATION_PENDING`
- 벨루 정체성: `RESOLVED / CANONICAL_NAME_BELU`
- 화면 명세 보드 V2: `NOT_WRITTEN`
- 승인 제품 에셋: `NONE`
- 새 이미지: 사실표·독립 브리프 사용자 승인 전 `BLOCKED`

중형 이상 작업은 다음을 분리한다.

```text
CURRENT_CANON
CURRENT_IMPLEMENTATION
LEGACY_PROVEN
PROPOSED
REJECTED_EVIDENCE
UNRESOLVED
CONTRADICTION_REGISTER
OPEN_P0_P1
```

- 열린 P0는 이미지·제품 구현·최종 기획 승격을 차단한다.
- 열린 P1은 관련 영역 작업을 차단한다.
- 사용자 정정은 GitHub·Sheet·PR 재조회 전 완료로 보지 않는다.
- 실패 산출물은 `NOT_CREATED`로 되돌리지 않는다.

## 11. 검증 게이트

- `C0`: 정본·Decision·Pending·구현 상태·Sheet 일치.
- `C1`: 세 물리 릴·TokenSource·영구 이동·snapshot.
- `C2`: PendingReward·보관·판매·비가역 배치.
- `C3`: 5구간 전장·건설 노드 1종·`6/3/0=30`·건물 lifecycle.
- `C4`: 공용 병종·진영 Visual 분리·전투 계약.
- `C5`: 20 Stage·checkpoint·유료 Retry·개발 Retry 분리.
- `C6`: 100,000 seed 분포·1080p/720p·첫 플레이 인과·벨루 비모달 안내.

## 12. 현재 판정

```text
PROJECT_INTEGRITY_GATE: ACTIVE
BELU_IDENTITY: USER_CONFIRMED_CANON
BATTLEFIELD_TOPOLOGY_6_3_0_30: USER_CONFIRMED_CANON
VISUAL_SCREEN_BOARD_V1: REJECTED_EVIDENCE
CURRENT_PRODUCT: LEGACY_PROTOTYPE
LATEST_VERTICAL_SLICE: NOT_IMPLEMENTED
LATEST_CONTRACT_RED_TESTS: NOT_WRITTEN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: NOT_AUTHORIZED
CODEX_EXECUTION: BLOCKED
PR_MERGE: NOT_AUTHORIZED
CORE_LOCK: NOT_ALLOWED
```

다음 순서는 **최신 계약 Red 테스트 명세 → 화면 명세 보드 V2 → 대표 화면 중간 검수 → 수치·저장 계약 → 사용자 승인 구현 Plan**이다.
