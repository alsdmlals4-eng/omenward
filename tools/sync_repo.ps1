[CmdletBinding()]
param(
    [string]$Branch = "main"
)

$ErrorActionPreference = "Stop"
$repositoryRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repositoryRoot

if (-not (Test-Path -LiteralPath ".git")) {
    throw "Run this command from a standard OMENWARD Git checkout."
}

if (git status --porcelain) {
    throw "Local changes detected. Commit, stash, or discard them before synchronization."
}

$currentBranch = git branch --show-current
if ($currentBranch -ne $Branch) {
    throw "Synchronization only runs from '$Branch'; current branch is '$currentBranch'."
}

git fetch origin --prune
$remoteRef = "origin/$Branch"
git rev-parse --verify $remoteRef | Out-Null

git merge-base --is-ancestor HEAD $remoteRef
if ($LASTEXITCODE -ne 0) {
    throw "Local '$Branch' is not an ancestor of '$remoteRef'. Resolve the divergence manually."
}

git pull --ff-only origin main
Write-Output "Synchronized $(git rev-parse --short HEAD) from $remoteRef."
