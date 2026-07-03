# Request app support

You can ask an app or framework developer to support Open Appearance Preferences.

## Short request

```text
Hi! Would you consider supporting Open Appearance Preferences?

The first preference is PreferTrueBlackInDarkMode.

It means: when the app is already using dark mode, prefer true-black or OLED-friendly dark surfaces where practical.

It does not force dark mode and should not override accessibility settings.

Spec:
https://github.com/MicaLovesKPOP/open-appearance-preferences
```

## More technical request

```text
Hi! Would you consider supporting Open Appearance Preferences?

It defines a small optional preference named PreferTrueBlackInDarkMode:

- If the app is already in dark mode, prefer true-black or OLED-friendly dark surfaces where practical.
- If the app is in light mode, ignore it.
- Accessibility and forced-color modes should take priority.
- It should not force dark mode.

On Windows, the value is:

HKCU\Software\OpenAppearance\Preferences
PreferTrueBlackInDarkMode = REG_DWORD 1

There are also JSON and environment-variable fallbacks for cross-platform apps.

Spec:
https://github.com/MicaLovesKPOP/open-appearance-preferences
```

## Where to ask

Good places:

- GitHub issues or discussions for the app
- GitHub issues or discussions for the app's theme library
- Discord/Matrix/forum support channels
- Reddit or community forums if the developer actively reads them

Best targets:

- Theme libraries
- UI frameworks
- Electron/Tauri apps
- .NET/WPF/WinUI apps
- Qt apps
- Flutter desktop apps
- Terminal apps
- Browser extensions

A framework or theme library adding support is more valuable than a single app adding support.
