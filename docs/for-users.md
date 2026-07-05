# For users

Open Appearance Preferences lets you express a simple preference:

> When an app is already using dark mode, I prefer true-black or OLED-friendly dark surfaces where practical.

## What this does

This creates a local preference on your system that apps may read.

On Windows, the preference is stored here:

```text
HKEY_CURRENT_USER\Software\OpenAppearance\Preferences
```

With this value:

```text
PreferTrueBlackInDarkMode = 1
```

This means:

> If an app is already using dark mode, prefer true-black / OLED-friendly dark surfaces.

## What this does not do

This does not force Windows into dark mode.

This does not change how Windows dark mode works.

This does not automatically change every app.

Apps need to support this preference before they will react to it.

## Enable on Windows

Download or open:

```text
examples/windows/Enable True Black Dark Mode Preference.reg
```

Then double-click it and accept the Windows registry prompt.

This only applies to your own Windows user account.

Admin rights are not required.

## Disable on Windows

Download or open:

```text
examples/windows/Disable True Black Dark Mode Preference.reg
```

Then double-click it and accept the Windows registry prompt.

## Check whether it is enabled

Run this in PowerShell:

```powershell
Get-ItemProperty -Path "HKCU:\Software\OpenAppearance\Preferences"
```

If enabled, you should see:

```text
PreferTrueBlackInDarkMode : 1
```

You can also run:

```powershell
.\examples\windows\check-preference.ps1
```

## Enable inside a supporting app

Apps that support Open Appearance Preferences may also let you enable or disable the same preference from inside the app.

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

If a setting says this, it should control the same `PreferTrueBlackInDarkMode` preference.

Some sandboxed apps may only be able to change their own local setting. In that case, the app should say:

```text
Prefer true black in dark mode for this app
```

## Will this affect my apps?

Only if the app supports Open Appearance Preferences.

If an app does not support it yet, nothing will change.

## Supported apps

No known apps yet.

If your app supports this preference, please open an adoption report.

## Is this safe?

This is a small per-user appearance preference.

It does not install software.
It does not run in the background.
It does not require admin rights.
It does not change Windows dark mode.
It can be disabled again at any time.
