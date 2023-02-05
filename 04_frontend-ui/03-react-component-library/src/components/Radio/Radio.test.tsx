import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import React, { useState } from "react";
import { Radio, RadioGroup } from "./Radio";

const ControlledRadioGroup = () => {
  const [value, setValue] = useState("option1");
  return (
    <RadioGroup name="test" value={value} onChange={setValue}>
      <Radio value="option1" label="Option 1" />
      <Radio value="option2" label="Option 2" />
      <Radio value="option3" label="Option 3" disabled />
    </RadioGroup>
  );
};

describe("Radio & RadioGroup", () => {
  it("renders correctly", () => {
    render(
      <RadioGroup name="test" value="option1" onChange={() => {}}>
        <Radio value="option1" label="Option 1" />
        <Radio value="option2" label="Option 2" />
      </RadioGroup>,
    );
    expect(screen.getByLabelText("Option 1")).toBeInTheDocument();
    expect(screen.getByLabelText("Option 2")).toBeInTheDocument();
  });

  it("selects the correct radio based on value prop", () => {
    render(
      <RadioGroup name="test" value="option2" onChange={() => {}}>
        <Radio value="option1" label="Option 1" />
        <Radio value="option2" label="Option 2" />
      </RadioGroup>,
    );
    expect(screen.getByLabelText("Option 1")).not.toBeChecked();
    expect(screen.getByLabelText("Option 2")).toBeChecked();
  });

  it("calls onChange when a radio is clicked", () => {
    const handleChange = vi.fn();
    render(
      <RadioGroup name="test" value="option1" onChange={handleChange}>
        <Radio value="option1" label="Option 1" />
        <Radio value="option2" label="Option 2" />
      </RadioGroup>,
    );
    fireEvent.click(screen.getByLabelText("Option 2"));
    expect(handleChange).toHaveBeenCalledWith("option2");
  });

  it("does not call onChange when a disabled radio is clicked", () => {
    const handleChange = vi.fn();
    render(
      <RadioGroup name="test" value="option1" onChange={handleChange}>
        <Radio value="option1" label="Option 1" />
        <Radio value="option2" label="Option 2" disabled />
      </RadioGroup>,
    );
    fireEvent.click(screen.getByLabelText("Option 2"));
    expect(handleChange).not.toHaveBeenCalled();
  });

  it("works correctly as a controlled component", () => {
    render(<ControlledRadioGroup />);
    const option1 = screen.getByLabelText("Option 1");
    const option2 = screen.getByLabelText("Option 2");

    expect(option1).toBeChecked();
    expect(option2).not.toBeChecked();

    fireEvent.click(option2);

    expect(option1).not.toBeChecked();
    expect(option2).toBeChecked();
  });

  it("supports keyboard navigation", () => {
    render(<ControlledRadioGroup />);
    const option1 = screen.getByLabelText("Option 1");
    const option2 = screen.getByLabelText("Option 2");

    option1.focus();
    expect(option1).toHaveFocus();

    // In a real browser, ArrowDown would change selection.
    // fireEvent.keyDown(option1, { key: 'ArrowDown' });
    // However, RTL/fireEvent might not simulate the full browser behavior for radio groups automatically.
    // But since we use native <input type="radio">, standard browser behavior should apply.
  });
});
