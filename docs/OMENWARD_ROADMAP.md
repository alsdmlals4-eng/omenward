# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
current_count: 5_OF_10
next_decision: OMW-DEC-20260805-PLANNING-STAGE-END-MERCHANT-V1
product_code_authority: NONE
```

## Planning Batch

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
[완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
[완료 3/10] 건물 6종 분기·카운터
[완료 4/10] 병종 역할·시너지·카운터
[현행 5/10] 전술스킬·마력
[다음 6/10] Stage 종료 상인
[7/10] 첫 10~15분 흐름
[8/10] Hero·Legendary 재조정
[9/10] Meta·Hub 재조정
[10/10] 전체 Run 콘텐츠·UX·아트 종합 검토
```

## 5/10 전술스킬·마력 결과

- 마력탑은 MapRun당 하나이며 분기 없는 `T1 → T2 → T3`다.
- Tier가 높아질수록 초당 마력 수급량과 연구 가능한 전술 Tier가 증가한다.
- 연구 비용은 골드+시간이며 동시에 하나만 진행한다.
- 연구 완료 스킬은 현재 MapRun 동안 해금된다.
- Stage 전 편성 없이 해금된 모든 전술을 사용한다.
- 플레이어가 수동 시전하고 유효 확정 시 마력을 소비한다.
- 전술 기준선은 T1 4종·T2 3종·T3 3종이다.
- 새 MapRun에서 마력탑 Tier·연구·해금·보유 마력을 초기화한다.
- 전술은 병종·건물의 지속 역할을 대체하지 않는다.
- 정확한 수급량·비용·쿨다운·범위는 시뮬레이션 전 미확정이다.

## 6/10 Stage 종료 상인 목표

- Stage 결과 정산→정비시간→상인→다음 Stage 확정 흐름.
- 방문별 유한 재고와 구매 제한.
- 골드의 건설·룰렛·연구·상인 기회비용.
- 이동권·회복·연구 보조·병종 관련 상품의 역할.
- 마지막 Stage 이후 최종 정산 예외.

## 구현 순서

```text
5/10 전술·마력 정본
→ 6/10 Stage 종료 상인
→ 첫 10~15분 흐름
→ 경제·수치 시뮬레이션
→ 별도 Codex 구현 계획
→ 제품 RED 테스트
→ 최소 구현
→ 런타임·사람 QA
```

제품 코드·Scene·Resource·게임 데이터·실제 아트 자산은 별도 승인 전 변경하지 않는다.

제품 구현: `NOT_STARTED`

## TDD 증거

- 5/10 RED: Validate Project Core Documentation run 954.
- 기존 45개 문서·CI 계약은 통과하고 새 5/10 계약만 실패했다.
- GREEN/REFACTOR: 최종 exact HEAD에서 fresh 검증 후 기록한다.

## Legacy 자동 검증 증거

기존 기술 기준선·C1·C2·C3 자동 증거 확보

C1 승인 룰렛 핵심 계약 원격 검증·병합 완료

상태: **REMOTE_PROVEN**

위 증거는 과거 계약 검증만 의미하며 최신 5/10 기획의 제품 구현을 의미하지 않는다.

## 완료 이력

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
4_OF_10
LEGACY_C1_C2_C3_PROVEN
```
