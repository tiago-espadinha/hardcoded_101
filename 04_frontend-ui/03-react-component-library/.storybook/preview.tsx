import '@fontsource/inter/400.css';
import '@fontsource/inter/500.css';
import '@fontsource/inter/600.css';
import '@fontsource/inter/700.css';
import type { Preview } from '@storybook/react-vite';
import { ThemeProvider } from '../src';
import '../src/tokens/colors.css';
import '../src/tokens/spacing.css';
import '../src/tokens/typography.css';
import './preview.css';

const preview: Preview = {
  parameters: {
    backgrounds: {
      default: 'light',
      options: [
        { name: 'Light', value: '#f4f7fb' },
        { name: 'Dark', value: '#111827' },
      ],
    },
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/i,
      },
    },
  },
  decorators: [
    (Story, context) => {
      const isDark = context.globals.backgrounds?.value === '#111827';

      return (
        <ThemeProvider theme={isDark ? 'dark' : 'light'}>
          <Story />
        </ThemeProvider>
      );
    },
  ],
};

export default preview;