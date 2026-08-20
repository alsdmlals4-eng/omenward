# [REFERENCE ONLY] OMENWARD · 사용자 시안 6종 Intake

```yaml
reference_id: OMW-VIS-REF-20260820-USER-MOCKUPS-01
status: REFERENCE_ONLY_NOT_CANON
received_at: 2026-08-20
user_statement: 이미지 시안은 예시이며 아직 확정이 아님
image_generation_authority: NONE
visual_canon_change: NONE
binary_persistence_to_repo: NOT_DONE
notion_binary_attachment: NOT_DONE
```

이 문서는 사용자가 대화에 제공한 시안 6종에서 **재사용 가능한 시각 원리와 충돌 위험만 추출**한다. 이미지 자체는 승인 정본 자산이 아니며, 최종 스타일/레이아웃/캐릭터/건물/색상/텍스트를 확정하지 않는다.

## 1. 입력 파일

| 파일 | 크기 | 관찰 범위 |
|---|---:|---|
| `ChatGPT Image 2026년 8월 4일 오전 08_08_16.png` | 1536×1024 | 3전선 전장 + 대형 하단 룰렛/보관/건설/전술 HUD + 벨루 |
| `생성된 이미지 1 (1)(4).png` | 1672×941 | 아군 SD 병종/진화 단계 시트 |
| `생성된 이미지 1 (2)(2).png` | 1254×1254 | Veil 측 건물/시설 콘셉트 시트 |
| `생성된 이미지 2(2).png` | 1921×819 | UI 없는 3전선 전장 구조 |
| `92fa25e2-c1a9-41d2-9b16-a4eaa40c1fc2(1).png` | 1672×941 | 3전선 + 룰렛/보상/병종 Tier/벨루 gameplay mockup |
| `519adac8-7e8f-42bf-91f6-d65d9bf194b0.png` | 1448×1086 | 수채화 SD / 고급 일러스트 SD / 픽셀 SD / 픽셀+일러스트 하이브리드 비교 보드 |

## 2. 강하게 재사용 가치가 있는 구조

### A. 3전선 공간 문법

두 전장 시안은 다음을 매우 빠르게 읽게 한다.

```text
아군 수호성 = 왼쪽
적/Veil 권역 = 오른쪽
상단 / 중단 / 하단 전선 = 화면 안에서 동시에 유지
중간 거점 / 접전 원형 노드 = 길 위 landmark
```

이 공간 문법은 현재 승인된 `FULL_BATTLEFIELD = 세 라인 전체`, `MINIMAP = NONE`, 세 전선 비가역 커밋과 잘 맞는다.

재사용 후보:

- 좌→우 전선 진행 방향.
- 전선별 큰 원형 접전/결정 지점.
- 양 진영 건축 팔레트의 강한 좌우 대비.
- 한 화면에서 3개 전선을 모두 추적 가능한 카메라.

미확정:

- 실제 맵 지형, 길 곡률, 노드 수, 성채 규모, 전선 사이 연결 방식.

### B. 진영 컬러 대비

아군:

```text
ivory / white stone
blue / navy
restrained gold
clean light / water / sky accents
```

Veil 측:

```text
dark violet
blackened metal / chitin-like silhouette
muted crimson / magenta glow
asymmetric spikes / cracks
```

장점:

- 전략 줌에서도 소유 진영 판독이 빠르다.
- 공용 10병종 combat archetype + faction visual set 구조와 잘 맞는다.

가드레일:

- Veil을 `보라색 악마 종족 하나`로 고정하지 않는다.
- 적 건물은 색만 바꾼 아군 건물 복제도, 전부 같은 가시 실루엣도 피한다.
- `Veil = 세계 현상`, 실제 적 세력/병단은 확장 가능하다는 Decision 7을 보존한다.

### C. SD 병종 silhouette와 Tier 진화

아군 병종 시트는 방패/대검/암살/창/궁/기병/사제/마법/비행/거대 체급을 장비 silhouette로 분리한다.

재사용 후보:

- 2.5~3등신 miniature/chibi proportion.
- Tier가 올라가도 무기와 핵심 silhouette를 보존.
- 흰색/청색/금색을 계층적으로 추가해 성장감을 표현.
- 역할 판독이 얼굴 디테일보다 먼저 오게 함.

주의:

- 현재 시트는 painterly watercolor/illustration에 가깝고 최신 사용자 요구인 `전체적으로 도트+픽셀 느낌`을 충족하지 않는다.
- 최종 sprite 제작에서는 low-resolution silhouette test가 별도로 필요하다.

### D. Dark navy + restrained gold UI frame

두 gameplay mockup의 짙은 navy/black panel과 얇은 gold trim은 세계관과 잘 맞는다.

재사용 후보:

- 패널 기본색 dark navy/charcoal.
- 금색은 frame/primary emphasis에 제한.
- 선택 상태에는 blue/omen glow를 사용.

주의:

- 현재 시안의 장식 테두리·작은 문자·동시 패널 수는 960×540 internal target에서 과밀해질 수 있다.
- 최종 UI는 Decision 6/10의 Focus Mode와 Question-first hierarchy를 우선한다.

## 3. 현재 정본과 충돌하거나 재설계가 필요한 부분

### 룰렛 표현

두 gameplay mockup은 중심 하단에 **정사각 3×3 grid + 행/열 이동 화살표**를 크게 둔다.

현재 승인 정본은:

```text
THREE_CIRCULAR_OMEN_WHEELS = one central triple mobilization device
3 reels = one 3×3 exposure window
THREE_REELS_TO_THREE_LANES_FIXED_MAPPING = FORBIDDEN
```

따라서 grid의 `3×3 노출/선택 읽기`는 참고 가능하지만 최종 시각은 **세 개의 징조륜/동원 장치가 어떻게 3×3 결과를 만든다고 읽히는지** 다시 설계해야 한다.

또한 `획득 보상`, 상자, 강한 희귀도 카드 표현이 전면에 나오면 룰렛이 military probability engine보다 gacha/reward machine으로 보일 위험이 있다.

### 화면 밀도

현재 mockup은 지도 + 자원 + Stage + 정비시간 + 배속 + 룰렛 + 이동권 + Tier 설명 + 보상 + 벨루 + 메뉴를 한 화면에 동시에 노출한다.

최종 정본은:

```text
PREPARE / COMMIT / BATTLE / REVIEW focus hierarchy
one primary question per mode
raw/debug data hidden
```

이므로 **패널의 미술 방향은 참고하되 동시 노출 구조는 그대로 채택하지 않는다.**

### 벨루 / guide character

밝은 청색 요정 SD는 friendly guidance와 아군 palette를 잘 연결한다.

다만:

- 최종 캐릭터 디자인은 미승인.
- player choice를 대신하는 assistant가 되면 안 됨.
- `정답 빌드 추천`보다 상태 설명/FTUE/세계관 안내 역할이 적합.
- 전체 pixel direction이 확정되면 초상화도 pixel/hybrid 처리 여부를 다시 정한다.

## 4. 스타일 비교 보드 disposition

비교 보드 자체는 1번 `동화풍 수채화 SD`를 권장으로 표시하지만, **사용자는 이 보드와 6개 시안 전체가 예시이며 미확정이라고 명시했고, 별도로 전체적인 도트+픽셀 감각을 요구했다.**

따라서 보드의 추천 라벨은 current canon이 아니다.

현재 재평가 후보:

```text
A = PIXEL_ILLUSTRATION_HYBRID
B = FULL_TACTICAL_PIXEL
C = WATERCOLOR_ILLUSTRATION_WITH_PIXEL_UI_ACCENTS
```

초기 판단:

- A는 기존 고급 fantasy depth와 최신 pixel/dot 요구를 함께 살릴 가능성이 가장 높음.
- B는 가독성/일관성은 강하지만 기존 성채·환경의 화려한 판타지 깊이를 많이 포기할 수 있음.
- C는 기존 시안을 가장 적게 바꾸지만 최신 pixel/dot 요구를 약하게 반영할 위험이 큼.

**아직 선택하지 않는다.** 후속 Visual Reference Reconciliation Decision에서 최소 3개 안으로 비교하고 사용자 승인을 받는다.

## 5. 현 시점 Visual 상태

```text
USER_REFERENCE_FILES_RECEIVED = TRUE
REFERENCE_COUNT = 6
REFERENCE_STATUS = REFERENCE_ONLY_NOT_CANON
FIRST_GENERATED_CANDIDATE = REJECTED_NOT_CANON
VISUAL_DIRECTION_FINAL = NOT_SELECTED
IMAGE_GENERATION = PAUSED_UNTIL_VISUAL_DIRECTION_REAPPROVAL
```

실제 이미지 generation/editing은 새 visual synthesis가 승인되기 전 재개하지 않는다.
