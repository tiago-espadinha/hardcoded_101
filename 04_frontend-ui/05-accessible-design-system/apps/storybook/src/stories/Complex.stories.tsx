import type { Meta, StoryObj } from '@storybook/react';
import {
  Modal, Tabs, Toast, ToastProvider, ToastViewport, Tooltip,
  Button, Stack, Text, Inline, Badge,
} from '@aurora-ds/components';
import { CheckCircleIcon, AlertCircleIcon, InfoIcon } from '@aurora-ds/icons';
import React, { useState } from 'react';

const meta = {
  title: 'Complex',
  tags: ['autodocs'],
} satisfies Meta;

export default meta;

// ── Modal ─────────────────────────────────────────────────────────────────────

/**
 * Modal dialogs interrupt the user for important tasks.
 *
 * ## Keyboard Interaction
 * | Key             | Action                              |
 * |-----------------|-------------------------------------|
 * | `Tab`           | Move focus within the dialog        |
 * | `Shift + Tab`   | Move focus backwards                |
 * | `Escape`        | Close the dialog                    |
 *
 * ## Accessibility
 * - Focus is trapped inside the dialog while open
 * - Focus returns to the trigger element on close
 * - Screen readers announce the dialog title via `role="dialog"` + `aria-labelledby`
 */
export const ModalDefault: StoryObj = {
  render: function ModalStory() {
    const [open, setOpen] = useState(false);
    return (
      <>
        <Button intent="brand" onClick={() => setOpen(true)}>Open modal</Button>
        <Modal open={open} onOpenChange={setOpen} title="Confirm deletion" description="This action cannot be undone. The item will be permanently deleted.">
          <Modal.Footer>
            <Button variant="ghost" onClick={() => setOpen(false)}>Cancel</Button>
            <Button intent="error" onClick={() => setOpen(false)}>Delete permanently</Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  },
};

export const ModalSizes: StoryObj = {
  render: function ModalSizes() {
    const [openSize, setOpenSize] = useState<string | null>(null);
    return (
      <Inline gap={2}>
        {(['sm','md','lg','xl'] as const).map(size => (
          <Button key={size} variant="outline" onClick={() => setOpenSize(size)}>{size.toUpperCase()}</Button>
        ))}
        {(['sm','md','lg','xl'] as const).map(size => (
          <Modal key={size} open={openSize === size} onOpenChange={() => setOpenSize(null)} title={`${size.toUpperCase()} Modal`} size={size}>
            <Text>This is a {size} modal. Resize the window to see how it adapts.</Text>
            <Modal.Footer>
              <Button onClick={() => setOpenSize(null)}>Close</Button>
            </Modal.Footer>
          </Modal>
        ))}
      </Inline>
    );
  },
};

// ── Tabs ──────────────────────────────────────────────────────────────────────

export const TabsDefault: StoryObj = {
  render: () => (
    <Tabs
      defaultValue="overview"
      items={[
        {
          value: 'overview',
          label: 'Overview',
          content: (
            <Stack gap={3}>
              <Text weight="semibold">Project Overview</Text>
              <Text muted>Aurora DS is a production-grade design system with full WCAG 2.1 AA compliance.</Text>
              <Inline gap={2}>
                <Badge intent="success" variant="subtle">Active</Badge>
                <Badge intent="brand" variant="subtle">v0.1.0</Badge>
              </Inline>
            </Stack>
          ),
        },
        {
          value: 'tokens',
          label: 'Tokens',
          content: (
            <Stack gap={2}>
              <Text weight="semibold">Design Tokens</Text>
              <Text muted>Primitive + semantic colour tokens, spacing scale, motion primitives.</Text>
            </Stack>
          ),
        },
        {
          value: 'components',
          label: 'Components',
          content: (
            <Stack gap={2}>
              <Text weight="semibold">30+ Components</Text>
              <Text muted>Four levels: Primitives → Simple → Composite → Complex.</Text>
            </Stack>
          ),
        },
        {
          value: 'disabled',
          label: 'Disabled',
          disabled: true,
          content: <Text>This tab is disabled.</Text>,
        },
      ]}
    />
  ),
};

// ── Toast ─────────────────────────────────────────────────────────────────────

export const ToastDefault: StoryObj = {
  render: function ToastStory() {
    const [toasts, setToasts] = useState<Array<{ id: number; title: string; description?: string; intent: 'default' | 'success' | 'warning' | 'error' }>>([]);
    let id = 0;

    function addToast(intent: 'default' | 'success' | 'warning' | 'error') {
      const configs = {
        default:  { title: 'Update available',    description: 'A new version of the app is ready.' },
        success:  { title: 'Changes saved',        description: 'Your profile has been updated.' },
        warning:  { title: 'Session expiring',     description: 'You will be logged out in 5 minutes.' },
        error:    { title: 'Upload failed',         description: 'The file exceeds the 10MB limit.' },
      };
      setToasts(prev => [...prev, { id: id++, intent, ...configs[intent] }]);
    }

    return (
      <ToastProvider>
        <Inline gap={2} wrap>
          <Button variant="outline" onClick={() => addToast('default')} iconLeft={<InfoIcon size={14} aria-hidden />}>Info</Button>
          <Button variant="outline" intent="success" onClick={() => addToast('success')} iconLeft={<CheckCircleIcon size={14} aria-hidden />}>Success</Button>
          <Button variant="outline" intent="warning" onClick={() => addToast('warning')} iconLeft={<AlertCircleIcon size={14} aria-hidden />}>Warning</Button>
          <Button variant="outline" intent="error" onClick={() => addToast('error')} iconLeft={<AlertCircleIcon size={14} aria-hidden />}>Error</Button>
        </Inline>
        {toasts.map(t => (
          <Toast key={t.id} intent={t.intent} title={t.title} description={t.description} defaultOpen onOpenChange={(open) => { if (!open) setToasts(prev => prev.filter(x => x.id !== t.id)); }} />
        ))}
        <ToastViewport />
      </ToastProvider>
    );
  },
};

// ── Tooltip ───────────────────────────────────────────────────────────────────

export const TooltipDefault: StoryObj = {
  render: () => (
    <Inline gap={6} style={{ paddingTop: '48px' }}>
      <Tooltip content="Appears on top" side="top">
        <Button variant="outline">Top</Button>
      </Tooltip>
      <Tooltip content="Appears on right" side="right">
        <Button variant="outline">Right</Button>
      </Tooltip>
      <Tooltip content="Appears on bottom" side="bottom">
        <Button variant="outline">Bottom</Button>
      </Tooltip>
      <Tooltip content="Appears on left" side="left">
        <Button variant="outline">Left</Button>
      </Tooltip>
    </Inline>
  ),
};

export const TooltipOnFocus: StoryObj = {
  name: 'A11y — Tooltip on keyboard focus',
  render: () => (
    <div style={{ paddingTop: '48px' }}>
      <Text muted style={{ marginBottom: '16px' }}>Tab to the button to trigger the tooltip via keyboard focus.</Text>
      <Tooltip content="This tooltip is accessible on keyboard focus — not just hover">
        <Button variant="outline">Focus me</Button>
      </Tooltip>
    </div>
  ),
};
