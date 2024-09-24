import type { Meta, StoryObj } from '@storybook/react';
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

export const AvatarStories: StoryObj = {
  render: () => <Avatar alt="Jane Doe" fallback="JD" />,
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

export const SpinnerStories: StoryObj = {
  render: () => <Spinner label="Loading" />,
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

export const ProgressBarStories: StoryObj = {
  render: () => <ProgressBar value={60} label="Progress" />,
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

export const SkeletonStories: StoryObj = {
  render: () => <Skeleton style={{ height: '20px', width: '240px' }} />,
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
