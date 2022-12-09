import React, { useId } from "react";
import styles from "./Toggle.module.css";

export interface ToggleProps {
  checked: boolean;
  onChange: (checked: boolean) => void;
  label?: string;
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
  className?: string;
  id?: string;
}

export const Toggle: React.FC<ToggleProps> = ({
  checked,
  onChange,
  label,
  size = "md",
  disabled,
  className,
  id,
}) => {
  const generatedId = useId();
  const toggleId = id || generatedId;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!disabled) {
      onChange(e.target.checked);
    }
  };

  const containerClasses = [
    styles.container,
    styles[size],
    disabled ? styles.disabled : "",
    className,
  ]
    .filter(Boolean)
    .join(" ");

  return (
    <label htmlFor={toggleId} className={containerClasses}>
      <div className={styles.toggleWrapper}>
        <input
          type="checkbox"
          id={toggleId}
          checked={checked}
          onChange={handleChange}
          disabled={disabled}
          className={styles.input}
          role="switch"
          aria-checked={checked}
        />
        <div className={styles.track}>
          <div className={styles.thumb} />
        </div>
      </div>
      {label && <span className={styles.labelText}>{label}</span>}
    </label>
  );
};
