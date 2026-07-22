# C1 승인 룰렛 계약 복구 보고서

- 기준 main: `ef9e66e3bc5be7711c36123e6c6d7fe8ec8dc9a2`
- 작업 상태: `IMPLEMENTED_CANDIDATE / REMOTE_VALIDATION_PENDING`
- 프로젝트 코어: `CORE_CONFIRMED / CORE_LOCKED`

## 1. 적용 Skill

- `foundation.project-intake` — 범위·보호 대상·검증·롤백 계약.
- `foundation.project-core` — 예측→확률 설계→전선 커밋 인과 보호.
- `foundation.pruning` — 구형 Work Order·Goal·Proposal의 활성 참조 차단과 Git 이력 보존.
- `discipline.game-design` — 중앙 판정·완성선·등급·보상 C1 경계.
- `discipline.engineering` — Godot 상태 소유·결정론·최소 데이터 변경.
- `discipline.qa` — 정상·실패·경계·결정론·저장·배치 테스트.
- `foundation.adversarial-review` — 9카드 placeholder·구형 참조·문서 상충 공격.
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
- 결과 보관 중 다음 회전만 차단.
- 같은 시드·건물 스냅샷 재현 로그.

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

## 6. 검증 경계

영구 CI가 다음을 실행한다.

- Ubuntu/Windows × Python 3.12/3.13 정적 계약.
- Godot 4.7.1 editor import.
- 모든 `tests/headless/*_test.gd`.
- runtime smoke.
- 프로젝트 코어·Skill Validator와 whitespace.

사람 플레이·시각 QA·100,000시드 분포는 이번 자동 C1 계약과 별도다.
