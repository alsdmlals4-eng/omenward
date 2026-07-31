# 오멘워드 시각자료 인덱스

- 갱신일: `2026-08-01`
- 상태: `CURRENT_VISUAL_REFERENCE_ROUTER / MIGRATION_GAPS_DECLARED`
- 책임 범위: 사용자 제공 이미지, 탐색 시안, 생성 실패물의 상태·용도·금지 해석
- 선행 게이트: `docs/operations/PROJECT_UNDERSTANDING_AND_OMISSION_PREVENTION_GATE_2026-08-01.md`
- 안내자 계약: `docs/design/APPROVED_BELU_GUIDE_IDENTITY_AND_NAMING_CONTRACT_2026-08-01.md`

이미지 파일만 보고 승인 범위를 추정하지 않는다. 각 항목의 `참고할 것`, `참고하지 않을 것`, `현재 상태`를 함께 읽는다.

## 1. 우선순위

```text
최신 사용자 지시
→ CURRENT_USER_CONFIRMED_DIRECTION
→ APPROVED_DIRECTION_REFERENCE
→ 관련 APPROVED 기획서
→ PARTIAL_REFERENCE
→ EXPLORATION
→ REJECTED_EVIDENCE / SUPERSEDED / ARCHIVE_SOURCE
```

시각자료 안의 수치·문구·맵 연결·노드 배치가 책임 기획서와 다르면 기획서가 우선한다.

## 2. 기존 핵심 이미지

### VR-001 — 전장 UI·병종 월드 스프라이트 형식

- 상태: `APPROVED_DIRECTION_REFERENCE / MIGRATION_PENDING`
- 원본: 2026-07-16 대화 사용자 제공 이미지
- 목표 경로: `docs/images/planning/canonical/omenward_battlefield_ui_and_unit_style_reference_v1.webp`

참고할 것:

- 실제 전장에 삽입되는 소형 고해상도 픽셀 월드 스프라이트
- 무기·자세·몸통 덩어리와 진영색에 의한 병종 식별
- 2.5~3등신 전술 미니어처 비율
- 공용 병종 계약과 진영별 Visual Set 분리

참고하지 않을 것:

- 임시 전장 토폴로지·노드 배치·수치·문구
- 미니맵처럼 보이는 전장 요약

### VR-002 — 10병종 × 등급 전개 도감표

- 상태: `SUPERSEDED_FOR_SPRITE_FORMAT / PARTIAL_REFERENCE / MIGRATION_PENDING`
- 원본: 2026-07-16 대화 사용자 제공 이미지

참고할 것:

- 방패·대검·암살·창·궁·기병·사제·마법·비행·거인 10병종 구분
- 등급 상승에 따른 제한적 실루엣 강화

참고하지 않을 것:

- 큰 전신 비율을 실제 전장 스프라이트로 사용
- 도감표 장식과 개별 디자인을 그대로 복제

## 3. 2026-07-31~08-01 사용자 제공 최신 시각자료

현재 대화 첨부 원본은 저장소에 아직 배치되지 않았다. 바이너리 경로가 생기기 전 저장 완료로 보고하지 않는다.

### VR-003 — 아군 공용 10병종·성장 표현 시안

- 상태: `CURRENT_USER_CONFIRMED_DIRECTION / PARTIAL_REFERENCE / MIGRATION_PENDING`

참고할 것:

- 10병종 역할 실루엣
- 백색·청색·금색의 아군 진영 언어
- 작은 전장 크기에서 무기·자세로 역할을 구분하는 방향

참고하지 않을 것:

- 모든 등급·장식을 제품 애니메이션 수량으로 확정
- 개별 캐릭터를 수집형 영웅으로 해석
- 큰 도감형 전신 비율을 전장에 그대로 사용

### VR-004 — 베일 진영 건축 시안

- 상태: `CURRENT_USER_PROVIDED / PARTIAL_REFERENCE / MIGRATION_PENDING`

참고할 것:

- 비대칭 갑각·가시·붉은 내부 발광·검보라 막 구조
- 아군의 정돈된 백색 구조와 실루엣 대비

참고하지 않을 것:

- 모든 건물을 별도 시스템·건물 종류로 추가
- 건물 수량·기능·노드 배치를 확정 데이터로 사용

### VR-005 — 밝은 3전선 전투·병종 구성 시안

- 상태: `CURRENT_USER_CONFIRMED_DIRECTION / APPROVED_DIRECTION_REFERENCE / MIGRATION_PENDING`

참고할 것:

- 밝은 회화·수채화 계열 전장과 소형 전술 유닛
- 백색·청색·금색 아군 영역과 검보라·적색 베일 영역의 대비
- 하나의 전장 안에서 상·중·하 세 전선을 동시에 읽는 방향

참고하지 않을 것:

- 임시 노드·거점·본진 수량을 제품 토폴로지로 복사
- HUD 없는 콘셉트를 실제 구현 화면으로 표시
- 스킬 카드·영웅 파티 UI를 임의 추가

### VR-006 — 초광각 3전선 전장 배경 시안

- 상태: `CURRENT_USER_PROVIDED / PARTIAL_REFERENCE / MIGRATION_PENDING`

참고할 것:

- 한 전장의 좌우 진영 대비
- 세 라인의 환경·전진 방향과 막별 변화 가능성

참고하지 않을 것:

- 16:9 제품 화면에 그대로 축소
- 이미지의 접전지·노드 위치를 정본으로 사용
- 중앙 접전지에 건설 노드를 추가

정확한 토폴로지:

```text
본진 6노드/진영
중간 거점 3라인×2진영, 거점당 3노드
중앙 접전지 3곳, 노드 0
건설 노드 종류 1개
전체 30노드
```

### VR-007 — 안내자 벨루 시안

- 상태: `CURRENT_USER_CONFIRMED_DIRECTION / BELU_CANON / PARTIAL_REFERENCE / MIGRATION_PENDING`
- 정본 캐릭터명: `벨루 / Belu`
- 과거 첨부 파일명: `요정 율비 시안.png`
- 과거 별칭: `율비 / Yulbi`
- 관계: `SAME_CHARACTER / HISTORICAL_ALIAS_ONLY`

참고할 것:

- 백색·하늘색·금색의 소형 요정 안내자 형태
- 위험 경고·결과 반응·짧은 비모달 안내에 사용할 수 있는 표정 구조
- 아군 진영의 밝은 시각 언어와의 일치

참고하지 않을 것:

- `율비`를 신규 UI·대사·에셋·데이터·파일명에 사용
- 안내자가 플레이어 대신 전술 결정을 수행하도록 표현
- 시안의 정확한 픽셀 크기·프레임 수·의상·색상값을 제품 사양으로 확정

현재 상태:

```text
BELU_YULBI_RELATION: RESOLVED_SAME_CHARACTER
CANONICAL_GUIDE_NAME: BELU
HISTORICAL_ALIAS: YULBI
GUIDE_VISUAL_DIRECTION: USER_CONFIRMED_PARTIAL_REFERENCE
PRODUCT_ASSET_APPROVAL: NOT_RUN
```

## 4. 생성 실패·폐기 자료

### VR-008 — 2026-07-31~08-01 인게임 화면 보드 생성 실패 묶음

- 상태: `REJECTED_EVIDENCE / DO_NOT_REUSE / CONVERSATION_ONLY`
- 개별 제품 자산 ID: `NONE`

폐기 사유:

- 일반 다크 판타지 RPG·수집형 영웅·장비 인벤토리로 변질
- 룰렛을 독립 원형 판 3개 또는 독립 9칸처럼 표현
- 하나의 전장·세 라인·양측 중간 거점 구조를 오해
- 건설 노드 종류·수량·위치와 접전지 0노드 누락
- 잘못된 화면 보드 V1의 어두운 UI 추론 반복

절대 재사용하지 않을 것:

- UI 프레임, 캐릭터, 영웅 파티, 장비 인벤토리, 룰렛·전선·노드 배치

보존 목적:

- 실패 원인과 적대적 검토 회귀 사례
- `REJECTED_EVIDENCE != NOT_CREATED` 규칙 검증

## 5. 기존 누락 자료 감사

| 자료 | 분류 | 현재 처리 |
|---|---|---|
| `스타일 후보 6안 비교표.png` | 아트 스타일 비교 | `MIGRATION_PENDING` |
| `image-gen-1.png`, `image-gen-3.png`, `image-gen-4.png`, `image-gen-5.png` | 스테이지·환경 탐색 | `MIGRATION_PENDING / PARTIAL_REFERENCE` |
| `어두운 전투의 전술 지도.png` | UI 탐색 | `MIGRATION_PENDING / PARTIAL_REFERENCE` |
| `중세 판타지 전장의 전투 중.png` | 전장 배치 탐색 | `MIGRATION_PENDING / PARTIAL_REFERENCE` |
| `전략적 전투의 시작.png` | 전장·하단 UI 탐색 | `MIGRATION_PENDING / PARTIAL_REFERENCE` |
| `오멘워드 유닛 도감.png` | 과거 병종 도감 | `VR-002 계열 / 형식 폐기` |
| `battle_map_tool.html` | 전장 설계 도구 | `MIGRATION_PENDING` |
| `전장_맵_툴_사용법.txt` | 도구 사용법 | `MIGRATION_PENDING` |
| `룰렛바운드_게임기획서_v0.7.docx` | Legacy GDD | `ARCHIVE_SOURCE` |

## 6. 시각자료 유입 규칙

1. 저장 가능한 원본 또는 변환본의 목표 경로를 정한다.
2. ID·날짜·상태·출처·경로를 기록한다.
3. `참고할 것`, `참고하지 않을 것`, `현재 기획과 달라진 것`을 기록한다.
4. 관련 APPROVED 계약·Work Order·Image ID에 연결한다.
5. 교체 자료는 `SUPERSEDED`, 폐기 자료는 `REJECTED_EVIDENCE`로 낮춘다.
6. 바이너리 이동 전에는 `MIGRATION_PENDING`을 유지한다.
7. 생성 실패도 오류·사용자 판정과 함께 기록한다.
8. 캐릭터 이름이 변경되면 현재 정본명과 역사 별칭을 분리한다.

## 7. 이미지 작업 전 검수 질문

- 최신 사용자 제공 이미지가 모두 등록됐는가.
- 참고·금지 범위를 설명할 수 있는가.
- 전장 노드가 `6/3/0`, 전체 30, 단일 건설 노드로 표현되는가.
- 룰렛이 세 물리 릴의 3×3 정지 보드로 표현되는가.
- 하나의 전장과 세 라인이 동시에 읽히는가.
- 폐기 이미지를 다시 사용하지 않는가.
- 안내자 명칭이 `벨루 / Belu / belu`로 통일됐는가.
- `율비`는 과거 파일명·변경 이력에서만 역사 별칭으로 남는가.

하나라도 답할 수 없으면 이미지 생성과 화면 정본 승격을 중단한다.
