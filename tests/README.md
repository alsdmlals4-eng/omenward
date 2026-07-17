# 오멘워드 테스트 실행

- 책임 상태 문서: [`docs/planning/05_QA_PM_PLAN.md`](../docs/planning/05_QA_PM_PLAN.md)
- 현재 자동 기준선: headless 6종, editor import, runtime smoke
- 수동 해상도 QA: 1920×1080·1280×720 모두 미실행

PowerShell에서 저장소 루트와 Godot 4.7.1 실행 파일을 기준으로 실행한다.

```powershell
$Godot = "C:\path\to\Godot_v4.7.1-stable_win64.exe"

& $Godot --headless --editor --path . --quit
if ($LASTEXITCODE -ne 0) { throw "Editor import failed" }

Get-ChildItem tests/headless/*_test.gd | ForEach-Object {
  & $Godot --headless --path . --script $_.FullName
  if ($LASTEXITCODE -ne 0) { throw "Headless test failed: $($_.Name)" }
}

& $Godot --headless --path . --quit-after 1
if ($LASTEXITCODE -ne 0) { throw "Runtime smoke failed" }

powershell -ExecutionPolicy Bypass -File tools/validate_documentation.ps1
git diff --check
```

테스트 실패 시 파일명, 명령, 커밋, 기대 결과, 실제 결과와 재현 여부를 기록한다. 일부 테스트만 통과한 결과를 전체 기준선 통과로 보고하지 않는다.

새 체크아웃은 Godot 전역 클래스 캐시가 없으므로 editor import를 먼저 실행한다. 2026-07-17 기준 위 순서로 editor import, headless 6종, runtime smoke가 모두 exit 0으로 통과했다.
