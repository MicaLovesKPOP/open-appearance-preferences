# Naming

## Chosen name

`PreferTrueBlackInDarkMode`

## Why this name?

It is explicit:

- It is a preference, not a command.
- It says "true black", not vague "true dark".
- It only applies in dark mode.
- It does not imply display hardware detection.

## Rejected names

### `OLEDMode`

Rejected because it refers to hardware.

A user might prefer true black on non-OLED displays. An app should not need to know the display type.

### `AMOLEDMode`

Rejected for the same reason as `OLEDMode`, and because it is too mobile-specific.

### `TrueDark`

Rejected because it is ambiguous.

Some people use "true dark" to mean a proper dark theme. Others use it to mean pure black.

### `ForceBlackTheme`

Rejected because the preference should not force dark mode or override app/accessibility choices.

### `DarkThemeVariant`

Rejected for v1 because it implies an enum or broader theme system.

It could be considered later if there is demand for values such as:

```text
soft-dark
true-black
low-glow
```

### `PreferOLEDDarkMode`

Rejected because the useful part is true-black surfaces, not OLED detection.

## Recommended user-facing wording

Best:

```text
Prefer true black in dark mode
```

Alternative:

```text
Use OLED-friendly black surfaces in dark mode
```

Short label:

```text
True black dark mode
```

Description:

```text
Use pure black or OLED-friendly surfaces when dark mode is enabled.
```
