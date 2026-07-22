# 프로젝트 코어·정본 복구 감사 — 2026-07-22

## 1. 목적

현재 저장소의 승인 기획, 상태 문서, 실제 코드, 데이터, 테스트와 열린 Issue·PR을 대조해 프로젝트 단계 오판을 제거한다.

이번 작업은 문서 책임과 검증 계약만 바꾼다. 게임 코드·Scene·Resource·게임 데이터·승인 수치·시각자료는 변경하지 않는다.

## 2. 기준점

- Omenward `main`: `69c571c5a49502f9da57e1c8d8eba04455380c0f`
- Skill 최적화 PR #47: Draft·미병합
- 조사일: 2026-07-22

PR #47의 프로젝트 코어·적대적 검토 Skill은 분석 방법으로 참고했지만, 이번 브랜치는 #47의 코드에 의존하지 않고 현재 `main`에서 생성한다.

## 3. 발견한 정본 충돌

| 위치 | 기존 주장 | 실제 증거 | 조치 |
|---|---|---|---|
| `README.md` | 플레이 가능한 수직 슬라이스 구현 완료 | 기술·데이터 구성요소는 있으나 룰렛·전투 목적·코어 UX가 미완결 | `CORE_VERTICAL_SLICE_PARTIAL`로 교정 |
| `OMENWARD_GAME_DESIGN.md` | Phase 0 대기·구현 전 | Godot 프로젝트·Scene·GDScript·Resource·테스트 존재 | 기술 기준선 구현과 코어 미완결을 분리 |
| `OMENWARD_ROADMAP.md` | Phase 0 Plan Mode 대기 | P1 기반과 P2 일부가 이미 구현 | 현재 복구 단계 중심으로 재작성 |
| `DECISIONS_PENDING.md` | 엔진·화면·상태 소유를 최초 승인 대기 | 실제 project·GameSession·Resource 구조 존재 | 구현 사실과 재검증 필요를 분리 |
| 열린 Issue 다수 | 구현 금지·과거 브랜치 정본 | 현재 main과 상태가 다름 | 본 PR에서 문서 정본을 먼저 복구하고 후속 Issue 정리 대상으로 기록 |
| 기존 테스트 | 9개 룰렛 카드 반환을 성공 계약으로 간주 | 승인 룰렛은 중앙 줄·완성선·등급·단일 보상 | 다음 단계의 P0 계약 복구 항목으로 지정 |

## 4. 채택한 상태 모델

```text
TECHNICAL_BASELINE_IMPLEMENTED
+ CORE_VERTICAL_SLICE_PARTIAL
+ CORE_LOOP_NOT_PROVEN
+ HUMAN_QA_NOT_RUN
```

이 네 상태를 동시에 사용한다. 어느 하나만 사용하면 다음 오판이 생긴다.

- `구현 전`만 사용: 이미 존재하는 기술 기반과 파일을 다시 설계한다.
- `수직 슬라이스 완료`만 사용: 승인 룰렛·전투 목적·UX 미완성을 놓친다.
- `테스트 통과`만 사용: placeholder 테스트를 제품 계약 검증으로 오인한다.
- `플레이 가능`만 사용: 사람 플레이·가독성·재미 검증을 완료로 오인한다.

## 5. 프로젝트 코어 스트레스 테스트

### 공격 1 — 룰렛 없이도 같은 게임인가

아니다. 룰렛을 제거하면 제한 노드 기반 3라인 디펜스가 된다.

### 공격 2 — 건물이 확률을 바꾸지 않아도 되는가

아니다. 건설과 룰렛이 분리돼 장르 혼합의 인과가 사라진다.

### 공격 3 — 공세 정보를 숨기면 더 전략적인가

아니다. 대응 자원 부족이 아니라 정보 부족으로 난이도를 만들면 RNG 좌절이 커진다.

### 공격 4 — 배치를 자동화해도 되는가

아니다. 당첨 결과를 어느 전선에 커밋할지가 플레이어의 마지막 전술 책임이다.

### 공격 5 — 전체 10병종과 W1~W20이 지금 필요한가

아니다. 대표 병종 3~5개와 짧은 공세 묶음으로 코어를 먼저 검증할 수 있다.

## 6. Critique–Refine 결과

초기 비판:

- 상태 문서만 갱신하면 다시 드리프트할 수 있다.
- 새 코어 문서가 기존 GDD를 중복할 수 있다.
- 파일 존재를 구현 완료로 오인할 수 있다.
- 코어 문구를 사용자 승인 없이 잠글 수 있다.

개선:

- `PROJECT_CORE.md`는 기능 상세가 아니라 분류·불변·제거 테스트·게이트만 소유한다.
- `CURRENT_IMPLEMENTATION_STATUS.md`는 실제 증거와 미검증 경계만 소유한다.
- 기존 GDD는 전체 설계, APPROVED 문서는 세부 규칙을 계속 소유한다.
- 문서 Validator가 stale 상태 문구와 필수 참조 누락을 차단한다.
- 코어 상태는 `EXISTING_CORE_IDENTIFIED`로 기록하고 잠금은 사용자 확인을 기다린다.

## 7. 변경 범위

추가:

- `docs/PROJECT_CORE.md`
- `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- `docs/CORE_RECOVERY_AUDIT_2026-07-22.md`
- `tools/validate_project_core_docs.py`
- `tests/python/test_project_core_docs.py`
- `.github/workflows/validate-project-core-docs.yml`

동기화:

- `README.md`
- `docs/ACTIVE_CONTEXT.md`
- `docs/HANDOFF_CONTEXT.md`
- `docs/DOCUMENTATION_MAP.md`
- `docs/OMENWARD_GAME_DESIGN.md`
- `docs/OMENWARD_ROADMAP.md`
- `docs/DECISIONS_PENDING.md`

## 8. 후속 순서

1. 이 문서 전용 Draft PR 검토.
2. 사용자가 프로젝트 코어 문구 잠금 여부를 확인.
3. 승인 룰렛 계약 복구를 별도 Plan·Build·Review PR로 수행.
4. 전투 목적 루프, 코어 UX, 사람 플레이 순으로 분리 진행.

## 9. 판정

- 정본 충돌: `FOUND`
- 코어 식별: `COMPLETE`
- 코어 잠금: `PENDING_USER_CONFIRMATION`
- 게임 기능 변경: `NONE`
- Godot 실행 검증: `NOT_RUN`
- 사람 플레이 검증: `NOT_RUN`


## 10. PR diff 적대적 재검토에서 발견한 P0

초기 자동 변환의 Roadmap 단계 표 정규식이 `re.S`와 결합돼 과거 G1~P6 상세 절 약 300줄을 함께 제거했다. 자동 Validator는 필수 현재 상태 문구만 검사해 이 손실을 잡지 못했다.

조치:

- 최신 `main`의 Roadmap과 Decisions를 Git에서 직접 복원.
- 현재 상태가 소유하는 1절·3절·15절만 경계 기반으로 교체.
- G1~P6의 목적·불변·종료 기준을 그대로 보존.
- Phase 0의 renderer·해상도·AutoLoad·데이터 경계·fallback 대안을 현재 Decisions에 재분류해 보존.
- Roadmap 상세 절·고유 문구·최소 길이와 Decisions 고유 대안·중복 제목을 검사하는 회귀 계약 추가.

판정: `P0_FOUND_AND_REPAIRED_BEFORE_MERGE`.
