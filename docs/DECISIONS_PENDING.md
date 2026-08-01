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

### 안내자 벨루

Decision: `OMW-DEC-20260801-BELU-IDENTITY-V1`

- [x] 정본명 `벨루 / Belu`.
- [x] `율비 / Yulbi`는 역사 별칭.
- [x] 안내·경고·결과 반응만 제공하고 결정을 대신하지 않음.

### 최신 계약 Red 테스트 명세

Decision: `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1`

- [x] 최신 Red 명세.
- [x] Legacy 테스트 보존·교체·폐기 판정.
- [ ] 실제 최신 test files.
- [ ] expected Red 실행 증거.
- [ ] test package Work Order.

### Base·GitHub·Google Sheet 전수 감사

Decision: `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1`

- [x] Base·PR #116·실제 Godot·Legacy tests·CI·Sheet 25개 탭 감사.
- [x] 활성 Base v9.1과 권장 v9.3 분리.
- [x] GitHub·Sheet·PR body read-back.
- [ ] 실패 workflow를 교체할 validator package.

### Screen Board V2 텍스트 계약

Decision: `OMW-DEC-20260801-VISUAL-SCREEN-BOARD-V2`

- [x] OM-IMG-011~018 8개 독립 화면·브리프·생성 순서.
- [x] GitHub·Sheet 동기화 read-back.
- [ ] 시각자료 바이너리 이관·Index 재검증.
- [ ] OM-IMG-013·015 독립 이미지 검수.
- [ ] 파생 화면·최종 통합 보드.

### 경제·Retry·save/checkpoint 구조

Decision: `OMW-DEC-20260801-ECONOMY-RETRY-SAVE-PLANNING-V1`

- [x] MapRun 경제·Profile 경제 분리.
- [x] Act 단위 비감소 회전가 구조.
- [x] 무료 회전 금화의 canonical reference cost.
- [x] 이동 `n×P`와 실행 뒤 비가역.
- [x] 보관 병력 식량 0·배치 시 예약.
- [x] 제한된 profile 시작 보관 용량 tier·런 내 무제한 확장 금지.
- [x] Stage 5+ MapRun당 최대 1회 paid Retry.
- [x] `Stage 5~10=T1 / 11~15=T2 / 16~20=T3`, `0<T1<T2<T3`.
- [x] ProfileSave·RunCheckpoint·SettingsSave·Journal·Backup 분리.
- [x] 안정 planning 경계 checkpoint·동일 RNG lineage·원자 저장/복구.
- [x] Parameter Registry와 100K simulation 계약.
- [x] 경제·Retry·save Red 테스트 확장.
- [ ] GitHub·Sheet 동기화 read-back.
- [ ] simulator Work Order·Candidate H0/H1/H2 config.
- [ ] 100,000-seed MapRun·profile trajectory 실행.
- [ ] fault injection harness·실행.
- [ ] 사람 플레이 후보 축소와 exact value Decision.

정본:

- `docs/design/APPROVED_OMENWARD_ECONOMY_RETRY_SAVE_CHECKPOINT_PLANNING_CONTRACT_2026-08-01.md`
- `docs/design/OMENWARD_ECONOMY_RETRY_SAVE_PARAMETER_REGISTRY_V1.json`
- `docs/testing/OMENWARD_ECONOMY_META_RETRY_100K_SIMULATION_CONTRACT_2026-08-01.md`
- `docs/testing/OMENWARD_ECONOMY_RETRY_SAVE_RED_TEST_EXTENSION_2026-08-01.md`

## 2. 현재 P1 차단 항목

### 2.1 CI·validator 최신화

마지막 관찰:

```text
Validate Base v9 adoption: PASS
Validate Project Core Documentation: FAIL
Validate Omenward GDD Sheet Adoption: FAIL
```

- [ ] Project Core validator 최신 라우터·Decision·상태 반영.
- [ ] GDD test의 오래된 Base SHA·C1 proof hardcode 분리.
- [ ] Python tests·workflow Green 증거.

### 2.2 최신 Red 실행 package

- [ ] `tests/headless/latest/**`.
- [ ] `tests/python/latest/**`.
- [ ] Parameter Registry parser·unique ID Gate.
- [ ] 경제·Retry·save fault injection tests.
- [ ] compile/import 성공 뒤 계약 미구현 expected failure.
- [ ] C1/C2/C3 과거 validator archive 전환.

### 2.3 Base v9.3 원자 migration

- [ ] v9.3 release/evidence/Registry SHA 검증.
- [ ] Adapter·routes·Snapshot·Health·compatibility view 원자 갱신.
- [ ] validators·tests·protected paths·reference freshness 검증.

## 3. 구현 전 기획 P1

### 3.1 경제 exact values·시뮬레이션

구조는 승인됐다. 다음 값은 여전히 미확정이다.

- [ ] 시작 골드·식량·무료 회전.
- [ ] 기본·접전지·금고 수입.
- [ ] 회전 base·Act multiplier.
- [ ] 이동 `P`·session cap 사용 여부.
- [ ] 병력 판매가.
- [ ] 보관 기본 용량·unlock tier·비용·상한.
- [ ] 5건물 비용·시간·HP·Tier·수리·철거·환불률.
- [ ] 영구재화 이름·정산 공식.
- [ ] Retry T1/T2/T3 실제값.
- [ ] save schema 번호·checksum·backup 수·migration 범위.

과거 `160골드`, `20회전가`, `70/50/40` 등은 `LEGACY_CANDIDATE_H0 / HISTORICAL_ONLY`다.

### 3.2 화면·시각 후속

- [ ] 시각자료 바이너리 이관.
- [ ] 실제 폰트·아이콘·픽셀 크기.
- [ ] Showcase·Standard 에셋 Manifest.
- [ ] 1080p·720p 독립 이미지 가독성 검수.

### 3.3 건물·점령·전투 콘텐츠

- [ ] 타워 분기·지휘소 오라 exact 값.
- [ ] 점령 유예·회복·반경·거점 HP·앵커.
- [ ] 10병종 능력치·Tier 3 20전문화.
- [ ] 등급·AI·방어·상태이상·비행·표적 점수.

### 3.4 Stage·위험·미션

- [ ] Stage 1~20 exact 공세.
- [ ] 일반 공세 8개·위험 Stage exact values.
- [ ] 난이도 변형·미션 12장 수치·event ID.

### 3.5 메타·저장 후속

- [ ] 프로필 해금 표와 장식 범위.
- [ ] 영구 성장 사용 여부·respec 정책.
- [ ] 실제 save schema·migration 구현 계약.
- [ ] checkpoint serialization field test.
- [ ] retry transaction journal 구현 계획.

## 4. 상태 분류

```text
STRUCTURE_CURRENT != EXACT_VALUES_APPROVED
SIMULATION_CONTRACT_WRITTEN != SIMULATION_RUN
TEXT_SPEC_CURRENT != IMAGE_GENERATED
RED_SPEC_WRITTEN != RED_TESTS_CREATED
BASE_RELEASED != PROJECT_ADOPTED
CI_PARTIAL_FAILURE != VALIDATED
```

## 5. 다음 순서

```text
경제·Retry·save Sheet 동기화·read-back
→ 100K simulator Work Order·Candidate H0/H1/H2
→ 시각자료 바이너리 이관·Visual Index 재검증
→ OM-IMG-013 독립 이미지 중간 검수
→ 최신 Red test Work Order·expected-failure package
→ Base v9.3 원자 migration package
→ validator Green
→ 사용자 승인 Codex 제품 구현 Plan
```