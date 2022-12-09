import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import React, { useState } from "react";
import { Toggle } from "./Toggle";

const ControlledToggle = ({ initialChecked = false, ...props }) => {
  const [checked, setChecked] = useState(initialChecked);
  return <Toggle checked={checked} onChange={setChecked} {...props} />;
};

describe("Toggle", () => {
  it("renders correctly", () => {
    render(
      <Toggle
        checked={false}
        onChange={() => {}}
        label="Enable notifications"
      />,
    );
    expect(screen.getByLabelText("Enable notifications")).toBeInTheDocument();
    expect(screen.getByRole("switch")).toBeInTheDocument();
  });

  it("reflects checked state", () => {
    const { rerender } = render(
      <Toggle checked={true} onChange={() => {}} label="Toggle" />,
    );
    expect(screen.getByRole("switch")).toBeChecked();
    expect(screen.getByRole("switch")).toHaveAttribute("aria-checked", "true");

    rerender(<Toggle checked={false} onChange={() => {}} label="Toggle" />);
    expect(screen.getByRole("switch")).not.toBeChecked();
    expect(screen.getByRole("switch")).toHaveAttribute("aria-checked", "false");
  });

  it("calls onChange when clicked", () => {
    const handleChange = vi.fn();
    render(<Toggle checked={false} onChange={handleChange} label="Toggle" />);
    fireEvent.click(screen.getByRole("switch"));
    expect(handleChange).toHaveBeenCalledWith(true);
  });

  it("does not call onChange when disabled", () => {
    const handleChange = vi.fn();
    render(
      <Toggle
        checked={false}
        onChange={handleChange}
        label="Toggle"
        disabled
      />,
    );
    fireEvent.click(screen.getByRole("switch"));
    expect(handleChange).not.toHaveBeenCalled();
    expect(screen.getByRole("switch")).toBeDisabled();
  });

  it("works correctly as a controlled component", () => {
    render(<ControlledToggle label="Controlled" />);
    const toggle = screen.getByRole("switch");

    expect(toggle).not.toBeChecked();
    fireEvent.click(toggle);
    expect(toggle).toBeChecked();
    fireEvent.click(toggle);
    expect(toggle).not.toBeChecked();
  });
});
