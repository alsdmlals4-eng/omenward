# [현행] 오멘워드 프로젝트 코어

- 공식명: **오멘워드 / OMENWARD**
- 갱신일: 2026-08-04
- 기준 저장소: `alsdmlals4-eng/omenward`
- 전체 시스템 기준선: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 현행 GDD: `docs/OMENWARD_GDD_CURRENT_CANON.md`
- 핵심 재미 정본: `docs/design/APPROVED_OMENWARD_CORE_FUN_AND_CONTENT_GUARDRAILS_2026-08-04.md`
- 문서 수명주기: `docs/DOCUMENT_LIFECYCLE_REGISTRY.md`
- 작업 모드: `PLANNING_ONLY_PROFILE`
- 제품 코드: `NOT_AUTHORIZED`
- 구현 상태: `VERTICAL_SLICE_NOT_IMPLEMENTED`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 검증: `HUMAN_QA_NOT_RUN`

이 문서는 제품 정체성·핵심 인과·플레이어 불변 조건을 소유한다. 충돌 시 **사용자 최신 지시 → 이 문서 → Documentation Map·Lifecycle Registry → 주제별 `[현행]` 책임 원본 → 실제 증거 → 구형 문서** 순서로 적용한다.

## 1. 정체성

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 미래 결과를 설계한 뒤, 룰렛에서 얻은 병력을 한 전선에 비가역 배치해 전황을 뒤집는 실시간 전략 오토배틀 게임.**

짧은 문구:

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

시장 차별화:

> **독립 슬롯에서 무작위 병력을 뽑는 게임이 아니라, 건물·TokenSource·가로 이동으로 미래 룰렛 자체를 다시 쓰고 그 결과를 세 전선에 커밋하는 게임.**

## 2. 핵심 재미 4축

```text
예고된 압력
→ 제작한 확률
→ 비가역 전선 커밋
→ 설명 가능한 결과와 다음 설계
```

1. **예측** — 다음 공세의 전선·역할·특수 행동을 읽는다.
2. **확률 설계** — 제한된 건물과 TokenSource로 미래 릴 구성을 바꾼다.
3. **결과 조작** — 멈춘 3×3 노출창에서 제한된 이동권을 사용한다.
4. **전선 커밋** — 보관·판매·한 전선 배치 중 선택한다.
5. **복기** — 승패 원인을 이해해 다음 Stage의 건물·릴·배치를 수정한다.

새 시스템은 공세 예측, 릴 설계, 결과 처리, 전선 결과, 복기 중 최소 두 축에 관찰 가능한 영향을 줘야 한다.

## 3. 핵심 루프

```text
MapRun·Stage 시작
→ 공세 예고 확인
→ 건설·업그레이드·수리와 TokenSource 구성
→ 룰렛 회전
→ 3×3 노출창의 열 상하·행 좌우 이동
→ 보상 확정
→ 보관·판매·한 전선 비가역 배치
→ 자동전투·점령·건물 운영
→ Stage 정산·결과 원인 복기
→ Stage 종료 정비·상인
→ 다음 Stage 설계
```

세 원형 릴은 3×3 노출창의 세 열을 구성한다. `세 릴`과 `3×3 보드`는 서로 다른 룰렛 시스템이 아니다.

## 4. 전장 코어

- 상·중·하 세 전선.
- 아군 본진 → 아군 중간 거점 → 중앙 접전 → 적 중간 거점 → 적 본진.
- 보이는 주 경로·우회로·공중 Route.
- 일반 병력의 자유로운 전선 횡단 없음.
- Ground·Flying·침투 역할을 시각과 Targeting 규칙으로 구분.
- 기본 공격은 같은 전선/Route의 가까운 유효 대상을 우선.
- Cross-lane 공격은 명시적 능력·건물만 허용하고 사전 표시.
- 아군 본진부터 적 본진까지 세 전선 전체 구도를 기본 화면에서 유지.
- 후방 침투·거점 함락은 경고하되 강제 카메라 이동으로 다른 전선을 숨기지 않는다.

좌표·거리식·Pathfinding·충돌·성능 구현은 Codex가 소유한다.

## 5. 룰렛 코어

- 세 개의 원형 릴.
- 3×3 노출창.
- 열 선택 후 상하 이동, 행 선택 후 좌우 이동.
- 가로 이동은 현재 결과뿐 아니라 미래 릴 구조에 지속 영향을 준다.
- 이동권은 룰렛 패널 내부에 `n/3`으로 표시.
- 럭키 무료 이동은 일반 저장 이동권과 구분.
- 중앙 판정과 동일 심벌 완성선 수로 보상 등급을 계산.
- 멈춘 결과는 immutable `SpinSnapshot`에서 계산.
- 보상은 명시적 확정 한 번에만 생성·지급.
- TokenSource 현재 구성은 설명 가능해야 하며 내부 구현 가중치는 상시 노출하지 않는다.

자산:

```text
금화 토큰 = 인게임 금화 이미지
병종 토큰 = 인게임 T1·T2 병종 이미지
T3 병종 토큰 = 금지
결과 보상 = 실제 지급 병종 이미지
```

## 6. 현행 자원

```text
현행 자원 집합 = 골드 / 마석 / 배치 병력·병력 한도 / 이동권
```

| 자원 | 역할 |
|---|---|
| 골드 | 건설·업그레이드·수리·룰렛·Stage 종료 상인 |
| 마석 | 전술스킬 |
| 배치 병력·병력 한도 | 전장 병력 규모 |
| 이동권 | 룰렛 결과와 미래 릴 편집 |

식량은 현행 핵심 HUD 자원이 아니다.

## 7. 기본 건물 6종

```text
현행 건물 집합 = 금고 / 농장 / 병영 / 방어탑 / 지휘소 / 마력탑
```

| 건물 | 현행 역할 |
|---|---|
| 금고 | 골드 운영·인게임 금화 토큰 |
| 농장 | 배치 병력·병력 한도 |
| 병영 | 병종 TokenSource·Tier 분기 |
| 방어탑 | 특정 전선 방어 |
| 지휘소 | 현재 MapRun 전체 아군 병력 오라 |
| 마력탑 | 마석 수급·보유량 지원 |

- 건물별 지속 유지비 없음.
- 토큰 초당 공급 없음.
- 지휘소를 주변 범위 오라로 해석하지 않는다.
- T2·T3 분기는 색·수치만 다른 업그레이드가 아니라 압력별 카운터와 기회비용을 가져야 한다.
- 정확한 분기·수치는 후속 콘텐츠 Decision이 소유한다.

## 8. HUD·상인·벨루

평상시 하단:

```text
[룰렛] [보관함] [건설] [전술스킬] [벨루]
```

- 주요 자원은 골드·마석·배치 병력/한도.
- 이동권은 룰렛 패널 안에서만 표시.
- 상인은 전투 중 상시 버튼이 아니라 Stage 종료 정비시간에 등장.
- 벨루는 상황·위험·선택 근거를 1~2문장으로 설명.
- 정확한 수치·지속 상태는 HUD가 소유.
- 벨루가 플레이어 대신 결정을 내리지 않는다.

## 9. Stage 콘텐츠 코어

후속 콘텐츠는 다음 압력 범주로 릴·건물·병종 선택을 시험한다.

```text
MASS / ARMORED / FLYING / INFILTRATION / SIEGE
```

- 일반 Stage는 1~2개 압력을 학습시킨다.
- Danger Stage는 기존 압력에 규칙 변형을 더한다.
- Boss Stage는 단순 HP 증가가 아니라 선택 구조를 다시 해석하게 한다.
- 정확한 Stage 매트릭스와 적 수치는 미확정이다.

## 10. 아트 코어

```text
STYLE = PIXEL_ILLUSTRATION_HYBRID
BATTLEFIELD = PIXEL_READABILITY + ILLUSTRATED_MATERIAL_AND_LIGHT
CLOSEUP_UI = ILLUSTRATION_FORWARD
ALLY = IVORY / BLUE / RESTRAINED_GOLD
VEIL = CHARCOAL / DEEP_PURPLE / CRIMSON / ASYMMETRIC_GOTHIC
```

- 전장에서는 실루엣·전선·노드 판독이 우선.
- 보상·도감·벨루에서는 일러스트의 재질과 표정을 강화.
- 생성 비교 이미지는 선택 근거·레이아웃 참고용이며 최종 자산이 아니다.
- 실제 아트 제작은 별도 승인 전 시작하지 않는다.

## 11. 문서·구현 경계

- `[현행]`만 신규 기획·구현 입력으로 사용.
- `[대체됨]`은 후속 문서가 권위 승계.
- `[보류]`는 최신 정본과 재검증 전 사용 금지.
- `[폐기]`는 사용 금지.
- `[증거]`는 과거 사실만 증명.
- `current_main`과 `context_baseline_commit`은 기본 브랜치에서 동적으로 해석.
- 문서 승인·CI·병합만으로 제품 구현을 주장하지 않는다.

```text
VERTICAL_SLICE_NOT_IMPLEMENTED
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

## 12. 다음 기획 순서

```text
Stage·Wave·Danger·Boss 압력 매트릭스
→ 건물 6종 T2/T3 분기·카운터
→ 병종 역할·시너지·카운터
→ 전술스킬·마석
→ Stage 종료 상인
→ 첫 10~15분 흐름
→ Hero·Legendary 재조정
→ Meta·Hub 재조정
```
