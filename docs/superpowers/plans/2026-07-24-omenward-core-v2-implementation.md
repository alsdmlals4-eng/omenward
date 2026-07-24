# 오멘워드 코어 V2 구현 계획

- 작성일: 2026-07-24
- 상태: `APPROVED_DESIGN / IMPLEMENTATION_PLAN_DRAFT / PRODUCT_CODE_NOT_AUTHORIZED`
- 기준 Issue: `#56`
- 기준 main: `95e5ae225262f2427f21d5b7e4a03fb24e7eed6c`
- 선행 정본: `docs/PROJECT_CORE.md`, `docs/design/APPROVED_ROULETTE_CORE_RULES.md`, `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`

이 계획은 구현 순서와 검증 경계를 정의한다. 제품 코드 변경은 각 단계별 Codex Plan Mode 제안과 사용자 승인 뒤 시작한다.

## 공통 제약

- Godot 4.7.1 Standard, GDScript, Compatibility renderer 유지.
- 공용 10병종과 진영 Visual 분리 유지.
- 중앙 판정·완성선·등급·금화 resolver 계약 보존.
- 문서 정본 변경과 제품 기능 코드를 다른 PR로 분리.
- Red → Green → Refactor → 전체 회귀 → 독립 커밋.
- 실제 실행 증거 전 `PROVEN`, `COMPLETE`, `CORE_LOCK_V2` 금지.
- 전술 아이템 심벌·mid-run save·미션 전체·영구 성장·무한 방어는 범위 밖.

## Phase D0 — 문서 정본 마이그레이션

목표:

- V2 승인 설계와 legacy 구현 증거를 분리한다.
- 활성 책임 원본이 같은 상태와 규칙을 말하게 한다.

변경:

- PROJECT_CORE, GDD, 룰렛, MapRun, 상태, Handoff, Documentation Map, Roadmap, Decisions, README, AGENTS.
- 문서 validator와 mutation test.

완료 기준:

- V2 핵심 규칙 충돌 0.
- 구형 규칙은 legacy 문맥에서만 등장.
- broken link 0.
- 제품 코드·Scene·Resource 변경 0.

롤백: 문서 전용 커밋 revert.

## Phase R1 — 순수 resolver 분리

목표:

- 검증된 중앙 판정·완성선·등급·금화 계산을 독립 순수 객체로 보존한다.

후보 파일:

- `scripts/roulette/roulette_board_resolver.gd`
- `scripts/roulette/roulette_service.gd`
- `tests/headless/roulette_resolver_preservation_test.gd`

Red:

- 기존 중앙 판정 truth cases를 새 resolver에 요구한다.

Green:

- 기존 서비스가 새 resolver에 위임하되 legacy 결과는 바꾸지 않는다.

완료 기준:

- 기존 C1 resolver 회귀 전부 통과.
- resolver가 경제·UI·전설 상태를 소유하지 않음.

## Phase R2 — 물리 릴 도메인

타입:

- `RouletteTokenInstance`
- `RouletteReelState`
- `RouletteRunState`
- `RouletteSpinSnapshot`

필수 테스트:

- 릴 길이 3 이상.
- 토큰 ID 유일성.
- 길이 3·4·N wrap.
- 최저 안정 index X 교체.
- X 없음 append.
- 균등 start index.
- immutable deep snapshot.
- 같은 상태·시드의 동일 결과.

완료 기준: UI·경제 연결 없이 순수 도메인 계약 통과.

## Phase R3 — 건물 출처 동기화

계약:

- TokenSource 완공 → 각 릴에 출처 토큰 1개.
- 가로 이동 뒤에도 source ID 유지.
- 파괴 → live 릴에서 source 토큰 제거.
- 릴 길이 3 미만 → X 보충.
- stopped snapshot → 파괴 뒤에도 reward payload 보존.

핵심 테스트:

- 가로 이동한 토큰의 출처 제거.
- 정지 뒤 건물 파괴 후 동일 보상.
- 비TokenSource 건물의 토큰 미생성.

## Phase R4 — 이동·럭키·전설·확정 거래

계약:

- 세로 이동은 선택 릴 cursor 회전.
- 가로 이동은 노출 인덱스 TokenInstance 순환 교환.
- 이동 자원 즉시 소비.
- undo/reset 없음.
- preview는 clone 계산.
- confirm exactly once.
- 럭키 truth table.
- 위험 주기 전설 상태는 MapRun 소유.

핵심 테스트:

- 가로 이동 뒤 길이·cursor 불변.
- 모든 럭키 분기.
- 반복 confirm 무보상.
- 금화는 전설 한도 무관.

## Phase S1 — 보관함·결과 대기·판매·식량

계약:

- 보관함 4칸, 한 기 한 칸, 식량 0.
- 초과 결과 전체 대기, 손실 없음.
- 미해결 결과 중 새 회전 금지.
- 개별 배치·판매.
- 남은 결과 전부가 맞을 때 일괄 보관.
- 배치 후 회수·라인 변경·판매 금지.
- 사망 시 식량 반환.
- 수용량 감소는 신규 배치만 차단.

핵심 테스트:

- 영웅 2기·빈 슬롯 1칸.
- 한 기 판매 후 나머지 보관.
- 배치 실패 시 자원 미소비.
- 사망 식량 반환.

## Phase M1 — MapRun·StageFlow

상태:

- PREPARATION
- NORMAL_COMBAT
- TACTICAL_PLANNING
- DANGER_COMBAT
- SYSTEM_PAUSE
- STAGE_CLEAR
- RUN_COMPLETE
- DEFEAT

필수 테스트:

- 상태별 시간 진행 행렬.
- 무료 회전권 진입당 1회.
- 일반 예약 명령 취소·동시 적용.
- 룰렛 이동 즉시 예외.
- 위험 중 전투·웨이브 지속.
- mid-run save 명시적 미지원.

## Phase W1 — 묶음 웨이브와 정확 예고

계약:

- 라인당 최대 3기 묶음.
- 마지막 1~2기 허용.
- 첫 묶음 스테이지 시작 즉시.
- 마지막 묶음 t=0, 다음 예고 t=10, 다음 첫 묶음 t=20.
- 병종·수량·라인·특수 능력·최종 간격 공개.
- 묶음 내부 조합·순서 숨김.
- 최종 예약 출현과 모든 적 전멸 후 클리어.

## Phase B1 — 접전지 V2

계약:

- 라인당 중간 접전지 1개.
- 적이 전투 반경에 있으면 점령 정지.
- 점령 구역 병력 최소 1기.
- 병력 수·등급과 무관한 고정 8초.
- 양방향 게이지와 소유권 보존.
- 반경 밖 추격 금지.
- 후방 상실 시 선발대 후퇴·약화 없음, 신규 증원만 재점령.

## Phase U1 — Core UX

필수 표시:

- 세 릴 전체 토큰·출처 장부.
- 노출 보드와 중앙 판정.
- 가로 이동 전 고스트와 릴별 변화.
- 럭키 발생 표시, 확률·실패 수 숨김.
- 전설 주기 0/1.
- 보관함·결과 대기·식량.
- 정확 공세 예고와 웨이브 타임라인.
- 접전지 소유권·게이지·정지 이유.
- 라인별 원인 보고.

위험 스테이지에서 핵심 행동은 속도 시험이 되지 않도록 단축키·포커스·핀 패널·명확한 차단 이유를 제공한다. 자동 전술정지는 추가하지 않는다.

## Phase Q1 — 시뮬레이션·사람 검증

자동:

- 최소 100,000시드 자연 결과·등급·금화 EV.
- 최적 이동·판매·비축 전략 탐색.
- 순환 차익과 softlock 탐지.
- 3·5·20스테이지 활성 전투·준비·총시간 계측.

사람:

- 10~15분 3스테이지 슬라이스.
- 1920×1080·1280×720.
- 건설 영향, 가로 이동 장기 효과, 배치 이유, 실패 원인 설명.

통과 뒤에만:

```text
V2_VERTICAL_SLICE_PROVEN
CORE_LOCK_V2
```

을 검토한다.

## 독립 커밋 권장 순서

1. `docs: migrate omenward canon to approved core v2`
2. `refactor: isolate deterministic roulette resolver`
3. `feat: add deterministic physical roulette reels`
4. `feat: synchronize building token sources`
5. `feat: add irreversible roulette spin transactions`
6. `feat: add lossless roulette reward storage`
7. `feat: add map run and stage flow state machine`
8. `feat: add deterministic batched wave timeline`
9. `feat: implement fixed-time midpoint control`
10. `feat: expose core v2 tactical ux`
11. `test: add distribution and human proof gates`
