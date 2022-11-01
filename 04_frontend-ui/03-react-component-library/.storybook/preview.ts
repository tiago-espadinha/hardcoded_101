import type { Preview } from '@storybook/react';
import '../src/tokens/colors.css';
import '../src/tokens/spacing.css';
import '../src/tokens/typography.css';

const preview: Preview = {
  parameters: {
    controls: {
      matchers: {
        color: /(background|color)$/i,
        date: /Date$/,
      },
    },
  },
};

export default preview;
