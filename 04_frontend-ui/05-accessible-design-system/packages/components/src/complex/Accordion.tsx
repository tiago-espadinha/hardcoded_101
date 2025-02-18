/**
 * @aurora-ds/components — Accordion
 *
 * Disclosure component for hiding/showing sections of content.
 * Built on Radix UI Accordion for correct ARIA expanded/collapsed state.
 *
 * Keyboard:
 *   Space / Enter — toggles the focused item
 *   Tab           — moves to next focusable element
 *   Arrow Down/Up — moves focus between accordion triggers (when type="single")
 *   Home / End    — moves focus to first / last trigger
 */

import React from 'react';
import * as AccordionPrimitive from '@radix-ui/react-accordion';
import { ChevronDownIcon } from '@aurora-ds/icons';
import { cn } from '../utils';

export type AccordionItem = {
  value: string;
  trigger: React.ReactNode;
  content: React.ReactNode;
  disabled?: boolean;
};

type AccordionProps = {
  items: AccordionItem[];
  type?: 'single' | 'multiple';
  defaultValue?: string | string[];
  className?: string;
};

export function Accordion({ items, type = 'single', defaultValue, className }: AccordionProps) {
  const commonProps = { className: cn('divide-y divide-[var(--aurora-color-border-default)] border-b border-t border-[var(--aurora-color-border-default)]', className) };

  const content = items.map(({ value, trigger, content: body, disabled }) => (
    <AccordionPrimitive.Item key={value} value={value} disabled={disabled} className="group">
      <AccordionPrimitive.Header>
        <AccordionPrimitive.Trigger
          className={cn(
            'flex w-full items-center justify-between py-4 px-1',
            'text-sm font-medium text-[var(--aurora-color-foreground-default)]',
            'transition-colors hover:text-[var(--aurora-color-brand-default)]',
            'focus-visible:outline-none focus-visible:ring-2',
            'focus-visible:ring-[var(--aurora-color-focus-ring)] focus-visible:ring-inset focus-visible:rounded-sm',
            'disabled:pointer-events-none disabled:opacity-50',
            '[&[data-state=open]>svg]:rotate-180',
          )}
        >
          {trigger}
          <ChevronDownIcon
            size={16}
            aria-hidden
            className="shrink-0 text-[var(--aurora-color-foreground-muted)] transition-transform duration-[var(--aurora-motion-duration-normal)]"
          />
        </AccordionPrimitive.Trigger>
      </AccordionPrimitive.Header>
      <AccordionPrimitive.Content
        className={cn(
          'overflow-hidden text-sm text-[var(--aurora-color-foreground-muted)]',
          'data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down',
        )}
      >
        <div className="pb-4 pt-0 px-1">{body}</div>
      </AccordionPrimitive.Content>
    </AccordionPrimitive.Item>
  ));

  if (type === 'multiple') {
    return (
      <AccordionPrimitive.Root type="multiple" defaultValue={defaultValue as string[] | undefined} {...commonProps}>
        {content}
      </AccordionPrimitive.Root>
    );
  }

  return (
    <AccordionPrimitive.Root
      type="single"
      collapsible
      defaultValue={Array.isArray(defaultValue) ? defaultValue[0] : defaultValue}
      {...commonProps}
    >
      {content}
    </AccordionPrimitive.Root>
  );
}
