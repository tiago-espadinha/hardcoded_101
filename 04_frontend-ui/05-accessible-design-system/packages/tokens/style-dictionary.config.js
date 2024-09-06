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
