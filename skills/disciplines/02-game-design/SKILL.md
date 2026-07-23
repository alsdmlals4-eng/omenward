# Omenward Game Design

- Skill ID: `discipline.game-design`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

핵심 컨셉·DDD·룰렛·전투·경제·병종·SWOT·VRIO·PoC·Vertical Slice를 설계·재조정할 때.

## 사용하지 않는 조건

확정 규칙을 바꾸지 않는 단순 문장 편집. 실제 사용자 증거 없이 코어 루프가 검증됐다고 승격하는 작업.

## 고유 책임

건물 구성→룰렛 확률→병력 획득→3라인 배치→거점·성문 공방의 코어를 보호하며 뾰족한 재미·제약·증거·품질 게이트를 관리한다.

## 입력

- 코어·승인 게임 규칙
- 대상 플레이어·제약
- 벤치마크·플레이테스트·텔레메트리
- PoC·구현 결과
- 현재 구현 상태와 미확정 결정

## 절차

- Modes: `concept-frame → constrain → sharpen → structure → benchmark-decision → playtest-experiment → poc-contract → recalibrate → vertical-slice → balance-design`
- 작업 단계는 `핵심 컨셉 → 제약·조건 → 뾰족한 재미 → 전체 요소 정돈 → PoC → 기획 재조정 → 프로덕션 준비`로 추적한다.
- 대상 플레이어·핵심 행동·선택·피드백·판타지를 한 문장으로 고정한다.
- 요소를 AMPLIFY·SUPPORT·NEUTRAL·CONFLICT·UNPROVEN으로 정렬한다.
- DDD는 첫 의미 있는 보상·피드백 지연·보상 사다리·피로로 분석한다.
- SWOT은 SO·WO·ST·WT 실행안으로, VRIO는 가치·희소성·모방 비용·조직화의 지속 우위 판정으로 변환한다.
- 비교 근거는 ADOPT·ADAPT·AVOID·TEST·IGNORE로 결정한다.
- 가장 위험한 가설을 최소 PoC·플레이테스트로 검증한다.
- PoC 뒤에는 규칙·정보·콘텐츠·기술 문제를 분리하고 가장 작은 재조정만 승인한다.
- Vertical Slice는 대표 경험·품질·접근성·성능·파이프라인을 함께 증명한다.
- 프로덕션 진입은 `discipline.production-pm`의 범위·의존성·위험·마일스톤과 `discipline.integration-review`의 무손실 검수를 통과한 뒤 판정한다.
- 첫 10~15분 사람 검증은 `docs/CORE_LOOP_HUMAN_PLAYTEST_PROTOCOL.md`와 `discipline.analytics-research`를 사용한다.

## 출력

- 핵심 컨셉·뾰족한 재미
- 제약·SWOT·VRIO·MDA/DDE/DDD 분석
- PoC·실험 계약
- 룰렛·전투·경제·밸런스 결정
- 재조정안과 보류 항목
- Vertical Slice·프로덕션 준비 gate

## 고유 검수

- 기능 복사·표본 편향·여러 변수 동시 실험을 피한다.
- DDD를 무의미한 자극이나 의학적 진단으로 사용하지 않는다.
- PoC·Vertical Slice 범위를 팽창시키지 않는다.
- 자동 계약, 플레이어 이해, 재미, 밸런스, 프로덕션 준비를 같은 상태로 합치지 않는다.
