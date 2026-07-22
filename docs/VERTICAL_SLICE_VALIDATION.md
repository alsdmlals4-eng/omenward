# Vertical Slice Validation

## Automated

Godot 4.7.1 Standard editor binary로 저장소 루트에서 실행한다.

```powershell
Get-ChildItem tests/headless/*_test.gd | ForEach-Object { & Godot_v4.7.1-stable_win64_console.exe --headless --path . -s ("res://tests/headless/" + $_.Name) }
Godot_v4.7.1-stable_win64_console.exe --headless --path . --editor --quit
Godot_v4.7.1-stable_win64_console.exe --headless --path . --quit-after 1
python tools/validate_project_core_docs.py
python tools/validate_c1_roulette.py
python -m unittest discover -s tests/python -v
git diff --check
```

GitHub Actions의 `Validate C1 Roulette Contract`가 Linux Godot runtime과 Ubuntu/Windows Python 계약을 재검증한다.

현재 자동 범위:

- 공용 병종·양 진영 데이터.
- 3라인·성문·거점·경제·건설·웨이브·암살자 우회.
- C1 중앙 판정·8개 완성선·등급·금화·전설 제한·결과 보관·배치.
- 구형 활성 파일 참조와 깨진 내부 링크.

## Manual QA still required

1. 튜토리얼과 정규 스테이지를 실행한다.
2. 1920×1080에서 병영 건설→룰렛→결과 보관→라인 배치를 확인한다.
3. 1280×720에서 보드·등급·보관 상태와 세 라인이 읽히는지 확인한다.
4. 이동권·럭키는 C1U 결정 전 최종 동작으로 판정하지 않는다.
5. W1~W20 연속 플레이와 재미·밸런스는 C2 이후 별도 실행한다.
