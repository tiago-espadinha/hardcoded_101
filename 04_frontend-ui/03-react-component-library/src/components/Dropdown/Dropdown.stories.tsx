import type { Meta, StoryObj } from "@storybook/react";
import React from "react";
import { Dropdown } from "./Dropdown";
import { Button } from "../Button";

const meta: Meta<typeof Dropdown> = {
  title: "Components/Dropdown",
  component: Dropdown,
  tags: ["autodocs"],
};

export default meta;
type Story = StoryObj<typeof Dropdown>;

export const Default: Story = {
  args: {
    trigger: <Button>Actions</Button>,
    items: [
      { id: "1", label: "Edit", onClick: () => alert("Edit") },
      { id: "2", label: "Duplicate", onClick: () => alert("Duplicate") },
      { type: "divider" },
      {
        id: "3",
        label: "Archive",
        onClick: () => alert("Archive"),
        disabled: true,
      },
      {
        id: "4",
        label: "Delete",
        onClick: () => alert("Delete"),
        variant: "danger",
      },
    ],
  },
};
