/**
 * @aurora-ds/components — Level 1 Typography Primitives
 * Text, Heading, Code, Link
 */

import React from 'react';
import { cn } from '../utils';

// ── Text ──────────────────────────────────────────────────────────────────────

type TextProps = React.HTMLAttributes<HTMLParagraphElement> & {
  as?: 'p' | 'span' | 'label' | 'legend' | 'figcaption';
  size?: 'xs' | 'sm' | 'base' | 'lg' | 'xl';
  weight?: 'light' | 'normal' | 'medium' | 'semibold' | 'bold';
  muted?: boolean;
  truncate?: boolean;
};

const TEXT_SIZE: Record<string, string> = {
  xs: 'text-xs', sm: 'text-sm', base: 'text-base', lg: 'text-lg', xl: 'text-xl',
};

const TEXT_WEIGHT: Record<string, string> = {
  light: 'font-light', normal: 'font-normal', medium: 'font-medium',
  semibold: 'font-semibold', bold: 'font-bold',
};

/**
 * Body text primitive. Handles size, weight, muted style, and truncation.
 *
 * Keyboard: not interactive — no keyboard requirements.
 *
 * @example
 * <Text size="sm" muted>Supporting description text</Text>
 */
export const Text = React.forwardRef<HTMLParagraphElement, TextProps>(
   (
     { 
       size = 'base', 
       weight = 'normal', 
       muted = false, 
       truncate = false,
       className, 
       children, 
       ...rest 
     },
     ref,
   ) => (
     <p
       ref={ref}
       className={cn(
         'leading-normal',
         TEXT_SIZE[size],
         TEXT_WEIGHT[weight],
         muted
           ? 'text-[var(--aurora-color-foreground-muted)]'
           : 'text-[var(--aurora-color-foreground-default)]',
         truncate && 'truncate',
         className,
       )}
       {...rest}
     >
       {children}
     </p>
   ),
 );
Text.displayName = 'Text';

// ── Heading ───────────────────────────────────────────────────────────────────

type HeadingLevel = 1 | 2 | 3 | 4 | 5 | 6;

type HeadingProps = React.HTMLAttributes<HTMLHeadingElement> & {
  level?: HeadingLevel;
  size?: 'sm' | 'md' | 'lg' | 'xl' | '2xl' | '3xl' | '4xl';
};

const HEADING_SIZE: Record<string, string> = {
  sm: 'text-lg', md: 'text-xl', lg: 'text-2xl',
  xl: 'text-3xl', '2xl': 'text-4xl', '3xl': 'text-5xl', '4xl': 'text-6xl',
};

const LEVEL_TO_DEFAULT_SIZE: Record<HeadingLevel, string> = {
  1: '3xl', 2: '2xl', 3: 'xl', 4: 'lg', 5: 'md', 6: 'sm',
};

/**
 * Semantic heading element. Level controls the HTML tag; size controls visual size
 * independently — allowing semantic and visual hierarchies to differ.
 *
 * @example
 * <Heading level={2} size="xl">Section title</Heading>
 */
export const Heading = React.forwardRef<HTMLHeadingElement, HeadingProps>(
  ({ level = 2, size, className, children, ...rest }, ref) => {
    const Tag = `h${level}` as 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6';
    const resolvedSize = size ?? LEVEL_TO_DEFAULT_SIZE[level];
    return (
      <Tag
        ref={ref}
        className={cn(
          'font-bold leading-tight tracking-tight text-[var(--aurora-color-foreground-default)]',
          HEADING_SIZE[resolvedSize],
          className,
        )}
        {...rest}
      >
        {children}
      </Tag>
    );
  },
);
Heading.displayName = 'Heading';

// ── Code ──────────────────────────────────────────────────────────────────────

type CodeProps = React.HTMLAttributes<HTMLElement> & {
  block?: boolean;
};

/**
 * Inline or block code element.
 *
 * @example
 * <Code>const x = 1;</Code>
 * <Code block>{'function hello() {\n  return "world";\n}'}</Code>
 */
export const Code = React.forwardRef<HTMLElement, CodeProps>(
  ({ block = false, className, children, ...rest }, ref) => {
    if (block) {
      return (
        <pre className={cn('overflow-x-auto rounded-lg bg-[var(--aurora-color-background-muted)] p-4', className)}>
          <code
            ref={ref as React.Ref<HTMLElement>}
            className={cn('font-mono text-sm text-[var(--aurora-color-foreground-default)]', className)}
            {...rest}
          >
            {children}
          </code>
        </pre>
      );
    }

    return (
      <code
        ref={ref as React.Ref<HTMLElement>}
        className={cn(
          'rounded px-1.5 py-0.5 font-mono text-sm',
          'bg-[var(--aurora-color-background-muted)]',
          'text-[var(--aurora-color-foreground-default)]',
          className,
        )}
        {...rest}
      >
        {children}
      </code>
    );
  },
);
Code.displayName = 'Code';

// ── Link ──────────────────────────────────────────────────────────────────────

type LinkProps = React.AnchorHTMLAttributes<HTMLAnchorElement> & {
  external?: boolean;
};

/**
 * Styled anchor element. Automatically adds `rel="noopener noreferrer"` and
 * a screen-reader-visible "(opens in new tab)" notice for external links.
 *
 * Keyboard: natively focusable; focus ring applied.
 *
 * @example
 * <Link href="https://example.com" external>Visit site</Link>
 */
export const Link = React.forwardRef<HTMLAnchorElement, LinkProps>(
  ({ external = false, className, children, ...rest }, ref) => (
    <a
      ref={ref}
      target={external ? '_blank' : undefined}
      rel={external ? 'noopener noreferrer' : undefined}
      className={cn(
        'text-[var(--aurora-color-brand-default)] underline underline-offset-2',
        'hover:text-[var(--aurora-color-brand-hover)] transition-colors',
        'focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2',
        'focus-visible:outline-[var(--aurora-color-focus-ring)] rounded-sm',
        className,
      )}
      {...rest}
    >
      {children}
      {external && (
        <span className="sr-only"> (opens in new tab)</span>
      )}
    </a>
  ),
);
Link.displayName = 'Link';
