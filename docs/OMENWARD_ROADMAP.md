# [현행] 오멘워드 로드맵

```yaml
updated_at: 2026-08-05
current_decision: OMW-DEC-20260805-PLANNING-TROOP-ROLES-SYNERGIES-AND-COUNTERS-V1
current_count: 4_OF_10
next_decision: OMW-DEC-20260805-PLANNING-TACTICAL-SKILLS-AND-MANA-V1
product_code_authority: NONE
```

## Planning Batch

```text
[완료 1/10] 핵심 재미·콘텐츠 가드레일
[완료 2/10] Stage·Wave·Danger·Boss 압력 매트릭스
[완료 3/10] 건물 6종 T2/T3 분기·카운터
[현행 4/10] 병종 역할·시너지·카운터
[다음 5/10] 전술스킬·마석
[6/10] Stage 종료 상인
[7/10] 첫 10~15분 흐름
[8/10] Hero·Legendary 재조정
[9/10] Meta·Hub 재조정
[10/10] 전체 Run 콘텐츠·UX·아트 종합 검토
```

## 4/10 병종 결과

- 열 종 기준선: 방패수호병·대검병·창병·궁수·마도사·사제·암살자·기병·비행병·거인.
- 병종 수는 불변 조건이 아니며 역할 공백·중복·제작비 근거로 별도 승인 후 증감 가능.
- 다섯 압력 각각에 최소 두 병종 대응 경로.
- 시너지는 전장 행동 연결이며 단순 세트 보너스는 금지.
- 병영은 전열/기동 후보 가중을 바꾸되 반대 계열을 삭제하지 않음.
- T3 병종 룰렛 토큰 금지.
- 정확한 수치·AI·가중치는 시뮬레이션 전 미확정.

## 5/10 전술스킬·마석 목표

- 병종·건물로 닫히지 않은 FLYING·SIEGE 대응 보완.
- 마석 수급·저장·사용 시점과 마력탑 분기 연결.
- 자동 시전이 아닌 플레이어 의도 기반 사용.
- 병종 역할을 대체하지 않는 전술적 시간 창 제공.
- 각 압력의 최소 두 대응 경로 재검증.

## 구현 순서

```text
4/10 병종 정본
→ 5/10 전술 정본
→ 건물+병종+전술 압력 대응 재검증
→ 경제·수치 시뮬레이션
→ 첫 10~15분 흐름
→ 별도 Codex 구현 계획
→ 제품 RED 테스트
→ 최소 구현
→ 런타임·사람 QA
```

제품 코드·Scene·Resource·병종 `.tres`·실제 아트 자산은 별도 승인 전 변경하지 않는다.

## TDD 증거

- 4/10 RED: Validate Project Core Documentation run 922.
- GREEN/REFACTOR: 현재 PR exact head에서 fresh 검증 후 기록.

## 완료 이력 보존

```text
OMW-DEC-20260805-PLANNING-SIX-BUILDING-T2-T3-BRANCHES-AND-COUNTERS-V1
3_OF_10
```