# Active Context

- 갱신일: `2026-08-01`
- 공식명: **오멘워드 / OMENWARD**
- Work Mode: `PLAN`
- 제품: `LEGACY_PROTOTYPE`
- 최신 Vertical Slice: `APPROVED_CANON / NOT_IMPLEMENTED`
- Screen Board V2: `TEXT_SPEC_CURRENT / SYNC_VERIFIED / IMAGE_NOT_GENERATED`
- 경제·Retry·저장: `STRUCTURE_CURRENT / EXACT_VALUES_PENDING / SIMULATION_NOT_RUN`
- 제품 코드·Codex: `NOT_AUTHORIZED / BLOCKED`
- PR: `#116 DRAFT / OPEN / NOT_MERGED`
- 마지막 관찰 CI: `BASE_ADOPTION_PASS / PROJECT_CORE_FAIL / GDD_SHEET_FAIL`
- Runtime·사람 검증: `NOT_RUN / NOT_RUN`
- 활성 Base: `v9.1`
- 권장 다음 Base: `v9.3 / SEPARATE_ATOMIC_MIGRATION`

## 1. 기준선

```yaml
project: OMENWARD / 오멘워드
platform: PC_PRIMARY
engine: Godot 4.7 / GDScript / Compatibility
viewport: 960x540
window_override: 1920x1080
scaling: integer
current_branch: main
context_baseline_commit: 774087dccc903bc9a8e2aec72eec2a2d13b216ce
active_base_version: 9.1.0
active_base_release: 3c158f52cfdad889970aef4d6ce6650a6fea0645
active_base_evidence: dd20ad3852e264d7e337e34d2cb963f71053a6cb
recommended_base_version: 9.3.0
product_code_authority: NONE
codex_execution: BLOCKED
```

## 2. 프로젝트 약속

> 세 물리 릴을 건물과 TokenSource로 설계하고, 남은 무작위성을 감수해 얻은 병력을 한 전선에 비가역 커밋하며, 전투 결과의 원인을 다음 설계에 반영한다.

```text
공세 예고
→ 건설·세 물리 릴 설계
→ 회전·이동·SpinSnapshot·확정
→ PendingReward 보관/판매/배치
→ 세 라인 자동전투·고정시간 점령
→ 정산·인과 복기
```

## 3. 승인 불변 조건

- 35분·20 Stage·4막·위험 Stage 5/10/15/20.
- 하나의 전장·상/중/하 세 라인.
- 본진 6노드/진영·중간 거점 6곳×3·접전지 0·전체 30노드.
- 세 물리 릴·TokenInstance·cursor·3×3 노출 보드.
- 가로 이동은 TokenInstance 전체를 영구 교환; 실행 뒤 undo/reset 없음.
- immutable SpinSnapshot.
- PendingReward 보관·판매·한 라인 배치; 배치 뒤 변경·회수·판매 없음.
- 고정시간 점령.
- 금고·농장·타워·병영·지휘소 5건물.
- Stage 5 이후 MapRun당 최대 1회 제품 유료 Retry.
- 정본 안내자 `벨루 / Belu`.

## 4. 경제·Retry·저장 계약

Decision: `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1`

```text
MapRun 경제와 Profile 경제 분리
Act 단위 비감소 유료 회전가
무료 회전 금화는 현재 Act 유료 회전 reference cost 사용
n번째 이동 비용 = n×P
보관 병력 식량 0 / 배치 시 식량 예약
제한된 profile 시작 보관 용량 tier
Stage 5~10=T1 / 11~15=T2 / 16~20=T3 / T1<T2<T3
동일 seed·공세·미션·룰렛 RNG lineage Retry
ProfileSave / RunCheckpoint / Settings / Journal / Backup 분리
안정 planning 경계 checkpoint·원자 save·복구
```

- Parameter Registry: `CURRENT / null=NOT_APPROVED`.
- 100K simulation contract: `CURRENT / NOT_RUN`.
- Red extension: `WRITTEN / TEST_FILES_NOT_CREATED`.
- 과거 160골드·20회전가·70/50/40 환급은 `LEGACY_CANDIDATE_H0`.
- 실제 비용·획득량·schema 값은 미확정.

## 5. Screen Board V2

Decision: `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2`

- OM-IMG-011~018 text canon·Sheet read-back `PASS`.
- 기초 이미지 순서 `013 → 015`.
- 시각자료 바이너리 이관 전 이미지 생성 차단.

## 6. 실제 구현 경계

```text
CURRENT_LEGACY
- Battlefield + Label HUD + StageSelect
- 독립 가중치 9칸 Roulette
- 병영·타워·농장
- front_a/front_b/rear
- capture_power 점령
- 무료 same-stage restart

LATEST_NOT_IMPLEMENTED
- 30노드 제품 topology
- 세 물리 릴·영구 이동·full snapshot transaction
- 5건물 최신 경제·고정시간 점령
- ProfileSave·RunCheckpoint·paid Retry·transaction journal
- Screen Board V2 제품 UI·벨루 Runtime
```

## 7. 현재 P1

1. Project Core·GDD Sheet CI validator 실패.
2. 최신 Red test files·expected failure 미실행.
3. 경제 exact values·simulator·100K·fault injection 미실행.
4. 시각자료 바이너리 이관·Visual Index 재검증 미완료.
5. Base v9.3 Adapter 원자 migration 미실행.

## 8. 우선 읽기

1. `AGENTS.md`
2. `docs/DOCUMENTATION_MAP.md`
3. `docs/PROJECT_CORE.md`
4. `docs/design/APPROVED_OMENWARD_ECONOMY_RETRY_SAVE_CHECKPOINT_PLANNING_CONTRACT_2026-08-01.md`
5. `docs/design/OMENWARD_ECONOMY_RETRY_SAVE_PARAMETER_REGISTRY_V1.json`
6. `docs/testing/OMENWARD_ECONOMY_META_RETRY_100K_SIMULATION_CONTRACT_2026-08-01.md`
7. `docs/PROJECT_CANON_DECISION_LEDGER.md`
8. `docs/DECISIONS_PENDING.md`
9. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
10. 실제 code/data/Scene/tests와 Sheet

## 9. 다음 작업

```text
경제·Retry·save Sheet 동기화·read-back
→ 100K simulator Work Order·Candidate H0/H1/H2
→ 시각자료 바이너리 이관·Visual Index 재검증
→ OM-IMG-013 독립 이미지 중간 검수
→ 최신 Red test Work Order·expected-failure package
→ Base v9.3 원자 migration package
→ validator Green
→ 사용자 승인 Codex 제품 구현 Plan
```

```text
PRODUCT_CODE: NOT_AUTHORIZED
SIMULATION: NOT_RUN
IMAGE_GENERATION: BLOCKED
CODEX: BLOCKED
PR_READY: NO
PR_MERGE: BLOCKED
```