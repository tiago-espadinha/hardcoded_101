import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { Badge } from "./Badge";

describe("Badge", () => {
  it("renders children correctly", () => {
    render(<Badge>Test Badge</Badge>);
    expect(screen.getByText("Test Badge")).toBeInTheDocument();
  });

  it("applies the correct variant class", () => {
    const { container } = render(<Badge variant="success">Success</Badge>);
    expect(container.firstChild).toHaveClass(/success/);
  });

  it("applies the correct size class", () => {
    const { container } = render(<Badge size="sm">Small</Badge>);
    expect(container.firstChild).toHaveClass(/sm/);
  });

  it("renders as a dot when dot prop is true", () => {
    render(<Badge dot>Content</Badge>);
    expect(screen.queryByText("Content")).not.toBeInTheDocument();
    // It should have the dot class
  });

  it("has dot class when dot prop is true", () => {
    const { container } = render(<Badge dot />);
    expect(container.firstChild).toHaveClass(/dot/);
  });
});
