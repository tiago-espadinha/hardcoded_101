const StyleDictionary = require('style-dictionary');

StyleDictionary.registerFormat({
  name: 'css/theme-aliases',
  formatter: ({ dictionary }) => {
    const semanticTokens = dictionary.allTokens.filter(token =>
      token.path[0] === 'color' && token.path[1] === 'semantic',
    );
    const aliases = semanticTokens.reduce((result, token) => {
      const theme = token.path.at(-1);
      const name = token.path.slice(2, -1).join('-');
      result[theme] ??= [];
      result[theme].push(`  --aurora-color-${name}: ${token.value};`);
      return result;
    }, {});

    return [
      ':root {',
      ...(aliases.light ?? []),
      '  --aurora-font-family-sans: var(--aurora-typography-font-family-sans);',
      '  --aurora-font-family-mono: var(--aurora-typography-font-family-mono);',
      '  --aurora-font-family-display: var(--aurora-typography-font-family-display);',
      '}',
      '',
      '[data-theme="dark"] {',
      ...(aliases.dark ?? []),
      '}',
      '',
    ].join('\n');
  },
});

/** @type {import('style-dictionary').Config} */
module.exports = {
  source: ['src/**/*.json'],
  platforms: {
    css: {
      transformGroup: 'css',
      prefix: 'aurora',
      buildPath: 'dist/',
      files: [
        {
          destination: 'tokens.css',
          format: 'css/variables',
          options: { outputReferences: true },
        },
        {
          destination: 'theme-aliases.css',
          format: 'css/theme-aliases',
        },
      ],
    },
    ts: {
      transformGroup: 'js',
      buildPath: 'dist/',
      files: [
        {
          destination: 'tokens.ts',
          format: 'javascript/es6',
        },
      ],
    },
    tailwind: {
      transformGroup: 'js',
      buildPath: 'dist/',
      files: [
        {
          destination: 'tailwind-tokens.js',
          format: 'javascript/module',
        },
      ],
    },
  },
};
