# Open Appearance Preferences v1

## Status

Draft proposal.

## Purpose

Open Appearance Preferences defines small, optional user appearance preferences that applications may respect in addition to operating-system theme settings and accessibility settings.

The first preference is:

`PreferTrueBlackInDarkMode`

It lets a user express:

> When an application is already using dark mode, I prefer true-black or OLED-friendly dark surfaces where practical.

## Goals

- Give users a simple way to request true-black dark mode.
- Let applications support the preference without changing how they already detect light mode or dark mode.
- Provide consistent wording and behavior when applications expose a user-facing setting for the preference.
- Avoid interfering with operating-system dark mode, app-specific theme settings, or accessibility settings.
- Keep implementation simple enough that individual developers, frameworks, and theme libraries can adopt it quickly.

## Non-goals

- This specification does not force applications into dark mode.
- This specification does not replace Windows, macOS, Linux, Android, iOS, browser, or application-level theme settings.
- This specification does not require exact colors.
- This specification does not attempt to detect whether the user's display is OLED.
- This specification is not a full theme system.
- This specification does not require every supporting application to provide a settings UI.

## Preference name

`PreferTrueBlackInDarkMode`

## Meaning

When this preference is enabled, applications should prefer true-black or OLED-friendly surfaces when the application is already using dark mode.

Applications should not apply this preference while using light mode.

## Values

Boolean.

| Value | Meaning |
|---|---|
| Missing | No special preference |
| `false` / `0` | No special preference |
| `true` / `1` | Prefer true-black surfaces in dark mode |

Invalid values must be treated as missing.

## Adoption levels

Applications may support this specification at either of two levels.

### Level 1: Reader

The application reads `PreferTrueBlackInDarkMode` and respects it when dark mode is active.

Level 1 is the minimum useful implementation.

### Level 2: Reader + Setter

The application reads `PreferTrueBlackInDarkMode` and also provides a user-facing setting to enable or disable it.

Level 2 support is optional.

Apps without appearance settings, apps without settings UI, libraries, command-line tools, and sandboxed apps may support Level 1 without supporting Level 2.

When an application provides Level 2 support, it should follow the user-facing UI guidance in this specification.

## Priority order

Applications should apply appearance preferences in this order:

1. Accessibility and forced-color modes
2. Explicit in-app user theme settings
3. Operating-system light/dark mode
4. `PreferTrueBlackInDarkMode`
5. Application default styling

This means `PreferTrueBlackInDarkMode` must never override accessibility modes, high-contrast modes, forced-color modes, or an explicit in-app setting.

## Expected application behavior

If the application is using light mode:

- Ignore `PreferTrueBlackInDarkMode`.

If the application is using dark mode and `PreferTrueBlackInDarkMode` is enabled:

- Prefer black or near-black colors for large base surfaces.
- Prefer pure black, such as `#000000`, for main window backgrounds where practical.
- Use near-black colors where needed for hierarchy, controls, cards, hover states, focus states, dividers, and readability.
- Preserve sufficient contrast for text, icons, focus indicators, and interactive states.
- Avoid decorative glow, bright full-screen surfaces, or high-luminance dark-mode styling where practical.
- Do not change content where color accuracy matters, such as images, videos, charts, maps, documents, previews, or design canvases.

Applications may partially apply or ignore this preference where true black would harm readability, accessibility, brand requirements, content accuracy, or usability.

## User-facing setting UI

Applications that provide Level 2 support should use consistent wording so users see the same concept across different apps.

Recommended setting label:

```text
Prefer true black in dark mode
```

Recommended helper text:

```text
Use pure black or OLED-friendly surfaces when dark mode is on. Only supported apps will change.
```

Longer helper text:

```text
Use pure black or OLED-friendly surfaces when dark mode is on. This does not force dark mode and only affects apps that support Open Appearance Preferences.
```

Recommended placement:

```text
Settings → Appearance
```

Recommended layout:

```text
[ ] Prefer true black in dark mode
    Use pure black or OLED-friendly surfaces when dark mode is on. Only supported apps will change.
```

Applications should not silently enable this preference, change it during installation, or imply that unsupported apps will change.

Applications should not require administrator rights to change this preference.

If an app cannot safely write the global/platform preference, it may expose an app-local setting instead. App-local settings should use this label:

```text
Prefer true black in dark mode for this app
```

App-local settings should not be presented as system-wide preferences.

## Windows registry binding

Registry path:

```text
HKEY_CURRENT_USER\Software\OpenAppearance\Preferences
```

Values:

| Name | Type | Meaning |
|---|---|---|
| `SchemaVersion` | `REG_DWORD` | Spec version. For this draft, `1`. |
| `PreferTrueBlackInDarkMode` | `REG_DWORD` | `0` or missing = no special preference. `1` = prefer true-black surfaces in dark mode. |

Example:

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\OpenAppearance\Preferences]
"SchemaVersion"=dword:00000001
"PreferTrueBlackInDarkMode"=dword:00000001
```

Applications should read this from `HKEY_CURRENT_USER`, not `HKEY_LOCAL_MACHINE`, because this is a per-user preference.

Applications may read the value at startup. Applications that already respond live to operating-system theme changes may also re-read the value when their theme is refreshed.

Applications that provide Level 2 support on Windows may write this same per-user value.

## JSON fallback binding

For cross-platform applications or sandboxed environments, applications may also read a JSON file.

Recommended locations:

Windows:

```text
%APPDATA%\OpenAppearance\preferences.json
```

Linux:

```text
$XDG_CONFIG_HOME/openappearance/preferences.json
```

macOS:

```text
~/Library/Application Support/OpenAppearance/preferences.json
```

Example:

```json
{
  "schemaVersion": 1,
  "preferTrueBlackInDarkMode": true
}
```

If both the platform-native setting and JSON fallback exist, applications should prefer the platform-native setting.

## Environment variable binding

Command-line applications and developer tools may also support:

```text
OPEN_APPEARANCE_PREFER_TRUE_BLACK_IN_DARK_MODE
```

Values:

| Value | Meaning |
|---|---|
| Missing | No special preference |
| `0` | No special preference |
| `1` | Prefer true-black surfaces in dark mode |
| `false` | No special preference |
| `true` | Prefer true-black surfaces in dark mode |

The environment variable is useful for terminals, scripts, portable applications, and development tooling.

## Suggested implementation logic

```text
if accessibility_forced_colors_enabled:
    use_accessibility_theme()
else if app_user_selected_theme:
    use_app_selected_theme()
else:
    use_os_light_or_dark_theme()

if app_is_using_dark_mode:
    if PreferTrueBlackInDarkMode is enabled:
        use_true_black_dark_variant_where_practical()
```

## Suggested color interpretation

This specification intentionally does not require exact colors.

Recommended interpretation:

| Surface type | Suggested behavior |
|---|---|
| Main app background | Prefer true black |
| Secondary panels | True black or near-black |
| Cards/popovers | Near-black allowed for hierarchy |
| Inputs/buttons | Near-black allowed for affordance |
| Borders/dividers | Low-luminance contrast |
| Text/icons | Must remain readable |
| Focus indicators | Must remain visible |
| Charts/maps/media/documents | Preserve content accuracy |

## Privacy

Applications should not use this preference for fingerprinting, analytics, advertising, or user profiling.

Applications should treat this as a local appearance preference only.

## Accessibility

`PreferTrueBlackInDarkMode` is not an accessibility mode.

It must not override high-contrast mode, forced-color mode, reduced-motion preferences, reduced-transparency preferences, or other accessibility settings.

## Recommended user-facing wording

Use this label when exposing the global preference:

```text
Prefer true black in dark mode
```

Use this helper text:

```text
Use pure black or OLED-friendly surfaces when dark mode is on. Only supported apps will change.
```

If the setting only affects the current app, use this label instead:

```text
Prefer true black in dark mode for this app
```

Avoid:

- "OLED mode"
- "AMOLED mode"
- "True dark"
- "Force black theme"
- "Battery saver theme"

Reason:

The preference is about the desired dark-mode appearance, not about detecting display hardware or forcing application behavior.

## Adoption targets

This preference is designed to be easy for the following to adopt:

- Native Windows apps
- Electron apps
- Qt apps
- Flutter desktop apps
- .NET/WPF/WinUI apps
- Python desktop apps
- Java desktop apps
- Terminal applications
- Theme libraries
- Design systems
- Browser extensions
- Cross-platform launchers and app frameworks

## Platform support levels

Normative:

- The preference name.
- The meaning of the preference.
- The values.
- The expected behavior.
- The accessibility priority rules.
- The user-facing wording for apps that expose the setting.

Recommended:

- Windows registry binding.
- JSON fallback binding.
- Environment variable binding.
- User-facing UI layout and helper text.

Informative:

- macOS, Linux, Android, iOS, and web implementation guidance.

## Future preferences

This specification intentionally starts with one preference.

Possible future preferences may include:

- `PreferLowLuminanceInDarkMode`
- `PreferReducedGlowInDarkMode`
- `PreferDarkDocumentCanvas`
- `PreferDimmedMediaChrome`

These should not be added until there is proven developer and user demand.

## Versioning

This draft defines schema version `1`.

Applications should ignore unknown future values and unknown future preference names.
