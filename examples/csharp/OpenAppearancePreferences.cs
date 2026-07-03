using System;
using Microsoft.Win32;

namespace OpenAppearance
{
    public static class OpenAppearancePreferences
    {
        private const string RegistryPath = @"HKEY_CURRENT_USER\Software\OpenAppearance\Preferences";
        private const string PreferTrueBlackValueName = "PreferTrueBlackInDarkMode";

        public static bool PreferTrueBlackInDarkMode()
        {
            object? value = Registry.GetValue(RegistryPath, PreferTrueBlackValueName, null);

            if (value is int intValue)
            {
                return intValue == 1;
            }

            return false;
        }

        public static bool ShouldUseTrueBlackDarkMode(bool appIsUsingDarkMode, bool accessibilityForcedColorsEnabled = false)
        {
            if (accessibilityForcedColorsEnabled)
            {
                return false;
            }

            return appIsUsingDarkMode && PreferTrueBlackInDarkMode();
        }
    }
}
