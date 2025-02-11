/**
 * @aurora-ds/components — Main export barrel
 */

// Level 1 — Primitives
export { Box, Stack, Inline, Grid, Divider } from './primitives/layout';
export { Text, Heading, Code, Link } from './primitives/typography';

// Level 2 — Simple
export { Button } from './simple/Button';
export type { ButtonProps } from './simple/Button';
export { Badge, Avatar, Spinner, ProgressBar, Skeleton } from './simple/simple';

// Level 3 — Composite (forms + select)
export { Input, Textarea, Checkbox, Switch, FieldWrapper } from './composite/forms';

// Level 4 — Complex (+ utilities)
export { Modal, Tabs, Toast, ToastProvider, ToastViewport, Tooltip, prefersReducedMotion } from './complex/complex';

// Utilities
export { cn } from './utils';
export type { Size, Variant, Intent } from './utils';
export { Select } from './composite/Select';
export type { SelectOption, SelectGroup } from './composite/Select';

// Simple additions
export { Tag } from './simple/Tag';

// Complex additions
export { Accordion } from './complex/Accordion';
export type { AccordionItem } from './complex/Accordion';
