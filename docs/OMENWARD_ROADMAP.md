# 오멘워드 개발 로드맵

- 갱신일: 2026-07-24
- 기준: `docs/PROJECT_CORE.md`, `docs/CURRENT_IMPLEMENTATION_STATUS.md`, V2 통합 명세
- 현재 단계: `D0 V2 문서 정본 마이그레이션`
- 제품 구현: `NOT_STARTED`
- 사람 검증: `NOT_RUN`

## 1. 현재 위치

```text
기존 기술 기준선·C1·C2·C3 자동 증거 확보
→ V2 설계·7개 계약 사용자 승인
→ [현재] 문서 정본 마이그레이션
→ resolver 보존 분리
→ 물리 릴·snapshot·조작
→ 보관·MapRun·웨이브·접전지
→ V2 UX
→ 100,000시드·사람 검증
→ CORE_LOCK_V2 검토
→ 콘텐츠·메타 확장
```

## 2. 전체 완료 정의

오멘워드 코어 V2는 다음 경험과 증거가 함께 있을 때만 검증됐다고 부른다.

- 플레이어가 정확한 공세를 읽는다.
- 건설로 릴 배열과 확률이 바뀌는 것을 이해한다.
- 세로·가로 이동의 현재·미래 효과를 구분한다.
- 보관·판매·영구 배치를 공세와 연결한다.
- 일반과 위험의 시간 규칙을 예측한다.
- 자동전투 결과와 실패 원인을 다음 선택에 사용한다.
- 자동 계약, 분포 시뮬레이션과 사람 플레이가 모두 통과한다.

## 3. 단계 표

| 단계 | 목표 | 현재 상태 | 통과 게이트 |
|---|---|---|---|
| D0 | V2 정본 일치 | 진행 | 문서·링크·상태 검사 |
| R1 | 순수 resolver 분리 | 미시작 | legacy 결과 불변 |
| R2 | 물리 릴 도메인 | 미시작 | 릴 invariant·결정론 |
| R3 | 건물 출처·snapshot | 미시작 | 파괴 후 보상 보존 |
| R4 | 이동·럭키·전설·확정 | 미시작 | truth table·idempotence |
| S1 | 보관·판매·식량 | 미시작 | 무손실·softlock 0 |
| M1 | MapRun·StageFlow | 미시작 | 시간 행렬 |
| W1 | 묶음 웨이브·예고 | 미시작 | deterministic timeline |
| B1 | 고정 8초 접전지 | 미시작 | 전투 반경·게이지 |
| U1 | V2 Core UX | 미시작 | 정보 인과·해상도 |
| Q1 | 분포·사람 검증 | 미시작 | 100k·10~15분 |
| P4 | 콘텐츠·메타 확장 | 보류 | 코어 V2 proven |

## 4. D0 — 문서 정본 마이그레이션

범위:

- PROJECT_CORE, V2 통합 명세, 룰렛, MapRun.
- GDD, Current Status, Handoff, Documentation Map, Roadmap, Decisions, Active Context, README, AGENTS.
- 문서 validator와 mutation tests.

금지:

- 제품 GDScript, Scene, Resource, 데이터 변경.
- `CORE_LOCK_V2` 선언.

통과:

- 구형 active 규칙 0.
- legacy evidence와 V2 상태 혼합 0.
- broken link 0.
- 문서 계약 테스트 통과.

## 5. R1 — resolver 보존 분리

플레이어 가치: 새 물리 릴을 도입하면서 검증된 당첨 판정을 잃지 않는다.

- 중앙 선행 판정.
- 8개 완성선.
- 일반·엘리트·영웅·전설.
- 금화 75/200/500%.
- 결정론적 출처 snapshot.

완료 기준: legacy generator가 resolver를 위임해 동일 결과를 만들고 resolver가 상태·경제·UI를 소유하지 않는다.

## 6. R2~R4 — 룰렛 V2

R2:

- TokenInstance, ReelState, RouletteRunState, SpinSnapshot.
- X 교체·append·wrap·균등 정지.

R3:

- TokenSource 건물 이벤트.
- 출처 토큰 제거와 X 보충.
- stopped snapshot 보상 보존.

R4:

- 세로·가로 이동.
- 즉시 소비·undo 없음.
- 럭키 truth table.
- 위험 주기 전설.
- 명시적 한 번 확정.

통과: C1V2 자동 계약.

## 7. S1 — 보관·판매·식량

- 4칸 보관함.
- 초과 결과 전체 대기.
- 개별 배치·판매.
- 식량 수용량과 사망 반환.
- 배치 비가역성.

통과: 결과 손실·중복·softlock 0.

## 8. M1·W1·B1 — 전투 흐름

M1:

- PREPARATION, NORMAL_COMBAT, TACTICAL_PLANNING, DANGER_COMBAT, SYSTEM_PAUSE.

W1:

- 3기 묶음, 10초 예고, 20초 시작, 정확 총수량.

B1:

- 전투 반경, 점령 구역, 고정 8초 양방향 게이지.

통과: C2V2·C3V2 자동 계약.

## 9. U1 — Core UX

- 릴 전체 배열·출처.
- 가로 이동 고스트와 장기 변화.
- 중앙 판정·보상 예측.
- 전설 주기·보관함·식량.
- 정확 공세와 웨이브 타임라인.
- 접전지 상태와 원인 보고.

위험 스테이지는 클릭 속도 시험이 되지 않도록 단축키와 포커스 계약을 검증한다.

## 10. Q1 — 검증

자동:

- 100,000시드 이상.
- 금화 EV·판매·비축·순환 차익.
- 3·5·20스테이지 시간.
- 저장 미지원 경계.

사람:

- 10~15분 3스테이지.
- 1080p·720p.
- 건설·가로 이동·배치·실패 이유 설명.

## 11. CORE_LOCK_V2 조건

다음을 모두 만족할 때만 검토한다.

- V2 정본 main 병합.
- C1V2·C2V2·C3V2·C5V2 자동 계약.
- C4V2 사람 플레이.
- P0·P1 잔여 0.
- 실제 source commit과 evidence 기록.

## 12. 확장 보류

코어 검증 전 구현하지 않는다.

- 미션 전체 세트와 최종 등급.
- 베테랑·나이트메어·헬 변형 풀.
- 대규모 영구 성장과 초기화 경제.
- 무한 방어.
- 전체 10병종·Tier·보스.
- 캠페인·아트 대량 제작.
- 전투 중 mid-run save.
