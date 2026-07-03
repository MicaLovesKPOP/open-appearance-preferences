from __future__ import annotations

import json
import os
import platform
from pathlib import Path


def _read_windows_registry_preference() -> bool:
    if platform.system() != "Windows":
        return False

    try:
        import winreg
    except ImportError:
        return False

    try:
        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\OpenAppearance\Preferences",
        ) as key:
            value, value_type = winreg.QueryValueEx(key, "PreferTrueBlackInDarkMode")
            return value_type == winreg.REG_DWORD and value == 1
    except OSError:
        return False


def _json_paths() -> list[Path]:
    system = platform.system()

    if system == "Windows":
        appdata = os.environ.get("APPDATA")
        return [Path(appdata) / "OpenAppearance" / "preferences.json"] if appdata else []

    if system == "Darwin":
        return [
            Path.home()
            / "Library"
            / "Application Support"
            / "OpenAppearance"
            / "preferences.json"
        ]

    xdg_config = os.environ.get("XDG_CONFIG_HOME")
    base = Path(xdg_config) if xdg_config else Path.home() / ".config"
    return [base / "openappearance" / "preferences.json"]


def _read_json_preference() -> bool:
    for path in _json_paths():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue

        return data.get("preferTrueBlackInDarkMode") is True

    return False


def _read_environment_preference() -> bool:
    value = os.environ.get("OPEN_APPEARANCE_PREFER_TRUE_BLACK_IN_DARK_MODE", "")
    return value.lower() in {"1", "true"}


def prefer_true_black_in_dark_mode() -> bool:
    return (
        _read_windows_registry_preference()
        or _read_json_preference()
        or _read_environment_preference()
    )


def should_use_true_black_dark_mode(
    app_is_using_dark_mode: bool,
    accessibility_forced_colors_enabled: bool = False,
) -> bool:
    if accessibility_forced_colors_enabled:
        return False

    return app_is_using_dark_mode and prefer_true_black_in_dark_mode()
