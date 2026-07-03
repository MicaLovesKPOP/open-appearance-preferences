# Platform notes

## Windows

Recommended v1 binding:

```text
HKEY_CURRENT_USER\Software\OpenAppearance\Preferences
PreferTrueBlackInDarkMode = REG_DWORD 1
```

Why Windows first:

- Per-user registry preferences are normal for Windows desktop apps.
- Native, Electron, .NET, Qt, and Tauri apps can read the registry easily.
- Users and tools can enable/disable the setting with `.reg` files or PowerShell.

## Linux

Recommended v1 fallback:

```text
$XDG_CONFIG_HOME/openappearance/preferences.json
```

If `XDG_CONFIG_HOME` is missing, apps may use:

```text
~/.config/openappearance/preferences.json
```

Future possibility:

A desktop portal or freedesktop appearance setting could expose the preference more formally.

Do not block v1 adoption on that.

## macOS

Recommended v1 fallback:

```text
~/Library/Application Support/OpenAppearance/preferences.json
```

Apps may also choose an app-local UserDefaults setting with the same semantic name:

```text
PreferTrueBlackInDarkMode
```

macOS apps should respect system appearance and accessibility settings first.

## Android

Android should be treated as implementation guidance, not a global v1 binding.

Recommended app-local setting name:

```text
preferTrueBlackInDarkMode
```

Apps that already offer light/dark/system theme choices may add:

```text
Prefer true black in dark mode
```

The app should store this using its normal app preference mechanism.

## iOS and iPadOS

iOS and iPadOS should be treated as implementation guidance, not a global v1 binding.

Recommended app-local setting name:

```text
preferTrueBlackInDarkMode
```

Apps should respect system appearance and accessibility settings first.

## Web

There is no standard web media query for this preference today.

A possible future direction could be:

```css
@media (prefers-dark-surface: true-black) {
  body {
    background: #000;
  }
}
```

This is not part of v1.

For now, websites may expose an app/site-local setting using the same user-facing wording.

## Electron

Electron apps are a strong adoption target.

Recommended behavior:

1. Use Electron/native APIs to determine light/dark mode as usual.
2. On Windows, read the registry binding.
3. If unavailable, read JSON fallback.
4. If unavailable, read environment variable.
5. Apply true-black surfaces only when dark mode is active.

## Tauri

Tauri apps can read the OS binding in Rust or via a plugin, then pass the preference to the frontend.

Recommended fallback:

- registry on Windows
- JSON on Linux/macOS
- environment variable for CLI/dev builds

## Qt

Qt apps can expose this as a theme variant.

Recommended behavior:

- Leave normal palette detection unchanged.
- If the app is in dark mode and the preference is enabled, select a true-black dark palette.

## Flutter desktop

Flutter apps can support this as an optional user/theme preference.

Recommended behavior:

- Respect platform brightness first.
- If dark mode is active and the preference is enabled, select a true-black ThemeData variant.
