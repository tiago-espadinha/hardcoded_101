import type { Meta, StoryObj } from '@storybook/react';
<<<<<<< HEAD
import React from 'react';
import { Badge, Avatar, Spinner, ProgressBar, Skeleton, Stack, Inline } from '@aurora-ds/components';

const meta = {
  title: 'Simple',
  tags: ['autodocs'],
} satisfies Meta;

export default meta;

// ── Badge ─────────────────────────────────────────────────────────────────────

export const BadgeStories: StoryObj = {
  render: () => <Badge>Badge</Badge>,
=======
import { Badge, Avatar, Spinner, ProgressBar, Skeleton, Stack, Inline } from '@aurora-ds/components';

// ── Badge ─────────────────────────────────────────────────────────────────────

export const BadgeStories: Meta<typeof Badge> = {
  title: 'Simple/Badge',
  component: Badge,
  tags: ['autodocs'],
  args: { children: 'Badge' },
>>>>>>> 1ef8b9a (docs(storybook): add Button stories — playground, variants, intents, sizes, icons, states, a11y)
};

export const BadgeVariants: StoryObj<typeof Badge> = {
  render: () => (
    <Stack gap={4}>
      <Inline gap={2}>
        {(['default','brand','success','warning','error'] as const).map(intent => (
          <Badge key={intent} variant="solid" intent={intent}>{intent}</Badge>
        ))}
      </Inline>
      <Inline gap={2}>
        {(['default','brand','success','warning','error'] as const).map(intent => (
          <Badge key={intent} variant="subtle" intent={intent}>{intent}</Badge>
        ))}
      </Inline>
      <Inline gap={2}>
        {(['default','brand','error'] as const).map(intent => (
          <Badge key={intent} variant="outline" intent={intent}>{intent}</Badge>
        ))}
      </Inline>
    </Stack>
  ),
};

// ── Avatar ────────────────────────────────────────────────────────────────────

<<<<<<< HEAD
export const AvatarStories: StoryObj = {
  render: () => <Avatar alt="Jane Doe" fallback="JD" />,
=======
export const AvatarStories: Meta<typeof Avatar> = {
  title: 'Simple/Avatar',
  component: Avatar,
  tags: ['autodocs'],
  args: { alt: 'Jane Doe' },
>>>>>>> 1ef8b9a (docs(storybook): add Button stories — playground, variants, intents, sizes, icons, states, a11y)
};

export const AvatarSizes: StoryObj<typeof Avatar> = {
  render: () => (
    <Inline gap={4} align="end">
      {(['xs','sm','md','lg','xl'] as const).map(size => (
        <Avatar key={size} size={size} alt={`${size} avatar`} fallback="JD" />
      ))}
    </Inline>
  ),
};

export const AvatarWithImage: StoryObj<typeof Avatar> = {
  render: () => (
    <Inline gap={4}>
      <Avatar alt="Alice Smith" src="https://i.pravatar.cc/150?img=1" size="lg" />
      <Avatar alt="Bob Jones" src="https://i.pravatar.cc/150?img=2" size="lg" />
      <Avatar alt="Carol White" fallback="CW" size="lg" />
    </Inline>
  ),
};

// ── Spinner ───────────────────────────────────────────────────────────────────

<<<<<<< HEAD
export const SpinnerStories: StoryObj = {
  render: () => <Spinner label="Loading" />,
=======
export const SpinnerStories: Meta<typeof Spinner> = {
  title: 'Simple/Spinner',
  component: Spinner,
  tags: ['autodocs'],
>>>>>>> 1ef8b9a (docs(storybook): add Button stories — playground, variants, intents, sizes, icons, states, a11y)
};

export const SpinnerSizes: StoryObj<typeof Spinner> = {
  render: () => (
    <Inline gap={6} align="center">
      {(['xs','sm','md','lg'] as const).map(size => (
        <Spinner key={size} size={size} label={`Loading (${size})`} />
      ))}
    </Inline>
  ),
};

// ── ProgressBar ───────────────────────────────────────────────────────────────

<<<<<<< HEAD
export const ProgressBarStories: StoryObj = {
  render: () => <ProgressBar value={60} label="Progress" />,
=======
export const ProgressBarStories: Meta<typeof ProgressBar> = {
  title: 'Simple/ProgressBar',
  component: ProgressBar,
  tags: ['autodocs'],
  args: { value: 60, label: 'Progress' },
  argTypes: { value: { control: { type: 'range', min: 0, max: 100, step: 1 } } },
>>>>>>> 1ef8b9a (docs(storybook): add Button stories — playground, variants, intents, sizes, icons, states, a11y)
};

export const ProgressBarIntents: StoryObj<typeof ProgressBar> = {
  render: () => (
    <Stack gap={3} style={{ maxWidth: '480px' }}>
      {(['brand','success','warning','error','default'] as const).map(intent => (
        <ProgressBar key={intent} value={65} intent={intent} label={`${intent} progress`} />
      ))}
    </Stack>
  ),
};

// ── Skeleton ──────────────────────────────────────────────────────────────────

<<<<<<< HEAD
export const SkeletonStories: StoryObj = {
  render: () => <Skeleton style={{ height: '20px', width: '240px' }} />,
=======
export const SkeletonStories: Meta<typeof Skeleton> = {
  title: 'Simple/Skeleton',
  component: Skeleton,
  tags: ['autodocs'],
>>>>>>> 1ef8b9a (docs(storybook): add Button stories — playground, variants, intents, sizes, icons, states, a11y)
};

export const SkeletonCard: StoryObj<typeof Skeleton> = {
  render: () => (
    <Stack gap={3} style={{ maxWidth: '360px', padding: '24px', border: '1px solid var(--aurora-color-border-default)', borderRadius: '12px' }}>
      <Skeleton style={{ height: '160px', borderRadius: '8px' }} />
      <Skeleton style={{ height: '20px', width: '60%' }} />
      <Skeleton style={{ height: '14px' }} />
      <Skeleton style={{ height: '14px', width: '80%' }} />
      <Inline gap={2}>
        <Skeleton style={{ height: '32px', width: '80px', borderRadius: '9999px' }} />
        <Skeleton style={{ height: '32px', width: '80px', borderRadius: '9999px' }} />
      </Inline>
    </Stack>
  ),
};
