# User-facing UI guidance

Applications that support Open Appearance Preferences may expose a user-facing setting for `PreferTrueBlackInDarkMode`.

This setting should use consistent wording so users see the same concept across different apps.

## Adoption levels

### Level 1: Reader

The application reads `PreferTrueBlackInDarkMode` and respects it when dark mode is active.

### Level 2: Reader + Setter

The application reads `PreferTrueBlackInDarkMode` and also provides a user-facing setting to enable or disable it.

Level 2 support is optional.

Apps without appearance settings, apps without settings UI, libraries, command-line tools, and sandboxed apps may support Level 1 without supporting Level 2.

## Recommended setting label

Use this label:

```text
Prefer true black in dark mode
```

## Recommended helper text

Use this helper text:

```text
Use pure black or OLED-friendly surfaces when dark mode is on. Only supported apps will change.
```

Longer version:

```text
Use pure black or OLED-friendly surfaces when dark mode is on. This does not force dark mode and only affects apps that support Open Appearance Preferences.
```

## Recommended placement

Place the setting in an appearance, theme, display, personalization, or accessibility-adjacent settings area.

Recommended location:

```text
Settings → Appearance
```

Recommended layout:

```text
[ ] Prefer true black in dark mode
    Use pure black or OLED-friendly surfaces when dark mode is on. Only supported apps will change.
```

## Behavior

When the user enables the setting, the app should set:

```text
PreferTrueBlackInDarkMode = 1
```

When the user disables the setting, the app should set:

```text
PreferTrueBlackInDarkMode = 0
```

On Windows, this means writing the per-user registry value:

```text
HKEY_CURRENT_USER\Software\OpenAppearance\Preferences
PreferTrueBlackInDarkMode
```

Apps should not require administrator rights to change this preference.

## Rules

Apps should not silently enable this preference.

Apps should not change this preference during installation.

Apps should not hide this preference behind hardware-specific wording such as "OLED mode" or "AMOLED mode".

Apps should not imply that enabling this preference will affect unsupported apps.

Apps should not imply that enabling this preference changes the operating system's dark mode setting.

Apps should not override accessibility settings, forced-color modes, or high-contrast modes.

## If the app cannot write the global preference

Some apps may be sandboxed or may not have a safe way to write the platform preference.

In that case, the app may show the same setting as an app-local preference.

For app-local settings, use this label:

```text
Prefer true black in dark mode for this app
```

Recommended helper text:

```text
Use pure black or OLED-friendly surfaces in this app when dark mode is on.
```

Apps should not present an app-local setting as a system-wide preference.

## Avoid these labels

Avoid:

- `OLED mode`
- `AMOLED mode`
- `True dark`
- `Force black theme`
- `Battery saver theme`

These labels are less clear because they imply hardware detection, forced behavior, or battery-saving guarantees.
