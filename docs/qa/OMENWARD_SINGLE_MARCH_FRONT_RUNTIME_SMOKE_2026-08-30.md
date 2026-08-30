# OMENWARD 단일 행군 전선 런타임 스모크 — 2026-08-30

```yaml
status: RUNTIME_TECHNICAL_SMOKE_PASS__HUMAN_USABILITY_NOT_RUN
scope: OMW-PLAN-20260830-SINGLE-MARCH-FRONT-THREE-TAB-01
engine: Godot 4.7.2 stable
execution: local editor runtime via project-owned Hera session
```

## 관찰한 흐름

1. `내정 / 룰렛 / 전선` 세 탭이 보이는 Run Command를 열었다.
2. 튜토리얼의 읽기 전용 전역 로스터에 사전 구축된 `일반병 병영` 하나가 보이고, 룰렛의 `warrior -> shield_guard` TokenSource가 실제로 노출되는 것을 확인했다.
3. `룰렛 → 징조륜 시작 → 결과 확인 → 결과 확정 → 전투 시작`을 실제 입력으로 완료했다.
4. 전투 중 지도는 Ward Citadel에서 Veil Citadel까지 하나의 넓은 연결 경로, Ward Forward/Clash/Veil Forward의 세 점령 앵커, 고정 탑 한 개만 표시했다. 지도 위 별도 건물 또는 건설 노드는 없었다.
5. 적 웨이브가 `front` 하나에 생성됐으며 Shield Guard, Archer, Assassin 역할이 단일 경로의 읽기 쉬운 대형 승인 아트 마커와 역할명으로 투영되는 것을 확인했다. 같은 위치의 유닛은 수평·수직 formation offset으로 겹치지 않도록 배치했다.

## 캡처와 진단

- 최종 로컬 런타임 캡처: `C:\Users\user\AppData\Local\Temp\omenward-single-front-battle-readable-20260830-v3.png`.
- 중첩 보정 전의 다중 적 웨이브 관찰 캡처: `C:\Users\user\AppData\Local\Temp\omenward-single-front-battle-readable-20260830-v2.png`.
- 런타임 diagnostics: `error_count = 0`, `warning_count = 0`.

로컬 Temp 캡처는 재현을 위한 관찰 증거일 뿐 release asset이나 repository artifact가 아니다. 단일 전선 지형 후보 `OMW-IMG-20260830-SINGLE-MARCH-FRONT-TERRAIN-V1`은 여전히 `GENERATED_CANDIDATE__USER_REVIEW_PENDING`이며 이 런타임에 바인딩하지 않았다.

## 증거 한계

- 이 스모크는 기술적 실행·기본 가독성 관찰이다. 사람 UX, 플레이 재미, 장시간 세션, 밸런스, 플랫폼/출시 검증은 실행하지 않았다.
- headless contract 검사는 별도 증거이며, 그 종료 단계의 RID/ObjectDB/resource teardown 경고는 이 런타임 diagnostics PASS와 별도로 남아 있다.
