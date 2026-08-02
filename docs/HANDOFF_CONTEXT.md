# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: PR_119_MERGE_PREFLIGHT
recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_world_decision: OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1
current_meta_decision: OMW-DEC-20260802-META-HUB-AUXILIARY-CONTENT-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
merge_batch_pr: 119
superseded_pr: 116_CLOSED_NOT_MERGED
base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
merge_authorization: USER_APPROVED / PREFLIGHT_REQUIRED
current_grill_me_count: 4
```

## 1. 현재 정본

- 오멘워드는 건물과 TokenSource로 세 물리 릴을 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 현재 제품은 Legacy 프로토타입이고 최신 기획은 미구현이다.
- 각 MapRun은 별개의 실제 경계 공세이며 징조는 제한된 예측 정보다.
- 베일은 현실과 이질적 외부 법칙 영역의 비의지적 경계 겹침이다.
- 오멘워드는 루메른 왕실 인가 자율 경계대응단이다.
- 플레이어는 활성 작전에서 제한된 비상 지휘권을 가진 현장 지휘관이지 통치자가 아니다.
- Profile 영구 성장은 수평 해금·제한 편의 + 한 런 1개 상한형 준비 보정이다.
- 메인 허브 보조 콘텐츠는 주점·허브 병영·연구다.
- 정산 영구재화로 유한한 공개 노드를 개방한다.
- 주점 영웅 영입은 공개 결정론적 노드이며 랜덤 뽑기·유료 재굴림이 아니다.

## 2. 보호할 코어

- PC-primary.
- 20 Stage·4막·약 35분.
- 위험 Stage 5·10·15·20.
- 세 물리 릴·비가역 가로 이동·SpinSnapshot.
- 보관·판매·한 라인 비가역 배치.
- 전장 3라인, 건설 노드 1종, 전체 30개.
- MapRun 건물 5종: 금고·농장·타워·전장 병영·지휘소.
- fixed-time capture.
- Stage 5 이후 MapRun당 최대 1회 paid Retry 원칙.
- 벨루 비모달 안내자.
- 기본 Profile로 모든 콘텐츠 완료 가능.

## 3. 보조 허브 경계

```text
메인 1순위 = 이어하기·새 작전
보조 시설 = 주점·병영·연구
노드 = 유한·비용/선행/결과 공개
```

- 주점: 영웅 이상 전문 인재 명부·영구 영입. 출전 상한과 실제 능력은 pending.
- 허브 병영: 병사 훈련·병종·전문화·교리 sidegrade. 전장 TokenSource 병영과 구분.
- 연구: 대체 건물·TokenSource·미션·징조 분석·편의 sidegrade.
- 금지: 랜덤 유료 영입, 무한 레벨, 전 구간 전투/생산 배율, 숨은 릴 확률 조작, 자동 플레이.
- 영구재화 balance는 노드·Retry 소비, total은 비감소 milestone 판정.

## 4. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_POLITICAL_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`

PR #116은 역사 승인 증거이며 병합·current local authority가 아니다.

## 5. 현재 병합 절차

1. GitHub·Sheet에 세 신규 Decision ID 반영.
2. current authority 경로 존재 확인.
3. PR 전체 changed path와 제품 경로 0변경 확인.
4. 댓글·리뷰·미해결 thread 확인.
5. exact HEAD에서 필수 CI 3개 Green 확인.
6. 적대적 premerge review에서 P0/P1 blocker 0 확인.
7. PR Ready 전환 후 expected-head squash merge.
8. main 파일·merge commit 재조회.
9. Sheet를 merged main SHA와 `SYNCED_TO_MAIN / MERGE_VERIFIED`로 갱신.
10. 새 branch·새 Draft PR, Grill Me counter `0/10`.

## 6. 실제 구현 경계

```text
CURRENT_PRODUCT
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- physical reels and permanent movement
- 30-node topology and five buildings
- paid Retry and Profile save
- world/Veil/political canon
- Tavern/Barracks/Research permanent-node hub
- deterministic Hero+ roster
```

## 7. 병합 후 다음 Gate

```text
OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
= 베일종·경계파쇄자의 발생·지성·사회·침공 목적
```

```text
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
