# [현행] 오멘워드 프로젝트 코어

```yaml
updated_at: 2026-08-05
profile: PLANNING_ONLY_PROFILE
current_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
current_count: 5_OF_10
status: VERTICAL_SLICE_NOT_IMPLEMENTED
제품 코드: `NOT_AUTHORIZED`
human_validation: HUMAN_QA_NOT_RUN
```

## 1. 프로젝트 정체성

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 수동 전술 타이밍
→ 설명 가능한 결과와 다음 설계
```

전술스킬은 실패를 지우는 만능 버튼이 아니라, 건물·병종·배치로 준비한 대응을 순간적으로 증폭하는 수단이다.

## 2. 현행 시스템 집합

```text
골드 / 마력 / 배치 병력·병력 한도 / 이동권
금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
```

- MapRun은 20 Stage다.
- 기본 Stage는 3 Wave Beat를 사용한다.
- 압력은 `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`다.
- 세 원형 릴은 하나의 3×3 노출창을 형성한다.
- 병력은 보관·판매 후 한 전선에 비가역 배치한다.
- 배치 뒤 자유 회수·판매·Cross-lane 이동은 금지한다.

## 3. 마력·마력탑·전술 연구

```text
MANA_TOWER_MAX_ACTIVE_INSTANCES = 1
마력탑 T1 → T2 → T3
BRANCHING = FORBIDDEN
ONE_CONCURRENT_RESEARCH
```

- 마력탑 Tier가 높아질수록 초당 마력 수급량과 연구 가능한 전술 Tier가 높아진다.
- 연구 비용은 골드+시간이다.
- 연구 완료 전술은 현재 MapRun 동안 해금된다.
- 시전 확정 시 마력을 소비하며 자동 시전은 금지한다.
- Stage 전 전술 편성은 없다.
- 새 MapRun에서 마력탑 Tier·연구·해금·보유 마력을 초기화한다.

```text
T1 = 속박진 / 수호장 / 집중 명령 / 충격파
T2 = 폭풍 억제 / 파쇄 명령 / 봉쇄 결계
T3 = 결전의 깃발 / 성역 / 시간 왜곡
```

## 4. 권위 문서

- `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`: 시스템 연결 계보.
- `APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`: 핵심 재미.
- `APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`: Stage 압력.
- `APPROVED_OMENWARD_SIX_BUILDING_T2_T3_BRANCHES_AND_COUNTERS_2026-08-05.md`: 건물 계보. 마력탑 부분은 5/10이 우선.
- `APPROVED_OMENWARD_TROOP_ROLES_SYNERGIES_AND_COUNTERS_2026-08-05.md`: 병종 역할.
- `APPROVED_OMENWARD_TACTICAL_SKILLS_AND_MANA_2026-08-05.md`: 현행 전술·마력 책임 원본.

## 5. 불변 가드레일

```text
AUTO_CAST = FORBIDDEN
STAGE_LOADOUT = NONE
FREE_RECALL = FORBIDDEN
FREE_CROSS_LANE_MOVE = FORBIDDEN
HIDDEN_ROUTE_REACTION = FORBIDDEN
T3_ROULETTE_TOKEN = FORBIDDEN
SINGLE_HARD_COUNTER = FORBIDDEN
EXACT_NUMERICS = PENDING_SIMULATION
```

## 6. 제품 경계

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA_NOT_RUN
```

문서 정본 병합은 제품 구현·수치 확정·실제 아트 제작을 승인하지 않는다.

## 7. Legacy 증거와 완료 이력

```text
LEGACY_C1_C2_C3_PROVEN
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
```

## 8. 다음 Gate

```text
OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
6_OF_10
```
