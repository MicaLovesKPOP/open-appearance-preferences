# Launch posts

## GitHub repo description

A tiny cross-platform appearance preference spec for true-black dark mode.

## Short post

I made a small draft spec called Open Appearance Preferences.

The first preference is `PreferTrueBlackInDarkMode`:

> When an app is already using dark mode, prefer true-black or OLED-friendly dark surfaces where practical.

It does not force dark mode, does not override accessibility settings, and does not try to detect OLED hardware.

The goal is to give apps/frameworks a tiny shared convention instead of every app inventing its own "OLED", "AMOLED", or "Lights out" toggle.

Repo:
https://github.com/YOUR-USER/open-appearance-preferences

Feedback welcome, especially from Windows, Electron, .NET, Qt, Tauri, Flutter, and accessibility folks.

## Pull request / issue pitch

Would you consider supporting Open Appearance Preferences?

The first preference is `PreferTrueBlackInDarkMode`, meaning:

> When the app is already using dark mode, prefer true-black or OLED-friendly dark surfaces where practical.

The minimum implementation is small:
- read the Windows registry binding or JSON/env fallback
- if dark mode is active and the preference is enabled, select the app's true-black dark variant where practical

It does not force dark mode and should not override accessibility settings.

Spec:
https://github.com/YOUR-USER/open-appearance-preferences
