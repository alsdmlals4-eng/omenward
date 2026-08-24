# [현행 검토] OMENWARD Final Planning Adversarial Review & Drift Check

```yaml
review_id: OMW-REV-20260824-FINAL-PLANNING-ADVERSARIAL-DRIFT-01
reviewed_at: 2026-08-24
status: PASS_5_OF_5
planning_contract: PROJECT_TOTAL_PLANNING_IMPLEMENTATION_AND_DELIVERY_INSTRUCTION_v4.8
scope: CURRENT_REPLAN_PLUS_NORTH_STAR_V2_1_AUDIT
new_product_decision_required: false
implementation_authority: NONE
runtime_mutation: NONE
scene_mutation: NONE
product_data_mutation: NONE
current_godot_runtime: NOT_RUN
current_windows_runtime: NOT_RUN
current_ui_runtime: NOT_RUN
human_usability: NOT_RUN
player_experience: NOT_RUN
corrected_north_star_image: USER_EXPLICIT_IMAGE_REQUEST_ONLY
```

## 1. 검토 목적과 입력

이 검토는 새 기능을 추가하는 단계가 아니라, current v4.8 기획 정본이 **서로 충돌하지 않고 구현 handoff 직전까지 닫혔는지**를 확인하는 마지막 planning gate다.

검토 입력:

- `docs/CURRENT_CONFIRMED_DECISIONS.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/PROJECT_CORE.md`
- `docs/OMENWARD_GDD_CURRENT_CANON.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/DECISIONS_PENDING.md`
- `docs/design/APPROVED_OMENWARD_NORTH_STAR_V2_1_AUDIT_AND_CORRECTION_BRIEF_2026-08-24.md`
- Project Notion Home `오멘워드 · Home`
- Project Notion visual surface `13 · 비주얼 컴포넌트 · 전장/룰렛/UI`
- PR #204 current diff / exact-head CI evidence

검토 원칙:

```text
MINIMUM_FULL_LOOPS = 5
NEW_FINDING_RESTARTS_FROM_LOOP_1 = TRUE
NOT_RUN_CANNOT_BECOME_PASS = TRUE
IMAGE_REFERENCE_CANNOT_PROVE_RUNTIME = TRUE
COMPETITOR_BEHAVIOR_AUTOMATIC_AUTHORITY = FORBIDDEN
```

## 2. Targeted benchmark fresh-check · 2026-08-24

같은 work item의 기존 benchmark-first 결정을 재사용하되, final review에서 현재 설계 질문에 직접 영향을 주는 비교축만 다시 확인했다.

| 비교작 | 1차 출처 | 확인한 구조 | 처분 | OMENWARD 적용 |
|---|---|---|---|---|
| Into the Breach | https://store.steampowered.com/app/590380/ | 적 행동을 미리 telegraph하고 플레이어가 counter를 설계하는 정보-선택 구조 | `ADAPT` | Forecast는 단순 경고가 아니라 다음 선택을 바꾸는 읽을 수 있는 압력 정보여야 한다. 실시간/auto-battle 구조 차이 때문에 UI를 그대로 복사하지 않는다. |
| Mechabellum | https://store.steampowered.com/app/669330/ | 병력 draft/customize/formation 뒤 자동 전투로 결과를 확인하는 strategy-first auto-battler 구조 | `ADAPT` | 전투 중 클릭량보다 PREPARE/COMMIT에서의 구조적 선택과 전장 가독성을 우선한다. OMENWARD는 세 전선 Forecast·확률 설계·비가역 commit으로 차별화한다. |
| Backpack Battles | https://store.steampowered.com/app/2427700/ | 전투 전에 구매·제작·배치하고 이후 auto-battle로 빌드 인과를 확인하는 구조 | `ADAPT` | 하단 작업면은 현재 질문 하나에 집중하고, 전투 결과가 이전 설계 선택의 인과를 읽게 해야 한다. 인벤토리 배치 자체는 복제하지 않는다. |

결론:

```text
BENCHMARK_RESULT = NO_PRODUCT_DIRECTION_CHANGE
FORECAST_READABILITY = REINFORCED
PRE_COMBAT_AGENCY = REINFORCED
AUTO_BATTLE_CAUSAL_REVIEW = REINFORCED
PERSISTENT_DASHBOARD_DENSITY = NOT_JUSTIFIED_BY_BENCHMARK
```

## 3. 최소 3안 비교

### A · Corrected North Star 이미지를 final planning 필수조건으로 둔다

- 장점: 구현자에게 한 장짜리 시각 reference가 더 직접적이다.
- 문제: 사용자가 새 이미지 제작을 명시하지 않은 상태에서 이미지 생성이 planning blocker가 된다.
- 판정: `REJECT`.

### B · Final review PASS와 동시에 구현을 자동 시작한다

- 장점: handoff 지연이 없다.
- 문제: 현재 정본의 `IMPLEMENTATION_AUTHORITY_REQUIRED`와 충돌하고 runtime evidence gate를 건너뛴다.
- 판정: `REJECT`.

### C · Planning을 닫고 implementation authority만 별도 gate로 남긴다

- 장점: 기획 완료와 실행 권한을 분리하고, 이미지·runtime·human evidence를 거짓 승격하지 않는다.
- 문제: 다음 단계 시작에는 명시적 사용자 권한이 필요하다.
- 판정: `ADOPT`.

```text
SELECTED_ROUTE = C
```

## 4. Adversarial Loop 1/5 · Authority / precedence / stale-state

공격 질문:

1. current v4.8보다 오래된 v4.4/v4.5/Phase B 상태가 현재 실행 authority로 되살아났는가?
2. 19개 current replan Decision의 owner와 North Star v2.1 audit이 충돌하는가?
3. 이미지 한 장이 기존 3×3 Roulette / Lower Deck owner를 덮어썼는가?

검토 결과:

- `North Star v2.1 = APPROVED_REFERENCE_WITH_BOUNDARY`이며 기존 상세 owner를 대체하지 않는다.
- Lower Deck는 `FOCUS_ADAPTIVE_COMPACT`, Roulette는 `3×3 + 12 direct arrows`가 계속 우선한다.
- exact 문구·수치·micro-layout은 `NON_CANON_REFERENCE`로 남는다.
- 과거 Phase B/C0/C1/C2/C3 증거는 historical evidence이며 current runtime PASS가 아니다.

```text
LOOP_1 = PASS
NEW_BLOCKING_FINDING = NONE
```

## 5. Adversarial Loop 2/5 · Player emotion / choice / differentiation

공격 질문:

1. 기능을 늘리면서 핵심 감정인 "예측 → 설계 → 결과 → 책임"이 약해졌는가?
2. Roulette가 카지노/무료 랜덤 보상처럼 보이는가?
3. 세 전선 commit이 형식적 선택으로 퇴행했는가?

검토 결과:

- Forecast가 미래 압력을 읽게 하고, 건물/TokenSource/징조륜이 미래 병력 분포를 바꾸며, 획득 병력을 비가역 전선에 commit한다는 인과가 유지된다.
- Roulette의 보상감은 `내가 만든 동원 확률이 원하는 병력으로 터졌다`에 묶여 있고 gambling fantasy는 금지되어 있다.
- 세 전선 선택은 회수·cross-lane 이동 불가와 연결되어 실제 opportunity cost를 가진다.

```text
LOOP_2 = PASS
CORE_EMOTION_PRESERVED = TRUE
DIFFERENTIATION_PRESERVED = TRUE
NEW_BLOCKING_FINDING = NONE
```

## 6. Adversarial Loop 3/5 · UI hierarchy / interaction clarity

공격 질문:

1. Battlefield가 다시 dashboard에 밀려 보조 화면이 되는가?
2. Lower Deck에서 여러 큰 작업면이 동시에 열려 인지부하가 커지는가?
3. 3×3 Roulette 조작 대상과 방향이 설명 없이는 읽히지 않는가?

검토 결과:

- `BATTLEFIELD_PRIMARY = TRUE`, full three lanes visible, Lower Deck secondary가 보호된다.
- Lower Deck Correction Brief는 `ONE_ACTIVE_WORK_SURFACE_AT_A_TIME = TRUE`와 mode별 Primary CTA를 명시한다.
- Roulette Focus는 3×3 보드 + 각 열 상·하 / 각 행 좌·우 direct arrow를 중심에 둔다.
- 현재 North Star 이미지의 부족한 Lower Deck/Roulette 부분은 **교정 사양으로 해결되었지만 새 이미지가 생성된 것은 아니다**.

남은 검증은 실제 해상도·keyboard/controller focus·human usability에서 수행한다.

```text
LOOP_3 = PASS_PLANNING
FINAL_UI_GEOMETRY = NOT_APPROVED
RUNTIME_UI_VALIDATION = NOT_RUN
HUMAN_USABILITY = NOT_RUN
NEW_BLOCKING_FINDING = NONE
```

## 7. Adversarial Loop 4/5 · Implementation Reality Gate / evidence ceiling

공격 질문:

1. 문서/Scene/resource 존재를 runtime 동작으로 오인했는가?
2. 과거 C1/C2/C3 proof나 10k simulation을 current v4.8 제품 경험 PASS로 승격했는가?
3. 이미지 upload/readback을 human usability evidence로 오인했는가?

검토 결과:

```text
CURRENT_GODOT_RUNTIME = NOT_RUN
CURRENT_WINDOWS_RUNTIME = NOT_RUN
CURRENT_UI_EVIDENCE = NOT_RUN
CURRENT_HUMAN_USABILITY_EVIDENCE = NOT_RUN
CURRENT_PLAYER_EXPERIENCE_EVIDENCE = NOT_RUN
FINAL_PARAMETER_VECTOR = NOT_SELECTED
FINAL_PRODUCT_NUMERICS = NOT_APPROVED
IMPLEMENTATION_AUTHORITY = NONE
```

과거 증거는 역사적 범위에서만 보존한다. 이번 planning review는 runtime PASS를 주장하지 않는다.

```text
LOOP_4 = PASS
FALSE_COMPLETION_CLAIM = NONE
NEW_BLOCKING_FINDING = NONE
```

## 8. Adversarial Loop 5/5 · GitHub / Notion drift / maintainability

GitHub current meaning과 Notion human-facing meaning을 항목별로 대조했다.

| 의미 | GitHub | Notion | 판정 |
|---|---|---|---|
| North Star 전체 지위 | `APPROVED_REFERENCE_WITH_BOUNDARY` | 부분 승인 Reference | MATCH |
| Battlefield / mood | `APPROVED_DIRECTION` | 승인 방향 | MATCH |
| Lower Deck | `NEEDS_CORRECTION` + Correction Brief complete | 교정 필요 + Focus-adaptive 설명 | MATCH |
| Roulette interaction | `NEEDS_CORRECTION` + 3×3 direct-arrow contract | 교정 필요 + 3×3/화살표 설명 | MATCH |
| 세부 문구·수치·pixel layout | `NON_CANON_REFERENCE` | final canon 아님 | MATCH |
| corrected image | `USER_EXPLICIT_IMAGE_REQUEST_ONLY` | 명시 요청 때만 제작 | MATCH |
| runtime/human evidence | `NOT_RUN` | `NOT_RUN` | MATCH |
| implementation | authority 없음 | 별도 authority 필요 | MATCH |

운영 관점에서는 `AGENTS.md`에 PR 번호·HEAD·Decision 개수 같은 live state를 다시 넣지 않고 current state owner를 따라가도록 유지한다.

Pre-finalization exact-head evidence:

```text
HEAD = f4a2009c1b1e4a2b5d098c0d6b13d3e00ddbf935
PR = #204
PR_MERGEABLE = TRUE
CHANGED_FILES_AT_REVIEW = 25
PRODUCT_RUNTIME_PATH_CHANGES = 0
PULL_REQUEST_WORKFLOWS = 15 / 15 SUCCESS
```

이 exact-head evidence는 **final state 변경 전 안전 스냅샷**이다. 최종 merge는 이후 생성되는 최신 head가 다시 GREEN일 때만 허용한다.

```text
LOOP_5 = PASS
GITHUB_NOTION_DRIFT = NONE_BLOCKING
LONG_TERM_ROUTING = PASS
NEW_BLOCKING_FINDING = NONE
```

## 9. 5회 전체 검토 결론

각 loop에서 새 blocking finding이 발생하지 않았으므로 Loop 1로의 rollback은 필요하지 않았다.

```text
ADVERSARIAL_REVIEW = PASS_5_OF_5
GITHUB_NOTION_DRIFT_CHECK = PASS
NEW_PRODUCT_DECISION_REQUIRED = FALSE
PLANNING_BLOCKER = NONE
IMPLEMENTATION_HANDOFF_READINESS = READY_AWAITING_EXPLICIT_USER_AUTHORITY
CURRENT_NEXT = IMPLEMENTATION_AUTHORITY_REQUIRED
IMPLEMENTATION_AUTHORITY = NONE
CORRECTED_NORTH_STAR_IMAGE = USER_EXPLICIT_IMAGE_REQUEST_ONLY
```

## 10. 남은 항목 · planning blocker가 아님

다음은 기획 미완료가 아니라 구현/측정 단계의 evidence gate다.

- economy baseline drift를 fresh current runtime과 재대조.
- 960×540 / 1280×720 / 1920×1080 정보 위계 검증.
- keyboard/controller/touch focus route 검증.
- 실제 Godot runtime 및 Windows runtime 검증.
- Human usability / player experience 검증.
- simulation/runtime/human evidence 이후 final product numerics 확정.

이 항목들은 명시적 implementation authority가 열리기 전에는 실행·PASS 처리하지 않는다.
