# 오멘워드 V2 검수 완료·v6 기획 전환 보고

- 전환일: 2026-07-27
- 적용 계약: `VERTICAL_SLICE_MASTER_REFERENCE v6`
- 제품 단계: `PROTOTYPE_AND_VERTICAL_SLICE`
- 완료 Work Mode: `REVIEW`
- 다음 Work Mode: `PLAN`
- 다음 실행 프로필: `PLANNING_ONLY_PROFILE`
- 제품 구현: `V2_IMPLEMENTATION_NOT_STARTED`
- 제품 코드 승인: `NO`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 코어 잠금: `CORE_LOCK_V2_PENDING`

## 1. 사용자 최신 지시 해석

사용자는 PR #93과 F-30 후속 작업을 진행하도록 승인하고, 이후 작업은 v6 기준으로 기획을 계속한다고 지시했다.

따라서 상태를 다음처럼 분리한다.

```text
REVIEW_PHASE: COMPLETE
F-30: RESOLVED_AND_CANONICAL
FINAL_CODEX_HANDOFF: DEFERRED_BY_USER_FOR_V6_PLANNING
CODEX_BUILD: NOT_AUTHORIZED
NEXT_WORK_MODE: PLAN
NEXT_EXECUTION_PROFILE: PLANNING_ONLY_PROFILE
```

이 전환은 `검수 완료`를 제품 구현 승인으로 해석하지 않는다. 다음 작업은 기획·벤치마킹·시스템 설계·Vertical Slice 계약·Codex Goal 준비이며, 실제 Godot Build는 별도 사용자 승인 전 금지한다.

## 2. 완료된 검수 범위

- R1+R2 범위와 Legacy C1 보존 seam.
- transient `RefCounted` V2 도메인.
- caller-injected token instance ID.
- snapshot copy-out 불변성.
- stopped-only `RouletteSpinSession`.
- 벤치마크 UX의 R1+R2 범위 분리.
- 거래 기반 순서 `R3 → U1-F → S1-F → R4 → U1-C → S1-C`.
- 전술계획 건물 작업 통합 계약.
- F-30 건설 진행 후 수리 정산 순서.

## 3. 현재 보호 대상

- 플레이어 약속: 건물로 미래 룰렛을 설계하고 결과를 세 전선에 비가역 커밋한다.
- 일반 유닛 라인 횡단 금지.
- 기본 난이도의 치명적 공세 정보 공개.
- 중앙 가로줄 선행 판정과 기존 C1 결과.
- immutable `SpinSnapshot`.
- 가로 이동의 token instance·출처 영구 편집.
- 배치 후 회수·라인 변경·판매 금지.
- 공용 병종 데이터와 진영 Visual 분리.
- UI의 규칙 계산 비소유.
- Godot 4.7.1 Standard / GDScript / Compatibility renderer.

## 4. 다음 v6 기획 범위

다음 작업은 기능 구현이 아니라 Stage 2 전체를 외부 플레이 가능한 통합 데모로 수렴시키는 기획이다.

우선순위:

1. `CORE_POC`에서 가장 위험한 플레이 가설과 관찰 기준 재정의.
2. R1+R2 이후 패키지의 플레이어 가치·의존성·제외 범위 재배열.
3. 버티컬 슬라이스 대표 3스테이지 흐름과 데모 종료점 확정.
4. 설계 청사진·전선 대응 브리핑·전투 인과 사슬의 UX 역할 설계.
5. 마스코트·상징 동반자의 세계관·UI·세일즈 역할 설계.
6. 에셋·UI·사운드 조달 순서와 라이선스 검증 계획.
7. 10~15분 사람 플레이, 1080p·720p 가독성, 성능·저장·복귀 증거 계획.
8. Codex 구현 패키지는 승인된 기획 결과에서만 작성.

## 5. 현재 차단과 미검증

```text
BLOCKED_UNVERIFIED:
- V2 Godot 실행 경로
- live physical reel 연결
- R1+R2 자동 계약과 원격 실행 증거
- CORE_POC 사람 플레이
- 10~15분 Slice 흐름
- 1080p·720p 가독성
- 성능·저장·복귀
- 마스코트 실제 적용과 기억도
```

위 항목은 기획 문서 존재만으로 통과 처리하지 않는다.

## 6. Requirement Coverage

| 요구·결정 | 상태 | 근거 | 다음 조치 |
|---|---|---|---|
| F-30 순서 확정 | `COVERED` | PR #93, F-30 검수, 승인 정본 | 구현 패키지 Red 테스트로 전달 |
| 검수 완료 상태 동기화 | `COVERED_IN_THIS_PR` | 이 전환 보고와 Context 문서 | 문서 CI·병합 확인 |
| 이후 v6 기준 기획 | `READY` | 사용자 최신 지시 | 다음 PLAN 작업 계약 작성 |
| 제품 코드 구현 | `NOT_AUTHORIZED` | 사용자 최신 지시·프로젝트 게이트 | 별도 Build 승인 필요 |

## 7. Skill Coverage

| 책임 | Skill·Mode | 상태 | 증거 |
|---|---|---|---|
| intake·작업 계약 | `managing-project-intake-and-work-contract: route/contract` 상당 절차 | `FALLBACK_USED` | 단계·프로필·범위 분리 |
| REVIEW Finding 처리 | `running-adversarial-review-and-refinement` 상당 절차 | `FALLBACK_USED` | F-30 기술 판정·범위 보호 |
| 정본 최신성 | `auditing-canonical-reference-freshness` 상당 절차 | `FALLBACK_USED` | F-30 승인 정본·Context·Map 동기화 |
| GitHub 통합 | GitHub PR 검증·squash merge | `EXECUTED_AND_EVIDENCED` | PR #93 / merge `8b0d8aac...` |
| 완료 전 검증 | Superpowers `verification-before-completion` | `IN_PROGRESS_UNTIL_PR_CI` | diff·문서 CI·PR 상태 확인 예정 |

Base 공용 Skill 본문을 실제 도구로 실행하지 않은 항목은 `FALLBACK_USED`로 기록한다.

## 8. Artifact Coverage

| 산출물 | 상태 | 책임 |
|---|---|---|
| F-30 기술 검수 | `MERGED` | `docs/reviews/2026-07-27-v2-construction-repair-same-timestamp-order-review.md` |
| F-30 승인 정본 | `CREATED_IN_THIS_PR` | `docs/design/APPROVED_V2_CONSTRUCTION_REPAIR_SAME_TIMESTAMP_ORDER_2026-07-27.md` |
| 검수 완료·v6 전환 | `CREATED_IN_THIS_PR` | 이 문서 |
| Documentation Map | `UPDATED_IN_THIS_PR` | 현재 라우팅 |
| Active Context | `UPDATED_IN_THIS_PR` | 현재 상태 캡슐 |
| Handoff Context | `UPDATED_IN_THIS_PR` | 다음 작업자 인계 |
| Codex 최종 인계 | `DEFERRED` | 다음 v6 기획 완료 뒤 별도 승인 |

## 9. Base 승격 후보와 프로젝트 전용

### Base 승격 후보

- 파일 쓰기 전에 대상 브랜치 존재를 강제 검증하는 GitHub 안전 게이트.
- 기본 브랜치 직접 쓰기를 connector 차원에서 차단하는 규칙.
- REVIEW 완료와 Build 승인을 별도 상태로 유지하는 전환 템플릿.

### 프로젝트 전용 유지

- F-30 처리 순서.
- R1+R2 경계와 후속 패키지 순서.
- 오멘워드 룰렛·건물·전선·수리 계약.

## 10. 다음 시작점

다음 요청에서는 v6 Context Pack을 먼저 갱신하고, `CORE_POC → Vertical Slice` 사이에서 가장 위험한 플레이어 경험 가설 하나를 첫 결과 단위로 선택한다.

```text
NEXT_ACTION: V6_PLANNING_INTAKE
NEXT_WORK_MODE: PLAN
NEXT_EXECUTION_PROFILE: PLANNING_ONLY_PROFILE
PRODUCT_CODE_AUTHORIZED: NO
```
