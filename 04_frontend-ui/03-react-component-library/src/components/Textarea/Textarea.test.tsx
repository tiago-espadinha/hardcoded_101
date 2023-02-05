import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { Textarea } from "./Textarea";

describe("Textarea", () => {
  it("renders correctly with label", () => {
    render(<Textarea label="Description" placeholder="Enter description" />);
    expect(screen.getByLabelText("Description")).toBeInTheDocument();
  });

  it("calls onChange when value changes", () => {
    const handleChange = vi.fn();
    render(<Textarea label="Description" onChange={handleChange} />);
    const textarea = screen.getByLabelText("Description");
    fireEvent.change(textarea, { target: { value: "test description" } });
    expect(handleChange).toHaveBeenCalledTimes(1);
  });

  it("shows error message and has correct role", () => {
    render(<Textarea label="Description" error="Too short" />);
    const errorMsg = screen.getByRole("alert");
    expect(errorMsg).toHaveTextContent("Too short");
  });

  it("shows character count when showCharCount and maxLength are provided", () => {
    render(
      <Textarea
        label="Description"
        maxLength={100}
        showCharCount
        value="Hello"
        onChange={() => {}}
      />,
    );
    expect(screen.getByText("5/100")).toBeInTheDocument();
  });

  it("is disabled when disabled prop is true", () => {
    render(<Textarea label="Description" disabled />);
    expect(screen.getByLabelText("Description")).toBeDisabled();
  });
});
