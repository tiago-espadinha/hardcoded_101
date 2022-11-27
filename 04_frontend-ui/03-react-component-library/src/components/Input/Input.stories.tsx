import type { Meta, StoryObj } from "@storybook/react";
import { Input } from "./Input";

const meta: Meta<typeof Input> = {
  title: "Components/Input",
  component: Input,
  tags: ["autodocs"],
  argTypes: {
    onChange: { action: "changed" },
    disabled: { control: "boolean" },
    required: { control: "boolean" },
  },
};

export default meta;
type Story = StoryObj<typeof Input>;

export const Default: Story = {
  args: {
    label: "Label",
    placeholder: "Placeholder text",
  },
};

export const WithHint: Story = {
  args: {
    label: "Label",
    placeholder: "Placeholder text",
    hint: "This is a hint message.",
  },
};

export const WithError: Story = {
  args: {
    label: "Label",
    placeholder: "Placeholder text",
    error: "This is an error message.",
  },
};

export const Disabled: Story = {
  args: {
    label: "Label",
    placeholder: "Placeholder text",
    disabled: true,
    value: "Disabled content",
  },
};

export const WithAdornments: Story = {
  args: {
    label: "Price",
    placeholder: "0.00",
    leftAdornment: <span>$</span>,
    rightAdornment: <span>USD</span>,
  },
};
