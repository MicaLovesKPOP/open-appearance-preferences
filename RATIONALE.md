# Rationale

## The problem

Many platforms expose a light/dark preference. Many apps support dark mode.

But "dark mode" can mean very different things:

- soft dark gray
- high-contrast black
- true-black OLED-friendly surfaces
- colorful dark themes with bright accents
- dark chrome around bright content

Some users prefer true-black dark mode, especially on OLED displays or in very dark environments. Today, that preference is usually app-specific. A user may need to enable "AMOLED mode", "lights out", or "pure black" separately in each app, if the app supports it at all.

## Why not change OS dark mode?

Changing the meaning of OS dark mode would be disruptive.

Many dark themes intentionally use gray surfaces for hierarchy, shadows, elevation, and readability. A global preference should not redefine dark mode itself.

This proposal adds a small, optional preference on top of existing dark mode:

> If the app is already dark, prefer true-black surfaces where practical.

## Why a boolean?

The first version uses one boolean preference:

`PreferTrueBlackInDarkMode`

A larger enum was considered:

```text
DarkSurfacePreference = system | soft-dark | true-black
```

That is more expressive, but it creates adoption friction. Developers are more likely to support one clear boolean than a mini theme language.

A missing or false value already means "no special preference", which lets apps keep their normal dark theme.

## Why not call it OLED mode?

"OLED mode" is familiar, but it describes hardware rather than the user preference.

A user might prefer true black on:

- OLED
- AMOLED
- QD-OLED
- Mini-LED displays
- LCD displays in a dark room
- Projectors
- Remote desktop sessions
- terminals or kiosk systems

Apps should not need to detect display technology. The setting is about preferred dark-surface treatment, not panel type.

## Why not require exact black everywhere?

Pure black everywhere can hurt usability. Cards, popovers, controls, hover states, focus rings, and dividers often need subtle separation.

The spec recommends true black for large base surfaces where practical, while allowing near-black for hierarchy and readability.

## Why accessibility comes first

True-black dark mode is not the same as high contrast.

Accessibility modes such as forced colors and high contrast exist for readability and usability. `PreferTrueBlackInDarkMode` must not override those modes.

## Why include JSON and environment variables?

The Windows registry binding is practical for native Windows apps.

JSON and environment variables make the preference usable by:

- cross-platform apps
- portable apps
- terminal tools
- Electron/Tauri apps
- Linux/macOS apps
- developer tooling
- sandboxed apps that cannot or should not read the registry

## Why start small?

The biggest adoption risk is complexity.

This project should succeed because it is boring:

- one key
- one boolean
- one clear meaning
- easy examples
- no forced behavior
- no platform politics
