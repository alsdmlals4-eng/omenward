# OMENWARD 픽셀·일러스트 하이브리드 정본 Post-Merge Sync

```yaml
sync_id: OMW-SYNC-20260804-POST-MERGE-PIXEL-ILLUSTRATION-HYBRID-CANON-V1
status: MAINTENANCE_SYNC / NON_COUNTER
source_pr: 133
source_head: 48466c4f669e24e19e2c8be3f4c879bdbfda04a9
merged_main: d8ce26ee3ee21dbab50839b7a1334116e147789e
approved_decision: OMW-DEC-20260804-PLANNING-PIXEL-ILLUSTRATION-HYBRID-ART-DIRECTION-V1
previous_counter: 10_OF_10
next_counter: 0_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

## 목적

PR #133의 10/10 기획 정본이 main에 squash merge된 사실을 중앙 문서와 Google Sheet에 동기화한다. 이 Sync는 새 제품 Decision이 아니며 카운터에 포함하지 않는다.

## 확정 상태

- 픽셀·일러스트 하이브리드가 현행 main 아트 방향이다.
- 전장은 픽셀풍 가독성, 보상·도감·벨루는 일러스트풍 재질·표정을 우선한다.
- 금화 토큰은 인게임 금화 이미지를 재사용한다.
- 병종 토큰은 인게임 T1·T2 병종 이미지만 사용한다.
- T3 병종 이미지는 룰렛 병종 토큰에 사용하지 않는다.
- 결과 보상은 실제 지급 병종 이미지를 사용한다.
- 별도 금화·병종 토큰 아이콘 세트를 제작하지 않는다.
- 제품 코드·런타임·실제 아트 자산은 변경하지 않았다.
- 추가 이미지 생성은 중단 상태다.

## Preflight 증거

```text
PR #133 = MERGED
MERGE_COMMIT = d8ce26ee3ee21dbab50839b7a1334116e147789e
SOURCE_HEAD = 48466c4f669e24e19e2c8be3f4c879bdbfda04a9
CI = 842 / 558 / 539 PASS
BEHIND = 0
CHANGED_PATHS = 19 DOCS_ONLY
UNRESOLVED_THREADS = 0
OPEN_P0 = 0
OPEN_P1 = 0
MERGE_BLOCKER = 0
```

## 다음 작업

GPT/Work는 구현 세부가 아니라 다음 순서로 진행한다.

```text
핵심 재미와 반복 플레이 동기 심화
→ Stage·Wave·Danger·Boss 콘텐츠 구조
→ 건물 6종 T2/T3 분기와 카운터
→ 전술스킬·마석·Stage 종료 상인 콘텐츠
→ 병종·영웅·전설 역할과 시너지
→ UX·아트 검수 기준
→ 별도 승인 뒤 Codex 구현 계약
```

## 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
LATEST_PLANNING = MAIN_CANONICAL_NOT_IMPLEMENTED
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
