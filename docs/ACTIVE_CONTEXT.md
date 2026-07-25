# Active Context

- 갱신일: 2026-07-26
- 공식명: **오멘워드 / OMENWARD**
- 현재 제품 작업: Issue `#69` — V2 R1+R2 중앙 판정 보존 seam·물리 릴 순수 도메인 Plan Mode
- 현재 계획: `docs/superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md`
- 패키지 범위: `R1_PLUS_R2_SCOPE_APPROVED`
- Plan Mode 입력: `READY`
- 제품 코드 승인: `NO`
- 설계 상태: `V2_SPEC_APPROVED`
- 정본 상태: `V2_CANON_CURRENT_BY_PR_57_MERGE`
- 구현 상태: `V2_IMPLEMENTATION_NOT_STARTED`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 잠금: `CORE_LOCK_V2_PENDING`
- 별도 운영 작업: Issue `#62` Ruleset·ci-gate·자동 병합

## 1. 지금 읽을 문서

1. `AGENTS.md`
2. `docs/BASE_RULES_VERSION.md`
3. `docs/DOCUMENTATION_MAP.md`
4. `docs/PROJECT_CORE.md`
5. `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`
6. `docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md`
7. `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
8. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
9. Issue `#69`
10. `docs/superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md`
11. 실제 코드·데이터·Scene·테스트

`docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`는 Issue #56과 구형 main 기준 역사적 초안이다. 현재 제품 구현 입력으로 사용하지 않는다.

## 2. 핵심 문장

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

오멘워드는 예고된 세 전선의 공세를 읽고, TokenSource 건물과 영구 가로 이동으로 세 원형 릴을 설계한 뒤, 당첨 병력을 한 라인에 커밋해 자동전투를 뒤집는 게임이다.

## 3. 현재 정본과 운영 병합

- PR #57: GM-01~GM-106 통합 결정 원장과 V2 정본.
- PR #65: Skill System v4와 사람 플레이 Skill 계약.
- PR #66: Base 아카이브 거버넌스 adapter-only 채택.
- PR #67: Base 공용 Skill route와 Godot 에셋 우선 탐색.
- PR #68: V2 current 상태·인계·validator 동기화.

위 병합은 Godot 제품 구현이나 `CORE_LOCK_V2`를 의미하지 않는다.

## 4. 이번 패키지의 문제와 플레이어 가치

현재 `RouletteService`는 독립 9칸 생성, 중앙 판정, 등급, 금화, 출처 선택, 전설 상태, 경제와 보상 생성을 함께 소유한다.

R1+R2의 목적은 화면 기능 추가가 아니라 다음 기반을 만드는 것이다.

```text
검증된 중앙 판정을 잃지 않는다
+ 세 원형 릴의 상태와 결정론을 독립 검증한다
+ 이후 건물·이동·확정 거래를 안전하게 연결할 seam을 만든다
```

## 5. 확정된 R1+R2 경계

### 포함

- 순수 `RouletteBoardResolver`.
- 중앙 가로줄 선행 판정, 8개 완성선, 등급, 금화, 출처 결정론 보존.
- Legacy `RouletteService`의 resolver 위임 adapter.
- `RouletteTokenInstance`.
- 길이 3 이상 원형 `RouletteReelState` 세 개.
- `NORMAL_X` 최저 안정 index 교체, 없으면 append.
- `SOURCE_BOUND_X` 일반 교체 제외 타입 경계.
- 전역 token ID 유일성.
- 동일 상태·시드의 동일 정지 index.
- 깊은 복사 불변 `RouletteSpinSnapshot`.
- row-major 3×3 board projection.
- 이동·확정이 없는 최소 stopped `RouletteSpinSession`.

### 제외

- Legacy `RouletteService.spin()`의 물리 릴 전환.
- `StageRun`·건물·경제·UI·보관·판매·배치 연결.
- TokenSource 완공·파괴·blocked 거래.
- 세로·가로 이동.
- 럭키·이동 아이템·전설 위험 주기.
- `[확정]` idempotency와 PendingReward V2 전환.
- MapRun, Scene, 아트, 사람 플레이, 100,000시드.

## 6. 보존과 교체

보존:

- 고정 3라인.
- 중앙 판정·완성선·등급·금화 resolver.
- 결정론과 출처 원장.
- 공용 병종 데이터.
- 전장 상태 기반 승패와 원인 보고.

교체 대상이지만 이번 패키지에서 아직 연결하지 않음:

- 독립 9칸 생성.
- 공개 12% 럭키·+8%p.
- 이동 되돌리기·확정 시 소비.
- 스테이지당 전설 1회.
- 60초 공세와 점령력 합산.
- 단일 StageRun 영속 상태.

## 7. 다음 작업

```text
Issue #69 기준 Codex 읽기 전용 Plan Mode 조사
→ 실제 파일·타입·테스트·validator 영향 제안서 제출
→ 사용자 제안서 검토·수정·명시적 승인
→ 승인된 범위만 격리 worktree에서 Red→Green 구현
→ 정확한 PR head의 Core·Godot CI 검증
→ squash merge
→ 별도 문서 PR로 R1/R2 실행 증거 동기화
```

`권장안으로 진행`은 R1+R2 계획 범위 승인이다. Codex 제안서가 아직 제출·승인되지 않았으므로 제품 코드 작업은 금지한다.