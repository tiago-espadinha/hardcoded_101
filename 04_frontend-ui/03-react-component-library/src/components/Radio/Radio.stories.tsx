import React, { useState } from "react";
import type { Meta, StoryObj } from "@storybook/react";
import { Radio, RadioGroup } from "./Radio";

const meta: Meta<typeof RadioGroup> = {
  title: "Components/Radio",
  component: RadioGroup,
  tags: ["autodocs"],
};

export default meta;

export const Default = {
  render: () => {
    const [value, setValue] = useState("option1");
    return (
      <RadioGroup
        name="options"
        value={value}
        onChange={setValue}
        label="Choose an option"
      >
        <Radio value="option1" label="Option 1" />
        <Radio value="option2" label="Option 2" />
        <Radio value="option3" label="Option 3" />
      </RadioGroup>
    );
  },
};

export const WithDisabled = {
  render: () => {
    const [value, setValue] = useState("option1");
    return (
      <RadioGroup
        name="options-disabled"
        value={value}
        onChange={setValue}
        label="Choose an option"
      >
        <Radio value="option1" label="Option 1" />
        <Radio value="option2" label="Option 2" disabled />
        <Radio value="option3" label="Option 3" />
      </RadioGroup>
    );
  },
};

export const Horizontal = {
  render: () => {
    const [value, setValue] = useState("option1");
    return (
      <RadioGroup
        name="options-horizontal"
        value={value}
        onChange={setValue}
        label="Choose an option"
        style={{ flexDirection: "row", gap: "24px" }}
      >
        <Radio value="option1" label="Option 1" />
        <Radio value="option2" label="Option 2" />
        <Radio value="option3" label="Option 3" />
      </RadioGroup>
    );
  },
};
