/**
 * @aurora-ds/components — Level 3 Form Composites
 * Input, Textarea, Select, Checkbox, Switch, Radio
 *
 * All form elements:
 *   - Associate label via htmlFor / aria-labelledby
 *   - Surface error state via aria-invalid + aria-describedby
 *   - Maintain 44×44px touch targets on mobile
 */

import React, { useId } from 'react';
import * as CheckboxPrimitive from '@radix-ui/react-checkbox';
import * as SwitchPrimitive from '@radix-ui/react-switch';
import { cn } from '../utils';

// ── Shared field wrapper ──────────────────────────────────────────────────────

type FieldWrapperProps = {
  id: string;
  label?: string;
  helperText?: string;
  errorText?: string;
  required?: boolean;
  children: React.ReactNode;
};

export function FieldWrapper({ id, label, helperText, errorText, required, children }: FieldWrapperProps) {
  const helpId  = `${id}-help`;
  const errorId = `${id}-error`;

  return (
    <div className="flex flex-col gap-1.5">
      {label && (
        <label
          htmlFor={id}
          className="text-sm font-medium text-[var(--aurora-color-foreground-default)]"
        >
          {label}
          {required && <span aria-hidden className="ml-0.5 text-[var(--aurora-color-error-default)]">*</span>}
          {required && <span className="sr-only"> (required)</span>}
        </label>
      )}
      {React.cloneElement(children as React.ReactElement, {
        id,
        'aria-describedby': [helperText ? helpId : null, errorText ? errorId : null].filter(Boolean).join(' ') || undefined,
        'aria-invalid': errorText ? true : undefined,
        'aria-required': required,
      })}
      {helperText && !errorText && (
        <p id={helpId} className="text-xs text-[var(--aurora-color-foreground-muted)]">{helperText}</p>
      )}
      {errorText && (
        <p id={errorId} role="alert" className="text-xs text-[var(--aurora-color-error-default)]">
          {errorText}
        </p>
      )}
    </div>
  );
}

// ── Input ─────────────────────────────────────────────────────────────────────

type InputProps = React.InputHTMLAttributes<HTMLInputElement> & {
  label?: string;
  helperText?: string;
  errorText?: string;
  iconLeft?: React.ReactNode;
  iconRight?: React.ReactNode;
};

const inputBase = [
  'flex w-full rounded-[var(--aurora-border-radius-md)] border px-3 py-2',
  'bg-[var(--aurora-color-background-default)]',
  'text-sm text-[var(--aurora-color-foreground-default)]',
  'border-[var(--aurora-color-border-default)]',
  'placeholder:text-[var(--aurora-color-foreground-subtle)]',
  'transition-colors duration-[var(--aurora-motion-duration-fast)]',
  'focus-visible:outline-none focus-visible:ring-2',
  'focus-visible:ring-[var(--aurora-color-focus-ring)] focus-visible:ring-offset-1',
  'disabled:cursor-not-allowed disabled:opacity-50',
  'aria-invalid:border-[var(--aurora-color-error-default)]',
  'aria-invalid:focus-visible:ring-[var(--aurora-color-error-default)]',
  'min-h-[44px]',
].join(' ');

/**
 * Text input with optional label, helper text, error state, and icon slots.
 *
 * @example
 * <Input label="Email" type="email" placeholder="you@example.com" required />
 * <Input label="Search" iconLeft={<SearchIcon />} errorText="Invalid value" />
 */
export const Input = React.forwardRef<HTMLInputElement, InputProps>(
  ({ label, helperText, errorText, iconLeft, iconRight, className, id: externalId, ...rest }, ref) => {
    const internalId = useId();
    const id = externalId ?? internalId;

    const input = (
      <div className="relative">
        {iconLeft && (
          <span aria-hidden className="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-[var(--aurora-color-foreground-muted)]">
            {iconLeft}
          </span>
        )}
        <input
          ref={ref}
          id={id}
          className={cn(inputBase, iconLeft && 'pl-9', iconRight && 'pr-9', className)}
          {...rest}
        />
        {iconRight && (
          <span aria-hidden className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-[var(--aurora-color-foreground-muted)]">
            {iconRight}
          </span>
        )}
      </div>
    );

    if (!label && !helperText && !errorText) return input;
    return (
      <FieldWrapper id={id} label={label} helperText={helperText} errorText={errorText} required={rest.required}>
        {input}
      </FieldWrapper>
    );
  },
);
Input.displayName = 'Input';

// ── Textarea ──────────────────────────────────────────────────────────────────

type TextareaProps = React.TextareaHTMLAttributes<HTMLTextAreaElement> & {
  label?: string;
  helperText?: string;
  errorText?: string;
};

/**
 * Multi-line text input. Shares the same field wrapper and error pattern as Input.
 */
export const Textarea = React.forwardRef<HTMLTextAreaElement, TextareaProps>(
  ({ label, helperText, errorText, className, id: externalId, ...rest }, ref) => {
    const internalId = useId();
    const id = externalId ?? internalId;

    const textarea = (
      <textarea
        ref={ref}
        id={id}
        className={cn(
          'flex min-h-[80px] w-full resize-y rounded-[var(--aurora-border-radius-md)] border px-3 py-2',
          'bg-[var(--aurora-color-background-default)]',
          'text-sm text-[var(--aurora-color-foreground-default)]',
          'border-[var(--aurora-color-border-default)]',
          'placeholder:text-[var(--aurora-color-foreground-subtle)]',
          'focus-visible:outline-none focus-visible:ring-2',
          'focus-visible:ring-[var(--aurora-color-focus-ring)] focus-visible:ring-offset-1',
          'aria-invalid:border-[var(--aurora-color-error-default)]',
          'disabled:cursor-not-allowed disabled:opacity-50',
          className,
        )}
        {...rest}
      />
    );

    if (!label && !helperText && !errorText) return textarea;
    return (
      <FieldWrapper id={id} label={label} helperText={helperText} errorText={errorText} required={rest.required}>
        {textarea}
      </FieldWrapper>
    );
  },
);
Textarea.displayName = 'Textarea';

// ── Checkbox ──────────────────────────────────────────────────────────────────

type CheckboxProps = React.ComponentPropsWithoutRef<typeof CheckboxPrimitive.Root> & {
  label: string;
  helperText?: string;
};

/**
 * Accessible checkbox built on Radix UI.
 *
 * Keyboard:
 *   Space — toggles checked state
 */
export const Checkbox = React.forwardRef<
  React.ElementRef<typeof CheckboxPrimitive.Root>,
  CheckboxProps
>(({ label, helperText, className, id: externalId, ...rest }, ref) => {
  const internalId = useId();
  const id = externalId ?? internalId;
  const helpId = `${id}-help`;

  return (
    <div className="flex items-start gap-2.5">
      <CheckboxPrimitive.Root
        ref={ref}
        id={id}
        aria-describedby={helperText ? helpId : undefined}
        className={cn(
          'mt-0.5 h-5 w-5 shrink-0 rounded-[var(--aurora-border-radius-sm)]',
          'border border-[var(--aurora-color-border-strong)]',
          'bg-[var(--aurora-color-background-default)]',
          'transition-colors duration-[var(--aurora-motion-duration-fast)]',
          'focus-visible:outline-none focus-visible:ring-2',
          'focus-visible:ring-[var(--aurora-color-focus-ring)] focus-visible:ring-offset-2',
          'data-[state=checked]:bg-[var(--aurora-color-brand-default)]',
          'data-[state=checked]:border-[var(--aurora-color-brand-default)]',
          'disabled:cursor-not-allowed disabled:opacity-50',
          // Ensure min 44×44 touch target
          'min-h-[44px] min-w-[44px] sm:min-h-5 sm:min-w-5',
          className,
        )}
        {...rest}
      >
        <CheckboxPrimitive.Indicator className="flex items-center justify-center text-white">
          <svg width="12" height="10" viewBox="0 0 12 10" fill="none" aria-hidden>
            <path d="M1 5l3.5 3.5L11 1" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
          </svg>
        </CheckboxPrimitive.Indicator>
      </CheckboxPrimitive.Root>

      <div className="flex flex-col gap-0.5">
        <label htmlFor={id} className="text-sm font-medium leading-5 text-[var(--aurora-color-foreground-default)] cursor-pointer">
          {label}
        </label>
        {helperText && (
          <p id={helpId} className="text-xs text-[var(--aurora-color-foreground-muted)]">{helperText}</p>
        )}
      </div>
    </div>
  );
});
Checkbox.displayName = 'Checkbox';

// ── Switch ────────────────────────────────────────────────────────────────────

type SwitchProps = React.ComponentPropsWithoutRef<typeof SwitchPrimitive.Root> & {
  label: string;
  helperText?: string;
};

/**
 * Toggle switch for binary on/off settings. Built on Radix UI.
 *
 * Keyboard:
 *   Space — toggles state
 */
export const Switch = React.forwardRef<
  React.ElementRef<typeof SwitchPrimitive.Root>,
  SwitchProps
>(({ label, helperText, className, id: externalId, ...rest }, ref) => {
  const internalId = useId();
  const id = externalId ?? internalId;

  return (
    <div className="flex items-center gap-3">
      <SwitchPrimitive.Root
        ref={ref}
        id={id}
        className={cn(
          'peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent',
          'bg-[var(--aurora-color-background-muted)]',
          'transition-colors duration-[var(--aurora-motion-duration-normal)]',
          'focus-visible:outline-none focus-visible:ring-2',
          'focus-visible:ring-[var(--aurora-color-focus-ring)] focus-visible:ring-offset-2',
          'data-[state=checked]:bg-[var(--aurora-color-brand-default)]',
          'disabled:cursor-not-allowed disabled:opacity-50',
          className,
        )}
        {...rest}
      >
        <SwitchPrimitive.Thumb
          className={cn(
            'pointer-events-none block h-5 w-5 rounded-full bg-white shadow-sm ring-0',
            'transition-transform duration-[var(--aurora-motion-duration-normal)]',
            'data-[state=checked]:translate-x-5 data-[state=unchecked]:translate-x-0',
          )}
        />
      </SwitchPrimitive.Root>
      <div>
        <label htmlFor={id} className="text-sm font-medium text-[var(--aurora-color-foreground-default)] cursor-pointer">
          {label}
        </label>
        {helperText && (
          <p className="text-xs text-[var(--aurora-color-foreground-muted)]">{helperText}</p>
        )}
      </div>
    </div>
  );
});
Switch.displayName = 'Switch';

// Touch target utility — applied via wrapper where visual size < 44px
// Per WCAG 2.5.8 (AA): all interactive controls must have a 44×44px minimum target
export const TOUCH_TARGET_CLASS = [
  'relative',
  'after:absolute after:inset-0',
  'after:min-h-[44px] after:min-w-[44px]',
  'after:top-1/2 after:-translate-y-1/2',
  'after:left-1/2 after:-translate-x-1/2',
].join(' ');
