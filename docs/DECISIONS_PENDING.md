# 오멘워드 미확정 결정 목록

- 갱신일: `2026-08-01`
- 상태: `PENDING_ONLY / PLANNING_ONLY / PRODUCT_CODE_NOT_AUTHORIZED`
- 전체 코어: `docs/PROJECT_CORE.md`
- 권위 라우터: `docs/DOCUMENTATION_MAP.md`
- 원칙: 체크되지 않은 값은 구현 사양으로 확정하지 않는다.

## 1. 최근 해결된 결정

### 프로젝트 무결성·전장 토폴로지

Decision: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`

- [x] 사실표·충돌 원장·적대적 검토.
- [x] 본진 6노드/진영·중간 거점 6곳×3·접전지 0·전체 30노드.
- [x] 폐기 이미지·문서 `REJECTED_EVIDENCE` 보존.

### 안내자 벨루

Decision: `OMW-DEC-20260801-BELU-IDENTITY-V1`

- [x] 정본명 `벨루 / Belu`.
- [x] `율비 / Yulbi`는 역사 별칭.
- [x] 안내·경고·결과 반응을 제공하되 결정을 대신하지 않음.

### 최신 계약 Red 테스트 명세

Decision: `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1`

- [x] 최신 Vertical Slice Red 테스트 명세.
- [x] Legacy 테스트 보존·분리·교체·현행 Gate 폐기 판정.
- [ ] 실제 최신 test files.
- [ ] expected Red 실행 증거.
- [ ] test package Work Order.

### Base·GitHub·Google Sheet 전수 감사

Decision: `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1`

- [x] Base 구조·PR #116·실제 Godot·Legacy tests·CI·Sheet 25개 탭 감사.
- [x] 활성 Base v9.1과 권장 v9.3 분리.
- [x] v9.3은 별도 원자 migration package로 결정.
- [x] Sheet·PR body read-back.
- [ ] 실패 workflow를 교체할 validator package.

### Screen Board V2 텍스트 계약

Decision: `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2`

- [x] 필수 메인·전투·자원관리·결과 화면 포함.
- [x] 건설·세 물리 릴·보스·제품 Retry 추가.
- [x] OM-IMG-011~018 8개 독립 화면 확정.
- [x] 8개 독립 브리프 작성.
- [x] 공통 전장·릴·벨루·UI·금지 요소 계약.
- [x] 독립 이미지 생성 순서 `013 → 015 → 012 → 014 → 016 → 017 → 018 → 011`.
- [ ] GitHub·Sheet 동기화 read-back.
- [ ] 사용자 제공 시각자료 바이너리 저장소 이관.
- [ ] Visual Reference Index 이관 후 재검증.
- [ ] OM-IMG-013 독립 이미지 생성·중간 검수.
- [ ] OM-IMG-015 독립 이미지 생성·중간 검수.
- [ ] 파생 화면과 최종 8패널 통합 보드.

화면 정본:

- `docs/design/APPROVED_OMENWARD_VISUAL_SCREEN_BOARD_V2_TEXT_SPEC_2026-08-01.md`
- `docs/design/screen-briefs/OMENWARD_SCREEN_BRIEF_OM_IMG_011...018_2026-08-01.md`

## 2. 현재 P1 차단 항목

### 2.1 CI·validator 최신화

마지막 관찰:

```text
Validate Base v9 adoption: PASS
Validate Project Core Documentation: FAIL
Validate Omenward GDD Sheet Adoption: FAIL
```

- [ ] Project Core validator 최신 라우터·감사·상태 반영.
- [ ] GDD test의 오래된 Base SHA·C1 proof hardcode 분리.
- [ ] Python tests·workflow Green 증거.

### 2.2 최신 Red 실행 package

- [ ] `tests/headless/latest/**`.
- [ ] `tests/python/latest/**`.
- [ ] 최신 validator.
- [ ] compile/import 성공 뒤 계약 미구현 expected failure.
- [ ] C1/C2/C3 과거 validator archive 전환.

### 2.3 Base v9.3 원자 migration

- [ ] v9.3 release/evidence/Registry SHA 검증.
- [ ] Adapter·routes·Snapshot·Health·compatibility view 원자 갱신.
- [ ] validators·tests·protected paths·reference freshness 검증.

## 3. 구현 전 기획 P1

### 3.1 화면·UX·시각 후속

완료:

- [x] 메인·준비·릴·자원관리·전투·보스·정산·Retry 브리프.
- [x] 1920×1080 기준과 1280×720 후속 검수 요구.
- [x] 세 물리 릴·3×3·30노드·비가역 배치 표현 계약.
- [x] 벨루 비모달·비자동결정 규칙.
- [x] 공통 팔레트·Shape Language·금지 RPG 표현.

남음:

- [ ] 시각자료 바이너리 이관.
- [ ] 실제 폰트·아이콘·픽셀 크기.
- [ ] Showcase·Standard 에셋 Manifest.
- [ ] 독립 이미지와 축소 가독성 검수.

### 3.2 룰렛·경제

- [ ] 회전 비용·Stage 배율.
- [ ] 무료 회전 금화 기준.
- [ ] 초기 릴 구성.
- [ ] 이동 기본가격 `P`와 `nP`.
- [ ] 판매가·보관 확장·금고·접전지 수입.
- [ ] 100,000 seed 목표 기대값.

### 3.3 건물·수리·점령

- [ ] 5건물 건설비·시간·HP·Tier.
- [ ] 타워 분기·지휘소 오라.
- [ ] 철거·수리 수치.
- [ ] 점령 유예·회복·반경·거점 HP·앵커.
- [ ] 정확한 노드 화면 배치.

과거 PR #92 값은 `HISTORICAL_APPROVED_SOURCE`이며 최신 값으로 자동 승계하지 않는다.

### 3.4 병종·전투

- [ ] 10병종 능력치·Tier 3 20전문화.
- [ ] 등급·AI·방어·상태이상·비행·표적 점수.

### 3.5 Stage·위험·미션

- [ ] Stage 1~20 exact 공세.
- [ ] 일반 공세 8개·위험 Stage exact values.
- [ ] 난이도 변형·미션 12장 수치·event ID.

### 3.6 패배·메타·저장

- [ ] 영구재화 명칭·획득·정산.
- [ ] `RETRY_COST_TIER_1/2/3`.
- [ ] 영구 성장·respec.
- [ ] save schema·migration·checksum·backup.
- [ ] checkpoint·retry transaction journal.

## 4. 자동·사람 검증 전 보류

- [ ] 100,000 seed 분포.
- [ ] 20 Stage checkpoint 왕복·손상 복구.
- [ ] 1080p·720p 화면 가독성.
- [ ] 첫 플레이 건물→릴→배치→전선 인과 이해.
- [ ] 벨루 안내·Retry 이해.

## 5. 상태 분류

```text
TEXT_SPEC_CURRENT != IMAGE_GENERATED
IMAGE_GENERATED != APPROVED_ASSET
APPROVED_STRUCTURE != EXACT_VALUES_APPROVED
RED_SPEC_WRITTEN != RED_TESTS_CREATED
BASE_RELEASED != PROJECT_ADOPTED
CI_PARTIAL_FAILURE != VALIDATED
```

## 6. 다음 순서

```text
Screen Board V2 Sheet 동기화·read-back
→ 경제·Retry·save/checkpoint Approval Bundle·시뮬레이션 계약
→ 시각자료 바이너리 이관·Visual Index 재검증
→ OM-IMG-013 독립 이미지 중간 검수
→ 최신 Red test Work Order·expected-failure package
→ Base v9.3 원자 migration package
→ validator Green
→ 사용자 승인 Codex 제품 구현 Plan
```