import React, { useState, useRef, useEffect, useCallback } from "react";
import styles from "./Dropdown.module.css";

export interface DropdownItem {
  label: string;
  onClick?: () => void;
  icon?: React.ReactNode;
  disabled?: boolean;
  divider?: boolean;
}

export interface DropdownProps {
  trigger: React.ReactNode;
  items: DropdownItem[];
  className?: string;
}

export const Dropdown: React.FC<DropdownProps> = ({
  trigger,
  items,
  className,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const [highlightedIndex, setHighlightedIndex] = useState(-1);
  const containerRef = useRef<HTMLDivElement>(null);
  const triggerRef = useRef<HTMLDivElement>(null);

  const toggleDropdown = () => setIsOpen((prev) => !prev);

  const closeDropdown = useCallback(() => {
    setIsOpen(false);
    setHighlightedIndex(-1);
  }, []);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        containerRef.current &&
        !containerRef.current.contains(event.target as Node)
      ) {
        closeDropdown();
      }
    };

    if (isOpen) {
      document.addEventListener("mousedown", handleClickOutside);
    }
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [isOpen, closeDropdown]);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Escape") {
      closeDropdown();
      triggerRef.current?.querySelector("button")?.focus();
      return;
    }

    if (!isOpen) {
      if (
        e.key === "ArrowDown" ||
        e.key === "ArrowUp" ||
        e.key === "Enter" ||
        e.key === " "
      ) {
        e.preventDefault();
        setIsOpen(true);
      }
      return;
    }

    const focusableItems = items.filter(
      (item) => !item.divider && !item.disabled,
    );
    const focusableIndices = items
      .map((item, index) => (!item.divider && !item.disabled ? index : -1))
      .filter((index) => index !== -1);

    const currentFocusableIndex = focusableIndices.indexOf(highlightedIndex);

    switch (e.key) {
      case "ArrowDown":
        e.preventDefault();
        const nextIndex = (currentFocusableIndex + 1) % focusableIndices.length;
        setHighlightedIndex(focusableIndices[nextIndex]);
        break;
      case "ArrowUp":
        e.preventDefault();
        const prevIndex =
          (currentFocusableIndex - 1 + focusableIndices.length) %
          focusableIndices.length;
        setHighlightedIndex(focusableIndices[prevIndex]);
        break;
      case "Enter":
      case " ":
        e.preventDefault();
        if (highlightedIndex !== -1) {
          const item = items[highlightedIndex];
          if (item.onClick) {
            item.onClick();
            closeDropdown();
          }
        }
        break;
      case "Tab":
        closeDropdown();
        break;
    }
  };

  const handleItemClick = (item: DropdownItem) => {
    if (item.disabled || item.divider) return;
    if (item.onClick) {
      item.onClick();
    }
    closeDropdown();
  };

  return (
    <div
      className={[styles.container, className].filter(Boolean).join(" ")}
      ref={containerRef}
      onKeyDown={handleKeyDown}
    >
      <div
        ref={triggerRef}
        onClick={toggleDropdown}
        className={styles.triggerWrapper}
      >
        {trigger}
      </div>

      {isOpen && (
        <ul className={styles.menu} role="menu">
          {items.map((item, index) => {
            if (item.divider) {
              return (
                <li
                  key={`divider-${index}`}
                  className={styles.divider}
                  role="separator"
                />
              );
            }

            const itemClasses = [
              styles.item,
              item.disabled ? styles.disabled : "",
              highlightedIndex === index ? styles.highlighted : "",
            ]
              .filter(Boolean)
              .join(" ");

            return (
              <li key={`item-${index}`} role="none">
                <button
                  type="button"
                  className={itemClasses}
                  onClick={() => handleItemClick(item)}
                  disabled={item.disabled}
                  role="menuitem"
                  onMouseEnter={() =>
                    !item.disabled && setHighlightedIndex(index)
                  }
                >
                  {item.icon && (
                    <span className={styles.icon}>{item.icon}</span>
                  )}
                  <span>{item.label}</span>
                </button>
              </li>
            );
          })}
        </ul>
      )}
    </div>
  );
};
