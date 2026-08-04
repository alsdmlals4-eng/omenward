# [현행] 오멘워드 GDD 정본 요약

```yaml
updated_at: 2026-08-04
status: CURRENT_GDD_CANON / PLANNING_ONLY / NOT_IMPLEMENTED
current_main: RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH
current_decision: OMW-DEC-20260804-PLANNING-STAGE-WAVE-DANGER-BOSS-PRESSURE-MATRIX-V1
current_count: 2_OF_10
vertical_slice_baseline: docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md
product_code_authority: NONE
art_asset_production_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: NOT_RUN
```

`APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`는 전체 시스템 연결 계보를 보존한다. 식량·건물 5종·주변 지휘소·구형 Stage 시계처럼 후속 현행 정본과 충돌하는 세부는 사용하지 않는다.

## 1. 한 문장

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 전략 오토배틀 게임.**

짧은 문구:

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

## 2. 핵심 루프

```text
Stage 전체 압력·Wave 순서 확인
→ 건설·업그레이드·수리와 TokenSource 구성
→ 세 원형 릴 회전
→ 3×3 노출창에서 릴·행 이동
→ 보상 확정
→ 보관·판매·한 전선 배치
→ 자동전투·점령·건물 운영
→ 결과 원인 복기
→ Stage 정비·상인
→ 다음 Stage 설계
```

세 원형 릴은 3×3 노출창의 세 열을 구성한다.

## 3. 핵심 재미

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과와 다음 설계
```

- **예측:** 다음 공세의 전선·역할·Route·특수 압력을 읽는다.
- **확률 설계:** 건물과 TokenSource로 미래 릴 구성을 바꾼다.
- **제한 조작:** 회전 뒤 제한된 이동권을 현재 결과와 미래 릴 중 어디에 쓸지 판단한다.
- **커밋:** 획득 병력을 보관·판매하거나 한 전선에 되돌릴 수 없이 배치한다.
- **복기:** 어떤 건물·이동·배치가 승패를 만들었는지 이해한다.

## 4. 전장

- 상·중·하 세 전선.
- 아군 본진, 중간 거점, 중앙 접전, 적 거점, 적 본진의 전진 구조.
- 주 경로·우회로·공중 Route를 화면에서 구분한다.
- Ground·Flying·침투 역할을 시각과 Targeting 규칙으로 구분한다.
- 기본 공격은 같은 전선/Route의 유효 대상을 우선한다.
- Cross-lane 공격은 명시적 능력·건물만 허용하고 사전 표시한다.
- 아군 본진부터 적 본진까지 전장 전체 구도를 기본 화면에서 유지한다.

정확한 좌표·Pathfinding·충돌·거리식은 Codex 구현 계약이다.

## 5. 룰렛

- 세 개의 원형 릴과 3×3 노출창.
- 열 상하 이동과 행 좌우 이동.
- 이동권은 룰렛 패널 내부에 `n/3`으로 표시.
- 럭키 무료 이동은 저장 이동권과 구분.
- 보상 등급은 동일 심벌 완성선 수로 결정.
- TokenSource 현재 구성은 설명 가능해야 하지만 내부 가중치 표를 상시 노출하지 않는다.
- 보상은 명시적 확정 뒤 한 번만 지급한다.

자산:

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
```

## 6. 런 자원

| 자원 | 역할 |
|---|---|
| 골드 | 건설·업그레이드·수리·룰렛·Stage 종료 상인 |
| 마석 | 전술스킬 사용 |
| 배치 병력·병력 한도 | 전장에 유지할 수 있는 병력 규모 |
| 이동권 | 룰렛 보드·미래 릴 조작 |

식량은 현행 핵심 HUD 자원이 아니다.

## 7. 기본 건물 6종

| 건물 | 현행 역할 |
|---|---|
| 금고 | 골드 운영·인게임 금화 토큰 |
| 농장 | 배치 병력·병력 한도 |
| 병영 | 병종 TokenSource·Tier 분기 |
| 방어탑 | 선택 전선 방어 |
| 지휘소 | 현재 MapRun 전체 아군 병력 오라 |
| 마력탑 | 마석 수급·보유량 지원 |

- 건물별 지속 유지비는 없다.
- 토큰을 초당 공급하지 않는다.
- 정확한 T2/T3 분기·압력 카운터와 수치는 3/10 Decision이다.

## 8. HUD·상인·벨루

평상시 하단:

```text
[룰렛] [보관함] [건설] [전술스킬] [벨루]
```

- 상인은 전투 중 상시 버튼이 아니라 Stage 종료 정비시간에 방문한다.
- 벨루는 우측 하단에서 상황과 선택 근거를 1~2문장으로 설명한다.
- 정확한 수치·지속 상태는 HUD가 소유한다.
- 벨루가 플레이어 대신 결정을 내리지 않는다.

## 9. MapRun·Stage·Wave 구조

```text
한 MapRun = 20 Stage
기본 Stage = 3개 Wave Beat
Danger Stage = 4 / 9 / 14 / 19
Boss Stage = 5 / 10 / 15 / 20
```

Wave 문법:

```text
Normal = Probe → Complication → Commitment Test
Danger = Distortion Introduction → Overlap → Consequence
Boss = Approach → Boss Entry → Finale
```

- Wave Beat는 Spawn Group 수와 같은 뜻이 아니다.
- Wave 사이에는 기본 정비시간을 만들지 않는다.
- Stage 종료 뒤 정산·checkpoint·정비시간·상인이 이어진다.
- 구형 `15웨이브=1스테이지` 구조는 `[대체됨]`이다.
- 구형 첫 4공세 수치·식량·병영 자동생산은 `[보류]`다.

## 10. Stage 압력 매트릭스

압력:

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

네 막:

| 구간 | 목적 |
|---|---|
| Stage 1~5 | 다섯 압력의 행동·Route·목표를 구분 |
| Stage 6~10 | 두 압력을 함께 해결 |
| Stage 11~15 | 서로 충돌하는 대응의 기회비용 |
| Stage 16~20 | 세 전선·여러 Route 종합 숙련 |

Stage 순서:

| Stage | 유형 | 주 압력·규칙 |
|---:|---|---|
| 1 | Normal | `MASS` 처리량·병력 한도 |
| 2 | Normal | `ARMORED` 집중 화력 |
| 3 | Normal | `FLYING` 공격 가능 Layer |
| 4 | Danger | `INFILTRATION`; 공개된 우회 Route 활성 순서 |
| 5 | Boss | `SIEGE`; 가시적 파괴 준비와 집중 공격 창 |
| 6 | Normal | `MASS + ARMORED` |
| 7 | Normal | `FLYING + INFILTRATION` |
| 8 | Normal | `SIEGE + MASS` |
| 9 | Danger | 공개된 Wave 겹침 시간표 |
| 10 | Boss | 공중 Route·우회 Route 전환 |
| 11 | Normal | `ARMORED + FLYING` |
| 12 | Normal | `INFILTRATION + SIEGE` |
| 13 | Normal | `MASS + FLYING`; 세 전선 포화 |
| 14 | Danger | 전체 순서가 공개된 주 전선 이동 |
| 15 | Boss | 행군 태세·포격 태세 전환 |
| 16 | Normal | `MASS + FLYING + SIEGE` |
| 17 | Normal | `ARMORED + INFILTRATION + MASS` |
| 18 | Normal | `FLYING + SIEGE + INFILTRATION` |
| 19 | Danger | 공개된 Route 수렴과 결정 전선 |
| 20 | Final Boss | 범람·붕괴·사냥 Omen Pattern |

공정성:

- Stage 시작 전에 주·보조 압력, 전선, Route, 예상 목표, 치명적 특수 행동을 공개한다.
- Danger는 한 가지 전역 규칙 변형만 사용한다.
- Boss는 HP 증가가 아니라 Route·태세·목표·호위·집중 공격 기회를 바꾼다.
- 압력 역할·학습 목표는 고정하고 실제 적 패키지·전선 배치는 맵별 작성 변형으로 둔다.
- 변형은 Stage 시작 뒤 필요한 카운터를 몰래 바꾸지 않는다.
- 각 Stage에는 최소 두 대응 경로가 필요하다.
- 정확한 시간·Threat Budget·적 수치는 시뮬레이션 전 미확정이다.

## 11. 아트 방향

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
ALLY = IVORY / BLUE / RESTRAINED_GOLD
VEIL = CHARCOAL / DEEP_PURPLE / CRIMSON / ASYMMETRIC_GOTHIC
```

- 전장에서는 실루엣·전선·노드 판독이 우선이다.
- 보상·도감·벨루는 일러스트의 재질과 표정을 강화한다.
- 실제 아트 자산 제작은 별도 승인 전 시작하지 않는다.

## 12. 문서 권위

읽기 순서:

```text
PROJECT_CORE.md
→ DOCUMENTATION_MAP.md
→ DOCUMENT_LIFECYCLE_REGISTRY.md
→ 이 문서
→ 주제별 [현행] APPROVED 문서
```

`[대체됨]`, `[보류]`, `[폐기]` 문서는 구현 입력으로 사용하지 않는다.

## 13. 현재 미확정

- 건물 6종 T2/T3 분기·압력 카운터.
- T1/T2/T3 병종 역할·시너지·카운터.
- 전술스킬·마석 리듬.
- Stage 종료 상인 재고·가격.
- 최신 첫 10~15분 흐름.
- Hero·Legendary 재조정.
- Meta·Hub 재조정.
- Stage 정확 시간·Threat Budget·적 패키지 수치.

## 14. 다음 순서

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
→ [완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
→ [다음 3/10] 건물 6종 T2/T3 분기·카운터
→ [4/10] 병종 역할·시너지·카운터
→ [5/10] 전술스킬·마석
→ [6/10] Stage 종료 상인
→ [7/10] 첫 10~15분 흐름
→ [8/10] Hero·Legendary 재조정
→ [9/10] Meta·Hub 재조정
→ [10/10] 전체 콘텐츠 Preflight
```

## 15. 구현 경계

```text
CURRENT_PRODUCT = LEGACY_PROTOTYPE
VERTICAL_SLICE_NOT_IMPLEMENTED
PRODUCT_CODE = NOT_AUTHORIZED
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA_NOT_RUN
```