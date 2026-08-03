# 오멘워드 미확정 결정 목록

- 갱신일: 2026-08-04
- 현재 main: `RESOLVE_FROM_REPOSITORY_DEFAULT_BRANCH`
- 전체 시스템 정본: `docs/design/APPROVED_VERTICAL_SLICE_SYSTEM_CONTRACT_2026-07-27.md`
- 현재 Decision: `OMW-DEC-20260804-PLANNING-COMBAT-HUD-REEL-AND-BUILD-UX-V1`
- 운영 정책: `OMW-PROC-20260804-PLANNING-VISUALS-CODEX-IMPLEMENTATION-BOUNDARY-V1`
- 현재 Grill Me: `9/10`
- 제품 코드: `NOT_AUTHORIZED`
- 이미지 생성: `PAUSED_BY_USER`

## 1. 이번 Decision으로 해결된 항목

- 평상시 하단 기능을 `[룰렛][보관함][건설][전술스킬][벨루]`로 확정.
- 상시 상점 버튼 제거와 Stage 종료 정비시간 상인 방문.
- 평상시 핵심 자원을 골드·마석·배치 병력/병력 한도로 정리.
- 마석을 전술스킬 소비 자원으로 확정.
- 이동권을 평상시 HUD가 아니라 룰렛 정보 패널에서 `n/3`으로 표시.
- 토큰 초당 공급 표현 폐기와 현재 TokenSource·릴 구성 표시.
- 세로 릴 선택→위/아래 이동, 노출 행 선택→좌/우 가로 이동 흐름.
- 병종 Tier와 완성선 기반 보상 등급의 분리 설명.
- 건물별 지속 유지비 없음.
- 기본 건물 6종: 금고·농장·병영·방어탑·지휘소·마력탑.
- 농장을 병력 한도 확장 건물로 정리.
- 지휘소를 현재 MapRun 전체 아군 병력 전역 오라로 변경.
- 마력탑을 마석 수급·최대 보유량 강화 건물로 추가.
- 벨루를 우측 하단 상황 설명·간단 조언 역할로 확정.

## 2. 다음 최우선 사용자 Decision — 10/10

`OMW-DEC-20260804-PLANNING-ART-DIRECTION-AND-IMAGE-PROTOTYPE-BRIEF-V1`

결정 필요:

- 아군 청백금 성전 병력의 공통 실루엣·재질·색 규칙.
- 일반→엘리트→영웅→전설의 시각 성장 문법.
- 적 진영 보라·흑색 Veil 건물과 병력의 공통 형태 언어.
- 세 전선·본진·중간 거점·경합 지역·건설 노드의 정확한 이미지 문법.
- 금고·농장·병영·방어탑·지휘소·마력탑의 역할별 실루엣 구분.
- 룰렛 토큰과 실제 병종·건물의 대응 규칙.
- 벨루의 표정·말풍선·위험 우선순위 표현.
- 기존 생성 이미지를 정본이 아닌 참고로 분류하고 최종 Brief만 확정.
- 10/10 preflight·적대적 검토·merge readiness.

## 3. 10/10 이후 핵심 재미·콘텐츠 기획

아트 방향 이후 GPT가 우선 논의할 항목:

- 세 릴을 반복 설계하게 만드는 선택 압력과 보상.
- Stage마다 달라지는 세 전선 공세 패턴.
- Wave·Danger·Boss가 릴·건물·배치 선택을 어떻게 시험하는지.
- 6종 건물의 T2·T3 분기와 카운터 관계.
- 전술스킬과 마석 수급의 선택 압력.
- Stage 종료 상인의 재고·가격·이벤트 변주.
- 표준 병종·영웅의 역할과 성장.
- 첫 10~15분 사람 검증 시나리오.

## 4. 별도 후속 콘텐츠 Decision

- 마석 기본 축적량·최대치·마력탑 강화 폭.
- 전술스킬 목록·마석 비용·쿨다운·표현.
- 상인 이동권 재고·가격·추가 상품군.
- 농장·병력 한도의 정확한 성장 수치.
- 지휘소 돌격·수비 오라의 정확한 효과와 밸런스.
- 마력탑 T2·T3 수급형·저장형 분기.
- 벨루 대사 우선순위·반복 억제·접근성.

## 5. Codex에 위임된 구현 결정

아래는 Grill Me에서 구현 정본으로 고정하지 않는다.

```text
coordinate unit and numeric representation
fixed/variable tick implementation
state/schema/class/resource design
pathfinding, avoidance and collision algorithms
distance and targeting search implementation
camera transform, FOV, occlusion and smoothing
HUD scene and responsive layout implementation
input binding and animation implementation
canonical sort and serialization details
performance and test architecture
```

Codex의 선택이 핵심 재미·콘텐츠 역할·플레이어 경험이나 밸런스를 바꾸면 다시 기획 Gate로 돌아온다.

## 6. 계속 금지되는 항목

```text
PRODUCT_CODE = UNCHANGED
SIMULATION_TOOL_CODE = NOT_AUTHORIZED
IMAGE_ANIMATION_HX_PRODUCTION = PAUSED_BY_USER
TRUE_DAMAGE_EXECUTE_REVIVE = FORBIDDEN_CURRENT_SLICE
BALANCE_CONCLUSION = FORBIDDEN
SIMULATION = NOT_RUN
RUNTIME = NOT_RUN
HUMAN_QA = NOT_RUN
```

## 7. Merge Cadence

```text
CURRENT_COUNT = 9/10
NEXT_PREFLIGHT = AT_10_OF_10
EARLY_PREFLIGHT = only high-risk conflict / session boundary / large canon impact
```
