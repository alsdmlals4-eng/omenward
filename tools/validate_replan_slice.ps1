param([Parameter(Mandatory = $true)][string]$Godot)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
foreach ($testScript in @('tests/replan_slice_test.gd', 'tests/replan_screen_test.gd')) {
    & $Godot --headless --path $projectRoot --script $testScript
    if ($LASTEXITCODE -ne 0) { throw "Replan verification failed: $testScript ($LASTEXITCODE)" }
}
& $Godot --headless --path $projectRoot --quit-after 10
if ($LASTEXITCODE -ne 0) { throw 'Default scene smoke failed' }
Write-Output 'REPLAN_LOCAL_GATE_PASS (model + UI/save + default scene; not full-project/Human/CI approval)'
