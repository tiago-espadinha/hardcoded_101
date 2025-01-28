# Aurora DS — Changelog

All notable changes to this project will be documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [Unreleased]

### Added
- `Tag` component — dismissible label chip with intent colours
- `Accordion` component — single/multiple expand modes via Radix UI
- `Select` component — listbox with grouping and type-ahead support
- `prefersReducedMotion()` helper exported from `@aurora-ds/components`

---

## [0.1.0] — 2025-01-21

### Added
- **Design tokens** — two-layer semantic + primitive architecture processed by Style Dictionary
  - Outputs: CSS custom properties, TypeScript constants, Tailwind extension
  - Light and dark mode semantic tokens via `[data-theme]` attribute
- **Level 1 Primitives**: `Box`, `Stack`, `Inline`, `Grid`, `Divider`, `Text`, `Heading`, `Code`, `Link`
- **Level 2 Simple**: `Button`, `Badge`, `Avatar`, `Spinner`, `ProgressBar`, `Skeleton`
- **Level 3 Composite**: `Input`, `Textarea`, `Checkbox`, `Switch`, `FieldWrapper`
- **Level 4 Complex**: `Modal`, `Tabs`, `Toast` + `ToastProvider`/`ToastViewport`, `Tooltip`
- **Icon library** — 40+ typed SVG React components via `@aurora-ds/icons`
- **Storybook 7** — interactive playground, axe-core a11y panel, theme switcher, MDX docs
  - Stories: Button, Badge, Avatar, Spinner, ProgressBar, Skeleton, Input, Textarea, Checkbox, Switch, Modal, Tabs, Toast, Tooltip
  - MDX: Design Tokens, Accessibility Guidelines
- **Next.js 14 docs site** — Aurora DS documentation landing page

### Accessibility
- All components pass axe-core with zero violations
- WCAG 2.1 AA contrast compliance in light and dark themes
- Full keyboard navigation with visible focus rings
- 44×44px minimum touch targets throughout
- Screen reader tested on VoiceOver (macOS) and NVDA (Windows)
