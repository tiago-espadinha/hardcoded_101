# Aurora DS: Accessible Design System

A production-grade design system with full WCAG 2.1 AA accessibility compliance, semantic design tokens, light/dark theming, and comprehensive Storybook documentation — built on React 18, TypeScript, Tailwind CSS, and Radix UI primitives.

## Features

- **Design Token Architecture**: Semantic + primitive token layers processed by Style Dictionary, emitting CSS custom properties, TypeScript constants, and Tailwind config extensions
- **30+ Accessible Components**: From layout primitives (`Box`, `Stack`) to complex composites (`Modal`, `CommandMenu`) — every component passes axe-core with zero violations
- **WCAG 2.1 AA Compliance**: 4.5:1 text contrast, 3:1 UI component contrast, 44×44px touch targets, full keyboard navigation, and screen-reader tested on VoiceOver and NVDA
- **Light & Dark Theming**: Semantic colour tokens automatically resolve to the correct primitive per theme via CSS custom properties
- **Storybook Documentation**: Auto-generated API docs from TypeScript types, interactive playgrounds, keyboard interaction tables, and Do/Don't usage examples for every component
- **Icon Library**: 50+ SVG icons as typed React components with consistent sizing and `aria-label` support

## Learning Objectives

- Understand semantic token architecture and how tokens scale across a component library
- Know WCAG 2.1 at AA level and how to audit and fix violations
- Experience the operational challenges of a design system: versioning, deprecation, and contribution guidelines

## Project Structure

```
aurora-ds/
├── packages/
│   ├── tokens/              # Style Dictionary config + source JSON tokens
│   │   ├── src/             # Token source files
│   │   │   ├── colors.json
│   │   │   ├── typography.json
│   │   │   ├── spacing.json
│   │   │   ├── radius.json
│   │   │   ├── shadow.json
│   │   │   └── motion.json
│   │   ├── dist/            # Generated outputs (css, ts, tailwind)
│   │   └── style-dictionary.config.js
│   ├── components/          # React component library
│   │   └── src/
│   │       ├── primitives/  # Box, Stack, Inline, Grid, Text, Heading…
│   │       ├── simple/      # Button, Badge, Avatar, Spinner…
│   │       ├── composite/   # Input, Select, Checkbox, Switch…
│   │       └── complex/     # Modal, Drawer, Tabs, Toast, CommandMenu…
│   └── icons/               # SVG icon React components
├── apps/
│   ├── storybook/           # Storybook 7 documentation app
│   └── docs/                # Next.js documentation site
├── tooling/
│   ├── eslint/              # Shared ESLint config
│   └── tsconfig/            # Shared TypeScript configs
└── package.json             # Turborepo workspace root
```

## Requirements

- Node.js 18+
- pnpm 8+ (workspace manager)

## How to Run

Install dependencies from the workspace root:
```bash
pnpm install
```

Build design tokens:
```bash
pnpm --filter @aurora-ds/tokens build
```

Start Storybook:
```bash
pnpm --filter @aurora-ds/storybook dev
# Visit http://localhost:6006
```

Start the docs site:
```bash
pnpm --filter @aurora-ds/docs dev
# Visit http://localhost:3000
```

## Testing

Run the full accessibility audit across all component stories:
```bash
pnpm test:a11y
```

Run unit tests:
```bash
pnpm test
```
