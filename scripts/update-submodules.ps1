[CmdletBinding(SupportsShouldProcess)]
param()

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
    if (-not $PSCmdlet.ShouldProcess('all configured upstream submodules', 'Fetch remote branches and update gitlinks')) {
        return
    }

    Invoke-Git @('-c', 'core.longpaths=true', 'submodule', 'sync', '--recursive')
    Invoke-Git @(
        '-c', 'core.longpaths=true',
        '-c', 'http.version=HTTP/1.1',
        'submodule', 'update', '--init', '--recursive', '--remote'
    )

    & (Join-Path $PSScriptRoot 'verify-submodules.ps1') -AllowGitlinkChanges

    Write-Host 'Review the changed gitlinks and upstream release notes before committing.'
}
finally {
    Pop-Location
}
