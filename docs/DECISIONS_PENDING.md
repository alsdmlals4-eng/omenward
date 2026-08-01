# 오멘워드 미확정 결정 목록

- 갱신일: `2026-08-01`
- 상태: `PENDING_ONLY / PLANNING_ONLY / PRODUCT_CODE_NOT_AUTHORIZED`
- 전체 코어: `docs/PROJECT_CORE.md`
- 권위 라우터: `docs/DOCUMENTATION_MAP.md`
- 원칙: 체크되지 않은 값은 구현 사양으로 확정하지 않는다.

이 문서는 승인된 구조를 다시 질문하는 목록이 아니다. 구현 전에 실제 수치·세부 콘텐츠·스키마로 고정해야 할 항목만 추적한다.

## 1. 최근 해결된 결정

### 프로젝트 무결성·전장 토폴로지

결정 ID: `OMW-DEC-20260801-PROJECT-INTEGRITY-GATE-V1`

- [x] 작업 전 사실표·충돌 원장·적대적 검토 의무화.
- [x] 건설 노드 종류 1개.
- [x] 본진 6노드/진영.
- [x] 중간 거점 `3라인 × 2진영 = 6곳`, 거점당 3노드.
- [x] 중앙 접전지 노드 0개.
- [x] 전체 건설 노드 30개.
- [x] 폐기 이미지·문서를 `REJECTED_EVIDENCE`로 보존.

### 안내자 벨루

결정 ID: `OMW-DEC-20260801-BELU-IDENTITY-V1`

- [x] 기존 문서의 벨루와 `요정 율비 시안.png`의 캐릭터는 동일 인물.
- [x] 최종 정본명은 `벨루 / Belu`.
- [x] `율비 / Yulbi`는 과거 파일명·변경 이력용 역사 별칭.
- [x] 신규 UI·대사·에셋·데이터·파일명은 `벨루 / Belu / belu` 사용.
- [x] 벨루는 설명·경고·결과 반응을 제공하며 플레이어 결정을 대신하지 않음.

### 최신 계약 테스트 게이트

결정 ID: `OMW-DEC-20260801-LATEST-CONTRACT-RED-TEST-V1`

- [x] 최신 Vertical Slice Red 테스트 명세 작성.
- [x] Legacy 테스트를 `PRESERVE / PRESERVE_SEAM / SPLIT_REPLACE / RETIRE_AS_CURRENT_GATE`로 판정.
- [x] 30노드·세 물리 릴·고정시간 점령·5건물·제품 유료 Retry 테스트 책임 분리.
- [x] 정확한 미확정 수치를 Red assertion에 임의 고정하지 않는 규칙 명시.
- [ ] 실제 최신 Red 테스트 파일 작성.
- [ ] 현재 Legacy에서 의도한 미구현 이유로 실패하는지 실행·증거 저장.
- [ ] 테스트 파일별 구현 소유권과 Codex Work Order 확정.

책임 원본:

- `docs/testing/LATEST_VERTICAL_SLICE_RED_TEST_SPEC_2026-08-01.md`
- `docs/testing/LEGACY_TEST_PRESERVE_REPLACE_RETIRE_MATRIX_2026-08-01.md`

### 기존 승인 구조

- [x] 표준 런 35분, 20 Stage, 4막.
- [x] 위험 Stage 5·10·15, 최종 위험 Stage 20.
- [x] 시스템 조합형 콘텐츠 Manifest와 12장 미션 풀.
- [x] Stage 6·11·16에서 미션 선택 또는 거절.
- [x] Stage 5 이후 MapRun당 최대 1회 영구재화 재시도.
- [x] GitHub·Sheet 동일 Decision ID 동기화.
- [x] Benchmark-First 기획 원칙.

## 2. 구현 전 P1 미확정

### 2.1 최신 계약 Red 실행 패키지

- [ ] `tests/headless/latest/**` 실제 테스트 파일.
- [ ] `tests/python/latest/**` repository boundary 테스트.
- [ ] `tools/validate_latest_vertical_slice_contracts.py`.
- [ ] 현재 Legacy에서 expected Red 실패 증거.
- [ ] compile/import/timeout이 아닌 계약 미구현 실패임을 확인.
- [ ] 기존 C1·C2·C3 validator의 archive 전환 시점.
- [ ] CI expected-failure 단계와 Green 전환 절차.

이 항목이 승인·실행되기 전 Codex 제품 구현을 시작하지 않는다.

### 2.2 화면·UX·시각

- [ ] 화면 명세 보드 V2.
- [ ] 메인·Stage 준비·전투·결과 화면별 독립 브리프.
- [ ] 1920×1080·1280×720 정보 예산과 가독성 기준.
- [ ] 세 물리 릴 3×3 보드의 조작·확정 UI.
- [ ] 하나의 전장·세 라인·`6/3/0=30` 노드 표현.
- [ ] 벨루의 화면별 위치·표정·등장 빈도·비모달 안내 규칙.
- [ ] 공용 UI 팔레트·폰트·아이콘 세트.
- [ ] 사용자 제공 최신 시각자료 바이너리 저장소 이전.
- [ ] Showcase·Standard 대표 에셋 Manifest.

### 2.3 룰렛·경제

- [ ] 유료 회전 기본 비용과 Stage 진행 배율.
- [ ] 무료 회전 금화 보상 기준 회전가.
- [ ] 초기 각 릴의 정확한 X·고정 토큰 구성.
- [ ] 이동 기본가격 `P`와 세션 내 `nP` 실제값.
- [ ] 병력 등급별 판매가.
- [ ] 보관함 영구 확장 상한과 비용.
- [ ] 금고 Tier별 골드/초.
- [ ] 중앙 접전지 골드/초 최종값.
- [ ] 100,000 seed 목표 기대값과 허용 범위.

### 2.4 건물·수리·점령

- [ ] 5건물 기본 건설비·건설시간·HP.
- [ ] Tier 업그레이드 비용·시간·HP 증가.
- [ ] 타워 분기와 지휘소 오라 정확한 수치.
- [ ] 철거 시간과 환불률.
- [ ] 수리 HPS·HP당 골드·중지·재개 규칙.
- [ ] 접전지·중간 거점 점령 유예시간과 진행도 회복속도.
- [ ] 점령 반경·거점 HP·진격 앵커·HoldRadius.
- [ ] 본진·중간 거점 노드의 정확한 화면 배치.

### 2.5 병종·전투

- [ ] 10병종 표준 능력치.
- [ ] Tier 3 20전문화 상세 능력.
- [ ] 등급별 강화와 AI 우선순위.
- [ ] 방어 공식 상한 또는 diminishing cap.
- [ ] 상태이상·절대 피해·처형 피해 분류.
- [ ] 비행 충돌·고도 표현 규칙.
- [ ] 타워와 유닛 표적 점수 통합.

### 2.6 Stage·위험·미션

- [ ] 20 Stage별 정확한 공세 조합.
- [ ] 일반 공세 템플릿 8개 실제 편성.
- [ ] Stage 5·10·15·20 정확한 수량·Threat·HP·행동 간격·페이즈.
- [ ] 난이도별 적 능력 배율과 변형 풀.
- [ ] 미션 12장의 막별 목표 수치와 보상량.
- [ ] 불가능 후보 필터와 진행도·정산 사건 ID.

### 2.7 패배·메타·저장

- [ ] 영구재화 공식 명칭.
- [ ] 영구재화 획득 공식과 런 정산량.
- [ ] `RETRY_COST_TIER_1/2/3` 실제값.
- [ ] 영구 성장 노드·respec·반복 clear 보상 범위.
- [ ] save schema version.
- [ ] migration·checksum·원자 교체·백업 정책.
- [ ] checkpoint 직렬화 필드와 사건 ID.
- [ ] retry transaction journal 형식.

## 3. 자동·사람 검증 전 보류

- [ ] 100,000 seed 경제·룰렛·미션·Retry 비용 분포.
- [ ] 다중 건물 수리의 골드 압박.
- [ ] 타워·지휘소가 유닛 조합을 대체하지 않는지.
- [ ] 20 Stage checkpoint 왕복과 저장 손상 복구.
- [ ] 1080p·720p 화면 가독성.
- [ ] 첫 플레이 건물→릴→배치→전선 인과 이해.
- [ ] 벨루 안내가 자동 결정·입력 방해를 만들지 않는지.
- [ ] 패배·Retry 비용·복원 범위 이해.

## 4. 상태 분류 규칙

```text
RESOLVED = 사용자 승인과 책임 원본·Sheet 동기화 완료
PENDING = 구현 전 반드시 결정해야 함
DEFERRED = 이번 Vertical Slice 범위 밖의 명시적 보류
HISTORICAL_RECORD = 과거 결정·PR·실험 기록
REJECTED_EVIDENCE = 폐기됐지만 실패 원인 보존
LEGACY_PROVEN = 과거 계약 실행 증거, 최신 구현 증거 아님
RED_SPEC_WRITTEN != RED_TESTS_CREATED
RED_TESTS_CREATED != EXPECTED_FAILURE_VERIFIED
EXPECTED_FAILURE_VERIFIED != PRODUCT_IMPLEMENTED
```

## 5. 다음 순서

```text
Base 전체 현행 스킬·작업 구조 분석
→ 프로젝트 GitHub·Google Sheet 전수 진행도 감사
→ 적대적 검토와 남은 기획 보완
→ 같은 Decision ID로 정본·Sheet 동기화
→ 화면 명세 보드 V2
→ 실제 최신 Red 테스트 작성·실행 계획
→ 사용자 승인 Codex 구현 Plan
```
