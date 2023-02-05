import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { Checkbox } from "./Checkbox";

describe("Checkbox", () => {
  it("renders correctly", () => {
    render(<Checkbox label="Click me" />);
    expect(screen.getByLabelText("Click me")).toBeInTheDocument();
  });

  it("calls onChange when clicked", () => {
    const handleChange = vi.fn();
    render(<Checkbox label="Click me" onChange={handleChange} />);
    fireEvent.click(screen.getByLabelText("Click me"));
    expect(handleChange).toHaveBeenCalledTimes(1);
  });

  it("is disabled when the disabled prop is true", () => {
    render(<Checkbox label="Click me" disabled />);
    expect(screen.getByLabelText("Click me")).toBeDisabled();
  });

  it("shows error state when error prop is provided", () => {
    render(<Checkbox label="Click me" error="Error message" />);
    expect(screen.getByRole("alert")).toBeInTheDocument();
  });
});
