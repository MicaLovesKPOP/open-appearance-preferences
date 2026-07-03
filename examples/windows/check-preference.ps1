$Path = "HKCU:\Software\OpenAppearance\Preferences"
$Name = "PreferTrueBlackInDarkMode"

try {
    $Value = Get-ItemPropertyValue -Path $Path -Name $Name -ErrorAction Stop
    if ($Value -eq 1) {
        Write-Output "PreferTrueBlackInDarkMode is enabled."
        exit 0
    }

    Write-Output "PreferTrueBlackInDarkMode is not enabled."
    exit 1
}
catch {
    Write-Output "PreferTrueBlackInDarkMode is not set."
    exit 1
}
