import { type ClassValue, clsx } from 'clsx';

/**
 * Merges class names using clsx.
 * Use this utility in every component to compose Tailwind classes.
 */
export function cn(...inputs: ClassValue[]): string {
  return clsx(inputs);
}

/** Shared size scale used across components */
export type Size = 'xs' | 'sm' | 'md' | 'lg' | 'xl';

/** Shared variant scale */
export type Variant = 'solid' | 'outline' | 'ghost' | 'link';

/** Semantic colour intents */
export type Intent = 'default' | 'brand' | 'success' | 'warning' | 'error';

/** Polymorphic `as` prop support */
export type AsProp<E extends React.ElementType> = { as?: E };

export type PolymorphicProps<E extends React.ElementType, P = object> = AsProp<E> &
  Omit<React.ComponentPropsWithRef<E>, keyof (AsProp<E> & P)> &
  P;
