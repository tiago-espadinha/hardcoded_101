/**
 * @aurora-ds/components — Select
 *
 * Accessible single-value select built on Radix UI Select.
 *
 * Keyboard:
 *   Space / Enter / ArrowDown — opens the listbox
 *   ArrowUp / ArrowDown       — navigates options
 *   Enter / Space             — selects focused option
 *   Escape                    — closes without selecting
 *   Home / End                — jumps to first / last option
 *   Type-ahead                — jumps to matching option
 */

import React, { useId } from 'react';
import * as SelectPrimitive from '@radix-ui/react-select';
import { ChevronDownIcon, ChevronUpIcon, CheckIcon } from '../../icons-shim';
import { cn } from '../utils';

export type SelectOption = { value: string; label: string; disabled?: boolean };
export type SelectGroup  = { label: string; options: SelectOption[] };

type SelectProps = {
  options: (SelectOption | SelectGroup)[];
  value?: string;
  defaultValue?: string;
  onValueChange?: (value: string) => void;
  placeholder?: string;
  label?: string;
  helperText?: string;
  errorText?: string;
  disabled?: boolean;
  required?: boolean;
  id?: string;
};

function isGroup(item: SelectOption | SelectGroup): item is SelectGroup {
  return 'options' in item;
}

export const Select = React.forwardRef<HTMLButtonElement, SelectProps>(
  ({
    options, value, defaultValue, onValueChange, placeholder = 'Select…',
    label, helperText, errorText, disabled, required, id: externalId,
  }, ref) => {
    const internalId = useId();
    const id      = externalId ?? internalId;
    const helpId  = `${id}-help`;
    const errorId = `${id}-error`;

    const trigger = (
      <SelectPrimitive.Trigger
        ref={ref}
        id={id}
        disabled={disabled}
        aria-required={required}
        aria-invalid={!!errorText || undefined}
        aria-describedby={
          [helperText ? helpId : null, errorText ? errorId : null]
            .filter(Boolean).join(' ') || undefined
        }
        className={cn(
          'flex h-10 w-full items-center justify-between gap-2',
          'rounded-[var(--aurora-border-radius-md)] border px-3 py-2',
          'bg-[var(--aurora-color-background-default)]',
          'text-sm text-[var(--aurora-color-foreground-default)]',
          'border-[var(--aurora-color-border-default)]',
          'focus:outline-none focus:ring-2 focus:ring-[var(--aurora-color-focus-ring)] focus:ring-offset-1',
          'aria-invalid:border-[var(--aurora-color-error-default)]',
          'disabled:cursor-not-allowed disabled:opacity-50',
          'min-h-[44px]',
        )}
      >
        <SelectPrimitive.Value placeholder={
          <span className="text-[var(--aurora-color-foreground-subtle)]">{placeholder}</span>
        } />
        <SelectPrimitive.Icon asChild>
          <ChevronDownIcon size={16} aria-hidden className="shrink-0 text-[var(--aurora-color-foreground-muted)]" />
        </SelectPrimitive.Icon>
      </SelectPrimitive.Trigger>
    );

    const content = (
      <SelectPrimitive.Portal>
        <SelectPrimitive.Content
          position="popper"
          sideOffset={4}
          className={cn(
            'relative z-50 min-w-[8rem] max-h-72 overflow-hidden',
            'rounded-[var(--aurora-border-radius-lg)]',
            'border border-[var(--aurora-color-border-default)]',
            'bg-[var(--aurora-color-background-default)]',
            'shadow-[var(--aurora-box-shadow-lg)]',
            'data-[state=open]:animate-in data-[state=closed]:animate-out',
            'data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0',
            'data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95',
            'data-[side=bottom]:slide-in-from-top-2 data-[side=top]:slide-in-from-bottom-2',
            'w-[var(--radix-select-trigger-width)]',
          )}
        >
          <SelectPrimitive.ScrollUpButton className="flex items-center justify-center h-6 cursor-default">
            <ChevronUpIcon size={14} aria-hidden />
          </SelectPrimitive.ScrollUpButton>

          <SelectPrimitive.Viewport className="p-1">
            {options.map((item, i) =>
              isGroup(item) ? (
                <SelectPrimitive.Group key={i}>
                  <SelectPrimitive.Label className="px-2 py-1.5 text-xs font-semibold text-[var(--aurora-color-foreground-muted)]">
                    {item.label}
                  </SelectPrimitive.Label>
                  {item.options.map(opt => <SelectItem key={opt.value} {...opt} />)}
                </SelectPrimitive.Group>
              ) : (
                <SelectItem key={item.value} {...item} />
              )
            )}
          </SelectPrimitive.Viewport>

          <SelectPrimitive.ScrollDownButton className="flex items-center justify-center h-6 cursor-default">
            <ChevronDownIcon size={14} aria-hidden />
          </SelectPrimitive.ScrollDownButton>
        </SelectPrimitive.Content>
      </SelectPrimitive.Portal>
    );

    return (
      <div className="flex flex-col gap-1.5 w-full">
        {label && (
          <label htmlFor={id} className="text-sm font-medium text-[var(--aurora-color-foreground-default)]">
            {label}
            {required && <span aria-hidden className="ml-0.5 text-[var(--aurora-color-error-default)]">*</span>}
            {required && <span className="sr-only"> (required)</span>}
          </label>
        )}
        <SelectPrimitive.Root value={value} defaultValue={defaultValue} onValueChange={onValueChange}>
          {trigger}
          {content}
        </SelectPrimitive.Root>
        {helperText && !errorText && <p id={helpId} className="text-xs text-[var(--aurora-color-foreground-muted)]">{helperText}</p>}
        {errorText && <p id={errorId} role="alert" className="text-xs text-[var(--aurora-color-error-default)]">{errorText}</p>}
      </div>
    );
  }
);
Select.displayName = 'Select';

function SelectItem({ value, label, disabled }: SelectOption) {
  return (
    <SelectPrimitive.Item
      value={value}
      disabled={disabled}
      className={cn(
        'relative flex w-full cursor-default select-none items-center',
        'rounded-[var(--aurora-border-radius-md)] py-1.5 pl-8 pr-2 text-sm',
        'text-[var(--aurora-color-foreground-default)]',
        'outline-none',
        'focus:bg-[var(--aurora-color-background-subtle)] focus:text-[var(--aurora-color-foreground-default)]',
        'data-[disabled]:pointer-events-none data-[disabled]:opacity-50',
      )}
    >
      <span className="absolute left-2 flex h-3.5 w-3.5 items-center justify-center">
        <SelectPrimitive.ItemIndicator>
          <CheckIcon size={12} aria-hidden />
        </SelectPrimitive.ItemIndicator>
      </span>
      <SelectPrimitive.ItemText>{label}</SelectPrimitive.ItemText>
    </SelectPrimitive.Item>
  );
}
