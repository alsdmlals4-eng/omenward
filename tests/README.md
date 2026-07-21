# Omenward 검증 실행

저장소 루트에서 실행한다. Godot 실행 파일은 환경변수 `GODOT_BIN`으로 지정하며, Python은 활성 환경의 `python`을 사용한다. Godot import가 전역 클래스 캐시를 준비하므로 headless 검사보다 먼저 실행한다.

## PowerShell

```powershell
if (-not $env:GODOT_BIN) { throw "GODOT_BIN에 Godot 4.7 console 실행 파일 경로를 지정하세요." }
& $env:GODOT_BIN --headless --path . --editor --quit
Get-ChildItem tests/headless/*_test.gd | Sort-Object Name | ForEach-Object {
  & $env:GODOT_BIN --headless --path . -s ("res://tests/headless/" + $_.Name)
  if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}
& $env:GODOT_BIN --headless --path . --quit-after 1
python -m unittest discover -s tests/python -v
git diff --check
```

## Bash

```bash
: "${GODOT_BIN:?Set GODOT_BIN to a Godot 4.7 console executable}"
"$GODOT_BIN" --headless --path . --editor --quit
for test_file in $(find tests/headless -maxdepth 1 -name '*_test.gd' -print | sort); do
  "$GODOT_BIN" --headless --path . -s "res://$test_file"
done
"$GODOT_BIN" --headless --path . --quit-after 1
python -m unittest discover -s tests/python -v
git diff --check
```

문서 변경 뒤에는 Registry 기반 PDF·Manifest·Skill Map 재생성, 활성 Markdown 링크 검사, PDF 전 페이지 렌더를 추가한다. 1920×1080·1280×720 사람 플레이/시각 QA는 실행 증거가 생길 때까지 `NOT_RUN` 또는 `[미검증]`이다.
