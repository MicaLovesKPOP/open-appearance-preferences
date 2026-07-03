# Open Appearance Preferences

A tiny appearance-preference proposal for apps that want to respect a user's preference for true-black dark mode.

## The first preference

`PreferTrueBlackInDarkMode`

Meaning:

> When an app is already using dark mode, prefer true-black or OLED-friendly dark surfaces where practical.

This preference does **not** force dark mode. It only affects apps that are already using dark mode.


## For users

You can enable the preference today, but apps will only respond to it if they support Open Appearance Preferences.

On Windows:

1. Open [`examples/windows/Enable True Black Dark Mode Preference.reg`](examples/windows/Enable%20True%20Black%20Dark%20Mode%20Preference.reg).
2. Double-click it.
3. Accept the Windows registry prompt.

This creates a per-user preference:

```text
HKEY_CURRENT_USER\Software\OpenAppearance\Preferences
PreferTrueBlackInDarkMode = 1
```

It does not force Windows into dark mode.
It does not change unsupported apps.
It does not require admin rights.

See [`docs/for-users.md`](docs/for-users.md) for the full user guide.


## Why this exists

Operating systems and browsers commonly expose whether the user prefers light mode or dark mode. Many apps also support dark mode.

But there is usually no simple shared way for a user to say:

> I like dark mode, but I prefer the true-black / OLED-friendly version.

Some apps have their own "AMOLED", "Lights out", "OLED", or "true black" toggles. This project proposes a small shared convention so apps, frameworks, and theme libraries can support that preference consistently.

## Design goals

- One clear preference.
- Easy for developers to support.
- No interference with system light/dark mode.
- No interference with accessibility settings.
- Per-user, local-only, and privacy-respecting.
- Cross-platform in concept, Windows-first in practical implementation.

## Quick Windows example

Registry path:

```text
HKEY_CURRENT_USER\Software\OpenAppearance\Preferences
```

Value:

```text
PreferTrueBlackInDarkMode = REG_DWORD 1
```

Example `.reg` file:

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\OpenAppearance\Preferences]
"SchemaVersion"=dword:00000001
"PreferTrueBlackInDarkMode"=dword:00000001
```

## Developer logic

```text
if app is using dark mode:
    if PreferTrueBlackInDarkMode is enabled:
        use true-black or OLED-friendly surfaces where practical
```

Accessibility and explicit in-app settings should take priority.

Recommended priority:

1. Accessibility and forced-color modes
2. Explicit in-app user theme settings
3. Operating-system light/dark mode
4. `PreferTrueBlackInDarkMode`
5. Application default styling

## Files in this repo

- [`SPEC.md`](SPEC.md) — the actual draft specification.
- [`RATIONALE.md`](RATIONALE.md) — why the spec exists and why it is intentionally small.
- [`ADOPTION.md`](ADOPTION.md) — how apps and libraries can support it.
- [`docs/for-users.md`](docs/for-users.md) — how users can enable and understand the preference.
- [`docs/request-app-support.md`](docs/request-app-support.md) — message templates for asking apps to support it.
- [`docs/platform-notes.md`](docs/platform-notes.md) — Windows, Linux, macOS, Android, iOS, web, and framework notes.
- [`docs/naming.md`](docs/naming.md) — naming decisions and rejected names.
- [`docs/future-preferences.md`](docs/future-preferences.md) — possible future ideas, intentionally not included in v1.
- [`examples/`](examples/) — small implementation examples.

## Current status

Draft proposal.

This project is intentionally small. The goal is not to create a full theme system. The goal is to create one easy preference that developers can adopt in minutes.

## Recommended user-facing wording

Good:

- "Prefer true black in dark mode"
- "Use OLED-friendly black surfaces in dark mode"
- "Prefer pure black backgrounds when dark mode is on"

Avoid:

- "OLED mode"
- "AMOLED mode"
- "True dark"
- "Force black theme"

The preference is about the user's desired dark-mode surface treatment, not about detecting display hardware or forcing app behavior.

## License

This project is released under CC0-1.0. Use it freely.
