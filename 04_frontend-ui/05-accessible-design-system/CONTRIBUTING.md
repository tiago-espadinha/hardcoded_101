# Contributing to Aurora DS

## Development Setup

```bash
pnpm install
pnpm tokens:build   # build design tokens first
pnpm storybook      # start Storybook at http://localhost:6006
```

## Adding a New Component

1. Choose the correct level:
   - **Level 1** — zero dependencies, layout/text primitive
   - **Level 2** — depends on Level 1 only
   - **Level 3** — form composite; use Radix UI for a11y logic
   - **Level 4** — complex overlay/widget; always use Radix UI

2. Create `packages/components/src/<level>/<ComponentName>.tsx`
3. Export from the appropriate level barrel and `src/index.ts`
4. Add a Storybook story in `apps/storybook/src/stories/`
5. The story **must** include an Accessibility story that verifies focus ring visibility
6. Run `pnpm test:a11y` — **zero violations is the acceptance criterion**

## Accessibility Checklist

Before opening a PR:
- [ ] Component passes axe-core with zero violations
- [ ] Keyboard navigation works correctly (Tab, Enter, Space, Arrow keys, Escape)
- [ ] Focus ring is visible in both light and dark themes
- [ ] All interactive elements have accessible names (`aria-label`, `<label>`, or visible text)
- [ ] Error states use `aria-invalid` + `aria-describedby`
- [ ] Touch targets are minimum 44×44px
- [ ] Colours are not the only means of conveying information

## Token Guidelines

- **Never** use primitive tokens directly in component styles (e.g. `--aurora-color-primitive-blue-600`)
- **Always** use semantic tokens (e.g. `--aurora-color-brand-default`)
- When adding new tokens, add them in both `light` and `dark` variants in `colors.json`
- Run `pnpm tokens:build` and commit the `dist/` changes alongside the source changes

## Commit Convention

This repository uses [Conventional Commits](https://www.conventionalcommits.org/):

```
feat(components): add RadioGroup component
fix(tokens): correct dark-mode border contrast ratio
docs(storybook): add Accordion keyboard interaction table
test(components): add axe tests for Select
chore: update Radix UI to 1.1.x
```
