/**
 * @aurora-ds/components — Simple Components
 * Badge, Avatar, Spinner, ProgressBar, Skeleton
 */

import React from 'react';
import { cva, type VariantProps } from 'class-variance-authority';
import { cn } from '../utils';

// ── Badge ─────────────────────────────────────────────────────────────────────

const badgeVariants = cva(
  'inline-flex items-center gap-1 rounded-full font-medium leading-none',
  {
    variants: {
      variant: {
        solid:   '',
        outline: 'border bg-transparent',
        subtle:  '',
      },
      intent: {
        default: '',
        brand:   '',
        success: '',
        warning: '',
        error:   '',
      },
      size: {
        sm: 'px-2 py-0.5 text-xs',
        md: 'px-2.5 py-1 text-xs',
        lg: 'px-3 py-1 text-sm',
      },
    },
    compoundVariants: [
      { variant: 'solid',   intent: 'default', className: 'bg-[var(--aurora-color-background-muted)] text-[var(--aurora-color-foreground-default)]' },
      { variant: 'solid',   intent: 'brand',   className: 'bg-[var(--aurora-color-brand-default)] text-white' },
      { variant: 'solid',   intent: 'success', className: 'bg-[var(--aurora-color-success-default)] text-white' },
      { variant: 'solid',   intent: 'warning', className: 'bg-[var(--aurora-color-warning-default)] text-white' },
      { variant: 'solid',   intent: 'error',   className: 'bg-[var(--aurora-color-error-default)] text-white' },
      { variant: 'subtle',  intent: 'default', className: 'bg-[var(--aurora-color-background-subtle)] text-[var(--aurora-color-foreground-muted)]' },
      { variant: 'subtle',  intent: 'brand',   className: 'bg-[var(--aurora-color-brand-subtle)] text-[var(--aurora-color-brand-default)]' },
      { variant: 'subtle',  intent: 'success', className: 'bg-[var(--aurora-color-success-subtle)] text-[var(--aurora-color-success-default)]' },
      { variant: 'subtle',  intent: 'error',   className: 'bg-[var(--aurora-color-error-subtle)] text-[var(--aurora-color-error-default)]' },
      { variant: 'outline', intent: 'default', className: 'border-[var(--aurora-color-border-default)] text-[var(--aurora-color-foreground-default)]' },
      { variant: 'outline', intent: 'brand',   className: 'border-[var(--aurora-color-brand-default)] text-[var(--aurora-color-brand-default)]' },
      { variant: 'outline', intent: 'error',   className: 'border-[var(--aurora-color-error-default)] text-[var(--aurora-color-error-default)]' },
    ],
    defaultVariants: { variant: 'subtle', intent: 'default', size: 'md' },
  },
);

export type BadgeProps = React.HTMLAttributes<HTMLSpanElement> &
  VariantProps<typeof badgeVariants>;

/** Non-interactive label pill for status, category, or count display. */
export const Badge = React.forwardRef<HTMLSpanElement, BadgeProps>(
  ({ variant, intent, size, className, ...rest }, ref) => (
    <span ref={ref} className={cn(badgeVariants({ variant, intent, size }), className)} {...rest} />
  ),
);
Badge.displayName = 'Badge';

// ── Avatar ────────────────────────────────────────────────────────────────────

type AvatarProps = React.HTMLAttributes<HTMLSpanElement> & {
  src?: string;
  alt: string;
  fallback?: string;
  size?: 'xs' | 'sm' | 'md' | 'lg' | 'xl';
};

const AVATAR_SIZE: Record<string, string> = {
  xs: 'h-6 w-6 text-xs', sm: 'h-8 w-8 text-sm', md: 'h-10 w-10 text-sm',
  lg: 'h-12 w-12 text-base', xl: 'h-16 w-16 text-xl',
};

/**
 * User or entity avatar. Renders an image when `src` is provided; falls back to
 * initials derived from `alt`, then a generic icon.
 *
 * Accessibility: always provide a descriptive `alt`.
 */
export const Avatar = React.forwardRef<HTMLSpanElement, AvatarProps>(
  ({ src, alt, fallback, size = 'md', className, ...rest }, ref) => {
    const initials = fallback ?? alt.split(' ').map(w => w[0]).join('').slice(0, 2).toUpperCase();

    return (
      <span
        ref={ref}
        role="img"
        aria-label={alt}
        className={cn(
          'inline-flex items-center justify-center rounded-full',
          'bg-[var(--aurora-color-background-muted)] text-[var(--aurora-color-foreground-muted)]',
          'font-semibold overflow-hidden select-none shrink-0',
          AVATAR_SIZE[size],
          className,
        )}
        {...rest}
      >
        {src ? (
          <img src={src} alt="" aria-hidden className="h-full w-full object-cover" />
        ) : (
          <span aria-hidden>{initials}</span>
        )}
      </span>
    );
  },
);
Avatar.displayName = 'Avatar';

// ── Spinner ───────────────────────────────────────────────────────────────────

type SpinnerProps = React.SVGAttributes<SVGElement> & {
  size?: 'xs' | 'sm' | 'md' | 'lg';
  label?: string;
};

const SPINNER_SIZE: Record<string, string> = {
  xs: 'h-3 w-3', sm: 'h-4 w-4', md: 'h-6 w-6', lg: 'h-8 w-8',
};

/**
 * Accessible loading indicator. Renders a visually-hidden `role="status"` label
 * for screen readers.
 */
export function Spinner({ size = 'md', label = 'Loading…', className, ...rest }: SpinnerProps) {
  return (
    <span role="status">
      <svg
        className={cn('animate-spin text-[var(--aurora-color-brand-default)]', SPINNER_SIZE[size], className)}
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        aria-hidden="true"
        {...rest}
      >
        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
      </svg>
      <span className="sr-only">{label}</span>
    </span>
  );
}

// ── ProgressBar ───────────────────────────────────────────────────────────────

type ProgressBarProps = React.HTMLAttributes<HTMLDivElement> & {
  value: number;
  max?: number;
  label?: string;
  intent?: 'default' | 'brand' | 'success' | 'warning' | 'error';
  size?: 'sm' | 'md' | 'lg';
};

const PROGRESS_INTENT: Record<string, string> = {
  default: 'bg-[var(--aurora-color-foreground-muted)]',
  brand:   'bg-[var(--aurora-color-brand-default)]',
  success: 'bg-[var(--aurora-color-success-default)]',
  warning: 'bg-[var(--aurora-color-warning-default)]',
  error:   'bg-[var(--aurora-color-error-default)]',
};

const PROGRESS_SIZE: Record<string, string> = {
  sm: 'h-1', md: 'h-2', lg: 'h-3',
};

/**
 * ARIA-compliant progress bar.
 *
 * @example
 * <ProgressBar value={72} label="Upload progress" intent="brand" />
 */
export const ProgressBar = React.forwardRef<HTMLDivElement, ProgressBarProps>(
  ({ value, max = 100, label, intent = 'brand', size = 'md', className, ...rest }, ref) => {
    const pct = Math.min(100, Math.max(0, (value / max) * 100));
    return (
      <div
        ref={ref}
        role="progressbar"
        aria-valuenow={value}
        aria-valuemin={0}
        aria-valuemax={max}
        aria-label={label}
        className={cn(
          'w-full overflow-hidden rounded-full bg-[var(--aurora-color-background-muted)]',
          PROGRESS_SIZE[size],
          className,
        )}
        {...rest}
      >
        <div
          className={cn('h-full rounded-full transition-[width] duration-[var(--aurora-motion-duration-slow)]', PROGRESS_INTENT[intent])}
          style={{ width: `${pct}%` }}
        />
      </div>
    );
  },
);
ProgressBar.displayName = 'ProgressBar';

// ── Skeleton ──────────────────────────────────────────────────────────────────

type SkeletonProps = React.HTMLAttributes<HTMLDivElement>;

/**
 * Loading placeholder that pulses to indicate content is loading.
 * Place in the same location and approximate size as the expected content.
 */
export const Skeleton = React.forwardRef<HTMLDivElement, SkeletonProps>(
  ({ className, ...rest }, ref) => (
    <div
      ref={ref}
      aria-hidden="true"
      className={cn(
        'animate-pulse rounded-[var(--aurora-border-radius-md)]',
        'bg-[var(--aurora-color-background-muted)]',
        className,
      )}
      {...rest}
    />
  ),
);
Skeleton.displayName = 'Skeleton';
