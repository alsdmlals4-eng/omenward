# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: 2026-07-26
- 현재 상태: `V2_SPEC_APPROVED / V2_CANON_CURRENT_BY_PR_57_MERGE / V2_IMPLEMENTATION_NOT_STARTED`
- 현재 단계: `PLANNING_COMPLETE / REVIEW_IN_PROGRESS`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 플레이: `HUMAN_QA_NOT_RUN`
- 잠금 상태: `CORE_LOCK_V2_PENDING`
- 현재 제품 Issue: `#69`
- 현재 패키지: `R1_PLUS_R2_SCOPE_APPROVED_AND_UNCHANGED`
- 제품 코드 승인: `NO`
- 현재 계획: `docs/superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md`
- 현재 검수: `docs/reviews/2026-07-26-v2-r1-r2-planning-review.md`
- 벤치마크 갱신: `docs/benchmarks/OMENWARD_V2_BENCHMARK_REFRESH_2026-07-26.md`
- 별도 운영 Issue: `#62`
- 프로젝트 코어: `docs/PROJECT_CORE.md`
- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

이 문서는 새 작업자가 이전 대화 없이 현재 제품 방향, 승인 규칙, 구현 경계와 다음 조사 순서를 이해하기 위한 출발점이다.

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 건물과 가로 이동으로 세 원형 릴의 미래 배열을 설계하고, 당첨 병력을 세 라인 중 하나에 영구 배치하는 실시간 전략 오토배틀이다.
2. PR #57에서 GM-01~GM-106 통합 결정 원장과 V2 제품 정본이 `main`에 병합됐다.
3. 현재 main의 C1·C2·C3는 기존 설계 기준 실행 증거이며 V2 구현 완료 증거가 아니다.
4. V2 Godot 제품 코드와 게임 데이터 구현은 아직 시작하지 않았다.
5. PR #65·#66·#67·#68은 Skill·아카이브·공용 어댑터·상태 동기화 작업이며 제품 구현이 아니다.
6. PR #70은 R1+R2 Plan Mode 입력과 구현 계획 초안을 병합했지만 제품 코드 승인이 아니다.
7. 사용자는 첫 패키지로 R1+R2 범위를 선택했고 정확히 `기획 완료`를 선언했다.
8. 현재는 적대적 검수 단계다. 정확한 `검수 완료` 전에는 최종 Codex 인계를 발행하지 않는다.
9. 공용 10병종과 진영 Visual 분리, Godot 4.7.1 Standard·GDScript·Compatibility 기준선은 유지한다.
10. 전술 아이템 룰렛 심벌과 코어 PoC mid-run save는 현재 코어 범위가 아니다.

## 2. 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ docs/PROJECT_CORE.md
→ docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md
→ docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md
→ docs/design/APPROVED_ROULETTE_CORE_RULES.md
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ Issue #69
→ docs/reviews/2026-07-26-v2-r1-r2-planning-review.md
→ docs/benchmarks/OMENWARD_V2_BENCHMARK_REFRESH_2026-07-26.md
→ docs/superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md
→ 실제 code/data/Scene/tests
→ docs/ACTIVE_CONTEXT.md
```

`docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`는 구형 main과 Issue #56 기준 역사적 초안이다. 현재 구현 근거로 사용하지 않는다.

기존 `docs/benchmarks/0001-core-game-benchmark-proposal.md` 계열은 Pre-V2 조사 이력이다. 현재 적용 판정은 V2 벤치마크 갱신 문서를 따른다.

## 3. 제품 약속

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 토큰 구조를 설계·영구 편집한 뒤, 당첨 병력을 어느 전선에 커밋할지 결정해 전황을 뒤집는다.**

시장 구분:

> 오멘워드는 좋은 슬롯 결과를 기다리는 게임이 아니다. 건물을 지어 토큰 출처를 만들고, 세 원형 릴의 미래 배열을 영구 편집한 뒤, 그 결과를 세 전선 중 하나에 커밋한다.

핵심 플레이 감정:

```text
설계했다 → 릴 토큰·출처·인접 순서를 만들었다
읽어냈다 → 보드·공세·보관·식량을 비교했다
적중했다 → 비가역 배치가 전선을 뒤집었다
학습했다 → 실패 원인을 다음 건설·조작·배치에 반영했다
```

## 4. 현재 실제 구조

`RouletteService`는 현재 다음을 한 객체에 함께 소유한다.

- 독립 9칸 가중 생성.
- 중앙 가로줄 판정과 8개 완성선.
- 등급·금화 보상.
- 출처 선택과 UnitSpawnDefinition 생성.
- 스테이지 전설 생성 상태.
- 경제 차감·금화 지급·입력 로그.

`StageRun`은 `RouletteService`를 만들고 결과를 pending reward에 보관한다. 기존 회귀는 `roulette_contract_test.gd`와 `stage_run_test.gd`가 보호한다.

## 5. 검수 후 R1+R2 구조

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

### R1 포함

- 중앙 가로줄 선행 판정.
- 8개 완성선·1/2/3~7/8 등급.
- 금화 75/200/500%.
- 동일 입력·시드 출처 결정론.
- `RouletteService`의 resolver 위임.
- 기존 C1 관찰 결과 불변.

### R2 포함

- caller-injected token instance ID.
- transient `RefCounted` state.
- `NORMAL_X`, `SOURCE_BOUND_X`, 일반 심벌 타입 경계.
- 길이 3 이상 원형 릴과 wrap.
- 최저 안정 배열 index `NORMAL_X` 교체, 없으면 append.
- 정확히 세 릴, 전역 token ID 유일성.
- 동일 상태·시드의 동일 정지 index.
- copy-out 방식의 깊은 불변 snapshot.
- row-major 3×3 board projection.
- 이동·확정이 없는 stopped session seam.

### 제외

- live `spin()`의 V2 릴 전환.
- TokenSource 완공·파괴·blocked 이벤트.
- 건물·경제·StageRun·MapRun·UI·보관·배치 연결.
- 세로·가로 이동.
- 럭키·이동 아이템·전설 위험 주기.
- `[확정]`·PendingReward V2 거래.
- 설계 청사진 UI, 전선 대응 브리핑, 전투 인과 보고.
- 런 청사진 저장, Scene·아트·사람 플레이·분포 시뮬레이션.

## 6. 벤치마크 반영 경계

### 후속 V2 UX 요구사항

- 설계 청사진: 전체 릴 배열, cursor, 출처, X 종류, 고스트 배열.
- 전선 대응 브리핑: 위협, 위험 이유, 현재 대응 자원, 미해결 위험.
- 전투 인과 사슬: 건물→토큰→snapshot→보상→배치→전투 결과.

### 새 코어 규칙이 아닌 UX 표현

- 설계 점검 구간은 강제 pause나 별도 planning phase가 아니다.
- 런 청사진은 맵 종료 로컬 요약만 의미한다.

### 제외

- 지형·경로 편집.
- 직접 영웅 조작.
- 일반 슬롯 덱빌더식 회전 후 심벌 선택.
- 무제한 리롤·무료 재배치.
- 온라인 PvP·시즌 랭크.
- 초기 대규모 조합 폭발.

## 7. Codex가 다시 결정하지 않는 것

- R1+R2 패키지 범위.
- Legacy live spin 유지.
- V2 domain의 StageRun 비연결.
- `RefCounted` transient runtime state.
- caller-injected token ID.
- global ID generator 미도입.
- snapshot copy-out 불변성.
- stopped-only session.

Codex는 위 결정이 실제 저장소와 Godot 4.7.1에서 안전하게 성립하는지 검증한다. 성립하지 않으면 임의 대안을 구현하지 않고 blocker와 최소 대안을 제안서에 기록한다.

## 8. Codex가 기술적으로 검증할 것

- 실제 파일·preload·class_name·typed Array 패턴.
- resolver DTO와 Legacy result adapter 필드 매핑.
- GDScript deep-copy 경계.
- built-in hash 안정성 또는 고정 salt 필요성.
- invalid state 처리 방식.
- C1 validator와 mutation fixture의 최소 변경.
- CI 비용 계약을 유지하는 validator 연결.
- rollback 시 Legacy C1 실행 경로 복구 방법.

기준선은 Codex 실행 시점의 최신 `origin/main`이다. 계획의 오래된 SHA는 조사 이력으로만 사용한다.

## 9. 다음 순서

```text
검수 문서 PR의 문서 CI 성공·main 병합
→ 사용자 정확한 `검수 완료`
→ 최종 Codex Plan Mode 인계
→ Codex 읽기 전용 저장소 조사
→ 제안서 제출
→ GPT 적대적 검수
→ 사용자 제안서 승인
→ 격리 worktree에서 R1+R2 Red→Green 구현
→ Core contracts + Godot CI
→ squash merge
→ 별도 문서 PR로 R1/R2 증거 동기화
→ R3 TokenSource 연동을 새 Plan Mode로 검토
```

## 10. 금지된 완료 표현

다음 조건 전에는 `CORE_LOCK_V2`, `V2_IMPLEMENTED`, `CORE_LOOP_PROVEN`, `MVP_COMPLETE`를 사용하지 않는다.

- 해당 V2 제품 실행 경로 구현.
- V2 자동 계약 통과.
- 10~15분 사람 플레이.
- 1080p·720p 가독성 검증.

R1+R2가 구현·원격 검증되더라도 live V2 룰렛은 연결되지 않으므로 `V2_IMPLEMENTATION_PARTIAL_FOUNDATION_ONLY`보다 강한 완료 표현을 사용하지 않는다.
