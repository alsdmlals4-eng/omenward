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
python tools/validate_c3_core_ux.py
python -m unittest discover -s tests/python -v
git diff --check
```

영구 `Validate Core Contracts` Workflow가 다음을 실행한다.

- Ubuntu/Windows × Python 3.12/3.13.
- C1·C2·C3·프로젝트 코어·Skill Validator.
- 전체 Python mutation tests.
- Godot 4.7.1 editor import를 120초 상한으로 실행.
- 모든 `tests/headless/*_test.gd`를 파일별 60초 상한으로 실행.
- runtime smoke를 60초 상한으로 실행.
- 임시 C3 수리·진단 파일의 재유입 거부.
- whitespace와 구형 활성 참조·깨진 링크 검사.

## Current automated scope

- 공용 10병종·양 진영 데이터와 점령력·구조물·전술 표시 태그.
- C1 중앙 판정·등급·금화·전설 제한·보관·배치.
- C2 같은 라인 목적 이동, 접전지·거점 점령·교착, 건물 효과·경제 전환.
- 라인별 성문·본진 공격, 자연 승리·패배, W15 전설 보스 승리.
- C3 건설 전 확률, 토큰 출처, 단계형 징조, 사거리·대상·상성, 웨이브 원인, 건설 비교.
- C3 금화 부족·점령/교착·빈 토큰·대상 없음·미완료 웨이브 경계와 snapshot 결정론.
- C3 핵심 의존 스크립트의 직접 headless 인스턴스화와 허위 성공 방지.
- 암살자 같은 라인 우회와 점령력 0.
- 결정론적 snapshot·input log.
- 활성 문서의 구형 현재 상태·실행 입력·깨진 링크.

## Manual QA still required

1. 튜토리얼과 정규 스테이지를 1920×1080에서 실행한다.
2. 병영 건설→확률 변화·토큰 출처→룰렛→결과 보관→라인 배치→접전지→중간거점→성문→웨이브 원인 보고를 확인한다.
3. 1280×720에서 보드·등급·보관·세 라인·징조·사거리/대상·건설 비교·목적 상태가 읽히는지 확인한다.
4. 텍스트 중심 C3 PoC의 겹침, 폰트 크기, 색상 의존, 정보 밀도와 전장 가림을 확인한다.
5. 이동권·럭키는 C1U 결정 전 최종 동작으로 판정하지 않는다.
6. W1~W20 연속 플레이, 10~15분 재미·학습, 밸런스·성능은 별도 실행한다.
