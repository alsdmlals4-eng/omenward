# [승인] OMENWARD Godot CSV import artifact hygiene

```yaml
updated_at: 2026-08-09
decision_id: OMW-DEC-20260809-TOOLING-GODOT-CSV-IMPORT-ARTIFACT-HYGIENE-V1
baseline_main: 5df41ec281e76b0226eb6e9586788652d0cb782c
trigger: USER_CONFIRMED_LOCAL_GODOT_HIGODOT_NORMAL_OPERATION
scope: GENERATED_IMPORT_ARTIFACT_RECOVERY_AND_RECURRENCE_PREVENTION
product_mutation: NONE
```

## 결론

Godot 4.7.1 local import가 `docs/analysis/barracks_simulation/*.csv`를 translation CSV로 인식해 `.csv.import` 및 `.translation` 생성물을 main에 추적시켰다. `41c48182...` 대비 `5df41ec2...`의 추가 변경은 해당 생성물 14개뿐이며 병영 runtime 제품 코드는 변경되지 않았다.

이 Gate는 원본 CSV/JSON/runner를 유지하고 생성된 import/translation sidecar만 제거한다. 재발 방지를 위해 아래 경로만 `.gitignore`에 추가한다.

```text
docs/analysis/barracks_simulation/*.csv.import
docs/analysis/barracks_simulation/*.translation
```

`*.csv` 전체를 무시하지 않는다. canonical simulation CSV는 계속 추적한다.

## 보호 경계

- `scripts/`, `data/`, `scenes/`, `assets/`, `project.godot`, `addons/` 변경 금지.
- 10k/2k canonical CSV 내용 변경 금지.
- final functional-value index/vector 선택 금지.
- 이 hygiene Gate는 `BARRACKS_ROLE_OUTPUT_RUNTIME_IMPLEMENTATION_REQUIRED`를 닫지 않는다.
- 사용자 확인으로 local Godot/HiGodot availability는 `USER_CONFIRMED_OPERATIONAL`로 취급하되, 실제 role-output 구현 Green/Hera QA는 별도 실행 증거가 필요하다.
