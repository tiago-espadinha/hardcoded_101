/**
 * @aurora-ds/components — Level 1 Layout Primitives
 * Box, Stack, Inline, Grid, Divider
 *
 * These are zero-dependency layout components that accept standard HTML
 * attributes plus semantic spacing/layout props.
 */

import React from 'react';
import { cn, type PolymorphicProps } from '../utils';

// ── Box ──────────────────────────────────────────────────────────────────────

type BoxOwnProps = {
  /** Padding shorthand using spacing scale (0–32) */
  p?: number | string;
  px?: number | string;
  py?: number | string;
};

type BoxProps<E extends React.ElementType = 'div'> = PolymorphicProps<E, BoxOwnProps>;

/**
 * The base layout primitive. Renders a `div` by default.
 * Accepts an `as` prop for semantic HTML elements.
 *
 * @example
 * <Box as="section" className="my-layout">…</Box>
 */
export function Box<E extends React.ElementType = 'div'>({
  as,
  className,
  children,
  ...rest
}: BoxProps<E>) {
  const Component = as ?? 'div';
  return (
    <Component className={cn(className)} {...rest}>
      {children}
    </Component>
  );
}

// ── Stack ─────────────────────────────────────────────────────────────────────

type StackProps = React.HTMLAttributes<HTMLDivElement> & {
  /** Gap between children using Tailwind gap scale */
  gap?: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 8 | 10 | 12 | 16;
  /** Horizontal alignment */
  align?: 'start' | 'center' | 'end' | 'stretch';
  /** Main-axis justification */
  justify?: 'start' | 'center' | 'end' | 'between' | 'around';
};

const GAP_MAP: Record<number, string> = {
  0: 'gap-0', 1: 'gap-1', 2: 'gap-2', 3: 'gap-3',
  4: 'gap-4', 5: 'gap-5', 6: 'gap-6', 8: 'gap-8',
  10: 'gap-10', 12: 'gap-12', 16: 'gap-16',
};

const ALIGN_MAP: Record<string, string> = {
  start: 'items-start', center: 'items-center',
  end: 'items-end', stretch: 'items-stretch',
};

const JUSTIFY_MAP: Record<string, string> = {
  start: 'justify-start', center: 'justify-center',
  end: 'justify-end', between: 'justify-between', around: 'justify-around',
};

/**
 * Vertical flex stack. Composes children with consistent spacing.
 *
 * @example
 * <Stack gap={4} align="center">
 *   <Text>One</Text>
 *   <Text>Two</Text>
 * </Stack>
 */
export const Stack = React.forwardRef<HTMLDivElement, StackProps>(
  ({ gap = 4, align = 'stretch', justify = 'start', className, children, ...rest }, ref) => (
    <div
      ref={ref}
      className={cn(
        'flex flex-col',
        GAP_MAP[gap],
        ALIGN_MAP[align],
        JUSTIFY_MAP[justify],
        className,
      )}
      {...rest}
    >
      {children}
    </div>
  ),
);
Stack.displayName = 'Stack';

// ── Inline ────────────────────────────────────────────────────────────────────

type InlineProps = React.HTMLAttributes<HTMLDivElement> & {
  gap?: 0 | 1 | 2 | 3 | 4 | 5 | 6 | 8;
  align?: 'start' | 'center' | 'end' | 'baseline' | 'stretch';
  wrap?: boolean;
};

/**
 * Horizontal flex row. Children are laid out inline with optional wrapping.
 *
 * @example
 * <Inline gap={2} wrap>
 *   <Badge>React</Badge>
 *   <Badge>TypeScript</Badge>
 * </Inline>
 */
export const Inline = React.forwardRef<HTMLDivElement, InlineProps>(
  ({ gap = 2, align = 'center', wrap = false, className, children, ...rest }, ref) => (
    <div
      ref={ref}
      className={cn(
        'flex flex-row',
        GAP_MAP[gap],
        ALIGN_MAP[align] ?? 'items-center',
        wrap && 'flex-wrap',
        className,
      )}
      {...rest}
    >
      {children}
    </div>
  ),
);
Inline.displayName = 'Inline';

// ── Grid ──────────────────────────────────────────────────────────────────────

type GridProps = React.HTMLAttributes<HTMLDivElement> & {
  columns?: 1 | 2 | 3 | 4 | 6 | 12;
  gap?: 0 | 1 | 2 | 3 | 4 | 6 | 8;
};

const COLS_MAP: Record<number, string> = {
  1: 'grid-cols-1', 2: 'grid-cols-2', 3: 'grid-cols-3',
  4: 'grid-cols-4', 6: 'grid-cols-6', 12: 'grid-cols-12',
};

/**
 * CSS grid wrapper with column and gap control.
 *
 * @example
 * <Grid columns={3} gap={6}>
 *   <Card />
 *   <Card />
 *   <Card />
 * </Grid>
 */
export const Grid = React.forwardRef<HTMLDivElement, GridProps>(
  ({ columns = 1, gap = 4, className, children, ...rest }, ref) => (
    <div
      ref={ref}
      className={cn('grid', COLS_MAP[columns], GAP_MAP[gap], className)}
      {...rest}
    >
      {children}
    </div>
  ),
);
Grid.displayName = 'Grid';

// ── Divider ───────────────────────────────────────────────────────────────────

type DividerProps = React.HTMLAttributes<HTMLHRElement> & {
  orientation?: 'horizontal' | 'vertical';
};

/**
 * Semantic separator element.
 *
 * @example
 * <Divider />
 * <Divider orientation="vertical" className="h-6" />
 */
export const Divider = React.forwardRef<HTMLHRElement, DividerProps>(
  ({ orientation = 'horizontal', className, ...rest }, ref) => (
    <hr
      ref={ref}
      role="separator"
      aria-orientation={orientation}
      className={cn(
        'border-0 bg-[var(--aurora-color-border-default)]',
        orientation === 'horizontal' ? 'h-px w-full' : 'h-full w-px',
        className,
      )}
      {...rest}
    />
  ),
);
Divider.displayName = 'Divider';
