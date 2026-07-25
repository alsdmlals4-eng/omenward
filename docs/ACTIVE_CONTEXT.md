# Active Context

- 갱신일: 2026-07-24
- 공식명: **오멘워드 / OMENWARD**
- 현재 작업: Issue `#56` V2 정본 마이그레이션
- 설계 상태: `V2_SPEC_APPROVED`
- 정본 상태: `V2_CANON_CANDIDATE`
- 구현 상태: `V2_IMPLEMENTATION_NOT_STARTED`
- 기존 증거: `LEGACY_C1_C2_C3_PROVEN`
- 사람 검증: `HUMAN_QA_NOT_RUN`
- 잠금: `CORE_LOCK_V2_PENDING`

## 1. 지금 읽을 문서

1. `docs/PROJECT_CORE.md`
2. `docs/design/APPROVED_CORE_V2_INTEGRATED_SPEC.md`
3. `docs/design/APPROVED_ROULETTE_CORE_RULES.md`
4. `docs/design/APPROVED_MAPRUN_STAGE_WAVE_AND_MIDPOINT_CORE_V1.md`
5. `docs/CURRENT_IMPLEMENTATION_STATUS.md`
6. `docs/HANDOFF_CONTEXT.md`
7. `docs/DOCUMENTATION_MAP.md`
8. `docs/OMENWARD_ROADMAP.md`
9. Issue `#56`과 현재 PR

## 2. 핵심 문장

> **건물로 룰렛을 만들고, 룰렛으로 전선을 지휘한다.**

오멘워드는 예고된 세 전선의 공세를 읽고, TokenSource 건물과 영구 가로 이동으로 세 원형 릴을 설계한 뒤, 당첨 병력을 한 라인에 커밋해 자동전투를 뒤집는 게임이다.

## 3. 2026-07-24 확정 계약

- 가로 이동: 노출 인덱스 `TokenInstance` 순환 교환, 길이·cursor 불변.
- X 교체: 가장 낮은 안정 배열 인덱스.
- 멈춤 보드: immutable SpinSnapshot.
- 출처 후보: snapshot 전체 릴의 동일 심벌 풀.
- 럭키: 숨김 15/25/35/45/55/100%와 최신 truth table.
- 심벌: 병종·금화·X, 전술 아이템 심벌 보류.
- 토큰 공급: TokenSource 건물만.
- 저장: 코어 PoC·첫 수직 슬라이스 mid-run save 미지원.

## 4. 보존과 교체

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

## 5. 현재 실행 경계

기존 C1·C2·C3는 legacy 설계 기준으로 원격 검증됐다. V2 물리 릴, MapRun, 묶음 웨이브, 고정 8초 접전지와 V2 UX는 구현되지 않았다.

```text
LEGACY_IMPLEMENTED != V2_IMPLEMENTED
DOCUMENT_APPROVED != EXECUTION_PROVEN
```

## 6. 다음 작업

```text
문서 PR 검증·병합
→ resolver 분리 제안서
→ 물리 릴 순수 도메인
→ snapshot·이동·럭키·전설
→ 보관·배치·식량
→ MapRun·웨이브·접전지
→ UX·분포·사람 플레이
```

제품 코드 작업은 별도 Plan Mode 승인 전 금지한다.
