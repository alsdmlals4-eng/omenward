# OMENWARD 프로젝트 인수인계 컨텍스트

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
phase: GAMEPLAY_HERO_UNIQUENESS_LIMIT_GRILL_ME_READY
current_world_decision: OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1
current_meta_decision: OMW-DEC-20260802-GAMEPLAY-HERO-BATTLEFIELD-ACTIVATION-V1
current_operating_decision: OMW-DEC-20260802-GRILL-ME-MERGE-CADENCE-V1
baseline_main: 12012f88bc1dc1d9aaaa538b578be3893e4b1591
working_branch: gpt/omenward-gameplay-planning-20260802
last_merged_pr: 120
superseded_pr: 116_CLOSED_NOT_MERGED
base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_BRANCH_SYNCED_NOT_IMPLEMENTED
product_code_authority: NONE
codex: BLOCKED
current_grill_me_count: 3
future_merge_cadence: 10
```

## 1. 현재 정본

- 오멘워드는 건물과 TokenSource로 세 물리 릴을 설계하고 당첨 병력을 세 전선에 비가역 배치하는 전략 오토배틀이다.
- 현재 제품은 Legacy 프로토타입이고 최신 기획은 미구현이다.
- 세계관은 `균열을 통해 넘어온 이계 생물종` 정도로만 사용자에게 제시한다.
- 적은 군집·돌격·원거리·방호·교란·공성 역할로 제작하며 경계파쇄자는 균열을 고정·확장하는 보스급 생물이다.
- 메인 허브 보조 콘텐츠는 주점·허브 병영·연구다.
- 영웅은 기존 병종에 고정 연결되며 같은 병종에 여러 영웅을 해금할 수 있다.
- 주점 해금은 Profile 영웅 명부 등록이며 별도 pre-run 영웅 편성은 없다.
- 룰렛의 동병종 `[영웅]` 등급 토큰을 보관한 뒤 원본 유지 또는 해금 영웅 변환을 선택한다.

## 2. 영웅 계약

```text
병종별 영웅 후보 복수 가능
→ 주점에서 영구 해금·명부 등록
→ 동병종 [영웅] 등급 토큰을 룰렛에서 획득
→ 보관함에서 원본 또는 해금 영웅 선택
→ 1토큰을 1유닛으로 치환
→ 한 전선에 비가역 배치
```

- 다른 병종 영웅은 후보가 아니다.
- 해금 영웅은 릴 확률·전역 능력치·과거 결과를 바꾸지 않는다.
- 영웅 변환은 보너스 병력을 추가하지 않는다.
- 변환하지 않은 원본 영웅 등급 병종도 정상 배치 가능하다.
- 배치 확정 전에는 취소·후보 변경 가능, 확정 뒤 되돌릴 수 없다.
- 동일 영웅 중복 배치와 동병종 활성 상한은 pending이다.

## 3. 보호할 코어

- PC-primary.
- 20 Stage·4막·약 35분.
- 위험 Stage 5·10·15·20.
- 세 물리 릴·비가역 가로 이동·SpinSnapshot.
- 보관·판매·한 라인 비가역 배치.
- 전장 3라인, 건설 노드 1종, 전체 30개.
- MapRun 건물 5종: 금고·농장·타워·전장 병영·지휘소.
- fixed-time capture·paid Retry 원칙·벨루 비모달 안내자.
- 기본 Profile로 모든 콘텐츠 완료 가능.

## 4. 보조 허브 경계

```text
메인 1순위 = 이어하기·새 작전
보조 시설 = 주점·병영·연구
노드 = 유한·비용/선행/결과 공개
```

- 주점: 병종별 복수 영웅 후보 해금·명부 관리.
- 보관함: 영웅 등급 토큰의 원본 유지 또는 동병종 해금 영웅 변환.
- 허브 병영: 병사·병종·전문화·교리 sidegrade.
- 연구: 대체 건물·TokenSource·미션·정보·편의 sidegrade.
- 금지: 랜덤 유료 영입, 중복 합성, 무한 레벨, 전 구간 배율, 숨은 릴 확률, 자동 플레이.

## 5. current authority

- `docs/PROJECT_CORE.md`
- `docs/PROJECT_CANON_DECISION_LEDGER.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/design/APPROVED_OMENWARD_HERO_UNLOCK_REGISTRATION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_HERO_TOKEN_CONVERSION_AND_DEPLOYMENT_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VEILSPECIES_GAMEPLAY_SCOPE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_AUXILIARY_HUB_PROGRESSION_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_META_PROGRESSION_ROLE_2026-08-02.md`
- `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- `docs/operations/GRILL_ME_MERGE_CADENCE_AND_PREFLIGHT_2026-08-02.md`

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
- minimal extradimensional-creature gameplay scope
- Tavern/Barracks/Research permanent-node hub
- multi-hero-per-unit unlock roster
- stored Hero-grade token conversion and irreversible deployment
```

## 7. Grill Me 운영

- 현재 승인 카운터는 `3/10`이다.
- 10번째 승인 시 병합 preflight를 실행한다.
- blocker가 있으면 병합하지 않는다.

## 8. 다음 Gate

```text
OMW-DEC-20260802-GAMEPLAY-HERO-UNIQUENESS-AND-ACTIVE-LIMIT-V1
= 영웅 등급 토큰이 여러 번 나왔을 때 동일 영웅과 동병종 영웅을 한 런에 몇 번 배치할 수 있는가
```

```text
EXACT_VALUES: PENDING
SIMULATION: NOT_RUN
RUNTIME: NOT_RUN
HUMAN_QA: NOT_RUN
PRODUCT_CODE: UNCHANGED
```
