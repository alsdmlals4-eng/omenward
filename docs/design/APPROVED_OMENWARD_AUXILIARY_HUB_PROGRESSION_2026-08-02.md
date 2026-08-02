# 오멘워드 메인 허브 보조 콘텐츠·영구 노드 승인 계약

```yaml
decision_id: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
approved_at: 2026-08-02 15:09 KST
latest_clarification_at: 2026-08-02 16:11 KST
approval: USER_DIRECT_APPROVAL_WITH_ADVERSARIAL_GUARDRAILS
status: USER_APPROVED_STRUCTURE / EXACT_VALUES_PENDING / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

메인 화면에는 런 진입과 별개인 `주점·병영·연구` 보조 콘텐츠 허브를 둔다. 정산된 Profile 영구재화를 사용해 유한하고 공개된 노드 그래프를 개방한다.

```text
MAIN_HUB_PRIMARY_ACTION = MAPRUN_ENTRY
AUXILIARY_FACILITIES = TAVERN + BARRACKS + RESEARCH
PURCHASE_CURRENCY = SETTLED_PERMANENT_CURRENCY_BALANCE
NODE_MODEL = FINITE_VISIBLE_PREREQUISITE_GRAPH
RANDOM_PAID_RECRUITMENT = FORBIDDEN
UNBOUNDED_STAT_GRIND = FORBIDDEN
```

## 2. 공통 노드 구조

- 정산이 끝난 영구재화만 소비한다.
- 비용·선행 노드·해금 결과를 구매 전에 공개한다.
- 구매는 명시적 확인 뒤 transaction journal과 idempotent receipt로 기록한다.
- 무한 prestige·반복 구매·끝없는 능력치 누적을 허용하지 않는다.
- 기본 Profile만으로 전체 콘텐츠 완료가 가능해야 한다.
- 비용·노드 수·환불·초기화 규칙은 simulation과 별도 승인 전 제품값이 아니다.

## 3. 주점

주점은 **기존 병종에 고정 대응하는 영웅 후보를 영구 해금하고 Profile 명부를 관리하는 시설**이다.

```text
RECRUITMENT = DETERMINISTIC_VISIBLE_NODE_UNLOCK
HERO_BINDING = FIXED_TO_EXISTING_UNIT_ARCHETYPE
MULTIPLE_HEROES_PER_UNIT_ARCHETYPE = ALLOWED
ROSTER_OWNERSHIP = PERMANENT
PRE_RUN_HERO_REGISTRATION = NOT_REQUIRED
HERO_USE = STORED_HERO_GRADE_TOKEN_CONVERSION
```

### 승인 원칙

- 영웅 후보·비용·전제 조건·연결 병종을 노드에서 사전에 공개한다.
- 랜덤 상자·확률 뽑기·유료 재굴림으로 영웅을 구매하지 않는다.
- 각 영웅은 하나의 기존 병종에 고정 연결되며 다른 병종에 자유 배속하지 않는다.
- 같은 병종에 서로 다른 영웅을 여러 명 해금할 수 있다.
- 해금 시 영웅이 Profile 명부에 영구 등록된다.
- 별도의 런 시작 전 영웅 등록·계약 단계는 없다.
- 룰렛에서 같은 병종의 `[영웅]` 등급 토큰을 획득해 보관함에 넣은 뒤, 원본 유지 또는 해금 영웅 변환을 선택한다.
- 변환은 `1토큰→1유닛`이며 추가 병력을 생성하지 않는다.
- 영웅 미해금 상태에서도 원본 영웅 등급 병종 토큰과 기본 Profile로 전체 Stage를 완료할 수 있어야 한다.
- 동일 영웅 중복 배치·동병종 활성 상한·능력은 후속 Decision이다.

주 책임 원본:

- `APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md`
- `APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`

### 금지

- 현실 화폐 또는 프리미엄 능력 구매.
- 중복 영웅 합성·확률 승급·무한 능력치.
- 다른 병종 영웅의 교차 선택.
- 해금 즉시 전역 패시브·자동 배치·릴 확률 변경.
- 영웅 변환 시 원본 토큰을 유지한 채 보너스 영웅 추가.
- 영웅 미보유를 이유로 핵심 Stage를 사실상 차단.
- 메인 화면을 일반 수집형 RPG 파티 화면으로 구성.

## 4. 병영

허브 병영은 Profile 훈련 시설이고 MapRun 병영은 TokenSource 건물이다.

```text
HUB_BARRACKS = PROFILE_TRAINING_AND_DOCTRINE
MAPRUN_BARRACKS = PHYSICAL_TOKENSOURCE_BUILDING
```

- 새로운 병종·전문화·시작 교리·훈련 선택지를 sidegrade로 해금한다.
- 병종 해금은 역할과 조건을 추가하며 모든 기존 병종의 능력치를 일괄 상승시키지 않는다.
- ReadinessPerk는 한 런 1개·유한 랭크·시작/Act 1 범위를 넘지 않는다.
- 특정 훈련이 모든 공세·릴 구조·난이도에서 우월하면 sidegrade 실패다.
- 무한 훈련·전 구간 영구 전투 배율·기본 병사 불완전 설계를 금지한다.

## 5. 연구

연구는 새로운 시스템 선택지와 정보·편의를 해금한다.

허용 후보:

- 대체 건물·TokenSource·미션의 sidegrade.
- 공세·징조·법칙 도감과 복기 분석.
- 시작 구성안·필터·선택 이력 같은 비전투 편의.
- 제한된 시작 보관 편의의 hard-cap 확장.
- 벨루 추가 분석 기록.

금지:

- 숨은 릴 당첨 확률 조작.
- 금고·농장·건물 생산량의 전 구간 영구 배율.
- 자동 건설·자동 배치·자동 릴 편집.
- 연구만으로 모든 공세 정답을 사전 공개.
- 사실상 필수 순서 하나로 수렴하는 연구 트리.

## 6. 영구재화와 Retry

```text
settled_permanent_currency_balance
= 주점·병영·연구 노드 + paid Retry 소비

settled_permanent_currency_total
= 비감소 누적 진행도·Readiness milestone
```

노드와 Retry의 같은 지갑 경쟁은 허용하되 과도한 비축·구매 후 후회·지배 시설·실패 보상 파밍을 simulation과 사람 검증으로 확인한다.

## 7. 메인 화면 정보 위계

```text
1순위 = 이어하기·새 MapRun·현재 작전
2순위 = 영구재화·Profile 준비 상태
3순위 = 주점·병영·연구
4순위 = 도감·기록·설정
```

- 보조 시설은 런 진입을 가리지 않는다.
- 잠긴 노드는 선행 조건과 결과를 공개한다.
- 영웅 초상은 주점 명부와 보관함 변환 선택에서 사용하되 메인 화면 전체를 파티 화면으로 만들지 않는다.
- 주점에서는 병종별 해금 영웅 수와 역할 차이를 표시한다.

## 8. 저장 책임

```yaml
AuxiliaryHubProgressionState:
  settled_permanent_currency_balance
  settled_permanent_currency_total
  unlocked_node_ids
  unlocked_hero_ids
  hero_unit_archetype_bindings
  unlocked_hero_ids_by_unit_archetype
  barracks_training_ids
  research_unlock_ids
  transaction_receipts
```

- pre-run hero registration 필드는 요구하지 않는다.
- node ID·hero ID·unit archetype ID는 안정 식별자를 사용한다.
- 중복 구매·중복 차감·병종 불일치·부분 저장을 허용하지 않는다.
- schema migration·journal replay·current/backup 복구는 기존 save 계약을 따른다.

## 9. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅이 일반 병사를 무가치하게 만든다 | 유효 | 원본 영웅 등급 토큰 유지 선택·기본 Profile 완주·sidegrade 검증 |
| 해금 영웅 효과가 자동 누적된다 | 유효 | 해금은 동병종 보관 토큰 변환 후보만 추가 |
| 주점이 가챠 UX로 변질된다 | 유효 | 공개 결정론적 노드·재굴림·중복 합성 금지 |
| 영웅이 다른 병종에 자유 배속된다 | 유효 | 영웅-UnitArchetype 고정 바인딩 |
| 영웅 변환이 보너스 병력을 만든다 | 유효 | 1토큰→1유닛 치환 불변식 |
| 병영이 무한 공격력 트리가 된다 | 유효 | sidegrade·유한 노드·전 구간 배율 금지 |
| 연구가 숨은 확률·생산량 버프가 된다 | 유효 | odds 조작·전 구간 생산 배율·자동 플레이 금지 |
| 세 시설이 런보다 중요해진다 | 유효 | MapRun 진입 1순위 |

## 10. 미확정 항목

- 영구재화 최종 명칭.
- 시설별 노드 수·비용·분기·환불.
- 병종별 영웅 명단·등급·능력.
- 동일 영웅 중복 배치와 동병종 활성 상한.
- 원본 영웅 등급 병종의 정확 능력 계약.
- 병영 훈련·연구 sidegrade 실제 목록.
- 보조 시설·보관함 변환의 최종 UI·아트·애니메이션.

## 11. 상태 경계

```text
DESIGN: USER_APPROVED_STRUCTURE
HERO_UNLOCK_AND_ROSTER: USER_APPROVED
HERO_TOKEN_CONVERSION_AND_DEPLOYMENT: USER_APPROVED
PRE_RUN_HERO_REGISTRATION: SUPERSEDED
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
