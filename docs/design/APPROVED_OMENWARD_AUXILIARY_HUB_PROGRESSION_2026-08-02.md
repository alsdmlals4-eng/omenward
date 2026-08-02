# 오멘워드 메인 허브 보조 콘텐츠·영구 노드 승인 계약

```yaml
decision_id: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
approved_at: 2026-08-02 15:09 KST
approval: USER_DIRECT_APPROVAL_WITH_ADVERSARIAL_GUARDRAILS
status: USER_APPROVED_STRUCTURE / EXACT_VALUES_PENDING / NOT_IMPLEMENTED
work_mode: TOTAL_PLANNING
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

## 1. 결정 요약

메인 화면에는 런 진입과 별개인 **보조 콘텐츠 허브**를 둔다. 보조 콘텐츠는 `주점·병영·연구` 세 시설로 구성하며, 정산된 Profile 영구재화를 사용해 유한한 노드 그래프를 개방한다.

```text
MAIN_HUB_PRIMARY_ACTION = MAPRUN_ENTRY
AUXILIARY_FACILITIES = TAVERN + BARRACKS + RESEARCH
PURCHASE_CURRENCY = SETTLED_PERMANENT_CURRENCY_BALANCE
NODE_MODEL = FINITE_VISIBLE_PREREQUISITE_GRAPH
RANDOM_PAID_RECRUITMENT = FORBIDDEN
UNBOUNDED_STAT_GRIND = FORBIDDEN
```

세 시설은 별도 게임 모드가 아니라 오멘워드 조직의 작전 준비·인재·교리 축적을 보여 주는 메인 허브 진입점이다.

## 2. 공통 노드 구조

모든 시설은 같은 거래 원칙을 공유한다.

- 정산이 끝난 영구재화만 소비한다.
- 각 노드의 비용·선행 노드·해금 결과를 구매 전에 공개한다.
- 구매는 명시적 확인 뒤 transaction journal과 idempotent receipt로 기록한다.
- 노드는 유한하며 무한 prestige·반복 구매·끝없는 능력치 누적을 허용하지 않는다.
- 기본 Profile만으로도 전체 콘텐츠 완료가 가능해야 한다.
- 해금 전 기본 구성도 완전한 게임이며 체험판 상태로 취급하지 않는다.
- 비용·노드 수·분기 수·환불·초기화 규칙은 simulation과 별도 사용자 승인 전 제품값으로 고정하지 않는다.

## 3. 주점

### 3.1 역할

주점은 여러 작전과 지역에서 발견한 **영웅 이상 등급의 전문 인재를 영구 영입**하고 명부를 관리하는 시설이다.

```text
RECRUITMENT = DETERMINISTIC_VISIBLE_NODE_UNLOCK
ROSTER_OWNERSHIP = PERMANENT
RUN_DEPLOYMENT_CAP = REQUIRED / EXACT_CAP_PENDING
HERO_GRADE_TAXONOMY = PENDING
```

### 3.2 승인 원칙

- 영입 후보·비용·전제 조건을 노드에서 사전에 공개한다.
- 랜덤 상자·확률 뽑기·유료 재굴림으로 영웅을 구매하지 않는다.
- 영웅은 일반 병사를 삭제하는 단순 상위 능력치 묶음이 아니라 고유 역할·지휘 규칙·조건·기회비용을 가진다.
- 영입은 영구지만 한 MapRun에 동시에 활성화·배속할 수 있는 영웅 수는 제한한다.
- 활성화 상한의 권장 후보는 `한 런 1계약`이지만 이는 `RECOMMENDED_DEFAULT`이며 별도 승인 전 확정값이 아니다.
- 영웅을 보유하지 않은 기본 Profile도 모든 Stage를 완료할 수 있어야 한다.
- `영웅 이상`의 정확한 등급명·단계 수·희귀도 관계는 후속 콘텐츠 결정으로 남긴다.

### 3.3 금지

- 현실 화폐 결제 또는 프리미엄 능력 구매.
- 중복 영웅을 합성해 무한 능력치를 올리는 구조.
- 영웅 미보유를 이유로 특정 핵심 Stage를 사실상 차단.
- 확률 공개 없이 재화를 소모하는 랜덤 영입.
- 메인 화면을 영웅 초상화·등급 카드 중심의 일반 수집형 RPG처럼 구성.

## 4. 병영

### 4.1 역할

병영은 병사 훈련·교리·병종 선택 폭을 확장하는 시설이다. 전장 건물 `병영`과 이름은 같지만, 메인 허브의 병영은 **Profile 훈련 시설**, MapRun의 병영은 **TokenSource 건물**이다. UI와 문서에서 두 책임을 구분한다.

```text
HUB_BARRACKS = PROFILE_TRAINING_AND_DOCTRINE
MAPRUN_BARRACKS = PHYSICAL_TOKENSOURCE_BUILDING
```

### 4.2 승인 원칙

- 새로운 병종·전문화·시작 교리·훈련 선택지를 sidegrade로 해금한다.
- 병종 해금은 역할과 조건을 추가하며 모든 기존 병종의 공격력·방어력을 일괄 상승시키지 않는다.
- 제한된 초기 준비 보정은 기존 `ReadinessPerk` 계약을 따르며 한 런 1개·유한 랭크·시작/Act 1 범위를 넘지 않는다.
- 훈련 노드는 어떤 토큰과 TokenSource가 새로 사용 가능해지는지 명시한다.
- 특정 훈련이 모든 공세·릴 구조·난이도에서 우월하면 sidegrade 실패로 판정한다.

### 4.3 금지

- 무한 레벨·무한 훈련 반복.
- 모든 유닛 공격력·공격속도·치명타·방어력의 전 구간 영구 배율.
- 반복 노가다로 Stage 5·10·15·20 기믹을 무시.
- 해금하지 않은 기본 병사를 의도적으로 불완전하게 설계.

## 5. 연구

### 5.1 역할

연구는 베일 법칙·징조·봉쇄 기록을 분석해 새로운 시스템 선택지와 정보·편의를 해금하는 시설이다.

허용 후보:

- 대체 건물·TokenSource·미션의 sidegrade 분기.
- 공세·징조·법칙 도감과 복기 분석.
- 시작 구성안·필터·선택 이력 같은 비전투 편의.
- 제한된 시작 보관 편의의 hard-cap 확장.
- 벨루의 추가 분석 기록.

### 5.2 금지

- 릴 당첨 확률을 숨겨서 유리하게 조작.
- 금고·농장·건물 생산량의 전 구간 영구 배율.
- 자동 건설·자동 배치·자동 릴 편집으로 핵심 판단 제거.
- 연구 완료만으로 모든 베일 법칙의 정답을 사전 공개.
- 연구 트리가 사실상 필수 순서 하나로 수렴.

## 6. 영구재화와 Retry의 관계

기존 Profile 계약을 유지한다.

```text
settled_permanent_currency_balance
= 주점·병영·연구 노드 + paid Retry의 소비 지갑

settled_permanent_currency_total
= 감소하지 않는 누적 진행도·Readiness milestone 판정
```

노드 해금과 Retry가 같은 소비 잔액을 사용하므로 명확한 기회비용이 생긴다. 이는 허용하지만 다음을 검증해야 한다.

- 플레이어가 Retry를 위해 노드를 영구적으로 미루는 과도한 비축 전략.
- 노드 구매 후 Retry 여력이 사라져 후회·중단이 커지는지.
- 특정 시설이 재화 효율상 항상 우선되는지.
- 실패 보상 파밍이 최적 진행법이 되는지.

정확 획득량·비용·환불은 100K Profile trajectory와 사람 검증 뒤 승인한다.

## 7. 메인 화면 정보 위계

```text
1순위 = 이어하기·새 MapRun·현재 작전 상태
2순위 = 영구재화 잔액·현재 Profile 준비 상태
3순위 = 주점·병영·연구 보조 시설
4순위 = 도감·기록·설정
```

- 보조 시설은 런 진입을 가리거나 메인 화면을 상점처럼 만들지 않는다.
- 각 시설은 현재 개방 가능 노드와 새 알림 수를 간결하게 표시한다.
- 잠긴 노드는 선행 조건과 결과를 공개한다.
- 구매 버튼에는 비용·잔액·비가역성 또는 환불 규칙을 함께 표시한다.
- 영웅 초상화는 주점 내부에서 명부 확인에 사용하되 메인 화면 전체를 파티 편성 화면으로 만들지 않는다.
- 키보드·마우스 포커스 순서와 색 외 잠금·해금 표시를 제공한다.

## 8. 저장 책임

ProfileSave는 최소 다음을 구분한다.

```yaml
AuxiliaryHubProgressionState:
  settled_permanent_currency_balance
  settled_permanent_currency_total
  unlocked_node_ids
  tavern_recruit_ids
  barracks_training_ids
  research_unlock_ids
  selected_run_loadout_ids
  transaction_receipts
```

- node ID는 시설을 포함한 안정 식별자를 사용한다.
- 중복 구매·중복 차감·부분 저장을 허용하지 않는다.
- schema migration·journal replay·current/backup 복구는 기존 경제·Retry·save 계약을 따른다.

## 9. 적대적 검토

| 공격 | 판정 | 보완 |
|---|---|---|
| 영웅 영입이 일반 병사를 무가치하게 만든다 | 유효 | 고유 역할·조건·출전 상한·기본 Profile 완주 불변 조건 |
| 주점이 랜덤 뽑기와 과금 UX로 변질된다 | 유효 | 공개된 결정론적 노드 영입, 유료 재굴림·확률 구매 금지 |
| 병사 훈련이 결국 무한 공격력 트리다 | 유효 | sidegrade 중심, 유한 노드, 전 구간 전투 배율 금지 |
| 연구가 숨은 확률·생산량 버프가 된다 | 유효 | 릴 확률 조작·전 구간 생산 배율·자동 플레이 금지 |
| 세 시설이 런보다 더 중요한 메뉴 게임이 된다 | 유효 | MapRun 진입 1순위, 시설은 2차 허브 콘텐츠 |
| Retry와 노드가 같은 재화를 써서 후회가 커진다 | 유효 | 비용·잔액·기회비용 공개, 100K trajectory·사람 검증 필수 |
| 영구 노드 수가 계속 늘어 콘텐츠 부채가 된다 | 유효 | 유한 그래프·시즌성 무한 추가 금지·대표 범위 우선 |
| 영웅 이상 등급이 곧 강제 희귀도 계단이 된다 | 유효 | 등급명은 콘텐츠 분류이며 단순 수치 우위는 별도 검증 |

## 10. 미확정 항목

- 영구재화의 최종 명칭.
- 시설별 노드 수·비용·분기 구조·해금 순서.
- 영웅 명단·등급 체계·능력·출전 상한.
- 병영 훈련의 정확한 병종·전문화 범위.
- 연구 sidegrade의 실제 목록.
- 환불·초기화·프리셋·알림 세부 UX.
- 보조 시설의 최종 아트·배치·애니메이션.

## 11. 상태 경계

```text
DESIGN: USER_APPROVED_STRUCTURE
EXACT_VALUES: PENDING
CONTENT_LIST: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
