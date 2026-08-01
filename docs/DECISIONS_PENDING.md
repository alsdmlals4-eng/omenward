# 오멘워드 미확정 결정 목록

- 갱신일: `2026-08-01`
- 상태: `PENDING_ONLY / PLANNING_ONLY / PRODUCT_CODE_NOT_AUTHORIZED`
- 전체 코어: `docs/PROJECT_CORE.md`
- 권위 라우터: `docs/DOCUMENTATION_MAP.md`
- 현재 감사: `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1`
- 원칙: 체크되지 않은 값은 구현 사양으로 확정하지 않는다.

이 문서는 승인된 구조를 다시 질문하는 목록이 아니다. 구현 전에 실제 수치·세부 콘텐츠·Schema·검증으로 고정해야 할 항목만 추적한다.

## 1. 최근 해결된 결정

### 프로젝트 무결성·전장 토폴로지

Decision: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`

- [x] 사실표·충돌 원장·적대적 검토 선행.
- [x] 건설 노드 종류 1개.
- [x] 본진 6노드/진영.
- [x] 중간 거점 6곳, 거점당 3노드.
- [x] 중앙 접전지 3곳, 노드 0개.
- [x] 전체 건설 노드 30개.
- [x] 폐기 이미지·문서는 `REJECTED_EVIDENCE`로 보존.

### 안내자 벨루

Decision: `OMW-DEC-20260801-BELU-IDENTITY-V1`

- [x] 벨루와 `요정 율비 시안.png`는 동일 인물.
- [x] 정본명 `벨루 / Belu`.
- [x] `율비 / Yulbi`는 역사 별칭.
- [x] 벨루는 설명·경고·결과 반응을 제공하며 결정을 대신하지 않음.

### 최신 계약 Red 테스트 명세

Decision: `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1`

- [x] 최신 Vertical Slice Red 테스트 명세.
- [x] Legacy 테스트 `PRESERVE / PRESERVE_SEAM / SPLIT_REPLACE / RETIRE_AS_CURRENT_GATE` 판정.
- [x] 30노드·세 물리 릴·고정시간 점령·5건물·제품 Retry 테스트 책임 분리.
- [x] 미확정 수치 hardcode 금지.
- [ ] 실제 최신 test files.
- [ ] expected Red 실행 증거.
- [ ] test package 소유권·Work Order.

### Base·GitHub·Google Sheet 전수 감사

Decision: `OMW-DEC-20260801-BASE-PROJECT-SHEET-AUDIT-V1`

- [x] Base 현행 권위·Work Mode·Skill·Adapter·v9.3 release 구조 분석.
- [x] Omenward PR #116·정본·실제 Godot 파일·Legacy tests·CI 분석.
- [x] Google Sheet 25개 탭 전수 대조.
- [x] Active Context·Handoff stale 상태 정정.
- [x] 활성 프로젝트 Base는 v9.1, 권장 다음 Base는 v9.3으로 분리.
- [x] v9.3 Adapter 이관은 별도 원자 package로 결정.
- [x] 과거 PR #92/#97 exact 값은 역사 승인 계보로 보존.
- [x] Screen Board V2 텍스트 명세를 다음 시각 산출물로 결정.
- [x] Sheet 의미 drift 정정·read-back.
- [ ] PR body 최신화·read-back.
- [ ] 실패 workflow를 교체할 validator package.

검증 원본:

- `docs/audits/OMENWARD_BASE_PROJECT_SHEET_AUDIT_SYNC_VERIFICATION_2026-08-01.md`
- 검증 commit: `e46ed794bcb5e90924362464bc3abff92deb86d1`

## 2. 현재 P1 차단 항목

### 2.1 CI·validator 최신화

마지막 확인 workflow 판정:

```text
Validate Base v9 adoption: PASS
Validate Project Core Documentation: FAIL
Validate Omenward GDD Sheet Adoption: FAIL
```

- [ ] `validate_project_core_docs.py`가 최신 라우터·감사·상태를 검사하도록 갱신.
- [ ] 역사 marker를 제거하지 않되 현재 제품 통과 Gate로 오용하지 않도록 분리.
- [ ] `test_bca_visual_sheet_adoption.py`의 오래된 Base SHA hardcode 제거.
- [ ] C1 proof string 존재와 최신 Sheet 계약 검증을 분리.
- [ ] 변경 후 Python tests·workflow Green 증거.

이 package는 non-product verification change지만 현재 감사 문서와 분리된 별도 검증 작업으로 수행한다.

### 2.2 최신 Red 실행 package

- [ ] `tests/headless/latest/**`.
- [ ] `tests/python/latest/**`.
- [ ] `tools/validate_latest_vertical_slice_contracts.py`.
- [ ] compile/import 성공 뒤 계약 미구현으로 실패하는 expected Red 증거.
- [ ] 기존 C1/C2/C3 validator archive 전환.
- [ ] CI expected-failure→Green 전환 절차.

제품 구현은 이 package 전 시작하지 않는다.

### 2.3 Base v9.3 원자 migration

- [ ] latest main·PR base 재확인.
- [ ] v9.3 release/evidence/Registry SHA 검증.
- [ ] `PROJECT_BASE_ADAPTER.json` 원자 migration.
- [ ] Base routes·project routes 정합성.
- [ ] Snapshot·Health·compatibility view 전체 재생성.
- [ ] validators·tests 동시 갱신.
- [ ] protected paths diff 0.
- [ ] reference freshness·adversarial review·required checks.

과거 2026-07-31 migration plan은 현재 실행문이 아니다.

## 3. 구현 전 기획 P1

### 3.1 Screen Board V2·UX·시각

- [ ] 메인·Stage 준비·전투·정산 화면별 독립 브리프.
- [ ] 위험 Stage·패배/Retry 파생 화면 브리프.
- [ ] Screen Board V2 텍스트 명세.
- [ ] 1920×1080·1280×720 정보 예산.
- [ ] 세 물리 릴 3×3 조작·확정 UI.
- [ ] 하나의 전장·세 라인·`6/3/0=30` 표현.
- [ ] 벨루 위치·표정·등장 빈도·비모달 규칙.
- [ ] 팔레트·폰트·아이콘·Shape Language.
- [ ] 사용자 제공 시각자료 저장소 이전.
- [ ] Showcase·Standard 에셋 Manifest.

이미지 생성은 텍스트 명세·중간 구조 검수 뒤 진행한다.

### 3.2 룰렛·경제

- [ ] 유료 회전 기본 비용과 Stage 배율.
- [ ] 무료 회전의 금화 보상 기준 회전가.
- [ ] 초기 각 릴의 정확한 X·고정 토큰 구성.
- [ ] 이동 기본가격 `P`와 세션 내 `nP`.
- [ ] 병력 등급별 판매가.
- [ ] 보관함 확장 상한·비용.
- [ ] 금고 Tier별 골드/초.
- [ ] 중앙 접전지 골드/초.
- [ ] 100,000 seed 목표 기대값·허용 범위.

### 3.3 건물·수리·점령

- [ ] 5건물 건설비·시간·HP.
- [ ] Tier 비용·시간·HP 증가.
- [ ] 타워 분기·지휘소 오라 수치.
- [ ] 철거 시간·환불률.
- [ ] 수리 HPS·HP당 골드·중지·재개.
- [ ] 점령 유예시간·진행도 회복속도.
- [ ] 점령 반경·거점 HP·앵커·HoldRadius.
- [ ] 본진·중간 거점 노드 화면 배치.

과거 PR #92 환급값은 `HISTORICAL_APPROVED_SOURCE`이며 최신 exact 값으로 자동 승계하지 않는다.

### 3.4 병종·전투

- [ ] 공용 10병종 표준 능력치.
- [ ] Tier 3 20전문화.
- [ ] 등급 강화·AI 우선순위.
- [ ] 방어 공식 상한/diminishing cap.
- [ ] 상태이상·절대·처형 피해.
- [ ] 비행 충돌·고도 표현.
- [ ] 타워·유닛 통합 표적 점수.

### 3.5 Stage·위험·미션

- [ ] Stage 1~20 정확 공세.
- [ ] 일반 공세 템플릿 8개 편성.
- [ ] Stage 5·10·15·20 수량·Threat·HP·간격·Phase.
- [ ] 난이도별 적 배율·변형 풀.
- [ ] 미션 12장 목표 수치·보상.
- [ ] 불가능 후보 필터·진행도·정산 event ID.

### 3.6 패배·메타·저장

- [ ] 영구재화 명칭.
- [ ] 획득 공식·런 정산량.
- [ ] `RETRY_COST_TIER_1/2/3`.
- [ ] 영구 성장·respec·반복 clear 보상.
- [ ] save schema version.
- [ ] migration·checksum·원자 교체·backup.
- [ ] checkpoint 직렬화 필드·event ID.
- [ ] retry transaction journal.

## 4. 자동·사람 검증 전 보류

- [ ] 100,000 seed 경제·룰렛·미션·Retry 분포.
- [ ] 다중 수리 골드 압박.
- [ ] 타워·지휘소가 유닛 조합을 대체하지 않는지.
- [ ] 20 Stage checkpoint 왕복·손상 복구.
- [ ] 1080p·720p 가독성.
- [ ] 첫 플레이 건물→릴→배치→전선 인과 이해.
- [ ] 벨루가 자동 결정·입력 방해를 만들지 않는지.
- [ ] 패배·Retry 비용·복원 범위 이해.

## 5. 상태 분류

```text
RESOLVED = 사용자 승인·책임 원본·Sheet 동기화 완료
PENDING = 구현 전 결정 필요
DEFERRED = 이번 Vertical Slice 범위 밖
HISTORICAL_RECORD = 과거 결정·PR·실험
REJECTED_EVIDENCE = 폐기됐지만 실패 원인 보존
LEGACY_PROVEN = 과거 계약 실행 증거
APPROVED_STRUCTURE != EXACT_VALUES_APPROVED
RED_SPEC_WRITTEN != RED_TESTS_CREATED
BASE_RELEASED != PROJECT_ADOPTED
CI_PARTIAL_FAILURE != VALIDATED
```

## 6. 다음 순서

```text
Screen Board V2 화면별 독립 브리프·텍스트 명세
→ 경제·Retry·save/checkpoint Approval Bundle·시뮬레이션 계약
→ 최신 Red test Work Order·expected-failure package
→ Base v9.3 원자 migration package
→ validator Green
→ 사용자 승인 Codex 제품 구현 Plan
```