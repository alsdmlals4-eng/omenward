# OMENWARD 프로젝트 인수인계 컨텍스트

- 갱신일: 2026-07-26
- 현재 상태: `V2_SPEC_APPROVED / V2_CANON_CURRENT_BY_PR_57_MERGE / V2_IMPLEMENTATION_NOT_STARTED`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 플레이: `HUMAN_QA_NOT_RUN`
- 잠금 상태: `CORE_LOCK_V2_PENDING`
- 현재 제품 작업: 첫 V2 구현 패키지 Plan Mode 준비
- 별도 운영 Issue: `#62`
- 프로젝트 코어: `docs/PROJECT_CORE.md`
- 실제 구현 상태: `docs/CURRENT_IMPLEMENTATION_STATUS.md`

이 문서는 새 작업자가 이전 대화 없이 현재 제품 방향, 승인 규칙, 구현 경계와 다음 조사 순서를 이해하기 위한 출발점이다.

## 1. 가장 먼저 알아야 할 것

1. 오멘워드는 건물과 가로 이동으로 세 원형 릴의 미래 배열을 설계하고, 당첨 병력을 세 라인 중 하나에 영구 배치하는 실시간 전략 오토배틀이다.
2. PR #57에서 GM-01~GM-106 통합 결정 원장과 V2 제품 정본이 `main`에 병합됐다.
3. 현재 main의 C1·C2·C3는 기존 설계 기준 실행 증거이며 V2 구현 완료 증거가 아니다.
4. V2 Godot 제품 코드와 게임 데이터 구현은 아직 시작하지 않았다.
5. PR #65·#66·#67은 Skill·아카이브·공용 어댑터 운영 변경이며 제품 구현이 아니다.
6. 제품 코드 변경은 최신 통합 결정 원장에 맞춘 단계별 Plan Mode 제안과 사용자 승인이 필요하다.
7. 공용 10병종과 진영 Visual 분리, Godot 4.7.1·GDScript 기술 기준선은 유지한다.
8. 전술 아이템 룰렛 심벌과 코어 PoC mid-run save는 현재 코어 범위가 아니다.

## 2. 읽기 순서

```text
최신 사용자 지시
→ AGENTS.md
→ docs/BASE_RULES_VERSION.md
→ docs/DOCUMENTATION_MAP.md
→ docs/PROJECT_CORE.md
→ docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md
→ docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md
→ docs/CURRENT_IMPLEMENTATION_STATUS.md
→ 작업별 세부 APPROVED 문서
→ docs/OMENWARD_GAME_DESIGN.md
→ docs/OMENWARD_ROADMAP.md
→ 현재 Issue·PR·승인 제안서
→ 실제 code/data/Scene/tests
→ docs/ACTIVE_CONTEXT.md
```

`docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`는 구형 main과 Issue #56 기준 `IMPLEMENTATION_PLAN_DRAFT`다. 최신 통합 결정 원장에 맞춰 다시 설계·승인하기 전에는 구현 근거로 사용하지 않는다.

## 3. 제품 약속

> **예고된 세 전선의 공세를 읽고, 제한된 건물로 세 원형 릴의 토큰 구조를 설계·영구 편집한 뒤, 당첨 병력을 어느 전선에 커밋할지 결정해 전황을 뒤집는다.**

핵심 플레이 감정:

```text
설계했다 → 릴 토큰·출처·인접 순서를 만들었다
읽어냈다 → 보드·공세·보관·식량을 비교했다
적중했다 → 비가역 배치가 전선을 뒤집었다
학습했다 → 실패 원인을 다음 건설·조작·배치에 반영했다
```

## 4. 핵심 구조

- 독립 상·중·하 3라인.
- TokenSource 건물이 각 릴에 같은 출처 토큰 1개씩 제공.
- 길이 3 이상의 세 원형 릴.
- 세로 이동은 릴 cursor 회전.
- 가로 이동은 노출 인덱스 토큰 순환 교환과 미래 배열 영구 편집.
- 중앙줄 선행 판정과 1/2/3~7/8 완성선 등급.
- immutable SpinSnapshot과 명시적 한 번 확정.
- 세부 병종 유지, Tier 패시브, 등급 액티브, AI 자동 발동.
- 보관함 4칸, 무손실 결과 대기, 판매와 라인 영구 배치.
- 배치 즉시 출격, 라인별 대기 앵커·공격 명령.
- blocked 건물·source-bound X·방어탑 소유권 이전.
- 글로벌 수리 예산·고정소수점 금화·성문 재건.
- Map→Stage→Wave 연속성과 맵 단위 런·메타 진행.

## 5. 기존 구현 증거

보존 가능한 legacy 증거:

- 중앙 판정·완성선·등급·금화.
- 결정론과 출처 ID.
- 3라인과 공용 병종.
- 구조물·본진 승패 경로.
- 도메인 snapshot→HUD와 원인 보고.

교체할 legacy 계약:

- 독립 9칸 가중 추첨.
- 구형 럭키·이동·전설 제한.
- 60초/T-30·15·5.
- 점령력 합산.
- StageRun 중심 런 상태.
- 계열 고정 상위 등급 템플릿.
- 아군 주기적 배치 묶음.

## 6. 구현 전 확인

제품 코드 변경 전 반드시 확인한다.

- 최신 통합 결정 원장과 충돌 없는 단계별 Plan Mode 제안서.
- 목표와 플레이어 가치.
- 포함·제외 범위.
- 상태 소유와 데이터 마이그레이션.
- Red 테스트와 회귀 테스트.
- 롤백 기준.
- 실행할 Godot 명령.
- 제품 코드·문서 정본 변경 PR 분리.

## 7. 다음 순서

1. 활성 상태·인계 문서를 `V2_CANON_CURRENT` 상태로 동기화한다.
2. 2026-07-24 구현 계획을 GM-01~GM-106 기준으로 재검증한다.
3. 첫 패키지에서 legacy C1 중앙 판정을 보존할 resolver seam을 설계한다.
4. 물리 릴·SpinSnapshot·SpinSession 순수 도메인의 포함·제외와 Red 테스트를 확정한다.
5. 사용자가 Plan Mode 제안서를 승인한 뒤 Codex 구현으로 전환한다.
6. 후속 패키지에서 건물 출처·이동 경제·결과 거래·병종 능력·MapRun·전장을 순차 연결한다.
7. V2 UX, 100,000시드와 10~15분 사람 검증을 실행한다.

## 8. 금지된 완료 표현

다음 조건 전에는 `CORE_LOCK_V2`, `V2_IMPLEMENTED`, `CORE_LOOP_PROVEN`, `MVP_COMPLETE`를 사용하지 않는다.

- 해당 V2 제품 실행 경로 구현.
- V2 자동 계약 통과.
- 10~15분 사람 플레이.
- 1080p·720p 가독성 검증.
