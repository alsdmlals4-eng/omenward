# Omenward Game Design

- Skill ID: `discipline.game-design`
- 공통 계약: `skills/SHARED_EXECUTION_CONTRACT.md`

## 사용 조건

핵심 컨셉·DDD·룰렛·전투·경제·병종·PoC·Vertical Slice를 설계·재조정할 때.

## 사용하지 않는 조건

확정 규칙을 바꾸지 않는 단순 문장 편집.

## 고유 책임

건물 구성→룰렛 확률→병력 획득→3라인 배치→거점·성문 공방의 코어를 보호하며 뾰족한 재미·제약·증거·품질 게이트를 관리한다.

## 입력

- 코어·승인 게임 규칙
- 대상 플레이어·제약
- 벤치마크·플레이테스트·텔레메트리
- PoC·구현 결과

## 절차

- Modes: `concept-frame → constrain → sharpen → structure → benchmark-decision → playtest-experiment → poc-contract → recalibrate → vertical-slice → balance-design`
- 대상 플레이어·핵심 행동·선택·피드백·판타지를 한 문장으로 고정한다.
- 요소를 AMPLIFY·SUPPORT·NEUTRAL·CONFLICT·UNPROVEN으로 정렬한다.
- DDD는 첫 의미 있는 보상·피드백 지연·보상 사다리·피로로 분석한다.
- 비교 근거는 ADOPT·ADAPT·AVOID·TEST·IGNORE로 결정한다.
- 가장 위험한 가설을 최소 PoC·플레이테스트로 검증한다.
- Vertical Slice는 대표 경험·품질·접근성·성능·파이프라인을 함께 증명한다.

## 출력

- 핵심 컨셉·뾰족한 재미
- 제약·SWOT·MDA/DDE/DDD 분석
- PoC·실험 계약
- 룰렛·전투·경제·밸런스 결정
- Vertical Slice gate

## 고유 검수

- 기능 복사·표본 편향·여러 변수 동시 실험을 피한다.
- DDD를 무의미한 자극이나 의학적 진단으로 사용하지 않는다.
- PoC·Vertical Slice 범위를 팽창시키지 않는다.
