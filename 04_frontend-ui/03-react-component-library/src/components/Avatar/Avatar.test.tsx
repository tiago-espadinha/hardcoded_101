import { render, screen } from "@testing-library/react";
import { describe, it, expect } from "vitest";
import { Avatar } from "./Avatar";

describe("Avatar", () => {
  it("renders image when src is provided", () => {
    render(<Avatar src="test.jpg" alt="User" />);
    const img = screen.getByAltText("User");
    expect(img).toBeInTheDocument();
    expect(img).toHaveAttribute("src", "test.jpg");
  });

  it("renders fallback when src fails to load", () => {
    render(<Avatar src="error.jpg" fallback="JD" />);
    // Initial render might have img, but we simulate error
    const img = screen.getByRole("img");
    fireEvent.error(img);
    expect(screen.getByText("JD")).toBeInTheDocument();
  });

  it("renders fallback if no src provided", () => {
    render(<Avatar fallback="JD" />);
    expect(screen.getByText("JD")).toBeInTheDocument();
  });
});

import { fireEvent } from "@testing-library/react";
