import type { Meta, StoryObj } from "@storybook/react";
import { Select } from "./Select";

const meta: Meta<typeof Select> = {
  title: "Components/Select",
  component: Select,
  tags: ["autodocs"],
};

export default meta;
type Story = StoryObj<typeof Select>;

const options = [
  { value: "react", label: "React" },
  { value: "vue", label: "Vue" },
  { value: "angular", label: "Angular" },
  { value: "svelte", label: "Svelte" },
];

export const Default: Story = {
  args: {
    label: "Framework",
    options,
    placeholder: "Select a framework",
  },
};

export const WithValue: Story = {
  args: {
    label: "Framework",
    options,
    value: "react",
  },
};

export const Error: Story = {
  args: {
    label: "Framework",
    options,
    error: "Please select a framework",
  },
};

export const Disabled: Story = {
  args: {
    label: "Framework",
    options,
    disabled: true,
  },
};
