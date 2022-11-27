import type { Meta, StoryObj } from "@storybook/react";
import { Textarea } from "./Textarea";

const meta: Meta<typeof Textarea> = {
  title: "Components/Textarea",
  component: Textarea,
  tags: ["autodocs"],
  argTypes: {
    onChange: { action: "changed" },
    disabled: { control: "boolean" },
    required: { control: "boolean" },
    showCharCount: { control: "boolean" },
  },
};

export default meta;
type Story = StoryObj<typeof Textarea>;

export const Default: Story = {
  args: {
    label: "Description",
    placeholder: "Enter a description...",
  },
};

export const WithCharCount: Story = {
  args: {
    label: "Description",
    placeholder: "Enter a description...",
    maxLength: 100,
    showCharCount: true,
    value: "Some initial text",
  },
};

export const WithError: Story = {
  args: {
    label: "Description",
    placeholder: "Enter a description...",
    error: "Description is too short.",
  },
};

export const Disabled: Story = {
  args: {
    label: "Description",
    placeholder: "Enter a description...",
    disabled: true,
  },
};
