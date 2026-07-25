# 오멘워드 개발 로드맵

- 갱신일: 2026-07-26
- 기준: `docs/PROJECT_CORE.md`, `docs/design/APPROVED_V2_LEGENDARY_DEPLOYMENT_LIMIT_2026-07-26.md`, `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`, `docs/design/APPROVED_V2_TRANSACTION_FOUNDATION_SEQUENCE_2026-07-26.md`, `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- 현재 단계: `D0_COMPLETE / FIRST_V2_IMPLEMENTATION_PACKAGE_PLANNING_PENDING`
- 제품 구현: `NOT_STARTED`
- 사람 검증: `NOT_RUN`
- 잠금: `CORE_LOCK_V2_PENDING`

이 로드맵은 승인된 V2 범위를 구현 패키지 순서로 보여준다. 각 제품 패키지는 별도 Plan Mode 제안과 사용자 승인 전에는 구현 권한이 없다.

`docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`는 Issue #56과 구형 main 기준 초안이다. 순서 참고는 가능하지만 GM-01~GM-106 통합 결정, 승인된 거래 기반 순서와 후속 전설 획득·배치 제한 계약에 맞춘 재검증 없이 실행하지 않는다.

## 1. 현재 위치

```text
기존 기술 기준선·C1·C2·C3 자동 증거 확보
→ V2 설계·GM-01~GM-106 사용자 승인
→ V2 문서 정본 main 병합
→ Skill System·아카이브·공용 Skill 어댑터 정리
→ [현재] 첫 V2 구현 패키지 기획·Plan Mode 준비
→ resolver 보존 seam
→ 물리 릴·SpinSnapshot·SpinSession
→ R3
→ U1-F
→ S1-F
→ R4
→ U1-C
→ S1-C
→ 후속 승인 패키지
→ V2 UX·100,000시드·사람 검증
→ CORE_LOCK_V2 검토
→ 콘텐츠·메타 확장
```

## 2. 전체 완료 정의

오멘워드 코어 V2는 다음 경험과 증거가 함께 있을 때만 검증됐다고 부른다.

- 플레이어가 정확한 공세를 읽는다.
- 건설로 릴 배열과 확률이 바뀌는 것을 이해한다.
- 세로·가로 이동의 현재·미래 효과를 구분한다.
- 보관·판매·영구 배치를 공세와 연결한다.
- Tier 패시브와 룰렛 등급 액티브의 차이를 이해한다.
- 라인 대기·공격 명령으로 전선 흐름을 바꾼다.
- 일반과 위험의 시간 규칙을 예측한다.
- 자동전투·건설·수리·재건 결과와 실패 원인을 다음 선택에 사용한다.
- 자동 계약, 분포 시뮬레이션과 사람 플레이가 모두 통과한다.

## 3. 단계 표

| 단계 | 목표 | 현재 상태 | 통과 게이트 |
|---|---|---|---|
| D0 | V2 정본·상태·Skill 경계 일치 | 완료 | PR #57·#65·#66·#67 및 문서 CI |
| P1 | 첫 구현 패키지 재설계·승인 | 진행 전 | 최신 원장 대조·사용자 Plan 승인 |
| R1 | 순수 resolver 보존 seam | 미시작 | legacy 결과 불변 |
| R2 | 물리 릴·SpinSnapshot·SpinSession 순수 도메인 | 미시작 | 릴 invariant·결정론·immutable snapshot |
| R3 | TokenSource·NORMAL_X·SOURCE_BOUND_X 동기화 | 미시작 | 출처·파괴·blocked 거래 |
| U1-F | immutable UnitRewardPayload 기반 | 미시작 | snapshot-only 조합·deterministic serialization |
| S1-F | PendingReward ID·put-once 저장 기반 | 미시작 | 중복 0·receipt 복구 |
| R4 | 이동 경제·럭키·전설 보상 보존·원자 확정 | 미시작 | truth table·항상-전설 pending·idempotency·자원 장부 |
| U1-C | 세부 병종·Tier 패시브·등급 액티브·AI 완성 | 미시작 | 생성 순서·영웅 변환 조합·우선순위·회귀 |
| S1-C | PendingReward 보관·판매·배치·식량·전설 배치 제한 완성 | 미시작 | 무손실·중복 0·softlock 0·경고 동의·commit 재검증·배치 rollback |
| M1 | MapRun·StageFlow·지속 상태 | 미시작 | 상태 소유·시간 행렬 |
| W1 | 묶음 웨이브·정확 예고 | 미시작 | deterministic timeline |
| L1 | 배치 즉시 출격·대기 앵커·공격 명령·접전지 | 미시작 | 명령 상속·HoldRadius·고정 8초 |
| B1 | 건설·blocked 교체·방어탑·수리·성문 재건 | 미시작 | 거래 순서·고정소수점·footprint |
| X1 | V2 Core UX | 미시작 | 정보 인과·1080p·720p |
| Q1 | 분포·경제·사람 검증 | 미시작 | 100k·10~15분·회귀 |
| P4 | 콘텐츠·메타 확장 | 보류 | 코어 V2 proven |

## 4. D0 — 정본·운영 정리

완료 범위:

- PR #57: V2 통합 정본과 GM-01~GM-106 결정 원장.
- PR #65: Skill System v4와 사람 플레이 검증 Skill.
- PR #66: Base 아카이브 거버넌스 adapter-only 채택.
- PR #67: Base 공용 Skill route와 Godot 에셋 우선 탐색.
- 활성 상태·인계 문서의 V2 current 동기화.

D0 완료는 제품 구현 완료가 아니다.

## 5. P1 — 첫 구현 패키지 설계

목표:

- legacy C1의 검증된 중앙 판정·완성선·등급·금화를 손실 없이 보존한다.
- V2 물리 릴 도메인이 기존 경제·UI·전투 상태와 뒤엉키기 전에 책임 경계를 고정한다.

필수 설계 항목:

- 플레이어 가치와 위험 가설.
- 포함·제외 범위.
- 기존 `RouletteService`와 resolver seam.
- `TokenInstance`, `ReelState`, `SpinSnapshot`, `SpinSession` 상태 소유.
- Red 테스트와 legacy 회귀.
- 마이그레이션·롤백.
- Godot 실행 명령과 완료 금지 표현.

## 6. R1 — resolver 보존 seam

플레이어 가치: 새 물리 릴을 도입하면서 검증된 당첨 판정을 잃지 않는다.

- 중앙 선행 판정.
- 8개 완성선.
- 일반·엘리트·영웅·전설.
- 금화 75/200/500%.
- 결정론적 출처 snapshot 경계.

완료 기준: legacy generator가 순수 resolver를 통해 동일 결과를 만들고 resolver가 릴 상태·경제·UI·전설 배치 정책을 소유하지 않는다.

## 7. R2~R4와 거래 기반

R2:

- `TokenInstance`, `ReelState`, `SpinSnapshot`, `SpinSession`.
- 길이 3 이상, wrap, cursor, 균등 정지, immutable deep snapshot.

R3:

- TokenSource 완공·업그레이드·파괴.
- `NORMAL_X` 교체·append.
- blocked TokenSource와 `SOURCE_BOUND_X` 위치 보존·복원·영구 제거.

U1-F:

- snapshot과 최종 보드만 소비하는 immutable `UnitRewardPayload`.
- 출처 건물·완성 Tier·세부 병종·등급·패시브·액티브 payload 동결.
- live 건물 재조회 금지.
- 전설 결과는 횟수·stage 주기와 무관하게 `reward_grade = legendary`로 동결.
- 실제 spawn·AI 실행 제외.

S1-F:

- `spin_session_id`, `confirm_transaction_id`, `pending_reward_id`, `reward_index`.
- `PendingRewardEnvelope`와 put-once 저장소.
- transaction별 reward와 `ConfirmReceipt` 재조회.
- 전설 PendingReward를 원래 등급 그대로 여러 개 보존.
- 보관·판매·배치·식량 제외.

R4:

- 세로·가로 이동과 미래 배열 영구 편집.
- 럭키 무료 이동·보관형 이동 상한·무보상 누적·pending.
- 전설 결과를 항상 전설 PendingReward로 원자 확정.
- 전설 획득 주기·확정 시 영웅 변환 없음.
- `[확정]` 원자 거래와 idempotency.
- 두 번째 동일 확정 요청은 기존 receipt 반환.
- 0.001 금화 고정소수점 장부.

## 8. U1-C — 병종·능력 성장 완성

- 모든 등급에서 선택 세부 병종 유지.
- 완성 출처 Tier 가중치.
- Tier 1~3 패시브 생성·강화.
- 일반~전설 액티브 기술 생성·강화.
- 병종별 작성 우선순위와 AI 자동 발동.
- 구형 `fixed_grade_unit_template_id` 제거 또는 마이그레이션.
- R4에서 확정한 payload를 변경하지 않고 실제 유닛 생성 데이터로 조합.
- 전설 배치 충돌이 승인된 경우 같은 출처·Tier·세부 병종의 영웅 등급 payload 2개를 결정론적으로 조합.

## 9. S1-C — 결과 처리·보관·식량·전설 배치 제한 완성

- 유닛 `PendingReward`, 금화 즉시 지급.
- 보관함 4칸과 초과 결과 전체 대기.
- 개별 배치·판매·조건부 일괄 보관.
- 배치 비가역성과 사망 식량 반환.
- 플레이어 전장의 실제 `is_alive` 전설 최대 1기.
- 생존 전설 충돌 시 변환 경고와 명시적 동의.
- 배치 커밋 순간 생존 전설 재검증.
- 경고 확인 뒤 기존 전설 사망 시 새 보상을 전설 그대로 배치.
- 경고 없이 시작했지만 커밋 순간 충돌이 생기면 무변경 중단 후 새 경고 요구.
- 충돌이 계속되면 동일 세부 병종 영웅 2기를 같은 라인에 원자 배치.
- spawn 실패 시 식량·pending 상태·로그 원자 rollback.

통과: 결과 손실·중복·softlock·부분 배치·무동의 자동 강등 0.

## 10. M1·W1·L1 — 런과 전선

M1:

- Map→Stage→Wave 계층.
- 같은 맵의 건물·병력·체력·자원·릴·보관함·접전지 지속.
- 전설 PendingReward 등급과 보관 상태를 stage 전환에서 변경하지 않음.
- 다른 맵은 NEW GAME.

W1:

- 라인당 최대 3기 묶음.
- 첫 묶음 즉시, 다음 예고 10초, 다음 첫 묶음 20초.
- 정확한 총수량·병종·라인·특수 행동 공개.

L1:

- 배치 즉시 출격.
- 라인별 최신 대기 앵커 또는 공격 명령.
- 현재·이동 중·향후 유닛의 명령 상속.
- `HoldRadius`와 고정 8초 비교전 접전지.
- 실제 spawn 결과와 `is_alive`를 생존 전설 판정의 유일한 전장 근거로 제공.

## 11. B1 — 건설·구조물·수리·재건

- 결정론적 건설·업그레이드·교체·철거 시간.
- 전방 건설 권리와 blocked 일반 건물.
- 방어탑 직접 공격 예외와 점령 시 소유권 이전.
- 글로벌 수리 예산·작업자 임금 곡선·1초 정산.
- 성문 `BREACHED`, 30초 재건, 진행 치유, footprint 활성화.

## 12. X1 — Core UX

- 릴 전체 배열·출처·가중치.
- 가로 이동 고스트와 장기 변화.
- 중앙 판정·보상·PendingReward.
- Tier 패시브·등급 액티브 구분.
- 전설 PendingReward, 생존 전설 1기 제한, 변환 경고·재검증 결과, 보관함·식량.
- 정확 공세·웨이브 타임라인.
- 라인 명령·접전지·건설·수리·재건 상태와 차단 이유.
- 라인별 원인 보고.

위험 스테이지는 클릭 속도 시험이 되지 않도록 단축키와 포커스 계약을 검증한다.

## 13. Q1 — 검증

자동:

- 최소 100,000시드.
- 금화 EV·판매·비축·순환 차익.
- 3·5·20스테이지 시간.
- 상태·거래·결정론·회귀.
- 전설 반복 획득, 생존 상한, 경고 동의, commit 재검증, 영웅 2기 원자 배치와 rollback.

사람:

- 10~15분 3스테이지.
- 1920×1080·1280×720.
- 건설·가로 이동·능력 성장·명령·배치·실패 이유 설명.
- 전설 보관과 두 번째 전설 배치 경고·결과 변경 이유 설명.

## 14. CORE_LOCK_V2 조건

다음을 모두 만족할 때만 검토한다.

- V2 정본 main 병합.
- 승인된 V2 제품 실행 경로 구현.
- C1V2·C2V2·C3V2·C5V2 자동 계약.
- C4V2 사람 플레이.
- P0·P1 잔여 0.
- 실제 source commit과 evidence 기록.

## 15. 확장 보류

코어 검증 전 구현하지 않는다.

- 미션 전체 세트와 최종 등급.
- 베테랑·나이트메어·헬 변형 풀.
- 전체 10병종·Tier·보스 콘텐츠.
- 대규모 영구 성장과 초기화 경제.
- 무한 방어.
- 캠페인·아트 대량 제작.
- 전투 중 mid-run save.
