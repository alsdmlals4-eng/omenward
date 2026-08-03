# OMENWARD HUD·룰렛 배치·전장 시야 교정 승인안

```yaml
amendment_id: OMW-AMEND-20260804-HUD-ROULETTE-LAYOUT-AND-BATTLEFIELD-VIEW-V1
parent_decisions:
  - OMW-DEC-20260804-PLANNING-BATTLEFIELD-VISUAL-HIERARCHY-AND-CAMERA-V1
  - OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1
approval: USER_DIRECT_APPROVAL
status: USER_APPROVED_PLANNING_CANON / NOT_IMPLEMENTED
work_mode: PLANNING_ONLY
product_code_authority: NONE
image_generation: STOPPED_BY_USER
```

## 1. 교정 목적

이 문서는 사용자 검수로 확인된 인게임 HUD·룰렛 배치와 전장 시야 교정을 소유한다. 기존 Decision 8·9의 내용 중 아래와 충돌하는 화면 배치는 이 문서가 우선한다.

## 2. 평상시 전장 시야

- 기본 카메라는 기존 시안보다 더 멀리서 본다.
- 전장은 화면의 약 82~85%를 사용한다.
- 평상시 하단 기능 바는 약 15~18%를 사용한다.
- 아군 본진부터 적 본진까지, 상·중·하 세 전선과 주요 거점·건설 노드를 한 화면에서 읽을 수 있어야 한다.
- 룰렛·건설 작업 패널을 열 때만 하단 패널이 일시적으로 확장된다.
- 작업 패널을 닫으면 넓은 기본 전장 시야로 복귀한다.

## 3. 건설 노드 시각 언어

건설 노드는 장식보다 상태 판독을 우선한다.

- 빈 노드: 밝은 원형 석판과 중앙 건설 문양.
- 설치 가능: 금색 외곽선과 약한 맥동.
- 선택: 예상 건물 실루엣과 설치 범위.
- 사용 중: 건물 바닥 문양으로 전환.
- 설치 불가: 잠금 또는 금지 아이콘.
- 점령권 상실: 적 문양과 오염된 외곽선.
- 색상만으로 상태를 구분하지 않고 형태·아이콘·맥동을 함께 사용한다.

## 4. 룰렛 보드와 이동 화살표

룰렛 조작 중심은 하나의 3×3 노출 보드다.

```text
      ▲     ▲     ▲

◀  [토큰] [토큰] [토큰]  ▶
◀  [토큰] [토큰] [토큰]  ▶
◀  [토큰] [토큰] [토큰]  ▶

      ▼     ▼     ▼
```

- 위·아래 화살표는 각 세로 릴을 직접 가리킨다.
- 왼쪽·오른쪽 화살표는 각 가로 행을 직접 가리킨다.
- 플레이어는 화살표 위치만 보고 어느 릴 또는 행이 어느 방향으로 이동하는지 알 수 있어야 한다.
- 선택된 릴·행만 강조하며 이동 후 위치를 반투명 미리보기로 보여준다.
- 세로 이동은 해당 릴만 회전한다.
- 가로 이동은 해당 행의 세 토큰을 순환 이동한다.

## 5. 룰렛 정보 공개 범위

플레이어에게 다음 정보는 보여준다.

- 현재 3×3 토큰.
- 선택한 릴의 숨은 위·아래 인접 토큰.
- 보관 이동권 `n/3`.
- 럭키 무료 이동 횟수.
- 병종 Tier 설명.
- 동일 심벌 완성선에 따른 보상 등급.
- 이동 전후 미리보기.

다음 내부 정보는 기본 룰렛 화면에서 숨긴다.

- TokenSource 출처 건물 목록.
- Source ID와 내부 가중치.
- `NORMAL_X`, `SOURCE_BOUND_X` 같은 내부 상태명.
- 전술스킬 목록과 마석 소비 UI.

건물 카드에는 플레이어용 효과만 간단히 설명한다. 예: `궁병 계열 토큰을 룰렛에 추가합니다.`

## 6. 룰렛 돌리기와 결과 확정의 배치

최종 화면 순서는 다음과 같다.

```text
3×3 룰렛 보드와 이동 화살표
→ [룰렛 돌리기]
→ 결과 판정·보상 미리보기
→ [결과 확정]
```

### 룰렛 돌리기

- 3×3 보드 바로 아래 중앙에 배치한다.
- `결과 확정` 영역보다 위에 둔다.
- 현재 live 릴 구성으로 SpinSession을 시작한다.
- 회전 비용과 실행 가능 여부를 버튼 주변에 명확히 표시한다.
- SpinSession이 열려 있거나 미처리 PendingReward가 있으면 비활성화한다.

### 결과 확정

- 기존 위치보다 아래로 내린다.
- 룰렛 정지와 판정이 끝난 뒤에만 활성화한다.
- 확정 시 immutable PendingReward를 생성한다.
- `룰렛 돌리기`와 같은 시각적 위계로 두지 않는다. 회전은 시작 행동, 확정은 결과 수령 행동으로 구분한다.

## 7. 하단 기능 바

평상시 순서는 유지한다.

```text
[룰렛] [보관함] [건설] [전술스킬] [벨루]
```

- 벨루는 우측 하단 초상과 짧은 말풍선으로 전황을 설명한다.
- 룰렛 작업대 안에는 전술스킬을 중복 노출하지 않는다.
- 상점 버튼은 없으며 상인은 Stage 종료 정비시간에만 방문한다.

## 8. 적대적 검토

| ID | 위험 | 대응 |
|---|---|---|
| OMW-AUD-331 | 회전 버튼이 없어 이동과 확정만으로 흐름이 끊김 | 3×3 보드 아래 중앙에 `룰렛 돌리기` 배치 |
| OMW-AUD-332 | 회전과 결과 확정이 같은 행동처럼 보임 | 확정 영역을 아래로 내리고 단계·시각 위계 분리 |
| OMW-AUD-333 | 화살표가 조작 대상과 떨어져 방향을 오해함 | 각 열 상·하, 각 행 좌·우에 직접 배치 |
| OMW-AUD-334 | TokenSource 내부 정보가 룰렛 핵심 판단을 압박함 | 출처·ID·가중치 기본 숨김 |
| OMW-AUD-335 | 룰렛 안에 전술스킬이 중복 노출됨 | 전술스킬은 평상시 독립 버튼에서만 제공 |
| OMW-AUD-336 | 하단 패널이 전장과 노드를 과도하게 가림 | 평상시 전장 82~85%, 하단 바 15~18% 목표 |
| OMW-AUD-337 | 건설 노드가 배경 장식처럼 보여 설치 상태를 읽지 못함 | 형태·아이콘·외곽선·맥동을 결합한 상태 언어 |

## 9. 상태 경계

```text
PLANNING_CANON = APPROVED_AMENDMENT
PRODUCT_CODE = UNCHANGED
ROULETTE_SPIN_BUTTON = BELOW_BOARD_ABOVE_CONFIRM
RESULT_CONFIRM = LOWER_SECTION
TOKEN_SOURCE_DETAILS = HIDDEN_FROM_DEFAULT_ROULETTE_UI
TACTICAL_SKILL_PANEL_IN_ROULETTE = HIDDEN
BATTLEFIELD_SHARE = ABOUT_82_TO_85_PERCENT
BOTTOM_BAR_SHARE = ABOUT_15_TO_18_PERCENT
IMAGE_GENERATION = STOPPED_BY_USER
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```
