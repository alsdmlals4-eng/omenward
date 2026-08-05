# [현행] 오멘워드 현재 구현 상태

```yaml
updated_at: 2026-08-05
current_planning_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_planning_count: 4_OF_10
latest_planning_status: MAIN_CANON_TARGET / NOT_IMPLEMENTED
최신 버티컬 슬라이스 구현: `NOT_STARTED`
product_code_authority: NONE
simulation: NOT_RUN
runtime: NOT_RUN
human_validation: HUMAN_QA_NOT_RUN
```

현재 시스템 연결 기준선은 `APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`다.

## 최신 구현 경계

```text
VERTICAL_SLICE_IMPLEMENTATION_NOT_STARTED
LATEST_AUTOMATED_CONTRACTS_NOT_RUN
HUMAN_QA_NOT_RUN
CORE_LOCK_NOT_ALLOWED
```

4/10 병종 역할·시너지·카운터는 문서 정본이며 다음은 아직 구현되지 않았다.

- 열 종 역할 재정의.
- 암살자·기병·비행병 역할 분리.
- 다섯 압력별 병종 대응 행위.
- 행동 기반 시너지.
- 전열/기동 병영 후보 가중.
- Tier별 역할 변화.
- Route·Layer·타기팅·AI.
- 병종 수치·확률·비용.

```text
PRODUCT_CODE = UNCHANGED
DATA_MIGRATION = NOT_AUTHORIZED
ART_ASSET_PRODUCTION = NOT_AUTHORIZED
```

`data/units/*.tres`는 현재 Legacy Prototype 증거이며 최신 병종 구현 권위가 아니다.

## 과거 자동 검증 증거

```text
LEGACY_C1_C2_C3_PROVEN
LEGACY_C1_ROULETTE_CORE_REMOTE_PROVEN
LEGACY_C2_BATTLE_OBJECTIVE_REMOTE_PROVEN
LEGACY_C3_AUTOMATED_CONTRACTS_PROVEN
```

C1 구현 검증 head: `19f1a4ff75ac393c09aff5d9c1154fed04ccc4f9`

C1 최종 검증 run: `29926598807`

C2 최종 검증 run: `29938742864`

이 C1·C2·C3 증거는 과거 룰렛·전투 목표·핵심 UX 계약 검증 사실만 보존하며 V2 구현 완료를 뜻하지 않는다. 최신 4/10 병종 기획이 제품에 구현됐다는 의미도 아니다.

## 구현 시작 전 필수 Gate

1. 5/10 전술스킬·마석 정본.
2. 건물+병종+전술 압력 대응 재검증.
3. 경제·수치 시뮬레이션.
4. 사용자 승인 Codex 구현 계획.
5. 제품 행동을 재현하는 RED 테스트.
6. 데이터 마이그레이션·롤백·수동 플레이 계획.

## 완료 이력 보존

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```

현재 구현 판정은 `VERTICAL_SLICE_NOT_IMPLEMENTED`다.