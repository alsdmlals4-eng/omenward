# Goal 0001 — Engine Selection and Phase 0 Bootstrap

> 상태: **완료 — Phase 0 구현·검증 완료 / 수직 슬라이스는 별도 승인 필요**

## 완료 결과

- Godot 4.7.1 Standard x86_64와 Compatibility renderer를 선택했다.
- 1920×1080 출력, 960×540 논리 해상도, viewport/keep/integer scaling을 설정했다.
- AutoLoad 없이 `Main → GameSession → core services` 소유 구조를 구현했다.
- 공용 `UnitArchetypeProfile` 10종, Tier·Rank·Attack·AnimationContract·FactionVisual·Battlefield·Boss 최소 Resource 계약을 구현했다.
- 적군 전용 UnitProfile·Unit Scene·전투 데이터·AnimationContract를 만들지 않았다.
- 결정론 seed·RNG·StageManifest·입력 로그 경계와 headless 계약 검사를 구현했다.

## 검증 근거

- `tests/headless/phase_0_contract_test.gd`
- `docs/PHASE_0_VALIDATION.md`
- `scenes/main/main.tscn`

## 제외된 범위

- 실제 전투, 이동, 타기팅, 공격, 룰렛, 건설, 점령, 성문, 웨이브.
- 최종 스프라이트·애니메이션·VFX·오디오.
- 적군 전용 병종 데이터와 별도 전투 Scene.

## 다음 단계

Issue #32와 Goal 0002의 Plan Mode 제안·사용자 승인을 거친 뒤에만 3라인 수직 슬라이스 구현을 시작한다.
