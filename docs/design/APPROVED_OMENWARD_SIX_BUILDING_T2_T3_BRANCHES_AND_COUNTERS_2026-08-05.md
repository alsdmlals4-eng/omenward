# [대체됨] OMENWARD 건물 6종 T2/T3 분기·카운터 정본

```yaml
decision_id: OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
approved_at: 2026-08-05 00:41 KST
status: SUPERSEDED / HISTORICAL_EVIDENCE_ONLY / IMPLEMENTATION_INPUT_FORBIDDEN
superseded_by: OMW-DEC-20260806-PLANNING-BUILDING-TIER-REALIGNMENT-V1
product_code_authority: NONE
```

## 수명주기 통지

이 문서는 2026-08-05 당시 승인된 건물 A/B 분기 설계의 역사적 증거다. 사용자가 건물의 실제 Tier 의도를 다시 정의했으므로 현재 기획·구현 입력으로 사용할 수 없다.

현행 책임 원본:

`docs/design/APPROVED_OMENWARD_BUILDING_TIER_REALIGNMENT_2026-08-06.md`

## 사용 금지된 이전 구조

```text
모든 6종 건물 공통 A/B 분기 = 사용 금지
안정 금고 / 행운 금고 = 사용 금지
징집 농장 / 예비 농장 = 사용 금지
전열 병영 / 기동 병영 = 사용 금지
연사탑 / 포격탑 = 사용 금지
돌격 지휘소 / 수비 지휘소 = 사용 금지
유량 마력탑 / 저장 마력탑 = 이미 후속 전술·마력 정본에서 대체됨
```

## 현행 구조 요약

```text
일반병 병영 T1
= 기본 보병 자동생산 + 기본 보병 TokenSource

일반병 병영 T2
= 방패병 / 대검병 / 창병 / 궁병 / 기병 전문화
+ 선택 병종 자동생산
+ 선택 병종 TokenSource

특수병 병영 T1
= 특수병 5종 중 하나 무작위 자동생산
+ TokenSource 없음

특수병 병영 T2
= 마도사 / 사제 / 암살자 / 비행병 / 거인 전문화
+ 선택 병종 자동생산
+ 선택 병종 TokenSource

방어탑 T2
= 포격탑 / 방어탑(방어 강화형) / 저격탑

금고 / 농장 / 지휘소 / 마력탑
= 분기 없는 직선 Tier 강화
```

## 보존 범위

이전 문서의 세부 내용은 Git 이력과 다음 증거 문서에서 확인할 수 있다.

- `docs/superpowers/specs/2026-08-05-six-building-t2-t3-branches-design.md`
- `docs/reviews/ADVERSARIAL_BUILDING_BRANCH_COUNTER_AND_OPPORTUNITY_COST_REVIEW_2026-08-05.md`
- PR #138

이 증거들은 과거 승인·검토 사실만 증명하며 신규 기획·제품 구현을 승인하지 않는다.

```text
PRODUCT_CODE = UNCHANGED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
