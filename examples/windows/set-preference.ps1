param(
    [Parameter(Mandatory = $true)]
    [bool]$Enabled
)

$Path = "HKCU:\Software\OpenAppearance\Preferences"

if (-not (Test-Path $Path)) {
    New-Item -Path $Path -Force | Out-Null
}

New-ItemProperty -Path $Path -Name "SchemaVersion" -Value 1 -PropertyType DWord -Force | Out-Null
New-ItemProperty -Path $Path -Name "PreferTrueBlackInDarkMode" -Value ([int]$Enabled) -PropertyType DWord -Force | Out-Null

if ($Enabled) {
    Write-Output "PreferTrueBlackInDarkMode enabled."
}
else {
    Write-Output "PreferTrueBlackInDarkMode disabled."
}
