const { nativeTheme } = require("electron");
const { execFileSync } = require("node:child_process");

function readWindowsRegistryPreference() {
  if (process.platform !== "win32") {
    return false;
  }

  try {
    const output = execFileSync(
      "reg",
      [
        "query",
        "HKCU\\Software\\OpenAppearance\\Preferences",
        "/v",
        "PreferTrueBlackInDarkMode"
      ],
      { encoding: "utf8", windowsHide: true }
    );

    return /PreferTrueBlackInDarkMode\s+REG_DWORD\s+0x1/i.test(output);
  } catch {
    return false;
  }
}

function readEnvironmentPreference() {
  const value = process.env.OPEN_APPEARANCE_PREFER_TRUE_BLACK_IN_DARK_MODE;

  if (!value) {
    return false;
  }

  return value === "1" || value.toLowerCase() === "true";
}

function preferTrueBlackInDarkMode() {
  return readWindowsRegistryPreference() || readEnvironmentPreference();
}

function shouldUseTrueBlackDarkMode() {
  const appIsDark =
    nativeTheme.shouldUseDarkColors ||
    nativeTheme.themeSource === "dark";

  return appIsDark && preferTrueBlackInDarkMode();
}

module.exports = {
  preferTrueBlackInDarkMode,
  shouldUseTrueBlackDarkMode
};
