# [현행] OMENWARD 문서 수명주기 레지스트리

```yaml
updated_at: 2026-08-04
policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
status: CURRENT_LIFECYCLE_AUTHORITY
current_decision: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
current_count: 2_OF_10
```

이 레지스트리는 파일명·과거 YAML보다 우선한다. 아래에 `[대체됨]`, `[보류]`, `[폐기]`로 분류된 문서는 신규 기획·Codex 구현·아트 제작 입력으로 사용하지 않는다.

## 1. [현행]

| 주제 | 파일 |
|---|---|
| 프로젝트 코어 | `docs/PROJECT_CORE.md` |
| 현행 GDD 요약 | `docs/OMENWARD_GDD_CURRENT_CANON.md` |
| 현재 상태 | `docs/ACTIVE_CONTEXT.md` |
| 구현 경계 | `docs/CURRENT_IMPLEMENTATION_STATUS.md` |
| 문서 지도 | `docs/DOCUMENTATION_MAP.md` |
| 핵심 재미·콘텐츠 가드레일 | `docs/design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md` |
| Stage·Wave·Danger·Boss 압력 | `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md` |
| MapRun·Stage·Wave·접전지 | `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md` |
| MapRun·Stage·Wave·정비시간 | `docs/design/APPROVED_OMENWARD_MAPRUN_STAGE_WAVE_MAINTENANCE_2026-08-02.md` |
| 전투 공간·Route | `docs/design/APPROVED_OMENWARD_COMBAT_SPACE_ROUTE_AND_TARGETING_EXPERIENCE_2026-08-04.md` |
| 전장 시각 계층 | `docs/design/APPROVED_OMENWARD_BATTLEFIELD_VISUAL_HIERARCHY_AND_CAMERA_2026-08-04.md` |
| HUD·룰렛·자원·건물 | `docs/design/APPROVED_OMENWARD_COMBAT_HUD_ROULETTE_RESOURCE_MERCHANT_AND_BUILDING_ROSTER_2026-08-04.md` |
| HUD 레이아웃·자산 재사용 | `docs/design/APPROVED_OMENWARD_HUD_ROULETTE_LAYOUT_AND_BATTLEFIELD_VIEW_AMENDMENT_2026-08-04.md` |
| 최종 아트 방향 | `docs/design/APPROVED_OMENWARD_PIXEL_ILLUSTRATION_HYBRID_ART_DIRECTION_2026-08-04.md` |
| 세계관·명칭 | `docs/design/APPROVED_OMENWARD_WORLD_AND_NAMING.md` |
| 벨루 정체성 | `docs/design/APPROVED_BELLU_MASCOT_AND_GUIDE_CONTRACT.md` |
| 핵심 재미 적대적 검토 | `docs/reviews/ADVERSARIAL_CORE_FUN_CANON_AND_LEGACY_CONFLICT_REVIEW_2026-08-04.md` |
| Stage 공정성·리플레이 검토 | `docs/reviews/ADVERSARIAL_STAGE_PRESSURE_REPLAYABILITY_AND_FAIRNESS_REVIEW_2026-08-04.md` |

전투 결정 1~6의 문서는 플레이어에게 보이는 의미·공정성·가드레일은 현행이며, 좌표·Tick·정렬 키·Resolver 구조 같은 내부 구현 방식은 Codex 참고안이다.

### 1.1 부분 승계 시스템 기준선

`docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 다음에 한해 현행 계보다.

- 전체 시스템을 가짜 UI가 아니라 연결된 Vertical Slice로 만든다는 목표.
- 세 전선·룰렛·건설·점령·저장·UI·아트의 연결 범위.
- `SpinSnapshot`, `SpinSession`, `TokenSource` 같은 거래·상태 경계.
- 20 Stage MapRun 목표.

다음 구형 세부는 후속 현행 정본이 대체한다.

- 식량을 현행 핵심 자원으로 사용하는 규칙.
- 기본 건물 5종.
- 지휘소 주변 범위 오라.
- 구형 Stage·Wave 시계와 전술계획 정지.
- Hero·Meta의 현재 구현 권위.

## 2. [대체됨]

| 파일 | 승계 문서·이유 |
|---|---|
| `docs/OMENWARD_GAME_DESIGN.md` | `docs/OMENWARD_GDD_CURRENT_CANON.md`; 식량·건물 5종·주변 지휘소 등 구형 계약 포함 |
| `docs/design/APPROVED_DOPAMINE_DRIVEN_DESIGN_AND_FIRST_10_MINUTES.md` | 핵심 원칙은 핵심 재미 가드레일로 승계; 구형 수치·자원·건물 흐름 분리 |
| `docs/design/APPROVED_15_WAVE_STAGE_CLOCK_AND_OVERTIME_V2.md` | 15~20 Wave 단일 Stage를 새 20 Stage·3 Wave Beat 압력 매트릭스로 대체 |
| `docs/process/POST_MERGE_PIXEL_ILLUSTRATION_HYBRID_CANON_SYNC_2026-08-04.md` | 병합 증거만 보존; 현재 상태는 동적으로 해석 |
| `docs/operations/PR121_POST_MERGE_SYNC_2026-08-02.md` | 과거 PR 증거만 보존 |
| `docs/design/proposals/0011-korean-natural-fantasy-names-law-and-mascot.md` | 세계관·명칭 및 벨루 승인 문서에 반영 완료 |
| `docs/archive/2026-07/pre-v2-canon/DOCUMENTATION_MAP_PRE_V2.md` | archive 역사 자료; 현행 지도는 `docs/DOCUMENTATION_MAP.md` |

## 3. [보류]

### 첫 10~15분·튜토리얼

- `docs/design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md`
- `docs/design/APPROVED_TUTORIAL_FIRST_FOUR_WAVES_BALANCE_V1.md`

이유: 식량, 바리케이드, 병영 자동생산, 일시정지 계획 모드, 구형 HUD 공개 순서를 포함한다. Stage 1~5의 최신 압력 학습과 자원·건물 6종에 맞춰 7/10 Decision에서 재설계하기 전 사용 금지.

### 메타·허브

- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`

이유: 핵심 Run 선택을 우회하지 않는다는 원칙은 유지 가능하지만 재화·시설·Retry 구조가 최신 Stage 압력과 런 경제에 아직 재검증되지 않았다.

### Hero·Legendary family

다음 파일군은 과거 승인 근거지만 최신 Stage 압력·전투 공간·Targeting·Modifier·HUD와 재조정 전까지 구현 권위가 없다.

- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_INITIAL_ROSTER_ARCHETYPE_SELECTION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_KIT_STRUCTURE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_POWER_BUDGET_AND_SIDEGRADE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SINGLE_ACTIVE_AND_REPEAT_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_GRADE_SLOT_AND_UNLOCKED_SKILL_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_EXIT_AND_REPLACEMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_SIGNATURE_DELTA_BALANCE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_UPGRADE_MODEL_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_ABILITY_ACTIVATION_MODE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_REPEAT_LEGENDARY_RESULT_HIGH_GRADE_SLOT_RESOLUTION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_FIRST_FIVE_UNIQUE_SKILL_2_CONCEPTS_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_COOLDOWN_CHARGE_AND_FAILURE_POLICY_2026-08-03.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNIQUE_SKILL_2_TRIGGER_TARGET_AND_POWER_BUDGET_VALIDATION_2026-08-03.md`

특히 `SAME_LANE_ONLY`, stable-ID tie-break, exact timer 구조는 최신 공통 Targeting·Codex 구현 경계와 다시 검토해야 한다.

### 구형 구현 계획

- `docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`
- `docs/superpowers/plans/2026-08-02-omenward-grillme-bundle-merge-plan.md`
- 과거 Issue/Goal 문서 중 완료·병합된 작업

과거 계획은 재실행하지 않고 Git 이력·결정 근거로만 사용한다.

## 4. [폐기]

| 파일·가정 | 이유 |
|---|---|
| `docs/design/proposals/0009-world-naming-directions.md` | 은종성채·삼문경계·무명야 명명안 미채택 |
| `docs/design/proposals/0010-english-world-names-and-game-title.md` | 완전 영문 음차형 명명안 미채택 |
| 식량을 현행 핵심 HUD 자원으로 사용 | 골드·마석·배치 병력/한도로 대체 |
| 기본 건물 5종 | 금고·농장·병영·방어탑·지휘소·마력탑 6종으로 대체 |
| 지휘소 주변 범위 오라 | 현재 MapRun 전체 아군 오라로 대체 |
| `15웨이브=1스테이지`와 고정 60초 공세 | 20 Stage·3 Wave Beat 압력 매트릭스로 대체 |
| Danger에서 핵심 UI·정보를 차단 | 공개된 한 가지 규칙 변형으로 대체 |
| 전투 중 주 압력·필수 카운터를 숨은 무작위로 변경 | Stage 시작 전 완전 공개와 작성 변형으로 대체 |
| 룰렛 전용 금화·병종 상징 아이콘 | 인게임 금화·T1/T2 병종 이미지 재사용으로 폐기 |
| T3 병종 룰렛 토큰 | 명시 금지 |

## 5. [증거]

- `docs/reviews/**`의 과거 PR·적대적 검토 기록.
- `docs/benchmarks/**`의 실험·Evidence Pilot.
- `docs/archive/**`.
- 완료된 PR·commit·CI run·Sheet 변경 이력.

`[증거]`는 사실을 증명하지만 현재 기획 규칙을 자동 변경하지 않는다.

## 6. 신규 작업자 규칙

1. `PROJECT_CORE.md`와 `DOCUMENTATION_MAP.md`를 먼저 읽는다.
2. 이 레지스트리에서 대상 파일이 `[현행]`인지 확인한다.
3. `[대체됨]`, `[보류]`, `[폐기]` 파일을 구현 입력으로 사용하지 않는다.
4. Stage 작업은 최신 압력 매트릭스의 Stage 번호·압력·Danger/Boss 규칙을 먼저 대조한다.
5. 필요한 과거 아이디어는 새 Decision에서 재검토·재승인한 뒤 승계한다.
