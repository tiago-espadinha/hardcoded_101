import type { Meta, StoryObj } from "@storybook/react";
import React, { useState } from "react";
import { Modal } from "./Modal";
import { Button } from "../Button";

const meta: Meta<typeof Modal> = {
  title: "Components/Modal",
  component: Modal,
  tags: ["autodocs"],
};

export default meta;
type Story = StoryObj<typeof Modal>;

export const Default: Story = {
  render: (args) => {
    const [isOpen, setIsOpen] = useState(false);
    return (
      <>
        <Button onClick={() => setIsOpen(true)}>Open Modal</Button>
        <Modal {...args} isOpen={isOpen} onClose={() => setIsOpen(false)}>
          <p>This is the modal content.</p>
        </Modal>
      </>
    );
  },
  args: {
    title: "Modal Title",
  },
};

export const Sizes: Story = {
  render: () => {
    const [size, setSize] = useState<"sm" | "md" | "lg" | "xl" | "full">("md");
    const [isOpen, setIsOpen] = useState(false);
    return (
      <div style={{ display: "flex", gap: "1rem" }}>
        {(["sm", "md", "lg", "xl", "full"] as const).map((s) => (
          <Button
            key={s}
            onClick={() => {
              setSize(s);
              setIsOpen(true);
            }}
          >
            Open {s}
          </Button>
        ))}
        <Modal
          isOpen={isOpen}
          onClose={() => setIsOpen(false)}
          title={`Modal ${size}`}
          size={size}
        >
          <p>This is a {size} modal.</p>
        </Modal>
      </div>
    );
  },
};
