[CmdletBinding()]
param(
    [switch]$Shallow
)

$ErrorActionPreference = 'Stop'
$repositoryRoot = Split-Path -Parent $PSScriptRoot

function Invoke-Git {
    param([Parameter(Mandatory)][string[]]$Arguments)

    & git @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "git $($Arguments -join ' ') failed with exit code $LASTEXITCODE"
    }
}

Push-Location $repositoryRoot
try {
    Invoke-Git @('-c', 'core.longpaths=true', 'submodule', 'sync', '--recursive')

    $updateArguments = @(
        '-c', 'core.longpaths=true',
        '-c', 'http.version=HTTP/1.1',
        'submodule', 'update', '--init', '--recursive'
    )

    if ($Shallow) {
        $updateArguments += @('--depth', '1')
    }

    Invoke-Git $updateArguments

    $verifyScript = Join-Path $PSScriptRoot 'verify-submodules.ps1'
    & $verifyScript -AllowShallow:$Shallow
}
finally {
    Pop-Location
}
