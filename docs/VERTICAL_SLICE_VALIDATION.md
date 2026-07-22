# Vertical Slice Validation

## Automated

Godot 4.7.1 Standard editor binary로 저장소 루트에서 실행한다.

```powershell
Get-ChildItem tests/headless/*_test.gd | ForEach-Object { & Godot_v4.7.1-stable_win64_console.exe --headless --path . -s ("res://tests/headless/" + $_.Name) }
Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64_console.exe --headless --path . --quit-after 1
python tools/validate_project_core_docs.py
python tools/validate_c1_roulette.py
python tools/validate_c2_battle_objective.py
python tools/validate_c2_battle_objective.py
python -m unittest discover -s tests/python -v
git diff --check
```

영구 `Validate Core Contracts` Workflow가 다음을 실행한다.

- Ubuntu/Windows × Python 3.12/3.13.
- C1·C2·프로젝트 코어·Skill Validator.
- 전체 Python mutation tests.
- Godot 4.7.1 editor import.
- 모든 `tests/headless/*_test.gd`.
- runtime smoke.
- whitespace와 구형 활성 참조·깨진 링크 검사.

## Current automated scope

- 공용 10병종·양 진영 데이터와 점령력·구조물 태그.
- C1 중앙 판정·등급·금화·전설 제한·보관·배치.
- C2 같은 라인 목적 이동, 접전지·거점 점령·교착, 건물 효과·경제 전환.
- 라인별 성문·본진 공격, 자연 승리·패배, W15 전설 보스 승리.
- 암살자 같은 라인 우회와 점령력 0.
- 결정론적 snapshot·input log.
- 활성 문서의 구형 현재 상태·실행 입력·깨진 링크.

## Manual QA still required

1. 튜토리얼과 정규 스테이지를 1920×1080에서 실행한다.
2. 병영 건설→룰렛→결과 보관→라인 배치→접전지→중간거점→성문→결과를 확인한다.
3. 1280×720에서 보드·등급·보관·세 라인·목적 상태가 읽히는지 확인한다.
4. 이동권·럭키는 C1U 결정 전 최종 동작으로 판정하지 않는다.
5. W1~W20 연속 플레이, 10~15분 재미·학습, 밸런스·성능은 별도 실행한다.
