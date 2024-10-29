import React from 'react';
import type { Preview } from '@storybook/react';
import '@aurora-ds/tokens/css';
import '@aurora-ds/tokens/theme';
import '../src/styles/generated.css';

const preview: Preview = {
  parameters: {
    actions: { argTypesRegex: '^on[A-Z].*' },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
    a11y: {
      // axe-core config — runs on every story automatically
      config: {
        rules: [
          { id: 'color-contrast', enabled: true },
          { id: 'focus-trap',     enabled: true },
        ],
      },
    },
    backgrounds: {
      options: {
        light: { name: 'light', value: '#f8fafc' },
        dark: { name: 'dark',  value: '#020617' }
      }
    },
  },

  decorators: [
    (Story, context) => {
      const theme = context.globals.theme ?? 'light';
      return (
        <div data-theme={theme} style={{ padding: '2rem', minHeight: '100vh', background: 'var(--aurora-color-background-default)', color: 'var(--aurora-color-foreground-default)', fontFamily: 'var(--aurora-font-family-sans)' }}>
          <Story />
        </div>
      );
    },
  ],

  globalTypes: {
    theme: {
      name: 'Theme',
      description: 'Aurora DS colour theme',
      defaultValue: 'light',
      toolbar: {
        icon: 'circlehollow',
        items: [
          { value: 'light', title: 'Light' },
          { value: 'dark',  title: 'Dark' },
        ],
        showName: true,
        dynamicTitle: true,
      },
    },
  },

  initialGlobals: {
    backgrounds: {
      value: 'light'
    }
  }
};

export default preview;
