# Adoption guide

## Who should adopt this?

This preference is useful for:

- desktop app developers
- app framework maintainers
- theme-library maintainers
- Electron/Tauri developers
- .NET/WPF/WinUI developers
- Qt developers
- Flutter desktop developers
- terminal and CLI tool developers
- browser extension authors

## Minimum viable support

An app can support this preference with three steps:

1. Detect whether the app is currently using dark mode.
2. Read `PreferTrueBlackInDarkMode`.
3. If both are true, use a true-black or OLED-friendly dark variant.

Pseudo-code:

```text
if app_is_dark_mode and prefer_true_black_in_dark_mode:
    use_true_black_dark_theme()
else:
    use_normal_theme()
```

## Windows support

Read:

```text
HKEY_CURRENT_USER\Software\OpenAppearance\Preferences
PreferTrueBlackInDarkMode
```

Treat only `REG_DWORD 1` as enabled.

Treat missing, invalid, or `0` as no special preference.

## Cross-platform fallback

Read:

```text
%APPDATA%\OpenAppearance\preferences.json
$XDG_CONFIG_HOME/openappearance/preferences.json
~/Library/Application Support/OpenAppearance/preferences.json
```

Expected JSON:

```json
{
  "schemaVersion": 1,
  "preferTrueBlackInDarkMode": true
}
```

## Environment variable fallback

For command-line tools:

```text
OPEN_APPEARANCE_PREFER_TRUE_BLACK_IN_DARK_MODE=1
```

Accepted true values:

```text
1
true
```

Accepted false values:

```text
0
false
missing
```

## Recommended priority

Use this priority order:

1. Accessibility and forced-color modes
2. Explicit in-app user theme settings
3. Operating-system light/dark mode
4. `PreferTrueBlackInDarkMode`
5. Application default styling

## User-facing setting

If your app already has a theme settings page, consider adding:

```text
Prefer true black in dark mode
```

Description:

```text
Use pure black or OLED-friendly surfaces when dark mode is enabled.
```

Avoid:

```text
Force OLED mode
```

because the preference should not force dark mode and should not imply hardware detection.

## Suggested color approach

You do not need to make every dark surface `#000000`.

Good default approach:

- Main app background: `#000000`
- Navigation/sidebar: `#000000` or near-black
- Cards/panels: near-black if needed
- Inputs/buttons: near-black if needed
- Borders/dividers: subtle but visible
- Text/icons/focus states: readable and accessible
- Media/documents/charts/maps: preserve content accuracy

## What not to do

Do not:

- Force dark mode when the app is light.
- Override high-contrast or forced-color modes.
- Use the preference for analytics or profiling.
- Assume the display is OLED.
- Break readability just to use pure black everywhere.
- Change documents, images, videos, design previews, or charts where color accuracy matters.

## Pull request template for other projects

```markdown
Hi! Would you consider supporting `PreferTrueBlackInDarkMode` from Open Appearance Preferences?

It is a tiny optional preference meaning:

> When the app is already using dark mode, prefer true-black or OLED-friendly dark surfaces where practical.

It does not force dark mode and should not override accessibility settings.

Spec:
https://github.com/YOUR-USER/open-appearance-preferences

Minimum support would be:
- read the Windows registry value or JSON fallback
- if dark mode is already active and the preference is enabled, use the app's pure-black dark variant if available

Thanks!
```
