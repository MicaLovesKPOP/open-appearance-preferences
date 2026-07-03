# Future preferences

This project intentionally starts with one preference:

```text
PreferTrueBlackInDarkMode
```

Do not add more preferences until there is real developer and user demand.

## Possible future preferences

### `PreferLowLuminanceInDarkMode`

Meaning:

> In dark mode, reduce the overall brightness/light output of the interface where practical.

This would be broader than true black. It could affect bright accents, empty states, charts, white canvases, and splash screens.

Risk:

- Harder to define.
- May conflict with brand or data visualization needs.

### `PreferReducedGlowInDarkMode`

Meaning:

> In dark mode, avoid bright decorative glows and high-luminance visual effects.

Useful for apps that use neon-style accents in dark mode.

Risk:

- Subjective.
- More design-system-specific.

### `PreferDarkDocumentCanvas`

Meaning:

> Prefer a dark canvas for documents or editors when practical.

Useful for writing apps, code editors, PDF readers, and note apps.

Risk:

- Can harm document fidelity.
- Some users need to preview actual page colors.

### `PreferDimmedMediaChrome`

Meaning:

> Prefer darker controls around media playback.

Useful for video, music, and gallery apps.

Risk:

- Too narrow for v1.

## Why not include these now?

The adoption pitch must stay small.

The first version should be easy to explain in one sentence:

> If dark mode is on, prefer true-black surfaces.

More preferences can be proposed later if the first one proves useful.
