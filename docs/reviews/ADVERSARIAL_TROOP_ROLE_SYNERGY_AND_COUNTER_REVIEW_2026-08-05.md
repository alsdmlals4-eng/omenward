# [현행] OMENWARD 병종 역할·시너지·카운터 적대적 검토

```yaml
review_id: OMW-REV-20260805-TROOP-ROLE-SYNERGY-COUNTER-V1
decision_id: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
status: PASS / REQUIRED_CANON_FIXES_APPLIED
review_scope: ROSTER / ROLES / PRESSURES / SYNERGY / BARRACKS / TIER / ROUTE / LAYER / LIFECYCLE
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결론

열 종 기준선과 비고정 로스터 수 계약은 오멘워드의 핵심 재미와 맞는다.

```text
예고된 압력
→ 병영·건물로 병종 결과 방향 설계
→ 룰렛 결과와 보관함에서 역할 선택
→ 한 전선에 비가역 커밋
→ 전장 행동 시너지와 카운터 결과 복기
```

```text
CORE_FIT = STRONG
ROLE_READABILITY = COHERENT
COUNTER_COVERAGE = STRUCTURALLY_VIABLE_WITH_TACTICAL_DEPENDENCY
DOCUMENT_PR_MERGE_READINESS = PASS
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_TACTICAL_AND_NUMERIC_DECISIONS
```

강점:

- 현행 자산 계보를 보존하면서 중복 역할을 분리한다.
- 다섯 압력에 최소 두 병종 경로를 제공한다.
- 병영 분기가 결과를 유도하지만 반대 계열을 삭제하지 않는다.
- 시너지가 숨은 세트 보너스가 아니라 관찰 가능한 전장 행동이다.
- 병종 수를 성역화하지 않으면서 증감에 증거와 비용 검토를 요구한다.

잔여 한계:

- 전술스킬이 미확정이어서 FLYING·SIEGE의 최종 대응망은 닫히지 않았다.
- 정확 수치와 AI 타기팅은 시뮬레이션·Codex 계획 전 확정할 수 없다.
- 첫 5 Stage에서 특정 병종이 강제되는지는 사람 플레이 검증이 필요하다.

## 2. P0 핵심 정체성·권위 공격

### OMW-AUD-420 — ROLE_OVERLAP_RISK

- 위험: 전열 3종과 후열 우선 3종이 이름만 다르고 같은 전투 판단을 만들 수 있다.
- 조치: 각 병종에 역할·주 압력·포기 비용을 부여하고 암살자·기병·비행병을 `우회 추적 / 공개 Route 대응 / 공중 우세`로 분리한다.

### OMW-AUD-421 — HARD_COUNTER_LOCK_RISK

- 위험: 특정 병종 미보유 시 Stage 통과가 불가능해 룰렛 결과가 패배를 확정한다.
- 조치: 압력별 최소 두 병종 대응 경로와 건물·전술 경로를 함께 요구하고 단일 하드키 병종을 금지한다.

### OMW-AUD-422 — FORCED_COMPOSITION_RISK

- 위험: 시너지 보너스가 특정 조합을 사실상 정답으로 만든다.
- 조치: 기본 세트 보너스를 금지하고 각 병종이 단독 역할을 수행하도록 한다. 시너지는 행동 연결만 허용한다.

### OMW-AUD-423 — ROSTER_BLOAT_RISK

- 위험: 압력마다 새 병종을 추가해 룰렛·보관함·학습량·아트 비용이 폭증한다.
- 조치: 새 병종은 기존 병종으로 표현할 수 없는 판단을 만들 때만 허용하고 별도 승인 Gate를 거친다.

### OMW-AUD-424 — ROSTER_SHRINK_ROLE_GAP

- 위험: 제작비를 줄이기 위해 병종을 합치면 다섯 압력의 대응 경로와 배치 판단이 사라진다.
- 조치: 제거 전 역할 공백·중복 증거와 건물·전술 대체 경로를 함께 검증한다.

### OMW-AUD-425 — LEGACY_TRES_AUTHORITY_LEAK

- 위험: `data/units/*.tres`의 구형 수치와 태그가 최신 정본으로 오인된다.
- 조치: 해당 데이터는 `[증거] LEGACY_PROTOTYPE_UNIT_DATA`로 격리하고 Decision 4/10·5/10·수치 시뮬레이션·Codex 계획 전 구현 입력을 금지한다.

## 3. P1 압력·시너지 공격

### OMW-AUD-426 — ASSASSIN_CAVALRY_FLIER_DUPLICATION

- 공격: 세 병종 모두 후열 우선이면 룰렛 결과만 다르고 실제 배치 판단은 같다.
- 조치: 암살자는 우회 Route 추적, 기병은 공개 Route 신속 대응, 비행병은 공중 Layer 우세를 소유한다.

### OMW-AUD-427 — FLYING_COUNTER_SINGLE_POINT_FAILURE

- 공격: 궁수 하나만 실제 대공이면 궁수 미보유가 자동 패배가 된다.
- 조치: 궁수와 비행병 두 병종 경로를 두고 요격탑·전술스킬을 추가 경로로 유지한다.

### OMW-AUD-428 — ARMORED_DEBUFF_DOMINANCE

- 공격: 마도사의 장갑 약화가 모든 물리 병종을 강화하면 마도사가 항상 정답이 된다.
- 조치: 마도사는 낮은 생존력·느린 템포를 부담하고 창병·거인도 독립 대응을 가진다. 정확 약화량은 시뮬레이션에서 상한을 검증한다.

### OMW-AUD-429 — SIEGE_STOP_AND_STRUCTURE_DAMAGE_CONFLATION

- 공격: 공성병 저지와 적 구조물 파괴를 한 병종이 모두 최고 효율로 수행하면 다른 병종이 사라진다.
- 조치: 창병·기병/암살자는 저지, 거인은 승리 전선의 역공·구조물 파괴로 역할을 분리한다.

### OMW-AUD-430 — SUPPORT_STALL_META

- 공격: 방패수호병+사제가 무한 유지해 처치력 선택을 무시할 수 있다.
- 조치: 둘 모두 낮은 직접 처치력·기동성을 가지며 Wave 겹침·공성·다전선 압력에서 공격 역할이 필요하다. 정확 회복과 생존 수치는 시뮬레이션 대상이다.

### OMW-AUD-431 — FIXED_PAIR_DEPENDENCY

- 공격: 특정 짝이 없으면 병종이 기능하지 않아 룰렛 변동성이 불공정해진다.
- 조치: 각 병종은 단독 최소 역할을 가지며 시너지는 성능 확장이지 기능 해금이 아니다.

### OMW-AUD-432 — HIDDEN_SET_BONUS_REGRESSION

- 공격: 문서 밖 데이터에서 `2종 보유 시 +N%`가 재도입될 수 있다.
- 조치: `단순 세트 보너스: FORBIDDEN`을 책임 원본과 검증 테스트에 고정한다.

## 4. 병영·룰렛·Tier 공격

### OMW-AUD-433 — BARRACKS_WEIGHT_HIDDENNESS

- 위험: 병영 분기가 실제 후보를 어떻게 바꾸는지 보이지 않으면 제작한 확률이 설명 불가능하다.
- 조치: TokenSource 가중·후보 역할 분포·승급 기회 변화를 UI에서 공개한다. 정확 확률은 시뮬레이션 후 확정한다.

### OMW-AUD-434 — BARRACKS_HARD_LOCK

- 위험: 전열/기동 선택이 반대 계열을 삭제하면 다음 Stage 예고에 대응할 유연성이 사라진다.
- 조치: 반대 계열 영구 삭제를 금지하고 가중·후보 분포 변화만 허용한다.

### OMW-AUD-435 — SUPPORT_EXCLUSIVITY

- 위험: 마도사·사제가 한 병영 분기의 독점물이 되면 해당 분기가 범용 정답이 된다.
- 조치: 공통 지원 계열로 두고 어느 한 분기의 필수 독점물로 만들지 않는다.

### OMW-AUD-436 — T3_TOKEN_REGRESSION

- 위험: T3 역할을 강조하려 별도 룰렛 토큰을 만들면 기존 자산 재사용 정본과 충돌한다.
- 조치: T1/T2 실제 인게임 이미지만 룰렛에 사용하고 T3는 Preview·보관함·배치 카드·전장에서 표현한다.

### OMW-AUD-437 — TIER_ROLE_DRIFT

- 위험: T3가 원래 역할과 무관한 만능 기능을 얻어 계보 판독이 무너진다.
- 조치: T3는 같은 역할 계보 안에서 표적·Route·Layer·유지 방식 중 하나를 변화시킨다.

## 5. 전선·Route·Layer 공격

### OMW-AUD-438 — FREE_CROSS_LANE_MOBILITY

- 위험: 기병의 신속 대응이 배치 후 자유 전선 이동으로 구현되면 비가역 커밋이 무너진다.
- 조치: 배치 전 선택과 공개 Route 내 행동으로 한정하고 자유 Cross-lane 이동을 금지한다.

### OMW-AUD-439 — HIDDEN_ROUTE_REACTION

- 위험: 암살자가 사전 공개되지 않은 우회로에 자동 대응하면 Stage 정보 계약이 깨진다.
- 조치: Stage 시작 전에 공개된 우회 Route와 목표만 추적한다.

### OMW-AUD-440 — LAYER_UI_MISMATCH

- 위험: 궁수·비행병의 대공 가능 여부가 아이콘·시각·판정에서 다르면 실패 원인을 설명할 수 없다.
- 조치: 카드·사거리 표시·공격 연출·실제 Layer 판정을 일치시킨다.

### OMW-AUD-441 — FLIER_OBJECTIVE_BYPASS

- 위험: 비행 이동이 점령·구조물 상호작용까지 자동 허용해 전선 규칙을 우회한다.
- 조치: 공중 이동과 점령·구조물 상호작용 권한을 분리한다.

## 6. 학습·수치·구현 공격

### OMW-AUD-442 — EARLY_STAGE_FORCED_ANSWER

- 위험: Stage 1~5 압력 학습이 특정 병종을 사실상 필수로 만들 수 있다.
- 조치: 기본 병력·건물·룰렛·후속 전술을 포함해 최소 두 경로를 제공하고, 첫 10~15분 설계와 사람 플레이에서 강제 정답 여부를 검증한다.

### OMW-AUD-443 — NUMERIC_PREMATURE_LOCK

- 위험: 역할 정본을 현재 `.tres` 수치와 동일시해 곧바로 제품 데이터에 반영할 수 있다.
- 조치: 모든 체력·공격력·관통·회복·속도·확률·비용은 `PENDING_SIMULATION`. 제품 변경은 5/10 전술 정본, 압력 대응 재검증, Codex 계획, 제품 RED 테스트 뒤에만 시작한다.

## 7. 벤치마킹 적합성

채택:

- 빠르게 읽히는 역할 분류.
- 명확한 강점·약점·카운터 관계.
- 특정 조합에 플레이어를 조기 고정하지 않는 유연성.

비채택:

- 타 게임의 피해 배율·비용·생산 체계 직접 복제.
- 단일 가위바위보로 모든 교전 해결.
- 강한 세트 보너스로 정해진 조합 강제.
- 병종별 독립 자원·메뉴·미니게임.

## 8. 병합·구현 판정

```text
DOCUMENT_PR_MERGE_READINESS = PASS
PRODUCT_CODE = UNCHANGED
IMPLEMENTATION_READINESS = BLOCKED_BY_TACTICAL_AND_NUMERIC_DECISIONS
```

문서 PR은 중앙 라우팅·Sheet 동기화·fresh CI·preflight가 Green이면 병합할 수 있다. 제품 구현은 아직 승인되지 않았다.