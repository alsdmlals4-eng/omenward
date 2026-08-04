# OMENWARD 프로젝트 AI 작업 규칙

이 저장소는 GPT/Work가 핵심 재미·콘텐츠·플레이어 규칙·UX·아트 정본을 관리하고, Codex가 별도 승인된 범위에서 Godot 구현·테스트를 수행하는 공동 작업 저장소다.

```yaml
current_planning_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_planning_count: 4_OF_10
current_process_policy: OMW-PROC-20260805-BENCHMARK-TDD-APPROVAL-BATCH-V1
product_code_authority: NONE
```

## 1. 규칙 우선순위

```text
사용자의 최신 지시
→ docs/PROJECT_CORE.md
→ docs/DOCUMENTATION_MAP.md
→ docs/DOCUMENT_LIFECYCLE_REGISTRY.md
→ 주제별 [현행] 책임 원본
→ 실제 코드·데이터·Scene·실행 증거
→ [증거]
→ [대체됨]·[보류]·[폐기]
```

파일명에 `APPROVED`가 있어도 lifecycle registry가 `[보류]` 또는 `[대체됨]`으로 분류하면 구현 권위가 없다.

## 2. 작업 전 읽기 순서

1. `AGENTS.md`
2. `docs/PROJECT_CORE.md`
3. `docs/ACTIVE_CONTEXT.md`
4. `docs/DOCUMENTATION_MAP.md`
5. `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
6. `docs/OMENWARD_GDD_CURRENT_CANON.md`
7. 작업 주제의 `[현행]` 책임 원본
8. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
9. `docs/DECISIONS_PENDING.md`
10. 현재 PR·실제 코드·테스트

필수 주제 문서:

- Stage: `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 건물: `docs/design/APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`
- 병종: `docs/design/APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`
- 운영: `docs/process/APPROVED_BENCHMARK_TDD_AND_APPROVAL_BATCH_POLICY_2026-08-05.md`

## 3. 역할 분리

```text
GPT / Work
= 핵심 재미, 콘텐츠 구조, 병종 역할, 시너지, 카운터, 플레이어 규칙, UX, 아트 방향, 검수 기준

Codex
= 자료구조, 알고리즘, 좌표, 경로탐색, 충돌, AI 타기팅, Spawn·Timer, 성능, 코드, 자동 테스트
```

Codex 구현 선택이 플레이어 경험·콘텐츠 역할·시각 계층을 바꾸면 구현을 중단하고 새 기획 Gate로 돌아온다.

## 4. 벤치마킹·승인 배치·TDD

```text
BENCHMARK_REQUIRED
INDUSTRY_COMPARISON_REQUIRED
MAX_APPROVAL_BATCH: 10
EARLY_CHECKPOINT_ON_HIGH_RISK_CONFLICT
EARLY_CHECKPOINT_ON_SESSION_END
EARLY_CHECKPOINT_ON_LARGE_CANON_IMPACT
TDD_MANDATORY
RED → GREEN → REFACTOR
EXPLICIT_BRANCH_REQUIRED_FOR_GITHUB_MUTATION
DIRECT_MAIN_WRITE: FORBIDDEN
```

관련 외부 사례가 판단을 개선할 때 공식 자료와 현업 관행을 비교하고 `가져올 원칙 / 다른 조건 / 복제하지 않을 부분 / 권장안`을 구분한다.

## 5. 현재 프로젝트 코어

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과와 다음 설계
```

- 한 MapRun은 20 Stage이며 기본 Stage는 3 Wave Beat다.
- 압력은 `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`다.
- 현행 자원은 골드·마석·배치 병력/병력 한도·이동권이다.
- 현행 건물은 금고·농장·병영·방어탑·지휘소·마력탑이다.
- 일반 병력은 배치 뒤 자유 회수·판매·전선 횡단이 불가능하다.
- 치명적 Route·Layer·필수 카운터는 Stage 시작 전에 공개한다.

## 6. 현행 병종 정본

```text
ROSTER_BASELINE: 10
ROSTER_COUNT_IS_NOT_SACRED
ROSTER_MIN_MAX: NOT_PRESET
```

기준선:

```text
방패수호병 / 대검병 / 창병 / 궁수 / 마도사
사제 / 암살자 / 기병 / 비행병 / 거인
```

- 다섯 압력 각각에 최소 두 병종 대응 경로를 둔다.
- 시너지는 관찰 가능한 전장 행동이며 단순 세트 보너스는 금지한다.
- 전열 병영과 기동 병영은 후보 가중을 바꾸되 반대 계열을 영구 삭제하지 않는다.
- T1/T2 병종 토큰은 실제 인게임 이미지를 재사용하고 T3 룰렛 토큰은 금지한다.
- 정확한 수치와 제품 데이터는 `PENDING_SIMULATION`이며 제품 구현 권한이 없다.

## 7. 문서·제품 경계

- `[현행]`만 신규 기획·구현 입력으로 사용한다.
- `[대체됨]`, `[보류]`, `[폐기]`는 구현 입력 금지.
- `[증거]`는 과거 사실만 증명한다.
- `data/units/*.tres`는 최신 병종 정본의 구현 권위가 아닌 Legacy Prototype 증거다.
- 문서 승인·CI·병합은 제품 구현 완료가 아니다.

완료 이력 보존:

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```

다음 Gate는 `OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1 / 5_OF_10`이다.