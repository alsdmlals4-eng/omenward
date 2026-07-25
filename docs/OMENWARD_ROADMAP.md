# 오멘워드 개발 로드맵

- 갱신일: 2026-07-26
- 기준: `docs/PROJECT_CORE.md`, `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`, `docs/CURRENT_IMPLEMENTATION_STATUS.md`
- 현재 단계: `D0_COMPLETE / FIRST_V2_IMPLEMENTATION_PACKAGE_PLANNING_PENDING`
- 제품 구현: `NOT_STARTED`
- 사람 검증: `NOT_RUN`
- 잠금: `CORE_LOCK_V2_PENDING`

이 로드맵은 승인된 V2 범위를 구현 패키지 순서로 보여준다. 각 제품 패키지는 별도 Plan Mode 제안과 사용자 승인 전에는 구현 권한이 없다.

`docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`는 Issue #56과 구형 main 기준 초안이다. 순서 참고는 가능하지만 GM-01~GM-106 통합 결정에 맞춘 재검증 없이 실행하지 않는다.

## 1. 현재 위치

```text
기존 기술 기준선·C1·C2·C3 자동 증거 확보
→ V2 설계·GM-01~GM-106 사용자 승인
→ V2 문서 정본 main 병합
→ Skill System·아카이브·공용 Skill 어댑터 정리
→ [현재] 첫 V2 구현 패키지 기획·Plan Mode 준비
→ resolver 보존 seam
→ 물리 릴·SpinSnapshot·SpinSession
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
| R4 | 이동 경제·럭키·전설·원자 확정 | 미시작 | truth table·idempotency·자원 장부 |
| U1 | 세부 병종·Tier 패시브·등급 액티브·AI | 미시작 | 생성 순서·우선순위·회귀 |
| S1 | PendingReward·보관·판매·식량 | 미시작 | 무손실·중복 0·softlock 0 |
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

완료 기준: legacy generator가 순수 resolver를 통해 동일 결과를 만들고 resolver가 릴 상태·경제·UI·전설 주기를 소유하지 않는다.

## 7. R2~R4 — 룰렛 V2

R2:

- `TokenInstance`, `ReelState`, `SpinSnapshot`, `SpinSession`.
- 길이 3 이상, wrap, cursor, 균등 정지, immutable deep snapshot.

R3:

- TokenSource 완공·업그레이드·파괴.
- `NORMAL_X` 교체·append.
- blocked TokenSource와 `SOURCE_BOUND_X` 위치 보존·복원·영구 제거.

R4:

- 세로·가로 이동과 미래 배열 영구 편집.
- 럭키 무료 이동·보관형 이동 상한·무보상 누적·pending.
- 위험 주기 전설.
- `[확정]` 원자 거래와 idempotency.
- 0.001 금화 고정소수점 장부.

## 8. U1 — 병종·능력 성장

- 모든 등급에서 선택 세부 병종 유지.
- 완성 출처 Tier 가중치.
- Tier 1~3 패시브 생성·강화.
- 일반~전설 액티브 기술 생성·강화.
- 병종별 작성 우선순위와 AI 자동 발동.
- 구형 `fixed_grade_unit_template_id` 제거 또는 마이그레이션.

## 9. S1 — 결과 처리·보관·식량

- 유닛 `PendingReward`, 금화 즉시 지급.
- 보관함 4칸과 초과 결과 전체 대기.
- 개별 배치·판매·조건부 일괄 보관.
- 배치 비가역성과 사망 식량 반환.

통과: 결과 손실·중복·softlock 0.

## 10. M1·W1·L1 — 런과 전선

M1:

- Map→Stage→Wave 계층.
- 같은 맵의 건물·병력·체력·자원·릴·보관함·접전지 지속.
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
- 전설 주기·보관함·식량.
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

사람:

- 10~15분 3스테이지.
- 1920×1080·1280×720.
- 건설·가로 이동·능력 성장·명령·배치·실패 이유 설명.

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
