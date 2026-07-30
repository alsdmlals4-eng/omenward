# 오멘워드 패배·재시도·checkpoint·메타 경량 벤치마킹

- 작성일: `2026-07-31`
- 상태: `BENCHMARK_COMPLETE / EVIDENCE_ONLY`
- 적용 원칙: `docs/operations/BENCHMARK_FIRST_PLANNING_RULE_2026-07-31.md`
- 제품 구현 권한: `NONE`

## 1. 조사 질문

35분 내외의 20 Stage MapRun에서 패배 긴장감을 유지하면서도, 후반 실패로 인한 피로를 줄이는 재시도 구조는 무엇인가?

## 2. 선별 사례

### Dead Cells

- 공식 소개는 `permadeath`, `No checkpoints`, `Kill, die, learn, repeat`를 전면에 둔다.
- 추출 원칙: 기본 패배는 런 종료로 읽혀야 하며, 반복 학습의 긴장감을 무상 재시도로 제거하지 않는다.

### Hades

- 공식 소개와 개발 자료는 반복 패배를 지식·서사·영구 성장으로 환류시키고, God Mode와 영구 진행으로 난이도 접근성을 조정한다.
- 추출 원칙: 패배 뒤에도 기록·해금·서사 같은 지속 진전이 있어야 하지만, 현재 런의 경제와 전투 상태가 그대로 영구 보존되어서는 안 된다.

### Returnal

- 공식 PlayStation 자료는 죽을 때 기본적으로 순환을 다시 시작한다고 설명한다.
- Reconstructor는 자원을 투입해 한 번 현재 주기의 진행을 잃지 않고 부활하는 선택형 장치로 소개된다.
- 추출 원칙: 재시도는 자동 기본권이 아니라 희소 자원을 미리 또는 패배 시점에 교환하는 보험이어야 한다.

## 3. 오멘워드 적용 원칙

1. 본진 HP 0은 기본적으로 MapRun 패배다.
2. 무료 무제한 재시도는 제품 기본 규칙으로 두지 않는다.
3. 영구재화 소모 재시도는 패배 종료의 선택형 예외다.
4. 재시도는 같은 실패 문제를 다시 풀도록 동일 Stage·동일 공세·동일 RNG 계보를 유지하는 방향이 적합하다.
5. 현재 런 골드·식량·무료 회전은 재시도 비용으로 대체하지 않는다.
6. 영구재화 소모와 checkpoint 복원은 한 거래로 원자 처리해야 한다.
7. 개발·플레이테스트 무료 재시도는 제품 규칙·메타 보상·기록에서 분리한다.
8. 재시도 횟수, 정확 비용, 막별 가중, 획득량은 경제 시뮬레이션 전 확정하지 않는다.

## 4. 설계 위험

- 비용이 낮으면 패배가 단순한 추가 생명으로 변한다.
- 비용이 높으면 후반 피로 완화 기능이 사실상 사용 불가가 된다.
- 재시도 때 seed나 미션 후보가 바뀌면 재굴림 수단이 된다.
- 실패 Stage에서 얻은 영구재화를 즉시 비용으로 쓸 수 있으면 자기 충당 루프가 생길 수 있다.
- 차감 뒤 checkpoint 로드 실패 시 재화 손실이 발생하지 않도록 거래 복구가 필요하다.

## 5. 현재 판정

```text
DEFAULT_DEFEAT_ENDS_RUN: RECOMMENDED
PERMANENT_CURRENCY_RETRY: USER_APPROVED_PRINCIPLE
EXACT_RETRY_LIMIT: PENDING
EXACT_RETRY_COST: PENDING
CHECKPOINT_RESTORE_FIELDS: PENDING
META_REWARD_FORMULA: PENDING
```

이 문서는 벤치마킹 근거이며 단독 제품 정본이 아니다.
