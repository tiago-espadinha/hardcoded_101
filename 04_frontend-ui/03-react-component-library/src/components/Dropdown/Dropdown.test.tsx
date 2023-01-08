import { render, screen, fireEvent } from "@testing-library/react";
import { describe, it, expect, vi } from "vitest";
import { Dropdown } from "./Dropdown";

describe("Dropdown", () => {
  const items = [
    { label: "Item 1", onClick: vi.fn() },
    { label: "Item 2", onClick: vi.fn() },
    { divider: true },
    { label: "Disabled Item", disabled: true, onClick: vi.fn() },
  ];

  it("toggles menu when trigger is clicked", () => {
    render(<Dropdown trigger={<button>Open</button>} items={items} />);

    expect(screen.queryByRole("menu")).not.toBeInTheDocument();

    fireEvent.click(screen.getByText("Open"));
    expect(screen.getByRole("menu")).toBeInTheDocument();

    fireEvent.click(screen.getByText("Open"));
    expect(screen.queryByRole("menu")).not.toBeInTheDocument();
  });

  it("calls onClick and closes menu when item is clicked", () => {
    render(<Dropdown trigger={<button>Open</button>} items={items} />);

    fireEvent.click(screen.getByText("Open"));
    fireEvent.click(screen.getByText("Item 1"));

    expect(items[0].onClick).toHaveBeenCalledTimes(1);
    expect(screen.queryByRole("menu")).not.toBeInTheDocument();
  });

  it("does not call onClick when disabled item is clicked", () => {
    render(<Dropdown trigger={<button>Open</button>} items={items} />);

    fireEvent.click(screen.getByText("Open"));
    fireEvent.click(screen.getByText("Disabled Item"));

    expect(items[3].onClick).not.toHaveBeenCalled();
    expect(screen.getByRole("menu")).toBeInTheDocument();
  });

  it("closes menu on Escape key", () => {
    render(<Dropdown trigger={<button>Open</button>} items={items} />);

    fireEvent.click(screen.getByText("Open"));
    expect(screen.getByRole("menu")).toBeInTheDocument();

    fireEvent.keyDown(screen.getByRole("menu"), { key: "Escape" });
    expect(screen.queryByRole("menu")).not.toBeInTheDocument();
  });

  it("navigates with keyboard", () => {
    render(<Dropdown trigger={<button>Open</button>} items={items} />);

    fireEvent.click(screen.getByText("Open"));
    const menu = screen.getByRole("menu");

    fireEvent.keyDown(menu, { key: "ArrowDown" });
    // Item 1 is highlighted
    expect(screen.getByText("Item 1").closest("button")).toHaveClass(
      /highlighted/,
    );

    fireEvent.keyDown(menu, { key: "ArrowDown" });
    // Item 2 is highlighted
    expect(screen.getByText("Item 2").closest("button")).toHaveClass(
      /highlighted/,
    );

    fireEvent.keyDown(menu, { key: "ArrowDown" });
    // It should skip the divider and disabled item
    // Actually my implementation cycles back if it's at the end of focusable.
    // Let's check my logic: it filters focusableIndices.
    // Item 1 (0), Item 2 (1). Focusable: [0, 1].
    // After index 1, it should go back to 0.
    expect(screen.getByText("Item 1").closest("button")).toHaveClass(
      /highlighted/,
    );

    fireEvent.keyDown(menu, { key: "Enter" });
    expect(items[0].onClick).toHaveBeenCalled();
  });
});
