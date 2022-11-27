import type { Meta, StoryObj } from '@storybook/react';
import { Checkbox } from './Checkbox';

const meta: Meta<typeof Checkbox> = {
  title: 'Components/Checkbox',
  component: Checkbox,
  tags: ['autodocs'],
};

export default meta;
type Story = StoryObj<typeof Checkbox>;

export const Default: Story = {
  args: {
    label: 'I agree to the terms',
  },
};

export const Checked: Story = {
  args: {
    label: 'I agree to the terms',
    checked: true,
  },
};

export const Indeterminate: Story = {
  args: {
    label: 'I agree to some terms',
    indeterminate: true,
  },
};

export const Error: Story = {
  args: {
    label: 'I agree to the terms',
    error: 'You must agree to the terms',
  },
};

export const Disabled: Story = {
  args: {
    label: 'I agree to the terms',
    disabled: true,
  },
};
