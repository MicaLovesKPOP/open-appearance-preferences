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

## Adoption levels

Apps can support Open Appearance Preferences at two levels.

### Level 1: Reader

The app reads `PreferTrueBlackInDarkMode` and respects it when dark mode is active.

This is the minimum useful implementation.

### Level 2: Reader + Setter

The app reads `PreferTrueBlackInDarkMode` and also provides a standardized user-facing setting to enable or disable it.

Level 2 support is optional, but recommended for apps that already have Appearance, Theme, Display, or Personalization settings.

Apps without settings UI, command-line tools, libraries, and sandboxed apps may support Level 1 without supporting Level 2.

## Minimum viable support

An app can support Level 1 with three steps:

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

Apps with Level 2 support may write the same per-user value.

When enabled, write:

```text
PreferTrueBlackInDarkMode = 1
```

When disabled, write:

```text
PreferTrueBlackInDarkMode = 0
```

Do not require administrator rights.

Do not write to `HKEY_LOCAL_MACHINE`.

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

## Standard user-facing setting

If your app provides Level 2 support, use the same wording as other supporting apps.

Recommended location:

```text
Settings → Appearance
```

Recommended label:

```text
Prefer true black in dark mode
```

Recommended helper text:

```text
Use pure black or OLED-friendly surfaces when dark mode is on. Only supported apps will change.
```

Recommended layout:

```text
[ ] Prefer true black in dark mode
    Use pure black or OLED-friendly surfaces when dark mode is on. Only supported apps will change.
```

Longer helper text, if there is room:

```text
Use pure black or OLED-friendly surfaces when dark mode is on. This does not force dark mode and only affects apps that support Open Appearance Preferences.
```

## App-local fallback setting

Some apps may be sandboxed or may not be able to write the global/platform preference safely.

In that case, the app may expose an app-local preference using this label:

```text
Prefer true black in dark mode for this app
```

Recommended helper text:

```text
Use pure black or OLED-friendly surfaces in this app when dark mode is on.
```

Do not present an app-local setting as a system-wide preference.

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
- Silently enable the preference.
- Change the preference during installation.
- Use the preference for analytics or profiling.
- Assume the display is OLED.
- Label the setting only as "OLED mode" or "AMOLED mode".
- Imply that unsupported apps will change.
- Break readability just to use pure black everywhere.
- Change documents, images, videos, design previews, or charts where color accuracy matters.

## Pull request template for other projects

```markdown
Hi! Would you consider supporting `PreferTrueBlackInDarkMode` from Open Appearance Preferences?

It is a tiny optional preference meaning:

> When the app is already using dark mode, prefer true-black or OLED-friendly dark surfaces where practical.

It does not force dark mode and should not override accessibility settings.

There are two support levels:

- Level 1: read the preference and respect it in dark mode.
- Level 2: also expose a standardized setting so users can enable or disable it.

If the app exposes the setting, the recommended label is:

`Prefer true black in dark mode`

Recommended helper text:

`Use pure black or OLED-friendly surfaces when dark mode is on. Only supported apps will change.`

Spec:
https://github.com/MicaLovesKPOP/open-appearance-preferences

Thanks!
```
