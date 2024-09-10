const path = require('node:path');

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    path.join(__dirname, 'apps/storybook/src/**/*.{js,ts,jsx,tsx,mdx}'),
    path.join(__dirname, 'apps/docs/src/**/*.{js,ts,jsx,tsx,mdx}'),
    path.join(__dirname, 'packages/components/src/**/*.{js,ts,jsx,tsx}'),
  ],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['var(--aurora-font-family-sans)'],
        mono: ['var(--aurora-font-family-mono)'],
        display: ['var(--aurora-font-family-display)'],
      },
    },
  },
  plugins: [],
};
