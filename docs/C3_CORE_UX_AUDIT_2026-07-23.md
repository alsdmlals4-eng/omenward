# C3 코어 UX 6종 감사·구현 계약

- 기준 main: `2670a9a0040d0618a8dfb98683076f6b4ded5c54`
- 작업 브랜치: `agent/c3-core-ux-minimum`
- 현재 상태: `C3_AUDIT_COMPLETE / IMPLEMENTATION_PENDING`
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

## 3. 현재 구현 감사

현재 `StageHud`는 다음만 표시한다.

- 금화·식량.
- 현재 웨이브.
- 단일 `Next omen Ns` 문자열.
- 룰렛 보드·결과·보관 개수의 디버그 문자열.
- 병영·포탑·농장 건설 버튼.
- 상·중·하 배치 버튼.
- 스테이지 결과·재시도.

현재 누락:

- 건설 전후 확률 차이와 비용·효과 비교가 없다.
- 토큰의 출처·가중치·전체 확률 장부가 없다.
- 다음 공세 라인·병종·수량·단계별 공개가 없다.
- 유닛의 사거리·현재 대상·상성 힌트가 없다.
- 웨이브 성공·실패 원인을 라인별로 기록하지 않는다.
- 건물 버튼이 현재 거점 상태, 비용, 식량, 토큰 기여를 비교하지 않는다.

## 4. 구현 책임 경계

### 도메인 서비스

- `RouletteService`: 현재 토큰 장부, 심벌 확률, 가상 토큰 추가 후 확률을 계산한다.
- `BuildingService`: 비파괴 건설 가능성, 비용·식량·토큰 효과와 비교 snapshot을 제공한다.
- `WaveDirector`: 다음 공세까지 시간과 T-30/T-15/T-5 공개 단계를 제공한다.
- `BattleSimulator`: 라인별 유닛의 사거리·현재 대상·전술 태그와 사망·목표 이벤트를 제공한다.
- `StageRun`: 여섯 UX를 하나의 읽기 전용 `core_ux_snapshot()`으로 조합하고 웨이브 보고를 소유한다.

### UI

- `StageHud`는 snapshot을 표시하고 기존 입력을 전달한다.
- UI에서 확률·경제·전투 결과·추천 원인을 새로 계산하지 않는다.
- 현재 960×540 논리 화면에서 전장 가시 영역을 보존하는 텍스트 중심 PoC를 먼저 사용한다.
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
- 토큰 출처 건물 ID와 개수.

### 징조

- T-30: 위험 라인과 핵심 역할 태그.
- T-15: 라인별 병종·수량과 승인 상성 힌트.
- T-5: 가장 높은 수량의 위험 라인 강조.
- 30초 밖에서는 다음 공세까지 시간만 표시한다.

### 전투 오버레이

- 라인, 팀, 병종, 역할, 공격 사거리, 현재 대상 ID.
- 승인된 `anti_air`, `anti_large`, `backline`, `siege`, `ranged_defense` 전술 힌트.

### 웨이브 보고

- 라인별 적 처치·아군 손실.
- 거점 상태 변화 수.
- 성문 피해량.
- 실제 지표에서 선택한 짧은 원인 코드와 수치 근거.

### 건설 비교

- 비용, 식량 보너스, 룰렛 심벌·가중치, 현재 건설 가능 여부와 차단 사유.

## 7. 완료 조건

- 여섯 UX가 모두 실제 도메인 snapshot에서 생성된다.
- 빈 토큰·금화 부족·점령 중·교착·적 없는 라인·대상 없음이 안전하게 표시된다.
- 같은 상태는 같은 snapshot과 보고를 만든다.
- C1·C2 계약과 C1U 보류 상태가 유지된다.
- Godot 4.7.1 editor import, 모든 headless, runtime smoke가 통과한다.
- Ubuntu/Windows × Python 3.12/3.13 계약·문서·Skill 검증이 통과한다.
- 1920×1080·1280×720 사람 QA 전에는 `C3_REMOTE_PROVEN` 또는 `CORE_LOOP_PROVEN`으로 부르지 않는다.
