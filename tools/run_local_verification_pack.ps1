[CmdletBinding()]
param(
    [string]$OutputDirectory = "artifacts/local-verification"
)

$ErrorActionPreference = "Stop"
$RepositoryRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
Set-Location $RepositoryRoot
$ExpectedHead = (git rev-parse HEAD).Trim()
if ($LASTEXITCODE -ne 0) { throw "git rev-parse HEAD failed" }

$Runtimes = @(
    @{ Id = "windows-py311"; Launcher = "py -3.11"; Args = @("-3.11") },
    @{ Id = "windows-py312"; Launcher = "py -3.12"; Args = @("-3.12") },
    @{ Id = "windows-py313"; Launcher = "py -3.13"; Args = @("-3.13") }
)

foreach ($Runtime in $Runtimes) {
    Write-Host ("Running {0} with {1}" -f $Runtime.Id, $Runtime.Launcher)
    $Receipt = Join-Path $OutputDirectory ($Runtime.Id + ".json")
    & py @($Runtime.Args) tools/run_local_verification_pack.py `
        --environment-id $Runtime.Id `
        --expected-head $ExpectedHead `
        --output $Receipt
    if ($LASTEXITCODE -ne 0) {
        throw ("Local verification failed for {0}" -f $Runtime.Id)
    }
}

Write-Host "Windows Python 3.11/3.12/3.13 local verification receipts are complete."
