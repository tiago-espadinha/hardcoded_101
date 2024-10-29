import type { Meta, StoryObj } from '@storybook/react';
import { Button } from '@aurora-ds/components';
import { PlusIcon, TrashIcon, DownloadIcon } from '@aurora-ds/icons';

/**
 * The `Button` component is the primary call-to-action element in Aurora DS.
 *
 * Use `intent` to convey semantic meaning and `variant` to control visual weight.
 * Every button maintains a minimum 44×44px touch target and a visible focus ring.
 *
 * ## Keyboard Interaction
 * | Key         | Action                    |
 * |-------------|---------------------------|
 * | `Tab`       | Move focus to button      |
 * | `Enter`     | Activate the button       |
 * | `Space`     | Activate the button       |
 *
 * ## Do
 * - Use a concise, action-oriented label ("Save changes", "Delete account")
 * - Use `intent="error"` for destructive actions
 * - Use `loading` while an async operation is pending
 *
 * ## Don't
 * - Don't use multiple `solid/brand` buttons in the same view — it dilutes hierarchy
 * - Don't use `link` variant for navigation; use the `Link` component instead
 * - Don't omit a label for icon-only buttons — use `aria-label`
 */
const meta: Meta<typeof Button> = {
  title: 'Simple/Button',
  component: Button,
  tags: ['autodocs'],
  args: { children: 'Button' },
  argTypes: {
    variant: {
      control: 'select',
      options: ['solid', 'outline', 'ghost', 'link'],
      description: 'Controls the visual weight of the button.',
    },
    intent: {
      control: 'select',
      options: ['default', 'brand', 'success', 'warning', 'error'],
      description: 'Semantic colour intent.',
    },
    size: {
      control: 'select',
      options: ['xs', 'sm', 'md', 'lg', 'xl'],
    },
    loading: { control: 'boolean' },
    disabled: { control: 'boolean' },
  },
};
export default meta;

type Story = StoryObj<typeof Button>;

// ── Playground ────────────────────────────────────────────────────────────────
export const Playground: Story = {
  args: { variant: 'solid', intent: 'brand', size: 'md', children: 'Save changes' },
};

// ── All Variants ──────────────────────────────────────────────────────────────
export const Variants: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', alignItems: 'center' }}>
      <Button variant="solid"   intent="brand">Solid</Button>
      <Button variant="outline" intent="brand">Outline</Button>
      <Button variant="ghost"   intent="brand">Ghost</Button>
      <Button variant="link"    intent="brand">Link</Button>
    </div>
  ),
};

// ── All Intents ───────────────────────────────────────────────────────────────
export const Intents: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
      <Button intent="default">Default</Button>
      <Button intent="brand">Brand</Button>
      <Button intent="success">Success</Button>
      <Button intent="warning">Warning</Button>
      <Button intent="error">Error</Button>
    </div>
  ),
};

// ── All Sizes ─────────────────────────────────────────────────────────────────
export const Sizes: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', alignItems: 'center' }}>
      <Button size="xs" intent="brand">XSmall</Button>
      <Button size="sm" intent="brand">Small</Button>
      <Button size="md" intent="brand">Medium</Button>
      <Button size="lg" intent="brand">Large</Button>
      <Button size="xl" intent="brand">XLarge</Button>
    </div>
  ),
};

// ── With Icons ────────────────────────────────────────────────────────────────
export const WithIcons: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', alignItems: 'center' }}>
      <Button intent="brand" iconLeft={<PlusIcon size={16} aria-hidden />}>Add item</Button>
      <Button intent="error" variant="outline" iconLeft={<TrashIcon size={16} aria-hidden />}>Delete</Button>
      <Button variant="ghost" iconRight={<DownloadIcon size={16} aria-hidden />}>Export</Button>
      <Button intent="brand" iconOnly aria-label="Add item"><PlusIcon size={16} aria-hidden /></Button>
    </div>
  ),
};

// ── States ────────────────────────────────────────────────────────────────────
export const States: Story = {
  render: () => (
    <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap', alignItems: 'center' }}>
      <Button intent="brand">Normal</Button>
      <Button intent="brand" loading>Loading…</Button>
      <Button intent="brand" disabled>Disabled</Button>
    </div>
  ),
};

// ── Accessibility ─────────────────────────────────────────────────────────────
export const Accessibility: Story = {
  name: 'A11y — Focus Ring Visibility',
  render: () => (
    <div>
      <p style={{ marginBottom: '16px', fontSize: '0.875rem', color: 'var(--aurora-color-foreground-muted)' }}>
        Tab through the buttons below to verify focus ring visibility in both light and dark themes.
      </p>
      <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
        <Button intent="brand">First button</Button>
        <Button variant="outline">Second button</Button>
        <Button variant="ghost" intent="error">Third button</Button>
      </div>
    </div>
  ),
};
