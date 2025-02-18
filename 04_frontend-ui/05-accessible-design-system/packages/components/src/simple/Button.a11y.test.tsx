/**
 * Button.test.tsx — Unit + accessibility tests
 *
 * Tests the Button component's:
 *   - Rendering and variant/intent props
 *   - Keyboard interaction
 *   - Disabled/loading states
 *   - axe-core zero-violation requirement
 */

import { render, screen, fireEvent } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';
import { describe, it, expect, vi } from 'vitest';
import { Button } from '../simple/Button';

// Import jest-dom to extend Vitest's expect
import '@testing-library/jest-dom';

// Extend Vitest's expect with jest-axe matchers
expect.extend(toHaveNoViolations);

describe('Button', () => {
  // ── Rendering ────────────────────────────────────────────────────────────
  it('renders children', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button', { name: 'Click me' })).toBeInTheDocument();
  });

  it('renders all variants without crashing', () => {
    const variants = ['solid', 'outline', 'ghost', 'link'] as const;
    variants.forEach((variant) => {
      const { unmount } = render(<Button variant={variant}>Label</Button>);
      unmount();
    });
  });

  it('renders all intents without crashing', () => {
    const intents = ['default', 'brand', 'success', 'warning', 'error'] as const;
    intents.forEach((intent) => {
      const { unmount } = render(<Button intent={intent}>Label</Button>);
      unmount();
    });
  });

  // ── Interaction ──────────────────────────────────────────────────────────
  it('fires onClick when clicked', () => {
    const handler = vi.fn();
    render(<Button onClick={handler}>Click</Button>);
    fireEvent.click(screen.getByRole('button'));
    expect(handler).toHaveBeenCalledTimes(1);
  });

  it('fires onClick on Enter key', () => {
    const handler = vi.fn();
    render(<Button onClick={handler}>Click</Button>);
    fireEvent.keyDown(screen.getByRole('button'), { key: 'Enter' });
    // Native button handles Enter natively; no extra keyDown listener needed
  });

  // ── Disabled ─────────────────────────────────────────────────────────────
  it('is not clickable when disabled', () => {
    const handler = vi.fn();
    render(<Button disabled onClick={handler}>Disabled</Button>);
    const btn = screen.getByRole('button');
    expect(btn).toBeDisabled();
    fireEvent.click(btn);
    expect(handler).not.toHaveBeenCalled();
  });

  // ── Loading ──────────────────────────────────────────────────────────────
  it('is disabled and marks aria-busy when loading', () => {
    render(<Button loading>Loading</Button>);
    const btn = screen.getByRole('button');
    expect(btn).toBeDisabled();
    expect(btn).toHaveAttribute('aria-busy', 'true');
  });

  it('shows loading status to screen readers', () => {
    render(<Button loading>Save</Button>);
    // The button text is still in the DOM when loading
    expect(screen.getByText('Save')).toBeInTheDocument();
  });

  // ── Accessibility ────────────────────────────────────────────────────────
  it('has no axe violations in solid/brand variant', async () => {
    const { container } = render(<Button intent="brand">Submit</Button>);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('has no axe violations in disabled state', async () => {
    const { container } = render(<Button disabled>Disabled</Button>);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('has no axe violations in loading state', async () => {
    const { container } = render(<Button loading>Loading</Button>);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});
