# Skill 실행 검증 매트릭스

## 자동 검증

```bash
python tools/validate_skill_system.py
python -m unittest discover -s tests/python -v
```

## 현재 로컬 결과

- Validator: `PASSED`
- 테스트: `14/14 PASSED`
- 중복 ID 변조 차단: `PASSED`
- Registry–Schema 필드 계약: `PASSED`
- 의존성 우선 정렬·순환 방어: `PASSED`
- 미등록 수동 Skill 거부: `PASSED`
- 일반 요청 Specialist 과선택 방지: `PASSED`
- REVIEW 강제 스택: `PASSED`

## 라우팅 Smoke

| 요청 | 예상 Mode | 필수 Skill |
|---|---|---|
| PR 누락·중복 적대적 검토 | REVIEW | project-intake, validation-review, integration-review |
| 룰렛 확률 기획 | PLAN | project-intake, game-design |
| Godot 성능 버그 수정 | BUILD | project-intake, engineering |
| HUD UI 아트 시각 감사 | REVIEW | validation-review, integration-review, ui-art-audit |
| 수직 슬라이스 MVP 설계 | PLAN | game-design, engineering, production-pm 이후 vertical-slice |

## 증거 판정

- 로컬 독립 실행: `PROVEN` — 현재 파일 집합에 대한 Validator·14개 테스트
- GitHub Actions: PR 생성 전 `NOT_RUN`
- PR Workflow 성공 후: 원격 Linux 환경에서도 Skill 구조·Router `PROVEN`
- Godot 게임 기능: 이 Workflow의 증거 범위 밖
