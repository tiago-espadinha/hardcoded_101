import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { Spinner } from "./Spinner";

describe("Spinner", () => {
  it("renders with default props", () => {
    render(<Spinner />);
    const spinner = screen.getByRole("status");
    expect(spinner).toBeInTheDocument();
    expect(screen.getByText("Loading...")).toBeInTheDocument();
  });

  it("renders with custom label", () => {
    render(<Spinner label="Custom Loading" />);
    expect(screen.getByText("Custom Loading")).toBeInTheDocument();
  });

  it("applies the correct size class", () => {
    const { container } = render(<Spinner size="lg" />);
    const spinner = container.firstChild;
    // We check if it contains a class that ends with 'lg' due to CSS Modules naming
    expect(spinner).toHaveClass(/lg/);
  });

  it("applies custom color via style", () => {
    const { container } = render(<Spinner color="red" />);
    const spinner = container.firstChild as HTMLElement;
    expect(spinner.style.color).toBe("red");
  });

  it("is accessible", () => {
    render(<Spinner label="Loading data" />);
    const spinner = screen.getByRole("status");
    expect(spinner).toHaveAttribute("aria-live", "polite");
    expect(screen.getByText("Loading data")).toHaveClass(/srOnly/);
  });
});
