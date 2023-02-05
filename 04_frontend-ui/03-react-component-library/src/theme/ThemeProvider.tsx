import React, { createContext, useContext, useEffect, useState } from "react";

export type Theme = "light" | "dark";

interface ThemeContextValue {
  theme: Theme;
  setTheme: (theme: Theme) => void;
}

const ThemeContext = createContext<ThemeContextValue | undefined>(undefined);

export interface ThemeProviderProps {
  children: React.ReactNode;
  theme?: Theme;
  defaultTheme?: Theme;
  onThemeChange?: (theme: Theme) => void;
}

export const ThemeProvider: React.FC<ThemeProviderProps> = ({
  children,
  theme: controlledTheme,
  defaultTheme = "light",
  onThemeChange,
}) => {
  const [uncontrolledTheme, setUncontrolledTheme] =
    useState<Theme>(defaultTheme);
  const theme = controlledTheme ?? uncontrolledTheme;

  const setTheme = (nextTheme: Theme) => {
    if (controlledTheme === undefined) {
      setUncontrolledTheme(nextTheme);
    }
    onThemeChange?.(nextTheme);
  };

  useEffect(() => {
    document.documentElement.dataset.theme = theme;
    document.documentElement.style.colorScheme = theme;
  }, [theme]);

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = (): ThemeContextValue => {
  const context = useContext(ThemeContext);

  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }

  return context;
};

ThemeProvider.displayName = "ThemeProvider";
