# Active Context

- 갱신일: 2026-07-26
- 공식명: **오멘워드 / OMENWARD**
- 현재 작업: V2 첫 구현 패키지 기획·Plan Mode 준비
- 설계 상태: `V2_SPEC_APPROVED`
- 정본 상태: `V2_CANON_CURRENT_BY_PR_57_MERGE`
- 구현 상태: `V2_IMPLEMENTATION_NOT_STARTED`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 잠금: `CORE_LOCK_V2_PENDING`
- 운영 작업: Issue `#62` Ruleset·ci-gate·자동 병합은 제품 구현과 별도

## 1. 지금 읽을 문서

1. `AGENTS.md`
2. `docs/PROJECT_CORE.md`
3. `docs/design/APPROVED_CORE_V2_INTEGRATED_DECISION_LEDGER_2026-07-25.md`
4. `docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md`
5. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
6. `docs/HANDOFF_CONTEXT.md`
7. `docs/DOCUMENTATION_MAP.md`
8. 작업별 세부 APPROVED 문서
9. 실제 코드·데이터·Scene·테스트

`docs/superpowers/plans/2026-07-24-omenward-core-v2-implementation.md`는 Issue #56과 구형 main 기준 초안이다. 최신 통합 결정 원장에 맞춘 재검증 전에는 제품 구현 권한이 없다.

## 2. 핵심 문장

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

오멘워드는 예고된 세 전선의 공세를 읽고, TokenSource 건물과 영구 가로 이동으로 세 원형 릴을 설계한 뒤, 당첨 병력을 한 라인에 커밋해 자동전투를 뒤집는 게임이다.

## 3. 현재 정본

- PR #57에서 GM-01~GM-106 통합 결정 원장과 V2 정본을 병합했다.
- PR #65에서 Skill System v4와 사람 플레이 Skill 계약을 재구성했다.
- PR #66에서 Base 아카이브 거버넌스를 adapter-only 방식으로 채택했다.
- PR #67에서 Base 공용 Skill route와 Godot 에셋 우선 탐색 연결을 병합했다.
- 위 문서·운영 병합은 Godot 제품 구현을 시작하거나 `CORE_LOCK_V2`를 선언한 것이 아니다.

## 4. 핵심 V2 계약

- 가로 이동: 노출 인덱스 `TokenInstance` 순환 교환, 길이·cursor 불변.
- X 교체: 가장 낮은 안정 배열 인덱스. `SOURCE_BOUND_X`는 일반 교체 대상이 아님.
- 멈춤 보드: immutable `SpinSnapshot`.
- 결과 처리: 명시적 `[확정]`에서 정확히 한 번 처리.
- 출처 후보: snapshot 전체 릴의 동일 심벌 출처 건물 풀.
- 세부 병종 유지, Tier 패시브, 룰렛 등급 액티브, AI 자동 발동.
- 배치 즉시 출격, 라인별 대기 앵커·공격 명령.
- blocked 건물·적 교체·source-bound X 거래.
- 글로벌 수리 예산·0.001 금화 고정소수점 장부·성문 재건.
- Map→Stage→Wave 연속성과 맵 단위 런·메타 진행.
- 전술 아이템 룰렛 심벌과 코어 PoC mid-run save는 보류.

## 5. 보존과 교체

보존:

- 고정 3라인.
- 중앙 판정·완성선·등급·금화 resolver.
- 결정론과 출처 원장.
- 공용 병종 데이터.
- 전장 상태 기반 승패와 원인 보고.

교체:

- 독립 9칸 추첨.
- 공개 12% 럭키·+8%p.
- 이동 되돌리기·확정 시 소비.
- 스테이지당 전설 1회.
- 60초 공세와 T-30/T-15/T-5.
- 점령력 합산.
- 단일 StageRun 영속 상태.
- 계열 고정 상위 등급 템플릿.

## 6. 현재 실행 경계

기존 C1·C2·C3는 legacy 설계 기준으로 원격 검증됐다. V2 물리 릴, SpinSession, MapRun, Tier·등급 능력 성장, 라인 명령, 건설·수리·재건과 V2 UX는 구현되지 않았다.

```text
LEGACY_IMPLEMENTED != V2_IMPLEMENTED
DOCUMENT_APPROVED != EXECUTION_PROVEN
```

## 7. 다음 작업

```text
활성 상태·인계 문서 동기화
→ 구형 구현 계획을 GM-01~GM-106 기준으로 재검증
→ 첫 구현 패키지의 목표·포함·제외·Red 테스트·롤백 설계
→ 사용자 Plan Mode 승인
→ Codex 구현
```

첫 구현 패키지는 검증된 C1 중앙 판정을 보존하는 `RouletteBoardResolver` seam과 물리 릴·`SpinSnapshot`·`SpinSession`의 순수 도메인 경계를 우선 검토한다. 제품 코드 작업은 별도 Plan Mode 승인 전 금지한다.
