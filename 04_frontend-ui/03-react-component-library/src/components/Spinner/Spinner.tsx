import React from "react";
import styles from "./Spinner.module.css";

export interface SpinnerProps {
  size?: "sm" | "md" | "lg";
  color?: string;
  label?: string;
}

export const Spinner: React.FC<SpinnerProps> = ({
  size = "md",
  color,
  label = "Loading...",
}) => {
  return (
    <div
      role="status"
      className={`${styles.spinner} ${styles[size]}`}
      style={{ color }}
      aria-live="polite"
    >
      <span className={styles.srOnly}>{label}</span>
    </div>
  );
};
