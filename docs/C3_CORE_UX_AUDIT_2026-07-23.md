# C3 코어 UX 6종 감사·구현 계약

- 기준 main: `2670a9a0040d0618a8dfb98683076f6b4ded5c54`
- 작업 브랜치: `agent/c3-core-ux-minimum`
- 현재 상태: `C3_IMPLEMENTED / REMOTE_VALIDATION_PENDING / HUMAN_QA_PENDING`
- 선행 완료: `C1_ROULETTE_CORE_REMOTE_PROVEN`, `C2_BATTLE_OBJECTIVE_REMOTE_PROVEN`
- 별도 사용자 결정: `C1U_PENDING_USER_DECISION`

## 1. 적용 Skill

- `foundation.project-intake` — C3 범위, 보호 대상, 완료 증거 고정.
- `foundation.project-core` — 예측→확률 설계→전선 커밋의 정보 인과 보호.
- `foundation.pruning` — C2 완료 뒤 구형 다음 작업·후보 상태 참조 제거.
- `discipline.game-design` — 여섯 정보가 실제 선택을 바꾸는지 검토.
- `discipline.engineering` — UI 계산 금지, 도메인 snapshot 책임 분리.
- `discipline.qa` — 정상·부족·중립·교착·빈 데이터·결정론 회귀.
- `foundation.adversarial-review` — 허위 확률·허위 원인·stale snapshot·C1U 혼입 공격.
- `foundation.validation-review`, `discipline.integration-review` — 코드·Scene·문서·검증 일치.

## 2. 승인된 C3 범위

1. 건설 전 룰렛 확률 미리보기.
2. 현재 룰렛 토큰 장부.
3. T-30/T-15/T-5 베일의 징조.
4. 상성·사거리·현재 타기팅 오버레이.
5. 웨이브 종료 후 라인별 원인 보고.
6. 건설 선택 비교 UI.

승인 책임 원본:

- `docs/design/APPROVED_UI_ART_AUDIO_POC_BIBLE_V1.md`
- `docs/design/APPROVED_BELLU_SINGLE_GUIDE_AND_FIRST_10_MINUTE_FLOW.md`
- `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
- `docs/design/APPROVED_BATTLEFIELD_TOPOLOGY_AND_SCALE_V1.md`
- `docs/design/APPROVED_COMMON_COMBAT_AND_RANK_BUDGET_POC_V1.md`
- `docs/design/APPROVED_STAGE_ECONOMY_AND_BUILDING_COST_BASELINE_V1.md`

## 3. 구현 결과

### 도메인 snapshot

- `RouletteService`가 현재 X·금화·활성 건물 심벌의 가중치, 확률, 출처 건물 ID와 보상 병종을 계산한다.
- 건설 전 미리보기는 실제 `BuildingDefinition`을 가상 `Array[Dictionary]` 출처로 추가해 건설 전후 확률과 변화량을 계산한다.
- `WaveDirector`가 다음 공세까지 시간과 `countdown / t30 / t15 / t5 / now / complete` 공개 단계를 소유한다.
- 공용 `UnitArchetypeProfile`과 `UnitInstance`가 역할, 실제 공격 사거리, 현재 대상 ID, 승인 상성·타기팅 힌트를 양 진영에 동일하게 제공한다.
- `CoreUxService`가 웨이브 출격 유닛과 실제 사망·거점·성문·본진 이벤트를 추적해 라인별 원인 보고를 만든다.
- `StageRun.core_ux_snapshot()`이 여섯 UX를 읽기 전용 snapshot 하나로 조합한다.

### HUD

- `StageHud`는 snapshot을 표시하고 기존 입력만 전달한다.
- 토큰 장부는 심벌·가중치·확률·출처 수·출처 건물 ID·보상 병종을 표시한다.
- 건설 비교는 비용·식량·룰렛 기여·건설 가능 여부·차단 사유를 표시하고 버튼 상태에 반영한다.
- 징조는 T-30 역할, T-15 병종·상성 힌트, T-5 위험 라인을 단계적으로 표시한다.
- 전술 오버레이는 라인·팀·병종·사거리·현재 대상·상성·타기팅 우선 태그를 표시한다.
- 웨이브 보고는 적 처치·아군 손실·거점 변화·성문/본진 피해의 가한 값과 받은 값을 구분한다.
- 현재 960×540 논리 화면의 텍스트 중심 PoC이며 최종 시각 배치가 아니다.

## 4. 구현 책임 경계

### 도메인 서비스

- `RouletteService`: 현재 토큰 장부, 심벌 확률, 가상 토큰 추가 후 확률을 계산한다.
- `BuildingService`: 실제 건물 정의, 현재 경제와 거점 상태를 제공한다.
- `WaveDirector`: 다음 공세까지 시간과 T-30/T-15/T-5 공개 단계를 제공한다.
- `BattleSimulator`: 라인별 유닛의 실제 사거리·현재 대상과 사망·목표 이벤트 원본을 제공한다.
- `CoreUxService`: 여섯 UX snapshot과 웨이브 원인 보고를 구성한다.
- `StageRun`: 서비스 수명주기와 읽기 전용 `core_ux_snapshot()` 진입점을 소유한다.

### UI

- `StageHud`는 snapshot을 표시하고 기존 입력을 전달한다.
- UI에서 확률·경제·전투 결과·추천 원인을 새로 계산하지 않는다.
- 최종 아트·애니메이션·색상은 별도 사람 QA 전 확정하지 않는다.

## 5. 데이터 원칙

- 확률은 현재 룰렛 가중치에서 직접 계산하며 반올림 전 원본 값을 보존한다.
- 상성 힌트는 승인된 역할·대공·대형·후열·공성 관계만 사용한다.
- 웨이브 원인 보고는 실제 전투 이벤트만 집계하며 추측 원인을 만들지 않는다.
- 건물 비교는 실제 `BuildingDefinition`, 현재 경제와 거점 상태를 사용한다.
- C1U 이동권 지급량·럭키 방식·보관함 3칸·고정 상위 템플릿은 구현하지 않는다.

## 6. 최소 표시 계약

### 확률·토큰

- X·금화·각 활성 건물 심벌의 가중치와 확률.
- 선택 건물 건설 전/후 해당 심벌 확률 변화.
- 토큰 출처 건물 ID와 개수, 보상 병종.

### 징조

- T-30: 위험 라인과 핵심 역할 태그.
- T-15: 라인별 병종·수량과 승인 상성 힌트.
- T-5: 가장 높은 수량의 위험 라인 강조.
- 30초 밖에서는 다음 공세까지 시간만 표시한다.

### 전투 오버레이

- 라인, 팀, 병종, 역할, 공격 사거리, 현재 대상 ID.
- 승인된 `anti_air`, `anti_large`, `backline`, `siege`, `ranged_defense` 전술 힌트와 타기팅 우선 태그.

### 웨이브 보고

- 라인별 적 처치·아군 손실.
- 거점 상태 변화 수.
- 성문·본진 피해의 가한 값과 받은 값.
- 실제 지표에서 선택한 짧은 원인 코드와 수치 근거.

### 건설 비교

- 비용, 식량 보너스, 룰렛 심벌·가중치, 현재 건설 가능 여부와 차단 사유.

## 7. 자동 회귀 계약

- 핵심 스크립트가 직접 headless 실행에서도 인스턴스화되는지 먼저 검사한다.
- 초기 빈 토큰, 건설 후 출처, 금화 부족, 점령·교착 중 건설 차단을 검사한다.
- T-30/T-15/T-5 공개 단계와 같은 상태의 snapshot 결정론을 검사한다.
- 실제 사거리·현재 대상·상성·타기팅 우선 힌트와 대상 없음 상태를 검사한다.
- 미완료 웨이브는 보고를 만들지 않고, 완료 웨이브는 실제 처치 라인과 원인 코드를 기록하는지 검사한다.
- 영구 CI는 각 Godot headless 파일에 60초 상한을 두고 임시 C3 수리·진단 파일의 재유입을 거부한다.

## 8. 남은 검증과 상태 승격 조건

- 최신 영구 `Validate Core Contracts`에서 Godot 4.7.1 editor import, 모든 headless, runtime smoke를 통과해야 한다.
- Ubuntu/Windows × Python 3.12/3.13에서 C1·C2·C3 계약, mutation tests, 프로젝트 코어·Skill·whitespace를 통과해야 한다.
- 원격 자동 검증 완료 뒤 상태는 `C3_AUTOMATED_CONTRACTS_PROVEN / HUMAN_QA_PENDING`으로 승격한다.
- 1920×1080·1280×720 사람 가독성 QA 전에는 `CORE_LOOP_PROVEN` 또는 `CORE_VERTICAL_SLICE_COMPLETE`를 사용하지 않는다.
- 사람 QA 전에는 최종 HUD 배치·폰트·팔레트·정보 밀도를 확정하지 않는다.
