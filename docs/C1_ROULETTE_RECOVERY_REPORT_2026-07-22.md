# C1 승인 룰렛 계약 복구 보고서

- 기준 main: `ef9e66e3bc5be7711c36123e6c6d7fe8ec8dc9a2`
- 작업 상태: `C1_ROULETTE_CORE_REMOTE_PROVEN`
- 프로젝트 코어: `CORE_CONFIRMED / CORE_LOCKED`

## 1. 적용 Skill

- `foundation.project-intake` — 범위·보호 대상·검증·롤백 계약.
- `foundation.project-core` — 예측→확률 설계→전선 커밋 인과 보호.
- `foundation.pruning` — 구형 Work Order·Goal·Proposal의 활성 참조 차단과 Git 이력 보존.
- `discipline.game-design` — 중앙 판정·완성선·등급·보상 C1 경계.
- `discipline.engineering` — Godot 상태 소유·결정론·최소 데이터 변경.
- `discipline.qa` — 정상·실패·경계·결정론·저장·배치 테스트.
- `foundation.adversarial-review` — 9카드 placeholder·구형 참조·문서 상충·테스트 허위 성공 공격.
- `foundation.validation-review`, `discipline.integration-review` — 실제 diff·CI·정본 동기화.

## 2. 감사

기계 감사 입력에서 텍스트 242개, 룰렛 관련 105개, 구형 상태·명칭 후보 39개와 내부 Markdown 참조를 조사했다. 깨진 내부 링크는 수집 시점 0개였다.

확인된 핵심 결함:

1. 룰렛 서비스가 보드 9칸을 곧바로 9개 유닛 카드로 반환했다.
2. placeholder 테스트가 잘못된 API를 회귀 계약으로 고정했다.
3. 농장·포탑이 유닛 토큰을 만들고 기본 병영이 없었다.
4. 보상 저장이 HUD 로컬 배열에 있어 StageRun 책임이 아니었다.
5. GDD·통합 인덱스·문서 라우터가 Phase 0 이전 파일과 상태를 활성 기준으로 노출했다.

## 3. C1 구현

```text
3×3 결정론적 보드
→ 중앙 가로줄 선행 판정
→ 같은 판정 심벌의 8개 완성선 계산
→ common / elite / hero / legendary
→ 출처 병영 결정
→ 1개 유닛 보상 또는 금화 지급
→ StageRun 보관
→ 라인 배치
```

- X·금화·기본 병영 전사 토큰 가중치 적용.
- 금화 75%/200%/500% 지급.
- 전설 스테이지 1회와 이후 영웅 2기 변환.
- 농장·포탑의 유닛 토큰 제거.
- 병영 40금화·전사 토큰 추가.
- 결과 보관 중 다음 회전만 차단하고 금화를 소비하지 않음.
- 보상 없는 결과는 저장 성공으로 기록하지 않음.
- 보관 유닛 배치 시 식량 비용을 정확히 예약.
- 같은 시드·건물 스냅샷·복수 출처가 같은 결과를 재현.

## 4. 의도적으로 보류

- 이동권 심벌의 완성선 지급량.
- 상충하는 럭키 규칙의 최종 해석.
- 계열별 고정 엘리트·영웅·전설 템플릿 ID.
- 100,000시드 확률·경제 분포 판정.

상위 등급 템플릿은 현재 공용 데이터에 확정 ID가 없어 `source_archetype_rank_fallback`으로 명시한다. 이는 숨은 최종 결정이 아니다.

## 5. 구형 참조 처리

- 과거 Work Order·Goal·Proposal은 활성 읽기·라우팅에서 제거한다.
- 고유 역사와 승인 근거는 Git 이력에 보존한다.
- 공식 명칭 교체표와 금지 예시는 구형 명칭을 설명하는 정본이므로 유지한다.
- mutation fixture의 구형 문자열은 Validator 공격 입력이므로 유지한다.
- 임시 감사 payload·실행 스크립트·진단 Workflow·진단 로그는 최종 트리에서 제거한다.

## 6. 회귀 실패 원인과 수정

적대적 보강 뒤 `stage_run_test.gd`에서 두 단계 문제가 드러났다.

1. `Variant` 경유 경제 값을 `:=`로 추론해 Godot 4.7.1 정적 타입 파싱이 실패했다.
2. `pending_roulette_rewards.front()`의 반환값을 암시적으로 추론해 경고-오류 정책에서 `StageRun` 파싱이 실패했다.
3. 기존 분리 테스트는 스크립트 로드 오류가 발생해도 `load()` 결과 객체만 보고 진행해 허위 성공 가능성이 있었다.

수정:

- 경제 스냅샷을 명시적 `int`로 변환.
- 대기 보상을 명시적 `UnitSpawnDefinition`으로 캐스팅하고 null을 방어.
- 테스트가 `Script.can_instantiate()`까지 검사한 뒤에만 인스턴스 테스트를 실행.
- 임시 분리 진단 Workflow와 로그는 원인 확인 후 삭제.

## 7. 최종 원격 검증 결과

- 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`
- GitHub Actions run: `29926598807`
- Godot: `4.7.1-stable`

통과:

- Ubuntu/Windows × Python 3.12/3.13 계약 검증 `4/4 SUCCESS`.
- C1 Validator·구형 활성 참조·깨진 링크 검사.
- 전체 Python 저장소 테스트.
- 프로젝트 코어·Skill Validator·compile·whitespace.
- Godot editor import.
- 모든 `tests/headless/*_test.gd`.
- runtime smoke.
- 강화된 보관 차단·금화 불변·식량 예약·복수 출처 결정론 회귀.

판정:

```text
C1_ROULETTE_CORE_REMOTE_PROVEN
+ C1U_PENDING_DECISIONS
+ CORE_LOOP_NOT_PROVEN
+ HUMAN_QA_NOT_RUN
```

사람 플레이·1920×1080/1280×720 시각 QA·100,000시드 분포는 이번 자동 C1 핵심 계약과 별도다.
