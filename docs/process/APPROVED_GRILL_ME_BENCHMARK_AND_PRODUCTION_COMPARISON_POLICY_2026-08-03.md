# OMENWARD Grill Me 벤치마크·현업 비교 운영 정책

```yaml
process_id: OMW-PROC-20260803-GRILL-ME-BENCHMARK-PRODUCTION-COMPARISON-V1
approved_at: 2026-08-03 00:06 KST
approval: USER_DIRECT_OPERATING_INSTRUCTION
status: ACTIVE_STANDING_POLICY
scope: GRILL_ME_QUESTIONS_AND_APPROVED_PLANNING_WORK
applies_to: OMENWARD_PROJECT
product_code_authority: NONE
```

## 1. 목적

앞으로 OMENWARD의 Grill Me 질문과 승인 기획 작업은 프로젝트 내부 논리만으로 추천하지 않는다. 유사한 상용 게임·공개된 개발 원칙·현업 제작 관행을 함께 비교하여 왜곡·누락·과잉 범위를 발견하고, OMENWARD의 핵심 재미와 제작 조건에 맞는 권장안을 제시한다.

벤치마크는 기능 복제나 유명 게임 추종이 아니다.

```text
BENCHMARK
= 유사 문제를 어떻게 풀었는지 관찰
+ 성공 조건과 실패 경계 추출
+ OMENWARD 조건에 맞게 축소·변형
```

## 2. 모든 Grill Me 질문의 필수 구성

각 Grill Me 질문은 가능한 범위에서 다음을 포함한다.

1. **정본 근거**
   - 현재 Project Core, Decision Ledger, 분야별 APPROVED 문서, 실제 제품 상태를 먼저 확인한다.
2. **상용 게임 벤치마크**
   - 질문과 직접 관련된 2~4개 사례를 우선 비교한다.
   - 공식 게임 페이지·개발자 글·패치 노트·GDC 발표·공식 기술 문서를 우선한다.
3. **차이 분석**
   - 장르·조작 방식·전투 규모·카메라·세션 길이·경제 구조가 OMENWARD와 다른 점을 명시한다.
4. **현업 제작 비교**
   - 구현 복잡도, 데이터·AI·pathfinding·animation·VFX/SFX·UI·save/load·network/determinism·QA 의존성을 비교한다.
5. **적대적 검토**
   - 복제 시 발생할 파워 크리프, 가독성 저하, 대응 불가능성, 범위 팽창, 유지보수 비용을 공격한다.
6. **2~4개 선택지와 권장안**
   - 각 선택지의 플레이 가치·제작비·검증 난이도를 함께 비교한다.
   - 권장안은 핵심 재미 보존과 제작 효율의 균형을 이유로 설명한다.
7. **미확정 경계**
   - 정확 수치·자산·simulation·runtime·human QA를 근거 없이 완료로 표시하지 않는다.

## 3. 벤치마크 선정 기준

우선순위:

```text
공식 1차 자료
> 개발자 발표·패치 노트
> 검증 가능한 전문 분석
> 커뮤니티 사례
```

사례는 이름이 유명해서 선택하지 않는다. 다음 비교축 중 하나 이상이 직접 맞아야 한다.

- 동일한 플레이어 결정 문제.
- 동일한 전투 역할 또는 발동 조건.
- 유사한 자동전투·다수 유닛 환경.
- 유사한 자산 재사용·제작비 제약.
- 유사한 가독성·counterplay 문제.

비교 날짜와 출처를 기록한다. 최신 상태가 중요하면 작업 시점에 다시 확인한다.

## 4. 현업 비교 체크리스트

| 축 | 필수 질문 |
|---|---|
| 게임플레이 | 플레이어가 결과 원인을 이해하고 다음 선택을 개선할 수 있는가 |
| Counterplay | 상대·환경·자동전투 규칙이 위협을 완화하거나 피할 방법이 있는가 |
| 가독성 | trigger·대상·범위·지속시간·종료를 전투 중 구분할 수 있는가 |
| 파워 위계 | 일반·엘리트·영웅·전설과 다른 중요 사건의 시청각·전투 위계를 침범하지 않는가 |
| 데이터 | 표준 schema와 공통 resolver로 표현 가능한가 |
| AI | 새 전용 AI·독립 target selection·pathfinding이 필요한가 |
| Animation | 원본 리그·모션 재사용으로 가능한가 |
| VFX/SFX | 화면 노이즈와 저사양 비용을 포함해 예산을 통제할 수 있는가 |
| Save/Load | 중간 상태와 예약 이벤트를 안정적으로 직렬화할 수 있는가 |
| Determinism | 동일 저장 상태와 입력 순서에서 같은 결과가 나오는가 |
| QA | 단위 테스트·simulation·runtime·human usability를 분리해 검증 가능한가 |
| 유지보수 | 새 콘텐츠 추가 시 예외 분기가 누적되지 않는가 |

## 5. 권장안 제시 형식

```text
[정본 문제]
[외부 벤치마크 2~4개]
[OMENWARD와의 핵심 차이]
[선택지 A/B/C]
[현업 제작비·위험 비교]
[적대적 검토]
[권장안]
[승인 시 Decision ID·동기화 범위]
```

벤치마크가 현재 질문과 실질적으로 맞지 않으면 억지로 사례를 붙이지 않고 `DIRECT_COMPARABLE_NOT_FOUND`라고 명시한 뒤, 더 상위 수준의 설계 원칙이나 제작 패턴을 비교한다.

## 6. 금지

- 유명 게임의 스킬명·수치·연출을 그대로 복사하는 것.
- 장르와 전투 규모 차이를 무시하고 성공 사례라고 단정하는 것.
- 커뮤니티 의견만으로 현재 상용 게임의 사실을 확정하는 것.
- 벤치마크를 근거로 Project Core를 자동 변경하는 것.
- 구현비·검증비를 숨기고 플레이 아이디어만 추천하는 것.
- 출처 확인 없이 최신 패치·현업 표준이라고 주장하는 것.
- 사용자의 승인 없이 제품 코드·데이터·Scene·Resource를 변경하는 것.

## 7. GitHub·Sheet 반영

중요한 승인 결과는 기존 운영 계약에 따라 다음을 수행한다.

```text
user approval
→ stable Decision ID
→ GitHub authority docs and ledger
→ connected Google Sheet with same Decision ID
→ bounded read-back
→ exact-head CI and preflight evidence
```

이 정책 자체는 Grill Me 제품 결정 카운터를 증가시키지 않는다. 제품 기획 Decision만 기존 10건 카운터에 포함한다.

## 8. 현재 적용

이 정책을 처음 적용한 제품 Decision:

`OMW-DEC-20260803-GAMEPLAY-HERO-FIRST-FIVE-UNIQUE-SKILL-2-CONCEPTS-V1`

비교 사례는 방벽 역할, 광역 화살 사건, 체력 하한, 지연 메테오, 종속 분신과 전투 가독성·counterplay 원칙을 포함한다.
