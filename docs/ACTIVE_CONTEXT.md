# Active Context

```yaml
updated_at: 2026-08-02
project: OMENWARD / 오멘워드
work_mode: TOTAL_PLANNING
current_phase: WORLD_OMENWARD_POLITICAL_ROLE_GRILL_ME_READY
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
current_planning_decision: OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1
current_branch: main
context_baseline_commit: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
working_branch: gpt/omenward-canon-recovery-20260802
active_base_version: 9.4.0
current_product: LEGACY_PROTOTYPE
latest_planning: USER_APPROVED / NOT_IMPLEMENTED
product_code_authority: NONE
codex_execution: BLOCKED
primary_platform: PC
future_platform: MOBILE_CONSIDERATION_ONLY
sheet_sync: CONTENT_READBACK_PASS / EXACT_HEAD_TRACKED_IN_SHEET_AND_PR
recovery_pr: 119_DRAFT
superseded_pr: 116_CLOSED_NOT_MERGED
runtime_validation: NOT_RUN
human_validation: NOT_RUN
simulation: NOT_RUN
```

`current_branch: main`과 `context_baseline_commit`은 정본 기준선을 뜻한다. 실제 쓰기 작업은 `working_branch`에서 수행하며 main 직접 변경을 의미하지 않는다.

## 1. 현재 작업

`OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1`의 권장 혼합안이 사용자 승인됐고 GitHub 정본과 Sheet bounded read-back이 통과했다.

```text
본질 = 현실과 외부 법칙 영역의 비의지적 경계 겹침
외형 = 생태적으로 자라는 물질적 패턴
베일 자체의 통일된 의지 = 없음
베일종의 독립 행위 가능성 = 별도 결정
```

현재 다음 작업은 `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1`이다. 오멘워드 조직, 루메른 왕국, 플레이어 지휘관 사이의 권한·책임·정치적 긴장을 확정한다.

## 2. 프로젝트 약속

> 공개된 세 전선의 공세를 읽고 건물과 TokenSource로 세 물리 릴의 미래 배열을 설계·영구 편집한 뒤, 얻은 병력을 한 전선에 비가역 커밋하고 결과 원인을 다음 설계에 반영한다.

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 3. 베일 존재론 승인 원칙

정본: `docs/design/APPROVED_OMENWARD_VEIL_ONTOLOGY_2026-08-02.md`

- 베일은 장소·장벽·신격이 아니라 현실과 이질적인 외부 법칙 영역의 접촉면과 겹침 과정이다.
- 베일 자체에는 통일된 의지·도덕·계획이 없다.
- 균사·혈관·결정·조직처럼 보이는 증식은 법칙 충돌의 물질적 패턴이다.
- 베일의 법칙은 공세별로 관측 가능한 유한 규칙 묶음이다.
- 징조는 겹침 전의 선행 공명으로 위협 구조를 예고하지만 결과를 확정하지 않는다.
- 균열 봉쇄는 국소 접촉면을 끊으며, 봉쇄 뒤에도 지형·생태·물질·기억에 상흔이 남을 수 있다.
- 베일종은 베일과 분리된 독립 행위자일 수 있으나 발생·지성·목적은 미확정이다.
- 외부 영역의 수·구조·기원과 최초 베일 발생 원인은 미확정이다.

```text
NO_SENTIENT_VEIL_GOD
NO_UNIFIED_VEIL_PLAN
NO_ARBITRARY_VEIL_MAGIC
NO_BIOLOGICAL_LIFE_ASSUMPTION
NO_LOCAL_VICTORY_NULLIFICATION
```

## 4. 세계·MapRun 승인 원칙

정본: `docs/design/APPROVED_OMENWARD_WORLD_RUN_MOTIVATION_2026-08-02.md`

- 하나의 MapRun은 징조로 감지된 별개의 실제 경계 공세를 막는 방어 작전이다.
- 20 Stage·4막은 한 공세와 겹침 강도가 단계적으로 고조되는 구조다.
- Stage 20 승리는 한 균열·침공로를 실제로 봉쇄한다.
- 패배는 전진 방어선 붕괴와 실제 피해이며 paid Retry는 같은 공세의 비상 재투입이다.
- Profile은 여러 실제 작전에서 축적된 교리·보급망·기록·준비 체계다.
- 벨루는 작전을 관측·기록하고 인과를 설명하는 안내자다.

## 5. 기존 세계관 명칭 계보

- 루메른 왕국, 루미엔 영토, 트리븐 전선, 실베른 성채.
- 베일런 황야, 베일의 법칙, 베일의 징조, 베일종.
- 벨루.

명칭은 보존한다. 베일·법칙·징조·균열·상흔의 상위 관계는 확정됐지만 정치적 소유·어원·정확한 지리와 역사는 아직 확정하지 않았다.

## 6. 보호할 게임 시스템

- 20 Stage·4막·약 35분 목표.
- 위험 Stage 5/10/15/20.
- 상·중·하 세 라인.
- 세 물리 원형 릴·TokenInstance·cursor·3×3 view.
- 가로 이동은 future reel structure에 영구 반영, undo 없음.
- immutable SpinSnapshot과 명시적 한 번 확정.
- PendingReward 보관·판매·한 라인 비가역 배치.
- 본진 6노드/진영, 중간 거점 6곳×3노드, 총 30노드.
- 금고·농장·타워·병영·지휘소.
- 고정시간 점령.
- Stage 5 이후 MapRun당 최대 1회 paid Retry 원칙.
- 정본 안내자 `벨루 / Belu`.

## 7. Profile 영구 성장 경계

```text
PRIMARY = 수평 해금 + 제한된 편의
SECONDARY = 선택형·상한형 준비 보정
FORBIDDEN = 무한 영구 능력치 누적
```

세계관상 Profile은 실제 작전의 교리·보급·기록 축적이다.

## 8. 실제 구현 경계

```text
CURRENT_LEGACY
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry

LATEST_APPROVED_NOT_IMPLEMENTED
- three physical reels and permanent movement
- 30-node product topology
- five-building economy
- fixed-time capture
- profile/checkpoint/journal/backup
- paid Retry
- world-run principle
- Veil ontology
- horizontal unlocks and selectable readiness perk
```

`APPROVED_PLAN != IMPLEMENTED != VALIDATED`.

## 9. 세계관 결정 순서

1. `OMW-DEC-20260802-WORLD-VEIL-ONTOLOGY-V1` — 승인·정본·Sheet read-back 완료.
2. `OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1` — 오멘워드·루메른 왕국·지휘관의 조직 및 정치적 위치.
3. `OMW-DEC-20260802-WORLD-VEILSPECIES-PURPOSE-V1` — 베일종·경계파쇄자의 발생·지성·목적.
4. `OMW-DEC-20260802-WORLD-REEL-METAPHYSICS-V1` — 징조와 세 물리 릴·TokenSource의 세계 내 원리.
5. 트리븐 전선·실베른 성채·베일런 황야의 지리와 역사.
6. 벨루의 종족·기원·조직과의 관계.
7. 승패와 베일 상흔이 지역·세력·인물에게 남기는 지속 결과.

## 10. 다음 Gate

```text
Grill Me: OMW-DEC-20260802-WORLD-OMENWARD-POLITICAL-ROLE-V1
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
PR_MERGE: NOT_REQUESTED
WORLD_DETAIL: PARTIALLY_APPROVED
```