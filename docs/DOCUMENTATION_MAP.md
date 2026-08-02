# 오멘워드 Documentation Map

```yaml
updated_at: 2026-08-02
work_mode: TOTAL_PLANNING
current_phase: CANON_RECOVERY_AND_ADVERSARIAL_PLANNING
current_recovery_decision: OMW-DEC-20260802-CANON-RECOVERY-V1
baseline_main: 9a39f6869f95ec4e6e1f6b96a6a2f896a22c5739
active_base: 9.4.0_RELEASED
current_product: LEGACY_PROTOTYPE
latest_planning: APPROVED_NOT_IMPLEMENTED
product_code_authority: NONE
superseded_pr: 116
```

이 문서는 질문별 현행 책임 원본을 선택하는 라우터다. 한 질문에 하나의 현행 책임 원본만 둔다. PR #116은 승인 결정의 역사·승계 근거이며 현재 작업 브랜치나 병합 권위가 아니다.

## 1. 기본 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ BASE_RULES_VERSION.md
→ 이 Documentation Map
→ PROJECT_CORE.md
→ PROJECT_CANON_DECISION_LEDGER.md
→ audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md
→ CURRENT_IMPLEMENTATION_STATUS.md
→ ACTIVE_CONTEXT.md
→ HANDOFF_CONTEXT.md
→ 현재 질문의 분야별 책임 원본
→ 실제 코드·데이터·Scene·Resource·테스트
→ 연결 Google Sheet
```

## 2. 현재 책임 원본

| 질문 | 현행 책임 원본 | 권한 |
|---|---|---|
| 제품 정체성·플레이어 약속·불변 조건 | `PROJECT_CORE.md` | `CURRENT_CORE_AUTHORITY` |
| 현재 승인 Decision·상태 | `PROJECT_CANON_DECISION_LEDGER.md` | `CURRENT_DECISION_AUTHORITY` |
| 정본 복구·적대적 finding·Grill Me 큐 | `audits/OMENWARD_CANON_RECOVERY_AND_TOTAL_PLANNING_RESTART_2026-08-02.md` | `CURRENT_RECOVERY_AND_REVIEW_AUTHORITY` |
| 실제 구현·Legacy·미검증 경계 | `CURRENT_IMPLEMENTATION_STATUS.md` | `CURRENT_IMPLEMENTATION_AUTHORITY` |
| 현재 작업과 다음 Gate | `ACTIVE_CONTEXT.md` | `CURRENT_CONTEXT_PACK` |
| 새 작업자 인계 | `HANDOFF_CONTEXT.md` | `CURRENT_HANDOFF` |
| Base v9.4 적용 | `BASE_RULES_VERSION.md`, `reviews/2026-08-01_BASE_V9_4_ADOPTION_AUDIT.md` | `CURRENT_BASE_ADOPTION` |
| Google Sheet 역할·동기화 계약 | `PROJECT_GOOGLE_SHEET_WORKBOOK.md` | `CURRENT_SHEET_CONTRACT` |
| 미확정 기획 | `DECISIONS_PENDING.md` | `PENDING_ONLY / MUST_BE_RECONCILED_WITH_LEDGER` |
| 제품 구현·검증 순서 | `OMENWARD_ROADMAP.md` | `HISTORICAL_SEQUENCE / REPLAN_REQUIRED_BEFORE_CODEX` |
| 통합 게임 설명 | `OMENWARD_GAME_DESIGN.md` | `REFERENCE_SUMMARY / CURRENT_DECISIONS_OVERRIDE` |

## 3. 현재 승인 기획 계보

다음은 PR #116에서 사용자 승인된 기획 계보다. 현행 상태와 대체 관계는 `PROJECT_CANON_DECISION_LEDGER.md`가 소유한다.

- 20 Stage·4막·런타임/피로도.
- 콘텐츠 Manifest·미션 카드.
- 위험 Stage·보스 패키지.
- 패배·paid Retry 원칙.
- 전장 6/3/0=30.
- 벨루 정체성.
- Screen Board V2.
- 경제·Retry·save/checkpoint 구조.
- 최신 Red test 책임과 Legacy test 분류.
- 즉시 Decision sync 운영 규칙.

PR #116의 Base v9.3 migration 상태, 오래된 PR HEAD와 CI 판정은 현행 권위가 아니다.

## 4. 분야별 라우팅

| 분야 | 먼저 읽을 원본 | 보조·검증 |
|---|---|---|
| 핵심 컨셉·뾰족한 재미 | `PROJECT_CORE.md`, Decision Ledger | 룰렛 agency Evidence·사람 검증 계획 |
| Core·Session·Meta Loop | `PROJECT_CORE.md`, 현재 Grill Me Decision | 실제 Legacy session/retry code |
| 룰렛·TokenSource·이동 | `design/APPROVED_ROULETTE_CORE_RULES.md`, Decision Ledger | Legacy `roulette_service.gd`, 최신 Red spec 계보 |
| 전장·노드·점령 | Project Core, 30-node inherited Decision | Legacy battle simulator·tests |
| 경제·Retry·저장 | 현재 Decision Ledger | PR #116의 승인 구조 문서 계보, simulator/fault test는 NOT_RUN |
| 콘텐츠·위험 Stage·미션 | 현재 Decision Ledger | PR #116 승인 계보, exact values pending |
| 세계·인물·세력 | 기존 세계·인물 문서 + 현재 Grill Me 큐 | 벨루 Decision, 반복 동기 충돌 검토 |
| UX·UI·접근성 | Screen Board V2 inherited Decision | 실제 HUD·Visual Index·해상도/접근성 NOT_RUN |
| 아트·오디오·에셋 | 관련 승인 아트 문서·Visual Index | 제품 적용·라이선스·runtime 확인 |
| 구현 인계 | Planning and Review Complete Gate 이후 새 승인 Plan | 현재 Codex BLOCKED |

## 5. 실제 구현 경계

```text
CURRENT_PRODUCT
- independent weighted 9-cell roulette
- barracks/tower/farm
- legacy outpost/capture_power
- free same-stage retry
- graybox HUD and battlefield

LATEST_APPROVED_NOT_IMPLEMENTED
- physical reels and permanent move
- 30-node topology
- five buildings and latest economy
- fixed-time capture
- ProfileSave/RunCheckpoint/Journal/Backup
- paid Retry
- Screen Board V2 and Belu runtime
```

최종 구현 상태와 검증 상태는 `CURRENT_IMPLEMENTATION_STATUS.md`와 실제 실행 증거만 소유한다.

## 6. 상세 수치 라우팅

```text
LEGACY_H0 / HISTORICAL_ONLY
RECOMMENDED_DEFAULT
TEST_VALUE
SIMULATION_CANDIDATE
USER_APPROVED_VALUE
IMPLEMENTED_VALUE
VALIDATED_VALUE
```

수치의 플레이어 의미·상대 관계·제약식은 기획 정본이 소유하고, 후보 산출·분포·꼬리 위험은 simulation이 소유한다. 사용자가 상세 수치를 권장안대로 진행하도록 승인했더라도 시험값을 제품 확정값으로 표시하지 않는다.

## 7. Grill Me 규칙

- 저장소·Sheet·실제 파일로 확인 가능한 사실은 묻지 않는다.
- 이미 승인된 결정은 재질문하지 않는다.
- 기술 세부와 시험값은 묻지 않는다.
- 프로젝트 방향을 다르게 만드는 핵심 충돌만 한 번에 하나씩 질문한다.
- 답변 후 GitHub·Sheet가 `SYNCED`가 되기 전 다음 질문으로 넘어가지 않는다.

현재 첫 질문:

```text
OMW-DEC-20260802-META-PROGRESSION-ROLE-V1
Profile 영구 성장의 역할
```

## 8. 현재 다음 Gate

```text
OMW-DEC-20260802-CANON-RECOVERY-V1 GitHub·Sheet sync
→ replacement Draft PR
→ PR #116 superseded
→ Grill Me #1
→ 승인 Decision 즉시 sync
→ 다음 validated conflict
```

```text
PRODUCT_CODE: UNCHANGED
CODEX: BLOCKED
RUNTIME/HUMAN/SIMULATION: NOT_RUN
MOBILE: FUTURE_CONSIDERATION_ONLY
```
