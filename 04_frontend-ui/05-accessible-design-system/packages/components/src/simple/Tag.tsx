/**
 * @aurora-ds/components — Tag
 *
 * Interactive dismissible label chip, typically used in multi-select inputs,
 * filter bars, and tag lists. Distinguishable from Badge by its dismiss affordance.
 *
 * Accessibility:
 *   - The dismiss button has an aria-label that includes the tag's text
 *   - Keyboard: Tab to focus, Enter/Space to activate dismiss
 */

import React from 'react';
import { CloseIcon } from '@aurora-ds/icons';
import { cn } from '../utils';

type TagProps = {
  label: string;
  onDismiss?: () => void;
  disabled?: boolean;
  intent?: 'default' | 'brand' | 'success' | 'warning' | 'error';
  className?: string;
};

const INTENT_CLASSES: Record<string, string> = {
  default: 'bg-[var(--aurora-color-background-muted)] text-[var(--aurora-color-foreground-default)] border-[var(--aurora-color-border-default)]',
  brand:   'bg-[var(--aurora-color-brand-subtle)] text-[var(--aurora-color-brand-default)] border-[var(--aurora-color-brand-default)]/30',
  success: 'bg-[var(--aurora-color-success-subtle)] text-[var(--aurora-color-success-default)] border-[var(--aurora-color-success-default)]/30',
  warning: 'bg-[var(--aurora-color-warning-default)]/10 text-[var(--aurora-color-warning-default)] border-[var(--aurora-color-warning-default)]/30',
  error:   'bg-[var(--aurora-color-error-subtle)] text-[var(--aurora-color-error-default)] border-[var(--aurora-color-error-default)]/30',
};

export const Tag = React.forwardRef<HTMLSpanElement, TagProps>(
  ({ label, onDismiss, disabled = false, intent = 'default', className }, ref) => (
    <span
      ref={ref}
      className={cn(
        'inline-flex items-center gap-1 rounded-full border px-2.5 py-0.5 text-xs font-medium',
        'transition-colors duration-[var(--aurora-motion-duration-fast)]',
        INTENT_CLASSES[intent],
        disabled && 'opacity-50',
        className,
      )}
    >
      {label}
      {onDismiss && (
        <button
          type="button"
          onClick={disabled ? undefined : onDismiss}
          disabled={disabled}
          aria-label={`Remove ${label}`}
          className={cn(
            'ml-0.5 rounded-full p-0.5 -mr-1',
            'hover:bg-black/10 dark:hover:bg-white/10',
            'focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-current',
            'disabled:cursor-not-allowed',
            // Ensure 44px touch target on mobile
            'min-h-[44px] min-w-[44px] sm:min-h-4 sm:min-w-4',
            'flex items-center justify-center',
          )}
        >
          <CloseIcon size={10} aria-hidden />
        </button>
      )}
    </span>
  )
);
Tag.displayName = 'Tag';
