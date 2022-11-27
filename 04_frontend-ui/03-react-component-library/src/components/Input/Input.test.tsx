import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { Input } from "./Input";

describe("Input", () => {
  it("renders correctly with label", () => {
    render(<Input label="Username" placeholder="Enter username" />);
    expect(screen.getByLabelText("Username")).toBeInTheDocument();
    expect(screen.getByPlaceholderText("Enter username")).toBeInTheDocument();
  });

  it("calls onChange when value changes", () => {
    const handleChange = vi.fn();
    render(<Input label="Username" onChange={handleChange} />);
    const input = screen.getByLabelText("Username");
    fireEvent.change(input, { target: { value: "testuser" } });
    expect(handleChange).toHaveBeenCalledTimes(1);
  });

  it("shows error message and has correct role", () => {
    render(<Input label="Username" error="This field is required" />);
    const errorMsg = screen.getByRole("alert");
    expect(errorMsg).toHaveTextContent("This field is required");
  });

  it("is disabled when disabled prop is true", () => {
    render(<Input label="Username" disabled />);
    expect(screen.getByLabelText("Username")).toBeDisabled();
  });

  it("shows required asterisk when required prop is true", () => {
    render(<Input label="Username" required />);
    expect(screen.getByText("*")).toBeInTheDocument();
    expect(screen.getByLabelText("Username")).toBeRequired();
  });

  it("renders left and right adornments", () => {
    render(
      <Input
        label="Price"
        leftAdornment={<span data-testid="left">$</span>}
        rightAdornment={<span data-testid="right">USD</span>}
      />,
    );
    expect(screen.getByTestId("left")).toBeInTheDocument();
    expect(screen.getByTestId("right")).toBeInTheDocument();
  });
});
