# Active Context

- 갱신일: 2026-07-26
- 공식명: **오멘워드 / OMENWARD**
- 현재 단계: `PLANNING_COMPLETE / REVIEW_IN_PROGRESS`
- 현재 제품 작업: Issue `#69` — V2 R1+R2 중앙 판정 보존 seam·물리 릴 순수 도메인
- 현재 계획: `docs/superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md`
- 현재 검수: `docs/reviews/2026-07-26-v2-r1-r2-planning-review.md`
- 벤치마크 갱신: `docs/benchmarks/OMENWARD_V2_BENCHMARK_REFRESH_2026-07-26.md`
- 패키지 범위: `R1_PLUS_R2_SCOPE_APPROVED_AND_UNCHANGED`
- Codex Plan Mode 입력: `READY_AFTER_REVIEW_MERGE`
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
10. `docs/reviews/2026-07-26-v2-r1-r2-planning-review.md`
11. `docs/benchmarks/OMENWARD_V2_BENCHMARK_REFRESH_2026-07-26.md`
12. `docs/superpowers/plans/2026-07-26-omenward-v2-r1-r2-roulette-foundation.md`
13. 실제 코드·데이터·Scene·테스트

`docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`는 Issue #56과 구형 main 기준 역사적 초안이다. 현재 제품 구현 입력으로 사용하지 않는다.

기존 `docs/benchmarks/0001-core-game-benchmark-proposal.md` 계열은 Pre-V2 조사 이력이다. 현재 적용 판정은 V2 벤치마크 갱신 문서를 따른다.

## 2. 핵심 문장

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

오멘워드는 좋은 슬롯 결과를 기다리는 게임이 아니다. 예고된 세 전선의 공세를 읽고, TokenSource 건물과 영구 가로 이동으로 세 원형 릴의 미래 배열을 설계한 뒤, 당첨 병력을 한 라인에 커밋해 자동전투를 뒤집는 게임이다.

## 3. 현재 정본과 운영 병합

- PR #57: GM-01~GM-106 통합 결정 원장과 V2 정본.
- PR #65: Skill System v4와 사람 플레이 Skill 계약.
- PR #66: Base 아카이브 거버넌스 adapter-only 채택.
- PR #67: Base 공용 Skill route와 Godot 에셋 우선 탐색.
- PR #68: V2 current 상태·인계·validator 동기화.
- PR #70: R1+R2 Plan Mode 입력과 구현 계획 초안.

위 병합은 Godot 제품 구현이나 `CORE_LOCK_V2`를 의미하지 않는다.

## 4. 검수 결과

기획 범위는 유지한다. 문서 권한과 UX 범위만 교정했다.

```text
R1_PLUS_R2_SCOPE: SOUND
LEGACY_C1_PRESERVATION: SOUND
PURE_DOMAIN_ISOLATION: SOUND
BENCHMARK_DIRECTION: SOUND
PRODUCT_CODE_AUTHORIZED: NO
```

검수에서 확정한 해석:

- transient V2 runtime state는 `RefCounted`.
- token instance ID는 caller가 주입.
- R1+R2에서 global ID generator를 만들지 않는다.
- Codex는 위 결정을 다시 자유 선택하지 않고 실제 Godot 4.7.1 구조에서 성립하는지 검증한다.
- 기준선은 Codex 실행 시점의 최신 `origin/main`이다. 오래된 고정 SHA는 조사 이력으로만 해석한다.
- 벤치마크 개선안은 R1+R2 구현 범위를 확장하지 않는다.

## 5. 확정된 R1+R2 경계

### 포함

- 순수 `RouletteBoardResolver`.
- 중앙 가로줄 선행 판정, 8개 완성선, 등급, 금화, 출처 결정론 보존.
- Legacy `RouletteService`의 resolver 위임 adapter.
- caller-injected ID의 `RouletteTokenInstance`.
- `RefCounted` 기반 길이 3 이상 원형 `RouletteReelState` 세 개.
- `NORMAL_X` 최저 안정 index 교체, 없으면 append.
- `SOURCE_BOUND_X` 일반 교체 제외 타입 경계.
- 전역 token ID 유일성.
- 동일 상태·시드의 동일 정지 index.
- copy-out 방식의 깊은 불변 `RouletteSpinSnapshot`.
- row-major 3×3 board projection.
- 이동·확정이 없는 최소 stopped `RouletteSpinSession`.

### 제외

- Legacy `RouletteService.spin()`의 물리 릴 전환.
- `StageRun`·MapRun·건물·경제·UI·보관·판매·배치 연결.
- TokenSource 완공·파괴·blocked 거래.
- 세로·가로 이동.
- 럭키·이동 아이템·전설 위험 주기.
- `[확정]` idempotency와 PendingReward V2 전환.
- 설계 청사진 UI, 전선 대응 브리핑, 전투 인과 보고.
- 런 청사진 저장, Scene, 아트, 사람 플레이, 100,000시드.

## 6. 벤치마크 반영

### 후속 V2 UX 요구사항

- 설계 청사진.
- 전선 대응 브리핑.
- 전투 인과 사슬.

### UX 표현으로만 채택

- 설계 점검 구간: 강제 pause나 새 planning phase가 아닌 기존 전환 시점 정보 surface.
- 런 청사진 기록: 맵 종료 로컬 요약만. 프리셋·공유·리플레이·영구 통계는 후속.

### 명시적 제외

- 지형·경로 편집.
- 직접 영웅 조작.
- 일반 슬롯 덱빌더식 회전 후 심벌 선택.
- 무제한 리롤·무료 재배치.
- 온라인 PvP·시즌 랭크.
- 초기부터의 대규모 조합 폭발.

## 7. 보존과 교체

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

## 8. 다음 작업

```text
검수 문서 PR의 문서 CI 성공·main 병합
→ 사용자 정확한 `검수 완료` 선언
→ 최종 Codex Plan Mode 인계 프롬프트 발행
→ Codex 읽기 전용 저장소 조사와 제안서 제출
→ 사용자 제안서 검토·명시적 Build 승인
→ 승인된 범위만 격리 worktree에서 Red→Green 구현
```

현재 단계에서는 제품 코드·Scene·Resource·게임 데이터·workflow를 변경하지 않는다.
