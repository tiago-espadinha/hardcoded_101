import React from "react";
import styles from "./Spinner.module.css";

export interface SpinnerProps extends React.HTMLAttributes<HTMLDivElement> {
  size?: "sm" | "md" | "lg";
  color?: string;
  label?: string;
}

export const Spinner: React.FC<SpinnerProps> = ({
  size = "md",
  color,
  label = "Loading...",
  className,
  style,
  ...props
}) => {
  return (
    <div
      {...props}
      role="status"
      className={`${styles.spinner} ${styles[size]} ${className ?? ""}`}
      style={{ ...style, ...(color ? { color } : {}) }}
      aria-live="polite"
    >
      <span className={styles.srOnly}>{label}</span>
    </div>
  );
};
