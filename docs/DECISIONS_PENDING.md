# [현행] 오멘워드 미확정 결정 목록

```yaml
updated_at: 2026-08-04
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_decision: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
current_process_policy: OMW-PROC-20260804-DYNAMIC-CURRENT-MAIN-AND-DOCUMENT-LIFECYCLE-V1
current_grill_me_count: 2_OF_10
product_code_authority: NONE
art_asset_production_authority: NONE
image_generation: STOPPED_BY_USER
```

- 전체 시스템 연결 기준선: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 현행 GDD: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- Stage 압력 정본: `docs/design/APPROVED_OMENWARD_STAGE_WAVE_DANGER_BOSS_PRESSURE_MATRIX_2026-08-04.md`
- 문서 수명주기: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`

## 1. Decision 2/10으로 해결된 항목

- 20 Stage를 4막×5 Stage로 분리.
- 기본 Stage를 3개 Wave Beat 기준선으로 정의.
- Danger Stage를 4·9·14·19로 배치.
- Boss Stage를 5·10·15·20으로 배치.
- Normal·Danger·Boss의 서로 다른 Wave 문법 확정.
- `MASS / ARMORED / FLYING / INFILTRATION / SIEGE`를 20 Stage에 배치.
- Danger는 한 가지 공개 규칙 변형만 사용.
- Boss는 Route·태세·목표·호위·집중 공격 기회를 변경.
- 압력 역할은 고정하고 적 패키지·전선·Route는 맵별 작성 변형으로 분리.
- Stage 시작 뒤 치명적 압력·필수 카운터를 숨은 무작위로 변경하지 않음.
- `15웨이브=1스테이지` 구형 계약을 `[대체됨]` 처리.
- 구형 첫 4공세 수치·식량·자동생산 문서를 `[보류]` 처리.

## 2. 다음 Decision — 건물 6종 T2/T3 분기·카운터

`OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1`

다룰 내용:

- 금고·농장·병영·방어탑·지휘소·마력탑의 T1 공통 정체성.
- 각 건물의 T2 양자택일 분기.
- T3가 같은 계열을 어떻게 전문화하는가.
- 각 분기가 `MASS / ARMORED / FLYING / INFILTRATION / SIEGE` 중 어떤 압력에 강한가.
- 다른 압력에서 어떤 기회비용이 생기는가.
- 건물·병종·전술스킬 사이 역할 중복 방지.
- MapRun 전체 지휘소 오라와 전선별 방어탑의 역할 분리.
- TokenSource 건물의 분기가 미래 릴 구성에 어떻게 보이는가.

다루지 않을 내용:

- exact 비용·생산량·피해·사거리·쿨다운.
- 업그레이드 시간·수치 배율.
- Scene·Resource·데이터 Schema.
- 제품 코드.

## 3. 다음 Decision이 반드시 답할 질문

1. 금고 분기가 단순 골드 증가와 무료 보상 중 어느 선택을 만들며 룰렛과 어떻게 연결되는가.
2. 농장 분기가 병력 수와 정예 운용 사이의 실제 선택을 만드는가.
3. 병영 분기는 병종 Decision을 침범하지 않으면서 TokenSource 전략을 어떻게 바꾸는가.
4. 방어탑이 `MASS / ARMORED / FLYING / SIEGE`를 모두 해결하는 만능 정답이 되지 않는가.
5. 지휘소의 MapRun 전역 오라가 전선 배치를 무의미하게 만들지 않는가.
6. 마력탑이 전술스킬 Decision 전에도 획득·저장 선택을 설명할 수 있는가.
7. 각 분기에 최소 하나의 명확한 강점과 하나의 실제 포기 비용이 있는가.

## 4. 후속 Planning Batch

```text
[완료] 1/10 핵심 재미·콘텐츠 가드레일
[완료] 2/10 Stage·Wave·Danger·Boss 압력 매트릭스
[다음] 3/10 건물 6종 T2/T3 분기·카운터
4/10 T1/T2/T3 병종 역할·시너지·카운터
5/10 전술스킬·마석 획득/소비
6/10 Stage 종료 상인 재고·가격·이벤트
7/10 최신 첫 10~15분 흐름·벨루
8/10 Hero·Legendary family 재조정
9/10 Meta·Hub 재조정
10/10 통합 플레이 시나리오·구현 handoff readiness
```

## 5. Stage 수치·콘텐츠 미확정

Stage 구조는 승인됐지만 다음은 아직 고정하지 않는다.

- 정확한 Wave 길이와 전환 시간.
- Spawn Group 수·간격.
- 적 개체 수·HP·Damage·Threat Budget.
- 맵별 실제 적 패키지와 전선 배치.
- Danger·Boss 보상.
- Boss 외형·이름·서사·정확 패턴 수치.
- 난이도별 Wave 겹침·수량 강화.

이는 건물·병종·전술 대응이 확정되고 시뮬레이션 근거가 생긴 뒤 조정한다.

## 6. [보류] 항목

- 구형 첫 10분 타임라인.
- 구형 첫 4공세 수치·식량·병영 자동생산.
- Hero·Legendary 획득·배치·자동 스킬·고유 스킬 문서군.
- Meta Profile·ReadinessPerk·주점·허브 병영·연구.
- 과거 V2 구현 계획.

상세 파일 목록은 `DOCUMENT_LIFECYCLE_REGISTRY.md`가 소유한다.

## 7. [폐기] 항목

- 식량을 현행 핵심 HUD 자원으로 사용.
- 기본 건물 5종.
- 지휘소 주변 범위 오라.
- `15웨이브=1스테이지`와 고정 60초 공세.
- Danger에서 핵심 기능·치명적 정보를 제거.
- 전투 중 필수 카운터·주 전선을 숨은 무작위로 변경.
- 룰렛 전용 금화·병종 상징 아이콘.
- T3 병종 룰렛 토큰.

## 8. 실제 아트 제작 전 결정

- Stage 압력별 적 실루엣·Route 아이콘.
- Danger·Boss 징조 표시 문법.
- 건물 분기별 실루엣 차이.
- 병종 역할·Counter 시각 문법.
- T1·T2 토큰 크롭 안전 영역.
- Boss VFX 화면 점유 제한.

사용자 별도 지시 전 실제 제작하지 않는다.

## 9. Codex 구현 결정

```text
coordinate unit and numeric representation
stage/wave data schema
spawn group structure and scheduling
fixed/variable tick implementation
pathfinding, avoidance and collision algorithms
targeting search and distance implementation
stage transition, checkpoint and serialization
performance and test architecture
```

플레이어 경험·콘텐츠 역할을 바꾸는 선택은 기획 Gate로 되돌린다.

## 10. 계속 금지되는 항목

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
IMAGE_GENERATION = STOPPED_BY_USER
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 11. Merge Cadence

```text
CURRENT_COUNT = 2/10
NEXT_PREFLIGHT = AFTER_10_APPROVED_DECISIONS_OR_HIGH_RISK_CANON_CHANGE
CURRENT_PR = FRESH_PREFLIGHT_REQUIRED_BECAUSE_STAGE_AUTHORITY_AND_LEGACY_CONFLICT_CHANGED
```
