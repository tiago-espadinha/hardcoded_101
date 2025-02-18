import type { Meta, StoryObj } from '@storybook/react';
import { Input, Textarea, Checkbox, Switch, Stack, Button } from '@aurora-ds/components';
import { SearchIcon, EyeIcon, EyeOffIcon } from '@aurora-ds/icons';
import React, { useState } from 'react';

// ── Input ─────────────────────────────────────────────────────────────────────

const inputMeta: Meta<typeof Input> = {
  title: 'Composite/Input',
  component: Input,
  tags: ['autodocs'],
  args: { label: 'Email address', placeholder: 'you@example.com' },
  /**
   * ## Keyboard Interaction
   * | Key     | Action                       |
   * |---------|------------------------------|
   * | `Tab`   | Move focus to / from input   |
   * | `Esc`   | Clear focus                  |
   *
   * ## Do
   * - Always pair with a visible label (use `label` prop, not just `placeholder`)
   * - Use `errorText` to surface validation failures, not just colour changes
   *
   * ## Don't
   * - Don't use placeholder text as a substitute for a label
   * - Don't rely on colour alone to convey error state
   */
};
export default inputMeta;

export const Default: StoryObj<typeof Input> = {};

export const WithHelperText: StoryObj<typeof Input> = {
  args: {
    label: 'Username',
    placeholder: 'e.g. aurora_user',
    helperText: 'Must be 3–24 characters, letters and numbers only.',
  },
};

export const WithError: StoryObj<typeof Input> = {
  args: {
    label: 'Email address',
    placeholder: 'you@example.com',
    defaultValue: 'not-an-email',
    errorText: 'Please enter a valid email address.',
  },
};

export const WithIcons: StoryObj<typeof Input> = {
  render: () => (
    <Stack gap={4} style={{ maxWidth: '360px' }}>
      <Input label="Search" placeholder="Search…" iconLeft={<SearchIcon size={16} aria-hidden />} />
    </Stack>
  ),
};

export const PasswordToggle: StoryObj<typeof Input> = {
  render: function PasswordInput() {
    const [show, setShow] = useState(false);
    return (
      <Stack gap={4} style={{ maxWidth: '360px' }}>
        <Input
          label="Password"
          type={show ? 'text' : 'password'}
          placeholder="••••••••"
          iconRight={
            <button
              type="button"
              aria-label={show ? 'Hide password' : 'Show password'}
              onClick={() => setShow(s => !s)}
              style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'inherit', display: 'flex' }}
            >
              {show ? <EyeOffIcon size={16} aria-hidden /> : <EyeIcon size={16} aria-hidden />}
            </button>
          }
        />
      </Stack>
    );
  },
};

export const Required: StoryObj<typeof Input> = {
  args: { label: 'Full name', required: true, placeholder: 'Jane Doe' },
};

// ── Textarea ──────────────────────────────────────────────────────────────────

export const TextareaDefault: StoryObj = {
  render: () => (
    <Textarea
      label="Message"
      placeholder="Write your message here…"
      helperText="Maximum 500 characters."
      style={{ maxWidth: '480px' }}
    />
  ),
};

export const TextareaError: StoryObj = {
  render: () => (
    <Textarea
      label="Bio"
      defaultValue="This is way too long and exceeds the character limit..."
      errorText="Bio must be 160 characters or fewer."
      style={{ maxWidth: '480px' }}
    />
  ),
};

// ── Checkbox ──────────────────────────────────────────────────────────────────

export const CheckboxDefault: StoryObj = {
  render: () => (
    <Stack gap={3}>
      <Checkbox label="I agree to the terms and conditions" />
      <Checkbox label="Subscribe to the newsletter" helperText="We send at most one email per week." />
      <Checkbox label="This option is disabled" disabled />
      <Checkbox label="Pre-selected option" defaultChecked />
    </Stack>
  ),
};

// ── Switch ────────────────────────────────────────────────────────────────────

export const SwitchDefault: StoryObj = {
  render: () => (
    <Stack gap={4}>
      <Switch label="Email notifications" helperText="Receive updates about your account." />
      <Switch label="Dark mode" defaultChecked />
      <Switch label="Disabled setting" disabled />
    </Stack>
  ),
};

// ── Full form example ─────────────────────────────────────────────────────────

export const FormExample: StoryObj = {
  render: function FormExample() {
    const [errors, setErrors] = useState<Record<string, string>>({});

    function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
      e.preventDefault();
      const data = new FormData(e.currentTarget);
      const newErrors: Record<string, string> = {};
      if (!data.get('name')) newErrors.name = 'Name is required.';
      if (!data.get('email')) newErrors.email = 'Email is required.';
      setErrors(newErrors);
    }

    return (
      <form onSubmit={handleSubmit} noValidate style={{ maxWidth: '400px' }}>
        <Stack gap={5}>
          <Input name="name" label="Full name" placeholder="Jane Doe" required errorText={errors.name} />
          <Input name="email" label="Email" type="email" placeholder="jane@example.com" required errorText={errors.email} />
          <Textarea name="bio" label="Bio" placeholder="Tell us about yourself…" helperText="Optional." />
          <Checkbox label="I agree to the terms of service" required />
          <Button type="submit" intent="brand">Create account</Button>
        </Stack>
      </form>
    );
  },
};
