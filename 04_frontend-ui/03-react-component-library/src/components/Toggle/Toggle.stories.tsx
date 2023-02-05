import React, { useState } from "react";
import type { Meta, StoryObj } from "@storybook/react";
import { Toggle } from "./Toggle";

const meta: Meta<typeof Toggle> = {
  title: "Components/Toggle",
  component: Toggle,
  tags: ["autodocs"],
};

export default meta;

export const Default = {
  render: () => {
    const [checked, setChecked] = useState(false);
    return (
      <Toggle
        checked={checked}
        onChange={setChecked}
        label="Enable notifications"
      />
    );
  },
};

export const Sizes = {
  render: () => {
    const [checked, setChecked] = useState(true);
    return (
      <div style={{ display: "flex", flexDirection: "column", gap: "16px" }}>
        <Toggle
          checked={checked}
          onChange={setChecked}
          size="sm"
          label="Small Toggle"
        />
        <Toggle
          checked={checked}
          onChange={setChecked}
          size="md"
          label="Medium Toggle"
        />
        <Toggle
          checked={checked}
          onChange={setChecked}
          size="lg"
          label="Large Toggle"
        />
      </div>
    );
  },
};

export const Disabled = {
  render: () => {
    return (
      <div style={{ display: "flex", flexDirection: "column", gap: "16px" }}>
        <Toggle
          checked={false}
          onChange={() => {}}
          label="Disabled Off"
          disabled
        />
        <Toggle
          checked={true}
          onChange={() => {}}
          label="Disabled On"
          disabled
        />
      </div>
    );
  },
};
