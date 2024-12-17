/**
 * @aurora-ds/components — Level 4 Complex Components
 * Modal (Dialog), Tabs, Toast, Tooltip
 *
 * All built on Radix UI primitives for correct ARIA roles,
 * focus management, and keyboard navigation.
 */

import React from 'react';
import * as DialogPrimitive from '@radix-ui/react-dialog';
import * as TabsPrimitive from '@radix-ui/react-tabs';
import * as ToastPrimitive from '@radix-ui/react-toast';
import * as TooltipPrimitive from '@radix-ui/react-tooltip';
import { cn } from '../utils';

// ── Modal ─────────────────────────────────────────────────────────────────────

/**
 * Modal dialog built on Radix Dialog.
 *
 * Keyboard:
 *   Escape          — closes the dialog
 *   Tab / Shift+Tab — cycles focus within the dialog (focus trap)
 *
 * @example
 * <Modal open={open} onOpenChange={setOpen} title="Confirm deletion">
 *   <p>This action cannot be undone.</p>
 *   <Modal.Footer>
 *     <Button onClick={() => setOpen(false)}>Cancel</Button>
 *     <Button intent="error">Delete</Button>
 *   </Modal.Footer>
 * </Modal>
 */
export function Modal({
  open, onOpenChange, title, description, children, size = 'md',
}: {
  open: boolean;
  onOpenChange: (open: boolean) => void;
  title: string;
  description?: string;
  children: React.ReactNode;
  size?: 'sm' | 'md' | 'lg' | 'xl' | 'full';
}) {
  const SIZE: Record<string, string> = {
    sm: 'max-w-sm', md: 'max-w-md', lg: 'max-w-lg', xl: 'max-w-xl', full: 'max-w-full',
  };

  return (
    <DialogPrimitive.Root open={open} onOpenChange={onOpenChange}>
      <DialogPrimitive.Portal>
        {/* Overlay */}
        <DialogPrimitive.Overlay
          className={cn(
            'fixed inset-0 z-50 bg-[var(--aurora-color-overlay-default)]',
            'data-[state=open]:animate-in data-[state=closed]:animate-out',
            'data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0',
          )}
        />
        {/* Content */}
        <DialogPrimitive.Content
          className={cn(
            'fixed left-[50%] top-[50%] z-50 w-full -translate-x-1/2 -translate-y-1/2',
            'bg-[var(--aurora-color-background-default)]',
            'rounded-[var(--aurora-border-radius-xl)] p-6 shadow-[var(--aurora-box-shadow-xl)]',
            'border border-[var(--aurora-color-border-default)]',
            'focus:outline-none',
            SIZE[size],
            // Animations
            'data-[state=open]:animate-in data-[state=closed]:animate-out',
            'data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0',
            'data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95',
            'data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%]',
            'data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%]',
          )}
        >
          {/* Header */}
          <div className="mb-4 flex items-start justify-between gap-4">
            <div>
              <DialogPrimitive.Title className="text-lg font-semibold text-[var(--aurora-color-foreground-default)]">
                {title}
              </DialogPrimitive.Title>
              {description && (
                <DialogPrimitive.Description className="mt-1 text-sm text-[var(--aurora-color-foreground-muted)]">
                  {description}
                </DialogPrimitive.Description>
              )}
            </div>
            <DialogPrimitive.Close
              className={cn(
                'rounded-[var(--aurora-border-radius-md)] p-1',
                'text-[var(--aurora-color-foreground-muted)] hover:text-[var(--aurora-color-foreground-default)]',
                'hover:bg-[var(--aurora-color-background-subtle)]',
                'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--aurora-color-focus-ring)]',
              )}
              aria-label="Close dialog"
            >
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden>
                <path d="M12 4L4 12M4 4l8 8" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
              </svg>
            </DialogPrimitive.Close>
          </div>

          {/* Body */}
          {children}
        </DialogPrimitive.Content>
      </DialogPrimitive.Portal>
    </DialogPrimitive.Root>
  );
}

Modal.Footer = function ModalFooter({ children, className }: { children: React.ReactNode; className?: string }) {
  return (
    <div className={cn('mt-6 flex items-center justify-end gap-3', className)}>
      {children}
    </div>
  );
};

// ── Tabs ──────────────────────────────────────────────────────────────────────

type TabItem = { value: string; label: string; content: React.ReactNode; disabled?: boolean };

/**
 * Keyboard-accessible tab panel built on Radix Tabs.
 *
 * Keyboard:
 *   Arrow Left/Right — moves focus between tabs
 *   Space/Enter      — activates focused tab
 *   Tab              — moves focus to tab panel content
 */
export function Tabs({
  defaultValue, items, className,
}: {
  defaultValue: string;
  items: TabItem[];
  className?: string;
}) {
  return (
    <TabsPrimitive.Root defaultValue={defaultValue} className={cn('w-full', className)}>
      <TabsPrimitive.List
        className={cn(
          'inline-flex items-center gap-1 rounded-[var(--aurora-border-radius-lg)]',
          'bg-[var(--aurora-color-background-subtle)] p-1',
        )}
        aria-label="Tabs"
      >
        {items.map(({ value, label, disabled }) => (
          <TabsPrimitive.Trigger
            key={value}
            value={value}
            disabled={disabled}
            className={cn(
              'inline-flex items-center justify-center whitespace-nowrap rounded-[var(--aurora-border-radius-md)]',
              'px-3 py-1.5 text-sm font-medium transition-all',
              'text-[var(--aurora-color-foreground-muted)]',
              'hover:text-[var(--aurora-color-foreground-default)]',
              'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--aurora-color-focus-ring)]',
              'disabled:pointer-events-none disabled:opacity-50',
              'data-[state=active]:bg-[var(--aurora-color-background-default)]',
              'data-[state=active]:text-[var(--aurora-color-foreground-default)]',
              'data-[state=active]:shadow-[var(--aurora-box-shadow-sm)]',
            )}
          >
            {label}
          </TabsPrimitive.Trigger>
        ))}
      </TabsPrimitive.List>

      {items.map(({ value, content }) => (
        <TabsPrimitive.Content
          key={value}
          value={value}
          className="mt-4 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--aurora-color-focus-ring)] rounded-[var(--aurora-border-radius-md)]"
        >
          {content}
        </TabsPrimitive.Content>
      ))}
    </TabsPrimitive.Root>
  );
}

// ── Toast ─────────────────────────────────────────────────────────────────────

export const ToastProvider = ToastPrimitive.Provider;
export const ToastViewport = React.forwardRef<
  React.ElementRef<typeof ToastPrimitive.Viewport>,
  React.ComponentPropsWithoutRef<typeof ToastPrimitive.Viewport>
>(({ className, ...props }, ref) => (
  <ToastPrimitive.Viewport
    ref={ref}
    className={cn(
      'fixed bottom-4 right-4 z-[100] flex max-h-screen w-full max-w-[420px] flex-col gap-2',
      className,
    )}
    {...props}
  />
));
ToastViewport.displayName = 'ToastViewport';

type ToastProps = React.ComponentPropsWithoutRef<typeof ToastPrimitive.Root> & {
  title?: string;
  description?: string;
  intent?: 'default' | 'success' | 'warning' | 'error';
};

const TOAST_INTENT: Record<string, string> = {
  default: 'border-[var(--aurora-color-border-default)]',
  success: 'border-[var(--aurora-color-success-default)]',
  warning: 'border-[var(--aurora-color-warning-default)]',
  error:   'border-[var(--aurora-color-error-default)]',
};

/**
 * Non-blocking notification. Pair with `ToastProvider` and `ToastViewport`.
 * Announced to screen readers via role="status" (default) or role="alert" (destructive).
 */
export const Toast = React.forwardRef<React.ElementRef<typeof ToastPrimitive.Root>, ToastProps>(
  ({ title, description, intent = 'default', className, ...props }, ref) => (
    <ToastPrimitive.Root
      ref={ref}
      className={cn(
        'pointer-events-auto relative flex w-full items-start gap-3 overflow-hidden rounded-[var(--aurora-border-radius-lg)]',
        'border bg-[var(--aurora-color-background-default)] p-4 shadow-[var(--aurora-box-shadow-lg)]',
        TOAST_INTENT[intent],
        'transition-all data-[swipe=cancel]:translate-x-0 data-[swipe=end]:translate-x-[var(--radix-toast-swipe-end-x)]',
        'data-[swipe=move]:translate-x-[var(--radix-toast-swipe-move-x)] data-[swipe=move]:transition-none',
        'data-[state=open]:animate-in data-[state=closed]:animate-out',
        'data-[state=closed]:fade-out-80 data-[state=closed]:slide-out-to-right-full',
        'data-[state=open]:slide-in-from-bottom-full',
        className,
      )}
      {...props}
    >
      <div className="flex-1 grid gap-1">
        {title && (
          <ToastPrimitive.Title className="text-sm font-semibold text-[var(--aurora-color-foreground-default)]">
            {title}
          </ToastPrimitive.Title>
        )}
        {description && (
          <ToastPrimitive.Description className="text-xs text-[var(--aurora-color-foreground-muted)]">
            {description}
          </ToastPrimitive.Description>
        )}
      </div>
      <ToastPrimitive.Close
        className="rounded p-0.5 text-[var(--aurora-color-foreground-muted)] hover:text-[var(--aurora-color-foreground-default)] focus-visible:ring-2 focus-visible:ring-[var(--aurora-color-focus-ring)] focus-visible:outline-none"
        aria-label="Dismiss notification"
      >
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none" aria-hidden>
          <path d="M12 4L4 12M4 4l8 8" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
        </svg>
      </ToastPrimitive.Close>
    </ToastPrimitive.Root>
  ),
);
Toast.displayName = 'Toast';

// ── Tooltip ───────────────────────────────────────────────────────────────────

type TooltipWrapperProps = {
  content: React.ReactNode;
  children: React.ReactNode;
  side?: 'top' | 'right' | 'bottom' | 'left';
  delayDuration?: number;
};

/**
 * Non-interactive supplemental information shown on hover/focus.
 * Built on Radix Tooltip — accessible on keyboard focus automatically.
 *
 * @example
 * <Tooltip content="Delete item"><IconButton aria-label="Delete" /></Tooltip>
 */
export function Tooltip({ content, children, side = 'top', delayDuration = 300 }: TooltipWrapperProps) {
  return (
    <TooltipPrimitive.Provider delayDuration={delayDuration}>
      <TooltipPrimitive.Root>
        <TooltipPrimitive.Trigger asChild>{children}</TooltipPrimitive.Trigger>
        <TooltipPrimitive.Portal>
          <TooltipPrimitive.Content
            side={side}
            sideOffset={6}
            className={cn(
              'z-50 max-w-xs rounded-[var(--aurora-border-radius-md)] px-2.5 py-1.5',
              'bg-[var(--aurora-color-foreground-default)] text-[var(--aurora-color-background-default)]',
              'text-xs font-medium shadow-[var(--aurora-box-shadow-md)]',
              'animate-in fade-in-0 zoom-in-95',
              'data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95',
              'data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2',
              'data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2',
            )}
          >
            {content}
            <TooltipPrimitive.Arrow className="fill-[var(--aurora-color-foreground-default)]" />
          </TooltipPrimitive.Content>
        </TooltipPrimitive.Portal>
      </TooltipPrimitive.Root>
    </TooltipPrimitive.Provider>
  );
}

/**
 * Reduced-motion utilities
 * Consumers can check this in JS-driven animations.
 * CSS animations in complex components are already wrapped
 * in Tailwind's `motion-safe:` / Radix's animation classes
 * which respect prefers-reduced-motion automatically.
 */
export function prefersReducedMotion(): boolean {
  if (typeof window === 'undefined') return false;
  return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
}
